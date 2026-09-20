# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-18 종가 $129.75는 [핵심 지표 A.2](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.** 같은 날 stockanalysis.com이 표시한 종가($129.75)와도 같다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-19 ~ 2026-09-18)

<style>
.pep-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .pep-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.pep-chart svg { width:100%; height:auto; display:block; }
.pep-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.pep-chart .title { fill: var(--ink); font-weight:600; }
.pep-chart .grid { stroke: var(--grid); stroke-width:1; }
.pep-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="pep-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="펩시코(PEP) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">펩시코 (PEP) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-19 ~ 2026-09-18 · 마지막 종가 $129.75 (2026-09-18) · 단위 USD</text>
<line x1="60" y1="600.7" x2="1052" y2="600.7" class="grid"/>
<text x="52" y="604.7" font-size="11" text-anchor="end" fill="var(--muted)">130</text>
<line x1="60" y1="474.0" x2="1052" y2="474.0" class="grid"/>
<text x="52" y="478.0" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="347.3" x2="1052" y2="347.3" class="grid"/>
<text x="52" y="351.3" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="220.7" x2="1052" y2="220.7" class="grid"/>
<text x="52" y="224.7" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="94.0" x2="1052" y2="94.0" class="grid"/>
<text x="52" y="98.0" font-size="11" text-anchor="end" fill="var(--muted)">170</text>
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
<line x1="62.0" y1="447.7" x2="62.0" y2="468.2" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="451.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="65.9" y1="454.7" x2="65.9" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="460.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="69.9" y1="445.8" x2="69.9" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="449.9" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="73.8" y1="444.4" x2="73.8" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="446.5" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="77.8" y1="430.7" x2="77.8" y2="475.8" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="436.0" width="2.45" height="39.0" fill="var(--down)"/>
<line x1="81.7" y1="461.5" x2="81.7" y2="475.9" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="468.4" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="85.7" y1="465.5" x2="85.7" y2="485.1" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="468.4" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="89.6" y1="461.0" x2="89.6" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="468.4" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="93.6" y1="431.3" x2="93.6" y2="467.9" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="434.2" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="97.5" y1="432.8" x2="97.5" y2="456.6" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="444.7" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="101.5" y1="431.4" x2="101.5" y2="450.4" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="445.4" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="105.5" y1="450.6" x2="105.5" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="451.6" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="109.4" y1="450.7" x2="109.4" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="464.0" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="113.4" y1="461.6" x2="113.4" y2="490.6" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="464.0" width="2.45" height="24.7" fill="var(--down)"/>
<line x1="117.3" y1="414.0" x2="117.3" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="414.3" width="2.45" height="53.8" fill="var(--up)"/>
<line x1="121.3" y1="336.9" x2="121.3" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="346.3" width="2.45" height="56.4" fill="var(--up)"/>
<line x1="125.2" y1="347.6" x2="125.2" y2="381.0" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="361.4" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="129.2" y1="326.8" x2="129.2" y2="366.3" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="327.8" width="2.45" height="36.1" fill="var(--up)"/>
<line x1="133.1" y1="317.1" x2="133.1" y2="357.8" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="330.5" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="137.1" y1="291.9" x2="137.1" y2="318.3" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="313.5" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="141.0" y1="297.8" x2="141.0" y2="325.3" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="299.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="145.0" y1="291.3" x2="145.0" y2="312.9" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="291.3" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="148.9" y1="281.6" x2="148.9" y2="311.4" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="287.8" width="2.45" height="19.3" fill="var(--down)"/>
<line x1="152.9" y1="281.7" x2="152.9" y2="313.0" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="307.4" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="156.8" y1="304.3" x2="156.8" y2="334.3" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="307.2" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="160.8" y1="316.7" x2="160.8" y2="331.2" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="321.5" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="164.7" y1="311.0" x2="164.7" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="314.0" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="168.7" y1="306.7" x2="168.7" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="329.5" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="172.6" y1="364.3" x2="172.6" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="372.0" width="2.45" height="23.9" fill="var(--down)"/>
<line x1="176.6" y1="371.5" x2="176.6" y2="394.8" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="378.4" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="180.5" y1="385.3" x2="180.5" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="395.5" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="184.5" y1="399.1" x2="184.5" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="399.8" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="188.4" y1="411.6" x2="188.4" y2="447.9" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="414.5" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="192.4" y1="432.5" x2="192.4" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="437.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="196.4" y1="433.3" x2="196.4" y2="457.5" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="443.5" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="200.3" y1="422.7" x2="200.3" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="436.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="204.3" y1="435.7" x2="204.3" y2="458.0" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="440.8" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="208.2" y1="401.0" x2="208.2" y2="440.1" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="409.7" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="212.2" y1="404.3" x2="212.2" y2="422.6" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="416.2" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="216.1" y1="393.1" x2="216.1" y2="427.8" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="410.4" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="220.1" y1="387.4" x2="220.1" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="399.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="224.0" y1="371.3" x2="224.0" y2="407.9" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="374.8" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="228.0" y1="349.5" x2="228.0" y2="379.6" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="362.9" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="231.9" y1="362.5" x2="231.9" y2="389.3" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="368.9" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="235.9" y1="384.3" x2="235.9" y2="411.9" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="390.4" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="239.8" y1="360.8" x2="239.8" y2="398.3" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="393.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="243.8" y1="393.7" x2="243.8" y2="413.7" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="400.2" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="247.7" y1="383.8" x2="247.7" y2="403.4" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="396.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="251.7" y1="366.7" x2="251.7" y2="395.1" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="372.9" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="255.6" y1="362.3" x2="255.6" y2="382.4" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="363.3" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="259.6" y1="349.6" x2="259.6" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="353.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="263.5" y1="353.5" x2="263.5" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="354.2" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="267.5" y1="338.5" x2="267.5" y2="373.8" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="363.9" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="271.4" y1="369.5" x2="271.4" y2="396.4" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="375.8" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="275.4" y1="400.5" x2="275.4" y2="416.9" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="402.8" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="279.3" y1="390.9" x2="279.3" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="402.7" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="283.3" y1="378.2" x2="283.3" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="393.6" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="287.3" y1="350.1" x2="287.3" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="351.1" width="2.45" height="24.4" fill="var(--up)"/>
<line x1="291.2" y1="336.1" x2="291.2" y2="371.0" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="345.4" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="295.2" y1="338.8" x2="295.2" y2="363.3" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="339.1" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="299.1" y1="325.8" x2="299.1" y2="343.8" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="331.9" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="303.1" y1="317.6" x2="303.1" y2="347.5" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="322.1" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="307.0" y1="331.6" x2="307.0" y2="353.9" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="342.5" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="311.0" y1="342.6" x2="311.0" y2="356.8" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="349.9" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="314.9" y1="348.7" x2="314.9" y2="373.9" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="358.1" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="318.9" y1="360.3" x2="318.9" y2="392.8" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="378.6" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="322.8" y1="382.9" x2="322.8" y2="428.9" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="382.9" width="2.45" height="44.5" fill="var(--down)"/>
<line x1="326.8" y1="423.5" x2="326.8" y2="436.6" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="426.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="330.7" y1="424.1" x2="330.7" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="426.1" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="334.7" y1="410.0" x2="334.7" y2="428.4" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="420.3" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="338.6" y1="407.2" x2="338.6" y2="424.3" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="421.3" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="342.6" y1="423.0" x2="342.6" y2="434.0" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="425.5" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="346.5" y1="430.8" x2="346.5" y2="447.4" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="433.2" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="350.5" y1="451.1" x2="350.5" y2="481.6" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="453.0" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="354.4" y1="473.2" x2="354.4" y2="492.1" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="478.1" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="358.4" y1="476.2" x2="358.4" y2="512.5" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="483.9" width="2.45" height="28.0" fill="var(--down)"/>
<line x1="362.3" y1="480.6" x2="362.3" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="482.0" width="2.45" height="35.5" fill="var(--up)"/>
<line x1="366.3" y1="464.0" x2="366.3" y2="490.5" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="475.1" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="370.2" y1="454.9" x2="370.2" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="456.8" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="374.2" y1="427.8" x2="374.2" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="429.9" width="2.45" height="30.1" fill="var(--up)"/>
<line x1="378.2" y1="394.2" x2="378.2" y2="434.2" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="399.0" width="2.45" height="35.2" fill="var(--up)"/>
<line x1="382.1" y1="385.1" x2="382.1" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="390.8" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="386.1" y1="378.4" x2="386.1" y2="404.2" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="383.3" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="390.0" y1="377.0" x2="390.0" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="377.0" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="394.0" y1="372.5" x2="394.0" y2="411.4" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="384.7" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="397.9" y1="383.7" x2="397.9" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="389.4" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="401.9" y1="412.7" x2="401.9" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="416.0" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="405.8" y1="399.0" x2="405.8" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="399.6" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="409.8" y1="362.3" x2="409.8" y2="406.5" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="362.8" width="2.45" height="38.4" fill="var(--up)"/>
<line x1="413.7" y1="346.8" x2="413.7" y2="375.7" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="366.3" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="417.7" y1="336.4" x2="417.7" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="362.0" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="421.6" y1="298.1" x2="421.6" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="301.4" width="2.45" height="58.5" fill="var(--up)"/>
<line x1="425.6" y1="263.5" x2="425.6" y2="306.9" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="281.5" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="429.5" y1="177.1" x2="429.5" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="184.6" width="2.45" height="79.2" fill="var(--up)"/>
<line x1="433.5" y1="120.1" x2="433.5" y2="167.8" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="142.4" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="437.4" y1="119.2" x2="437.4" y2="154.2" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="125.3" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="441.4" y1="84.5" x2="441.4" y2="128.7" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="87.8" width="2.45" height="38.5" fill="var(--up)"/>
<line x1="445.3" y1="94.9" x2="445.3" y2="158.1" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="100.3" width="2.45" height="38.4" fill="var(--down)"/>
<line x1="449.3" y1="126.8" x2="449.3" y2="173.3" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="132.4" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="453.2" y1="90.6" x2="453.2" y2="144.4" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="104.8" width="2.45" height="19.0" fill="var(--up)"/>
<line x1="457.2" y1="75.3" x2="457.2" y2="130.9" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="97.0" width="2.45" height="32.4" fill="var(--down)"/>
<line x1="461.1" y1="120.9" x2="461.1" y2="157.3" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="129.5" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="465.1" y1="125.2" x2="465.1" y2="210.4" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="143.1" width="2.45" height="53.2" fill="var(--down)"/>
<line x1="469.1" y1="163.3" x2="469.1" y2="212.7" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="165.1" width="2.45" height="32.9" fill="var(--up)"/>
<line x1="473.0" y1="156.7" x2="473.0" y2="181.0" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="162.5" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="477.0" y1="157.7" x2="477.0" y2="182.4" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="158.1" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="480.9" y1="109.1" x2="480.9" y2="167.0" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="115.3" width="2.45" height="48.5" fill="var(--up)"/>
<line x1="484.9" y1="96.7" x2="484.9" y2="122.2" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="99.8" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="488.8" y1="100.3" x2="488.8" y2="144.7" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="104.5" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="492.8" y1="93.2" x2="492.8" y2="130.0" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="98.7" width="2.45" height="26.0" fill="var(--down)"/>
<line x1="496.7" y1="90.5" x2="496.7" y2="121.6" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="97.3" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="500.7" y1="99.8" x2="500.7" y2="130.2" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="106.0" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="504.6" y1="129.2" x2="504.6" y2="174.2" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="137.8" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="508.6" y1="145.6" x2="508.6" y2="178.0" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="156.8" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="512.5" y1="177.6" x2="512.5" y2="218.6" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="193.3" width="2.45" height="18.5" fill="var(--down)"/>
<line x1="516.5" y1="226.6" x2="516.5" y2="270.2" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="227.9" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="520.4" y1="189.9" x2="520.4" y2="244.7" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="201.3" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="524.4" y1="184.4" x2="524.4" y2="225.9" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="210.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="528.3" y1="209.1" x2="528.3" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="216.7" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="532.3" y1="201.2" x2="532.3" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="235.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="536.2" y1="201.5" x2="536.2" y2="230.3" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="222.2" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="540.2" y1="200.7" x2="540.2" y2="251.8" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="203.4" width="2.45" height="46.1" fill="var(--down)"/>
<line x1="544.1" y1="231.9" x2="544.1" y2="267.7" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="235.5" width="2.45" height="29.5" fill="var(--down)"/>
<line x1="548.1" y1="269.8" x2="548.1" y2="305.7" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="280.8" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="552.0" y1="288.1" x2="552.0" y2="313.6" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="299.8" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="556.0" y1="304.1" x2="556.0" y2="355.7" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="316.3" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="560.0" y1="318.2" x2="560.0" y2="348.1" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="318.2" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="563.9" y1="314.7" x2="563.9" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="339.9" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="567.9" y1="324.0" x2="567.9" y2="359.6" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="325.4" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="571.8" y1="307.4" x2="571.8" y2="338.8" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="322.9" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="575.8" y1="289.8" x2="575.8" y2="341.4" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="308.8" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="579.7" y1="241.1" x2="579.7" y2="304.6" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="260.9" width="2.45" height="38.0" fill="var(--up)"/>
<line x1="583.7" y1="250.2" x2="583.7" y2="294.5" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="250.2" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="587.6" y1="282.1" x2="587.6" y2="306.0" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="288.4" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="591.6" y1="257.9" x2="591.6" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="258.5" width="2.45" height="29.8" fill="var(--up)"/>
<line x1="595.5" y1="260.4" x2="595.5" y2="278.9" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="262.1" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="599.5" y1="264.5" x2="599.5" y2="314.8" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="269.1" width="2.45" height="37.6" fill="var(--down)"/>
<line x1="603.4" y1="286.3" x2="603.4" y2="325.2" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="286.5" width="2.45" height="37.0" fill="var(--up)"/>
<line x1="607.4" y1="245.9" x2="607.4" y2="306.2" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="252.5" width="2.45" height="48.0" fill="var(--up)"/>
<line x1="611.3" y1="248.7" x2="611.3" y2="267.2" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="256.6" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="615.3" y1="258.3" x2="615.3" y2="284.6" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="258.8" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="619.2" y1="263.4" x2="619.2" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="274.9" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="623.2" y1="274.4" x2="623.2" y2="305.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="283.7" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="627.1" y1="223.3" x2="627.1" y2="293.4" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="241.2" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="631.1" y1="220.3" x2="631.1" y2="265.4" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="242.7" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="635.0" y1="235.4" x2="635.0" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="236.6" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="639.0" y1="258.2" x2="639.0" y2="300.1" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="262.0" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="642.9" y1="255.9" x2="642.9" y2="302.4" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="283.0" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="646.9" y1="263.6" x2="646.9" y2="289.4" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="275.1" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="650.9" y1="267.8" x2="650.9" y2="288.3" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="272.2" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="654.8" y1="263.1" x2="654.8" y2="296.7" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="277.3" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="658.8" y1="244.6" x2="658.8" y2="279.9" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="261.2" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="662.7" y1="265.1" x2="662.7" y2="303.3" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="276.5" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="666.7" y1="233.3" x2="666.7" y2="280.5" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="239.8" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="670.6" y1="220.7" x2="670.6" y2="265.9" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="226.4" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="674.6" y1="262.1" x2="674.6" y2="300.8" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="272.6" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="678.5" y1="267.4" x2="678.5" y2="315.2" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="283.5" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="682.5" y1="259.6" x2="682.5" y2="285.6" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="271.8" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="686.4" y1="254.2" x2="686.4" y2="285.5" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="267.7" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="690.4" y1="254.9" x2="690.4" y2="291.9" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="261.8" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="694.3" y1="287.8" x2="694.3" y2="359.2" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="291.7" width="2.45" height="63.1" fill="var(--down)"/>
<line x1="698.3" y1="312.9" x2="698.3" y2="368.1" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="323.9" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="702.2" y1="306.3" x2="702.2" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="338.6" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="706.2" y1="347.5" x2="706.2" y2="370.8" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="353.7" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="710.1" y1="345.9" x2="710.1" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="352.9" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="714.1" y1="345.8" x2="714.1" y2="379.3" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="347.5" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="718.0" y1="314.8" x2="718.0" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="342.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="722.0" y1="339.1" x2="722.0" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="352.8" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="725.9" y1="351.5" x2="725.9" y2="393.2" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="356.3" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="729.9" y1="336.7" x2="729.9" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="340.1" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="733.8" y1="344.2" x2="733.8" y2="404.3" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="351.0" width="2.45" height="51.0" fill="var(--down)"/>
<line x1="737.8" y1="361.1" x2="737.8" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="376.0" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="741.8" y1="364.9" x2="741.8" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="375.6" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="745.7" y1="388.2" x2="745.7" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="408.9" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="749.7" y1="421.9" x2="749.7" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="441.2" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="753.6" y1="437.4" x2="753.6" y2="463.7" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="448.7" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="757.6" y1="427.4" x2="757.6" y2="451.6" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="441.8" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="761.5" y1="401.8" x2="761.5" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="412.4" width="2.45" height="34.3" fill="var(--down)"/>
<line x1="765.5" y1="419.0" x2="765.5" y2="458.7" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="449.7" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="769.4" y1="450.4" x2="769.4" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="462.3" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="773.4" y1="419.5" x2="773.4" y2="463.2" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="438.8" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="777.3" y1="405.0" x2="777.3" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="419.3" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="781.3" y1="405.6" x2="781.3" y2="428.8" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="412.4" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="785.2" y1="418.8" x2="785.2" y2="443.5" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="419.9" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="789.2" y1="388.2" x2="789.2" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="394.8" width="2.45" height="40.9" fill="var(--up)"/>
<line x1="793.1" y1="377.2" x2="793.1" y2="410.3" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="387.0" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="797.1" y1="399.6" x2="797.1" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="404.2" width="2.45" height="49.7" fill="var(--down)"/>
<line x1="801.0" y1="439.4" x2="801.0" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="448.4" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="805.0" y1="442.5" x2="805.0" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="457.8" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="808.9" y1="427.4" x2="808.9" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="427.4" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="812.9" y1="426.6" x2="812.9" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="445.2" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="816.8" y1="434.7" x2="816.8" y2="482.0" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="448.8" width="2.45" height="31.3" fill="var(--down)"/>
<line x1="820.8" y1="446.9" x2="820.8" y2="471.5" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="456.4" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="824.7" y1="444.0" x2="824.7" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="449.0" width="2.45" height="41.7" fill="var(--down)"/>
<line x1="828.7" y1="484.9" x2="828.7" y2="538.1" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="489.1" width="2.45" height="43.2" fill="var(--down)"/>
<line x1="832.7" y1="457.0" x2="832.7" y2="516.9" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="459.3" width="2.45" height="50.0" fill="var(--up)"/>
<line x1="836.6" y1="414.0" x2="836.6" y2="446.6" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="420.5" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="840.6" y1="414.5" x2="840.6" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="420.3" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="844.5" y1="359.5" x2="844.5" y2="416.5" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="385.5" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="848.5" y1="398.0" x2="848.5" y2="443.1" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="398.0" width="2.45" height="44.2" fill="var(--down)"/>
<line x1="852.4" y1="490.0" x2="852.4" y2="541.3" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="501.1" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="856.4" y1="499.8" x2="856.4" y2="533.4" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="507.2" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="860.3" y1="470.8" x2="860.3" y2="502.5" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="493.1" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="864.3" y1="489.3" x2="864.3" y2="532.1" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="496.2" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="868.2" y1="512.1" x2="868.2" y2="541.8" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="532.3" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="872.2" y1="478.8" x2="872.2" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="481.2" width="2.45" height="30.3" fill="var(--up)"/>
<line x1="876.1" y1="449.2" x2="876.1" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="462.7" width="2.45" height="47.8" fill="var(--down)"/>
<line x1="880.1" y1="504.5" x2="880.1" y2="550.6" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="504.8" width="2.45" height="26.7" fill="var(--down)"/>
<line x1="884.0" y1="532.5" x2="884.0" y2="546.6" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="537.3" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="888.0" y1="520.1" x2="888.0" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="520.1" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="891.9" y1="533.0" x2="891.9" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="538.0" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="895.9" y1="510.4" x2="895.9" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="516.6" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="899.8" y1="470.1" x2="899.8" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="476.7" width="2.45" height="34.5" fill="var(--up)"/>
<line x1="903.8" y1="405.2" x2="903.8" y2="451.3" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="433.3" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="907.7" y1="407.8" x2="907.7" y2="441.3" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="429.7" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="911.7" y1="442.1" x2="911.7" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="460.1" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="915.6" y1="472.0" x2="915.6" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="479.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="919.6" y1="454.4" x2="919.6" y2="490.3" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="460.3" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="923.6" y1="484.0" x2="923.6" y2="510.4" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="485.4" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="927.5" y1="470.6" x2="927.5" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="471.1" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="931.5" y1="467.4" x2="931.5" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="472.9" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="935.4" y1="480.5" x2="935.4" y2="510.1" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="486.4" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="939.4" y1="492.7" x2="939.4" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="492.7" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="943.3" y1="492.9" x2="943.3" y2="513.3" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="494.1" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="947.3" y1="489.8" x2="947.3" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="490.5" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="951.2" y1="463.5" x2="951.2" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="466.1" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="955.2" y1="457.9" x2="955.2" y2="472.5" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="464.0" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="959.1" y1="475.4" x2="959.1" y2="503.6" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="477.7" width="2.45" height="18.6" fill="var(--down)"/>
<line x1="963.1" y1="463.9" x2="963.1" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="469.4" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="967.0" y1="428.0" x2="967.0" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="441.3" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="971.0" y1="431.3" x2="971.0" y2="459.9" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="447.7" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="974.9" y1="428.9" x2="974.9" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="429.9" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="978.9" y1="399.3" x2="978.9" y2="418.5" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="411.8" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="982.8" y1="425.0" x2="982.8" y2="447.7" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="426.8" width="2.45" height="18.5" fill="var(--down)"/>
<line x1="986.8" y1="439.9" x2="986.8" y2="458.5" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="439.9" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="990.7" y1="460.2" x2="990.7" y2="478.1" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="466.9" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="994.7" y1="457.7" x2="994.7" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="460.4" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="998.6" y1="460.8" x2="998.6" y2="482.5" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="460.8" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="1002.6" y1="455.9" x2="1002.6" y2="482.0" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="458.9" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="1006.5" y1="452.3" x2="1006.5" y2="482.9" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="467.4" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="1010.5" y1="464.5" x2="1010.5" y2="492.0" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="469.9" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="1014.5" y1="480.7" x2="1014.5" y2="506.6" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="502.6" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="1018.4" y1="486.9" x2="1018.4" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="493.6" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="1022.4" y1="497.8" x2="1022.4" y2="520.5" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="499.2" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="1026.3" y1="502.0" x2="1026.3" y2="518.6" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="505.7" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="1030.3" y1="505.8" x2="1030.3" y2="524.2" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="508.1" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="1034.2" y1="489.2" x2="1034.2" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="499.3" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="1038.2" y1="524.3" x2="1038.2" y2="540.5" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="527.6" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="1042.1" y1="524.0" x2="1042.1" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="532.0" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="1046.1" y1="538.5" x2="1046.1" y2="563.6" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="540.1" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="1050.0" y1="571.5" x2="1050.0" y2="606.4" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="572.7" width="2.45" height="31.2" fill="var(--down)"/>
<line x1="60" y1="407.7" x2="1052" y2="407.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="411.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$145 R1</text>
<text x="1058" y="423.2" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="341.3" x2="1052" y2="341.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="344.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$150 R2</text>
<text x="1058" y="356.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="240.9" x2="1052" y2="240.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="244.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$158 R3</text>
<text x="1058" y="256.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="603.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="595.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $130 (2026-09-18)</text>
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
| R3 | $158 | 4 | 2025-10-21·2026-03-30·2026-04-17·2026-05-01 — 2025년 가을과 2026년 봄의 반등 꼭대기. 현재가 대비 +22% |
| R2 | $150 | 4 | 2025-11-18·2025-12-03·2025-12-16·2026-07-07 — Elliott 합의 전후 구간과 Q2 실적 직전의 마지막 반등 |
| R1 | $145 | 4 | 2026-06-16·2026-07-17·2026-07-28·2026-08-24 — 여름 내내 네 번 시도했다가 매번 되밀린 자리. 현재가 대비 +12% |
| **현재가** | **$129.75** (2026-09-18 종가) | — | **기간 내 하단 스윙 저점 없음(신저가 구간)** — 아래쪽에 검출된 지지 레벨이 하나도 없다. 가장 가까운 저항은 R1 |
| 참고선 | $127.60 | — | 최근 **5년** 최저(2022년 가을, [주봉 문서](./10_technical_weekly.md) 참고). 현재가 **1.7% 아래**에 있어, 근시일 하방을 가늠할 유일한 참고점이다 |

> **레벨이 전부 위쪽에만 있다.** 최근 1년 내내 내려오기만 해서 되돌림 저점이 만들어지지 않았고, 그래서 아래쪽 클러스터가 0개다. **"지지가 없다"는 것은 하방이 열려 있다는 뜻이지 안전하다는 뜻이 아니다** — 유일하게 참고할 수 있는 것이 5년 최저($127.60)인데 1.7% 아래다.

> **R1·R2·R3가 각각 4회씩 터치됐다는 점이 이 표의 특징이다.** 저항이 세 겹으로 촘촘하게 쌓여 있어, 반등하더라도 $145 → $150 → $158을 차례로 넘어야 한다. 위 저항 중 가장 최근 것(R1, 2026-08-24)까지 되밀린 뒤 한 달 만에 −11% 내려온 것이 현재 위치다.

---

## 3. 관측된 특이 구간 — 2026-07-09 FY2026 Q2 실적 발표와 2026-09-18 신저가

**① 2026-07-09 — Q2 실적 발표 갭다운**

- FY2026 Q2 실적이 발표된 날이다([최근 뉴스 / 이슈](./08_news.md) 로그 2026-07-09 항목). 매출은 컨센서스를 넘겼지만 **북미(PFNA 유기적 −2%)와 코어 영업이익률(−0.4%p)**이 실망을 샀다.
- 종가 기준 전일 대비 **−3.3%** ($142.51 → $137.86), 장중 저가 $134.69. 거래량은 평소(일 778만 주 내외) 대비 약 **2.4배**인 **1,876만 주**.
- 이 하루로 $140대가 저항으로 바뀌었다. 이후 8월에 R1($145)까지 한 번 되밀어 올렸다가 다시 내려왔다.

**② 2026-09-18 — 1년 최저 경신**

- 종가 **$129.75**(전일 대비 **−2.9%**, $133.66 → $129.75), 장중 저가 **$129.55**로 최근 1년 최저. 거래량 **2,352만 주**로 평소의 약 **3.0배**.
- 직전 주에 애널리스트 목표가 하향이 이어졌다(Barclays $144, 2026-09-13). 다만 **2026-09-18은 9월 셋째 금요일로 지수·옵션 동시 만기일**이라 거래량이 구조적으로 부푸는 날이므로, 3배 거래량 전부를 뉴스 반응으로 읽으면 안 된다.
- 이 하루로 1년 저점 구조가 갱신돼 아래쪽 참고점이 **5년 최저($127.60)**밖에 남지 않았다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-19~2026-09-18. 수집 시점: 2026-09-20. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PEP --name "펩시코" --close-on 2026-09-18 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **아래쪽 레벨이 0개라는 점이 이 문서의 가장 큰 한계다.** 스크립트는 "기간 내 하단 스윙 저점 없음(신저가 구간)"으로 판정했고, 이는 지지가 강하거나 약하다는 판단이 아니라 **판단할 표본이 없다**는 뜻이다. 하방을 보려면 1년이 아니라 5년 구간이 필요하며 [주봉 문서](./10_technical_weekly.md)의 S1($128)을 함께 봐야 한다.
    - **3절 ②의 거래량은 만기일 효과를 포함한다.** 같은 날 다른 대형주도 거래량이 부풀었을 가능성이 높아, 이 하루만으로 매도 압력의 크기를 추정하지 않는다.
    - **기간 내 배당이 4회 있었고 원주가라 반영돼 있지 않다.** 배당수익률이 4.56%로 높은 종목이라 **1년 가격 하락률(−24%)과 총수익률의 차이가 크다** — 이 차트의 하락률을 투자 손익으로 그대로 읽으면 안 된다.
    - 해당 기간에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다.

---

*작성일: 2026-09-20*
