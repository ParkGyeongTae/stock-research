# 미국 실업률 (U-3)

::: info
경제활동인구 가운데 일자리를 구하지 못한 사람의 비율이다(FRED `UNRATE`). 매달 가구조사(household survey)로 집계하며, 사업체 조사에 기반한 [비농업부문 고용 증감](./nonfarm_payrolls.md)과는 조사 방식 자체가 다르다.

:::
---

## 1. 차트 — 최근 5년 월간

<div class="fred-unrate">
<style>
.fred-unrate {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-unrate:#2a78d6;
}
@media (prefers-color-scheme: dark) {
  .dark .fred-unrate { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-unrate:#3987e5; }
}
.dark .fred-unrate { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-unrate:#3987e5; }
.fred-unrate svg { width:100%; height:auto; display:block; }
.fred-unrate text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-unrate .title { fill: var(--ink); font-weight:600; }
.fred-unrate .grid { stroke: var(--grid); stroke-width:1; }
.fred-unrate .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="실업률, 최근 5년 월간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 실업률 (U-3) (최근 5년 월간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-08-01 · 단위: % · 출처: FRED UNRATE</text>
<line x1="60" y1="526.4" x2="1052" y2="526.4" class="grid"/>
<text x="52" y="530.4" font-size="11" text-anchor="end" fill="var(--muted)">3.5</text>
<line x1="60" y1="346.0" x2="1052" y2="346.0" class="grid"/>
<text x="52" y="350.0" font-size="11" text-anchor="end" fill="var(--muted)">4.0</text>
<line x1="60" y1="165.7" x2="1052" y2="165.7" class="grid"/>
<text x="52" y="169.7" font-size="11" text-anchor="end" fill="var(--muted)">4.5</text>
<line x1="127.4" y1="56" x2="127.4" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="127.4" y1="600" x2="127.4" y2="605" class="axis"/>
<text x="127.4" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="329.1" y1="56" x2="329.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="329.1" y1="600" x2="329.1" y2="605" class="axis"/>
<text x="329.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="530.9" y1="56" x2="530.9" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="530.9" y1="600" x2="530.9" y2="605" class="axis"/>
<text x="530.9" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="733.1" y1="56" x2="733.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="733.1" y1="600" x2="733.1" y2="605" class="axis"/>
<text x="733.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="934.8" y1="56" x2="934.8" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="934.8" y1="600" x2="934.8" y2="605" class="axis"/>
<text x="934.8" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<polyline points="60.0,93.5 76.6,165.7 93.7,310.0 110.3,382.1 127.4,346.0 144.6,382.1 160.0,454.3 177.2,454.3 193.7,490.3 210.9,490.3 227.5,526.4 244.6,490.3 261.7,526.4 278.3,490.3 295.4,490.3 312.0,526.4 329.1,526.4 346.3,490.3 361.7,526.4 378.9,562.5 395.5,490.3 412.6,490.3 429.2,526.4 446.3,454.3 463.4,454.3 480.0,382.1 497.1,454.3 513.7,418.2 530.9,454.3 548.0,382.1 564.0,382.1 581.1,382.1 597.7,382.1 614.9,310.0 631.4,273.9 648.6,273.9 665.7,310.0 682.3,310.0 699.4,273.9 716.0,310.0 733.1,346.0 750.3,273.9 765.7,273.9 782.9,273.9 799.4,237.8 816.6,310.0 833.2,237.8 850.3,237.8 867.4,201.7" fill="none" stroke="var(--s-unrate)" stroke-width="2"/>
<polyline points="901.1,165.7 917.7,201.7 934.8,237.8 952.0,201.7 967.4,237.8 984.6,237.8 1001.2,237.8 1018.3,273.9 1034.9,310.0 1052.0,310.0" fill="none" stroke="var(--s-unrate)" stroke-width="2"/>
<text x="1058" y="314.0" font-size="11.5" font-weight="700" fill="var(--s-unrate)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">실업률 4.1%</text>
</svg>
</div>

<p style="font-size:0.85em;opacity:0.75;margin-top:0.4em">차트 중간이 끊긴 구간은 해당 월 발표가 없었다는 뜻이다 — 연방정부 셧다운으로 미 노동통계국(BLS)이 그달 지표를 공표하지 못해 FRED에도 결측으로 남아 있다. 없는 값을 직선으로 잇지 않고 그대로 비워 둔다.</p>

---

## 2. 해석

- **상승**: 노동시장이 식고 있다는 신호로 흔히 해석한다 — 고용이 줄면 가계 소득이 줄고 소비가 위축되므로 기업 매출에는 하방 요인이다. 다만 자산시장에서는 방향이 갈린다: 같은 숫자가 연준의 금리인하 기대를 키워 주가·채권가격에는 오히려 우호적으로 받아들여지는 국면이 반복해서 나타난다.
- **하락**: 노동시장이 탄탄하다는 신호로 흔히 해석한다 — 다만 지나치게 낮은 실업률은 임금 상승 압력을 통해 물가로 옮겨붙는다고 보아, 긴축이 길어질 근거로 읽히기도 한다.
- **왜 이런 신호로 읽히나**: U-3는 "최근 4주간 실제로 구직활동을 한 사람"만 실업자로 센다. 그래서 **구직을 아예 포기하면 실업자에서 빠져 실업률이 오히려 떨어진다** — 실업률 하락이 항상 좋은 뉴스는 아니라는 뜻이라, 경제활동참가율(participation rate)과 함께 봐야 방향을 오독하지 않는다.
- **한계**: 대표적인 후행지표다. 기업은 감원을 마지막에 하므로 실업률은 경기가 꺾인 뒤에야 오르고, 그래서 이 지표만으로 국면 전환을 미리 잡기는 어렵다. 저점 대비 상승폭으로 침체 진입을 판정하려는 경험칙(삼 법칙, Sahm Rule)이 쓰이지만 이 역시 과거 사이클에서 도출된 규칙이지 인과 법칙이 아니다.

---

*작성일: 2026-09-17*
