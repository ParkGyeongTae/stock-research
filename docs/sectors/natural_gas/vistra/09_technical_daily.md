# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-18 종가 $140.67은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.**

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-19 ~ 2026-09-18)

<style>
.vst-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .vst-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.vst-chart svg { width:100%; height:auto; display:block; }
.vst-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.vst-chart .title { fill: var(--ink); font-weight:600; }
.vst-chart .grid { stroke: var(--grid); stroke-width:1; }
.vst-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="vst-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vistra(VST) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Vistra (VST) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-19 ~ 2026-09-18 · 마지막 종가 $140.67 (2026-09-18) · 단위 USD</text>
<line x1="60" y1="565.4" x2="1052" y2="565.4" class="grid"/>
<text x="52" y="569.4" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="444.1" x2="1052" y2="444.1" class="grid"/>
<text x="52" y="448.1" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="322.8" x2="1052" y2="322.8" class="grid"/>
<text x="52" y="326.8" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="60" y1="201.5" x2="1052" y2="201.5" class="grid"/>
<text x="52" y="205.5" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="80.3" x2="1052" y2="80.3" class="grid"/>
<text x="52" y="84.3" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="93.6" y1="626.0" x2="93.6" y2="631.0" class="axis"/>
<text x="93.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="184.5" y1="626.0" x2="184.5" y2="631.0" class="axis"/>
<text x="184.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="259.6" y1="626.0" x2="259.6" y2="631.0" class="axis"/>
<text x="259.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="346.5" y1="626.0" x2="346.5" y2="631.0" class="axis"/>
<text x="346.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="425.6" y1="626.0" x2="425.6" y2="631.0" class="axis"/>
<text x="425.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="500.7" y1="626.0" x2="500.7" y2="631.0" class="axis"/>
<text x="500.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="587.6" y1="626.0" x2="587.6" y2="631.0" class="axis"/>
<text x="587.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="670.6" y1="626.0" x2="670.6" y2="631.0" class="axis"/>
<text x="670.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="749.7" y1="626.0" x2="749.7" y2="631.0" class="axis"/>
<text x="749.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="832.7" y1="626.0" x2="832.7" y2="631.0" class="axis"/>
<text x="832.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="919.6" y1="626.0" x2="919.6" y2="631.0" class="axis"/>
<text x="919.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1002.6" y1="626.0" x2="1002.6" y2="631.0" class="axis"/>
<text x="1002.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="117.6" x2="62.0" y2="170.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="132.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="65.9" y1="81.3" x2="65.9" y2="154.2" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="92.9" width="2.45" height="42.0" fill="var(--up)"/>
<line x1="69.9" y1="124.1" x2="69.9" y2="180.6" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="140.2" width="2.45" height="35.6" fill="var(--down)"/>
<line x1="73.8" y1="164.0" x2="73.8" y2="190.2" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="181.8" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="77.8" y1="175.7" x2="77.8" y2="225.7" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="191.7" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="81.7" y1="156.1" x2="81.7" y2="195.6" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="157.8" width="2.45" height="36.5" fill="var(--up)"/>
<line x1="85.7" y1="158.3" x2="85.7" y2="215.5" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="189.4" width="2.45" height="24.6" fill="var(--down)"/>
<line x1="89.6" y1="198.5" x2="89.6" y2="257.9" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="206.4" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="93.6" y1="171.6" x2="93.6" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="192.4" width="2.45" height="39.5" fill="var(--up)"/>
<line x1="97.5" y1="171.2" x2="97.5" y2="209.4" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="177.0" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="101.5" y1="139.7" x2="101.5" y2="192.4" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="175.2" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="105.5" y1="153.4" x2="105.5" y2="217.1" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="164.2" width="2.45" height="34.9" fill="var(--down)"/>
<line x1="109.4" y1="178.3" x2="109.4" y2="226.5" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="192.0" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="113.4" y1="161.4" x2="113.4" y2="200.8" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="161.8" width="2.45" height="30.1" fill="var(--up)"/>
<line x1="117.3" y1="134.4" x2="117.3" y2="169.2" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="140.9" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="121.3" y1="126.5" x2="121.3" y2="220.7" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="142.3" width="2.45" height="78.2" fill="var(--down)"/>
<line x1="125.2" y1="141.2" x2="125.2" y2="199.1" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="143.6" width="2.45" height="51.1" fill="var(--up)"/>
<line x1="129.2" y1="147.9" x2="129.2" y2="193.0" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="166.4" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="133.1" y1="104.3" x2="133.1" y2="162.7" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="135.7" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="137.1" y1="97.8" x2="137.1" y2="148.9" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="111.8" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="141.0" y1="140.6" x2="141.0" y2="201.2" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="155.0" width="2.45" height="38.3" fill="var(--down)"/>
<line x1="145.0" y1="168.2" x2="145.0" y2="245.1" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="176.5" width="2.45" height="60.0" fill="var(--down)"/>
<line x1="148.9" y1="241.4" x2="148.9" y2="289.0" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="244.7" width="2.45" height="38.6" fill="var(--down)"/>
<line x1="152.9" y1="265.2" x2="152.9" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="277.0" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="156.8" y1="248.8" x2="156.8" y2="288.2" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="253.9" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="160.8" y1="189.4" x2="160.8" y2="234.3" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="192.6" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="164.7" y1="179.3" x2="164.7" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="179.3" width="2.45" height="26.4" fill="var(--down)"/>
<line x1="168.7" y1="217.8" x2="168.7" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="217.8" width="2.45" height="40.8" fill="var(--down)"/>
<line x1="172.6" y1="197.1" x2="172.6" y2="265.4" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="205.4" width="2.45" height="42.9" fill="var(--up)"/>
<line x1="176.6" y1="208.7" x2="176.6" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="233.8" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="180.5" y1="244.6" x2="180.5" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="250.0" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="184.5" y1="230.7" x2="184.5" y2="275.2" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="243.7" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="188.4" y1="253.1" x2="188.4" y2="295.5" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="273.7" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="192.4" y1="247.2" x2="192.4" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="265.9" width="2.45" height="19.0" fill="var(--up)"/>
<line x1="196.4" y1="267.5" x2="196.4" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="294.8" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="200.3" y1="255.7" x2="200.3" y2="343.4" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="256.1" width="2.45" height="75.8" fill="var(--up)"/>
<line x1="204.3" y1="220.9" x2="204.3" y2="297.6" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="233.1" width="2.45" height="39.5" fill="var(--down)"/>
<line x1="208.2" y1="274.7" x2="208.2" y2="330.0" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="286.9" width="2.45" height="41.0" fill="var(--down)"/>
<line x1="212.2" y1="314.9" x2="212.2" y2="339.2" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="320.8" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="216.1" y1="335.2" x2="216.1" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="341.5" width="2.45" height="32.4" fill="var(--down)"/>
<line x1="220.1" y1="322.8" x2="220.1" y2="410.2" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="355.0" width="2.45" height="45.5" fill="var(--up)"/>
<line x1="224.0" y1="325.7" x2="224.0" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="350.5" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="228.0" y1="338.5" x2="228.0" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="356.6" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="231.9" y1="313.7" x2="231.9" y2="357.9" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="328.0" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="235.9" y1="266.5" x2="235.9" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="293.6" width="2.45" height="66.9" fill="var(--down)"/>
<line x1="239.8" y1="361.1" x2="239.8" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="371.3" width="2.45" height="20.7" fill="var(--down)"/>
<line x1="243.8" y1="351.9" x2="243.8" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="352.3" width="2.45" height="33.8" fill="var(--up)"/>
<line x1="247.7" y1="354.8" x2="247.7" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="358.7" width="2.45" height="19.6" fill="var(--down)"/>
<line x1="251.7" y1="336.5" x2="251.7" y2="364.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="342.2" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="255.6" y1="318.1" x2="255.6" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="328.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="259.6" y1="344.2" x2="259.6" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="347.0" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="263.5" y1="347.4" x2="263.5" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="350.7" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="267.5" y1="360.1" x2="267.5" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="367.3" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="271.4" y1="334.6" x2="271.4" y2="380.6" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="346.6" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="275.4" y1="343.2" x2="275.4" y2="404.9" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="343.9" width="2.45" height="56.7" fill="var(--down)"/>
<line x1="279.3" y1="396.7" x2="279.3" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="396.7" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="283.3" y1="384.0" x2="283.3" y2="415.4" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="411.5" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="287.3" y1="407.6" x2="287.3" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="411.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="291.2" y1="353.8" x2="291.2" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="355.6" width="2.45" height="76.1" fill="var(--up)"/>
<line x1="295.2" y1="322.8" x2="295.2" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="351.9" width="2.45" height="30.9" fill="var(--down)"/>
<line x1="299.1" y1="365.3" x2="299.1" y2="401.8" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="365.5" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="303.1" y1="359.6" x2="303.1" y2="404.4" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="362.5" width="2.45" height="41.2" fill="var(--up)"/>
<line x1="307.0" y1="352.3" x2="307.0" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="359.1" width="2.45" height="85.1" fill="var(--down)"/>
<line x1="311.0" y1="371.8" x2="311.0" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="406.7" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="314.9" y1="374.9" x2="314.9" y2="427.7" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="403.5" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="318.9" y1="418.0" x2="318.9" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="419.8" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="322.8" y1="421.6" x2="322.8" y2="443.3" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="434.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="326.8" y1="428.4" x2="326.8" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="432.2" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="330.7" y1="425.9" x2="330.7" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="434.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="334.7" y1="418.6" x2="334.7" y2="444.5" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="432.9" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="338.6" y1="425.5" x2="338.6" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="428.2" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="342.6" y1="416.8" x2="342.6" y2="436.7" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="426.6" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="346.5" y1="387.8" x2="346.5" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="412.4" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="350.5" y1="373.4" x2="350.5" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="387.3" width="2.45" height="39.1" fill="var(--down)"/>
<line x1="354.4" y1="367.6" x2="354.4" y2="421.2" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="386.3" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="358.4" y1="391.6" x2="358.4" y2="483.3" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="391.6" width="2.45" height="85.2" fill="var(--down)"/>
<line x1="362.3" y1="469.6" x2="362.3" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="472.9" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="366.3" y1="354.7" x2="366.3" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="357.2" width="2.45" height="48.3" fill="var(--down)"/>
<line x1="370.2" y1="342.6" x2="370.2" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="367.8" width="2.45" height="48.0" fill="var(--up)"/>
<line x1="374.2" y1="350.4" x2="374.2" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="359.2" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="378.2" y1="376.3" x2="378.2" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="387.1" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="382.1" y1="307.3" x2="382.1" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="321.7" width="2.45" height="43.5" fill="var(--up)"/>
<line x1="386.1" y1="376.7" x2="386.1" y2="425.8" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="398.3" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="390.0" y1="407.7" x2="390.0" y2="466.8" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="436.4" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="394.0" y1="432.1" x2="394.0" y2="481.9" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="444.0" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="397.9" y1="422.9" x2="397.9" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="432.4" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="401.9" y1="426.7" x2="401.9" y2="456.2" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="443.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="405.8" y1="411.9" x2="405.8" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="440.5" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="409.8" y1="416.1" x2="409.8" y2="455.3" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="418.3" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="413.7" y1="404.3" x2="413.7" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="407.7" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="417.7" y1="396.3" x2="417.7" y2="451.6" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="407.9" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="421.6" y1="416.8" x2="421.6" y2="463.1" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="435.0" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="425.6" y1="444.2" x2="425.6" y2="480.3" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="458.3" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="429.5" y1="465.3" x2="429.5" y2="502.3" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="467.6" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="433.5" y1="482.5" x2="433.5" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="485.4" width="2.45" height="64.7" fill="var(--down)"/>
<line x1="437.4" y1="541.7" x2="437.4" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="546.7" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="441.4" y1="491.0" x2="441.4" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="504.7" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="445.3" y1="469.7" x2="445.3" y2="518.2" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="486.7" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="449.3" y1="435.5" x2="449.3" y2="475.6" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="441.7" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="453.2" y1="411.9" x2="453.2" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="413.8" width="2.45" height="29.4" fill="var(--down)"/>
<line x1="457.2" y1="406.4" x2="457.2" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="425.3" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="461.1" y1="373.4" x2="461.1" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="374.4" width="2.45" height="55.1" fill="var(--up)"/>
<line x1="465.1" y1="343.1" x2="465.1" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="361.1" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="469.1" y1="350.1" x2="469.1" y2="385.8" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="359.1" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="473.0" y1="367.9" x2="473.0" y2="394.1" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="368.3" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="477.0" y1="362.2" x2="477.0" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="369.5" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="480.9" y1="372.3" x2="480.9" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="379.6" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="484.9" y1="373.3" x2="484.9" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="373.6" width="2.45" height="26.3" fill="var(--up)"/>
<line x1="488.8" y1="347.4" x2="488.8" y2="383.0" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="350.9" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="492.8" y1="339.6" x2="492.8" y2="419.2" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="342.1" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="496.7" y1="333.1" x2="496.7" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="353.1" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="500.7" y1="343.9" x2="500.7" y2="408.7" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="382.2" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="504.6" y1="422.7" x2="504.6" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="433.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="508.6" y1="418.6" x2="508.6" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="423.7" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="512.5" y1="395.8" x2="512.5" y2="433.9" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="399.2" width="2.45" height="33.5" fill="var(--up)"/>
<line x1="516.5" y1="393.3" x2="516.5" y2="454.4" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="417.1" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="520.4" y1="416.0" x2="520.4" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="422.1" width="2.45" height="46.8" fill="var(--up)"/>
<line x1="524.4" y1="390.8" x2="524.4" y2="418.0" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="411.6" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="528.3" y1="419.9" x2="528.3" y2="473.5" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="422.3" width="2.45" height="26.9" fill="var(--down)"/>
<line x1="532.3" y1="424.7" x2="532.3" y2="464.1" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="446.6" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="536.2" y1="412.3" x2="536.2" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="433.4" width="2.45" height="17.0" fill="var(--down)"/>
<line x1="540.2" y1="422.9" x2="540.2" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="432.0" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="544.1" y1="411.0" x2="544.1" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="417.8" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="548.1" y1="365.3" x2="548.1" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="382.7" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="552.0" y1="385.9" x2="552.0" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="399.4" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="556.0" y1="404.9" x2="556.0" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="404.9" width="2.45" height="124.0" fill="var(--down)"/>
<line x1="560.0" y1="468.9" x2="560.0" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="495.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="563.9" y1="479.9" x2="563.9" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="488.2" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="567.9" y1="456.5" x2="567.9" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="474.4" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="571.8" y1="488.5" x2="571.8" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="490.8" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="575.8" y1="442.9" x2="575.8" y2="494.1" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="471.5" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="579.7" y1="450.6" x2="579.7" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="461.7" width="2.45" height="58.0" fill="var(--down)"/>
<line x1="583.7" y1="495.8" x2="583.7" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="502.7" width="2.45" height="39.0" fill="var(--up)"/>
<line x1="587.6" y1="466.3" x2="587.6" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="480.7" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="591.6" y1="477.1" x2="591.6" y2="504.0" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="497.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="595.5" y1="485.9" x2="595.5" y2="505.5" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="495.1" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="599.5" y1="479.5" x2="599.5" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="482.4" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="603.4" y1="436.1" x2="603.4" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="439.5" width="2.45" height="29.5" fill="var(--down)"/>
<line x1="607.4" y1="428.7" x2="607.4" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="469.0" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="611.3" y1="452.4" x2="611.3" y2="485.9" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="476.0" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="615.3" y1="439.7" x2="615.3" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="455.0" width="2.45" height="33.7" fill="var(--up)"/>
<line x1="619.2" y1="412.1" x2="619.2" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="420.0" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="623.2" y1="404.5" x2="623.2" y2="431.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="410.7" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="627.1" y1="402.1" x2="627.1" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="410.6" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="631.1" y1="392.6" x2="631.1" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="406.1" width="2.45" height="17.0" fill="var(--down)"/>
<line x1="635.0" y1="419.5" x2="635.0" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="425.6" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="639.0" y1="437.4" x2="639.0" y2="479.7" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="439.5" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="642.9" y1="449.7" x2="642.9" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="457.4" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="646.9" y1="450.9" x2="646.9" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="463.2" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="650.9" y1="410.9" x2="650.9" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="417.7" width="2.45" height="48.6" fill="var(--up)"/>
<line x1="654.8" y1="393.0" x2="654.8" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="404.2" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="658.8" y1="423.9" x2="658.8" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="428.9" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="662.7" y1="437.2" x2="662.7" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="438.9" width="2.45" height="42.9" fill="var(--down)"/>
<line x1="666.7" y1="446.3" x2="666.7" y2="470.0" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="457.2" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="670.6" y1="443.2" x2="670.6" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="454.3" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="674.6" y1="429.7" x2="674.6" y2="459.6" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="438.9" width="2.45" height="19.2" fill="var(--up)"/>
<line x1="678.5" y1="421.0" x2="678.5" y2="445.3" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="425.9" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="682.5" y1="426.0" x2="682.5" y2="464.7" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="435.0" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="686.4" y1="393.2" x2="686.4" y2="481.9" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="425.7" width="2.45" height="55.1" fill="var(--down)"/>
<line x1="690.4" y1="474.4" x2="690.4" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="474.4" width="2.45" height="44.1" fill="var(--down)"/>
<line x1="694.3" y1="488.0" x2="694.3" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="492.3" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="698.3" y1="502.8" x2="698.3" y2="531.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="507.8" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="702.2" y1="527.3" x2="702.2" y2="568.3" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="527.3" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="706.2" y1="545.4" x2="706.2" y2="565.8" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="553.8" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="710.1" y1="558.8" x2="710.1" y2="578.6" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="566.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="714.1" y1="568.2" x2="714.1" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="571.4" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="718.0" y1="585.4" x2="718.0" y2="609.9" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="590.8" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="722.0" y1="535.6" x2="722.0" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="541.1" width="2.45" height="36.4" fill="var(--up)"/>
<line x1="725.9" y1="509.1" x2="725.9" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="510.3" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="729.9" y1="458.8" x2="729.9" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="466.7" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="733.8" y1="399.2" x2="733.8" y2="454.9" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="416.4" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="737.8" y1="413.6" x2="737.8" y2="453.7" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="414.0" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="741.8" y1="422.7" x2="741.8" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="442.4" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="745.7" y1="430.2" x2="745.7" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="442.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="749.7" y1="452.9" x2="749.7" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="462.3" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="753.6" y1="439.4" x2="753.6" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="456.4" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="757.6" y1="456.8" x2="757.6" y2="486.8" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="465.2" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="761.5" y1="480.2" x2="761.5" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="482.3" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="765.5" y1="478.7" x2="765.5" y2="519.9" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="492.6" width="2.45" height="19.6" fill="var(--down)"/>
<line x1="769.4" y1="509.0" x2="769.4" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="515.0" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="773.4" y1="502.9" x2="773.4" y2="556.0" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="514.3" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="777.3" y1="541.1" x2="777.3" y2="578.0" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="545.0" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="781.3" y1="523.5" x2="781.3" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="526.7" width="2.45" height="32.7" fill="var(--up)"/>
<line x1="785.2" y1="501.7" x2="785.2" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="516.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="789.2" y1="471.7" x2="789.2" y2="503.2" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="483.4" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="793.1" y1="435.1" x2="793.1" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="452.5" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="797.1" y1="429.3" x2="797.1" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="451.2" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="801.0" y1="381.4" x2="801.0" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="421.3" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="805.0" y1="380.4" x2="805.0" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="400.1" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="808.9" y1="408.8" x2="808.9" y2="449.3" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="429.6" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="812.9" y1="409.9" x2="812.9" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="425.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="816.8" y1="375.3" x2="816.8" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="397.0" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="820.8" y1="396.0" x2="820.8" y2="424.7" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="408.6" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="824.7" y1="410.1" x2="824.7" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="421.6" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="828.7" y1="411.0" x2="828.7" y2="465.2" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="428.4" width="2.45" height="24.0" fill="var(--down)"/>
<line x1="832.7" y1="460.3" x2="832.7" y2="498.4" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="468.3" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="836.6" y1="466.9" x2="836.6" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="480.8" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="840.6" y1="460.8" x2="840.6" y2="492.5" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="460.9" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="844.5" y1="447.7" x2="844.5" y2="480.4" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="467.6" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="848.5" y1="465.4" x2="848.5" y2="496.7" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="475.5" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="852.4" y1="436.9" x2="852.4" y2="459.6" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="450.1" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="856.4" y1="444.0" x2="856.4" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="451.0" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="860.3" y1="447.5" x2="860.3" y2="467.1" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="455.5" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="864.3" y1="394.3" x2="864.3" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="438.0" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="868.2" y1="402.0" x2="868.2" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="428.9" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="872.2" y1="455.6" x2="872.2" y2="513.7" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="457.0" width="2.45" height="32.2" fill="var(--down)"/>
<line x1="876.1" y1="460.8" x2="876.1" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="471.7" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="880.1" y1="452.8" x2="880.1" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="456.3" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="884.0" y1="417.0" x2="884.0" y2="444.0" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="430.0" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="888.0" y1="396.7" x2="888.0" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="403.2" width="2.45" height="40.2" fill="var(--up)"/>
<line x1="891.9" y1="389.1" x2="891.9" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="389.6" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="895.9" y1="384.9" x2="895.9" y2="430.1" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="391.4" width="2.45" height="32.2" fill="var(--down)"/>
<line x1="899.8" y1="406.8" x2="899.8" y2="471.1" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="410.7" width="2.45" height="51.1" fill="var(--down)"/>
<line x1="903.8" y1="480.5" x2="903.8" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="481.0" width="2.45" height="32.0" fill="var(--down)"/>
<line x1="907.7" y1="509.1" x2="907.7" y2="552.3" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="512.5" width="2.45" height="35.9" fill="var(--down)"/>
<line x1="911.7" y1="492.8" x2="911.7" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="513.1" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="915.6" y1="485.7" x2="915.6" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="493.5" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="919.6" y1="462.5" x2="919.6" y2="527.8" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="468.7" width="2.45" height="43.5" fill="var(--up)"/>
<line x1="923.6" y1="462.3" x2="923.6" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="470.8" width="2.45" height="75.0" fill="var(--down)"/>
<line x1="927.5" y1="532.0" x2="927.5" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="541.7" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="931.5" y1="547.0" x2="931.5" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="553.2" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="935.4" y1="549.0" x2="935.4" y2="597.2" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="561.8" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="939.4" y1="535.9" x2="939.4" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="548.0" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="943.3" y1="523.5" x2="943.3" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="535.5" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="947.3" y1="508.5" x2="947.3" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="510.8" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="951.2" y1="518.2" x2="951.2" y2="536.2" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="526.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="955.2" y1="503.6" x2="955.2" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="516.1" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="959.1" y1="505.5" x2="959.1" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="508.5" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="963.1" y1="531.8" x2="963.1" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="538.1" width="2.45" height="24.1" fill="var(--down)"/>
<line x1="967.0" y1="548.6" x2="967.0" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="549.0" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="971.0" y1="544.1" x2="971.0" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="549.0" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="974.9" y1="563.4" x2="974.9" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="565.4" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="978.9" y1="582.3" x2="978.9" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="590.3" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="982.8" y1="563.8" x2="982.8" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="571.2" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="986.8" y1="540.9" x2="986.8" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="565.2" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="990.7" y1="550.2" x2="990.7" y2="574.8" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="553.2" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="994.7" y1="558.7" x2="994.7" y2="585.9" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="560.0" width="2.45" height="23.0" fill="var(--down)"/>
<line x1="998.6" y1="577.9" x2="998.6" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="581.3" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="1002.6" y1="569.7" x2="1002.6" y2="596.3" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="577.0" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="1006.5" y1="540.2" x2="1006.5" y2="583.9" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="544.4" width="2.45" height="34.2" fill="var(--up)"/>
<line x1="1010.5" y1="512.1" x2="1010.5" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="535.0" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="1014.5" y1="508.1" x2="1014.5" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="509.0" width="2.45" height="32.9" fill="var(--up)"/>
<line x1="1018.4" y1="475.0" x2="1018.4" y2="502.5" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="494.3" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="1022.4" y1="495.3" x2="1022.4" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="498.1" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="1026.3" y1="487.7" x2="1026.3" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="504.7" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="1030.3" y1="510.3" x2="1030.3" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="511.9" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="1034.2" y1="533.6" x2="1034.2" y2="563.1" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="541.1" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="1038.2" y1="545.8" x2="1038.2" y2="563.8" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="554.2" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="1042.1" y1="542.9" x2="1042.1" y2="567.7" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="544.9" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="1046.1" y1="528.3" x2="1046.1" y2="556.1" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="540.5" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="1050.0" y1="538.4" x2="1050.0" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="544.8" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="60" y1="468.7" x2="1052" y2="468.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="472.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$156 R1</text>
<text x="1058" y="484.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="388.5" x2="1052" y2="388.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="392.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$169 R2</text>
<text x="1058" y="404.0" font-size="9.5" fill="var(--muted)">터치 10회</text>
<line x1="60" y1="326.6" x2="1052" y2="326.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="330.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$179 R3</text>
<text x="1058" y="342.1" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="576.2" x2="1052" y2="576.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="570.2" font-size="11.5" fill="var(--support)" font-weight="600">$138 S1</text>
<text x="1058" y="582.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="600.5" x2="1052" y2="600.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="594.5" font-size="11.5" fill="var(--support)" font-weight="600">$134 S2</text>
<text x="1058" y="606.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="561.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="553.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $141 (2026-09-18)</text>
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
| R3 | $179 | 4 | 2025-12-12·2026-01-15·2026-02-17·2026-02-27 스윙 고점대(4회). **Meta PPA 발표(2026-01-09)와 Cogentrix 인수 발표(2026-01-05) 전후**의 고점 구간이다 |
| R2 | $169 | 10 | 2026-01-29~2026-07-24에 걸친 스윙 고점대(**10회, 이 표에서 가장 촘촘하다**). 상반기 내내 반복해서 부딪힌 가격대로, 그만큼 매물이 두껍다 |
| R1 | $156 | 2 | 2026-08-04·2026-09-08 스윙 고점대(2회). **2분기 실적발표(2026-08-07) 전후**에 형성된 가장 최근 저항 |
| **현재가** | **$140.67** (2026-09-18 종가) | — | R1($156)과 S1($138) 사이. **아래쪽 지지 S1까지 2% 거리**로 바짝 붙어 있다 |
| S1 | $138 | 2 | 2026-02-05·2026-06-10 스윙 저점대(2회). 현재가에 가장 근접한 지지 — 터치가 2회뿐이라 강도는 약하다 |
| S2 | $134 | 4 | 2026-05-19·2026-08-07·2026-08-24·2026-09-01 스윙 저점대(4회). **8~9월에 세 번 몰려 있어 최근 형성된 지지**이며, 52주 최저 $132.66도 이 근처다 |

> **[NRG](../nrg/09_technical_daily.md)와의 차이가 이 표의 의미다.** 같은 1년 동안 NRG는 현재가 아래에 지지 클러스터가 하나도 없는 신저가 구간인 반면, **Vistra는 위아래로 레벨이 모두 잡힌다**(저항 3개·지지 2개). 52주 최저($132.66)와도 6.0% 떨어져 있다 — **두 회사가 같은 거시 압력을 받았지만 하락의 깊이가 다르다는 것**을 레벨 분포가 보여준다.
>
> 참고선으로 둘 만한 것은 **52주 최고 $219.82**(현재가 대비 +56%)인데, R3($179)보다 훨씬 위에 있어 클러스터를 이루지 않았다 — 근시일 저항으로 보기 어렵고 구간 상단의 기록으로만 읽는다.

---

## 3. 관측된 특이 구간 — 2026년 2월 이후의 단계적 하락

**단일 이벤트로 인한 갭이 아니라 7개월에 걸친 단계적 하락**이라, 이 절은 특정 날짜가 아니라 구간을 다룬다.

- 고점대(R3 $179)가 **2026년 2월까지** 형성됐고, 그 직전에 **Meta PPA(2026-01-09)와 Cogentrix 인수(2026-01-05)**라는 이 회사 최대의 호재 둘이 발표됐다([최근 뉴스 / 이슈](./08_news.md)). **호재 발표 직후가 고점이었다**는 점이 이 구간의 특징이다.
- 이후 R2($169) 부근에서 **10회에 걸쳐 반복적으로 부딪히며** 상반기 내내 횡보했고, **2026-08-07 2분기 실적발표를 기점으로 그 아래로 내려왔다.** 실적 자체는 Adjusted EBITDA +31%로 좋았으나 같은 날 회사가 **2027년 기회범위의 하단으로 가고 있다**고 밝힌 것이 겹친다.
- **8~9월에 지지 클러스터(S2 $134)가 새로 만들어진 것**이 최근 구간의 특징이다 — 2026-08-07·08-24·09-01 세 번이 여기 몰려 있다. **매물대가 아래쪽에도 쌓이기 시작했다는 뜻**이며, 위쪽만 촘촘한 [NRG](../nrg/09_technical_daily.md)와 대비된다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-19~2026-09-18. 수집 시점: 2026-09-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py VST --name "Vistra" --close-on 2026-09-18 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨 5개(R3·R2·R1·S1·S2)가 나왔고 `--force-level`로 추가하거나 제거하지 않았다.** S1은 터치 2회로 강도가 약하다는 점을 §2 비고에 남겼다.
    - **기간 내 배당 4회가 반영되지 않은 원주가다.** 연 $0.92 수준이라 1년 총수익률과 차트상 하락률이 약 0.65%p 어긋난다.
    - **진행 중인 Cogentrix 인수(신주 500만 주 발행 예정)는 아직 주가에 반영된 이벤트가 아니다** — 종결되면 희석주식수가 약 1.5% 늘지만 주가 연속성을 깨는 이벤트(분할·액면변경)는 아니다.

---

*작성일: 2026-09-19*
