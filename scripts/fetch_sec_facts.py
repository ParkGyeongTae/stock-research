#!/usr/bin/env python3
"""04_metrics.md A절(연간)·B절(분기)를 채울 재무 수치를 SEC XBRL에서 뽑는다.

    uv run python scripts/fetch_sec_facts.py EQT                    # 연간 3개년
    uv run python scripts/fetch_sec_facts.py EQT --emit all         # 연간 + 분기
    uv run python scripts/fetch_sec_facts.py EQT --quarters 6 --emit quarterly
    uv run python scripts/fetch_sec_facts.py 0000033213 --emit sources   # 셀별 원공시
    uv run python scripts/fetch_sec_facts.py EQT --emit all -o $S/facts.md

왜 스크립트로 두는가: 10-K HTML을 내려받아 텍스트로 바꾼 뒤 grep으로 훑는 방식은
같은 값을 회사마다 다른 표에서 다르게 읽어오고, 무엇보다 **한 회사에 수십 번의
도구 호출**이 든다. companyfacts API는 회사가 XBRL로 태깅해 제출한 값 그 자체이므로
한 번의 호출로 끝나고, 각 값이 어느 태그·어느 공시에서 왔는지가 같이 온다.

정의 혼동을 스크립트 단에서 막는다 — 이 저장소가 반복해서 틀리는 지점들:

- **순이익**: `NetIncomeLoss`(지배주주 귀속)와 `ProfitLoss`(연결, NCI 포함)를 둘 다 뽑는다.
  비지배지분이 큰 회사(예: 미드스트림을 붙인 E&P)에서 둘은 크게 벌어진다.
- **자기자본**: `StockholdersEquity`(지배주주 귀속)와
  `...IncludingPortionAttributableToNoncontrollingInterest`(자본총계)를 둘 다 뽑는다.
- **부채**: `Liabilities`(부채총계)와 이자부 차입금(장기+유동성 장기차입금+단기차입금)을
  **별도 행으로** 뽑는다. 둘을 섞으면 D/E·순부채가 전부 틀어진다.
- 여기서 나오는 값은 전부 **GAAP**이다. Adjusted EBITDA·Adjusted EPS 같은 Non-GAAP은
  XBRL에 없다 — 회사 실적발표(8-K Ex-99)에서 따로 확인하고 라벨을 붙여야 한다.

한계(문서에 그대로 옮기지 말고 확인할 것):
- 회사가 태깅하지 않은 항목은 `—`로 나온다. 없는 게 아니라 태그가 다를 수 있다.
- Q4는 대개 별도 공시되지 않아 `FY − (Q1+Q2+Q3)`로 계산하며 `ᵈ`로 표시한다. 주당 지표·주식수는
  분기별 주식수가 달라 이 뺄셈이 성립하지 않으므로 파생하지 않고 비워 둔다.
- 현금흐름표 항목은 10-Q에서 연초 누적(YTD)으로 태깅되어 분기 표에선 Q1만 잡힌다.
- 소급 수정(restatement)이 있으면 **가장 최근 제출본**의 값을 쓴다. 그 셀에는 `*`가 붙고
  `--emit sources`에서 어느 공시인지 볼 수 있다.

의존성 없음(표준 라이브러리만). SEC는 User-Agent에 연락처를 요구한다 —
`SEC_USER_AGENT` 환경변수로 바꿀 수 있다.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date

UA = os.environ.get("SEC_USER_AGENT", "stock-research pgt0409@gmail.com")
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

# ── 뽑을 항목: (라벨, 종류, [태그 후보 — 앞이 우선]) ────────────────────────
#   종류 duration = 기간 합계(매출·현금흐름), instant = 시점 잔액(자산·부채)
#   태그를 바꾸면 이미 만든 04_metrics.md와 정의가 어긋나므로 바꿀 땐 사유를 남길 것.
ITEMS: list[tuple[str, str, list[str]]] = [
    ("매출액", "duration", [
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "RevenueFromContractWithCustomerIncludingAssessedTax",
        "Revenues", "SalesRevenueNet"]),
    ("영업이익", "duration", ["OperatingIncomeLoss"]),
    ("세전이익", "duration", [
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]),
    ("순이익 (지배주주 귀속)", "duration", ["NetIncomeLoss"]),
    ("순이익 (연결·NCI 포함)", "duration", ["ProfitLoss"]),
    ("EPS 희석 (GAAP)", "duration", ["EarningsPerShareDiluted", "EarningsPerShareBasicAndDiluted"]),
    ("EPS 기본 (GAAP)", "duration", ["EarningsPerShareBasic", "EarningsPerShareBasicAndDiluted"]),
    ("희석 주식수 (가중평균)", "duration", [
        "WeightedAverageNumberOfDilutedSharesOutstanding",
        "WeightedAverageNumberOfDilutedSharesOutstandingAdjustment"]),
    ("자산총계", "instant", ["Assets"]),
    ("부채총계", "instant", ["Liabilities"]),
    ("장기차입금 (비유동)", "instant", ["LongTermDebtNoncurrent", "LongTermDebt"]),
    ("장기차입금 유동성 대체", "instant", ["LongTermDebtCurrent"]),
    ("단기차입금", "instant", ["ShortTermBorrowings", "OtherShortTermBorrowings"]),
    ("현금및현금성자산", "instant", [
        "CashAndCashEquivalentsAtCarryingValue",
        "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]),
    ("자기자본 (지배주주 귀속)", "instant", ["StockholdersEquity"]),
    ("자본총계 (NCI 포함)", "instant", [
        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]),
    ("비지배지분 (NCI)", "instant", ["MinorityInterest"]),
    ("영업활동 현금흐름 (CFO)", "duration", [
        "NetCashProvidedByUsedInOperatingActivities",
        "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]),
    ("자본적지출 (CapEx)", "duration", [
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PaymentsToAcquireProductiveAssets", "PaymentsToExploreAndDevelopOilAndGasProperties"]),
    ("감가상각비 (D&A)", "duration", [
        "DepreciationDepletionAndAmortization",
        "DepreciationAmortizationAndAccretionNet", "DepreciationAndAmortization"]),
    ("주식보상비용 (SBC)", "duration", ["ShareBasedCompensation"]),
    ("배당 (주당, 선언)", "duration", [
        "CommonStockDividendsPerShareDeclared", "CommonStockDividendsPerShareCashPaid"]),
    ("배당 지급액", "duration", [
        "PaymentsOfDividendsCommonStock", "PaymentsOfDividends"]),
    ("자사주 매입액", "duration", ["PaymentsForRepurchaseOfCommonStock"]),
]

# 이자부 차입금 = 아래 행들의 합 (부채총계와 혼동 금지)
DEBT_ROWS = ("장기차입금 (비유동)", "장기차입금 유동성 대체", "단기차입금")


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept-Encoding": "gzip, deflate", "Host": url.split("/")[2]})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                import gzip
                raw = gzip.decompress(raw)
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        sys.exit(f"SEC 응답 {e.code}: {url}\n  User-Agent를 SEC_USER_AGENT로 지정했는지 확인.")
    except urllib.error.URLError as e:
        sys.exit(f"SEC 접속 실패: {e.reason}")


def resolve_cik(arg: str) -> tuple[str, str]:
    if arg.isdigit():
        return arg.zfill(10), arg
    data = fetch(TICKERS_URL)
    for row in data.values():
        if row["ticker"].upper() == arg.upper():
            return str(row["cik_str"]).zfill(10), row["title"]
    sys.exit(f"티커 '{arg}'를 SEC 목록에서 못 찾았습니다. CIK를 직접 넣어 보세요.")


def pick(facts: dict, tags: list[str], kind: str, periods: list) -> tuple[str, dict, list]:
    """태그 후보를 순서대로 시도해 값이 가장 많이 채워지는 것을 고른다."""
    best: tuple[int, str, dict, list] = (0, "", {}, [])
    for ns in ("us-gaap", "ifrs-full", "dei"):
        for tag in tags:
            node = facts.get(ns, {}).get(tag)
            if not node:
                continue
            for unit, entries in node["units"].items():
                got = match(entries, kind, periods)
                filled = sum(1 for v in got.values() if v is not None)
                if filled > best[0]:
                    best = (filled, f"{ns}:{tag} ({unit})", got, entries)
    return best[1], best[2], best[3]


def match(entries: list[dict], kind: str, periods: list) -> dict:
    """기간별로 조건에 맞는 항목 중 가장 최근에 제출된 것을 고른다."""
    out: dict = {p[0]: None for p in periods}
    for label, want_end, lo, hi in periods:
        cands = []
        for e in entries:
            if e.get("end") != want_end:
                continue
            if kind == "instant":
                if e.get("start"):
                    continue
            else:
                if not e.get("start"):
                    continue
                days = (date.fromisoformat(e["end"]) - date.fromisoformat(e["start"])).days
                if not lo <= days <= hi:
                    continue
            cands.append(e)
        if cands:
            latest = max(cands, key=lambda e: (e.get("filed", ""), e.get("accn", "")))
            first = min(cands, key=lambda e: (e.get("filed", ""), e.get("accn", "")))
            # 값 자체가 바뀐 경우만 소급 수정으로 본다 — 최신 10-K가 비교연도를
            # 다시 싣는 것은 수정이 아니므로 표시하지 않는다.
            latest = dict(latest, restated=(first["val"] != latest["val"]),
                          orig=first["val"], orig_accn=first.get("accn", ""))
            out[label] = latest
    return out


def fy_ends(facts: dict, n: int) -> list[str]:
    """10-K로 보고된 회계연도 종료일을 최신순으로."""
    ends = set()
    for tag in ("Assets", "Liabilities", "StockholdersEquity"):
        for entries in facts.get("us-gaap", {}).get(tag, {}).get("units", {}).values():
            for e in entries:
                if e.get("form", "").startswith("10-K") and e.get("fp") == "FY" and not e.get("start"):
                    ends.add(e["end"])
    return sorted(ends, reverse=True)[:n]


def q_ends(facts: dict, n: int) -> list[str]:
    ends = set()
    for tag in ("Assets", "Liabilities", "StockholdersEquity"):
        for entries in facts.get("us-gaap", {}).get(tag, {}).get("units", {}).values():
            for e in entries:
                if e.get("form", "").startswith(("10-Q", "10-K")) and not e.get("start"):
                    ends.add(e["end"])
    return sorted(ends, reverse=True)[:n]


def fmt(e: dict | None, unit_hint: str) -> str:
    if e is None:
        return "—"
    v = e["val"]
    if "USD/shares" in unit_hint:
        s = f"{v:,.2f}"
    elif "shares" in unit_hint:
        s = f"{v/1e6:,.1f}"
    elif abs(v) >= 1e6:
        s = f"{v/1e6:,.0f}"
    else:
        s = f"{v:,.0f}"
    return s


def derive_q4(entries: list, got: dict, periods: list, tag: str, fy_set: set) -> None:
    """Q4는 대개 별도 공시되지 않는다 — FY − (Q1+Q2+Q3)로 채우고 (파생)으로 표시한다.
    주당 지표·주식수는 분기별 주식수가 달라 이 뺄셈이 성립하지 않으므로 제외한다."""
    if "/shares" in tag or "(shares)" in tag:
        return
    for i, (label, end, *_) in enumerate(periods):
        if got.get(label) is not None or end not in fy_set or i < 3:
            continue
        fy = match(entries, "duration", [(label, end, 350, 380)]).get(label)
        prior = [got.get(periods[j][0]) for j in (i - 3, i - 2, i - 1)]
        if fy is None or any(p is None for p in prior):
            continue
        got[label] = {"val": fy["val"] - sum(p["val"] for p in prior),
                      "derived": True, "form": fy.get("form", ""),
                      "filed": fy.get("filed", ""), "accn": fy.get("accn", "")}


def build(facts: dict, periods: list, fy_set: set | None = None) -> tuple[list, dict]:
    rows, srcs = [], {}
    for label, kind, tags in ITEMS:
        tag, got, entries = pick(facts, tags, kind, periods)
        if fy_set and kind == "duration":
            derive_q4(entries, got, periods, tag, fy_set)
        rows.append((label, tag, got))
        srcs[label] = got
    # 이자부 차입금 합계 행을 파생으로 추가
    idx = {r[0]: r for r in rows}
    total = {}
    for p in periods:
        s, any_v = 0.0, False
        for name in DEBT_ROWS:
            e = idx[name][2].get(p[0])
            if e:
                s += e["val"]; any_v = True
        total[p[0]] = {"val": s, "derived": True} if any_v else None
    rows.append(("**이자부 차입금 (합계)**", "위 3개 행의 합 (파생)", total))
    return rows, srcs


def render(title: str, rows: list, periods: list) -> list[str]:
    heads = [p[0] for p in periods]
    out = [f"### {title}", "",
           "단위: 백만 USD (EPS·DPS는 USD, 주식수는 백만 주) · 전부 **GAAP**",
           "",
           "| 항목 | XBRL 태그 | " + " | ".join(heads) + " |",
           "|---|---|" + "---|" * len(heads)]
    for label, tag, got in rows:
        cells = []
        for h in heads:
            e = got.get(h)
            mark = "ᵈ" if e and e.get("derived") else ("*" if e and e.get("restated") else "")
            cells.append(fmt(e, tag) + mark)
        out.append(f"| {label} | `{tag or '—'}` | " + " | ".join(cells) + " |")
    out += ["", "`*` = **최초 공시 이후 값이 바뀐 항목**(소급 수정) — 여기 쓴 값은 최신 제출본이고 "
                "최초값은 `--emit sources`에 있다. `—` = 회사가 해당 태그로 태깅하지 않음"
                "(없다는 뜻이 아니라 태그가 다를 수 있음). "
                "`ᵈ` = 파생값(Q4 = FY − Q1·Q2·Q3, 또는 이자부 차입금 합계) — 회사가 그렇게 "
                "공시한 것이 아니므로 인용할 땐 파생임을 밝힐 것.", ""]
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="SEC XBRL companyfacts에서 04_metrics.md용 GAAP 수치 추출")
    ap.add_argument("ticker", help="티커(EQT) 또는 CIK(0000033213)")
    ap.add_argument("--emit", choices=["annual", "quarterly", "all", "sources"], default="annual")
    ap.add_argument("--years", type=int, default=3)
    ap.add_argument("--quarters", type=int, default=6)
    ap.add_argument("-o", "--out", help="파일로 저장(대화로 통과시키지 말 것)")
    a = ap.parse_args()

    cik, name = resolve_cik(a.ticker)
    facts = fetch(FACTS_URL.format(cik=cik))
    F = facts["facts"]

    lines = [f"# {facts.get('entityName', name)} — SEC XBRL companyfacts (CIK {cik})", "",
             f"출처: `https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json` "
             f"(회사가 XBRL로 태깅해 제출한 원공시 값) · 조회일 {date.today()}", ""]

    ann_periods = [(e[:4], e, 350, 380) for e in fy_ends(F, a.years)][::-1]
    qtr_periods = [(e, e, 80, 100) for e in q_ends(F, a.quarters)][::-1]

    if a.emit in ("annual", "all", "sources"):
        rows, _ = build(F, ann_periods)
        lines += render(f"A. 연간 (최근 {len(ann_periods)}개 회계연도)", rows, ann_periods)
    fy_set = set(fy_ends(F, a.years + 2))
    if a.emit in ("quarterly", "all", "sources"):
        rows, _ = build(F, qtr_periods, fy_set)
        lines += render(f"B. 분기 (최근 {len(qtr_periods)}분기)", rows, qtr_periods)

    if a.emit == "sources":
        lines += ["### 셀별 원공시", "",
                  "| 기간 | 항목 | form | 제출일 | accession | 최초값(다를 때만) |",
                  "|---|---|---|---|---|---|"]
        for periods, fs in ((ann_periods, None), (qtr_periods, fy_set)):
            rows, _ = build(F, periods, fs)
            for label, tag, got in rows:
                for p in periods:
                    e = got.get(p[0])
                    if e and e.get("accn"):
                        orig = f"{e['orig']:,.0f} (`{e['orig_accn']}`)" if e.get("restated") else ""
                        lines.append(f"| {p[0]} | {label} | {e.get('form','')} | "
                                     f"{e.get('filed','')} | {e['accn']} | {orig} |")
        lines.append("")

    lines += ["---", "",
              "**여기 없는 것 — 따로 확인해야 함**: Adjusted EBITDA·Adjusted EPS 등 Non-GAAP "
              "(8-K Ex-99 실적발표), 사업 고유 지표(생산량·실현가격·매장량 등, 10-K 본문/IR), "
              "종가·시가총액·베타·컨센서스(XBRL 아님), 가이던스.", "",
              "**분기 표의 빈칸**: 현금흐름표 항목(CFO·CapEx·SBC·배당지급·자사주매입)은 10-Q에서 "
              "분기가 아니라 **연초 누적(YTD)**으로 태깅되므로 Q1만 잡힌다. 분기 값이 필요하면 "
              "누적값끼리 빼야 하고, 그건 회사 공시가 아닌 파생이다. 04_metrics.md B절은 "
              "손익계산서 항목만 요구하므로 대개 문제되지 않는다.", ""]

    text = "\n".join(lines)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"저장: {a.out} ({len(text):,}자, {len(lines)}줄)")
    else:
        print(text)


if __name__ == "__main__":
    main()
