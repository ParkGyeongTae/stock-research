# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-01 종가 **$372.67**은 [핵심 지표](./04_metrics.md) A.2의 "현재" 주가 및 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다. 세 문서 모두 배당·분할 미반영 원주가 기준이다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-02 ~ 2026-09-01)

<div class="v-chart">
<style>
.v-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.v-chart svg { width:100%; height:auto; display:block; }
.v-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.v-chart .title { fill: var(--ink); font-weight:600; }
.v-chart .grid { stroke: var(--grid); stroke-width:1; }
.v-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visa(V) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Visa (V) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-02 ~ 2026-09-01 · 마지막 종가 $372.67 (2026-09-01) · 단위 USD</text>
<line x1="60" y1="569.0" x2="1052" y2="569.0" class="grid"/>
<text x="52" y="573.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="455.0" x2="1052" y2="455.0" class="grid"/>
<text x="52" y="459.0" font-size="11" text-anchor="end" fill="var(--muted)">320</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">340</text>
<line x1="60" y1="227.0" x2="1052" y2="227.0" class="grid"/>
<text x="52" y="231.0" font-size="11" text-anchor="end" fill="var(--muted)">360</text>
<line x1="60" y1="113.0" x2="1052" y2="113.0" class="grid"/>
<text x="52" y="117.0" font-size="11" text-anchor="end" fill="var(--muted)">380</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="145.0" y1="626.0" x2="145.0" y2="631.0" class="axis"/>
<text x="145.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="235.9" y1="626.0" x2="235.9" y2="631.0" class="axis"/>
<text x="235.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="311.0" y1="626.0" x2="311.0" y2="631.0" class="axis"/>
<text x="311.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="397.9" y1="626.0" x2="397.9" y2="631.0" class="axis"/>
<text x="397.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="477.0" y1="626.0" x2="477.0" y2="631.0" class="axis"/>
<text x="477.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="552.0" y1="626.0" x2="552.0" y2="631.0" class="axis"/>
<text x="552.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="639.0" y1="626.0" x2="639.0" y2="631.0" class="axis"/>
<text x="639.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="722.0" y1="626.0" x2="722.0" y2="631.0" class="axis"/>
<text x="722.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="801.0" y1="626.0" x2="801.0" y2="631.0" class="axis"/>
<text x="801.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="884.0" y1="626.0" x2="884.0" y2="631.0" class="axis"/>
<text x="884.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="971.0" y1="626.0" x2="971.0" y2="631.0" class="axis"/>
<text x="971.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1050.0" y1="626.0" x2="1050.0" y2="631.0" class="axis"/>
<text x="1050.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="283.0" x2="62.0" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="283.6" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="65.9" y1="278.9" x2="65.9" y2="299.6" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="279.0" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="69.9" y1="269.0" x2="69.9" y2="288.8" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="278.4" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="73.8" y1="269.1" x2="73.8" y2="339.9" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="276.1" width="2.45" height="46.5" fill="var(--down)"/>
<line x1="77.8" y1="316.0" x2="77.8" y2="335.3" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="327.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="81.7" y1="305.0" x2="81.7" y2="333.6" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="318.3" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="85.7" y1="326.1" x2="85.7" y2="361.3" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="326.1" width="2.45" height="25.6" fill="var(--down)"/>
<line x1="89.6" y1="320.9" x2="89.6" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="321.1" width="2.45" height="27.1" fill="var(--up)"/>
<line x1="93.6" y1="322.8" x2="93.6" y2="345.7" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="334.0" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="97.5" y1="325.6" x2="97.5" y2="350.2" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="337.5" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="101.5" y1="337.9" x2="101.5" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="340.8" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="105.5" y1="305.7" x2="105.5" y2="343.7" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="305.7" width="2.45" height="35.7" fill="var(--up)"/>
<line x1="109.4" y1="311.0" x2="109.4" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="314.0" width="2.45" height="37.3" fill="var(--down)"/>
<line x1="113.4" y1="325.7" x2="113.4" y2="351.0" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="331.8" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="117.3" y1="313.3" x2="117.3" y2="348.6" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="316.1" width="2.45" height="30.5" fill="var(--up)"/>
<line x1="121.3" y1="311.0" x2="121.3" y2="354.5" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="314.8" width="2.45" height="33.6" fill="var(--down)"/>
<line x1="125.2" y1="341.6" x2="125.2" y2="352.9" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="346.0" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="129.2" y1="339.9" x2="129.2" y2="372.3" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="350.4" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="133.1" y1="343.8" x2="133.1" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="356.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="137.1" y1="337.4" x2="137.1" y2="366.4" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="340.1" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="141.0" y1="309.0" x2="141.0" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="333.1" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="145.0" y1="287.6" x2="145.0" y2="339.2" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="296.4" width="2.45" height="42.9" fill="var(--up)"/>
<line x1="148.9" y1="300.1" x2="148.9" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="305.5" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="152.9" y1="266.0" x2="152.9" y2="306.8" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="284.9" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="156.8" y1="277.6" x2="156.8" y2="316.2" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="283.9" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="160.8" y1="258.7" x2="160.8" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="270.2" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="164.7" y1="255.5" x2="164.7" y2="277.7" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="262.5" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="168.7" y1="267.6" x2="168.7" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="275.6" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="172.6" y1="281.7" x2="172.6" y2="322.5" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="297.5" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="176.6" y1="297.3" x2="176.6" y2="336.8" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="319.8" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="180.5" y1="283.9" x2="180.5" y2="339.7" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="293.2" width="2.45" height="42.1" fill="var(--up)"/>
<line x1="184.5" y1="283.5" x2="184.5" y2="318.2" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="293.2" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="188.4" y1="308.6" x2="188.4" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="312.5" width="2.45" height="54.7" fill="var(--down)"/>
<line x1="192.4" y1="321.3" x2="192.4" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="330.2" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="196.4" y1="312.7" x2="196.4" y2="347.0" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="315.9" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="200.3" y1="286.0" x2="200.3" y2="323.9" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="299.9" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="204.3" y1="294.4" x2="204.3" y2="315.3" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="296.4" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="208.2" y1="300.2" x2="208.2" y2="315.6" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="305.7" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="212.2" y1="289.2" x2="212.2" y2="310.7" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="294.3" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="216.1" y1="286.7" x2="216.1" y2="312.4" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="289.7" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="220.1" y1="284.6" x2="220.1" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="292.1" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="224.0" y1="278.4" x2="224.0" y2="346.7" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="306.8" width="2.45" height="26.9" fill="var(--down)"/>
<line x1="228.0" y1="285.6" x2="228.0" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="312.3" width="2.45" height="16.0" fill="var(--up)"/>
<line x1="231.9" y1="323.9" x2="231.9" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="329.1" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="235.9" y1="334.1" x2="235.9" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="335.3" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="239.8" y1="339.2" x2="239.8" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="339.3" width="2.45" height="21.8" fill="var(--up)"/>
<line x1="243.8" y1="329.0" x2="243.8" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="340.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="247.7" y1="348.7" x2="247.7" y2="376.9" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="349.0" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="251.7" y1="350.7" x2="251.7" y2="370.4" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="359.6" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="255.6" y1="348.5" x2="255.6" y2="373.4" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="360.1" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="259.6" y1="346.2" x2="259.6" y2="379.8" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="347.2" width="2.45" height="19.5" fill="var(--up)"/>
<line x1="263.5" y1="316.7" x2="263.5" y2="355.8" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="347.4" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="267.5" y1="332.7" x2="267.5" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="346.5" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="271.4" y1="363.3" x2="271.4" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="364.4" width="2.45" height="33.5" fill="var(--down)"/>
<line x1="275.4" y1="378.8" x2="275.4" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="391.4" width="2.45" height="30.8" fill="var(--down)"/>
<line x1="279.3" y1="426.5" x2="279.3" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="429.4" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="283.3" y1="429.0" x2="283.3" y2="455.7" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="431.5" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="287.3" y1="407.1" x2="287.3" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="431.5" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="291.2" y1="391.8" x2="291.2" y2="430.5" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="409.5" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="295.2" y1="393.8" x2="295.2" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="402.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="299.1" y1="363.5" x2="299.1" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="372.2" width="2.45" height="32.1" fill="var(--up)"/>
<line x1="303.1" y1="365.5" x2="303.1" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="372.2" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="307.0" y1="369.4" x2="307.0" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="372.7" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="311.0" y1="379.2" x2="311.0" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="381.2" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="314.9" y1="382.0" x2="314.9" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="389.7" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="318.9" y1="384.6" x2="318.9" y2="401.7" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="400.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="322.8" y1="384.4" x2="322.8" y2="430.6" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="390.7" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="326.8" y1="374.6" x2="326.8" y2="418.5" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="390.9" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="330.7" y1="390.4" x2="330.7" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="398.7" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="334.7" y1="408.1" x2="334.7" y2="426.1" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="417.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="338.6" y1="405.1" x2="338.6" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="417.2" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="342.6" y1="299.3" x2="342.6" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="308.9" width="2.45" height="74.3" fill="var(--up)"/>
<line x1="346.5" y1="284.9" x2="346.5" y2="307.0" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="295.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="350.5" y1="292.8" x2="350.5" y2="319.2" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="296.4" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="354.4" y1="297.6" x2="354.4" y2="319.8" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="306.8" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="358.4" y1="296.6" x2="358.4" y2="320.0" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="309.4" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="362.3" y1="298.1" x2="362.3" y2="316.7" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="306.7" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="366.3" y1="284.5" x2="366.3" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="288.3" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="370.2" y1="264.4" x2="370.2" y2="286.3" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="272.1" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="374.2" y1="247.6" x2="374.2" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="264.7" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="378.2" y1="249.9" x2="378.2" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="254.7" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="382.1" y1="245.6" x2="382.1" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="254.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="386.1" y1="246.7" x2="386.1" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="252.7" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="390.0" y1="256.2" x2="390.0" y2="268.8" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="261.2" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="394.0" y1="254.4" x2="394.0" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="263.2" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="397.9" y1="283.7" x2="397.9" y2="321.2" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="284.7" width="2.45" height="19.3" fill="var(--down)"/>
<line x1="401.9" y1="241.0" x2="401.9" y2="317.9" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="262.3" width="2.45" height="53.0" fill="var(--up)"/>
<line x1="405.8" y1="234.9" x2="405.8" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="240.9" width="2.45" height="22.1" fill="var(--up)"/>
<line x1="409.8" y1="236.8" x2="409.8" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="243.2" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="413.7" y1="247.8" x2="413.7" y2="286.8" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="255.5" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="417.7" y1="257.2" x2="417.7" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="271.7" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="421.6" y1="303.9" x2="421.6" y2="356.3" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="322.8" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="425.6" y1="355.1" x2="425.6" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="358.1" width="2.45" height="52.0" fill="var(--down)"/>
<line x1="429.5" y1="398.6" x2="429.5" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="402.7" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="433.5" y1="388.4" x2="433.5" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="401.8" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="437.4" y1="402.3" x2="437.4" y2="424.2" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="407.7" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="441.4" y1="407.6" x2="441.4" y2="446.1" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="421.8" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="445.3" y1="405.6" x2="445.3" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="418.3" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="449.3" y1="407.2" x2="449.3" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="418.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="453.2" y1="410.5" x2="453.2" y2="428.7" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="419.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="457.2" y1="386.6" x2="457.2" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="406.6" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="461.1" y1="404.1" x2="461.1" y2="427.0" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="406.7" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="465.1" y1="407.2" x2="465.1" y2="427.2" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="415.2" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="469.1" y1="378.8" x2="469.1" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="387.7" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="473.0" y1="380.9" x2="473.0" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="385.3" width="2.45" height="59.2" fill="var(--down)"/>
<line x1="477.0" y1="371.3" x2="477.0" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="376.1" width="2.45" height="51.4" fill="var(--up)"/>
<line x1="480.9" y1="365.0" x2="480.9" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="388.6" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="484.9" y1="390.5" x2="484.9" y2="429.8" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="398.3" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="488.8" y1="354.7" x2="488.8" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="380.9" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="492.8" y1="368.8" x2="492.8" y2="414.5" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="387.9" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="496.7" y1="381.9" x2="496.7" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="393.7" width="2.45" height="29.5" fill="var(--down)"/>
<line x1="500.7" y1="398.7" x2="500.7" y2="429.1" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="408.4" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="504.6" y1="392.1" x2="504.6" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="402.3" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="508.6" y1="385.2" x2="508.6" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="404.3" width="2.45" height="26.8" fill="var(--down)"/>
<line x1="512.5" y1="418.1" x2="512.5" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="433.2" width="2.45" height="55.6" fill="var(--down)"/>
<line x1="516.5" y1="447.1" x2="516.5" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="457.9" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="520.4" y1="442.0" x2="520.4" y2="473.7" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="453.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="524.4" y1="453.9" x2="524.4" y2="479.3" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="461.1" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="528.3" y1="441.6" x2="528.3" y2="467.4" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="449.6" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="532.3" y1="452.0" x2="532.3" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="460.5" width="2.45" height="71.4" fill="var(--down)"/>
<line x1="536.2" y1="516.2" x2="536.2" y2="551.4" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="527.8" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="540.2" y1="489.5" x2="540.2" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="495.0" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="544.1" y1="458.3" x2="544.1" y2="489.5" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="473.8" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="548.1" y1="453.7" x2="548.1" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="454.2" width="2.45" height="32.4" fill="var(--up)"/>
<line x1="552.0" y1="440.2" x2="552.0" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="452.1" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="556.0" y1="443.4" x2="556.0" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="450.3" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="560.0" y1="422.1" x2="560.0" y2="456.1" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="446.8" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="563.9" y1="439.0" x2="563.9" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="456.1" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="567.9" y1="468.2" x2="567.9" y2="498.9" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="470.0" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="571.8" y1="475.5" x2="571.8" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="478.0" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="575.8" y1="471.4" x2="575.8" y2="503.7" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="481.0" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="579.7" y1="483.0" x2="579.7" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="493.5" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="583.7" y1="506.6" x2="583.7" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="522.6" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="587.6" y1="510.0" x2="587.6" y2="532.4" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="525.7" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="591.6" y1="505.6" x2="591.6" y2="526.9" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="511.4" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="595.5" y1="496.7" x2="595.5" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="504.5" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="599.5" y1="523.7" x2="599.5" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="526.8" width="2.45" height="47.8" fill="var(--down)"/>
<line x1="603.4" y1="554.9" x2="603.4" y2="585.9" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="570.7" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="607.4" y1="552.4" x2="607.4" y2="574.6" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="559.8" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="611.3" y1="524.3" x2="611.3" y2="552.8" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="539.4" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="615.3" y1="534.6" x2="615.3" y2="565.5" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="547.6" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="619.2" y1="520.6" x2="619.2" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="537.8" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="623.2" y1="524.1" x2="623.2" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="537.5" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="627.1" y1="542.8" x2="627.1" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="544.4" width="2.45" height="50.2" fill="var(--down)"/>
<line x1="631.1" y1="565.1" x2="631.1" y2="592.4" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="571.6" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="635.0" y1="550.0" x2="635.0" y2="588.4" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="556.2" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="639.0" y1="540.2" x2="639.0" y2="603.8" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="540.2" width="2.45" height="37.3" fill="var(--down)"/>
<line x1="642.9" y1="554.9" x2="642.9" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="564.4" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="646.9" y1="543.8" x2="646.9" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="550.0" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="650.9" y1="540.6" x2="650.9" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="554.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="654.8" y1="505.8" x2="654.8" y2="525.1" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="517.9" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="658.8" y1="514.4" x2="658.8" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="521.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="662.7" y1="517.7" x2="662.7" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="519.4" width="2.45" height="24.8" fill="var(--down)"/>
<line x1="666.7" y1="513.4" x2="666.7" y2="555.7" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="515.5" width="2.45" height="31.1" fill="var(--up)"/>
<line x1="670.6" y1="499.9" x2="670.6" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="504.2" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="674.6" y1="473.6" x2="674.6" y2="503.3" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="478.3" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="678.5" y1="466.4" x2="678.5" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="475.8" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="682.5" y1="458.2" x2="682.5" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="472.0" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="686.4" y1="469.0" x2="686.4" y2="498.6" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="475.5" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="690.4" y1="472.7" x2="690.4" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="489.1" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="694.3" y1="504.2" x2="694.3" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="504.6" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="698.3" y1="499.5" x2="698.3" y2="540.4" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="509.1" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="702.2" y1="512.1" x2="702.2" y2="543.4" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="515.3" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="706.2" y1="507.3" x2="706.2" y2="534.5" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="514.0" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="710.1" y1="489.4" x2="710.1" y2="519.2" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="499.5" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="714.1" y1="329.7" x2="714.1" y2="376.4" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="361.5" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="718.0" y1="383.8" x2="718.0" y2="408.9" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="385.9" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="722.0" y1="364.7" x2="722.0" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="381.6" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="725.9" y1="399.2" x2="725.9" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="409.4" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="729.9" y1="423.2" x2="729.9" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="425.9" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="733.8" y1="428.9" x2="733.8" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="433.6" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="737.8" y1="434.0" x2="737.8" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="447.7" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="741.8" y1="448.9" x2="741.8" y2="476.9" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="449.4" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="745.7" y1="425.5" x2="745.7" y2="466.3" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="433.0" width="2.45" height="27.1" fill="var(--up)"/>
<line x1="749.7" y1="404.2" x2="749.7" y2="431.1" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="418.4" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="753.6" y1="424.1" x2="753.6" y2="456.1" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="433.4" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="757.6" y1="436.0" x2="757.6" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="440.6" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="761.5" y1="403.6" x2="761.5" y2="433.1" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="422.2" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="765.5" y1="378.4" x2="765.5" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="383.0" width="2.45" height="46.8" fill="var(--up)"/>
<line x1="769.4" y1="368.5" x2="769.4" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="379.0" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="773.4" y1="388.5" x2="773.4" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="393.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="777.3" y1="383.6" x2="777.3" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="391.6" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="781.3" y1="378.4" x2="781.3" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="395.0" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="785.2" y1="406.5" x2="785.2" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="418.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="789.2" y1="389.7" x2="789.2" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="411.6" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="793.1" y1="414.6" x2="793.1" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="420.7" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="797.1" y1="388.5" x2="797.1" y2="424.5" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="418.7" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="801.0" y1="410.2" x2="801.0" y2="462.5" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="413.6" width="2.45" height="25.6" fill="var(--down)"/>
<line x1="805.0" y1="435.0" x2="805.0" y2="492.7" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="440.7" width="2.45" height="29.6" fill="var(--down)"/>
<line x1="808.9" y1="468.4" x2="808.9" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="468.4" width="2.45" height="29.9" fill="var(--down)"/>
<line x1="812.9" y1="427.9" x2="812.9" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="454.0" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="816.8" y1="420.9" x2="816.8" y2="449.5" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="434.7" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="820.8" y1="432.7" x2="820.8" y2="463.9" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="447.3" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="824.7" y1="423.7" x2="824.7" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="426.2" width="2.45" height="36.4" fill="var(--up)"/>
<line x1="828.7" y1="415.7" x2="828.7" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="417.3" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="832.7" y1="433.9" x2="832.7" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="443.6" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="836.6" y1="421.2" x2="836.6" y2="456.1" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="441.4" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="840.6" y1="418.3" x2="840.6" y2="439.3" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="433.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="844.5" y1="379.2" x2="844.5" y2="430.0" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="380.2" width="2.45" height="42.4" fill="var(--up)"/>
<line x1="848.5" y1="359.1" x2="848.5" y2="398.2" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="378.0" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="852.4" y1="384.7" x2="852.4" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="392.3" width="2.45" height="21.4" fill="var(--down)"/>
<line x1="856.4" y1="380.9" x2="856.4" y2="421.6" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="407.5" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="860.3" y1="390.7" x2="860.3" y2="408.9" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="404.7" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="864.3" y1="370.6" x2="864.3" y2="413.8" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="385.3" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="868.2" y1="341.3" x2="868.2" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="383.4" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="872.2" y1="342.6" x2="872.2" y2="389.8" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="362.5" width="2.45" height="22.7" fill="var(--up)"/>
<line x1="876.1" y1="307.9" x2="876.1" y2="350.9" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="331.6" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="880.1" y1="316.5" x2="880.1" y2="346.2" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="323.4" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="884.0" y1="264.8" x2="884.0" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="277.8" width="2.45" height="37.2" fill="var(--up)"/>
<line x1="888.0" y1="214.9" x2="888.0" y2="269.7" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="214.9" width="2.45" height="54.8" fill="var(--up)"/>
<line x1="891.9" y1="198.4" x2="891.9" y2="290.6" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="209.9" width="2.45" height="32.8" fill="var(--down)"/>
<line x1="895.9" y1="249.3" x2="895.9" y2="301.6" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="271.5" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="899.8" y1="274.9" x2="899.8" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="282.3" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="903.8" y1="292.6" x2="903.8" y2="315.8" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="294.3" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="907.7" y1="277.3" x2="907.7" y2="310.6" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="280.4" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="911.7" y1="229.9" x2="911.7" y2="278.0" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="239.8" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="915.6" y1="227.3" x2="915.6" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="249.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="919.6" y1="224.5" x2="919.6" y2="289.0" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="254.7" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="923.6" y1="197.7" x2="923.6" y2="243.5" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="197.7" width="2.45" height="40.5" fill="var(--up)"/>
<line x1="927.5" y1="200.6" x2="927.5" y2="244.1" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="206.7" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="931.5" y1="209.9" x2="931.5" y2="247.3" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="223.8" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="935.4" y1="232.0" x2="935.4" y2="257.3" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="244.2" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="939.4" y1="241.1" x2="939.4" y2="271.1" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="246.6" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="943.3" y1="272.3" x2="943.3" y2="292.6" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="272.3" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="947.3" y1="250.7" x2="947.3" y2="278.0" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="251.3" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="951.2" y1="206.1" x2="951.2" y2="237.0" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="212.6" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="955.2" y1="163.4" x2="955.2" y2="211.4" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="189.4" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="959.1" y1="147.4" x2="959.1" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="177.2" width="2.45" height="66.9" fill="var(--up)"/>
<line x1="963.1" y1="187.1" x2="963.1" y2="222.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="191.3" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="967.0" y1="187.8" x2="967.0" y2="226.4" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="192.1" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="971.0" y1="158.8" x2="971.0" y2="202.2" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="178.6" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="974.9" y1="163.7" x2="974.9" y2="226.5" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="172.3" width="2.45" height="44.6" fill="var(--up)"/>
<line x1="978.9" y1="156.3" x2="978.9" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="156.9" width="2.45" height="21.4" fill="var(--down)"/>
<line x1="982.8" y1="163.7" x2="982.8" y2="197.1" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="167.3" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="986.8" y1="168.6" x2="986.8" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="178.5" width="2.45" height="34.3" fill="var(--down)"/>
<line x1="990.7" y1="203.2" x2="990.7" y2="233.4" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="215.6" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="994.7" y1="201.1" x2="994.7" y2="227.2" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="210.9" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="998.6" y1="207.9" x2="998.6" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="221.3" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="1002.6" y1="195.9" x2="1002.6" y2="234.4" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="195.9" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="1006.5" y1="188.2" x2="1006.5" y2="211.3" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="193.4" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="1010.5" y1="206.7" x2="1010.5" y2="235.4" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="210.8" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="1014.5" y1="193.3" x2="1014.5" y2="238.1" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="202.8" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="1018.4" y1="166.4" x2="1018.4" y2="210.5" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="195.4" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="1022.4" y1="176.1" x2="1022.4" y2="206.3" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="194.3" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="1026.3" y1="159.7" x2="1026.3" y2="189.0" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="164.1" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="1030.3" y1="93.4" x2="1030.3" y2="157.4" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="99.3" width="2.45" height="52.2" fill="var(--up)"/>
<line x1="1034.2" y1="89.1" x2="1034.2" y2="111.5" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="89.4" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="1038.2" y1="81.3" x2="1038.2" y2="106.8" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="89.4" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="1042.1" y1="102.9" x2="1042.1" y2="121.6" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="106.5" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="1046.1" y1="98.9" x2="1046.1" y2="119.8" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="105.3" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="1050.0" y1="108.7" x2="1050.0" y2="157.3" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="115.0" width="2.45" height="39.8" fill="var(--down)"/>
<line x1="60" y1="306.9" x2="1052" y2="306.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="300.9" font-size="11.5" fill="var(--support)" font-weight="600">$346 S1</text>
<text x="1058" y="312.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="374.9" x2="1052" y2="374.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="368.9" font-size="11.5" fill="var(--support)" font-weight="600">$334 S2</text>
<text x="1058" y="380.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="453.2" x2="1052" y2="453.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="447.2" font-size="11.5" fill="var(--support)" font-weight="600">$320 S3</text>
<text x="1058" y="459.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="154.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="146.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $373 (2026-09-01)</text>
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
| **현재가** | **$372.67** (2026-09-01 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $346 | 2 | 2026-01-02·2026-07-23 스윙 저점대. 2026-07-28 실적 발표 직전 눌림목이 이 대에서 잡혔다 |
| S2 | $334 | 3 | 2025-09-16·2025-09-25·2025-10-16 스윙 저점대. FY2025 실적 발표(2025-10-28) 이전 구간의 박스 하단이며, 2026-04-29 급등이 이 대를 위로 벗어난 자리(3. 관측된 특이 구간)와 겹친다 |
| S3 | $320 | 5 | 2025-11-18·2025-12-04·2026-01-20·2026-01-30·2026-05-08 스윙 저점대. 기간 내 터치가 가장 많은 밀집대 |
| 참고선 | $384 | — | 2026-08-25 종가 기준 52주 최고. 스윙 클러스터가 아니라 단일 고점이라 저항으로 잡히지 않았고, 현재가에서 3% 위에 있어 근시일 저항으로 보기에는 표본이 부족하다 |

> 기간 내 유효한 저항 클러스터가 하나도 잡히지 않았다 — 주가가 1년 내내 계단식으로 올라 스윙 고점들이 서로 다른 가격대에 흩어졌기 때문이며, 마지막 구간은 신고가라 위쪽에 참조점 자체가 없다. 참고선($384)은 생성 스크립트 출력이 아니라 사람이 덧붙인 행이다(4. 방법론 · 한계).

---

## 3. 관측된 특이 구간 — 2026-04-29 FY2026 Q2 실적 갭 상승

- 2026-04-28 장 마감 후 발표된 FY2026 Q2 실적(순매출 $11.23B **+17%**, GAAP EPS $3.14 **+36%**)에 대한 반응 → [최근 뉴스 / 이슈](./08_news.md) 로그의 실적 항목과 같은 계열의 이벤트다.
- 종가 기준 전일 대비 **+8.3%** ($309.30 → $334.86), 거래량은 평소(일 724만 주 내외) 대비 약 **2.3배**인 **1,666만 주**.
- 이 하루로 주가가 3월 말 저점권($295~$310)을 벗어나 상단 레짐으로 재설정됐다. 이후 4개월간 $334 아래로 종가가 내려온 적이 없어, S2($334)를 "갭 이전 박스 하단"이 아니라 "갭 이후 지지"로 읽는 근거가 된다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-02~2026-09-01. 수집 시점: 2026-09-02. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py V --name "Visa" --close-on 2026-09-01 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 2. 지지선 / 저항선 요약의 **참고선($384)은 스크립트 산출물이 아니라 사람이 추가한 행**이다 — 저항 클러스터가 하나도 잡히지 않아 위쪽 참조점을 남기기 위한 것이며, 터치 횟수 기준을 통과한 레벨이 아니다.
    - 3. 관측된 특이 구간의 2026-04-29 갭(+8.3%)으로 가격대가 한 번 재설정됐다 — 갭 이전 구간의 스윙 저점(S2·S3)은 그 이후 실제로 시험된 적이 없어, 터치 횟수가 많다고 해서 현재 유효한 지지라고 볼 수는 없다.
    - 표시 기간(2025-09-02~2026-09-01)에 주식분할·유상증자 등 가격 연속성을 깨는 이벤트는 없었다(마지막 분할은 2015-03). 배당은 기간 내 4회 지급됐으나 원주가라 반영되지 않았다.

---

*작성일: 2026-09-02*
