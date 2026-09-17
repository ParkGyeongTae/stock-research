# 미국 소비자물가 상승률 (CPI)

::: info
도시 소비자가 사는 상품·서비스 묶음의 가격을 지수로 만든 뒤, 1년 전 같은 달과 비교한 상승률이다(FRED `CPIAUCSL`). 물가 이야기에서 가장 널리 인용되는 헤드라인 지표다. 에너지·식품을 뺀 기조는 [Core CPI](./core_cpi.md)가, 연준이 실제 목표를 매기는 지표는 [Core PCE](./core_pce.md)가 따로 있으며 셋의 차이는 [물가지표 3종 비교](./comparison.md)에서 본다.
:::

---

## 1. 차트 — 최근 5년 월간

<style>
.fred-cpiaucsl {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-cpiaucsl:#2a78d6;
}
.dark .fred-cpiaucsl { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-cpiaucsl:#3987e5; }
.fred-cpiaucsl svg { width:100%; height:auto; display:block; }
.fred-cpiaucsl text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-cpiaucsl .title { fill: var(--ink); font-weight:600; }
.fred-cpiaucsl .grid { stroke: var(--grid); stroke-width:1; }
.fred-cpiaucsl .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-cpiaucsl">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CPI, 최근 5년 월간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 소비자물가 상승률 (CPI, 전년동월비) (최근 5년 월간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-08-01 · 단위: % · 출처: FRED CPIAUCSL</text>
<line x1="60" y1="562.5" x2="1052" y2="562.5" class="grid"/>
<text x="52" y="566.5" font-size="11" text-anchor="end" fill="var(--muted)">2.0</text>
<line x1="60" y1="428.1" x2="1052" y2="428.1" class="grid"/>
<text x="52" y="432.1" font-size="11" text-anchor="end" fill="var(--muted)">4.0</text>
<line x1="60" y1="293.7" x2="1052" y2="293.7" class="grid"/>
<text x="52" y="297.7" font-size="11" text-anchor="end" fill="var(--muted)">6.0</text>
<line x1="60" y1="159.3" x2="1052" y2="159.3" class="grid"/>
<text x="52" y="163.3" font-size="11" text-anchor="end" fill="var(--muted)">8.0</text>
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
<line x1="60" y1="562.5" x2="1052" y2="562.5" stroke="var(--base)" stroke-width="1.2" stroke-dasharray="5,3" opacity="0.85"/>
<text x="66" y="557.5" font-size="10.5" fill="var(--muted)">연준 물가목표 2%</text>
<polyline points="60.0,337.3 76.6,277.9 93.7,233.1 110.3,214.8 127.4,189.0 144.6,163.5 160.0,120.9 177.2,143.8 193.7,123.2 210.9,93.5 227.5,128.2 244.6,144.4 261.7,146.4 278.3,175.5 295.4,218.3 312.0,266.5 329.1,271.7 346.3,296.5 361.7,366.4 378.9,364.3 395.5,419.2 412.6,490.5 429.2,476.0 446.3,446.7 463.4,449.1 480.0,478.4 497.1,486.3 513.7,474.1 530.9,489.4 548.0,484.7 564.0,462.6 581.1,471.0 597.7,478.9 614.9,497.3 631.4,499.2 648.6,521.7 665.7,533.8 682.3,523.6 699.4,514.1 716.0,504.0 733.1,495.9 750.3,508.6 765.7,536.8 782.9,540.6 799.4,537.1 816.6,516.8 833.2,512.6 850.3,499.4 867.4,493.8" fill="none" stroke="var(--s-cpiaucsl)" stroke-width="2"/>
<polyline points="901.1,515.7 917.7,518.6 934.8,536.2 952.0,533.3 967.4,476.1 984.6,442.9 1001.2,416.9 1018.3,464.1 1034.9,474.9 1052.0,471.6" fill="none" stroke="var(--s-cpiaucsl)" stroke-width="2"/>
<text x="1058" y="475.6" font-size="11.5" font-weight="700" fill="var(--s-cpiaucsl)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">CPI 3.4%</text>
</svg>
</div>

---

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **한 줄로**: 장바구니 전체의 가격이 1년 전보다 몇 % 올랐는지를 나타낸 숫자다.
- **오르면**: 구매력이 깎이고 있다는 뜻이며, 금리를 높게 유지하거나 더 올릴 근거로 흔히 해석한다 — 할인율이 오르면 먼 미래 현금흐름 비중이 큰 성장주에 특히 큰 하방 압력이다.
- **내리면**: 물가 압력이 누그러졌다는 뜻으로 금리인하 여지를 넓히는 신호로 흔히 해석한다. 다만 수요가 무너져 내려가는 것이라면 같은 하락이 경기 둔화 신호가 된다 — 원인을 함께 본다.
- **전년동월비에는 기저효과가 따라붙는다**: 12개월 전 값과 비교한 수치라, 비교 대상인 작년 숫자가 유난히 높거나 낮으면 올해 물가가 그대로여도 상승률이 움직인다. 급변 구간의 원인을 볼 때는 전월비를 연율로 환산한 값을 함께 확인하는 편이 낫다.
- **기조를 보기엔 잡음이 많다**: 유가·농산물에 크게 흔들린다. 또 바스켓의 3분의 1가량을 차지하는 주거비(shelter)는 계약 갱신 주기 탓에 시장 임대료를 1년 안팎 늦게 반영해, 실제 전환점보다 지수가 늦게 돌아서는 구조적 시차가 있다.
- **나중에 고쳐진다**: FRED가 주는 값은 항상 최신 수정본이라, 같은 차트를 몇 달 뒤 다시 그리면 과거 구간까지 달라져 있을 수 있다. 계절조정 계수는 매년 갱신되고 원자료 개정도 소급 반영된다.
- **차트의 회색 음영과 점선**: 음영은 NBER이 사후에 판정한 침체 국면, 가로 점선은 연준의 물가목표 2%다. 목표선은 정책 판단의 기준점이지 도달해야 하는 상한선이 아니다.

---

*작성일: 2026-09-18*
