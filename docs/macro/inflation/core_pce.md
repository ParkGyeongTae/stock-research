# 미국 근원 개인소비지출 물가 상승률 (Core PCE)

::: info
개인소비지출(PCE) 물가지수에서 에너지·식품을 제외한 전년동월비 상승률이다(FRED `PCEPILFE`). **연준이 2% 물가안정 목표를 매기는 기준 지표가 바로 이것**이라, 정책 방향을 가늠할 때는 [CPI](./cpi.md)보다 이쪽을 본다.

:::
---

## 1. 차트 — 최근 5년 월간

<style>
.fred-pcepilfe {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-pcepilfe:#1baf7a;
}
.dark .fred-pcepilfe { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-pcepilfe:#199e70; }
.fred-pcepilfe svg { width:100%; height:auto; display:block; }
.fred-pcepilfe text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-pcepilfe .title { fill: var(--ink); font-weight:600; }
.fred-pcepilfe .grid { stroke: var(--grid); stroke-width:1; }
.fred-pcepilfe .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-pcepilfe">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Core PCE, 최근 5년 월간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 근원 개인소비지출 물가 상승률 (Core PCE, 전년동월비) (최근 5년 월간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-07-01 · 단위: % · 출처: FRED PCEPILFE</text>
<line x1="60" y1="562.5" x2="1052" y2="562.5" class="grid"/>
<text x="52" y="566.5" font-size="11" text-anchor="end" fill="var(--muted)">2.0</text>
<line x1="60" y1="432.4" x2="1052" y2="432.4" class="grid"/>
<text x="52" y="436.4" font-size="11" text-anchor="end" fill="var(--muted)">3.0</text>
<line x1="60" y1="302.4" x2="1052" y2="302.4" class="grid"/>
<text x="52" y="306.4" font-size="11" text-anchor="end" fill="var(--muted)">4.0</text>
<line x1="60" y1="172.4" x2="1052" y2="172.4" class="grid"/>
<text x="52" y="176.4" font-size="11" text-anchor="end" fill="var(--muted)">5.0</text>
<line x1="128.6" y1="56" x2="128.6" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="128.6" y1="600" x2="128.6" y2="605" class="axis"/>
<text x="128.6" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="333.9" y1="56" x2="333.9" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="333.9" y1="600" x2="333.9" y2="605" class="axis"/>
<text x="333.9" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="539.1" y1="56" x2="539.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="539.1" y1="600" x2="539.1" y2="605" class="axis"/>
<text x="539.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="745.0" y1="56" x2="745.0" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="745.0" y1="600" x2="745.0" y2="605" class="axis"/>
<text x="745.0" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="950.2" y1="56" x2="950.2" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="950.2" y1="600" x2="950.2" y2="605" class="axis"/>
<text x="950.2" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<line x1="60" y1="562.5" x2="1052" y2="562.5" stroke="var(--base)" stroke-width="1.2" stroke-dasharray="5,3" opacity="0.85"/>
<text x="66" y="557.5" font-size="10.5" fill="var(--muted)">연준 물가목표 2%</text>
<polyline points="60.0,300.6 76.9,245.6 94.3,186.6 111.2,144.5 128.6,125.8 146.0,94.0 161.8,95.2 179.2,127.5 196.1,148.4 213.5,131.3 230.4,158.4 247.8,125.2 265.3,93.5 282.1,112.6 299.6,145.3 316.4,176.7 333.9,180.5 351.3,191.2 367.0,200.6 384.5,199.7 401.4,207.3 418.8,252.5 435.7,263.5 453.1,324.8 470.5,343.0 487.4,370.8 504.8,394.6 521.7,417.8 539.1,411.8 556.6,424.7 572.9,416.6 590.3,431.6 607.2,462.2 624.6,464.5 641.5,457.6 658.9,448.9 676.3,453.4 693.2,434.2 710.6,435.0 727.5,433.9 745.0,461.0 762.4,436.5 778.1,475.3 795.6,482.5 812.4,460.6 829.9,457.5 846.7,450.3 864.2,443.8 881.6,455.2 898.5,464.4 915.9,454.7 932.8,436.2 950.2,418.8 967.6,426.0 983.4,399.4 1000.8,389.6 1017.7,372.2 1035.1,387.8 1052.0,387.7" fill="none" stroke="var(--s-pcepilfe)" stroke-width="2"/>
<text x="1058" y="391.7" font-size="11.5" font-weight="700" fill="var(--s-pcepilfe)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">Core PCE 3.3%</text>
</svg>
</div>

---

## 2. 해석

- **상승**: 연준의 목표에서 멀어지고 있다는 뜻으로, 긴축을 유지하거나 강화할 근거로 흔히 해석한다.
- **하락**: 목표에 가까워지고 있다는 뜻으로, 금리인하 경로를 여는 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 같은 물가인데 CPI와 다른 숫자가 나오는 이유는 셋이다. ① **가중치 산출 방식** — PCE는 실제 지출액 비중을 매 분기 갱신해 소비자가 비싼 품목을 싼 품목으로 갈아타는 대체효과를 반영하지만, CPI는 상대적으로 고정된 바스켓을 쓴다. ② **포함 범위** — PCE에는 고용주가 내는 건강보험료나 정부가 부담하는 의료비처럼 **가계가 직접 지불하지 않는 지출**까지 들어간다. ③ 그 결과 의료비 비중이 CPI보다 크고 주거비 비중은 작다. 이 차이 때문에 **Core PCE는 통상 Core CPI보다 낮게 나오는 경향**이 있어, 두 숫자를 같은 잣대로 비교하면 안 된다.
- **한계**: CPI보다 발표가 늦어 속보성이 떨어지고, 소매판매·CPI·PPI 등 다른 통계를 재료로 만들기 때문에 그 원자료가 개정되면 함께 소급 수정된다.

---

*작성일: 2026-09-17*
