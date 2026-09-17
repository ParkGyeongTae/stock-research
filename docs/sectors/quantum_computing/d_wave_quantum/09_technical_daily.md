# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-10 종가 **$16.66**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-11 ~ 2026-09-10)

<style>
.qbts-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .qbts-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.qbts-chart svg { width:100%; height:auto; display:block; }
.qbts-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.qbts-chart .title { fill: var(--ink); font-weight:600; }
.qbts-chart .grid { stroke: var(--grid); stroke-width:1; }
.qbts-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="qbts-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="D-Wave Quantum(QBTS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">D-Wave Quantum (QBTS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-11 ~ 2026-09-10 · 마지막 종가 $16.66 (2026-09-10) · 단위 USD</text>
<line x1="60" y1="571.3" x2="1052" y2="571.3" class="grid"/>
<text x="52" y="575.3" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="493.3" x2="1052" y2="493.3" class="grid"/>
<text x="52" y="497.3" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="415.2" x2="1052" y2="415.2" class="grid"/>
<text x="52" y="419.2" font-size="11" text-anchor="end" fill="var(--muted)">25</text>
<line x1="60" y1="337.1" x2="1052" y2="337.1" class="grid"/>
<text x="52" y="341.1" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="259.0" x2="1052" y2="259.0" class="grid"/>
<text x="52" y="263.0" font-size="11" text-anchor="end" fill="var(--muted)">35</text>
<line x1="60" y1="180.9" x2="1052" y2="180.9" class="grid"/>
<text x="52" y="184.9" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="102.8" x2="1052" y2="102.8" class="grid"/>
<text x="52" y="106.8" font-size="11" text-anchor="end" fill="var(--muted)">45</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="117.3" y1="626.0" x2="117.3" y2="631.0" class="axis"/>
<text x="117.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="208.2" y1="626.0" x2="208.2" y2="631.0" class="axis"/>
<text x="208.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="283.3" y1="626.0" x2="283.3" y2="631.0" class="axis"/>
<text x="283.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="370.2" y1="626.0" x2="370.2" y2="631.0" class="axis"/>
<text x="370.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="449.3" y1="626.0" x2="449.3" y2="631.0" class="axis"/>
<text x="449.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="524.4" y1="626.0" x2="524.4" y2="631.0" class="axis"/>
<text x="524.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="611.3" y1="626.0" x2="611.3" y2="631.0" class="axis"/>
<text x="611.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="694.3" y1="626.0" x2="694.3" y2="631.0" class="axis"/>
<text x="694.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="773.4" y1="626.0" x2="773.4" y2="631.0" class="axis"/>
<text x="773.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="856.4" y1="626.0" x2="856.4" y2="631.0" class="axis"/>
<text x="856.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="943.3" y1="626.0" x2="943.3" y2="631.0" class="axis"/>
<text x="943.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1026.3" y1="626.0" x2="1026.3" y2="631.0" class="axis"/>
<text x="1026.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="544.5" x2="62.0" y2="556.4" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="547.6" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="65.9" y1="524.8" x2="65.9" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="528.2" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="69.9" y1="515.4" x2="69.9" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="519.5" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="73.8" y1="506.1" x2="73.8" y2="526.1" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="509.2" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="77.8" y1="448.8" x2="77.8" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="453.6" width="2.45" height="55.6" fill="var(--up)"/>
<line x1="81.7" y1="417.5" x2="81.7" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="430.5" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="85.7" y1="378.8" x2="85.7" y2="441.4" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="385.8" width="2.45" height="55.6" fill="var(--up)"/>
<line x1="89.6" y1="395.5" x2="89.6" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="404.7" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="93.6" y1="368.5" x2="93.6" y2="405.8" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="375.8" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="97.5" y1="349.9" x2="97.5" y2="393.9" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="361.5" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="101.5" y1="378.9" x2="101.5" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="394.3" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="105.5" y1="360.5" x2="105.5" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="387.7" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="109.4" y1="359.4" x2="109.4" y2="415.6" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="383.6" width="2.45" height="26.7" fill="var(--down)"/>
<line x1="113.4" y1="407.8" x2="113.4" y2="435.9" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="416.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="117.3" y1="402.4" x2="117.3" y2="432.2" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="405.3" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="121.3" y1="343.2" x2="121.3" y2="399.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="349.4" width="2.45" height="47.0" fill="var(--up)"/>
<line x1="125.2" y1="285.9" x2="125.2" y2="337.9" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="294.9" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="129.2" y1="236.9" x2="129.2" y2="308.2" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="258.7" width="2.45" height="47.0" fill="var(--up)"/>
<line x1="133.1" y1="213.7" x2="133.1" y2="277.0" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="228.4" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="137.1" y1="188.0" x2="137.1" y2="297.9" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="241.5" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="141.0" y1="233.4" x2="141.0" y2="280.9" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="257.9" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="145.0" y1="245.9" x2="145.0" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="248.4" width="2.45" height="41.5" fill="var(--down)"/>
<line x1="148.9" y1="150.2" x2="148.9" y2="296.2" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="171.2" width="2.45" height="99.0" fill="var(--up)"/>
<line x1="152.9" y1="98.2" x2="152.9" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="133.1" width="2.45" height="39.7" fill="var(--up)"/>
<line x1="156.8" y1="75.5" x2="156.8" y2="161.9" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="81.0" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="160.8" y1="100.8" x2="160.8" y2="186.7" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="107.5" width="2.45" height="66.2" fill="var(--down)"/>
<line x1="164.7" y1="189.2" x2="164.7" y2="242.5" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="204.4" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="168.7" y1="185.9" x2="168.7" y2="282.1" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="188.4" width="2.45" height="80.0" fill="var(--down)"/>
<line x1="172.6" y1="274.9" x2="172.6" y2="319.6" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="280.6" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="176.6" y1="316.6" x2="176.6" y2="393.8" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="335.4" width="2.45" height="44.0" fill="var(--down)"/>
<line x1="180.5" y1="283.5" x2="180.5" y2="342.4" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="296.5" width="2.45" height="24.0" fill="var(--down)"/>
<line x1="184.5" y1="256.0" x2="184.5" y2="301.2" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="287.2" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="188.4" y1="223.4" x2="188.4" y2="286.7" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="258.4" width="2.45" height="16.4" fill="var(--up)"/>
<line x1="192.4" y1="234.5" x2="192.4" y2="308.2" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="254.4" width="2.45" height="51.5" fill="var(--down)"/>
<line x1="196.4" y1="264.5" x2="196.4" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="270.6" width="2.45" height="27.9" fill="var(--up)"/>
<line x1="200.3" y1="231.1" x2="200.3" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="241.7" width="2.45" height="50.0" fill="var(--up)"/>
<line x1="204.3" y1="221.0" x2="204.3" y2="258.2" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="226.8" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="208.2" y1="218.1" x2="208.2" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="221.2" width="2.45" height="67.6" fill="var(--down)"/>
<line x1="212.2" y1="297.6" x2="212.2" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="321.2" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="216.1" y1="311.6" x2="216.1" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="321.2" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="220.1" y1="326.3" x2="220.1" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="329.4" width="2.45" height="32.9" fill="var(--down)"/>
<line x1="224.0" y1="341.5" x2="224.0" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="344.9" width="2.45" height="32.3" fill="var(--up)"/>
<line x1="228.0" y1="312.1" x2="228.0" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="335.4" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="231.9" y1="336.8" x2="231.9" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="352.9" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="235.9" y1="343.8" x2="235.9" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="355.5" width="2.45" height="37.8" fill="var(--down)"/>
<line x1="239.8" y1="407.4" x2="239.8" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="407.7" width="2.45" height="32.6" fill="var(--down)"/>
<line x1="243.8" y1="415.3" x2="243.8" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="436.9" width="2.45" height="31.7" fill="var(--up)"/>
<line x1="247.7" y1="431.9" x2="247.7" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="442.8" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="251.7" y1="439.4" x2="251.7" y2="464.5" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="447.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="255.6" y1="423.9" x2="255.6" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="439.5" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="259.6" y1="420.0" x2="259.6" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="431.3" width="2.45" height="54.0" fill="var(--down)"/>
<line x1="263.5" y1="481.5" x2="263.5" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="486.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="267.5" y1="441.1" x2="267.5" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="444.7" width="2.45" height="40.4" fill="var(--up)"/>
<line x1="271.4" y1="447.8" x2="271.4" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="452.8" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="275.4" y1="446.7" x2="275.4" y2="462.0" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="451.3" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="279.3" y1="447.1" x2="279.3" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="450.3" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="283.3" y1="458.2" x2="283.3" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="461.9" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="287.3" y1="447.9" x2="287.3" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="454.2" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="291.2" y1="410.7" x2="291.2" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="413.9" width="2.45" height="34.7" fill="var(--up)"/>
<line x1="295.2" y1="354.3" x2="295.2" y2="419.9" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="356.9" width="2.45" height="57.5" fill="var(--up)"/>
<line x1="299.1" y1="354.6" x2="299.1" y2="396.4" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="359.4" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="303.1" y1="350.4" x2="303.1" y2="389.6" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="361.5" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="307.0" y1="356.5" x2="307.0" y2="381.9" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="363.2" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="311.0" y1="359.3" x2="311.0" y2="388.3" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="365.5" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="314.9" y1="360.7" x2="314.9" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="368.6" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="318.9" y1="366.3" x2="318.9" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="374.9" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="322.8" y1="389.7" x2="322.8" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="393.3" width="2.45" height="41.5" fill="var(--down)"/>
<line x1="326.8" y1="406.0" x2="326.8" y2="433.1" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="407.1" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="330.7" y1="379.4" x2="330.7" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="399.6" width="2.45" height="34.4" fill="var(--down)"/>
<line x1="334.7" y1="402.1" x2="334.7" y2="427.4" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="416.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="338.6" y1="383.0" x2="338.6" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="386.8" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="342.6" y1="299.8" x2="342.6" y2="374.3" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="302.9" width="2.45" height="70.7" fill="var(--up)"/>
<line x1="346.5" y1="307.7" x2="346.5" y2="358.2" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="327.6" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="350.5" y1="342.1" x2="350.5" y2="384.9" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="342.6" width="2.45" height="33.3" fill="var(--down)"/>
<line x1="354.4" y1="376.1" x2="354.4" y2="418.8" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="376.1" width="2.45" height="34.5" fill="var(--down)"/>
<line x1="358.4" y1="387.7" x2="358.4" y2="414.1" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="397.2" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="362.3" y1="376.3" x2="362.3" y2="399.2" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="391.1" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="366.3" y1="377.2" x2="366.3" y2="399.1" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="397.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="370.2" y1="362.9" x2="370.2" y2="408.5" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="366.3" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="374.2" y1="316.3" x2="374.2" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="327.1" width="2.45" height="31.0" fill="var(--up)"/>
<line x1="378.2" y1="315.5" x2="378.2" y2="347.4" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="317.3" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="382.1" y1="303.4" x2="382.1" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="319.9" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="386.1" y1="329.6" x2="386.1" y2="358.2" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="339.2" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="390.0" y1="319.3" x2="390.0" y2="367.2" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="340.7" width="2.45" height="25.9" fill="var(--down)"/>
<line x1="394.0" y1="355.2" x2="394.0" y2="375.7" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="355.8" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="397.9" y1="341.3" x2="397.9" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="350.4" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="401.9" y1="334.3" x2="401.9" y2="376.0" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="334.8" width="2.45" height="26.7" fill="var(--up)"/>
<line x1="405.8" y1="315.9" x2="405.8" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="329.6" width="2.45" height="27.5" fill="var(--down)"/>
<line x1="409.8" y1="335.1" x2="409.8" y2="364.1" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="351.9" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="413.7" y1="360.8" x2="413.7" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="375.0" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="417.7" y1="366.0" x2="417.7" y2="419.2" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="375.0" width="2.45" height="23.9" fill="var(--down)"/>
<line x1="421.6" y1="374.7" x2="421.6" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="377.2" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="425.6" y1="380.8" x2="425.6" y2="411.5" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="384.7" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="429.5" y1="399.1" x2="429.5" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="405.8" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="433.5" y1="415.5" x2="433.5" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="419.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="437.4" y1="404.4" x2="437.4" y2="422.6" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="415.6" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="441.4" y1="414.8" x2="441.4" y2="454.7" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="423.0" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="445.3" y1="444.1" x2="445.3" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="445.9" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="449.3" y1="469.1" x2="449.3" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="469.5" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="453.2" y1="468.7" x2="453.2" y2="490.0" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="469.2" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="457.2" y1="472.5" x2="457.2" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="472.5" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="461.1" y1="499.2" x2="461.1" y2="541.4" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="503.7" width="2.45" height="33.1" fill="var(--down)"/>
<line x1="465.1" y1="478.0" x2="465.1" y2="527.0" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="482.0" width="2.45" height="44.0" fill="var(--up)"/>
<line x1="469.1" y1="472.3" x2="469.1" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="474.4" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="473.0" y1="469.5" x2="473.0" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="481.1" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="477.0" y1="481.5" x2="477.0" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="481.5" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="480.9" y1="497.3" x2="480.9" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="499.7" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="484.9" y1="492.2" x2="484.9" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="498.4" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="488.8" y1="504.2" x2="488.8" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="507.3" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="492.8" y1="499.2" x2="492.8" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="507.8" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="496.7" y1="501.2" x2="496.7" y2="518.7" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="502.9" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="500.7" y1="503.3" x2="500.7" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="510.1" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="504.6" y1="518.9" x2="504.6" y2="533.7" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="523.7" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="508.6" y1="510.8" x2="508.6" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="514.2" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="512.5" y1="496.2" x2="512.5" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="498.7" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="516.5" y1="466.7" x2="516.5" y2="497.6" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="482.8" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="520.4" y1="501.1" x2="520.4" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="502.4" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="524.4" y1="509.4" x2="524.4" y2="527.1" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="509.8" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="528.3" y1="513.4" x2="528.3" y2="532.9" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="520.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="532.3" y1="507.8" x2="532.3" y2="521.7" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="510.3" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="536.2" y1="511.1" x2="536.2" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="511.5" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="540.2" y1="499.4" x2="540.2" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="515.3" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="544.1" y1="507.3" x2="544.1" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="508.3" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="548.1" y1="500.8" x2="548.1" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="504.7" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="552.0" y1="501.5" x2="552.0" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="510.3" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="556.0" y1="512.2" x2="556.0" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="516.1" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="560.0" y1="513.7" x2="560.0" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="522.6" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="563.9" y1="517.9" x2="563.9" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="524.8" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="567.9" y1="528.5" x2="567.9" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="532.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="571.8" y1="535.1" x2="571.8" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="536.2" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="575.8" y1="549.8" x2="575.8" y2="565.7" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="554.2" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="579.7" y1="554.9" x2="579.7" y2="567.9" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="558.2" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="583.7" y1="548.5" x2="583.7" y2="562.8" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="550.9" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="587.6" y1="551.3" x2="587.6" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="554.8" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="591.6" y1="544.4" x2="591.6" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="551.7" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="595.5" y1="558.3" x2="595.5" y2="578.1" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="559.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="599.5" y1="577.1" x2="599.5" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="579.0" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="603.4" y1="588.6" x2="603.4" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="589.9" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="607.4" y1="579.3" x2="607.4" y2="600.5" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="580.2" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="611.3" y1="571.5" x2="611.3" y2="592.4" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="573.8" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="615.3" y1="581.1" x2="615.3" y2="602.4" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="582.0" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="619.2" y1="576.5" x2="619.2" y2="590.4" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="583.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="623.2" y1="587.7" x2="623.2" y2="596.6" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="588.2" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="627.1" y1="565.9" x2="627.1" y2="585.4" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="567.4" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="631.1" y1="577.4" x2="631.1" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="580.7" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="635.0" y1="574.9" x2="635.0" y2="586.4" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="583.1" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="639.0" y1="574.7" x2="639.0" y2="589.9" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="576.8" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="642.9" y1="538.8" x2="642.9" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="540.6" width="2.45" height="26.2" fill="var(--up)"/>
<line x1="646.9" y1="477.0" x2="646.9" y2="528.1" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="480.6" width="2.45" height="35.7" fill="var(--up)"/>
<line x1="650.9" y1="454.7" x2="650.9" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="462.0" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="654.8" y1="454.4" x2="654.8" y2="471.6" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="465.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="658.8" y1="463.1" x2="658.8" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="467.3" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="662.7" y1="464.4" x2="662.7" y2="488.9" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="464.8" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="666.7" y1="465.2" x2="666.7" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="473.9" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="670.6" y1="475.2" x2="670.6" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="483.1" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="674.6" y1="498.3" x2="674.6" y2="526.1" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="498.4" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="678.5" y1="509.0" x2="678.5" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="512.0" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="682.5" y1="517.5" x2="682.5" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="522.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="686.4" y1="518.1" x2="686.4" y2="538.4" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="520.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="690.4" y1="487.6" x2="690.4" y2="521.1" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="488.9" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="694.3" y1="482.9" x2="694.3" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="485.6" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="698.3" y1="466.4" x2="698.3" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="478.9" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="702.2" y1="466.7" x2="702.2" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="469.2" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="706.2" y1="430.2" x2="706.2" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="433.4" width="2.45" height="29.8" fill="var(--up)"/>
<line x1="710.1" y1="435.8" x2="710.1" y2="465.0" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="445.6" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="714.1" y1="451.6" x2="714.1" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="453.1" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="718.0" y1="418.6" x2="718.0" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="430.3" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="722.0" y1="432.2" x2="722.0" y2="479.5" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="455.5" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="725.9" y1="455.9" x2="725.9" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="456.1" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="729.9" y1="453.8" x2="729.9" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="460.0" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="733.8" y1="473.7" x2="733.8" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="475.5" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="737.8" y1="490.1" x2="737.8" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="491.5" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="741.8" y1="506.8" x2="741.8" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="512.5" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="745.7" y1="501.8" x2="745.7" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="504.2" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="749.7" y1="402.2" x2="749.7" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="403.6" width="2.45" height="62.2" fill="var(--up)"/>
<line x1="753.6" y1="312.9" x2="753.6" y2="397.8" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="346.5" width="2.45" height="47.8" fill="var(--up)"/>
<line x1="757.6" y1="345.2" x2="757.6" y2="394.4" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="347.2" width="2.45" height="23.9" fill="var(--down)"/>
<line x1="761.5" y1="367.5" x2="761.5" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="376.4" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="765.5" y1="333.7" x2="765.5" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="345.1" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="769.4" y1="334.6" x2="769.4" y2="377.4" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="334.9" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="773.4" y1="319.6" x2="773.4" y2="371.0" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="349.9" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="777.3" y1="316.8" x2="777.3" y2="352.9" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="338.5" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="781.3" y1="337.9" x2="781.3" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="345.1" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="785.2" y1="355.5" x2="785.2" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="374.0" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="789.2" y1="390.3" x2="789.2" y2="442.0" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="390.8" width="2.45" height="42.3" fill="var(--down)"/>
<line x1="793.1" y1="388.2" x2="793.1" y2="430.8" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="402.2" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="797.1" y1="389.3" x2="797.1" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="403.4" width="2.45" height="34.9" fill="var(--down)"/>
<line x1="801.0" y1="418.6" x2="801.0" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="442.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="805.0" y1="424.4" x2="805.0" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="433.6" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="808.9" y1="423.3" x2="808.9" y2="448.6" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="436.5" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="812.9" y1="381.6" x2="812.9" y2="416.6" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="395.5" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="816.8" y1="397.8" x2="816.8" y2="432.6" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="403.5" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="820.8" y1="422.2" x2="820.8" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="428.5" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="824.7" y1="419.7" x2="824.7" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="420.0" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="828.7" y1="405.3" x2="828.7" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="423.5" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="832.7" y1="388.5" x2="832.7" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="414.7" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="836.6" y1="424.1" x2="836.6" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="424.2" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="840.6" y1="433.8" x2="840.6" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="438.6" width="2.45" height="24.8" fill="var(--down)"/>
<line x1="844.5" y1="448.6" x2="844.5" y2="478.7" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="450.2" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="848.5" y1="426.7" x2="848.5" y2="454.8" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="433.4" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="852.4" y1="419.4" x2="852.4" y2="442.5" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="431.0" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="856.4" y1="422.4" x2="856.4" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="437.1" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="860.3" y1="420.2" x2="860.3" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="436.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="864.3" y1="436.7" x2="864.3" y2="458.1" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="453.3" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="868.2" y1="455.9" x2="868.2" y2="485.1" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="459.5" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="872.2" y1="470.0" x2="872.2" y2="491.2" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="483.3" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="876.1" y1="470.1" x2="876.1" y2="485.1" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="475.1" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="880.1" y1="467.6" x2="880.1" y2="494.0" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="470.1" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="884.0" y1="498.1" x2="884.0" y2="516.4" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="498.1" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="888.0" y1="504.9" x2="888.0" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="509.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="891.9" y1="503.1" x2="891.9" y2="526.5" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="508.3" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="895.9" y1="524.5" x2="895.9" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="524.5" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="899.8" y1="533.6" x2="899.8" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="544.3" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="903.8" y1="531.5" x2="903.8" y2="545.0" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="540.1" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="907.7" y1="524.2" x2="907.7" y2="540.1" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="527.6" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="911.7" y1="525.0" x2="911.7" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="530.7" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="915.6" y1="526.8" x2="915.6" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="538.5" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="919.6" y1="539.5" x2="919.6" y2="552.9" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="540.0" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="923.6" y1="500.4" x2="923.6" y2="528.4" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="500.9" width="2.45" height="25.8" fill="var(--up)"/>
<line x1="927.5" y1="510.6" x2="927.5" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="514.3" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="931.5" y1="533.9" x2="931.5" y2="554.6" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="535.6" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="935.4" y1="522.5" x2="935.4" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="524.8" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="939.4" y1="510.1" x2="939.4" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="518.6" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="943.3" y1="491.2" x2="943.3" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="493.6" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="947.3" y1="463.6" x2="947.3" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="464.7" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="951.2" y1="462.0" x2="951.2" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="468.0" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="955.2" y1="484.0" x2="955.2" y2="519.3" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="502.6" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="959.1" y1="478.9" x2="959.1" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="481.4" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="963.1" y1="479.4" x2="963.1" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="486.4" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="967.0" y1="484.8" x2="967.0" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="489.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="971.0" y1="477.6" x2="971.0" y2="492.3" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="480.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="974.9" y1="465.9" x2="974.9" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="479.2" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="978.9" y1="470.5" x2="978.9" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="475.0" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="982.8" y1="472.1" x2="982.8" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="479.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="986.8" y1="482.2" x2="986.8" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="496.4" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="990.7" y1="497.1" x2="990.7" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="503.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="994.7" y1="502.2" x2="994.7" y2="517.6" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="505.4" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="998.6" y1="484.0" x2="998.6" y2="507.3" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="487.2" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="1002.6" y1="494.0" x2="1002.6" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="497.2" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="1006.5" y1="500.6" x2="1006.5" y2="514.7" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="503.4" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="1010.5" y1="508.3" x2="1010.5" y2="533.1" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="513.1" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="1014.5" y1="518.7" x2="1014.5" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="526.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1018.4" y1="528.9" x2="1018.4" y2="545.2" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="531.4" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="1022.4" y1="534.6" x2="1022.4" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="537.0" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="1026.3" y1="541.7" x2="1026.3" y2="549.6" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="547.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1030.3" y1="544.7" x2="1030.3" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="548.1" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="1034.2" y1="540.8" x2="1034.2" y2="547.6" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="542.9" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="1038.2" y1="542.0" x2="1038.2" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="543.4" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="1042.1" y1="517.0" x2="1042.1" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="529.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1046.1" y1="529.4" x2="1046.1" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="531.7" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="1050.0" y1="538.5" x2="1050.0" y2="546.4" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="544.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="60" y1="464.9" x2="1052" y2="464.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="468.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$22 R1</text>
<text x="1058" y="480.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="350.1" x2="1052" y2="350.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="353.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$29 R2</text>
<text x="1058" y="365.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="309.8" x2="1052" y2="309.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="313.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$32 R3</text>
<text x="1058" y="325.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="554.2" x2="1052" y2="554.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="548.2" font-size="11.5" fill="var(--support)" font-weight="600">$16.09 S1</text>
<text x="1058" y="560.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="545.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="537.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $16.66 (2026-09-10)</text>
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
| R3 | $32 | 5 | 2025-12-22·2026-01-07·2026-01-15·2026-05-22·2026-06-02 — 2025년 말 반등 상단과 CHIPS LOI 직후 고점이 같은 대에서 겹침 |
| R2 | $29 | 2 | 2025-09-24·2025-12-08 — 2025-10 고점($46.75) 전후의 중간 정체대 |
| R1 | $22 | 3 | 2026-02-26·2026-08-05·2026-08-13 — 2026년 들어 반등이 세 번 멈춘 대(8월 두 번은 Q2 실적 직후) |
| **현재가** | **$16.66** (2026-09-10 종가) | — | R1과 S1 사이 |
| S1 | $16.09 | 3 | 2026-07-17·2026-07-29·2026-09-02 — 최근 두 달 사이 세 번 확인된 구간. **현재가와 3.5% 차이** |

> **현재가($16.66)가 S1($16.09)과 불과 3.5% 떨어져 있다** — 이 1년 중 현재가가 지지대에 가장 가까이 붙은 상태다. S1은 터치 3회(2026-07-17·07-29·09-02)로 최근 두 달 사이 반복해서 확인된 구간이라 표본이 최신이라는 점에서는 위 저항대들보다 유효성이 높다.
>
> 이 기간의 **최근 1년 최고는 $46.75(2025-10-15)**, **최저는 $12.75(2026-03-30)**다. 둘 다 터치가 1회뿐이라 위 클러스터에는 잡히지 않았고 참고선으로만 둔다 — 현재가는 그 최고 대비 -64.4%, 최저 대비 +30.7% 지점이다.

---

## 3. 관측된 특이 구간 — 2026-05-21 CHIPS 자금 의향서(LOI) 발표

이 1년에서 단일 사건이 가격을 가장 크게 움직인 날이다.

- **2026-05-21**: 미 상무부와 CHIPS법 $100M 지원 의향서(LOI) 체결이 발표되며 종가가 전일 대비 **+33.37%**($19.30 → $25.74), 거래량은 평소(일 3,471만 주) 대비 약 **3.4배인 1억 1,913만 주**였다([최근 뉴스 / 이슈](./08_news.md)).
- 다만 **그 상승은 유지되지 않았다.** 월말 종가가 2026-05 $30.14 → 06 $23.99 → 07 $18.08 → 08 $17.20 → 09-10 $16.66으로 넉 달 연속 내려왔고, 2026-09-08 **CHIPS 최종 계약 확정**은 일간 10%를 넘는 재평가를 만들지 못했다. **의향서 단계의 기대가 확정 단계에서 재확인되지 않은 형태**로, 정책 모멘텀이 이미 가격에 소화됐음을 시사한다(원인을 단정할 근거는 없다).
- 그 밖에 일간 20% 이상 움직인 날이 이 1년에만 5회(2025-10-13 +23.02%, 2026-02-06 +20.40%, 2026-04-15 +22.63%, 2026-05-21 +33.37%, 2026-07-27 +20.36%)다. **매출이 분기 $3M인 회사에서 이 정도 진폭이 반복된다는 것은 가격이 실적이 아니라 뉴스·섹터 심리로 결정되고 있다는 뜻**으로 읽는 편이 정확하다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-11~2026-09-10. 수집 시점: 2026-09-11. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py QBTS --name "D-Wave Quantum" --close-on 2026-09-10 --emit all` (기본 파라미터, `--levels` 미지정 — 유효 클러스터가 4개라 4개 모두 표기)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간에서 보듯 이 1년 동안 일간 20% 이상 변동이 5회 있었다. **이런 구간에서는 ±2.5% 클러스터링 허용오차가 상대적으로 좁아** 실제로는 같은 매물대인 스윙이 서로 다른 레벨로 쪼개졌을 수 있다(R3 $32와 R2 $29가 그 예일 가능성).
    - 이 기간에 주식분할·병합은 없었다. 다만 **2026-09-08 CHIPS 최종 계약으로 미 상무부에 발행될 주식(약 600만 주 추정)은 아직 이 차트 기간에 반영되지 않았다** — 가격 차트는 주식수 변화를 보여주지 않는다([핵심 지표](./04_metrics.md) A.4).

---

*작성일: 2026-09-11*
