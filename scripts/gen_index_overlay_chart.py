#!/usr/bin/env python3
"""여러 시계열을 한 기준일=100으로 지수화해 겹쳐 보는 비교 차트(SVG) 생성기.

`gen_technical_chart.py`가 자산 하나의 캔들·지지/저항을 그리는 것과 달리, 이 스크립트는
스케일이 서로 다른 여러 자산(환율·지수·금리 등)을 같은 시작일 기준 상대 변화율로 겹쳐
비교하는 용도다. 개별 자산 문서로는 안 보이는 "어느 쪽이 상대적으로 더 크게 움직였는지"를
드러내기 위한 것이라 지지/저항 레벨은 다루지 않는다.

    uv run python scripts/gen_index_overlay_chart.py \\
        --series "DX-Y.NYB:달러인덱스 (DXY):1" \\
        --series "EURUSD=X:유로/달러 환율:2" \\
        --series "JPY=X:엔/달러 환율:3" \\
        --series "KRW=X:원/달러 환율:4" \\
        --title "fx 4종 비교" -o out.md

`--series`는 `티커:라벨:색상슬롯` 형식이며 반복 지정한다. 색상슬롯 1~8은
`docs/meta/macro/`가 이미 쓰고 있는 검증된 8색 팔레트(파랑·주황·아쿠아·노랑·마젠타·초록·보라·빨강)
순번과 동일하다 — 새 슬롯을 추가로 정의하지 않고 그 순서를 그대로 재사용한다.

기준일(모든 시리즈가 공통으로 데이터를 가진 첫 날, "가장 늦게 시작한 시리즈의 시작일")을
100으로 맞춘다. 시리즈마다 상장일·거래소 휴장일이 달라 봉 개수가 다를 수 있으므로,
x축은 봉 인덱스가 아니라 **실제 날짜** 기준 연속 축이다 — `gen_technical_chart.py`(봉
인덱스 기준 x축)와 다른 부분.

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

VB_W, VB_H = 1200, 700
X_LEFT, X_RIGHT = 60.0, 1052.0
Y_TOP, Y_BOTTOM = 56.0, 600.0
LABEL_X = X_RIGHT + 6
NICE = (1.0, 2.0, 2.5, 5.0)

# docs/meta/macro/ 캔들차트와 동일한 검증된 8색 팔레트(라이트/다크) — 슬롯 순서 고정.
PALETTE = {
    1: ("#2a78d6", "#3987e5"),  # blue
    2: ("#eb6834", "#d95926"),  # orange
    3: ("#1baf7a", "#199e70"),  # aqua
    4: ("#eda100", "#c98500"),  # yellow
    5: ("#e87ba4", "#d55181"),  # magenta
    6: ("#008300", "#008300"),  # green
    7: ("#4a3aa7", "#9085e9"),  # violet
    8: ("#e34948", "#e66767"),  # red
}


@dataclass(frozen=True)
class Series:
    ticker: str
    label: str
    slot: int
    closes: dict  # date -> float


def slug(ticker: str) -> str:
    return "".join(c for c in ticker.lower() if c.isalnum())


def fetch_closes(ticker: str, rng: str, interval: str) -> dict:
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        f"?range={rng}&interval={interval}&events=div,split"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"[에러] Yahoo 응답 {e.code} — 티커 '{ticker}' 확인 필요")
    err = payload.get("chart", {}).get("error")
    if err:
        sys.exit(f"[에러] Yahoo: {err}")
    res = payload["chart"]["result"][0]
    meta = res["meta"]
    q = res["indicators"]["quote"][0]
    tzoff = timedelta(seconds=meta.get("gmtoffset", 0))
    out = {}
    for i, ts in enumerate(res["timestamp"]):
        c = q["close"][i]
        if c is None or c == 0:
            continue
        d = (datetime.fromtimestamp(ts, timezone.utc) + tzoff).date()
        out[d] = c
    if not out:
        sys.exit(f"[에러] '{ticker}' 데이터가 비어 있음")
    return out


def nice_unit(target: float) -> float:
    if target <= 0:
        return 1.0
    k = math.floor(math.log10(target))
    for n in NICE:
        v = n * 10**k
        if v >= target:
            return v
    return 10 * 10**k


def money(v: float, nd: int = 1) -> str:
    return f"{v:,.{nd}f}"


def price_str(v: float) -> str:
    """표에 원가격을 적을 때 쓰는 자릿수 휴리스틱 — 20 이상이면 정수 단위가 유의미해
    소수 2자리, 미만이면(예: 유로/달러 ~1.17) 4자리로 소수점 이하를 살린다."""
    return f"{v:,.2f}" if v >= 20 else f"{v:,.4f}"


def build_indexed(series_list: list[Series]) -> tuple[dict, date, date]:
    common_start = max(min(s.closes) for s in series_list)
    global_end = max(max(s.closes) for s in series_list)
    indexed = {}
    for s in series_list:
        dates_sorted = sorted(d for d in s.closes if d >= common_start)
        base_date = dates_sorted[0]
        base_price = s.closes[base_date]
        indexed[s.ticker] = [(d, 100.0 * s.closes[d] / base_price) for d in dates_sorted]
    return indexed, common_start, global_end


def render_svg(series_list: list[Series], indexed: dict, common_start: date, global_end: date, title: str, period_label: str) -> str:
    cls = "idx-overlay-" + "-".join(slug(s.ticker) for s in series_list)[:40]
    start_ord, end_ord = common_start.toordinal(), global_end.toordinal()
    span_days = max(end_ord - start_ord, 1)

    def x_of(d: date) -> float:
        return X_LEFT + (d.toordinal() - start_ord) / span_days * (X_RIGHT - X_LEFT)

    all_vals = [v for pts in indexed.values() for _, v in pts]
    lo, hi = min(all_vals), max(all_vals)
    pad = (hi - lo) * 0.08 or 1.0
    p_min, p_max = lo - pad, hi + pad
    step = nice_unit((p_max - p_min) / 6)
    grid_start = math.floor(p_min / step) * step
    grids = []
    v = grid_start
    while v <= p_max:
        if v >= p_min:
            grids.append(round(v, 2))
        v += step

    def y_of(val: float) -> float:
        return Y_BOTTOM - (val - p_min) / (p_max - p_min) * (Y_BOTTOM - Y_TOP)

    L: list[str] = []
    a = L.append
    light_vars = "; ".join(f"--s-{slug(s.ticker)}:{PALETTE[s.slot][0]}" for s in series_list)
    dark_vars = "; ".join(f"--s-{slug(s.ticker)}:{PALETTE[s.slot][1]}" for s in series_list)

    a(f'<div class="{cls}">')
    a("<style>")
    a(
        f".{cls} {{\n"
        "  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; "
        f"--muted:#898781; --base:#898781; {light_vars};\n}}"
    )
    a(
        f"@media (prefers-color-scheme: dark) {{\n  .{cls} {{ --bg:#1a1a19; --grid:#2c2c2a; "
        f"--axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; {dark_vars}; }}\n}}"
    )
    a(
        f'[data-md-color-scheme="slate"] .{cls} {{ --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; '
        f'--ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; {dark_vars}; }}'
    )
    a(f".{cls} svg {{ width:100%; height:auto; display:block; }}")
    a(f'.{cls} text {{ font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }}')
    a(f".{cls} .title {{ fill: var(--ink); font-weight:600; }}")
    a(f".{cls} .grid {{ stroke: var(--grid); stroke-width:1; }}")
    a(f".{cls} .axis {{ stroke: var(--axis); stroke-width:1; }}")
    a("</style>")
    names = "·".join(s.label for s in series_list)
    a(
        f'<svg viewBox="0 0 {VB_W} {VB_H}" xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="{names}, {common_start} 기준 100 지수화, {period_label} 비교선 차트">'
    )
    a(f'<rect x="0" y="0" width="{VB_W}" height="{VB_H}" fill="var(--bg)"/>')
    a(f'<text x="60" y="26" class="title" font-size="18">{title} — {common_start} = 100 지수화 ({period_label})</text>')
    a(f'<text x="60" y="44" font-size="12.5" fill="var(--ink2)">{common_start} ~ {global_end} · 단위: 지수(index)</text>')

    for gv in grids:
        y = y_of(gv)
        a(f'<line x1="{X_LEFT:.0f}" y1="{y:.1f}" x2="{X_RIGHT:.0f}" y2="{y:.1f}" class="grid"/>')
        a(f'<text x="52" y="{y+4:.1f}" font-size="11" text-anchor="end" fill="var(--muted)">{gv:.0f}</text>')

    for yr in range(common_start.year, global_end.year + 1):
        jan1 = date(yr, 1, 1)
        if jan1 < common_start or jan1 > global_end:
            continue
        x = x_of(jan1)
        a(
            f'<line x1="{x:.1f}" y1="{Y_TOP:.0f}" x2="{x:.1f}" y2="{Y_BOTTOM:.0f}" '
            'stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>'
        )
        a(f'<line x1="{x:.1f}" y1="{Y_BOTTOM:.0f}" x2="{x:.1f}" y2="{Y_BOTTOM+5:.0f}" class="axis"/>')
        a(f'<text x="{x:.1f}" y="{Y_BOTTOM+18:.0f}" font-size="10.5" text-anchor="middle" fill="var(--muted)">{yr}</text>')

    a(f'<line x1="{X_LEFT:.0f}" y1="{Y_BOTTOM:.0f}" x2="{X_RIGHT:.0f}" y2="{Y_BOTTOM:.0f}" class="axis"/>')
    a(f'<line x1="{X_LEFT:.0f}" y1="{Y_TOP:.0f}" x2="{X_LEFT:.0f}" y2="{Y_BOTTOM:.0f}" class="axis"/>')

    y100 = y_of(100)
    a(
        f'<line x1="{X_LEFT:.0f}" y1="{y100:.1f}" x2="{X_RIGHT:.0f}" y2="{y100:.1f}" '
        'stroke="var(--base)" stroke-width="1.2" stroke-dasharray="5,3" opacity="0.8"/>'
    )
    a(f'<text x="{LABEL_X:.0f}" y="{y100+3.5:.1f}" font-size="10.5" fill="var(--muted)">100 (시작={common_start})</text>')

    for s in series_list:
        pts = indexed[s.ticker]
        path = " ".join(f"{x_of(d):.1f},{y_of(v):.1f}" for d, v in pts)
        a(f'<polyline points="{path}" fill="none" stroke="var(--s-{slug(s.ticker)})" stroke-width="2"/>')

    ends = []
    for s in series_list:
        d, v = indexed[s.ticker][-1]
        ends.append([y_of(v), s, v])
    ends.sort(key=lambda e: e[0])
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < 16.0:
            ends[i][0] = ends[i - 1][0] + 16.0
    for y, s, v in ends:
        a(
            f'<text x="{LABEL_X:.0f}" y="{y+4:.1f}" font-size="11.5" font-weight="700" '
            f'fill="var(--s-{slug(s.ticker)})" paint-order="stroke" stroke="var(--bg)" '
            f'stroke-width="3">{s.label} {v:.1f}</text>'
        )

    a("</svg>")
    a("</div>")
    return "\n".join(L)


def render_table(series_list: list[Series], indexed: dict, common_start: date) -> str:
    rows = ["| 지표 | 시작 값 | 현재 값 | 지수 | 순변화 |", "|------|---------|---------|------|--------|"]
    for s in series_list:
        base_date = indexed[s.ticker][0][0]
        base_price = s.closes[base_date]
        last_date, last_idx = indexed[s.ticker][-1]
        last_price = last_idx / 100 * base_price
        pct = last_idx - 100
        sign = "+" if pct >= 0 else ""
        rows.append(
            f"| {s.label} | {price_str(base_price)} ({base_date}) | {price_str(last_price)} ({last_date}) "
            f"| {last_idx:.1f} | {sign}{pct:.1f}% |"
        )
    return "\n".join(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--series", action="append", required=True, metavar="티커:라벨:색상슬롯",
        help="반복 지정. 색상슬롯 1~8은 팔레트 순번(1=파랑 2=주황 3=아쿠아 4=노랑 …)",
    )
    ap.add_argument("--title", required=True, help="차트 상단 제목")
    ap.add_argument("--range", default="5y")
    ap.add_argument("--interval", default="1wk", choices=["1d", "1wk"])
    ap.add_argument("--period-label", default=None, help="차트 상단 기간 표기 (기본: --range·--interval에서 추정)")
    ap.add_argument("--emit", choices=["all", "chart", "table"], default="all")
    ap.add_argument("-o", "--out", help="파일로 저장 (기본: 표준출력)")
    args = ap.parse_args()

    series_list = []
    for spec in args.series:
        parts = spec.split(":")
        if len(parts) != 3:
            sys.exit(f"[에러] --series 형식 오류: '{spec}' (티커:라벨:색상슬롯 이어야 함)")
        ticker, label, slot_s = parts
        slot = int(slot_s)
        if slot not in PALETTE:
            sys.exit(f"[에러] 색상슬롯은 1~8: '{spec}'")
        closes = fetch_closes(ticker, args.range, args.interval)
        series_list.append(Series(ticker, label, slot, closes))

    indexed, common_start, global_end = build_indexed(series_list)
    period_label = args.period_label or f"최근 {args.range} {'주간' if args.interval == '1wk' else '일간'}"

    parts = []
    if args.emit in ("all", "chart"):
        parts.append(render_svg(series_list, indexed, common_start, global_end, args.title, period_label))
    if args.emit in ("all", "table"):
        parts.append(render_table(series_list, indexed, common_start))
    text = "\n\n".join(parts) + "\n"

    if args.out:
        with open(args.out, "w") as f:
            f.write(text)
        print(f"[완료] {args.out} ({len(series_list)}개 시리즈, 기준일 {common_start})", file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
