#!/usr/bin/env python3
"""09_technical.md 용 일봉 캔들차트(SVG)·지지/저항 레벨 생성기.

`docs/meta/.template/company/09_technical.md`가 요구하는 기계적 산출물
(캔들 SVG 블록, §2 레벨 표, §4 방법론 수치)을 만든다. 서술·판단은 만들지 않는다.

    uv run python scripts/gen_technical_chart.py SNPS
    uv run python scripts/gen_technical_chart.py SNPS --event 2025-09-10:"실적발표 갭다운" \
        --ref-line 626.24:"52주 최고" --force-level 366 --close-on 2026-08-13

왜 스크립트로 두는가: 좌표 매핑·스윙 탐지·클러스터링 파라미터를 회사마다 다시
구현하면 값이 조용히 달라져 회사 간 차트 비교가 깨진다. 아래 상수가 그 단일
출처이며, **바꾸면 이미 만든 문서와 어긋나므로** 바꿀 땐 기존 09_technical.md를
전부 재생성하고 각 문서의 §4에 변경된 파라미터를 남길 것.

의존성 없음(표준 라이브러리만). 원자료는 저장소에 커밋하지 않는다.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone

# ── 파라미터: 모든 회사가 공유하는 단일 출처 (임의 변경 금지) ──────────────
SWING_WINDOW = 5  # 전후 N거래일 (총 2N+1 창) 내 최고/최저면 스윙 포인트
CLUSTER_TOL = 0.025  # 스윙 포인트를 묶는 가격 허용오차 (±2.5%)
MIN_TOUCHES = 2  # 선으로 그릴 최소 터치 횟수
LEVELS_PER_SIDE = 3  # 현재가 위/아래로 각각 최대 몇 개까지 표시할지
PAD_RATIO = 0.03  # y축 위아래 여백 = (고가−저가) × 이 비율
MAX_GRIDLINES = 8  # 가로 그리드 최대 개수

# ── 캔버스 좌표계 (viewBox 0 0 1200 680) ────────────────────────────────
VB_W, VB_H = 1200, 680
X_LEFT, X_RIGHT = 60.0, 1052.0  # 플롯 영역 좌우
Y_TOP, Y_BOTTOM = 56.0, 626.0  # 플롯 영역 상하
BODY_RATIO = 0.62  # 캔들 몸통 폭 = 캔들 간격 × 이 비율
BODY_W_MIN, BODY_W_MAX = 1.6, 6.0
BODY_H_MIN = 1.0  # 시가=종가일 때도 최소 이 높이로 그린다
LABEL_X = X_RIGHT + 6  # 우측 레벨 라벨 x

NICE = (1.0, 2.0, 2.5, 5.0)  # 눈금 단위로 쓸 "깔끔한" 수


@dataclass(frozen=True)
class Bar:
    d: date
    o: float
    h: float
    lo: float
    c: float
    v: int


@dataclass
class Level:
    price: float
    touches: int
    kind: str  # "support" | "resistance"
    name: str = ""
    forced: bool = False


# ── 데이터 수집 ──────────────────────────────────────────────────────────
def fetch_daily(ticker: str, rng: str = "1y") -> tuple[list[Bar], dict]:
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        f"?range={rng}&interval=1d&events=div,split"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:  # 티커 오타·상장폐지 등
        sys.exit(f"[에러] Yahoo 응답 {e.code} — 티커 '{ticker}' 확인 필요")

    err = payload.get("chart", {}).get("error")
    if err:
        sys.exit(f"[에러] Yahoo: {err}")
    res = payload["chart"]["result"][0]
    meta = res["meta"]
    q = res["indicators"]["quote"][0]
    tzoff = timedelta(seconds=meta.get("gmtoffset", 0))

    bars: list[Bar] = []
    for i, ts in enumerate(res["timestamp"]):
        o, h, lo, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if None in (o, h, lo, c):  # 거래정지일 등 결측 봉은 버린다
            continue
        bars.append(
            Bar(
                d=(datetime.fromtimestamp(ts, timezone.utc) + tzoff).date(),
                o=o,
                h=h,
                lo=lo,
                c=c,
                v=q["volume"][i] or 0,
            )
        )
    if len(bars) < 60:
        sys.exit(
            f"[에러] 거래일이 {len(bars)}개뿐 — 표본이 부족해 스윙 클러스터가 "
            "무의미하다. 템플릿 상단 경고 참고."
        )

    events = res.get("events", {})
    meta["_splits"] = list(events.get("splits", {}).values())
    meta["_divs"] = list(events.get("dividends", {}).values())
    return bars, meta


# ── 스윙 포인트 · 클러스터링 ─────────────────────────────────────────────
def find_swings(bars: list[Bar], w: int = SWING_WINDOW) -> tuple[list[float], list[float]]:
    """고가/저가가 전후 w거래일 창 내 최고/최저와 같은 지점."""
    highs, lows = [], []
    for i in range(w, len(bars) - w):
        win = bars[i - w : i + w + 1]
        if bars[i].h == max(b.h for b in win):
            highs.append(bars[i].h)
        if bars[i].lo == min(b.lo for b in win):
            lows.append(bars[i].lo)
    return highs, lows


def cluster(points: list[float], tol: float = CLUSTER_TOL) -> list[tuple[float, int]]:
    """가격 오름차순으로 훑으며 중심 ±tol 이내면 합치고 중심을 재계산."""
    out: list[list[float]] = []
    for p in sorted(points):
        if out and abs(p - sum(out[-1]) / len(out[-1])) <= tol * p:
            out[-1].append(p)
        else:
            out.append([p])
    return [(sum(g) / len(g), len(g)) for g in out]


def pick_levels(
    bars: list[Bar],
    forced: list[tuple[float, str]],
    min_touches: int,
    per_side: int,
) -> list[Level]:
    """현재가에서 가까운 순으로 각 방향 per_side개까지. 터치 수가 모자라도
    forced에 지정한 가격과 ±CLUSTER_TOL 안에 드는 클러스터는 개수 제한 없이 포함."""
    last = bars[-1].c
    hi_sw, lo_sw = find_swings(bars)
    res = [(c, n) for c, n in cluster(hi_sw) if c > last]
    sup = [(c, n) for c, n in cluster(lo_sw) if c < last]

    def suffix_for(price: float) -> str:
        for f, lab in forced:
            if abs(price - f) <= f * CLUSTER_TOL:
                return lab
        return ""

    def take(cands, kind, prefix):
        keep = sorted(
            (c for c in cands if c[1] >= min_touches), key=lambda c: abs(c[0] - last)
        )[:per_side]
        extra = [
            c
            for c in cands
            if c not in keep and any(abs(c[0] - f) <= f * CLUSTER_TOL for f, _ in forced)
        ]
        merged = sorted(keep + extra, key=lambda c: abs(c[0] - last))
        out = []
        for i, (c, n) in enumerate(merged):
            sfx = suffix_for(c)
            name = f"{prefix}{i + 1}" + (f" {sfx}" if sfx else "")
            out.append(Level(c, n, kind, name, forced=(c, n) in extra))
        return out

    return take(res, "resistance", "R") + take(sup, "support", "S")


# ── 좌표계 ───────────────────────────────────────────────────────────────
def nice_unit(target: float) -> float:
    """target에 가장 가까운 (1|2|2.5|5)×10^k."""
    if target <= 0:
        return 1.0
    k = math.floor(math.log10(target))
    return min((n * 10**k for n in NICE), key=lambda v: abs(v - target))


class Geom:
    def __init__(self, bars: list[Bar]):
        hi = max(b.h for b in bars)
        lo = min(b.lo for b in bars)
        pad = (hi - lo) * PAD_RATIO
        snap = nice_unit((hi - lo) / 50)  # 축 끝을 깔끔한 수로 스냅
        self.p_min = math.floor((lo - pad) / snap) * snap
        self.p_max = math.ceil((hi + pad) / snap) * snap
        self.scale = (Y_BOTTOM - Y_TOP) / (self.p_max - self.p_min)
        # 캔들 하나가 폭 step의 밴드를 차지하고 그 중앙에 놓인다
        # (끝점 기준으로 잡으면 마지막 캔들이 축에 붙는다)
        self.step = (X_RIGHT - X_LEFT) / len(bars)
        self.body_w = min(max(self.step * BODY_RATIO, BODY_W_MIN), BODY_W_MAX)
        self.hi, self.lo = hi, lo

    def y(self, p: float) -> float:
        return Y_BOTTOM - (p - self.p_min) * self.scale

    def x(self, i: int) -> float:
        return X_LEFT + (i + 0.5) * self.step

    def grid_prices(self) -> list[float]:
        span = self.p_max - self.p_min
        for k in range(-4, 7):
            for n in NICE:
                s = n * 10**k
                if span / s <= MAX_GRIDLINES:
                    start = math.ceil(self.p_min / s) * s
                    return [
                        round(start + i * s, 10)
                        for i in range(int((self.p_max - start) / s) + 1)
                    ]
        return []


def fmt(v: float, nd: int = 1) -> str:
    return f"{v:.{nd}f}"


def money(p: float) -> str:
    """레벨 라벨용 — 저가주는 소수점을 살린다."""
    return f"{p:,.0f}" if p >= 20 else f"{p:,.2f}"


# ── SVG ──────────────────────────────────────────────────────────────────
def render_svg(
    bars: list[Bar],
    g: Geom,
    levels: list[Level],
    ticker: str,
    name: str,
    events: list[tuple[str, str]],
    refs: list[tuple[float, str]],
) -> str:
    cls = f"{ticker.lower()}-chart"
    first, lastbar = bars[0], bars[-1]
    L: list[str] = []
    a = L.append

    a(f'<div class="{cls}">')
    a("<style>")
    a(
        f".{cls} {{\n"
        "  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; "
        "--muted:#898781;\n"
        "  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; "
        "--ref:#898781;\n}"
    )
    dark = (
        "--bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; "
        "--muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; "
        "--resistance:#d95926; --ref:#898781;"
    )
    a(f"@media (prefers-color-scheme: dark) {{\n  .{cls} {{ {dark} }}\n}}")
    a(f'[data-md-color-scheme="slate"] .{cls} {{ {dark} }}')
    a(f".{cls} svg {{ width:100%; height:auto; display:block; }}")
    a(f'.{cls} text {{ font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }}')
    a(f".{cls} .title {{ fill: var(--ink); font-weight:600; }}")
    a(f".{cls} .grid {{ stroke: var(--grid); stroke-width:1; }}")
    a(f".{cls} .axis {{ stroke: var(--axis); stroke-width:1; }}")
    a("</style>")
    a(
        f'<svg viewBox="0 0 {VB_W} {VB_H}" xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="{name}({ticker}) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">'
    )
    a(f'<rect x="0" y="0" width="{VB_W}" height="{VB_H}" fill="var(--bg)"/>')
    a(f'<text x="60" y="26" class="title" font-size="18">{name} ({ticker}) — 최근 1년 일봉</text>')
    a(
        f'<text x="60" y="44" font-size="12.5" fill="var(--ink2)">{first.d} ~ {lastbar.d} · '
        f"마지막 종가 ${lastbar.c:,.2f} ({lastbar.d}) · 단위 USD</text>"
    )

    for p in g.grid_prices():
        y = g.y(p)
        a(f'<line x1="{X_LEFT:.0f}" y1="{fmt(y)}" x2="{X_RIGHT:.0f}" y2="{fmt(y)}" class="grid"/>')
        a(
            f'<text x="52" y="{fmt(y + 4)}" font-size="11" text-anchor="end" '
            f'fill="var(--muted)">{money(p)}</text>'
        )

    seen: set[tuple[int, int]] = set()
    for i, b in enumerate(bars):  # 각 월 첫 거래일에 눈금
        key = (b.d.year, b.d.month)
        if key in seen:
            continue
        seen.add(key)
        x = g.x(i)
        a(f'<line x1="{fmt(x)}" y1="{fmt(Y_BOTTOM)}" x2="{fmt(x)}" y2="{fmt(Y_BOTTOM + 5)}" class="axis"/>')
        a(
            f'<text x="{fmt(x)}" y="{fmt(Y_BOTTOM + 18)}" font-size="10.5" '
            f'text-anchor="middle" fill="var(--muted)">{b.d.strftime("%y-%m")}</text>'
        )

    a(f'<line x1="{X_LEFT:.0f}" y1="{fmt(Y_BOTTOM)}" x2="{X_RIGHT:.0f}" y2="{fmt(Y_BOTTOM)}" class="axis"/>')
    a(f'<line x1="{X_LEFT:.0f}" y1="{fmt(Y_TOP)}" x2="{X_LEFT:.0f}" y2="{fmt(Y_BOTTOM)}" class="axis"/>')

    for price, label in refs:
        y = g.y(price)
        a(
            f'<line x1="{X_LEFT:.0f}" y1="{fmt(y)}" x2="{X_RIGHT:.0f}" y2="{fmt(y)}" '
            'stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>'
        )
        a(
            f'<text x="{LABEL_X:.0f}" y="{fmt(y + 3)}" font-size="10.5" '
            f'fill="var(--muted)">${money(price)} {label}</text>'
        )

    idx = {b.d.isoformat(): i for i, b in enumerate(bars)}
    for ds, label in events:
        if ds not in idx:
            print(f"[경고] 이벤트 날짜 {ds} 가 거래일에 없음 — 건너뜀", file=sys.stderr)
            continue
        x = g.x(idx[ds])
        a(
            f'<line x1="{fmt(x)}" y1="{fmt(Y_TOP)}" x2="{fmt(x)}" y2="{fmt(Y_BOTTOM)}" '
            'stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>'
        )
        a(f'<text x="{fmt(x + 6)}" y="68.0" font-size="10.5" fill="var(--down)">{ds} {label}</text>')

    for i, b in enumerate(bars):
        x = g.x(i)
        col = "var(--up)" if b.c >= b.o else "var(--down)"
        top, bot = g.y(max(b.o, b.c)), g.y(min(b.o, b.c))
        a(f'<line x1="{fmt(x)}" y1="{fmt(g.y(b.h))}" x2="{fmt(x)}" y2="{fmt(g.y(b.lo))}" stroke="{col}" class="wick"/>')
        a(
            f'<rect x="{fmt(x - g.body_w / 2, 2)}" y="{fmt(top)}" width="{fmt(g.body_w, 2)}" '
            f'height="{fmt(max(bot - top, BODY_H_MIN))}" fill="{col}"/>'
        )

    for lv in levels:
        y = g.y(lv.price)
        var = f"var(--{lv.kind})"
        a(
            f'<line x1="{X_LEFT:.0f}" y1="{fmt(y)}" x2="{X_RIGHT:.0f}" y2="{fmt(y)}" '
            f'stroke="{var}" stroke-width="1.4" stroke-dasharray="6,4"/>'
        )
        # 저항 라벨은 선 아래, 지지 라벨은 선 위 — 캔들과 덜 겹친다
        ly, ty = (y + 3.5, y + 15.5) if lv.kind == "resistance" else (y - 6, y + 6)
        a(
            f'<text x="{LABEL_X:.0f}" y="{fmt(ly)}" font-size="11.5" fill="{var}" '
            f'font-weight="600">${money(lv.price)} {lv.name}</text>'
        )
        a(f'<text x="{LABEL_X:.0f}" y="{fmt(ty)}" font-size="9.5" fill="var(--muted)">터치 {lv.touches}회</text>')

    a(f'<circle cx="{X_RIGHT:.1f}" cy="{fmt(g.y(lastbar.c))}" r="3" fill="var(--ink)"/>')

    a('<rect x="60" y="651" width="10" height="10" fill="var(--up)"/>')
    a('<text x="74" y="660" font-size="11" fill="var(--ink2)">상승(양봉)</text>')
    a('<rect x="150" y="651" width="10" height="10" fill="var(--down)"/>')
    a('<text x="164" y="660" font-size="11" fill="var(--ink2)">하락(음봉)</text>')
    a('<line x1="240" y1="656" x2="258" y2="656" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>')
    a('<text x="264" y="660" font-size="11" fill="var(--ink2)">지지선(Support)</text>')
    a('<line x1="390" y1="656" x2="408" y2="656" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>')
    a('<text x="414" y="660" font-size="11" fill="var(--ink2)">저항선(Resistance)</text>')
    a("</svg>")
    a("</div>")
    return "\n".join(L)


# ── 마크다운 산출물 ──────────────────────────────────────────────────────
def render_table(bars: list[Bar], levels: list[Level], refs: list[tuple[float, str]]) -> str:
    last = bars[-1]
    rows = ["| 레벨 | 가격 | 터치 횟수 | 비고 |", "|------|------|-----------|------|"]
    res = sorted([lv for lv in levels if lv.kind == "resistance"], key=lambda l: -l.price)
    sup = sorted([lv for lv in levels if lv.kind == "support"], key=lambda l: -l.price)
    for lv in res:
        note = "강제 포함(사유 기입)" if lv.forced else "<어느 시기의 스윙 고점대인지>"
        rows.append(f"| {lv.name} | ${money(lv.price)} | {lv.touches} | {note} |")
    if res and sup:
        where = f"{res[-1].name}과 {sup[0].name} 사이"
    elif sup:  # 기간 내 위쪽 스윙 고점 클러스터가 없음 = 신고가 구간
        where = f"기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 {sup[0].name}"
    elif res:
        where = f"기간 내 하단 지지 없음(신저가 구간) — 가장 가까운 저항은 {res[-1].name}"
    else:
        where = "유효한 클러스터 없음 — §4에 표본 부족 사유 기입"
    rows.append(f"| **현재가** | **${last.c:,.2f}** ({last.d} 종가) | — | {where} |")
    for lv in sup:
        note = "강제 포함(사유 기입)" if lv.forced else "<어느 시기의 스윙 저점대인지>"
        rows.append(f"| {lv.name} | ${money(lv.price)} | {lv.touches} | {note} |")
    for price, label in refs:
        rows.append(f"| 참고선 | ${money(price)} | — | {label} — <근시일 지지/저항으로 보지 않는 사유> |")
    return "\n".join(rows)


def render_facts(bars: list[Bar], g: Geom, meta: dict, min_touches: int, closes: list[str]) -> str:
    first, last = bars[0], bars[-1]
    today = date.today().isoformat()
    adj = "원주가(과거 분할은 소급 반영, 배당은 미반영)"
    out = [
        f"- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), {len(bars)}개 거래일, "
        f"{first.d}~{last.d}. 수집 시점: {today}. {adj}",
        f"- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 {SWING_WINDOW}거래일"
        f"(총 {2 * SWING_WINDOW + 1}거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.",
        f"- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 "
        f"±{CLUSTER_TOL:.1%} 이내면 같은 클러스터로 합산하고 중심을 재계산. "
        f"터치 {min_touches}회 이상만 표시(예외는 §2 비고).",
        "",
        "<!-- 참고용 수치 (문서에는 필요한 것만 옮길 것) -->",
        f"<!-- 52주 최고 {g.hi:,.2f} / 최저 {g.lo:,.2f} / y축 {g.p_min:,.2f}~{g.p_max:,.2f}"
        f" / 일평균 거래량 {sum(b.v for b in bars) / len(bars):,.0f}주 -->",
    ]
    if meta.get("_splits"):
        out.append(f"<!-- ⚠️ 기간 내 주식분할 이벤트 있음: {meta['_splits']} — §4에 소급조정 여부 명시 -->")
    if meta.get("_divs"):
        out.append(f"<!-- ⚠️ 기간 내 배당 {len(meta['_divs'])}회 — 원주가라 배당 미반영임을 §4에 명시 -->")
    if closes:
        by_date = {b.d.isoformat(): b for b in bars}
        out.append("<!-- 05_metrics.md/06_valuation.md 대조용 종가 -->")
        for ds in closes:
            b = by_date.get(ds)
            out.append(f"<!-- {ds} 종가 " + (f"${b.c:,.2f} -->" if b else "— 거래일 아님 -->"))
    return "\n".join(out)


# ── CLI ──────────────────────────────────────────────────────────────────
def kv(s: str, cast=str):
    k, _, v = s.partition(":")
    return cast(k), v.strip('"') or ""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--name", help="차트 제목에 쓸 회사명 (기본: Yahoo longName)")
    ap.add_argument("--range", default="1y", help="수집 기간 (기본 1y)")
    ap.add_argument("--emit", choices=["all", "chart", "table", "facts"], default="all")
    ap.add_argument("--event", action="append", default=[], metavar="YYYY-MM-DD:설명",
                    help="수직 이벤트선 (반복 가능)")
    ap.add_argument("--ref-line", action="append", default=[], metavar="가격:라벨",
                    help="참고선 — 현재 레짐과 단절된 수준 (반복 가능)")
    ap.add_argument("--force-level", action="append", default=[], metavar="가격[:라벨]",
                    help="터치 횟수가 모자라도 포함할 레벨 (52주 최저 등, 사유는 문서에 기입)")
    ap.add_argument("--close-on", action="append", default=[], metavar="YYYY-MM-DD",
                    help="다른 문서와 대조할 특정일 종가 출력 (반복 가능)")
    ap.add_argument("--min-touches", type=int, default=MIN_TOUCHES)
    ap.add_argument("--levels", type=int, default=LEVELS_PER_SIDE,
                    help=f"현재가 위/아래로 각각 최대 몇 개 (기본 {LEVELS_PER_SIDE})")
    ap.add_argument("-o", "--out", help="파일로 저장 (기본: 표준출력)")
    args = ap.parse_args()

    bars, meta = fetch_daily(args.ticker, args.range)
    g = Geom(bars)
    levels = pick_levels(
        bars, [kv(f, float) for f in args.force_level], args.min_touches, args.levels
    )
    name = args.name or meta.get("longName") or args.ticker
    events = [kv(e) for e in args.event]
    refs = [kv(r, float) for r in args.ref_line]

    parts = []
    if args.emit in ("all", "chart"):
        parts.append(render_svg(bars, g, levels, args.ticker, name, events, refs))
    if args.emit in ("all", "table"):
        parts.append(render_table(bars, levels, refs))
    if args.emit in ("all", "facts"):
        parts.append(render_facts(bars, g, meta, args.min_touches, args.close_on))
    text = "\n\n".join(parts) + "\n"

    if args.out:
        with open(args.out, "w") as f:
            f.write(text)
        print(f"[완료] {args.out} ({len(bars)}개 거래일, 레벨 {len(levels)}개)", file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
