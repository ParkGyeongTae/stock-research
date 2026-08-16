# Robinhood Markets — 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [`09_technical.md`](./09_technical.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 Yahoo Finance 주봉 API에서 직접 수집했다(5년 주봉은 `04_metrics.md`가 다루는 범위 밖). 두 문서에서 겹치는 시점의 종가를 대조한 결과: 2026-08-14 종가 $95.56은 [`09_technical.md`](./09_technical.md)의 동일 시점 종가와 일치(같은 스크립트·같은 원자료 출처).
>
> ⚠️ **자연 클러스터가 희소한 종목**: Robinhood는 2021년 IPO 이후 5년간 주가 변동폭이 극단적으로 커서(최저 $6.81~최고 $153.86, 약 23배 차이) [Coinbase](../coinbase/10_technical_weekly.md)와 마찬가지로 스윙 고점이 ±2.5% 이내로 반복되는 경우가 드물다. 표준 파라미터(전후 4주·±2.5%)로는 현재가 위쪽에 터치 2회 이상인 저항선이 하나도 없었다 — 아래 R1·R2는 모두 터치 1회 강제 포함 예외다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="hood-chart">
<style>
.hood-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .hood-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .hood-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.hood-chart svg { width:100%; height:auto; display:block; }
.hood-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.hood-chart .title { fill: var(--ink); font-weight:600; }
.hood-chart .grid { stroke: var(--grid); stroke-width:1; }
.hood-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Robinhood(HOOD) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Robinhood (HOOD) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $95.56 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="554.8" x2="1052" y2="554.8" class="grid"/>
<text x="52" y="558.8" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="483.5" x2="1052" y2="483.5" class="grid"/>
<text x="52" y="487.5" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="412.2" x2="1052" y2="412.2" class="grid"/>
<text x="52" y="416.2" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="269.8" x2="1052" y2="269.8" class="grid"/>
<text x="52" y="273.8" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="198.5" x2="1052" y2="198.5" class="grid"/>
<text x="52" y="202.5" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="127.2" x2="1052" y2="127.2" class="grid"/>
<text x="52" y="131.2" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.6" y1="626.0" x2="137.6" y2="631.0" class="axis"/>
<text x="137.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="334.5" y1="626.0" x2="334.5" y2="631.0" class="axis"/>
<text x="334.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="531.4" y1="626.0" x2="531.4" y2="631.0" class="axis"/>
<text x="531.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="732.1" y1="626.0" x2="732.1" y2="631.0" class="axis"/>
<text x="732.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.9" y1="626.0" x2="928.9" y2="631.0" class="axis"/>
<text x="928.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="77.9" x2="1052" y2="77.9" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="80.9" font-size="10.5" fill="var(--muted)">$154 5년 최고(2025-10-06)</text>
<line x1="224.7" y1="56.0" x2="224.7" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="230.7" y="68.0" font-size="10.5" fill="var(--down)">2022-06-13 IPO 버블 붕괴 저점(고점 대비 -86.9%)</text>
<line x1="61.9" y1="440.5" x2="61.9" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="450.0" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="65.7" y1="444.3" x2="65.7" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="459.0" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="69.5" y1="458.1" x2="69.5" y2="478.1" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="461.1" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="73.3" y1="471.4" x2="73.3" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="471.6" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="77.0" y1="473.2" x2="77.0" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="475.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="80.8" y1="455.6" x2="80.8" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="466.0" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="84.6" y1="462.3" x2="84.6" y2="479.5" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="465.9" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="88.4" y1="473.4" x2="88.4" y2="482.6" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="477.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="92.2" y1="474.7" x2="92.2" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="479.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="96.0" y1="471.5" x2="96.0" y2="485.0" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="480.1" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="99.8" y1="482.6" x2="99.8" y2="504.9" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="484.4" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="103.5" y1="490.8" x2="103.5" y2="503.7" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="494.2" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="107.3" y1="490.0" x2="107.3" y2="505.8" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="494.0" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="111.1" y1="499.1" x2="111.1" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="499.5" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="114.9" y1="521.4" x2="114.9" y2="531.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="522.7" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="118.7" y1="525.2" x2="118.7" y2="549.4" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="525.9" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="122.5" y1="541.4" x2="122.5" y2="555.4" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="550.0" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="126.3" y1="554.0" x2="126.3" y2="565.2" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="555.8" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="130.0" y1="557.4" x2="130.0" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="558.7" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="133.8" y1="558.8" x2="133.8" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="558.9" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="137.6" y1="558.5" x2="137.6" y2="573.3" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="561.7" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="141.4" y1="564.7" x2="141.4" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="571.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="145.2" y1="572.7" x2="145.2" y2="580.5" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="572.9" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="149.0" y1="577.6" x2="149.0" y2="590.6" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="580.6" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="152.8" y1="571.4" x2="152.8" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="571.9" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="156.5" y1="571.7" x2="156.5" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="572.3" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="160.3" y1="575.9" x2="160.3" y2="584.5" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="579.3" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="164.1" y1="584.2" x2="164.1" y2="590.6" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="584.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="167.9" y1="582.3" x2="167.9" y2="587.3" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="585.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="171.7" y1="581.6" x2="171.7" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="586.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="175.5" y1="576.3" x2="175.5" y2="589.7" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="578.1" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="179.3" y1="576.6" x2="179.3" y2="582.3" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="578.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="183.1" y1="567.3" x2="183.1" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="577.9" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="186.8" y1="576.3" x2="186.8" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="577.9" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="190.6" y1="583.0" x2="190.6" y2="587.4" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="585.5" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="194.4" y1="584.6" x2="194.4" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="585.8" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="198.2" y1="587.6" x2="198.2" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="589.9" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="202.0" y1="586.9" x2="202.0" y2="592.1" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="589.9" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="205.8" y1="587.3" x2="205.8" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="587.9" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="209.6" y1="588.1" x2="209.6" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="588.1" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="213.3" y1="588.9" x2="213.3" y2="594.0" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="589.0" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="217.1" y1="588.4" x2="217.1" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="589.4" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="220.9" y1="591.1" x2="220.9" y2="598.9" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="593.0" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="224.7" y1="599.4" x2="224.7" y2="601.7" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="600.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="228.5" y1="596.1" x2="228.5" y2="600.1" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="597.5" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="232.3" y1="591.4" x2="232.3" y2="598.1" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="596.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="236.1" y1="593.0" x2="236.1" y2="598.3" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="593.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="239.8" y1="594.2" x2="239.8" y2="597.3" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="594.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="243.6" y1="592.2" x2="243.6" y2="595.5" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="593.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="247.4" y1="593.3" x2="247.4" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="593.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="251.2" y1="585.6" x2="251.2" y2="595.0" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="589.0" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="255.0" y1="585.8" x2="255.0" y2="590.4" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="587.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="258.8" y1="584.7" x2="258.8" y2="593.3" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="587.6" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="262.6" y1="590.5" x2="262.6" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="592.6" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="266.4" y1="590.9" x2="266.4" y2="594.0" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="592.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="270.1" y1="587.1" x2="270.1" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="588.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="273.9" y1="584.6" x2="273.9" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="587.7" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="277.7" y1="586.5" x2="277.7" y2="593.3" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="590.4" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="281.5" y1="588.7" x2="281.5" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="590.0" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="285.3" y1="586.2" x2="285.3" y2="591.4" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="587.5" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="289.1" y1="586.7" x2="289.1" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="587.5" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="292.9" y1="587.6" x2="292.9" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="589.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="296.6" y1="584.8" x2="296.6" y2="591.4" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="585.0" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="300.4" y1="580.5" x2="300.4" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="582.3" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="304.2" y1="581.3" x2="304.2" y2="596.5" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="581.8" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="308.0" y1="589.0" x2="308.0" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="590.4" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="311.8" y1="592.2" x2="311.8" y2="595.2" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="592.5" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="315.6" y1="590.1" x2="315.6" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="590.4" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="319.4" y1="589.8" x2="319.4" y2="593.4" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="590.4" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="323.1" y1="589.5" x2="323.1" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="592.5" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="326.9" y1="595.5" x2="326.9" y2="598.6" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="595.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="330.7" y1="596.9" x2="330.7" y2="599.0" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="597.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="334.5" y1="596.1" x2="334.5" y2="597.8" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="596.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="338.3" y1="592.4" x2="338.3" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="592.8" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="342.1" y1="591.4" x2="342.1" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="592.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="345.9" y1="588.4" x2="345.9" y2="592.8" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="589.0" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="349.6" y1="585.0" x2="349.6" y2="590.3" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="587.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="353.4" y1="586.2" x2="353.4" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="588.1" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="357.2" y1="587.1" x2="357.2" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="589.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="361.0" y1="589.3" x2="361.0" y2="592.3" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="589.9" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="364.8" y1="589.8" x2="364.8" y2="593.2" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="590.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="590.2" x2="368.6" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="590.6" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="372.4" y1="592.2" x2="372.4" y2="595.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="593.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="376.2" y1="592.5" x2="376.2" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="593.4" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="379.9" y1="591.3" x2="379.9" y2="595.6" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="591.4" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="383.7" y1="590.1" x2="383.7" y2="592.1" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="590.3" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="387.5" y1="589.7" x2="387.5" y2="591.6" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="590.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="391.3" y1="590.3" x2="391.3" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="590.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="395.1" y1="591.5" x2="395.1" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="591.7" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="398.9" y1="594.4" x2="398.9" y2="596.8" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="594.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="402.7" y1="590.5" x2="402.7" y2="595.0" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="594.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="406.4" y1="594.8" x2="406.4" y2="596.4" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="594.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="410.2" y1="594.4" x2="410.2" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="594.6" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="414.0" y1="592.7" x2="414.0" y2="594.9" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="592.7" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="417.8" y1="591.1" x2="417.8" y2="595.4" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="592.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="421.6" y1="589.6" x2="421.6" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="590.3" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="425.4" y1="590.2" x2="425.4" y2="593.6" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="590.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="429.2" y1="588.5" x2="429.2" y2="592.6" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="590.4" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="432.9" y1="587.1" x2="432.9" y2="590.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="587.6" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="436.7" y1="581.1" x2="436.7" y2="588.5" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="581.9" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="440.5" y1="578.9" x2="440.5" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="580.5" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="444.3" y1="579.9" x2="444.3" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="580.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="579.6" x2="448.1" y2="587.2" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="580.4" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="451.9" y1="585.0" x2="451.9" y2="588.3" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="585.7" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="455.7" y1="588.0" x2="455.7" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="588.0" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="459.5" y1="588.2" x2="459.5" y2="589.9" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="588.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="463.2" y1="585.5" x2="463.2" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="586.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="467.0" y1="586.7" x2="467.0" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="586.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="470.8" y1="586.8" x2="470.8" y2="588.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="587.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="474.6" y1="587.6" x2="474.6" y2="591.7" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="588.1" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="478.4" y1="590.3" x2="478.4" y2="592.4" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="591.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="482.2" y1="590.4" x2="482.2" y2="592.4" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="590.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="486.0" y1="589.7" x2="486.0" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="591.0" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="489.7" y1="591.7" x2="489.7" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="593.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="493.5" y1="591.8" x2="493.5" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="593.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="497.3" y1="591.1" x2="497.3" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="591.5" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="501.1" y1="590.9" x2="501.1" y2="597.8" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="591.2" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="504.9" y1="595.0" x2="504.9" y2="597.8" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="596.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="508.7" y1="596.4" x2="508.7" y2="597.6" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="596.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="512.5" y1="592.5" x2="512.5" y2="596.8" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="592.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="516.2" y1="584.2" x2="516.2" y2="592.8" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="584.2" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="520.0" y1="581.9" x2="520.0" y2="586.4" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="584.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="578.1" x2="523.8" y2="585.2" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="579.9" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="527.6" y1="577.9" x2="527.6" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="579.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="531.4" y1="580.6" x2="531.4" y2="584.9" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="580.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="535.2" y1="581.2" x2="535.2" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="583.4" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="539.0" y1="586.7" x2="539.0" y2="589.0" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="587.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="542.7" y1="585.7" x2="542.7" y2="588.2" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="587.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="546.5" y1="585.6" x2="546.5" y2="588.2" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="587.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="550.3" y1="584.7" x2="550.3" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="584.9" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="554.1" y1="574.9" x2="554.1" y2="585.3" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="576.1" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="557.9" y1="574.3" x2="557.9" y2="578.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="574.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="561.7" y1="566.9" x2="561.7" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="566.9" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="565.5" y1="563.2" x2="565.5" y2="570.2" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="565.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="569.3" y1="557.5" x2="569.3" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="561.3" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="573.0" y1="556.8" x2="573.0" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="560.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="576.8" y1="552.8" x2="576.8" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="554.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="580.6" y1="554.2" x2="580.6" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="554.8" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="584.4" y1="558.0" x2="584.4" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="558.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="588.2" y1="560.9" x2="588.2" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="561.6" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="592.0" y1="562.2" x2="592.0" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="562.3" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="595.8" y1="560.8" x2="595.8" y2="567.9" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="562.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="599.5" y1="556.6" x2="599.5" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="563.2" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="603.3" y1="553.5" x2="603.3" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="554.4" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="607.1" y1="550.4" x2="607.1" y2="558.1" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="552.9" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="610.9" y1="546.4" x2="610.9" y2="554.6" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="551.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="614.7" y1="541.6" x2="614.7" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="547.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="618.5" y1="539.5" x2="618.5" y2="547.4" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="546.1" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="622.3" y1="545.1" x2="622.3" y2="550.5" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="546.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="626.0" y1="542.9" x2="626.0" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="545.1" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="629.8" y1="543.6" x2="629.8" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="544.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="633.6" y1="543.1" x2="633.6" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="545.1" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="637.4" y1="537.4" x2="637.4" y2="545.3" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="542.6" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="641.2" y1="540.4" x2="641.2" y2="552.5" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="543.2" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="645.0" y1="548.2" x2="645.0" y2="563.0" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="549.2" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="648.8" y1="560.9" x2="648.8" y2="576.2" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="562.2" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="652.5" y1="554.5" x2="652.5" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="554.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="656.3" y1="550.4" x2="656.3" y2="556.5" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="550.8" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="660.1" y1="549.3" x2="660.1" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="550.8" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="663.9" y1="553.9" x2="663.9" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="555.6" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="667.7" y1="546.1" x2="667.7" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="547.4" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="671.5" y1="540.3" x2="671.5" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="545.0" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="675.3" y1="540.6" x2="675.3" y2="546.9" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="540.9" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="679.1" y1="540.0" x2="679.1" y2="547.4" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="540.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="682.8" y1="531.1" x2="682.8" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="532.4" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="686.6" y1="528.6" x2="686.6" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="530.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="690.4" y1="527.1" x2="690.4" y2="532.7" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="529.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="694.2" y1="524.2" x2="694.2" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="526.5" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="698.0" y1="516.9" x2="698.0" y2="542.1" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="517.2" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="701.8" y1="503.7" x2="701.8" y2="514.6" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="508.7" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="705.6" y1="490.2" x2="705.6" y2="508.8" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="495.4" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="709.3" y1="484.4" x2="709.3" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="486.3" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="713.1" y1="473.7" x2="713.1" y2="495.6" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="477.6" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="716.9" y1="476.1" x2="716.9" y2="499.1" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="478.5" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="720.7" y1="469.9" x2="720.7" y2="504.8" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="479.9" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="724.5" y1="481.8" x2="724.5" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="487.0" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="728.3" y1="478.6" x2="728.3" y2="494.1" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="478.7" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="732.1" y1="472.1" x2="732.1" y2="487.8" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="476.0" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="735.8" y1="450.5" x2="735.8" y2="489.1" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="454.5" width="2.35" height="32.6" fill="var(--up)"/>
<line x1="739.6" y1="440.5" x2="739.6" y2="454.5" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="443.9" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="743.4" y1="435.4" x2="743.4" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="440.9" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="747.2" y1="426.6" x2="747.2" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="427.0" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="751.0" y1="387.6" x2="751.0" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="393.4" width="2.35" height="28.9" fill="var(--up)"/>
<line x1="754.8" y1="392.4" x2="754.8" y2="442.7" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="393.7" width="2.35" height="48.5" fill="var(--down)"/>
<line x1="758.6" y1="437.4" x2="758.6" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="439.9" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="762.4" y1="430.6" x2="762.4" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="431.1" width="2.35" height="36.7" fill="var(--down)"/>
<line x1="766.1" y1="479.2" x2="766.1" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="480.2" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="769.9" y1="466.6" x2="769.9" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="468.0" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="773.7" y1="448.3" x2="773.7" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="460.7" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="777.5" y1="470.7" x2="777.5" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="484.3" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="781.3" y1="470.0" x2="781.3" y2="520.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="470.4" width="2.35" height="46.3" fill="var(--up)"/>
<line x1="785.1" y1="463.7" x2="785.1" y2="483.3" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="465.7" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="788.9" y1="447.9" x2="788.9" y2="486.3" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="449.8" width="2.35" height="31.1" fill="var(--up)"/>
<line x1="792.6" y1="443.2" x2="792.6" y2="461.5" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="446.0" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="796.4" y1="425.4" x2="796.4" y2="463.7" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="431.3" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="800.2" y1="398.8" x2="800.2" y2="426.9" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="406.0" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="804.0" y1="387.7" x2="804.0" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="401.0" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="807.8" y1="386.8" x2="807.8" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="390.3" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="811.6" y1="348.8" x2="811.6" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="359.2" width="2.35" height="31.5" fill="var(--up)"/>
<line x1="815.4" y1="356.7" x2="815.4" y2="381.8" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="367.4" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="819.1" y1="343.2" x2="819.1" y2="366.4" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="346.3" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="822.9" y1="321.2" x2="822.9" y2="361.0" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="330.2" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="826.7" y1="266.6" x2="826.7" y2="321.4" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="289.7" width="2.35" height="31.2" fill="var(--up)"/>
<line x1="830.5" y1="264.4" x2="830.5" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="275.7" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="834.3" y1="221.9" x2="834.3" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="235.1" width="2.35" height="31.6" fill="var(--up)"/>
<line x1="838.1" y1="233.0" x2="838.1" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="237.7" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="841.9" y1="237.5" x2="841.9" y2="293.4" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="248.9" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="845.6" y1="209.2" x2="845.6" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="217.6" width="2.35" height="47.7" fill="var(--up)"/>
<line x1="849.4" y1="206.7" x2="849.4" y2="247.3" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="212.0" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="853.2" y1="207.5" x2="853.2" y2="273.3" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="223.4" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="857.0" y1="234.7" x2="857.0" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="239.5" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="860.8" y1="248.3" x2="860.8" y2="285.2" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="265.3" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="864.6" y1="186.2" x2="864.6" y2="233.7" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="216.2" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="868.4" y1="180.0" x2="868.4" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="181.5" width="2.35" height="33.6" fill="var(--up)"/>
<line x1="872.2" y1="162.6" x2="872.2" y2="196.9" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="185.6" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="875.9" y1="90.9" x2="875.9" y2="185.0" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="96.4" width="2.35" height="88.7" fill="var(--up)"/>
<line x1="879.7" y1="77.9" x2="879.7" y2="131.0" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="80.9" width="2.35" height="50.0" fill="var(--down)"/>
<line x1="883.5" y1="103.9" x2="883.5" y2="178.6" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="110.8" width="2.35" height="52.4" fill="var(--down)"/>
<line x1="887.3" y1="119.4" x2="887.3" y2="195.4" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="128.0" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="891.1" y1="90.0" x2="891.1" y2="137.0" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="103.1" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="894.9" y1="93.7" x2="894.9" y2="196.0" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="95.9" width="2.35" height="65.7" fill="var(--down)"/>
<line x1="898.7" y1="130.8" x2="898.7" y2="219.9" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="143.5" width="2.35" height="46.1" fill="var(--down)"/>
<line x1="902.4" y1="189.1" x2="902.4" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="196.7" width="2.35" height="47.0" fill="var(--down)"/>
<line x1="906.2" y1="163.1" x2="906.2" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="168.3" width="2.35" height="66.2" fill="var(--up)"/>
<line x1="910.0" y1="136.7" x2="910.0" y2="202.6" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="155.9" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="913.8" y1="128.1" x2="913.8" y2="206.2" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="148.3" width="2.35" height="52.0" fill="var(--down)"/>
<line x1="917.6" y1="181.8" x2="917.6" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="193.7" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="921.4" y1="182.3" x2="921.4" y2="210.1" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="186.0" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="925.2" y1="202.2" x2="925.2" y2="232.7" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="209.6" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="928.9" y1="183.0" x2="928.9" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="205.9" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="932.7" y1="195.4" x2="932.7" y2="245.2" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="218.1" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="936.5" y1="228.9" x2="936.5" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="244.8" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="940.3" y1="237.5" x2="940.3" y2="275.6" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="247.4" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="944.1" y1="284.4" x2="944.1" y2="370.0" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="284.4" width="2.35" height="46.5" fill="var(--down)"/>
<line x1="947.9" y1="310.4" x2="947.9" y2="375.1" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="323.6" width="2.35" height="31.7" fill="var(--down)"/>
<line x1="951.7" y1="347.2" x2="951.7" y2="366.4" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="354.9" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="955.5" y1="342.5" x2="955.5" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="355.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="959.2" y1="324.1" x2="959.2" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="351.4" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="963.0" y1="338.3" x2="963.0" y2="366.7" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="355.5" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="966.8" y1="349.2" x2="966.8" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="358.5" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="970.6" y1="360.3" x2="970.6" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="370.0" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="974.4" y1="371.1" x2="974.4" y2="399.7" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="380.5" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="978.2" y1="348.6" x2="978.2" y2="388.7" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="379.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="982.0" y1="293.5" x2="982.0" y2="384.5" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="302.7" width="2.35" height="80.3" fill="var(--up)"/>
<line x1="985.7" y1="296.9" x2="985.7" y2="334.8" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="306.4" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="989.5" y1="320.7" x2="989.5" y2="376.9" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="325.8" width="2.35" height="37.8" fill="var(--down)"/>
<line x1="993.3" y1="342.8" x2="993.3" y2="361.5" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="351.6" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="997.1" y1="334.1" x2="997.1" y2="359.5" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="351.2" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="1000.9" y1="341.3" x2="1000.9" y2="365.3" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="355.2" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="1004.7" y1="289.7" x2="1004.7" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="290.1" width="2.35" height="70.6" fill="var(--up)"/>
<line x1="1008.5" y1="296.8" x2="1008.5" y2="342.8" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="305.6" width="2.35" height="26.6" fill="var(--down)"/>
<line x1="1012.2" y1="283.6" x2="1012.2" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="294.0" width="2.35" height="30.5" fill="var(--up)"/>
<line x1="1016.0" y1="231.5" x2="1016.0" y2="289.1" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="240.7" width="2.35" height="33.6" fill="var(--up)"/>
<line x1="1019.8" y1="225.2" x2="1019.8" y2="295.4" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="241.2" width="2.35" height="33.2" fill="var(--down)"/>
<line x1="1023.6" y1="198.3" x2="1023.6" y2="276.7" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="224.4" width="2.35" height="43.0" fill="var(--up)"/>
<line x1="1027.4" y1="200.5" x2="1027.4" y2="238.4" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="227.1" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="1031.2" y1="210.6" x2="1031.2" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="229.6" width="2.35" height="40.3" fill="var(--down)"/>
<line x1="1035.0" y1="240.5" x2="1035.0" y2="294.6" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="260.9" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="1038.7" y1="271.7" x2="1038.7" y2="327.9" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="280.5" width="2.35" height="37.1" fill="var(--down)"/>
<line x1="1042.5" y1="284.9" x2="1042.5" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="293.7" width="2.35" height="23.5" fill="var(--up)"/>
<line x1="1046.3" y1="268.5" x2="1046.3" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="285.6" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="1050.1" y1="275.4" x2="1050.1" y2="286.0" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="277.4" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="60" y1="198.3" x2="1052" y2="198.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="201.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$120 R1 (2026년 6월 스윙 고점)</text>
<text x="1058" y="213.8" font-size="9.5" fill="var(--muted)">터치 1회</text>
<line x1="60" y1="128.1" x2="1052" y2="128.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="131.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$140 R2 (2025년 12월 스윙 고점)</text>
<text x="1058" y="143.6" font-size="9.5" fill="var(--muted)">터치 1회</text>
<line x1="60" y1="590.8" x2="1052" y2="590.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="584.8" font-size="11.5" fill="var(--support)" font-weight="600">$9.89 S1</text>
<text x="1058" y="596.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="596.5" x2="1052" y2="596.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="590.5" font-size="11.5" fill="var(--support)" font-weight="600">$8.29 S2</text>
<text x="1058" y="602.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="285.6" r="3" fill="var(--ink)"/>
<rect x="60" y="651" width="10" height="10" fill="var(--up)"/>
<text x="74" y="660" font-size="11" fill="var(--ink2)">상승(양봉)</text>
<rect x="150" y="651" width="10" height="10" fill="var(--down)"/>
<text x="164" y="660" font-size="11" fill="var(--ink2)">하락(음봉)</text>
<line x1="240" y1="656" x2="258" y2="656" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="264" y="660" font-size="11" fill="var(--ink2)">지지선(Support)</text>
<line x1="390" y1="656" x2="408" y2="656" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="414" y="660" font-size="11" fill="var(--ink2)">저항선(Resistance)</text>
</svg>
</div>

---

## 2. 지지선 / 저항선 요약

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고). `09_technical.md`의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다 — 둘을 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $140 | 1 | 2025년 12월(2025-12-08) 스윙 고점. 터치 1회지만 R1과 함께 최근 레인지 상단을 보여줘 예외 포함 |
| R1 | $120 | 1 | 2026년 6월(2026-06-29) 스윙 고점 — 터치 1회지만 가장 최근 레짐의 저항으로 참고 |
| **현재가** | **$95.56** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $9.89 | 2 | 2022년 2월·2023년 2월(2022-02-21·2023-02-06) 반복 저점대 |
| S2 | $8.29 | 3 | 2022년 11월~2023년 5월(2022-11-07·2023-03-20·2023-05-01)에 걸쳐 3회 반복된 저점대 — §3의 IPO 버블 붕괴 저점과 같은 국면에 형성됨 |
| 참고선 | $154 | — | 5년 최고(2025-10-06). 이후 조정을 거쳐 §3와 무관한 최근 레인지($95~140대)를 형성 중이라 근시일 저항으로 보지 않음 |

> 표시 기준은 "현재가에서 가까운 순으로 각 방향 3개"다(§4 생성 스크립트 기본값). 상단 경고에서 밝혔듯 저항 쪽 자연 클러스터가 전혀 없어 R1·R2 모두 `--force-level`로 강제 포함한 예외다.

---

## 3. 관측된 특이 구간 — 2022-06-13 IPO 버블 붕괴 저점

- 2021-07-29 나스닥 상장(공모가 $38) 직후 GameStop발 밈주식 열풍에 편승해 급등했다가, 이 5년 데이터 구간이 시작되는 2021-08-16 주간 고점 $52.06(상장 초기 열기가 아직 남아있던 구간, 실제 상장 직후 고점은 이보다 높았을 수 있음)에서 2022-06-13 주간 저점 $6.81까지 약 10개월간 **-86.9%** 폭락했다(주간 종가 기준이 아닌 고가·저가 기준). 2022년 전반적인 금리인상기 성장주 조정에 더해, 밈주식 열기 자체의 급격한 냉각과 회사 고유의 성장 서사 훼손이 겹친 결과로 해석된다.
- 이후 회복은 매우 더뎠다 — 2022-06-13 저점 형성 후 상장 초기 고점($52.06)을 다시 상회하기까지 약 2.6년(2025-02-03)이 걸렸다. [Coinbase](../coinbase/10_technical_weekly.md)의 2023년 크립토 겨울(−91.4%, 회복까지 약 2.5년)과 낙폭·회복 기간 모두 매우 유사한 패턴이다 — 두 종목 모두 2021년 상장·급등 후 2022년 극단적 조정, 2025년 전후 뒤늦은 완전 회복이라는 공통된 사이클을 거쳤다.
- 이 폭락·회복 사이클은 특정 분기 실적 이벤트라기보다 밈주식·성장주 밸류에이션 재조정이라는 시장 전반의 구조적 변화에 가깝다 — `07_investment.md`가 짚는 "밸류에이션 방법론 간 괴리가 유독 크다"는 리스크와 함께, 이 종목의 가격이 펀더멘털만으로 설명되지 않는 구간이 반복돼왔음을 보여주는 역사적 사례로 볼 수 있다. `09_technical.md` §3의 최근 이벤트(회사 고유·단기)와는 시점·원인이 다르므로 혼동하지 말 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영) — Robinhood는 이 구간 내 주식분할 이력이 없다(`04_metrics.md` 상단 각주·`09_technical.md` §4와 동일 확인). 무배당 기업이라 배당 관련 조정 이슈 자체가 없다(`04_metrics.md` A.4).
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. `09_technical.md`(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py HOOD --name Robinhood --interval 1wk --ref-line 153.86:"5년 최고(2025-10-06)" --force-level '120.05:(2026년 6월 스윙 고점)' --force-level '139.75:(2025년 12월 스윙 고점)' --event '2022-06-13:IPO 버블 붕괴 저점(고점 대비 -86.9%)' --close-on 2026-08-13 --close-on 2026-08-14`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **이 종목도 Coinbase와 마찬가지로 방법론의 한계가 두드러진다** — 위 상단 경고대로 저항 쪽 자연 클러스터가 전무해 R1·R2 모두 강제 포함 예외다. 지지/저항 레벨을 다른 회사 문서와 같은 신뢰도로 취급하지 말 것.
    - `09_technical.md` §3의 최근 이벤트처럼 뉴스 이벤트로 인한 불연속 구간은 통상적인 지지/저항 해석이 적용되기 어렵다.

---

## 관련 문서

같은 폴더 내 다른 문서로 이동 (없는 문서는 링크 제거):

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 일봉·1년](./09_technical.md)

---

## 참고 자료

- [Yahoo Finance — HOOD Chart API](https://query1.finance.yahoo.com/v8/finance/chart/HOOD) (주봉 OHLCV 원자료, 2026-08-16 수집)
- [stockanalysis.com — HOOD Price History](https://stockanalysis.com/stocks/hood/history/)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-16)*
