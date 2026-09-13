# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 최근 1년 구조는 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-11 종가 $152.31**(Yahoo Finance)는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)가 인용한 stockanalysis.com 기준과 **정확히 일치**한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (`2021-09-13` ~ `2026-09-11`)

<div class="leu-chart">
<style>
.leu-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .leu-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .leu-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.leu-chart svg { width:100%; height:auto; display:block; }
.leu-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.leu-chart .title { fill: var(--ink); font-weight:600; }
.leu-chart .grid { stroke: var(--grid); stroke-width:1; }
.leu-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Centrus Energy(LEU) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Centrus Energy (LEU) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $152.31 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="507.2" x2="1052" y2="507.2" class="grid"/>
<text x="52" y="511.2" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="388.5" x2="1052" y2="388.5" class="grid"/>
<text x="52" y="392.5" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="269.8" x2="1052" y2="269.8" class="grid"/>
<text x="52" y="273.8" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="151.0" x2="1052" y2="151.0" class="grid"/>
<text x="52" y="155.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.5" y1="56.0" x2="122.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.5" y1="626.0" x2="122.5" y2="631.0" class="axis"/>
<text x="122.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="319.4" y1="56.0" x2="319.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="319.4" y1="626.0" x2="319.4" y2="631.0" class="axis"/>
<text x="319.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="516.2" y1="56.0" x2="516.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="516.2" y1="626.0" x2="516.2" y2="631.0" class="axis"/>
<text x="516.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.9" y1="56.0" x2="716.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.9" y1="626.0" x2="716.9" y2="631.0" class="axis"/>
<text x="716.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.8" y1="56.0" x2="913.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.8" y1="626.0" x2="913.8" y2="631.0" class="axis"/>
<text x="913.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="578.6" x2="61.9" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="582.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="582.6" x2="65.7" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="583.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="69.5" y1="576.5" x2="69.5" y2="583.5" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="576.9" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="73.3" y1="576.3" x2="73.3" y2="582.6" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="576.9" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="77.0" y1="561.0" x2="77.0" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="567.3" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="80.8" y1="557.4" x2="80.8" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="566.7" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="84.6" y1="558.7" x2="84.6" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="558.7" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="88.4" y1="531.9" x2="88.4" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="549.8" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="92.2" y1="520.5" x2="92.2" y2="548.4" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="524.4" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="96.0" y1="522.1" x2="96.0" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="528.4" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="99.8" y1="547.0" x2="99.8" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="551.7" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="103.5" y1="550.7" x2="103.5" y2="569.5" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="554.5" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="107.3" y1="553.4" x2="107.3" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="557.2" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="111.1" y1="557.4" x2="111.1" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="557.6" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="114.9" y1="560.1" x2="114.9" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="562.0" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="118.7" y1="561.4" x2="118.7" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="562.0" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="122.5" y1="557.5" x2="122.5" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="564.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="126.3" y1="563.7" x2="126.3" y2="572.9" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="564.1" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="130.0" y1="570.7" x2="130.0" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="572.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="133.8" y1="570.7" x2="133.8" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="578.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="137.6" y1="572.3" x2="137.6" y2="579.6" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="575.9" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="141.4" y1="567.9" x2="141.4" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="573.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="145.2" y1="571.4" x2="145.2" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="573.7" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="149.0" y1="577.2" x2="149.0" y2="585.2" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="577.6" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="152.8" y1="569.8" x2="152.8" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="577.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="156.5" y1="559.8" x2="156.5" y2="579.3" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="576.5" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="160.3" y1="579.3" x2="160.3" y2="591.3" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="579.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="164.1" y1="579.1" x2="164.1" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="582.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="167.9" y1="582.9" x2="167.9" y2="588.9" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="584.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="171.7" y1="584.1" x2="171.7" y2="591.4" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="586.3" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="175.5" y1="587.3" x2="175.5" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="587.4" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="179.3" y1="582.4" x2="179.3" y2="591.1" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="586.8" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="183.1" y1="589.7" x2="183.1" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="591.4" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="186.8" y1="589.7" x2="186.8" y2="601.9" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="593.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="190.6" y1="595.1" x2="190.6" y2="605.4" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="595.1" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="194.4" y1="595.1" x2="194.4" y2="601.0" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="598.0" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="198.2" y1="595.3" x2="198.2" y2="599.9" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="595.6" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="202.0" y1="592.6" x2="202.0" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="594.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="205.8" y1="584.5" x2="205.8" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="590.2" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="209.6" y1="590.5" x2="209.6" y2="596.4" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="592.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="213.3" y1="590.8" x2="213.3" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="591.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="217.1" y1="589.9" x2="217.1" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="591.4" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="220.9" y1="592.4" x2="220.9" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="593.2" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="224.7" y1="592.2" x2="224.7" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="592.8" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="228.5" y1="588.5" x2="228.5" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="592.0" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="232.3" y1="586.2" x2="232.3" y2="594.2" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="586.6" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="236.1" y1="579.7" x2="236.1" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="579.9" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="239.8" y1="571.4" x2="239.8" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="574.3" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="243.6" y1="574.3" x2="243.6" y2="582.4" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="574.3" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="247.4" y1="569.7" x2="247.4" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="574.8" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="251.2" y1="563.7" x2="251.2" y2="576.1" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="569.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="255.0" y1="560.7" x2="255.0" y2="571.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="561.2" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="258.8" y1="560.0" x2="258.8" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="560.5" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="262.6" y1="572.0" x2="262.6" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="573.5" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="266.4" y1="574.4" x2="266.4" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="577.3" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="270.1" y1="573.6" x2="270.1" y2="580.5" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="576.1" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="273.9" y1="579.1" x2="273.9" y2="585.9" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="579.2" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="277.7" y1="575.1" x2="277.7" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="575.2" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="281.5" y1="570.1" x2="281.5" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="570.1" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="285.3" y1="568.7" x2="285.3" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="569.5" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="289.1" y1="570.2" x2="289.1" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="574.1" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="292.9" y1="576.5" x2="292.9" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="579.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="296.6" y1="579.6" x2="296.6" y2="582.5" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="580.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="300.4" y1="579.8" x2="300.4" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="580.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="304.2" y1="580.3" x2="304.2" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="580.7" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="308.0" y1="583.5" x2="308.0" y2="587.4" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="586.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="311.8" y1="586.2" x2="311.8" y2="589.4" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="586.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="315.6" y1="586.6" x2="315.6" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="587.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="319.4" y1="584.7" x2="319.4" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="585.0" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="323.1" y1="581.9" x2="323.1" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="582.1" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="326.9" y1="581.4" x2="326.9" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="582.6" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="330.7" y1="576.8" x2="330.7" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="577.7" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="334.5" y1="574.0" x2="334.5" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="577.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="338.3" y1="576.5" x2="338.3" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="576.5" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="342.1" y1="565.8" x2="342.1" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="575.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="345.9" y1="565.2" x2="345.9" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="568.2" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="349.6" y1="567.7" x2="349.6" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="567.8" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="353.4" y1="575.2" x2="353.4" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="575.3" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="357.2" y1="581.8" x2="357.2" y2="588.4" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="582.3" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="361.0" y1="585.1" x2="361.0" y2="590.1" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="586.6" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="364.8" y1="586.7" x2="364.8" y2="588.7" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="587.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="586.7" x2="368.6" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="587.4" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="372.4" y1="587.1" x2="372.4" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="588.5" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="376.2" y1="588.2" x2="376.2" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="588.5" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="379.9" y1="591.0" x2="379.9" y2="593.5" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="591.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="383.7" y1="591.2" x2="383.7" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="591.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="387.5" y1="587.3" x2="387.5" y2="593.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="589.5" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="391.3" y1="588.2" x2="391.3" y2="590.0" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="589.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="395.1" y1="587.0" x2="395.1" y2="590.6" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="589.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="398.9" y1="589.4" x2="398.9" y2="596.5" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="590.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="402.7" y1="586.7" x2="402.7" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="587.8" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="406.4" y1="583.2" x2="406.4" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="584.0" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="410.2" y1="582.8" x2="410.2" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="584.3" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="414.0" y1="586.4" x2="414.0" y2="589.1" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="587.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="586.7" x2="417.8" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="587.3" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="421.6" y1="586.0" x2="421.6" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="588.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="425.4" y1="582.0" x2="425.4" y2="588.4" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="585.5" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="429.2" y1="582.2" x2="429.2" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="584.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="432.9" y1="574.1" x2="432.9" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="575.8" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="436.7" y1="572.2" x2="436.7" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="575.2" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="440.5" y1="575.1" x2="440.5" y2="578.3" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="575.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="444.3" y1="572.0" x2="444.3" y2="575.8" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="573.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="567.4" x2="448.1" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="567.7" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="451.9" y1="564.2" x2="451.9" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="565.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="455.7" y1="561.7" x2="455.7" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="562.9" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="459.5" y1="560.4" x2="459.5" y2="567.6" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="561.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="463.2" y1="553.1" x2="463.2" y2="561.3" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="558.6" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="467.0" y1="558.3" x2="467.0" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="558.6" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="470.8" y1="560.0" x2="470.8" y2="565.4" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="560.5" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="474.6" y1="560.7" x2="474.6" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="562.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="478.4" y1="561.1" x2="478.4" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="565.6" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="482.2" y1="559.9" x2="482.2" y2="569.9" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="560.8" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="486.0" y1="560.0" x2="486.0" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="560.3" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="489.7" y1="562.0" x2="489.7" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="563.6" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="493.5" y1="562.8" x2="493.5" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="564.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="497.3" y1="564.7" x2="497.3" y2="568.8" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="565.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="501.1" y1="563.2" x2="501.1" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="565.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="504.9" y1="559.8" x2="504.9" y2="569.4" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="563.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="508.7" y1="556.6" x2="508.7" y2="565.3" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="561.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="512.5" y1="558.1" x2="512.5" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="561.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="516.2" y1="560.8" x2="516.2" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="561.3" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="520.0" y1="561.0" x2="520.0" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="561.3" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="523.8" y1="558.3" x2="523.8" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="561.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="527.6" y1="558.3" x2="527.6" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="560.7" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="531.4" y1="560.7" x2="531.4" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="564.8" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="535.2" y1="562.6" x2="535.2" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="567.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="539.0" y1="568.3" x2="539.0" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="571.4" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="542.7" y1="574.2" x2="542.7" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="574.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="546.5" y1="575.1" x2="546.5" y2="578.7" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="576.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="550.3" y1="573.5" x2="550.3" y2="579.4" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="573.7" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="554.1" y1="577.8" x2="554.1" y2="581.1" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="577.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="557.9" y1="576.6" x2="557.9" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="578.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="561.7" y1="576.4" x2="561.7" y2="579.4" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="576.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="565.5" y1="569.2" x2="565.5" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="572.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="569.3" y1="571.5" x2="569.3" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="571.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="573.0" y1="573.1" x2="573.0" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="573.2" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="576.8" y1="575.2" x2="576.8" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="576.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="580.6" y1="571.0" x2="580.6" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="572.5" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="584.4" y1="570.2" x2="584.4" y2="580.6" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="572.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="588.2" y1="570.1" x2="588.2" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="570.7" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="592.0" y1="565.3" x2="592.0" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="569.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="595.8" y1="564.0" x2="595.8" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="566.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="599.5" y1="566.1" x2="599.5" y2="574.8" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="566.3" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="603.3" y1="572.3" x2="603.3" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="573.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="607.1" y1="573.5" x2="607.1" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="574.0" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="610.9" y1="572.2" x2="610.9" y2="576.5" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="574.0" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="614.7" y1="574.4" x2="614.7" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="574.4" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="618.5" y1="567.9" x2="618.5" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="568.1" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="622.3" y1="567.3" x2="622.3" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="567.3" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="626.0" y1="573.0" x2="626.0" y2="576.7" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="573.6" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="629.8" y1="573.0" x2="629.8" y2="581.8" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="575.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="633.6" y1="574.0" x2="633.6" y2="586.2" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="578.6" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="637.4" y1="577.5" x2="637.4" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="577.5" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="641.2" y1="578.1" x2="641.2" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="578.6" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="645.0" y1="578.1" x2="645.0" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="578.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="648.8" y1="579.7" x2="648.8" y2="584.5" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="580.1" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="652.5" y1="578.3" x2="652.5" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="579.1" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="656.3" y1="571.7" x2="656.3" y2="579.5" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="572.6" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="660.1" y1="557.3" x2="660.1" y2="571.5" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="557.5" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="663.9" y1="545.3" x2="663.9" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="545.5" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="667.7" y1="543.5" x2="667.7" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="543.5" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="671.5" y1="506.2" x2="671.5" y2="558.4" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="508.9" width="2.35" height="46.3" fill="var(--up)"/>
<line x1="675.3" y1="501.9" x2="675.3" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="502.5" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="679.1" y1="485.4" x2="679.1" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="495.9" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="682.8" y1="513.2" x2="682.8" y2="539.7" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="515.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="686.6" y1="513.2" x2="686.6" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="513.2" width="2.35" height="29.5" fill="var(--down)"/>
<line x1="690.4" y1="521.7" x2="690.4" y2="549.3" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="522.9" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="694.2" y1="516.3" x2="694.2" y2="529.3" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="517.9" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="698.0" y1="515.8" x2="698.0" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="515.8" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="701.8" y1="531.8" x2="701.8" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="532.9" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="705.6" y1="533.4" x2="705.6" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="540.0" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="709.3" y1="537.2" x2="709.3" y2="548.1" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="542.0" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="713.1" y1="528.6" x2="713.1" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="530.0" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="716.9" y1="526.0" x2="716.9" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="526.5" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="720.7" y1="532.0" x2="720.7" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="533.6" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="724.5" y1="507.8" x2="724.5" y2="532.1" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="516.8" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="728.3" y1="522.1" x2="728.3" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="526.8" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="732.1" y1="493.1" x2="732.1" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="496.7" width="2.35" height="36.7" fill="var(--up)"/>
<line x1="735.8" y1="480.0" x2="735.8" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="490.6" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="739.6" y1="488.5" x2="739.6" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="492.7" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="743.4" y1="509.6" x2="743.4" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="510.4" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="747.2" y1="515.2" x2="747.2" y2="535.8" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="516.0" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="751.0" y1="532.7" x2="751.0" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="534.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="754.8" y1="530.9" x2="754.8" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="534.9" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="758.6" y1="533.7" x2="758.6" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="535.2" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="762.4" y1="545.0" x2="762.4" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="550.3" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="766.1" y1="548.3" x2="766.1" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="549.6" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="769.9" y1="544.8" x2="769.9" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="546.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="773.7" y1="542.1" x2="773.7" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="543.4" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="777.5" y1="537.5" x2="777.5" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="538.8" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="781.3" y1="514.3" x2="781.3" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="514.9" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="785.1" y1="505.4" x2="785.1" y2="517.2" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="507.4" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="788.9" y1="485.6" x2="788.9" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="491.5" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="792.6" y1="464.5" x2="792.6" y2="488.5" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="475.3" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="796.4" y1="451.6" x2="796.4" y2="479.6" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="456.1" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="800.2" y1="429.8" x2="800.2" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="433.3" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="804.0" y1="375.1" x2="804.0" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="400.3" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="807.8" y1="382.6" x2="807.8" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="390.0" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="811.6" y1="407.0" x2="811.6" y2="432.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="417.4" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="815.4" y1="380.2" x2="815.4" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="380.9" width="2.35" height="38.5" fill="var(--up)"/>
<line x1="819.1" y1="329.8" x2="819.1" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="329.9" width="2.35" height="53.8" fill="var(--up)"/>
<line x1="822.9" y1="328.1" x2="822.9" y2="379.0" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="329.5" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="826.7" y1="333.7" x2="826.7" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="333.9" width="2.35" height="44.7" fill="var(--down)"/>
<line x1="830.5" y1="311.4" x2="830.5" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="361.0" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="834.3" y1="352.9" x2="834.3" y2="415.8" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="365.0" width="2.35" height="43.2" fill="var(--down)"/>
<line x1="838.1" y1="398.0" x2="838.1" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="404.6" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="841.9" y1="370.3" x2="841.9" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="386.4" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="845.6" y1="376.7" x2="845.6" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="382.1" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="849.4" y1="349.7" x2="849.4" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="362.2" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="853.2" y1="267.9" x2="853.2" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="276.3" width="2.35" height="85.3" fill="var(--up)"/>
<line x1="857.0" y1="224.6" x2="857.0" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="263.4" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="860.8" y1="198.3" x2="860.8" y2="270.4" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="218.1" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="864.6" y1="123.4" x2="864.6" y2="223.4" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="194.1" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="868.4" y1="74.7" x2="868.4" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="133.5" width="2.35" height="41.1" fill="var(--down)"/>
<line x1="872.2" y1="140.3" x2="872.2" y2="277.1" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="151.0" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="875.9" y1="148.6" x2="875.9" y2="209.7" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="161.5" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="879.7" y1="196.0" x2="879.7" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="209.5" width="2.35" height="67.2" fill="var(--down)"/>
<line x1="883.5" y1="249.4" x2="883.5" y2="352.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="259.1" width="2.35" height="70.1" fill="var(--down)"/>
<line x1="887.3" y1="286.4" x2="887.3" y2="363.1" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="338.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="891.1" y1="313.0" x2="891.1" y2="350.3" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="318.1" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="894.9" y1="285.0" x2="894.9" y2="331.5" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="309.9" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="898.7" y1="300.6" x2="898.7" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="306.3" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="902.4" y1="310.3" x2="902.4" y2="364.5" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="315.1" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="906.2" y1="291.9" x2="906.2" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="305.1" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="910.0" y1="302.2" x2="910.0" y2="342.2" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="302.4" width="2.35" height="29.7" fill="var(--up)"/>
<line x1="913.8" y1="238.4" x2="913.8" y2="298.2" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="262.4" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="917.6" y1="230.0" x2="917.6" y2="286.4" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="232.9" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="921.4" y1="215.6" x2="921.4" y2="281.5" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="242.4" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="925.2" y1="222.6" x2="925.2" y2="299.4" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="268.0" width="2.35" height="27.5" fill="var(--down)"/>
<line x1="928.9" y1="279.7" x2="928.9" y2="352.3" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="294.4" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="932.7" y1="297.2" x2="932.7" y2="408.2" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="318.1" width="2.35" height="71.4" fill="var(--down)"/>
<line x1="936.5" y1="371.4" x2="936.5" y2="403.5" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="384.1" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="940.3" y1="368.4" x2="940.3" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="385.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="944.1" y1="375.6" x2="944.1" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="396.2" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="947.9" y1="356.0" x2="947.9" y2="409.8" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="377.1" width="2.35" height="29.3" fill="var(--up)"/>
<line x1="951.7" y1="363.7" x2="951.7" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="375.8" width="2.35" height="28.4" fill="var(--down)"/>
<line x1="955.5" y1="384.9" x2="955.5" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="402.9" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="959.2" y1="401.0" x2="959.2" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="407.2" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="963.0" y1="396.6" x2="963.0" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="403.7" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="966.8" y1="376.6" x2="966.8" y2="412.2" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="384.2" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="970.6" y1="352.3" x2="970.6" y2="401.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="381.8" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="974.4" y1="359.1" x2="974.4" y2="401.0" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="375.8" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="978.2" y1="346.9" x2="978.2" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="379.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="982.0" y1="368.7" x2="982.0" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="382.7" width="2.35" height="26.4" fill="var(--down)"/>
<line x1="985.7" y1="401.2" x2="985.7" y2="432.1" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="409.2" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="989.5" y1="401.5" x2="989.5" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="406.2" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="993.3" y1="382.8" x2="993.3" y2="438.4" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="416.1" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="997.1" y1="427.5" x2="997.1" y2="454.2" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="427.6" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="1000.9" y1="397.6" x2="1000.9" y2="429.7" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="398.7" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="1004.7" y1="398.0" x2="1004.7" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="409.7" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="1008.5" y1="414.6" x2="1008.5" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="429.5" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="1012.2" y1="412.5" x2="1012.2" y2="434.1" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="422.9" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="1016.0" y1="424.1" x2="1016.0" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="427.7" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="1019.8" y1="414.1" x2="1019.8" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="431.4" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="1023.6" y1="410.1" x2="1023.6" y2="438.5" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="415.9" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="1027.4" y1="384.7" x2="1027.4" y2="420.6" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="398.7" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="1031.2" y1="391.0" x2="1031.2" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="399.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1035.0" y1="400.4" x2="1035.0" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="401.6" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="1038.7" y1="378.3" x2="1038.7" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="407.7" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="1042.5" y1="414.4" x2="1042.5" y2="432.4" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="419.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1046.3" y1="398.9" x2="1046.3" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="416.4" width="2.35" height="28.7" fill="var(--down)"/>
<line x1="1050.1" y1="427.1" x2="1050.1" y2="445.3" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="430.1" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="60" y1="455.7" x2="1052" y2="455.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="449.7" font-size="11.5" fill="var(--support)" font-weight="600">$143 S1</text>
<text x="1058" y="461.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="549.0" x2="1052" y2="549.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="543.0" font-size="11.5" fill="var(--support)" font-weight="600">$65 S2</text>
<text x="1058" y="555.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="590.1" x2="1052" y2="590.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="584.1" font-size="11.5" fill="var(--support)" font-weight="600">$30 S3</text>
<text x="1058" y="596.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="445.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="437.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $152 (2026-09-11)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$152.31** (2026-09-11 종가) | — | **기간 내 상단 저항 클러스터 없음** — 아래 주석 참고. 가장 가까운 유효 레벨은 S1($143) |
| S1 | $143 | 2 | 2026-06-08·2026-07-13 — 2026년 여름에 두 차례 지지된 구간이며 5년 구간 전체에서 **현재가 바로 아래 유일한 지지**다. 현재가 대비 −6.1% |
| S2 | $65 | 2 | 2024-11-18·2024-12-30 — 2024년 말의 스윙 저점대. 현재가 대비 −57.3%로, 2025년 대폭등 이전의 가격 체계에 속한다 |
| S3 | $30 | 2 | 2022-11-07·2022-12-26 — 4년 전 저점대. 현재가 대비 −80.3%. **참고용 이상의 의미는 없다** |
| 참고선 | $464.25 | — | 최근 5년 최고가(2025-10월). 현재가 대비 +204.8% |
| 참고선 | $17.36 | — | 최근 5년 최저가(2021~2022년경). 현재가 대비 −88.6% |

> **"상단 저항 없음"을 신고가 구간으로 오독하지 말 것.** 현재가($152.31)는 5년 최고가($464.25) 대비 **−67.2%**다. 저항 클러스터가 잡히지 않는 이유는 주가가 높아서가 아니라, **2025년 후반의 $300~$464 급등 구간이 너무 빠르게 지나가 반복 터치된 가격대를 남기지 않았기 때문**이다. 위쪽에는 저항 대신 **되돌림 매물대**가 있다고 보는 편이 정확하다.

---

## 3. 관측된 특이 구간 — 2024~2025년 급등과 2026년 되돌림

- 5년 차트의 형태는 **완만한 바닥(2021~2024년 $17~$65) → 수직 급등(2025년 $65 → $464) → 급락(2026년 $464 → $143)**의 세 국면으로 나뉜다. 현재는 세 번째 국면의 끝자락에 있다.
- 급등의 계기는 실적이 아니라 **정책**이었다. 2024-05 러시아산 농축우라늄 수입금지법 시행 이후 "미국이 소유한 유일한 농축 사업자"라는 서사가 가격에 반영됐고, 2026-01 DOE의 $900M HALEU 상업 증설 과제 선정이 정점이었다([역사 / 주요 이벤트](./02_history.md)). 같은 기간 GAAP 희석 EPS는 오히려 $4.47(FY2024) → $3.90(FY2025)으로 **줄었다**.
- 2026년의 되돌림도 대칭적이다. 2026-05 1분기 실적 급감(순이익 YoY −63.2%), 2026-08 DOE 옵션 미행사 통보, 2026-09 $500M 증자가 차례로 나오며 −67.2%가 빠졌다.
- **5년 구조가 말해주는 것은 이 종목의 가격이 이익이 아니라 서사에 연동돼 왔다는 사실이다.** 따라서 기술적 레벨보다 [투자 판단](./07_investment.md) 3. 리스크의 정책·희석 트리거가 가격을 훨씬 잘 설명한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-13. 원주가(과거 분할은 소급 반영, 배당은 미반영 — Centrus는 무배당)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py LEU --name "Centrus Energy" --interval 1wk --close-on 2026-09-11 --emit all` (기본 파라미터, `--force-level` 미사용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **이 문서에서 특히 중요한 한계 ①**: 3절의 수직 급등·급락 때문에 $152~$464 구간(현재가의 3배 폭)에 **유효 레벨이 하나도 없다.** 위쪽 방향에 대해 이 문서는 아무 정보도 주지 못한다.
    - **특히 중요한 한계 ②**: 5년 구간 안에 주식분할·병합은 없었으나(10-K 확인, 소급조정 불필요), **희석주식수가 15.4백만 주(FY2022) → 프로포마 24.41백만 주(2026-09 증자 후)로 약 58% 늘었다.** 주가 시계열에는 순수 펀더멘털 외에 반복적 신주 물량 소화라는 수급 요인이 섞여 있고, 미행사 워런트 6,992,382주가 이 요인을 앞으로도 남겨둔다.

---

*작성일: 2026-09-13*
