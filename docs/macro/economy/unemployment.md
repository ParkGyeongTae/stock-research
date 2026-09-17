# 미국 실업률 (U-3)

::: info
일할 의사가 있는 사람(경제활동인구) 가운데 일자리를 구하지 못한 사람의 비율이다(FRED `UNRATE`). 매달 가구를 상대로 한 설문(가구조사)으로 집계하며, 사업체의 급여대장에서 뽑는 [비농업부문 고용 증감](./nonfarm_payrolls.md)과는 조사 대상 자체가 다르다.
:::

---

## 1. 차트 — 최근 5년 월간

<style>
.fred-unrate {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-unrate:#2a78d6;
}
.dark .fred-unrate { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-unrate:#3987e5; }
.fred-unrate svg { width:100%; height:auto; display:block; }
.fred-unrate text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-unrate .title { fill: var(--ink); font-weight:600; }
.fred-unrate .grid { stroke: var(--grid); stroke-width:1; }
.fred-unrate .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-unrate">
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

---

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **한 줄로**: 노동시장의 온도를 재는 가장 널리 쓰이는 숫자이지만, **경기보다 늦게 움직인다**.
- **오르면**: 노동시장이 식고 있다는 신호로 흔히 해석한다. 가계 소득과 소비에는 하방 요인이다. 다만 자산시장에서는 같은 숫자가 금리인하 기대를 키워 주가·채권에 우호적으로 받아들여지는 국면이 반복된다.
- **내리면**: 노동시장이 탄탄하다는 신호로 흔히 해석한다. 지나치게 낮은 실업률은 임금 상승을 통해 물가로 옮겨붙는다고 보아 긴축이 길어질 근거로 읽히기도 한다.
- **하락이 항상 좋은 뉴스는 아니다**: U-3는 "최근 4주간 실제로 구직활동을 한 사람"만 실업자로 센다. 구직을 아예 포기하면 실업자에서 빠져 실업률이 오히려 내려간다 — 경제활동참가율을 함께 봐야 방향을 오독하지 않는다.
- **후행지표라는 한계**: 기업은 감원을 마지막에 하므로 실업률은 경기가 꺾인 뒤에야 오른다. 저점 대비 상승폭으로 침체를 판정하는 경험칙(삼 법칙, Sahm Rule)이 쓰이지만 과거 사이클에서 나온 규칙이지 인과 법칙은 아니다.
- **경제지표는 나중에 고쳐진다**: FRED가 주는 값은 항상 최신 수정본이라, 같은 차트를 몇 달 뒤 다시 그리면 과거 구간까지 조용히 달라져 있을 수 있다. 차트가 기억과 다르다면 오류가 아니라 개정(revision)일 가능성이 크다.
- **차트의 회색 음영**: 전미경제연구소(NBER)가 사후에 판정한 미국의 침체 국면이다. 실시간 신호가 아니라 나중에 붙는 라벨이라, 음영이 없다고 해서 그 시점에 침체가 아니었다고 단정할 수 없다.

---

*작성일: 2026-09-18*
