# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉 데이터는 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-08-21 종가 **$277.51**은 [핵심 지표](./04_metrics.md) A.2 밸류에이션 지표 및 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 현재가와 **일치**한다. 이 차트는 원주가(배당 미반영)를 쓰므로, 같은 기간 수정주가와는 배당만큼 차이가 난다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-22 ~ 2026-08-21)

<div class="lng-chart">
<style>
.lng-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .lng-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .lng-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lng-chart svg { width:100%; height:auto; display:block; }
.lng-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lng-chart .title { fill: var(--ink); font-weight:600; }
.lng-chart .grid { stroke: var(--grid); stroke-width:1; }
.lng-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cheniere Energy(LNG) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cheniere Energy (LNG) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-22 ~ 2026-08-21 · 마지막 종가 $277.51 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="544.6" x2="1052" y2="544.6" class="grid"/>
<text x="52" y="548.6" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="451.5" x2="1052" y2="451.5" class="grid"/>
<text x="52" y="455.5" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
<line x1="60" y1="358.4" x2="1052" y2="358.4" class="grid"/>
<text x="52" y="362.4" font-size="11" text-anchor="end" fill="var(--muted)">240</text>
<line x1="60" y1="265.4" x2="1052" y2="265.4" class="grid"/>
<text x="52" y="269.4" font-size="11" text-anchor="end" fill="var(--muted)">260</text>
<line x1="60" y1="172.3" x2="1052" y2="172.3" class="grid"/>
<text x="52" y="176.3" font-size="11" text-anchor="end" fill="var(--muted)">280</text>
<line x1="60" y1="79.3" x2="1052" y2="79.3" class="grid"/>
<text x="52" y="83.3" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="85.7" y1="626.0" x2="85.7" y2="631.0" class="axis"/>
<text x="85.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="168.7" y1="626.0" x2="168.7" y2="631.0" class="axis"/>
<text x="168.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="259.6" y1="626.0" x2="259.6" y2="631.0" class="axis"/>
<text x="259.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="334.7" y1="626.0" x2="334.7" y2="631.0" class="axis"/>
<text x="334.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="421.6" y1="626.0" x2="421.6" y2="631.0" class="axis"/>
<text x="421.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="500.7" y1="626.0" x2="500.7" y2="631.0" class="axis"/>
<text x="500.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="575.8" y1="626.0" x2="575.8" y2="631.0" class="axis"/>
<text x="575.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="662.7" y1="626.0" x2="662.7" y2="631.0" class="axis"/>
<text x="662.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="745.7" y1="626.0" x2="745.7" y2="631.0" class="axis"/>
<text x="745.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="824.7" y1="626.0" x2="824.7" y2="631.0" class="axis"/>
<text x="824.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="907.7" y1="626.0" x2="907.7" y2="631.0" class="axis"/>
<text x="907.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="994.7" y1="626.0" x2="994.7" y2="631.0" class="axis"/>
<text x="994.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="351.1" x2="62.0" y2="372.9" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="355.2" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="65.9" y1="352.6" x2="65.9" y2="371.5" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="361.5" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="69.9" y1="346.6" x2="69.9" y2="365.4" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="351.1" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="73.8" y1="335.6" x2="73.8" y2="356.4" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="351.0" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="77.8" y1="346.4" x2="77.8" y2="361.8" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="346.4" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="81.7" y1="341.0" x2="81.7" y2="354.4" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="349.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="85.7" y1="347.1" x2="85.7" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="354.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="89.6" y1="342.2" x2="89.6" y2="364.0" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="351.0" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="93.6" y1="347.7" x2="93.6" y2="379.5" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="360.1" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="97.5" y1="367.8" x2="97.5" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="375.1" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="101.5" y1="368.4" x2="101.5" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="377.9" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="105.5" y1="370.9" x2="105.5" y2="386.6" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="383.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="109.4" y1="365.9" x2="109.4" y2="384.5" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="372.2" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="113.4" y1="366.2" x2="113.4" y2="381.7" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="372.1" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="117.3" y1="357.8" x2="117.3" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="368.9" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="121.3" y1="365.7" x2="121.3" y2="392.4" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="375.2" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="125.2" y1="379.8" x2="125.2" y2="391.5" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="381.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="129.2" y1="373.1" x2="129.2" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="380.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="133.1" y1="369.8" x2="133.1" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="384.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="137.1" y1="376.2" x2="137.1" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="378.6" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="141.0" y1="392.7" x2="141.0" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="399.4" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="145.0" y1="371.1" x2="145.0" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="382.1" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="148.9" y1="360.1" x2="148.9" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="374.2" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="152.9" y1="359.0" x2="152.9" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="369.5" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="156.8" y1="356.6" x2="156.8" y2="371.4" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="365.8" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="160.8" y1="365.5" x2="160.8" y2="387.4" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="365.5" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="164.7" y1="378.1" x2="164.7" y2="392.1" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="381.8" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="168.7" y1="377.1" x2="168.7" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="382.6" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="172.6" y1="379.0" x2="172.6" y2="400.0" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="395.2" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="176.6" y1="386.4" x2="176.6" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="393.1" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="180.5" y1="380.2" x2="180.5" y2="401.2" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="389.8" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="184.5" y1="374.1" x2="184.5" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="380.1" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="188.4" y1="370.3" x2="188.4" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="378.3" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="192.4" y1="366.3" x2="192.4" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="374.8" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="196.4" y1="388.0" x2="196.4" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="402.4" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="200.3" y1="406.4" x2="200.3" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="414.3" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="204.3" y1="417.4" x2="204.3" y2="435.9" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="422.6" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="208.2" y1="402.7" x2="208.2" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="414.3" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="212.2" y1="422.5" x2="212.2" y2="461.3" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="428.2" width="2.45" height="23.0" fill="var(--down)"/>
<line x1="216.1" y1="447.5" x2="216.1" y2="464.5" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="453.9" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="220.1" y1="442.3" x2="220.1" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="445.4" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="224.0" y1="431.8" x2="224.0" y2="444.3" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="441.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="228.0" y1="426.6" x2="228.0" y2="444.5" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="430.8" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="231.9" y1="415.6" x2="231.9" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="415.6" width="2.45" height="28.8" fill="var(--down)"/>
<line x1="235.9" y1="435.2" x2="235.9" y2="455.7" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="442.2" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="239.8" y1="446.9" x2="239.8" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="449.1" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="243.8" y1="451.5" x2="243.8" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="457.4" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="247.7" y1="467.2" x2="247.7" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="470.1" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="251.7" y1="469.7" x2="251.7" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="491.0" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="255.6" y1="484.1" x2="255.6" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="486.4" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="259.6" y1="478.4" x2="259.6" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="490.9" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="263.5" y1="499.9" x2="263.5" y2="516.7" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="508.7" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="267.5" y1="503.8" x2="267.5" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="505.8" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="271.4" y1="496.9" x2="271.4" y2="511.3" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="507.2" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="275.4" y1="504.2" x2="275.4" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="507.8" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="279.3" y1="489.7" x2="279.3" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="490.8" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="283.3" y1="478.3" x2="283.3" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="488.7" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="287.3" y1="472.2" x2="287.3" y2="492.1" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="481.5" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="291.2" y1="467.7" x2="291.2" y2="489.0" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="479.5" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="295.2" y1="465.7" x2="295.2" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="473.9" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="299.1" y1="461.7" x2="299.1" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="473.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="303.1" y1="466.4" x2="303.1" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="471.9" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="307.0" y1="496.3" x2="307.0" y2="519.0" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="499.8" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="311.0" y1="471.8" x2="311.0" y2="508.1" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="497.3" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="314.9" y1="500.6" x2="314.9" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="503.6" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="318.9" y1="521.3" x2="318.9" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="523.3" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="322.8" y1="521.1" x2="322.8" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="521.7" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="326.8" y1="510.4" x2="326.8" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="517.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="497.6" x2="330.7" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="505.2" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="334.7" y1="492.4" x2="334.7" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="494.8" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="338.6" y1="491.5" x2="338.6" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="493.8" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="342.6" y1="498.6" x2="342.6" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="500.6" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="346.5" y1="501.1" x2="346.5" y2="514.0" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="505.2" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="350.5" y1="500.4" x2="350.5" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="506.1" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="354.4" y1="522.9" x2="354.4" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="529.6" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="358.4" y1="533.9" x2="358.4" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="542.9" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="362.3" y1="545.0" x2="362.3" y2="584.8" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="549.2" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="366.3" y1="570.4" x2="366.3" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="579.1" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="370.2" y1="573.8" x2="370.2" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="580.4" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="374.2" y1="595.3" x2="374.2" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="595.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="378.2" y1="590.6" x2="378.2" y2="608.8" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="594.5" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="382.1" y1="582.3" x2="382.1" y2="599.4" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="589.5" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="386.1" y1="576.8" x2="386.1" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="591.8" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="390.0" y1="584.8" x2="390.0" y2="596.0" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="588.8" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="394.0" y1="587.3" x2="394.0" y2="596.7" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="591.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="397.9" y1="581.3" x2="397.9" y2="597.9" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="583.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="401.9" y1="580.8" x2="401.9" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="583.1" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="405.8" y1="588.5" x2="405.8" y2="599.8" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="589.1" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="409.8" y1="578.5" x2="409.8" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="579.0" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="413.7" y1="569.8" x2="413.7" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="575.1" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="417.7" y1="569.0" x2="417.7" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="570.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="421.6" y1="545.5" x2="421.6" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="554.8" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="425.6" y1="540.8" x2="425.6" y2="583.5" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="545.9" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="429.5" y1="549.6" x2="429.5" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="552.0" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="433.5" y1="548.2" x2="433.5" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="562.9" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="437.4" y1="549.0" x2="437.4" y2="565.8" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="560.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="441.4" y1="547.7" x2="441.4" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="554.2" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="445.3" y1="563.2" x2="445.3" y2="577.8" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="571.7" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="449.3" y1="566.3" x2="449.3" y2="581.7" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="570.9" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="453.2" y1="527.2" x2="453.2" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="545.9" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="457.2" y1="526.8" x2="457.2" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="531.8" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="461.1" y1="505.0" x2="461.1" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="513.4" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="465.1" y1="503.1" x2="465.1" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="510.7" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="469.1" y1="509.4" x2="469.1" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="510.6" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="473.0" y1="500.4" x2="473.0" y2="521.8" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="507.3" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="477.0" y1="501.1" x2="477.0" y2="515.8" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="506.2" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="480.9" y1="496.7" x2="480.9" y2="519.7" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="499.0" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="484.9" y1="508.5" x2="484.9" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="513.3" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="488.8" y1="493.7" x2="488.8" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="507.2" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="492.8" y1="481.1" x2="492.8" y2="494.7" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="484.1" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="496.7" y1="479.2" x2="496.7" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="485.2" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="500.7" y1="496.0" x2="500.7" y2="514.3" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="501.0" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="504.6" y1="493.5" x2="504.6" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="493.6" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="508.6" y1="480.0" x2="508.6" y2="515.8" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="480.1" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="512.5" y1="484.6" x2="512.5" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="485.0" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="516.5" y1="481.2" x2="516.5" y2="499.1" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="483.6" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="520.4" y1="471.2" x2="520.4" y2="484.5" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="471.8" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="524.4" y1="457.7" x2="524.4" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="459.1" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="528.3" y1="447.3" x2="528.3" y2="461.6" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="452.0" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="532.3" y1="437.9" x2="532.3" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="452.1" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="536.2" y1="443.2" x2="536.2" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="447.8" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="540.2" y1="435.0" x2="540.2" y2="462.9" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="439.9" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="544.1" y1="431.7" x2="544.1" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="434.2" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="548.1" y1="414.1" x2="548.1" y2="432.7" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="422.7" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="552.0" y1="418.2" x2="552.0" y2="432.9" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="421.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="556.0" y1="407.3" x2="556.0" y2="437.3" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="420.1" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="560.0" y1="441.4" x2="560.0" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="447.0" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="563.9" y1="442.4" x2="563.9" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="447.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="567.9" y1="374.4" x2="567.9" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="393.3" width="2.45" height="50.1" fill="var(--up)"/>
<line x1="571.8" y1="374.1" x2="571.8" y2="400.4" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="378.3" width="2.45" height="21.5" fill="var(--up)"/>
<line x1="575.8" y1="300.3" x2="575.8" y2="337.8" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="316.9" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="579.7" y1="285.0" x2="579.7" y2="339.1" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="302.6" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="583.7" y1="313.5" x2="583.7" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="316.7" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="587.6" y1="297.4" x2="587.6" y2="328.9" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="309.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="591.6" y1="268.9" x2="591.6" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="288.0" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="595.5" y1="272.5" x2="595.5" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="291.5" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="599.5" y1="311.9" x2="599.5" y2="344.6" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="311.9" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="603.4" y1="306.7" x2="603.4" y2="334.9" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="310.4" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="607.4" y1="273.1" x2="607.4" y2="308.8" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="294.1" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="611.3" y1="269.2" x2="611.3" y2="312.8" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="289.1" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="615.3" y1="295.2" x2="615.3" y2="320.5" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="299.5" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="619.2" y1="288.2" x2="619.2" y2="309.6" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="302.6" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="623.2" y1="231.7" x2="623.2" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="236.4" width="2.45" height="63.3" fill="var(--up)"/>
<line x1="627.1" y1="81.6" x2="627.1" y2="213.7" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="163.6" width="2.45" height="38.4" fill="var(--up)"/>
<line x1="631.1" y1="126.8" x2="631.1" y2="170.5" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="157.8" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="635.0" y1="135.3" x2="635.0" y2="212.1" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="138.8" width="2.45" height="61.7" fill="var(--up)"/>
<line x1="639.0" y1="86.1" x2="639.0" y2="134.9" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="104.5" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="642.9" y1="128.2" x2="642.9" y2="162.1" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="139.9" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="646.9" y1="114.7" x2="646.9" y2="143.0" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="119.3" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="650.9" y1="84.5" x2="650.9" y2="112.7" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="93.6" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="654.8" y1="75.1" x2="654.8" y2="115.3" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="75.1" width="2.45" height="33.7" fill="var(--down)"/>
<line x1="658.8" y1="105.0" x2="658.8" y2="178.6" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="128.7" width="2.45" height="26.1" fill="var(--down)"/>
<line x1="662.7" y1="154.8" x2="662.7" y2="207.1" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="172.5" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="666.7" y1="140.7" x2="666.7" y2="184.8" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="150.3" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="670.6" y1="149.9" x2="670.6" y2="172.1" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="153.5" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="674.6" y1="121.7" x2="674.6" y2="160.9" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="150.5" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="678.5" y1="189.0" x2="678.5" y2="264.8" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="194.6" width="2.45" height="66.1" fill="var(--up)"/>
<line x1="682.5" y1="169.4" x2="682.5" y2="254.9" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="183.8" width="2.45" height="54.7" fill="var(--down)"/>
<line x1="686.4" y1="229.2" x2="686.4" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="239.6" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="690.4" y1="209.8" x2="690.4" y2="271.5" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="224.6" width="2.45" height="33.3" fill="var(--down)"/>
<line x1="694.3" y1="262.6" x2="694.3" y2="285.0" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="262.7" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="698.3" y1="260.0" x2="698.3" y2="283.6" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="273.8" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="702.2" y1="239.7" x2="702.2" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="252.6" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="706.2" y1="288.7" x2="706.2" y2="328.5" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="295.9" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="710.1" y1="280.0" x2="710.1" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="301.0" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="714.1" y1="272.8" x2="714.1" y2="303.5" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="275.7" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="718.0" y1="263.9" x2="718.0" y2="285.8" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="270.0" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="722.0" y1="263.3" x2="722.0" y2="288.5" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="273.7" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="725.9" y1="278.5" x2="725.9" y2="296.7" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="278.9" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="729.9" y1="259.0" x2="729.9" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="268.2" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="733.8" y1="235.6" x2="733.8" y2="260.2" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="242.2" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="737.8" y1="202.0" x2="737.8" y2="227.1" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="208.5" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="741.8" y1="193.5" x2="741.8" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="195.8" width="2.45" height="26.9" fill="var(--up)"/>
<line x1="745.7" y1="195.7" x2="745.7" y2="245.6" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="199.4" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="749.7" y1="196.3" x2="749.7" y2="214.9" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="205.6" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="753.6" y1="201.4" x2="753.6" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="212.1" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="757.6" y1="234.6" x2="757.6" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="258.8" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="761.5" y1="311.4" x2="761.5" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="326.9" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="765.5" y1="326.7" x2="765.5" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="339.8" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="769.4" y1="340.3" x2="769.4" y2="356.4" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="354.1" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="773.4" y1="327.6" x2="773.4" y2="351.5" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="338.4" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="777.3" y1="335.2" x2="777.3" y2="364.9" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="338.7" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="781.3" y1="348.2" x2="781.3" y2="365.4" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="353.4" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="785.2" y1="320.5" x2="785.2" y2="353.5" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="339.8" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="789.2" y1="317.8" x2="789.2" y2="354.3" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="322.4" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="793.1" y1="319.2" x2="793.1" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="322.0" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="797.1" y1="303.9" x2="797.1" y2="346.8" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="327.0" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="801.0" y1="327.0" x2="801.0" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="330.5" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="805.0" y1="353.1" x2="805.0" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="354.5" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="808.9" y1="367.8" x2="808.9" y2="388.1" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="377.1" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="812.9" y1="387.2" x2="812.9" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="400.5" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="816.8" y1="385.1" x2="816.8" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="395.9" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="820.8" y1="410.7" x2="820.8" y2="433.7" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="412.3" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="824.7" y1="391.8" x2="824.7" y2="418.9" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="414.8" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="828.7" y1="359.8" x2="828.7" y2="412.8" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="377.0" width="2.45" height="35.8" fill="var(--up)"/>
<line x1="832.7" y1="351.3" x2="832.7" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="369.0" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="836.6" y1="351.8" x2="836.6" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="353.5" width="2.45" height="28.7" fill="var(--up)"/>
<line x1="840.6" y1="353.3" x2="840.6" y2="375.7" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="353.3" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="844.5" y1="356.9" x2="844.5" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="360.2" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="848.5" y1="360.1" x2="848.5" y2="389.5" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="361.2" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="852.4" y1="330.7" x2="852.4" y2="366.8" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="350.0" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="856.4" y1="331.0" x2="856.4" y2="361.9" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="345.8" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="860.3" y1="339.9" x2="860.3" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="352.5" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="864.3" y1="375.2" x2="864.3" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="380.6" width="2.45" height="24.3" fill="var(--up)"/>
<line x1="868.2" y1="378.7" x2="868.2" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="393.3" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="872.2" y1="396.4" x2="872.2" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="398.4" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="876.1" y1="407.3" x2="876.1" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="414.2" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="880.1" y1="395.0" x2="880.1" y2="427.8" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="401.0" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="884.0" y1="377.5" x2="884.0" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="385.3" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="888.0" y1="391.3" x2="888.0" y2="410.1" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="397.7" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="891.9" y1="372.9" x2="891.9" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="381.2" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="895.9" y1="348.8" x2="895.9" y2="390.3" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="350.8" width="2.45" height="37.4" fill="var(--up)"/>
<line x1="899.8" y1="336.3" x2="899.8" y2="352.7" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="340.0" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="903.8" y1="335.5" x2="903.8" y2="365.1" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="340.0" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="907.7" y1="339.7" x2="907.7" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="340.2" width="2.45" height="26.0" fill="var(--up)"/>
<line x1="911.7" y1="311.6" x2="911.7" y2="353.2" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="322.2" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="915.6" y1="322.1" x2="915.6" y2="342.4" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="330.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="919.6" y1="277.2" x2="919.6" y2="318.9" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="288.7" width="2.45" height="27.9" fill="var(--up)"/>
<line x1="923.6" y1="259.6" x2="923.6" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="261.0" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="927.5" y1="244.8" x2="927.5" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="259.4" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="931.5" y1="242.4" x2="931.5" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="251.4" width="2.45" height="20.3" fill="var(--down)"/>
<line x1="935.4" y1="239.5" x2="935.4" y2="260.7" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="250.1" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="939.4" y1="231.2" x2="939.4" y2="261.9" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="242.0" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="943.3" y1="247.9" x2="943.3" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="253.9" width="2.45" height="30.8" fill="var(--down)"/>
<line x1="947.3" y1="262.7" x2="947.3" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="270.0" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="951.2" y1="247.9" x2="951.2" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="252.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="955.2" y1="231.7" x2="955.2" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="242.4" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="959.1" y1="232.4" x2="959.1" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="246.3" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="963.1" y1="229.4" x2="963.1" y2="260.2" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="231.0" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="967.0" y1="202.0" x2="967.0" y2="225.5" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="208.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="971.0" y1="186.8" x2="971.0" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="212.3" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="974.9" y1="242.6" x2="974.9" y2="289.1" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="246.8" width="2.45" height="37.8" fill="var(--down)"/>
<line x1="978.9" y1="287.6" x2="978.9" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="290.9" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="982.8" y1="259.7" x2="982.8" y2="281.0" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="271.9" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="986.8" y1="270.5" x2="986.8" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="274.4" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="990.7" y1="241.6" x2="990.7" y2="292.3" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="248.8" width="2.45" height="29.7" fill="var(--up)"/>
<line x1="994.7" y1="261.6" x2="994.7" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="267.2" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="998.6" y1="267.2" x2="998.6" y2="308.4" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="278.0" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="1002.6" y1="269.8" x2="1002.6" y2="293.4" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="269.8" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="1006.5" y1="226.4" x2="1006.5" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="230.2" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="1010.5" y1="239.5" x2="1010.5" y2="284.4" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="245.0" width="2.45" height="38.4" fill="var(--down)"/>
<line x1="1014.5" y1="235.0" x2="1014.5" y2="276.9" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="239.0" width="2.45" height="37.9" fill="var(--up)"/>
<line x1="1018.4" y1="222.4" x2="1018.4" y2="241.4" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="238.0" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="1022.4" y1="214.6" x2="1022.4" y2="256.0" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="227.7" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="1026.3" y1="218.0" x2="1026.3" y2="242.1" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="235.2" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="1030.3" y1="207.1" x2="1030.3" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="211.2" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="1034.2" y1="202.9" x2="1034.2" y2="243.3" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="202.9" width="2.45" height="30.2" fill="var(--down)"/>
<line x1="1038.2" y1="196.7" x2="1038.2" y2="218.1" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="201.3" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="1042.1" y1="193.3" x2="1042.1" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="198.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1046.1" y1="169.5" x2="1046.1" y2="191.2" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="176.2" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="1050.0" y1="164.2" x2="1050.0" y2="188.8" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="172.5" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="60" y1="78.4" x2="1052" y2="78.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="81.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$300 R1</text>
<text x="1058" y="93.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="311.8" x2="1052" y2="311.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="305.8" font-size="11.5" fill="var(--support)" font-weight="600">$250 S1</text>
<text x="1058" y="317.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="387.1" x2="1052" y2="387.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="381.1" font-size="11.5" fill="var(--support)" font-weight="600">$234 S2</text>
<text x="1058" y="393.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="426.6" x2="1052" y2="426.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="420.6" font-size="11.5" fill="var(--support)" font-weight="600">$225 S3</text>
<text x="1058" y="432.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="183.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="175.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $278 (2026-08-21)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $300 | 2 | 2026-03-19·2026-03-30 — 카타르 라스라판 피격 직후 급등이 멈춘 자리. 1년 최고가($300.89, 2026-03-30)와 겹친다 |
| **현재가** | **$277.51** (2026-08-21 종가) | — | R1과 S1 사이 |
| S1 | $250 | 3 | 2026-04-17·2026-07-15·2026-07-28 — 3월 급등 이후 네 달에 걸쳐 세 번 되돌려진 자리로, 현재가에 가장 근접한 지지 |
| S2 | $234 | 2 | 2025-09-05·2026-05-07 — 사건 이전 거래대와 사건 이후 조정 저점이 우연히 겹친 구간 |
| S3 | $225 | 3 | 2025-09-19·2026-05-29·2026-06-18 — 사건 이전 레짐의 상단대이자 5월 이후 조정의 하단 |
| 참고선 | $186.20 | — | 1년 최저(2025-12-15 주간, 종가 기준 $186.20). 3월 이후 레짐과 단절돼 있어 근시일 지지로 보지 않는다 |

> 유효 클러스터가 저항 쪽에 1개(R1)뿐인 것은 현재가가 1년 고점대에 가깝기 때문이다 — 위쪽에 스윙 고점이 쌓일 시간이 없었다. 억지로 채우지 않고 1개만 뒀다.

---

## 3. 관측된 특이 구간 — 2026-03-18~19 카타르 라스라판 LNG 설비 피격

- 2026년 3월 18~19일 이란 미사일 공격으로 카타르 라스라판 LNG 단지의 트레인 두 기가 손상돼 세계 LNG 공급의 약 20%가 불가항력으로 이탈했다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 **3월 17일 $251.50 → 18일 $266.22(+5.85%) → 19일 $281.87(+5.88%)**로 이틀간 **+12.1%** 올랐다. 거래량은 평소(일 219만 주 내외) 대비 18일 509만 주(2.3배), **19일 1,219만 주(5.6배)**로 이 기간 최대였다.
- **이 급등은 회사 고유 이벤트가 아니다.** 같은 이틀간 유럽 TTF 가스 선물이 $51.56 → $61.85(+20%)로 뛰었고 Venture Global +14.5%, NextDecade +21.7%가 함께 올랐지만 S&P 500은 오히려 하락했다. 헨리허브(미국 가스)는 $3.03 → $3.17로 거의 움직이지 않았다 — **미국 가스가 아니라 국제 LNG 수급이 이 주식을 움직였다**는 것이 이 구간의 요점이다.
- 이 사건 이후 거래 레짐이 한 단계 올라섰다. 사건 이전 6개월은 $186~$252 구간이었으나 이후 5개월은 $240~$301 구간에서 거래되고 있다. 그래서 사건 이전 저점대인 1년 최저($186.20)는 지지 클러스터가 아니라 **참고선**으로만 처리했다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-22~2026-08-21. 수집 시점: 2026-08-24. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(2회 미만인데도 넣은 참고선은 2. 지지선 / 저항선 요약 비고에 사유를 적었다).
- **생성**: `scripts/gen_technical_chart.py` (`LNG --name "Cheniere Energy" --close-on 2026-08-21`). 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **3. 관측된 특이 구간의 3월 급등으로 가격대가 구조적으로 재설정됐다.** 사건 전후를 하나의 표본으로 묶어 계산했으므로, 사건 이전 구간에서 나온 S2·S3는 현재 레짐에서의 유효성이 사건 이후 형성된 S1보다 낮다고 보아야 한다.
    - 기간 내 주식분할·대규모 유상증자는 없었다. 다만 **분기배당 4회가 지급됐고 이 차트는 원주가라 배당을 반영하지 않는다** — 배당수익률이 0.8% 수준이라 영향은 작지만, 수정주가 기반 차트와는 미세하게 다르다.

---

*작성일: 2026-08-24*
