# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-10 종가 **$136.65**는 [핵심 지표 A.2](./04_metrics.md)·[밸류에이션 / 적정주가 5. 결론 — 목표주가와 판단](./06_valuation.md)에 인용된 값과 **일치**한다.

:::

---

## 1. 차트 — 최근 1년 일봉 (2025-09-11 ~ 2026-09-10)

<div class="pep-chart">
<style>
.pep-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .pep-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .pep-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.pep-chart svg { width:100%; height:auto; display:block; }
.pep-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.pep-chart .title { fill: var(--ink); font-weight:600; }
.pep-chart .grid { stroke: var(--grid); stroke-width:1; }
.pep-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="펩시코(PEP) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">펩시코 (PEP) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-11 ~ 2026-09-10 · 마지막 종가 $136.65 (2026-09-10) · 단위 USD</text>
<line x1="60" y1="520.4" x2="1052" y2="520.4" class="grid"/>
<text x="52" y="524.4" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="379.7" x2="1052" y2="379.7" class="grid"/>
<text x="52" y="383.7" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="239.0" x2="1052" y2="239.0" class="grid"/>
<text x="52" y="243.0" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="98.2" x2="1052" y2="98.2" class="grid"/>
<text x="52" y="102.2" font-size="11" text-anchor="end" fill="var(--muted)">170</text>
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
<line x1="62.0" y1="453.6" x2="62.0" y2="485.3" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="460.9" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="65.9" y1="460.6" x2="65.9" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="463.2" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="69.9" y1="470.8" x2="69.9" y2="513.0" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="472.6" width="2.45" height="38.8" fill="var(--down)"/>
<line x1="73.8" y1="502.0" x2="73.8" y2="521.7" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="510.7" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="77.8" y1="491.7" x2="77.8" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="503.1" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="81.7" y1="497.5" x2="81.7" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="510.2" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="85.7" y1="491.2" x2="85.7" y2="514.0" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="495.7" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="89.6" y1="499.1" x2="89.6" y2="521.3" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="505.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="93.6" y1="489.1" x2="93.6" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="493.7" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="97.5" y1="487.5" x2="97.5" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="489.9" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="101.5" y1="472.3" x2="101.5" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="478.2" width="2.45" height="43.3" fill="var(--down)"/>
<line x1="105.5" y1="506.5" x2="105.5" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="514.3" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="109.4" y1="511.0" x2="109.4" y2="532.8" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="514.3" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="113.4" y1="505.9" x2="113.4" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="514.3" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="117.3" y1="473.0" x2="117.3" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="476.3" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="121.3" y1="474.7" x2="121.3" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="487.9" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="125.2" y1="473.2" x2="125.2" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="488.6" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="129.2" y1="494.4" x2="129.2" y2="536.2" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="495.5" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="133.1" y1="494.5" x2="133.1" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="509.3" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="137.1" y1="506.7" x2="137.1" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="509.3" width="2.45" height="27.4" fill="var(--down)"/>
<line x1="141.0" y1="453.7" x2="141.0" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="454.2" width="2.45" height="59.8" fill="var(--up)"/>
<line x1="145.0" y1="368.2" x2="145.0" y2="450.1" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="378.6" width="2.45" height="62.6" fill="var(--up)"/>
<line x1="148.9" y1="380.0" x2="148.9" y2="417.1" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="395.3" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="152.9" y1="356.9" x2="152.9" y2="400.8" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="358.0" width="2.45" height="40.1" fill="var(--up)"/>
<line x1="156.8" y1="346.1" x2="156.8" y2="391.4" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="361.0" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="160.8" y1="318.1" x2="160.8" y2="347.5" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="342.1" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="164.7" y1="324.7" x2="164.7" y2="355.2" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="326.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="168.7" y1="317.5" x2="168.7" y2="341.4" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="317.5" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="172.6" y1="306.7" x2="172.6" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="313.6" width="2.45" height="21.4" fill="var(--down)"/>
<line x1="176.6" y1="306.8" x2="176.6" y2="341.6" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="335.4" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="180.5" y1="331.9" x2="180.5" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="335.1" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="184.5" y1="345.6" x2="184.5" y2="361.8" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="351.0" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="188.4" y1="339.3" x2="188.4" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="342.7" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="192.4" y1="334.5" x2="192.4" y2="380.8" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="359.9" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="196.4" y1="398.6" x2="196.4" y2="468.8" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="407.1" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="200.3" y1="406.6" x2="200.3" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="414.2" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="204.3" y1="421.9" x2="204.3" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="433.2" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="208.2" y1="437.3" x2="208.2" y2="474.7" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="438.0" width="2.45" height="31.8" fill="var(--down)"/>
<line x1="212.2" y1="451.1" x2="212.2" y2="491.5" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="454.3" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="216.1" y1="474.3" x2="216.1" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="479.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="220.1" y1="475.3" x2="220.1" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="486.5" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="224.0" y1="463.4" x2="224.0" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="478.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="228.0" y1="477.9" x2="228.0" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="483.6" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="231.9" y1="439.4" x2="231.9" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="448.9" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="235.9" y1="443.0" x2="235.9" y2="463.3" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="456.3" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="239.8" y1="430.5" x2="239.8" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="449.8" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="243.8" y1="424.2" x2="243.8" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="437.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="247.7" y1="406.3" x2="247.7" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="410.2" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="251.7" y1="382.1" x2="251.7" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="397.0" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="255.6" y1="396.6" x2="255.6" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="403.6" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="259.6" y1="420.8" x2="259.6" y2="451.5" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="427.6" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="263.5" y1="394.6" x2="263.5" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="431.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="267.5" y1="431.2" x2="267.5" y2="453.5" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="438.4" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="271.4" y1="420.2" x2="271.4" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="434.5" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="275.4" y1="401.2" x2="275.4" y2="432.8" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="408.1" width="2.45" height="23.4" fill="var(--up)"/>
<line x1="279.3" y1="396.3" x2="279.3" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="397.4" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="283.3" y1="382.2" x2="283.3" y2="400.7" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="386.6" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="287.3" y1="386.6" x2="287.3" y2="428.5" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="387.3" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="291.2" y1="369.9" x2="291.2" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="398.1" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="295.2" y1="404.3" x2="295.2" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="411.4" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="299.1" y1="438.8" x2="299.1" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="441.3" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="303.1" y1="428.1" x2="303.1" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="441.2" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="307.0" y1="414.0" x2="307.0" y2="465.4" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="431.1" width="2.45" height="24.1" fill="var(--down)"/>
<line x1="311.0" y1="382.8" x2="311.0" y2="421.9" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="383.9" width="2.45" height="27.2" fill="var(--up)"/>
<line x1="314.9" y1="367.2" x2="314.9" y2="406.0" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="377.6" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="318.9" y1="370.3" x2="318.9" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="370.6" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="322.8" y1="355.8" x2="322.8" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="362.5" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="326.8" y1="346.6" x2="326.8" y2="379.8" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="351.7" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="330.7" y1="362.3" x2="330.7" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="374.4" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="334.7" y1="374.5" x2="334.7" y2="390.3" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="382.5" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="338.6" y1="381.3" x2="338.6" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="391.7" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="342.6" y1="394.1" x2="342.6" y2="430.2" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="414.5" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="346.5" y1="419.3" x2="346.5" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="419.3" width="2.45" height="49.4" fill="var(--down)"/>
<line x1="350.5" y1="464.3" x2="350.5" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="467.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="354.4" y1="465.0" x2="354.4" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="467.2" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="358.4" y1="449.4" x2="358.4" y2="469.8" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="460.8" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="362.3" y1="446.3" x2="362.3" y2="465.3" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="461.9" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="366.3" y1="463.7" x2="366.3" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="466.5" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="370.2" y1="472.5" x2="370.2" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="475.1" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="374.2" y1="495.0" x2="374.2" y2="528.9" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="497.1" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="378.2" y1="519.6" x2="378.2" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="524.9" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="382.1" y1="522.8" x2="382.1" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="531.4" width="2.45" height="31.1" fill="var(--down)"/>
<line x1="386.1" y1="527.8" x2="386.1" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="529.3" width="2.45" height="39.4" fill="var(--up)"/>
<line x1="390.0" y1="509.3" x2="390.0" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="521.7" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="394.0" y1="499.2" x2="394.0" y2="540.7" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="501.3" width="2.45" height="20.4" fill="var(--up)"/>
<line x1="397.9" y1="469.1" x2="397.9" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="471.5" width="2.45" height="33.5" fill="var(--up)"/>
<line x1="401.9" y1="431.8" x2="401.9" y2="476.3" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="437.1" width="2.45" height="39.1" fill="var(--up)"/>
<line x1="405.8" y1="421.6" x2="405.8" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="428.0" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="409.8" y1="414.2" x2="409.8" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="419.7" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="413.7" y1="412.6" x2="413.7" y2="459.6" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="412.6" width="2.45" height="20.3" fill="var(--up)"/>
<line x1="417.7" y1="407.7" x2="417.7" y2="450.9" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="421.2" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="421.6" y1="420.1" x2="421.6" y2="461.8" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="426.4" width="2.45" height="32.1" fill="var(--down)"/>
<line x1="425.6" y1="452.3" x2="425.6" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="456.0" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="429.5" y1="437.1" x2="429.5" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="437.8" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="433.5" y1="396.3" x2="433.5" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="396.9" width="2.45" height="42.6" fill="var(--up)"/>
<line x1="437.4" y1="379.1" x2="437.4" y2="411.2" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="400.8" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="441.4" y1="367.6" x2="441.4" y2="401.7" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="396.0" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="445.3" y1="325.0" x2="445.3" y2="399.5" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="328.6" width="2.45" height="65.0" fill="var(--up)"/>
<line x1="449.3" y1="286.5" x2="449.3" y2="334.8" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="306.5" width="2.45" height="16.0" fill="var(--up)"/>
<line x1="453.2" y1="190.5" x2="453.2" y2="302.3" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="198.9" width="2.45" height="88.0" fill="var(--up)"/>
<line x1="457.2" y1="127.2" x2="457.2" y2="180.3" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="152.0" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="461.1" y1="126.2" x2="461.1" y2="165.1" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="133.0" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="465.1" y1="87.7" x2="465.1" y2="136.8" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="91.3" width="2.45" height="42.8" fill="var(--up)"/>
<line x1="469.1" y1="99.2" x2="469.1" y2="169.4" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="105.3" width="2.45" height="42.6" fill="var(--down)"/>
<line x1="473.0" y1="134.7" x2="473.0" y2="186.3" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="140.9" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="477.0" y1="94.4" x2="477.0" y2="154.2" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="110.2" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="480.9" y1="77.4" x2="480.9" y2="139.2" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="101.6" width="2.45" height="36.0" fill="var(--down)"/>
<line x1="484.9" y1="128.1" x2="484.9" y2="168.6" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="137.6" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="488.8" y1="132.8" x2="488.8" y2="227.6" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="152.8" width="2.45" height="59.1" fill="var(--down)"/>
<line x1="492.8" y1="175.2" x2="492.8" y2="230.1" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="177.2" width="2.45" height="36.6" fill="var(--up)"/>
<line x1="496.7" y1="167.9" x2="496.7" y2="194.9" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="174.4" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="500.7" y1="169.0" x2="500.7" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="169.4" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="504.6" y1="115.0" x2="504.6" y2="179.3" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="121.9" width="2.45" height="53.9" fill="var(--up)"/>
<line x1="508.6" y1="101.2" x2="508.6" y2="129.6" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="104.7" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="512.5" y1="105.3" x2="512.5" y2="154.5" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="109.9" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="516.5" y1="97.4" x2="516.5" y2="138.2" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="103.4" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="520.4" y1="94.3" x2="520.4" y2="128.9" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="101.9" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="524.4" y1="104.7" x2="524.4" y2="138.5" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="111.6" width="2.45" height="24.9" fill="var(--down)"/>
<line x1="528.3" y1="137.3" x2="528.3" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="146.9" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="532.3" y1="155.5" x2="532.3" y2="191.5" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="168.0" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="536.2" y1="191.1" x2="536.2" y2="236.7" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="208.6" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="540.2" y1="245.6" x2="540.2" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="247.0" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="544.1" y1="204.8" x2="544.1" y2="265.7" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="217.4" width="2.45" height="33.2" fill="var(--up)"/>
<line x1="548.1" y1="198.7" x2="548.1" y2="244.7" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="228.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="552.0" y1="226.2" x2="552.0" y2="268.7" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="234.6" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="556.0" y1="217.3" x2="556.0" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="254.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="560.0" y1="217.7" x2="560.0" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="240.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="563.9" y1="216.7" x2="563.9" y2="273.6" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="219.8" width="2.45" height="51.2" fill="var(--down)"/>
<line x1="567.9" y1="251.5" x2="567.9" y2="291.2" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="255.4" width="2.45" height="32.8" fill="var(--down)"/>
<line x1="571.8" y1="293.6" x2="571.8" y2="333.4" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="305.8" width="2.45" height="24.1" fill="var(--down)"/>
<line x1="575.8" y1="313.8" x2="575.8" y2="342.3" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="326.9" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="579.7" y1="331.7" x2="579.7" y2="389.0" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="345.2" width="2.45" height="33.9" fill="var(--down)"/>
<line x1="583.7" y1="347.3" x2="583.7" y2="380.5" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="347.3" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="587.6" y1="343.4" x2="587.6" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="371.4" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="591.6" y1="353.8" x2="591.6" y2="393.4" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="355.4" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="595.5" y1="335.4" x2="595.5" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="352.5" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="599.5" y1="315.8" x2="599.5" y2="373.1" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="336.9" width="2.45" height="26.7" fill="var(--up)"/>
<line x1="603.4" y1="261.6" x2="603.4" y2="332.3" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="283.7" width="2.45" height="42.2" fill="var(--up)"/>
<line x1="607.4" y1="271.8" x2="607.4" y2="321.0" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="271.8" width="2.45" height="33.5" fill="var(--down)"/>
<line x1="611.3" y1="307.2" x2="611.3" y2="333.8" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="314.3" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="615.3" y1="280.3" x2="615.3" y2="320.3" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="281.0" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="619.2" y1="283.2" x2="619.2" y2="303.7" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="285.0" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="623.2" y1="287.7" x2="623.2" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="292.7" width="2.45" height="41.8" fill="var(--down)"/>
<line x1="627.1" y1="311.9" x2="627.1" y2="355.1" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="312.1" width="2.45" height="41.1" fill="var(--up)"/>
<line x1="631.1" y1="267.0" x2="631.1" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="274.3" width="2.45" height="53.3" fill="var(--up)"/>
<line x1="635.0" y1="270.1" x2="635.0" y2="290.6" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="278.9" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="639.0" y1="280.8" x2="639.0" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="281.3" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="642.9" y1="286.4" x2="642.9" y2="319.3" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="299.2" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="646.9" y1="298.6" x2="646.9" y2="332.7" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="309.1" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="650.9" y1="241.9" x2="650.9" y2="319.7" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="261.8" width="2.45" height="40.0" fill="var(--up)"/>
<line x1="654.8" y1="238.5" x2="654.8" y2="288.6" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="263.5" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="658.8" y1="255.3" x2="658.8" y2="297.5" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="256.7" width="2.45" height="24.6" fill="var(--down)"/>
<line x1="662.7" y1="280.6" x2="662.7" y2="327.2" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="284.8" width="2.45" height="25.6" fill="var(--down)"/>
<line x1="666.7" y1="278.1" x2="666.7" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="308.2" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="670.6" y1="286.7" x2="670.6" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="299.5" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="674.6" y1="291.3" x2="674.6" y2="314.1" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="296.2" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="678.5" y1="286.1" x2="678.5" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="301.9" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="682.5" y1="265.6" x2="682.5" y2="304.8" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="284.0" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="686.4" y1="288.4" x2="686.4" y2="330.7" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="301.0" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="690.4" y1="253.0" x2="690.4" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="260.2" width="2.45" height="35.3" fill="var(--up)"/>
<line x1="694.3" y1="239.0" x2="694.3" y2="289.2" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="245.3" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="698.3" y1="285.0" x2="698.3" y2="328.1" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="296.7" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="702.2" y1="290.9" x2="702.2" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="308.8" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="706.2" y1="282.2" x2="706.2" y2="311.2" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="295.8" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="710.1" y1="276.3" x2="710.1" y2="311.0" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="291.2" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="714.1" y1="277.0" x2="714.1" y2="318.1" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="284.7" width="2.45" height="30.0" fill="var(--down)"/>
<line x1="718.0" y1="313.6" x2="718.0" y2="392.9" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="317.9" width="2.45" height="70.1" fill="var(--down)"/>
<line x1="722.0" y1="341.4" x2="722.0" y2="402.8" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="353.7" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="725.9" y1="334.1" x2="725.9" y2="394.3" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="370.0" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="729.9" y1="379.8" x2="729.9" y2="405.7" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="386.7" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="733.8" y1="378.2" x2="733.8" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="385.9" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="737.8" y1="378.0" x2="737.8" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="379.8" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="741.8" y1="343.5" x2="741.8" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="374.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="745.7" y1="370.6" x2="745.7" y2="402.4" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="385.8" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="749.7" y1="384.3" x2="749.7" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="389.7" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="753.6" y1="367.9" x2="753.6" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="371.7" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="757.6" y1="376.2" x2="757.6" y2="443.0" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="383.8" width="2.45" height="56.7" fill="var(--down)"/>
<line x1="761.5" y1="395.0" x2="761.5" y2="440.2" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="411.5" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="765.5" y1="399.3" x2="765.5" y2="441.3" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="411.1" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="769.4" y1="425.2" x2="769.4" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="448.1" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="773.4" y1="462.6" x2="773.4" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="484.0" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="777.3" y1="479.8" x2="777.3" y2="509.0" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="492.3" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="781.3" y1="468.7" x2="781.3" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="484.7" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="785.2" y1="440.2" x2="785.2" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="452.0" width="2.45" height="38.1" fill="var(--down)"/>
<line x1="789.2" y1="459.4" x2="789.2" y2="503.4" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="493.4" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="793.1" y1="494.3" x2="793.1" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="507.5" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="797.1" y1="459.9" x2="797.1" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="481.3" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="801.0" y1="443.7" x2="801.0" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="459.6" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="805.0" y1="444.4" x2="805.0" y2="470.2" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="452.0" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="808.9" y1="459.1" x2="808.9" y2="486.5" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="460.3" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="812.9" y1="425.2" x2="812.9" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="432.5" width="2.45" height="45.5" fill="var(--up)"/>
<line x1="816.8" y1="412.9" x2="816.8" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="423.8" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="820.8" y1="437.8" x2="820.8" y2="508.5" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="442.9" width="2.45" height="55.2" fill="var(--down)"/>
<line x1="824.7" y1="482.0" x2="824.7" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="492.0" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="828.7" y1="485.4" x2="828.7" y2="513.7" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="502.4" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="832.7" y1="468.7" x2="832.7" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="468.7" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="836.6" y1="467.8" x2="836.6" y2="496.9" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="488.5" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="840.6" y1="476.8" x2="840.6" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="492.4" width="2.45" height="34.8" fill="var(--down)"/>
<line x1="844.5" y1="490.3" x2="844.5" y2="517.6" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="500.9" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="848.5" y1="487.1" x2="848.5" y2="555.2" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="492.7" width="2.45" height="46.3" fill="var(--down)"/>
<line x1="852.4" y1="532.5" x2="852.4" y2="591.7" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="537.2" width="2.45" height="48.0" fill="var(--down)"/>
<line x1="856.4" y1="501.6" x2="856.4" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="504.1" width="2.45" height="55.6" fill="var(--up)"/>
<line x1="860.3" y1="453.7" x2="860.3" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="461.1" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="864.3" y1="454.3" x2="864.3" y2="501.0" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="460.8" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="868.2" y1="393.2" x2="868.2" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="422.1" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="872.2" y1="436.0" x2="872.2" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="436.0" width="2.45" height="49.1" fill="var(--down)"/>
<line x1="876.1" y1="538.2" x2="876.1" y2="595.2" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="550.6" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="880.1" y1="549.2" x2="880.1" y2="586.5" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="557.3" width="2.45" height="21.4" fill="var(--up)"/>
<line x1="884.0" y1="516.9" x2="884.0" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="541.7" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="888.0" y1="537.5" x2="888.0" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="545.1" width="2.45" height="39.4" fill="var(--down)"/>
<line x1="891.9" y1="562.8" x2="891.9" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="585.2" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="895.9" y1="525.8" x2="895.9" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="528.5" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="899.8" y1="492.9" x2="899.8" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="507.9" width="2.45" height="53.1" fill="var(--down)"/>
<line x1="903.8" y1="554.4" x2="903.8" y2="605.6" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="554.6" width="2.45" height="29.7" fill="var(--down)"/>
<line x1="907.7" y1="585.5" x2="907.7" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="590.8" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="911.7" y1="571.7" x2="911.7" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="571.7" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="915.6" y1="586.0" x2="915.6" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="591.5" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="919.6" y1="560.8" x2="919.6" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="567.7" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="923.6" y1="516.1" x2="923.6" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="523.4" width="2.45" height="38.3" fill="var(--up)"/>
<line x1="927.5" y1="444.0" x2="927.5" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="475.3" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="931.5" y1="446.8" x2="931.5" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="471.2" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="935.4" y1="485.0" x2="935.4" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="505.0" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="939.4" y1="518.2" x2="939.4" y2="543.2" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="526.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="943.3" y1="498.6" x2="943.3" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="505.2" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="947.3" y1="531.6" x2="947.3" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="533.1" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="951.2" y1="516.6" x2="951.2" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="517.2" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="955.2" y1="513.1" x2="955.2" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="519.2" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="959.1" y1="527.6" x2="959.1" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="534.2" width="2.45" height="20.8" fill="var(--up)"/>
<line x1="963.1" y1="541.3" x2="963.1" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="541.3" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="967.0" y1="541.4" x2="967.0" y2="564.1" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="542.8" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="971.0" y1="538.0" x2="971.0" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="538.7" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="974.9" y1="508.8" x2="974.9" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="511.7" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="978.9" y1="502.6" x2="978.9" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="509.3" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="982.8" y1="522.0" x2="982.8" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="524.5" width="2.45" height="20.7" fill="var(--down)"/>
<line x1="986.8" y1="509.2" x2="986.8" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="515.4" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="990.7" y1="469.4" x2="990.7" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="484.1" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="994.7" y1="473.0" x2="994.7" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="491.2" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="998.6" y1="470.3" x2="998.6" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="471.5" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="1002.6" y1="437.4" x2="1002.6" y2="458.8" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="451.3" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="1006.5" y1="466.0" x2="1006.5" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="467.9" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="1010.5" y1="482.6" x2="1010.5" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="482.6" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="1014.5" y1="505.1" x2="1014.5" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="512.6" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="1018.4" y1="502.3" x2="1018.4" y2="520.6" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="505.4" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="1022.4" y1="505.8" x2="1022.4" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="505.8" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="1026.3" y1="500.3" x2="1026.3" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="503.7" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="1030.3" y1="496.4" x2="1030.3" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="513.1" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="1034.2" y1="509.9" x2="1034.2" y2="540.4" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="515.9" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="1038.2" y1="527.9" x2="1038.2" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="552.3" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="1042.1" y1="534.8" x2="1042.1" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="542.3" width="2.45" height="20.4" fill="var(--up)"/>
<line x1="1046.1" y1="546.9" x2="1046.1" y2="572.1" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="548.5" width="2.45" height="18.6" fill="var(--down)"/>
<line x1="1050.0" y1="551.5" x2="1050.0" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="555.6" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="60" y1="451.9" x2="1052" y2="451.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="455.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$145 R1</text>
<text x="1058" y="467.4" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="372.9" x2="1052" y2="372.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="376.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$150 R2</text>
<text x="1058" y="388.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="261.4" x2="1052" y2="261.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="264.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$158 R3</text>
<text x="1058" y="276.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="569.1" x2="1052" y2="569.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="563.1" font-size="11.5" fill="var(--support)" font-weight="600">$137 S1</text>
<text x="1058" y="575.1" font-size="9.5" fill="var(--muted)">터치 6회</text>
<circle cx="1052.0" cy="567.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="559.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $137 (2026-09-10)</text>
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
| R3 | $158 | 4 | 2025-10-21·2026-03-30·2026-04-17·2026-05-01 — 2026년 봄의 거래 상단대 |
| R2 | $150 | 4 | 2025-11-18·2025-12-03·2025-12-16·2026-07-07 — Elliott 합의 전후의 반등 고점대 |
| R1 | $145 | 5 | 2025-09-25·2026-06-16·2026-07-17·2026-07-28·2026-08-24 — **1년 내내 반복해서 막힌 자리**(터치 5회) |
| **현재가** | **$136.65** (2026-09-10 종가) | — | **S1($137) 바로 아래** — 아래 설명 참고 |
| S1 | $137 | 6 | 2025-10-09·2026-01-08·2026-06-08·2026-06-30·2026-07-23·2026-08-12 — 1년 구간에서 **가장 많이 닿은 레벨**(터치 6회) |
| 참고선 | $133.73 | — | 최근 1년 최저(2026-07-20 주). S1 클러스터와 2.5% 안에 있어 별도 레벨로 잡히지 않았다 |

> **이 표에서 가장 중요한 것은 현재가가 S1 바로 아래에 있다는 사실이다.** 스크립트가 만든 표는 현재가를 "R1과 S1 사이"로 적지만, 실제 값은 $136.65 < $137이다. 1년 동안 여섯 번 지지로 작동한 자리를 **지금 막 아래로 통과한 상태**이고, 그 아래로는 1년 최저($133.73)까지 별다른 클러스터가 없다. 유효 클러스터가 저항 3개·지지 1개로 나온 것도 같은 이유다 — **1년 내내 방향이 아래였기 때문에 위쪽에만 스윙 고점이 쌓였다.**

---

## 3. 관측된 특이 구간 — 2026-07-09 FY2026 Q2 실적발표

- FY2026 2분기 실적 발표일이다. 유기적 매출 +2.4%로 가이던스를 유지했지만 **코어 영업이익률이 전년 동기보다 0.4%p 낮게 나왔다**([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−3.3%** ($142.51 → $137.86), 거래량은 평소(일 767만 주 내외) 대비 약 **2.4배**인 **1,876만 주**.
- 이 하락 이후 거래 레짐이 좁아졌다 — 그 전 $140~150에서 움직이던 주가가 **$134~145 박스**로 내려앉았고, 두 달간 그 안에서만 거래됐다. 위 표의 S1($137)에 몰린 터치 6회 중 절반이 이 구간에서 나왔다. **물량은 돌아왔는데 마진이 따라오지 않았다는 사실이 시장에 확인된 날**이며, 그 판정이 아직 뒤집히지 않았다는 것이 현재 레짐이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-11~2026-09-10. 수집 시점: 2026-09-11. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PEP --name "펩시코" --close-on 2026-09-10 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **현재가와 S1의 간격이 0.3%에 불과하다** — 클러스터 중심($137)과 현재가($136.65)의 차이가 허용오차(±2.5%) 안쪽이라, "지지 위인지 아래인지"를 이 방법론으로 단정할 수 없다. 위 §2의 서술은 두 숫자의 대소 비교일 뿐이다.
    - 기간 내 **주식분할은 없었다**(마지막 분할 1996년). 이 차트는 **원주가**라 기간 중 배당 4회가 반영돼 있지 않다 — 총수익률 기준으로 보면 실제 성과는 이보다 약 4.2%p 높다.

---

*작성일: 2026-09-11*
