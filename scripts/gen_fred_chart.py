#!/usr/bin/env python3
"""FRED 경제지표 시계열 차트(SVG) 생성기 — 선형(line)·막대(bar) 모드.

`gen_technical_chart.py`(캔들·지지/저항)·`gen_index_overlay_chart.py`(Yahoo 종가 겹치기)와
달리, 이 스크립트는 **가격이 아닌 경제지표**를 그린다. 데이터 출처가 Yahoo가 아니라
FRED(세인트루이스 연은)이며, 세 스크립트의 차이는 다음과 같다.

| | 대상 | 출처 | 그림 |
|---|---|---|---|
| `gen_technical_chart.py` | 자산 하나의 가격 | Yahoo OHLC | 캔들 + 지지/저항 |
| `gen_index_overlay_chart.py` | 여러 자산의 가격 | Yahoo 종가 | 지수화/원값 겹친 선 |
| **이 스크립트** | 경제지표 | FRED | 선 또는 막대 + 침체 음영 |

**왜 캔들을 쓰지 않는가**: CPI·실업률 같은 지표는 한 기간에 값이 **하나**뿐이라 시가·고가·
저가가 존재하지 않는다. 캔들은 그릴 수 없고, 스윙 클러스터로 뽑는 "지지/저항 3.4%"도
의미가 없다 — 경제지표에는 가격처럼 되돌림이 일어나는 호가 레벨이 없기 때문이다.
대신 이 스크립트는 **기준선**(`--ref-line`, 예: 연준 물가목표 2%, 확산지수의 50 또는 0)과
**NBER 침체 음영**(`--recession`)을 지원한다 — 경제지표는 절대 수준 자체보다 "기준을
넘었는가", "침체기에 어떻게 움직였는가"로 읽히기 때문이다.

    # 단일 지표 — CPI 전년동월비
    uv run python scripts/gen_fred_chart.py \\
        --series "CPIAUCSL:소비자물가지수 (CPI):1:pc1" \\
        --title "미국 소비자물가 상승률 (CPI, 전년동월비)" \\
        --start 2021-09-01 --unit-label "%" --ref-line "2:연준 목표 2%" --recession -o out.md

    # 여러 지표 겹치기 — 단위가 같을 때만(전부 %)
    uv run python scripts/gen_fred_chart.py \\
        --series "CPIAUCSL:CPI:1:pc1" --series "CPILFESL:Core CPI:2:pc1" \\
        --series "PCEPILFE:Core PCE:3:pc1" \\
        --title "물가지표 3종 비교" --start 2021-09-01 --unit-label "%" -o out.md

    # 증감(플로우) 지표는 막대가 맞다 — 비농업고용 전월대비 증감
    uv run python scripts/gen_fred_chart.py --chart-type bar \\
        --series "PAYEMS:비농업부문 고용 증감:1:chg" \\
        --title "미국 비농업부문 고용 증감" --start 2021-09-01 \\
        --unit-label "천 명" --decimals 0 -o out.md

`--series`는 `시리즈ID:라벨:색상슬롯[:변환]` 형식이며 반복 지정한다. 색상슬롯 1~8은
`gen_index_overlay_chart.py`와 **동일한 8색 팔레트** 순번이고, CSS 변수·다크모드 처리도
같다 — `docs/macro/`의 기존 차트와 나란히 놓았을 때 톤이 어긋나지 않게 하기 위해서다.

**변환(units)은 FRED가 서버에서 해준다** — 직접 계산하지 않는다:
- `lin`(기본) 원값 그대로. 실업률·확산지수처럼 이미 비율/지수인 지표.
- `pc1` 전년동월비 %. **물가지수는 반드시 이것을 쓴다** — `CPIAUCSL` 원값은
  "1982-84=100" 지수라 그대로 그리면 우상향 직선만 나오고 인플레이션은 안 보인다.
- `chg` 전기대비 증감(원단위). 고용자수(`PAYEMS`)처럼 **누적 레벨로 발표되는 지표**에 쓴다
  — 원값은 1.6억 명대 완만한 선이라 월별 고용 창출 규모가 전혀 드러나지 않는다.
- `pch` 전기대비 %. 그 밖의 변환 코드는 FRED `units` 파라미터 문서와 같다.

**주의 — 경제지표는 개정(revision)된다.** FRED가 돌려주는 값은 항상 **최신 빈티지**라,
같은 커맨드를 몇 달 뒤 다시 돌리면 과거 구간의 값까지 조용히 달라질 수 있다(GDP는 속보치
→ 잠정치 → 확정치, 고용은 매년 벤치마크 개정). 차트가 과거와 달라졌다고 스크립트 버그로
의심하지 말 것 — 발표 당시 값이 필요하면 FRED ALFRED(`realtime_start`)를 써야 하는데
이 스크립트는 지원하지 않는다.

**결측(`.`)은 버리고 그 자리에서 선을 끊는다.** 발표 자체가 없었던 달을 직선으로 메우면
"완만하게 변했다"로 읽히기 때문이다 — 2025년 10월 CPI·Core CPI·실업률이 실제로 그렇다
(연방정부 셧다운으로 BLS 발표가 취소됐고, FRED에 결측으로 남아 있다). 차트 중간이
끊겨 있으면 스크립트 오류가 아니라 그 달에 데이터가 없다는 뜻이다.

`FRED_API_KEY` 환경변수가 필요하다(저장소 루트 `.env`에 두면 자동으로 읽는다 — `.env`는
`.gitignore` 대상이고 `.env.template`이 키 이름을 알려준다). 키 발급은 무료:
https://fredaccount.stlouisfed.org/apikeys

의존성 없음(표준 라이브러리만). 원자료는 저장소에 커밋하지 않는다.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path

VB_W, VB_H = 1200, 700
X_LEFT, X_RIGHT = 60.0, 1052.0
Y_TOP, Y_BOTTOM = 56.0, 600.0
LABEL_X = X_RIGHT + 6
NICE = (1.0, 2.0, 2.5, 5.0)
FRED = "https://api.stlouisfed.org/fred"

# gen_index_overlay_chart.py와 동일한 8색 팔레트(라이트/다크) — 슬롯 순서 고정.
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
    sid: str
    label: str
    slot: int
    units: str
    obs: list  # [(date, float)] 오름차순
    meta: dict


def slug(s: str) -> str:
    return "".join(c for c in s.lower() if c.isalnum())


# ── 데이터 수집 ──────────────────────────────────────────────────────────
def load_api_key() -> str:
    """환경변수 우선, 없으면 저장소 루트 `.env`에서 읽는다."""
    key = os.environ.get("FRED_API_KEY")
    if key:
        return key.strip()
    env = Path(__file__).resolve().parent.parent / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip().strip("'\"")
    sys.exit(
        "[에러] FRED_API_KEY를 찾을 수 없다 — 환경변수로 넘기거나 저장소 루트 .env에 "
        "적어라(.env.template 참고). 키 발급: https://fredaccount.stlouisfed.org/apikeys"
    )


def fred_get(path: str, key: str, **params) -> dict:
    params.update(api_key=key, file_type="json")
    url = f"{FRED}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        sid = params.get("series_id", "")
        sys.exit(
            f"[에러] FRED 응답 {e.code} (series_id='{sid}') — 시리즈 ID 또는 API 키 확인 필요\n{body}"
        )


def fetch_series(sid: str, key: str, units: str, start: str | None) -> tuple[list, dict]:
    meta = fred_get("series", key, series_id=sid)["seriess"][0]
    p = dict(series_id=sid, units=units, sort_order="asc")
    if start:
        # pc1·chg는 변환에 직전 기간 값이 필요하다. FRED는 요청 구간 밖의 원자료로 변환을
        # 계산해 주므로 observation_start를 그대로 넘겨도 첫 점이 비지 않는다.
        p["observation_start"] = start
    obs = []
    for o in fred_get("series/observations", key, **p)["observations"]:
        if o["value"] == ".":  # FRED의 결측 표기
            continue
        obs.append((date.fromisoformat(o["date"]), float(o["value"])))
    if not obs:
        sys.exit(f"[에러] '{sid}' 관측치가 비어 있음 — --start가 시리즈 종료일보다 뒤인지 확인")
    return obs, meta


def fetch_recessions(key: str, lo: date, hi: date) -> list:
    """NBER 침체 국면(USREC=1)을 (시작, 끝) 구간 목록으로. 차트 범위로 잘라 돌려준다."""
    obs = fred_get(
        "series/observations", key, series_id="USREC", sort_order="asc",
        observation_start=lo.isoformat(),
    )["observations"]
    spans, run_start, prev = [], None, None
    for o in obs:
        if o["value"] == ".":
            continue
        d, v = date.fromisoformat(o["date"]), float(o["value"])
        if v == 1 and run_start is None:
            run_start = d
        elif v == 0 and run_start is not None:
            spans.append((run_start, prev or d))
            run_start = None
        prev = d
    if run_start is not None:
        spans.append((run_start, prev))
    return [(max(a, lo), min(b, hi)) for a, b in spans if b >= lo and a <= hi]


# ── 렌더링 ───────────────────────────────────────────────────────────────
def xml_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def split_gaps(obs: list) -> list:
    """결측으로 끊긴 구간마다 나눈 관측치 묶음 목록.

    폴리라인 하나로 이어 그리면 발표되지 않은 달을 직선으로 메워 버린다 — 값이 없었던
    구간이 "완만하게 변했다"로 보이게 되므로 선을 끊는다. 실제로 일어나는 일이다:
    2025년 10월 CPI·실업률은 연방정부 셧다운으로 BLS가 발표하지 못해 FRED에 결측(`.`)으로
    남아 있다. 간격이 중앙값의 1.8배를 넘으면 끊는다 — 월간 시리즈에서 한 달을 건너뛰면
    간격이 2배가 되고, 월 길이 차이(28~31일)로는 1.8배에 못 미친다."""
    if len(obs) < 3:
        return [obs]
    steps = sorted((obs[i + 1][0] - obs[i][0]).days for i in range(len(obs) - 1))
    median = steps[len(steps) // 2]
    out, cur = [], [obs[0]]
    for prev, nxt in zip(obs, obs[1:]):
        if (nxt[0] - prev[0]).days > median * 1.8:
            out.append(cur)
            cur = []
        cur.append(nxt)
    out.append(cur)
    return [g for g in out if g]


def nice_unit(target: float) -> float:
    if target <= 0:
        return 1.0
    k = math.floor(math.log10(target))
    for n in NICE:
        v = n * 10**k
        if v >= target:
            return v
    return 10 * 10**k


def render_svg(
    series_list: list[Series],
    title: str,
    period_label: str,
    unit_label: str,
    decimals: int,
    chart_type: str,
    ref_lines: list,
    recessions: list,
    include_zero: bool,
) -> str:
    cls = "fred-" + "-".join(slug(s.sid) for s in series_list)[:40]
    lo_d = min(s.obs[0][0] for s in series_list)
    hi_d = max(s.obs[-1][0] for s in series_list)
    start_ord, end_ord = lo_d.toordinal(), hi_d.toordinal()
    span_days = max(end_ord - start_ord, 1)
    # 막대 모드는 마지막 막대가 오른쪽 축을 넘지 않도록 폭의 절반만큼 여백을 둔다.
    n_bars = max(len(series_list[0].obs), 1)
    bar_w = (X_RIGHT - X_LEFT) / n_bars * 0.62 if chart_type == "bar" else 0.0

    def x_of(d: date) -> float:
        inner_l, inner_r = X_LEFT + bar_w / 2, X_RIGHT - bar_w / 2
        return inner_l + (d.toordinal() - start_ord) / span_days * (inner_r - inner_l)

    vals = [v for s in series_list for _, v in s.obs] + [r[0] for r in ref_lines]
    lo, hi = min(vals), max(vals)
    if include_zero or chart_type == "bar" or lo < 0 < hi:
        # 막대는 0에서 자라므로 0이 축 안에 없으면 길이가 값을 뜻하지 않게 된다.
        lo, hi = min(lo, 0.0), max(hi, 0.0)
    pad = (hi - lo) * 0.08 or 1.0
    p_min, p_max = lo - pad, hi + pad
    step = nice_unit((p_max - p_min) / 6)
    grids, v = [], math.floor(p_min / step) * step
    while v <= p_max:
        if v >= p_min:
            grids.append(round(v, 6))
        v += step

    def y_of(val: float) -> float:
        return Y_BOTTOM - (val - p_min) / (p_max - p_min) * (Y_BOTTOM - Y_TOP)

    L: list[str] = []
    a = L.append
    light = "; ".join(f"--s-{slug(s.sid)}:{PALETTE[s.slot][0]}" for s in series_list)
    dark = "; ".join(f"--s-{slug(s.sid)}:{PALETTE[s.slot][1]}" for s in series_list)

    a(f'<div class="{cls}">')
    a("<style>")
    a(
        f".{cls} {{\n"
        "  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; "
        f"--muted:#898781; --base:#898781; --rec:#898781; {light};\n}}"
    )
    a(
        f"@media (prefers-color-scheme: dark) {{\n"
        f'  .dark .{cls} {{ --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; '
        f"--ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; {dark}; }}\n}}"
    )
    a(
        f'.dark .{cls} {{ --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; '
        f'--ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; {dark}; }}'
    )
    a(f".{cls} svg {{ width:100%; height:auto; display:block; }}")
    a(f'.{cls} text {{ font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }}')
    a(f".{cls} .title {{ fill: var(--ink); font-weight:600; }}")
    a(f".{cls} .grid {{ stroke: var(--grid); stroke-width:1; }}")
    a(f".{cls} .axis {{ stroke: var(--axis); stroke-width:1; }}")
    a("</style>")

    names = "·".join(xml_escape(s.label) for s in series_list)
    kind = "막대" if chart_type == "bar" else "선"
    a(
        f'<svg viewBox="0 0 {VB_W} {VB_H}" xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="{names}, {period_label}, 단위 {xml_escape(unit_label)} {kind} 차트">'
    )
    a(f'<rect x="0" y="0" width="{VB_W}" height="{VB_H}" fill="var(--bg)"/>')
    a(f'<text x="60" y="26" class="title" font-size="18">{xml_escape(title)} ({period_label})</text>')
    sids = " · ".join(f"FRED {s.sid}" for s in series_list)
    a(
        f'<text x="60" y="44" font-size="12.5" fill="var(--ink2)">{lo_d} ~ {hi_d} · '
        f'단위: {xml_escape(unit_label)} · 출처: {xml_escape(sids)}</text>'
    )

    for r_lo, r_hi in recessions:
        x1, x2 = x_of(r_lo), x_of(r_hi)
        a(
            f'<rect x="{x1:.1f}" y="{Y_TOP:.0f}" width="{max(x2-x1,1.5):.1f}" '
            f'height="{Y_BOTTOM-Y_TOP:.0f}" fill="var(--rec)" opacity="0.14"/>'
        )

    for gv in grids:
        y = y_of(gv)
        a(f'<line x1="{X_LEFT:.0f}" y1="{y:.1f}" x2="{X_RIGHT:.0f}" y2="{y:.1f}" class="grid"/>')
        a(f'<text x="52" y="{y+4:.1f}" font-size="11" text-anchor="end" fill="var(--muted)">{gv:,.{decimals}f}</text>')

    for yr in range(lo_d.year, hi_d.year + 1):
        jan1 = date(yr, 1, 1)
        if jan1 < lo_d or jan1 > hi_d:
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

    for rv, rlabel in ref_lines:
        y = y_of(rv)
        a(
            f'<line x1="{X_LEFT:.0f}" y1="{y:.1f}" x2="{X_RIGHT:.0f}" y2="{y:.1f}" '
            'stroke="var(--base)" stroke-width="1.2" stroke-dasharray="5,3" opacity="0.85"/>'
        )
        if rlabel:
            a(f'<text x="{X_LEFT+6:.0f}" y="{y-5:.1f}" font-size="10.5" fill="var(--muted)">{xml_escape(rlabel)}</text>')

    if chart_type == "bar":
        s = series_list[0]
        y0 = y_of(0.0)
        for d, v in s.obs:
            y = y_of(v)
            a(
                f'<rect x="{x_of(d)-bar_w/2:.1f}" y="{min(y,y0):.1f}" width="{bar_w:.1f}" '
                f'height="{max(abs(y-y0),0.8):.1f}" fill="var(--s-{slug(s.sid)})" opacity="0.9"/>'
            )
        a(f'<line x1="{X_LEFT:.0f}" y1="{y0:.1f}" x2="{X_RIGHT:.0f}" y2="{y0:.1f}" class="axis"/>')
    else:
        for s in series_list:
            for seg in split_gaps(s.obs):
                path = " ".join(f"{x_of(d):.1f},{y_of(v):.1f}" for d, v in seg)
                if len(seg) == 1:  # 양옆이 다 결측인 외딴 관측치 — 선으로는 안 보인다
                    d, v = seg[0]
                    a(f'<circle cx="{x_of(d):.1f}" cy="{y_of(v):.1f}" r="2.4" fill="var(--s-{slug(s.sid)})"/>')
                    continue
                a(f'<polyline points="{path}" fill="none" stroke="var(--s-{slug(s.sid)})" stroke-width="2"/>')

    ends = []
    for s in series_list:
        d, v = s.obs[-1]
        ends.append([y_of(v), s, v, d])
    ends.sort(key=lambda e: e[0])
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < 16.0:
            ends[i][0] = ends[i - 1][0] + 16.0
    for y, s, v, d in ends:
        a(
            f'<text x="{LABEL_X:.0f}" y="{y+4:.1f}" font-size="11.5" font-weight="700" '
            f'fill="var(--s-{slug(s.sid)})" paint-order="stroke" stroke="var(--bg)" '
            f'stroke-width="3">{xml_escape(s.label)} {v:,.{decimals}f}{xml_escape(unit_label)}</text>'
        )
    if recessions:
        a(
            f'<text x="{X_LEFT:.0f}" y="{Y_BOTTOM+40:.0f}" font-size="10.5" fill="var(--muted)">'
            '음영 = NBER 기준 경기침체 국면 (FRED USREC)</text>'
        )

    a("</svg>")
    a("</div>")
    return "\n".join(L)


def render_table(series_list: list[Series], unit_label: str, decimals: int) -> str:
    rows = ["| 지표 | 시작 | 현재 | 변화 | 기간 최고 | 기간 최저 |",
            "|------|------|------|------|-----------|-----------|"]
    u = unit_label
    for s in series_list:
        (d0, v0), (d1, v1) = s.obs[0], s.obs[-1]
        vals = [v for _, v in s.obs]
        hi_d = max(s.obs, key=lambda t: t[1])
        lo_d = min(s.obs, key=lambda t: t[1])
        diff = v1 - v0
        sign = "+" if diff >= 0 else ""
        rows.append(
            f"| {s.label} | {v0:,.{decimals}f}{u} ({d0}) | {v1:,.{decimals}f}{u} ({d1}) "
            f"| {sign}{diff:,.{decimals}f} | {hi_d[1]:,.{decimals}f}{u} ({hi_d[0]}) "
            f"| {lo_d[1]:,.{decimals}f}{u} ({lo_d[0]}) |"
        )
    return "\n".join(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--series", action="append", required=True, metavar="ID:라벨:슬롯[:변환]",
        help="반복 지정. 슬롯 1~8은 팔레트 순번(1=파랑 2=주황 3=아쿠아 …), "
             "변환은 FRED units 코드(lin·pc1·chg·pch, 기본 lin)",
    )
    ap.add_argument("--title", required=True, help="차트 상단 제목")
    ap.add_argument("--start", default=None, metavar="YYYY-MM-DD", help="관측 시작일 (기본: 시리즈 전체)")
    ap.add_argument("--unit-label", default="%", help="값 뒤에 붙일 단위 표시 (기본 %%)")
    ap.add_argument("--decimals", type=int, default=1, help="그리드·라벨·표의 소수 자릿수 (기본 1)")
    ap.add_argument(
        "--chart-type", choices=["line", "bar"], default="line",
        help="line=수준·비율 지표(기본). bar=증감 등 0을 기준으로 부호가 갈리는 플로우 지표 "
             "(막대 모드는 첫 --series 하나만 그린다)",
    )
    ap.add_argument("--ref-line", action="append", default=[], metavar="값[:라벨]",
                    help="수평 기준선. 예: '2:연준 목표 2%%', '50:확장/수축 경계', '0'")
    ap.add_argument("--recession", action="store_true", help="NBER 침체 국면(USREC)을 음영으로 표시")
    ap.add_argument("--include-zero", action="store_true", help="y축 범위에 0을 강제로 포함")
    ap.add_argument("--period-label", default=None, help="차트 상단 기간 표기 (기본: 관측 주기에서 추정)")
    ap.add_argument("--emit", choices=["all", "chart", "table"], default="all")
    ap.add_argument("-o", "--out", help="파일로 저장 (기본: 표준출력)")
    args = ap.parse_args()

    key = load_api_key()
    series_list = []
    for spec in args.series:
        parts = spec.split(":")
        if len(parts) not in (3, 4):
            sys.exit(f"[에러] --series 형식 오류: '{spec}' (ID:라벨:슬롯[:변환] 이어야 함)")
        sid, label, slot_s = parts[0], parts[1], parts[2]
        units = parts[3] if len(parts) == 4 else "lin"
        slot = int(slot_s)
        if slot not in PALETTE:
            sys.exit(f"[에러] 색상슬롯은 1~8: '{spec}'")
        obs, meta = fetch_series(sid, key, units, args.start)
        series_list.append(Series(sid, label, slot, units, obs, meta))

    if args.chart_type == "bar" and len(series_list) > 1:
        sys.exit("[에러] --chart-type bar는 시리즈 하나만 지원한다 — 막대가 겹치면 읽을 수 없다")

    ref_lines = []
    for spec in args.ref_line:
        v, _, lab = spec.partition(":")
        ref_lines.append((float(v), lab))

    lo_d = min(s.obs[0][0] for s in series_list)
    hi_d = max(s.obs[-1][0] for s in series_list)
    recessions = fetch_recessions(key, lo_d, hi_d) if args.recession else []

    freq = series_list[0].meta.get("frequency_short", "")
    period = args.period_label or {
        "M": "월간", "Q": "분기", "W": "주간", "D": "일간", "A": "연간",
    }.get(freq, "")
    years = (hi_d - lo_d).days / 365.25
    if args.period_label is None:
        period = f"최근 {years:.0f}년 {period}".strip()

    parts = []
    if args.emit in ("all", "chart"):
        parts.append(render_svg(
            series_list, args.title, period, args.unit_label, args.decimals,
            args.chart_type, ref_lines, recessions, args.include_zero,
        ))
    if args.emit in ("all", "table"):
        parts.append(render_table(series_list, args.unit_label, args.decimals))
    text = "\n\n".join(parts) + "\n"

    if args.out:
        Path(args.out).write_text(text)
        print(f"[완료] {args.out} ({len(series_list)}개 시리즈, {lo_d} ~ {hi_d})", file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
