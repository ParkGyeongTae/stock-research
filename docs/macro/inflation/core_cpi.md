# 미국 근원 소비자물가 상승률 (Core CPI)

::: info
[CPI](./cpi.md) 바스켓에서 변동성이 큰 에너지와 식품을 제외하고 산출한 전년동월비 상승률이다(FRED `CPILFESL`). 헤드라인이 유가에 흔들릴 때 기조적 물가 흐름을 가려내기 위한 지표다.

:::
---

## 1. 차트 — 최근 5년 월간

<div class="fred-cpilfesl">
<style>
.fred-cpilfesl {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-cpilfesl:#eb6834;
}
@media (prefers-color-scheme: dark) {
  .dark .fred-cpilfesl { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-cpilfesl:#d95926; }
}
.dark .fred-cpilfesl { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-cpilfesl:#d95926; }
.fred-cpilfesl svg { width:100%; height:auto; display:block; }
.fred-cpilfesl text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-cpilfesl .title { fill: var(--ink); font-weight:600; }
.fred-cpilfesl .grid { stroke: var(--grid); stroke-width:1; }
.fred-cpilfesl .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Core CPI, 최근 5년 월간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 근원 소비자물가 상승률 (Core CPI, 전년동월비) (최근 5년 월간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-08-01 · 단위: % · 출처: FRED CPILFESL</text>
<line x1="60" y1="562.5" x2="1052" y2="562.5" class="grid"/>
<text x="52" y="566.5" font-size="11" text-anchor="end" fill="var(--muted)">2.0</text>
<line x1="60" y1="461.1" x2="1052" y2="461.1" class="grid"/>
<text x="52" y="465.1" font-size="11" text-anchor="end" fill="var(--muted)">3.0</text>
<line x1="60" y1="359.7" x2="1052" y2="359.7" class="grid"/>
<text x="52" y="363.7" font-size="11" text-anchor="end" fill="var(--muted)">4.0</text>
<line x1="60" y1="258.2" x2="1052" y2="258.2" class="grid"/>
<text x="52" y="262.2" font-size="11" text-anchor="end" fill="var(--muted)">5.0</text>
<line x1="60" y1="156.8" x2="1052" y2="156.8" class="grid"/>
<text x="52" y="160.8" font-size="11" text-anchor="end" fill="var(--muted)">6.0</text>
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
<polyline points="60.0,359.4 76.6,299.8 93.7,261.0 110.3,208.7 127.4,151.3 144.6,110.7 160.0,107.9 177.2,140.7 193.7,154.2 210.9,166.3 227.5,167.0 244.6,127.8 261.7,93.5 278.3,126.9 295.4,159.9 312.0,188.7 329.1,203.5 346.3,207.7 361.7,200.8 378.9,206.1 395.5,224.0 412.6,273.1 429.2,288.6 446.3,319.2 463.4,346.6 480.0,356.9 497.1,357.8 513.7,368.2 530.9,374.0 548.0,383.8 564.0,378.3 581.1,397.6 597.7,421.1 614.9,434.2 631.4,437.7 648.6,432.2 665.7,432.4 682.3,430.8 699.4,432.1 716.0,439.4 733.1,432.4 750.3,447.1 765.7,480.5 782.9,483.8 799.4,484.8 816.6,470.1 833.2,455.5 850.3,449.7 867.4,459.0" fill="none" stroke="var(--s-cpilfesl)" stroke-width="2"/>
<polyline points="901.1,501.7 917.7,496.9 934.8,510.6 952.0,514.6 967.4,501.4 984.6,487.1 1001.2,479.0 1018.3,505.1 1034.9,515.2 1052.0,517.2" fill="none" stroke="var(--s-cpilfesl)" stroke-width="2"/>
<text x="1058" y="521.2" font-size="11.5" font-weight="700" fill="var(--s-cpilfesl)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">Core CPI 2.4%</text>
</svg>
</div>

<p style="font-size:0.85em;opacity:0.75;margin-top:0.4em">차트 중간이 끊긴 구간은 해당 월 발표가 없었다는 뜻이다 — 연방정부 셧다운으로 미 노동통계국(BLS)이 그달 지표를 공표하지 못해 FRED에도 결측으로 남아 있다. 없는 값을 직선으로 잇지 않고 그대로 비워 둔다.</p>

---

## 2. 해석

- **상승**: 에너지·식품 같은 일시적 요인이 아니라 **물가 압력이 경제 전반에 퍼져 있다**는 신호로 흔히 해석한다 — 헤드라인 상승보다 통화정책에 더 무겁게 받아들여진다.
- **하락**: 기조적 물가 압력이 실제로 꺾이고 있다는 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 에너지·식품은 공급 충격(전쟁·기후·감산)으로 튀었다가 되돌아오는 경우가 많아, 여기에 반응해 금리를 움직이면 정책이 잡음을 좇게 된다. 그래서 중앙은행은 "빼고 본 물가"를 기조 판단의 기준으로 삼는다 — 근원 물가를 중시하는 것이 식비·기름값이 중요하지 않다는 뜻은 아니다.
- **한계**: 에너지·식품을 빼면 남는 항목에서 **주거비 비중이 헤드라인보다 더 커지므로**, 주거비가 시장 임대료를 늦게 반영하는 시차 문제가 오히려 증폭된다. 또 가계가 체감하는 생활물가와의 괴리가 커서, 이 지표만으로 "물가가 잡혔다"고 말하면 체감과 어긋나기 쉽다.

---

*작성일: 2026-09-17*
