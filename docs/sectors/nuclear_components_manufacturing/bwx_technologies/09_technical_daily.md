# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(1년 일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-11 종가 $150.12**(Yahoo Finance)는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)가 인용한 stockanalysis.com 기준 $150.12와 **정확히 일치**한다.

:::
---

## 1. 차트 — 최근 1년 일봉 (`2025-09-12` ~ `2026-09-11`)

<div class="bwxt-chart">
<style>
.bwxt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .bwxt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .bwxt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.bwxt-chart svg { width:100%; height:auto; display:block; }
.bwxt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.bwxt-chart .title { fill: var(--ink); font-weight:600; }
.bwxt-chart .grid { stroke: var(--grid); stroke-width:1; }
.bwxt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="BWX Technologies(BWXT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">BWX Technologies (BWXT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-12 ~ 2026-09-11 · 마지막 종가 $150.12 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="536.6" x2="1052" y2="536.6" class="grid"/>
<text x="52" y="540.6" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="424.8" x2="1052" y2="424.8" class="grid"/>
<text x="52" y="428.8" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="60" y1="313.1" x2="1052" y2="313.1" class="grid"/>
<text x="52" y="317.1" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="201.3" x2="1052" y2="201.3" class="grid"/>
<text x="52" y="205.3" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
<line x1="60" y1="89.5" x2="1052" y2="89.5" class="grid"/>
<text x="52" y="93.5" font-size="11" text-anchor="end" fill="var(--muted)">240</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="113.4" y1="626.0" x2="113.4" y2="631.0" class="axis"/>
<text x="113.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="204.3" y1="626.0" x2="204.3" y2="631.0" class="axis"/>
<text x="204.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="366.3" y1="626.0" x2="366.3" y2="631.0" class="axis"/>
<text x="366.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="445.3" y1="626.0" x2="445.3" y2="631.0" class="axis"/>
<text x="445.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="607.4" y1="626.0" x2="607.4" y2="631.0" class="axis"/>
<text x="607.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="690.4" y1="626.0" x2="690.4" y2="631.0" class="axis"/>
<text x="690.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="769.4" y1="626.0" x2="769.4" y2="631.0" class="axis"/>
<text x="769.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="852.4" y1="626.0" x2="852.4" y2="631.0" class="axis"/>
<text x="852.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="939.4" y1="626.0" x2="939.4" y2="631.0" class="axis"/>
<text x="939.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1022.4" y1="626.0" x2="1022.4" y2="631.0" class="axis"/>
<text x="1022.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="472.3" x2="62.0" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="480.7" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="65.9" y1="453.1" x2="65.9" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="456.7" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="69.9" y1="430.0" x2="69.9" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="443.5" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="73.8" y1="440.2" x2="73.8" y2="492.4" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="447.2" width="2.45" height="42.6" fill="var(--down)"/>
<line x1="77.8" y1="454.7" x2="77.8" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="458.2" width="2.45" height="28.1" fill="var(--up)"/>
<line x1="81.7" y1="446.8" x2="81.7" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="455.6" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="85.7" y1="431.9" x2="85.7" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="434.9" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="89.6" y1="413.6" x2="89.6" y2="441.4" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="435.9" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="93.6" y1="426.2" x2="93.6" y2="453.2" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="432.4" width="2.45" height="20.3" fill="var(--down)"/>
<line x1="97.5" y1="438.0" x2="97.5" y2="475.8" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="446.0" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="101.5" y1="419.3" x2="101.5" y2="438.8" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="421.4" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="105.5" y1="396.9" x2="105.5" y2="419.0" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="405.5" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="109.4" y1="394.7" x2="109.4" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="400.4" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="113.4" y1="377.9" x2="113.4" y2="413.1" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="384.7" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="117.3" y1="368.9" x2="117.3" y2="406.8" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="378.8" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="121.3" y1="375.6" x2="121.3" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="387.7" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="125.2" y1="350.8" x2="125.2" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="361.2" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="129.2" y1="337.6" x2="129.2" y2="371.3" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="357.6" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="133.1" y1="326.9" x2="133.1" y2="357.8" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="329.8" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="137.1" y1="314.6" x2="137.1" y2="345.6" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="326.6" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="141.0" y1="322.9" x2="141.0" y2="369.6" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="337.6" width="2.45" height="30.8" fill="var(--down)"/>
<line x1="145.0" y1="314.3" x2="145.0" y2="351.9" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="327.8" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="148.9" y1="285.3" x2="148.9" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="299.3" width="2.45" height="41.5" fill="var(--up)"/>
<line x1="152.9" y1="234.8" x2="152.9" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="238.2" width="2.45" height="53.5" fill="var(--down)"/>
<line x1="156.8" y1="230.8" x2="156.8" y2="285.1" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="262.7" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="160.8" y1="259.5" x2="160.8" y2="329.9" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="279.5" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="164.7" y1="264.0" x2="164.7" y2="297.1" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="269.9" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="168.7" y1="269.9" x2="168.7" y2="313.0" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="279.5" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="172.6" y1="277.1" x2="172.6" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="285.1" width="2.45" height="77.3" fill="var(--down)"/>
<line x1="176.6" y1="310.7" x2="176.6" y2="363.4" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="313.5" width="2.45" height="49.8" fill="var(--up)"/>
<line x1="180.5" y1="293.1" x2="180.5" y2="308.7" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="294.7" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="184.5" y1="273.2" x2="184.5" y2="299.8" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="284.7" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="188.4" y1="234.8" x2="188.4" y2="276.7" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="238.7" width="2.45" height="31.7" fill="var(--down)"/>
<line x1="192.4" y1="225.8" x2="192.4" y2="282.3" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="236.6" width="2.45" height="34.0" fill="var(--up)"/>
<line x1="196.4" y1="209.7" x2="196.4" y2="247.0" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="235.9" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="200.3" y1="219.5" x2="200.3" y2="249.0" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="229.2" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="204.3" y1="218.5" x2="204.3" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="224.4" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="208.2" y1="273.9" x2="208.2" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="289.1" width="2.45" height="21.8" fill="var(--down)"/>
<line x1="212.2" y1="301.9" x2="212.2" y2="341.2" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="323.6" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="216.1" y1="324.2" x2="216.1" y2="366.7" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="324.4" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="220.1" y1="348.7" x2="220.1" y2="396.9" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="349.1" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="224.0" y1="317.7" x2="224.0" y2="350.5" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="319.8" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="228.0" y1="321.4" x2="228.0" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="325.7" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="231.9" y1="313.1" x2="231.9" y2="344.3" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="331.1" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="235.9" y1="338.2" x2="235.9" y2="444.0" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="338.4" width="2.45" height="98.2" fill="var(--down)"/>
<line x1="239.8" y1="408.7" x2="239.8" y2="467.2" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="434.3" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="243.8" y1="419.2" x2="243.8" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="428.0" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="247.7" y1="437.2" x2="247.7" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="447.7" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="251.7" y1="418.0" x2="251.7" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="425.9" width="2.45" height="20.3" fill="var(--up)"/>
<line x1="255.6" y1="385.5" x2="255.6" y2="452.6" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="396.9" width="2.45" height="54.3" fill="var(--down)"/>
<line x1="259.6" y1="454.3" x2="259.6" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="469.5" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="263.5" y1="452.1" x2="263.5" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="454.9" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="267.5" y1="445.7" x2="267.5" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="451.3" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="271.4" y1="426.0" x2="271.4" y2="449.5" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="435.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="275.4" y1="424.8" x2="275.4" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="425.4" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="279.3" y1="441.8" x2="279.3" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="444.3" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="283.3" y1="429.3" x2="283.3" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="434.5" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="287.3" y1="449.1" x2="287.3" y2="471.3" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="449.1" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="291.2" y1="410.9" x2="291.2" y2="458.0" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="434.2" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="295.2" y1="416.6" x2="295.2" y2="453.5" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="419.2" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="299.1" y1="422.7" x2="299.1" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="430.6" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="303.1" y1="424.8" x2="303.1" y2="441.0" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="436.2" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="307.0" y1="413.6" x2="307.0" y2="458.4" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="426.8" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="311.0" y1="402.8" x2="311.0" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="405.9" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="314.9" y1="403.9" x2="314.9" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="404.8" width="2.45" height="47.8" fill="var(--down)"/>
<line x1="318.9" y1="442.1" x2="318.9" y2="480.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="444.0" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="322.8" y1="453.4" x2="322.8" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="462.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="326.8" y1="458.4" x2="326.8" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="462.8" width="2.45" height="28.4" fill="var(--down)"/>
<line x1="330.7" y1="460.0" x2="330.7" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="465.2" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="334.7" y1="442.3" x2="334.7" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="444.8" width="2.45" height="31.0" fill="var(--up)"/>
<line x1="338.6" y1="424.8" x2="338.6" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="425.7" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="342.6" y1="419.2" x2="342.6" y2="441.4" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="436.5" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="346.5" y1="434.9" x2="346.5" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="434.9" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="350.5" y1="438.2" x2="350.5" y2="453.9" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="439.9" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="354.4" y1="438.2" x2="354.4" y2="456.2" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="450.0" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="358.4" y1="444.2" x2="358.4" y2="458.5" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="444.3" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="362.3" y1="452.4" x2="362.3" y2="466.1" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="452.7" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="366.3" y1="413.5" x2="366.3" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="414.5" width="2.45" height="40.9" fill="var(--up)"/>
<line x1="370.2" y1="369.6" x2="370.2" y2="391.3" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="374.4" width="2.45" height="16.9" fill="var(--up)"/>
<line x1="374.2" y1="338.2" x2="374.2" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="339.3" width="2.45" height="35.1" fill="var(--up)"/>
<line x1="378.2" y1="325.8" x2="378.2" y2="357.3" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="340.7" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="382.1" y1="312.3" x2="382.1" y2="370.7" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="325.7" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="386.1" y1="296.3" x2="386.1" y2="335.6" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="304.9" width="2.45" height="28.4" fill="var(--up)"/>
<line x1="390.0" y1="271.6" x2="390.0" y2="304.7" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="276.1" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="394.0" y1="248.2" x2="394.0" y2="276.1" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="254.2" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="397.9" y1="262.8" x2="397.9" y2="311.2" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="265.1" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="401.9" y1="207.5" x2="401.9" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="239.0" width="2.45" height="29.3" fill="var(--up)"/>
<line x1="405.8" y1="198.1" x2="405.8" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="213.1" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="409.8" y1="223.6" x2="409.8" y2="289.0" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="245.4" width="2.45" height="33.7" fill="var(--down)"/>
<line x1="413.7" y1="255.7" x2="413.7" y2="296.6" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="259.9" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="417.7" y1="247.2" x2="417.7" y2="286.0" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="250.1" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="421.6" y1="268.6" x2="421.6" y2="299.1" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="269.8" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="425.6" y1="250.1" x2="425.6" y2="287.9" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="275.5" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="429.5" y1="234.1" x2="429.5" y2="295.3" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="243.8" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="433.5" y1="220.7" x2="433.5" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="222.0" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="437.4" y1="202.1" x2="437.4" y2="284.4" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="215.9" width="2.45" height="40.3" fill="var(--down)"/>
<line x1="441.4" y1="246.0" x2="441.4" y2="298.7" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="276.7" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="445.3" y1="275.3" x2="445.3" y2="306.9" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="279.3" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="449.3" y1="240.5" x2="449.3" y2="288.0" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="252.3" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="453.2" y1="251.6" x2="453.2" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="251.6" width="2.45" height="116.8" fill="var(--down)"/>
<line x1="457.2" y1="356.2" x2="457.2" y2="401.1" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="383.4" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="461.1" y1="319.8" x2="461.1" y2="357.8" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="328.8" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="465.1" y1="277.0" x2="465.1" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="296.3" width="2.45" height="30.3" fill="var(--up)"/>
<line x1="469.1" y1="293.5" x2="469.1" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="293.5" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="473.0" y1="287.2" x2="473.0" y2="345.9" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="296.3" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="477.0" y1="280.0" x2="477.0" y2="332.1" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="296.2" width="2.45" height="34.1" fill="var(--down)"/>
<line x1="480.9" y1="297.5" x2="480.9" y2="350.6" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="310.8" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="484.9" y1="295.8" x2="484.9" y2="335.7" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="307.0" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="488.8" y1="279.5" x2="488.8" y2="313.1" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="294.8" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="492.8" y1="261.5" x2="492.8" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="262.4" width="2.45" height="41.4" fill="var(--up)"/>
<line x1="496.7" y1="242.1" x2="496.7" y2="297.4" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="269.8" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="500.7" y1="279.5" x2="500.7" y2="326.4" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="290.7" width="2.45" height="31.4" fill="var(--down)"/>
<line x1="504.6" y1="224.7" x2="504.6" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="248.9" width="2.45" height="40.5" fill="var(--down)"/>
<line x1="508.6" y1="251.4" x2="508.6" y2="290.8" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="266.8" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="512.5" y1="252.0" x2="512.5" y2="307.0" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="260.0" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="516.5" y1="270.7" x2="516.5" y2="298.5" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="279.6" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="520.4" y1="208.8" x2="520.4" y2="286.8" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="221.0" width="2.45" height="65.6" fill="var(--up)"/>
<line x1="524.4" y1="241.9" x2="524.4" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="251.9" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="528.3" y1="263.2" x2="528.3" y2="307.4" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="280.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="532.3" y1="289.5" x2="532.3" y2="368.8" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="299.1" width="2.45" height="39.1" fill="var(--down)"/>
<line x1="536.2" y1="320.0" x2="536.2" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="339.7" width="2.45" height="29.2" fill="var(--up)"/>
<line x1="540.2" y1="304.6" x2="540.2" y2="350.9" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="310.9" width="2.45" height="35.7" fill="var(--up)"/>
<line x1="544.1" y1="299.5" x2="544.1" y2="337.3" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="313.2" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="548.1" y1="317.9" x2="548.1" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="335.5" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="552.0" y1="315.9" x2="552.0" y2="363.4" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="325.2" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="556.0" y1="309.6" x2="556.0" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="313.1" width="2.45" height="32.8" fill="var(--down)"/>
<line x1="560.0" y1="279.8" x2="560.0" y2="328.1" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="287.0" width="2.45" height="41.1" fill="var(--up)"/>
<line x1="563.9" y1="267.6" x2="563.9" y2="296.7" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="271.3" width="2.45" height="21.8" fill="var(--up)"/>
<line x1="567.9" y1="243.1" x2="567.9" y2="276.8" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="262.9" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="571.8" y1="241.1" x2="571.8" y2="310.0" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="256.5" width="2.45" height="45.2" fill="var(--up)"/>
<line x1="575.8" y1="248.7" x2="575.8" y2="328.6" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="259.1" width="2.45" height="55.4" fill="var(--down)"/>
<line x1="579.7" y1="255.9" x2="579.7" y2="314.1" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="286.0" width="2.45" height="28.1" fill="var(--up)"/>
<line x1="583.7" y1="266.6" x2="583.7" y2="300.5" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="286.5" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="587.6" y1="188.5" x2="587.6" y2="258.5" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="189.4" width="2.45" height="60.2" fill="var(--up)"/>
<line x1="591.6" y1="202.4" x2="591.6" y2="287.9" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="214.0" width="2.45" height="70.6" fill="var(--down)"/>
<line x1="595.5" y1="268.5" x2="595.5" y2="301.9" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="297.4" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="599.5" y1="288.6" x2="599.5" y2="374.5" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="289.6" width="2.45" height="70.4" fill="var(--down)"/>
<line x1="603.4" y1="281.0" x2="603.4" y2="344.9" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="288.0" width="2.45" height="52.5" fill="var(--up)"/>
<line x1="607.4" y1="223.3" x2="607.4" y2="276.2" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="241.5" width="2.45" height="34.8" fill="var(--up)"/>
<line x1="611.3" y1="207.7" x2="611.3" y2="284.7" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="229.3" width="2.45" height="44.6" fill="var(--up)"/>
<line x1="615.3" y1="208.2" x2="615.3" y2="232.6" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="217.4" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="619.2" y1="212.0" x2="619.2" y2="247.7" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="224.7" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="623.2" y1="127.7" x2="623.2" y2="178.9" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="135.5" width="2.45" height="43.0" fill="var(--up)"/>
<line x1="627.1" y1="101.3" x2="627.1" y2="144.1" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="137.6" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="631.1" y1="124.8" x2="631.1" y2="154.0" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="143.3" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="635.0" y1="121.5" x2="635.0" y2="156.6" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="129.6" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="639.0" y1="91.5" x2="639.0" y2="125.7" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="99.2" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="642.9" y1="87.2" x2="642.9" y2="115.6" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="98.4" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="646.9" y1="79.4" x2="646.9" y2="143.0" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="89.5" width="2.45" height="51.4" fill="var(--down)"/>
<line x1="650.9" y1="99.4" x2="650.9" y2="132.1" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="113.1" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="654.8" y1="109.8" x2="654.8" y2="165.0" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="117.5" width="2.45" height="37.8" fill="var(--down)"/>
<line x1="658.8" y1="146.0" x2="658.8" y2="223.6" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="151.0" width="2.45" height="69.0" fill="var(--down)"/>
<line x1="662.7" y1="174.2" x2="662.7" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="196.6" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="666.7" y1="165.3" x2="666.7" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="170.5" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="670.6" y1="157.9" x2="670.6" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="167.8" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="674.6" y1="178.9" x2="674.6" y2="217.9" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="184.4" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="678.5" y1="195.1" x2="678.5" y2="246.0" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="210.4" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="682.5" y1="222.3" x2="682.5" y2="281.5" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="222.4" width="2.45" height="45.5" fill="var(--down)"/>
<line x1="686.4" y1="217.4" x2="686.4" y2="265.6" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="221.5" width="2.45" height="36.8" fill="var(--up)"/>
<line x1="690.4" y1="211.0" x2="690.4" y2="240.4" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="218.1" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="694.3" y1="195.6" x2="694.3" y2="225.2" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="216.6" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="698.3" y1="161.5" x2="698.3" y2="296.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="213.8" width="2.45" height="64.9" fill="var(--down)"/>
<line x1="702.2" y1="224.9" x2="702.2" y2="279.8" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="228.1" width="2.45" height="37.7" fill="var(--up)"/>
<line x1="706.2" y1="222.4" x2="706.2" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="223.6" width="2.45" height="34.2" fill="var(--down)"/>
<line x1="710.1" y1="237.8" x2="710.1" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="241.9" width="2.45" height="41.4" fill="var(--down)"/>
<line x1="714.1" y1="245.4" x2="714.1" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="252.7" width="2.45" height="51.1" fill="var(--up)"/>
<line x1="718.0" y1="269.7" x2="718.0" y2="306.6" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="273.2" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="722.0" y1="259.1" x2="722.0" y2="306.6" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="274.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="725.9" y1="248.3" x2="725.9" y2="284.9" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="251.9" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="729.9" y1="262.8" x2="729.9" y2="300.5" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="267.1" width="2.45" height="19.6" fill="var(--down)"/>
<line x1="733.8" y1="278.6" x2="733.8" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="278.7" width="2.45" height="23.5" fill="var(--down)"/>
<line x1="737.8" y1="306.0" x2="737.8" y2="352.2" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="319.0" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="741.8" y1="289.6" x2="741.8" y2="321.4" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="298.2" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="745.7" y1="291.4" x2="745.7" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="299.0" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="749.7" y1="278.3" x2="749.7" y2="303.3" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="287.6" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="753.6" y1="263.7" x2="753.6" y2="300.5" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="267.1" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="757.6" y1="287.9" x2="757.6" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="289.1" width="2.45" height="29.8" fill="var(--down)"/>
<line x1="761.5" y1="310.8" x2="761.5" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="317.1" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="765.5" y1="313.4" x2="765.5" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="314.6" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="769.4" y1="360.3" x2="769.4" y2="399.3" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="369.0" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="773.4" y1="377.7" x2="773.4" y2="406.4" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="383.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="777.3" y1="383.1" x2="777.3" y2="410.9" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="391.5" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="781.3" y1="364.7" x2="781.3" y2="407.9" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="364.7" width="2.45" height="39.1" fill="var(--up)"/>
<line x1="785.2" y1="367.7" x2="785.2" y2="402.1" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="375.9" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="789.2" y1="372.8" x2="789.2" y2="393.0" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="372.8" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="793.1" y1="349.4" x2="793.1" y2="427.8" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="374.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="797.1" y1="370.1" x2="797.1" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="382.9" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="801.0" y1="341.4" x2="801.0" y2="408.9" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="342.8" width="2.45" height="63.0" fill="var(--up)"/>
<line x1="805.0" y1="320.8" x2="805.0" y2="352.6" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="332.6" width="2.45" height="17.0" fill="var(--down)"/>
<line x1="808.9" y1="318.4" x2="808.9" y2="349.0" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="321.4" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="812.9" y1="313.0" x2="812.9" y2="342.5" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="330.2" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="816.8" y1="282.7" x2="816.8" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="295.9" width="2.45" height="33.9" fill="var(--up)"/>
<line x1="820.8" y1="252.0" x2="820.8" y2="297.5" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="272.4" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="824.7" y1="232.0" x2="824.7" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="257.2" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="828.7" y1="227.1" x2="828.7" y2="290.7" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="257.8" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="832.7" y1="250.4" x2="832.7" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="258.9" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="836.6" y1="251.5" x2="836.6" y2="296.2" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="271.2" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="840.6" y1="301.3" x2="840.6" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="313.1" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="844.5" y1="316.9" x2="844.5" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="328.0" width="2.45" height="45.2" fill="var(--down)"/>
<line x1="848.5" y1="341.3" x2="848.5" y2="370.5" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="343.0" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="852.4" y1="341.1" x2="852.4" y2="362.5" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="348.6" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="856.4" y1="324.8" x2="856.4" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="348.3" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="860.3" y1="324.3" x2="860.3" y2="360.1" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="330.4" width="2.45" height="29.7" fill="var(--up)"/>
<line x1="864.3" y1="339.2" x2="864.3" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="345.6" width="2.45" height="45.2" fill="var(--down)"/>
<line x1="868.2" y1="386.1" x2="868.2" y2="422.0" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="401.9" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="872.2" y1="373.2" x2="872.2" y2="399.6" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="385.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="876.1" y1="376.4" x2="876.1" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="386.8" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="880.1" y1="399.3" x2="880.1" y2="447.0" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="403.8" width="2.45" height="37.0" fill="var(--down)"/>
<line x1="884.0" y1="409.5" x2="884.0" y2="433.3" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="415.9" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="888.0" y1="405.5" x2="888.0" y2="452.8" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="415.9" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="891.9" y1="447.3" x2="891.9" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="455.4" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="895.9" y1="453.5" x2="895.9" y2="493.7" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="474.1" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="899.8" y1="453.5" x2="899.8" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="463.2" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="903.8" y1="458.4" x2="903.8" y2="490.1" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="463.4" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="907.7" y1="429.6" x2="907.7" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="451.8" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="911.7" y1="422.0" x2="911.7" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="443.4" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="915.6" y1="434.1" x2="915.6" y2="457.5" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="441.3" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="919.6" y1="416.2" x2="919.6" y2="463.9" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="433.2" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="923.6" y1="458.9" x2="923.6" y2="506.1" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="458.9" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="927.5" y1="491.9" x2="927.5" y2="552.8" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="491.9" width="2.45" height="59.0" fill="var(--down)"/>
<line x1="931.5" y1="500.7" x2="931.5" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="505.4" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="935.4" y1="478.1" x2="935.4" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="488.0" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="939.4" y1="453.7" x2="939.4" y2="497.7" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="459.5" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="943.3" y1="433.2" x2="943.3" y2="475.6" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="461.1" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="947.3" y1="461.5" x2="947.3" y2="490.5" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="469.5" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="951.2" y1="466.5" x2="951.2" y2="501.3" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="491.9" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="955.2" y1="473.3" x2="955.2" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="481.3" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="959.1" y1="469.5" x2="959.1" y2="487.4" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="475.3" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="963.1" y1="463.2" x2="963.1" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="476.4" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="967.0" y1="455.6" x2="967.0" y2="489.8" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="461.1" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="971.0" y1="460.0" x2="971.0" y2="496.2" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="467.0" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="974.9" y1="461.1" x2="974.9" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="462.7" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="978.9" y1="455.0" x2="978.9" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="465.3" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="982.8" y1="485.8" x2="982.8" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="491.3" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="986.8" y1="506.6" x2="986.8" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="507.3" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="990.7" y1="528.4" x2="990.7" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="529.3" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="994.7" y1="538.7" x2="994.7" y2="557.4" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="542.3" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="998.6" y1="554.8" x2="998.6" y2="597.1" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="561.8" width="2.45" height="33.4" fill="var(--down)"/>
<line x1="1002.6" y1="577.9" x2="1002.6" y2="605.1" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="582.4" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="1006.5" y1="557.2" x2="1006.5" y2="590.0" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="574.8" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="1010.5" y1="542.7" x2="1010.5" y2="567.1" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="556.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="1014.5" y1="557.5" x2="1014.5" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="557.5" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="1018.4" y1="577.7" x2="1018.4" y2="588.2" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="579.7" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="1022.4" y1="527.3" x2="1022.4" y2="586.9" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="528.0" width="2.45" height="58.9" fill="var(--up)"/>
<line x1="1026.3" y1="531.1" x2="1026.3" y2="570.1" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="531.1" width="2.45" height="29.7" fill="var(--down)"/>
<line x1="1030.3" y1="526.5" x2="1030.3" y2="553.0" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="535.2" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="1034.2" y1="525.9" x2="1034.2" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="545.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="1038.2" y1="520.3" x2="1038.2" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="534.3" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="1042.1" y1="532.6" x2="1042.1" y2="555.5" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="535.0" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="1046.1" y1="547.8" x2="1046.1" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="567.3" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="1050.0" y1="568.5" x2="1050.0" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="568.5" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="60" y1="430.9" x2="1052" y2="430.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="434.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$179 R1</text>
<text x="1058" y="446.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="209.3" x2="1052" y2="209.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="212.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$219 R2</text>
<text x="1058" y="224.8" font-size="9.5" fill="var(--muted)">터치 7회</text>
<circle cx="1052.0" cy="591.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="583.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $150 (2026-09-11)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $219 | 7 | 2025-10-16·2025-10-30·2026-01-16·2026-01-29·2026-03-02·2026-03-25·2026-06-23 — **최근 1년 중 가장 두꺼운 클러스터**(터치 7회). 2025년 4분기부터 2026년 6월까지 8개월에 걸쳐 반복적으로 되밀린 구간으로, 이 기간 주가의 사실상 상단이었다 |
| R1 | $179 | 4 | 2025-12-23·2026-07-27·2026-08-04·2026-08-17 — 2026년 7~8월에 세 차례 몰려 있다. R2($219)가 무너진 뒤 형성된 **한 단계 낮은 저항대**로, 8월 중순 이후 이 아래로 이탈해 현재에 이른다 |
| **현재가** | **$150.12** (2026-09-11 종가) | — | **기간 내 하단 지지 없음(1년 신저가 구간)** — 가장 가까운 유효 레벨은 위쪽 R1($179)뿐 |
| 참고선 | $147.74 | — | 최근 1년 최저가(2026-09월 중 기록). 스윙 클러스터가 아니라 단일 저점이라 지지대로 보지 않는다 — 현재가가 이보다 1.6% 위에 있을 뿐이다 |
| 참고선 | $241.82 | — | 최근 1년 최고가. 현재가 대비 **+61.1%** 위에 있어 근시일 저항으로서의 의미는 없고, 밸류에이션 논의의 기준점(현재가는 52주 최고 대비 −37.9%)으로만 쓴다 |

> 유효 클러스터가 저항 2개뿐이고 **지지가 하나도 잡히지 않았다** — 최근 1년 구간의 최저가 부근에서 거래되고 있어 아래쪽에 반복 터치된 가격대가 존재하지 않기 때문이다. 레벨 개수를 3개로 맞추기 위해 억지로 넣지 않았다.

---

## 3. 관측된 특이 구간 — 2026년 8~9월 원자력 섹터 재평가

- 개별 이벤트가 아니라 **약 4주에 걸친 연속적 하락 구간**이다. 2026-08-17 종가 $172.86에서 2026-09-11 $150.12까지 **−13.2%** 밀렸고, 같은 기간 52주 최고($241.82) 대비로는 −37.9%가 됐다.
- 특이한 것은 **이 하락 구간에 회사 고유 악재가 없었다**는 점이다. 오히려 2026-08-26 미 육군 Janus 프로그램 선정(포트캠벨 20MW BANR), 2026-09-03 NNSA 리튬처리시설 개념설계 수주라는 호재가 나왔고 주가는 그때마다 단기 반등했다가 다시 밀렸다([최근 뉴스 / 이슈](./08_news.md)).
- 2026-09-11에는 원자력주 전반이 동반 하락했는데 같은 날 S&P 500은 +0.9% 상승했다 — **개별 종목이 아니라 섹터 단위의 재평가**임을 시사한다.
- 이 구간의 결과로 R1($179)이 저항으로 굳어졌고, 그 아래에는 참조할 스윙 구조가 없다. 즉 **현재 가격대는 "지난 1년간 거래된 적이 거의 없는 구간"**이며, 이 상태에서 기술적 레벨은 설명력이 약하다 — [밸류에이션 / 적정주가](./06_valuation.md)와 [투자 판단](./07_investment.md)의 펀더멘털 기준이 우선한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-12~2026-09-11. 수집 시점: 2026-09-13. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py BWXT --name "BWX Technologies" --close-on 2026-09-11 --emit all` (기본 파라미터, `--force-level` 미사용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **이 문서에서 특히 중요한 한계**: 현재가가 1년 최저 부근이라 **하단 지지 클러스터가 0개**다. 위쪽 저항 2개만으로 가격 구조를 읽어야 하므로, "어디까지 빠질 수 있는가"에 대해 이 문서는 아무 정보도 주지 않는다.
    - 기간 내 배당이 4회 지급됐으나 **원주가 기준이라 배당은 반영되지 않았다**(분기 $0.25~$0.27). 총수익률 기준으로 보면 실제 손실폭은 위 수치보다 약 0.7%p 작다.
    - 기간 내 주식분할·병합은 없었고(소급조정 불필요), 희석주식수도 91.7~92.0백만 주로 사실상 고정이라 유상증자 등 가격 연속성을 깨는 이벤트도 없다.

---

*작성일: 2026-09-13*
