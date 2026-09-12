# 기술적 분석 (주봉 캔들차트 · 5년)

> 최근 5년 주봉으로 다년 구조를 본 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 2026-09-11 종가 **$518.97**은 [기술적 분석 — 일봉](./09_technical_daily.md)·[밸류에이션 / 적정주가](./06_valuation.md)의 값과 일치한다.
- **최근 5년 범위**: 최고 $774.00 · 최저 $344.89 · 주평균 거래량 4,149,300주.

:::

---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-11)

<div class="noc-chart">
<style>
.noc-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.noc-chart svg { width:100%; height:auto; display:block; }
.noc-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.noc-chart .title { fill: var(--ink); font-weight:600; }
.noc-chart .grid { stroke: var(--grid); stroke-width:1; }
.noc-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="노스롭 그루먼(NOC) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">노스롭 그루먼 (NOC) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $518.97 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="539.3" x2="1052" y2="539.3" class="grid"/>
<text x="52" y="543.3" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="415.3" x2="1052" y2="415.3" class="grid"/>
<text x="52" y="419.3" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="291.4" x2="1052" y2="291.4" class="grid"/>
<text x="52" y="295.4" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="167.5" x2="1052" y2="167.5" class="grid"/>
<text x="52" y="171.5" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
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
<line x1="61.9" y1="591.9" x2="61.9" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="594.1" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="65.7" y1="592.4" x2="65.7" y2="607.5" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="594.2" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="69.5" y1="581.4" x2="69.5" y2="594.0" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="587.7" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="73.3" y1="550.5" x2="73.3" y2="587.0" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="552.0" width="2.35" height="34.8" fill="var(--up)"/>
<line x1="77.0" y1="543.3" x2="77.0" y2="559.6" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="545.0" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="80.8" y1="531.4" x2="80.8" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="531.6" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="84.6" y1="529.3" x2="84.6" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="532.3" width="2.35" height="60.0" fill="var(--down)"/>
<line x1="88.4" y1="580.7" x2="88.4" y2="601.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="583.4" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="92.2" y1="580.3" x2="92.2" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="582.6" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="96.0" y1="586.9" x2="96.0" y2="606.3" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="588.2" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="99.8" y1="578.5" x2="99.8" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="595.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="103.5" y1="590.3" x2="103.5" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="591.5" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="107.3" y1="574.1" x2="107.3" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="575.1" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="111.1" y1="560.2" x2="111.1" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="567.2" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="114.9" y1="558.9" x2="114.9" y2="580.2" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="562.6" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="118.7" y1="553.9" x2="118.7" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="555.3" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="122.5" y1="537.8" x2="122.5" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="538.7" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="126.3" y1="530.8" x2="126.3" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="533.1" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="130.0" y1="528.1" x2="130.0" y2="544.4" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="535.1" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="133.8" y1="528.4" x2="133.8" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="541.7" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="137.6" y1="566.3" x2="137.6" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="568.1" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="141.4" y1="537.7" x2="141.4" y2="578.7" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="540.1" width="2.35" height="35.7" fill="var(--up)"/>
<line x1="145.2" y1="537.6" x2="145.2" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="543.0" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="149.0" y1="525.5" x2="149.0" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="527.3" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="152.8" y1="448.9" x2="152.8" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="454.3" width="2.35" height="67.2" fill="var(--up)"/>
<line x1="156.5" y1="426.7" x2="156.5" y2="495.0" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="449.5" width="2.35" height="44.8" fill="var(--down)"/>
<line x1="160.3" y1="479.3" x2="160.3" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="490.6" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="164.1" y1="464.4" x2="164.1" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="467.2" width="2.35" height="28.4" fill="var(--up)"/>
<line x1="167.9" y1="467.5" x2="167.9" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="471.4" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="171.7" y1="443.5" x2="171.7" y2="484.3" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="460.4" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="175.5" y1="451.3" x2="175.5" y2="465.8" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="456.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="179.3" y1="447.8" x2="179.3" y2="485.9" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="456.0" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="183.1" y1="474.2" x2="183.1" y2="499.1" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="484.8" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="186.8" y1="452.2" x2="186.8" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="454.1" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="190.6" y1="456.3" x2="190.6" y2="486.3" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="457.5" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="194.4" y1="462.1" x2="194.4" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="472.8" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="198.2" y1="444.5" x2="198.2" y2="481.9" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="451.6" width="2.35" height="29.9" fill="var(--up)"/>
<line x1="202.0" y1="441.9" x2="202.0" y2="477.7" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="442.2" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="205.8" y1="424.9" x2="205.8" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="441.0" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="209.6" y1="457.8" x2="209.6" y2="494.6" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="465.2" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="213.3" y1="459.0" x2="213.3" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="460.3" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="217.1" y1="430.3" x2="217.1" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="432.2" width="2.35" height="31.0" fill="var(--up)"/>
<line x1="220.9" y1="431.6" x2="220.9" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="439.6" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="224.7" y1="437.9" x2="224.7" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="441.8" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="228.5" y1="459.5" x2="228.5" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="461.2" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="232.3" y1="440.4" x2="232.3" y2="497.3" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="441.5" width="2.35" height="33.5" fill="var(--up)"/>
<line x1="236.1" y1="429.8" x2="236.1" y2="453.3" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="438.4" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="239.8" y1="437.4" x2="239.8" y2="457.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="440.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="243.6" y1="418.8" x2="243.6" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="426.8" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="247.4" y1="419.4" x2="247.4" y2="440.5" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="430.2" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="251.2" y1="428.8" x2="251.2" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="440.1" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="255.0" y1="421.1" x2="255.0" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="426.0" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="258.8" y1="426.4" x2="258.8" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="426.4" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="262.6" y1="396.2" x2="262.6" y2="447.5" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="436.2" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="266.4" y1="432.9" x2="266.4" y2="459.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="443.4" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="270.1" y1="418.9" x2="270.1" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="420.2" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="273.9" y1="397.3" x2="273.9" y2="461.1" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="416.8" width="2.35" height="42.9" fill="var(--down)"/>
<line x1="277.7" y1="383.9" x2="277.7" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="387.3" width="2.35" height="68.7" fill="var(--up)"/>
<line x1="281.5" y1="345.6" x2="281.5" y2="405.4" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="355.7" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="285.3" y1="348.9" x2="285.3" y2="402.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="359.8" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="289.1" y1="361.8" x2="289.1" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="386.8" width="2.35" height="37.6" fill="var(--down)"/>
<line x1="292.9" y1="384.6" x2="292.9" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="390.0" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="296.6" y1="373.5" x2="296.6" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="380.9" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="300.4" y1="353.6" x2="300.4" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="358.8" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="304.2" y1="357.4" x2="304.2" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="366.4" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="308.0" y1="368.7" x2="308.0" y2="388.6" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="377.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="311.8" y1="363.2" x2="311.8" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="372.3" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="315.6" y1="357.3" x2="315.6" y2="369.5" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="358.8" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="319.4" y1="356.1" x2="319.4" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="359.7" width="2.35" height="29.1" fill="var(--down)"/>
<line x1="323.1" y1="393.0" x2="323.1" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="393.0" width="2.35" height="70.1" fill="var(--down)"/>
<line x1="326.9" y1="458.4" x2="326.9" y2="489.6" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="460.8" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="330.7" y1="448.6" x2="330.7" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="474.9" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="334.5" y1="471.8" x2="334.5" y2="495.1" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="483.5" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="338.3" y1="459.5" x2="338.3" y2="486.0" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="460.1" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="342.1" y1="451.3" x2="342.1" y2="469.4" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="451.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="345.9" y1="437.2" x2="345.9" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="446.6" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="349.6" y1="447.4" x2="349.6" y2="465.8" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="451.7" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="353.4" y1="445.1" x2="353.4" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="456.7" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="357.2" y1="461.4" x2="357.2" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="471.5" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="361.0" y1="469.6" x2="361.0" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="470.8" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="364.8" y1="460.8" x2="364.8" y2="470.9" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="462.8" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="368.6" y1="444.8" x2="368.6" y2="461.6" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="452.0" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="372.4" y1="442.4" x2="372.4" y2="457.4" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="449.3" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="376.2" y1="435.9" x2="376.2" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="448.8" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="379.9" y1="449.3" x2="379.9" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="451.1" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="383.7" y1="457.4" x2="383.7" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="462.5" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="387.5" y1="476.1" x2="387.5" y2="498.1" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="479.4" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="391.3" y1="479.3" x2="391.3" y2="495.3" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="485.6" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="395.1" y1="481.8" x2="395.1" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="487.1" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="398.9" y1="480.9" x2="398.9" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="484.9" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="402.7" y1="465.3" x2="402.7" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="472.0" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="406.4" y1="466.3" x2="406.4" y2="483.3" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="467.0" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="410.2" y1="461.7" x2="410.2" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="466.2" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="414.0" y1="465.5" x2="414.0" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="470.1" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="417.8" y1="464.1" x2="417.8" y2="476.4" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="473.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="421.6" y1="462.4" x2="421.6" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="474.1" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="425.4" y1="464.1" x2="425.4" y2="491.4" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="473.1" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="429.2" y1="465.1" x2="429.2" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="472.5" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="432.9" y1="476.7" x2="432.9" y2="492.6" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="476.7" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="436.7" y1="490.5" x2="436.7" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="492.3" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="440.5" y1="492.7" x2="440.5" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="500.6" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="444.3" y1="489.7" x2="444.3" y2="503.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="502.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="492.9" x2="448.1" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="495.1" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="451.9" y1="494.8" x2="451.9" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="495.9" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="455.7" y1="495.0" x2="455.7" y2="518.6" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="497.8" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="459.5" y1="484.9" x2="459.5" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="494.8" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="463.2" y1="485.7" x2="463.2" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="489.5" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="467.0" y1="482.6" x2="467.0" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="489.2" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="470.8" y1="426.5" x2="470.8" y2="478.9" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="427.6" width="2.35" height="49.8" fill="var(--up)"/>
<line x1="474.6" y1="419.2" x2="474.6" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="425.0" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="478.4" y1="425.3" x2="478.4" y2="453.9" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="432.4" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="482.2" y1="443.8" x2="482.2" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="448.0" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="486.0" y1="447.1" x2="486.0" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="449.3" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="489.7" y1="454.2" x2="489.7" y2="464.2" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="459.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="493.5" y1="448.0" x2="493.5" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="450.6" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="497.3" y1="439.4" x2="497.3" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="440.3" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="501.1" y1="435.6" x2="501.1" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="442.0" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="504.9" y1="432.2" x2="504.9" y2="471.1" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="443.9" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="508.7" y1="455.8" x2="508.7" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="461.0" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="512.5" y1="453.8" x2="512.5" y2="461.9" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="454.8" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="516.2" y1="435.4" x2="516.2" y2="456.0" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="452.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="520.0" y1="438.3" x2="520.0" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="438.8" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="523.8" y1="436.5" x2="523.8" y2="454.4" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="438.3" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="527.6" y1="448.8" x2="527.6" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="453.2" width="2.35" height="39.0" fill="var(--down)"/>
<line x1="531.4" y1="477.7" x2="531.4" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="481.5" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="535.2" y1="470.4" x2="535.2" y2="489.4" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="471.2" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="539.0" y1="470.3" x2="539.0" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="471.1" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="542.7" y1="463.0" x2="542.7" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="463.5" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="546.5" y1="457.8" x2="546.5" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="462.1" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="550.3" y1="459.2" x2="550.3" y2="473.4" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="465.5" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="554.1" y1="459.5" x2="554.1" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="462.7" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="557.9" y1="448.1" x2="557.9" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="454.1" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="561.7" y1="439.2" x2="561.7" y2="455.1" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="441.8" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="565.5" y1="441.6" x2="565.5" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="442.1" width="2.35" height="29.6" fill="var(--down)"/>
<line x1="569.3" y1="454.7" x2="569.3" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="469.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="573.0" y1="459.2" x2="573.0" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="461.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="576.8" y1="427.0" x2="576.8" y2="462.3" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="439.6" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="580.6" y1="427.4" x2="580.6" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="438.3" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="584.4" y1="444.7" x2="584.4" y2="455.9" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="446.6" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="588.2" y1="439.2" x2="588.2" y2="457.1" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="446.1" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="592.0" y1="445.9" x2="592.0" y2="458.9" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="450.2" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="595.8" y1="458.6" x2="595.8" y2="483.7" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="458.6" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="599.5" y1="473.1" x2="599.5" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="478.3" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="603.3" y1="487.4" x2="603.3" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="489.7" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="607.1" y1="493.7" x2="607.1" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="499.5" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="610.9" y1="492.0" x2="610.9" y2="505.7" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="494.7" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="614.7" y1="489.1" x2="614.7" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="492.7" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="618.5" y1="492.6" x2="618.5" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="495.7" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="622.3" y1="482.4" x2="622.3" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="492.2" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="626.0" y1="434.6" x2="626.0" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="439.8" width="2.35" height="52.9" fill="var(--up)"/>
<line x1="629.8" y1="409.2" x2="629.8" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="422.1" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="633.6" y1="406.9" x2="633.6" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="418.5" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="637.4" y1="405.8" x2="637.4" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="407.1" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="641.2" y1="400.6" x2="641.2" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="403.8" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="645.0" y1="386.1" x2="645.0" y2="405.4" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="386.6" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="648.8" y1="379.7" x2="648.8" y2="397.1" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="387.3" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="652.5" y1="381.9" x2="652.5" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="390.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="656.3" y1="381.3" x2="656.3" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="384.2" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="660.1" y1="372.5" x2="660.1" y2="388.1" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="382.2" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="663.9" y1="346.5" x2="663.9" y2="388.2" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="369.8" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="667.7" y1="366.7" x2="667.7" y2="383.3" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="370.4" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="671.5" y1="370.6" x2="671.5" y2="387.9" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="377.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="675.3" y1="369.6" x2="675.3" y2="396.2" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="373.6" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="679.1" y1="391.5" x2="679.1" y2="413.1" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="391.5" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="682.8" y1="376.6" x2="682.8" y2="412.7" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="379.4" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="686.6" y1="366.1" x2="686.6" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="374.5" width="2.35" height="48.3" fill="var(--down)"/>
<line x1="690.4" y1="415.3" x2="690.4" y2="430.9" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="419.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="694.2" y1="422.8" x2="694.2" y2="442.1" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="423.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="698.0" y1="428.8" x2="698.0" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="431.5" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="701.8" y1="432.4" x2="701.8" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="440.1" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="705.6" y1="431.6" x2="705.6" y2="461.4" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="441.6" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="709.3" y1="446.8" x2="709.3" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="450.8" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="713.1" y1="445.0" x2="713.1" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="455.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="716.9" y1="457.2" x2="716.9" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="458.4" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="720.7" y1="435.9" x2="720.7" y2="466.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="437.2" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="724.5" y1="405.8" x2="724.5" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="419.0" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="728.3" y1="406.2" x2="728.3" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="412.4" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="732.1" y1="423.6" x2="732.1" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="429.7" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="735.8" y1="443.3" x2="735.8" y2="496.9" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="452.8" width="2.35" height="38.3" fill="var(--down)"/>
<line x1="739.6" y1="476.0" x2="739.6" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="479.8" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="743.4" y1="458.8" x2="743.4" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="462.8" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="747.2" y1="426.4" x2="747.2" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="432.1" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="751.0" y1="402.7" x2="751.0" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="432.2" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="754.8" y1="418.2" x2="754.8" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="426.8" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="758.6" y1="392.2" x2="758.6" y2="428.9" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="400.2" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="762.4" y1="384.4" x2="762.4" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="400.5" width="2.35" height="32.8" fill="var(--down)"/>
<line x1="766.1" y1="368.6" x2="766.1" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="373.2" width="2.35" height="66.7" fill="var(--up)"/>
<line x1="769.9" y1="359.9" x2="769.9" y2="383.5" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="365.3" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="773.7" y1="365.8" x2="773.7" y2="477.1" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="365.8" width="2.35" height="82.8" fill="var(--down)"/>
<line x1="777.5" y1="417.2" x2="777.5" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="426.0" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="781.3" y1="420.0" x2="781.3" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="423.3" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="785.1" y1="436.7" x2="785.1" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="440.2" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="788.9" y1="438.8" x2="788.9" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="444.9" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="792.6" y1="432.7" x2="792.6" y2="454.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="434.2" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="796.4" y1="420.4" x2="796.4" y2="441.5" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="428.5" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="800.2" y1="391.3" x2="800.2" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="394.6" width="2.35" height="33.1" fill="var(--up)"/>
<line x1="804.0" y1="396.8" x2="804.0" y2="430.2" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="402.0" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="807.8" y1="405.0" x2="807.8" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="414.3" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="811.6" y1="408.9" x2="811.6" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="410.1" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="815.4" y1="396.5" x2="815.4" y2="414.3" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="397.3" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="819.1" y1="380.3" x2="819.1" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="391.8" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="822.9" y1="320.1" x2="822.9" y2="397.5" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="328.9" width="2.35" height="63.7" fill="var(--up)"/>
<line x1="826.7" y1="306.5" x2="826.7" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="308.2" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="830.5" y1="298.0" x2="830.5" y2="317.3" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="309.2" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="834.3" y1="307.7" x2="834.3" y2="321.9" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="311.3" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="838.1" y1="290.2" x2="838.1" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="300.8" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="841.9" y1="296.6" x2="841.9" y2="315.1" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="301.3" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="845.6" y1="296.2" x2="845.6" y2="322.6" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="301.5" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="849.4" y1="309.1" x2="849.4" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="321.2" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="853.2" y1="307.2" x2="853.2" y2="334.2" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="323.7" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="857.0" y1="297.7" x2="857.0" y2="328.3" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="298.2" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="860.8" y1="278.0" x2="860.8" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="279.6" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="864.6" y1="240.8" x2="864.6" y2="280.3" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="262.3" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="868.4" y1="257.5" x2="868.4" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="266.7" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="872.2" y1="279.3" x2="872.2" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="284.5" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="875.9" y1="284.4" x2="875.9" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="285.4" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="879.7" y1="314.7" x2="879.7" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="315.7" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="883.5" y1="327.6" x2="883.5" y2="349.2" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="335.1" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="887.3" y1="324.5" x2="887.3" y2="345.6" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="332.7" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="891.1" y1="313.0" x2="891.1" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="325.8" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="894.9" y1="330.5" x2="894.9" y2="361.2" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="331.4" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="898.7" y1="326.6" x2="898.7" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="328.9" width="2.35" height="25.7" fill="var(--up)"/>
<line x1="902.4" y1="321.4" x2="902.4" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="329.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="906.2" y1="307.2" x2="906.2" y2="330.0" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="319.5" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="910.0" y1="309.0" x2="910.0" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="309.2" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="913.8" y1="243.3" x2="913.8" y2="323.0" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="268.1" width="2.35" height="30.8" fill="var(--up)"/>
<line x1="917.6" y1="205.1" x2="917.6" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="208.5" width="2.35" height="53.6" fill="var(--up)"/>
<line x1="921.4" y1="195.7" x2="921.4" y2="225.7" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="201.0" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="925.2" y1="160.8" x2="925.2" y2="246.8" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="177.1" width="2.35" height="27.6" fill="var(--up)"/>
<line x1="928.9" y1="152.8" x2="928.9" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="156.2" width="2.35" height="29.9" fill="var(--up)"/>
<line x1="932.7" y1="148.2" x2="932.7" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="152.5" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="936.5" y1="111.1" x2="936.5" y2="169.1" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="138.3" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="940.3" y1="124.7" x2="940.3" y2="178.6" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="137.3" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="944.1" y1="75.8" x2="944.1" y2="124.9" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="98.0" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="947.9" y1="86.3" x2="947.9" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="89.5" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="951.7" y1="121.2" x2="951.7" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="126.0" width="2.35" height="32.9" fill="var(--down)"/>
<line x1="955.5" y1="159.2" x2="955.5" y2="206.9" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="160.3" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="959.2" y1="156.9" x2="959.2" y2="212.2" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="164.4" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="963.0" y1="163.7" x2="963.0" y2="210.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="166.3" width="2.35" height="33.8" fill="var(--down)"/>
<line x1="966.8" y1="187.5" x2="966.8" y2="213.3" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="195.1" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="970.6" y1="200.6" x2="970.6" y2="329.8" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="208.4" width="2.35" height="113.9" fill="var(--down)"/>
<line x1="974.4" y1="306.0" x2="974.4" y2="331.9" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="319.9" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="978.2" y1="319.3" x2="978.2" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="331.9" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="982.0" y1="341.7" x2="982.0" y2="366.8" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="358.3" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="985.7" y1="343.9" x2="985.7" y2="367.0" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="346.5" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="989.5" y1="336.1" x2="989.5" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="336.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="993.3" y1="341.1" x2="993.3" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="341.1" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="997.1" y1="341.4" x2="997.1" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="353.0" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="1000.9" y1="342.5" x2="1000.9" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="362.9" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="1004.7" y1="391.0" x2="1004.7" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="396.0" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="1008.5" y1="354.6" x2="1008.5" y2="423.0" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="354.6" width="2.35" height="58.3" fill="var(--up)"/>
<line x1="1012.2" y1="350.1" x2="1012.2" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="357.1" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="1016.0" y1="358.9" x2="1016.0" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="365.1" width="2.35" height="23.5" fill="var(--down)"/>
<line x1="1019.8" y1="357.4" x2="1019.8" y2="441.3" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="363.0" width="2.35" height="23.2" fill="var(--up)"/>
<line x1="1023.6" y1="334.3" x2="1023.6" y2="390.9" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="362.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1027.4" y1="325.2" x2="1027.4" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="326.7" width="2.35" height="31.7" fill="var(--up)"/>
<line x1="1031.2" y1="308.3" x2="1031.2" y2="329.2" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="308.9" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="1035.0" y1="298.2" x2="1035.0" y2="353.2" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="313.9" width="2.35" height="38.2" fill="var(--down)"/>
<line x1="1038.7" y1="348.9" x2="1038.7" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="349.7" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="1042.5" y1="353.7" x2="1042.5" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="366.2" width="2.35" height="30.5" fill="var(--down)"/>
<line x1="1046.3" y1="382.0" x2="1046.3" y2="396.7" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="391.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="1050.1" y1="386.8" x2="1050.1" y2="396.5" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="388.1" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="60" y1="354.8" x2="1052" y2="354.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="358.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$549 R1</text>
<text x="1058" y="370.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="294.2" x2="1052" y2="294.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="297.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$598 R2</text>
<text x="1058" y="309.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="479.3" x2="1052" y2="479.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="473.3" font-size="11.5" fill="var(--support)" font-weight="600">$448 S1</text>
<text x="1058" y="485.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="505.2" x2="1052" y2="505.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="499.2" font-size="11.5" fill="var(--support)" font-weight="600">$427 S2</text>
<text x="1058" y="511.2" font-size="9.5" fill="var(--muted)">터치 9회</text>
<circle cx="1052.0" cy="391.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="383.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $519 (2026-09-11)</text>
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

각 레벨은 "전후 일정 기간 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $598 | 2 | 2025-08-18·2026-08-17 — 2025·2026년 8월에 각각 한 번씩 닿은 상단. **두 번 모두 8월이라는 점은 우연으로 보는 것이 안전하다**(계절성 근거 없음) |
| R1 | $549 | 5 | 2022-10-24·2023-01-02·2024-09-30·2024-11-11·2025-04-14 — 5년 중 가장 여러 번(5회) 닿은 대역. 2022년 말부터 2025년까지 박스권 상단 역할을 했다 |
| **현재가** | **$518.97** (2026-09-11 종가) | — | R1 $549와 S1 $448 사이. **5년 박스권 상단이던 $549를 아래에서 다시 올려다보는 자리** |
| S1 | $448 | 5 | 2023-03-13·2023-12-11·2024-04-15·2025-01-06·2025-04-21 — 2023~2025년 하단 지지. 현재가에서 −13.7% |
| S2 | $427 | 9 | 2022-05-02·2022-06-13·2022-07-25·2023-01-23·2023-05-22·2023-10-02·2024-01-22·2024-06-10·2025-02-17 — **9회로 5년 중 최다 터치.** 2022~2025년의 구조적 바닥 |

---

## 3. 관측된 특이 구간 — 2026년 상반기의 레짐 이탈과 복귀

- 2025년 말까지 이 종목은 **$427~$549 박스권**에서 3년 가까이 움직였다(위 S2·R1이 각각 9회·5회 터치). 2026년 1~3월에 그 박스를 위로 크게 벗어나 **$774.00(최고)**까지 올랐다가, 4월 실적 갭다운과 6월 지정학 프리미엄 축소를 거치며 되돌렸다([기술적 분석 — 일봉](./09_technical_daily.md) 3. 관측된 특이 구간).
- **현재가 $518.97은 그 박스권의 상단($549) 바로 아래**다. 즉 5년 구조에서 보면 2026년 상반기의 급등·급락은 아직 **박스 위쪽 경계로 되돌아온 단계**이고, 박스 안으로 완전히 되돌아간 것은 아니다.
- 이 관찰은 **가격 구조에 대한 서술일 뿐 방향 예측이 아니다.** 같은 기간 회사의 수주잔고·이익은 박스권 시절보다 크게 늘었으므로([핵심 지표](./04_metrics.md) C. 사업 고유 지표), 과거 박스권 가격대를 그대로 현재의 적정 범위로 읽으면 안 된다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `uv run python scripts/gen_technical_chart.py NOC --name "노스롭 그루먼" --interval 1wk --close-on 2026-09-11 --emit all`

- **한계**: 원주가 기준이라 기간 내 배당 20회가 반영돼 있지 않다 — 5년 누적으로는 총수익률과의 괴리가 10%p를 넘는다. 또한 주봉 스윙 탐지 창(전후 4주)은 일봉(전후 5거래일)보다 넓어 **같은 회사라도 두 문서의 레벨이 일치하지 않는 것이 정상**이다.

---

*작성일: 2026-09-12*
