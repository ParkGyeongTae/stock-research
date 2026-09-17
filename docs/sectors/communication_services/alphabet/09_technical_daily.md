# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$338.50**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치한다**. 세 문서 모두 배당 미반영 원주가를 쓴다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-12 ~ 2026-09-11)

<style>
.googl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .googl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.googl-chart svg { width:100%; height:auto; display:block; }
.googl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.googl-chart .title { fill: var(--ink); font-weight:600; }
.googl-chart .grid { stroke: var(--grid); stroke-width:1; }
.googl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="googl-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Alphabet(GOOGL) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Alphabet (GOOGL) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-12 ~ 2026-09-11 · 마지막 종가 $338.50 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="564.4" x2="1052" y2="564.4" class="grid"/>
<text x="52" y="568.4" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="487.4" x2="1052" y2="487.4" class="grid"/>
<text x="52" y="491.4" font-size="11" text-anchor="end" fill="var(--muted)">275</text>
<line x1="60" y1="410.3" x2="1052" y2="410.3" class="grid"/>
<text x="52" y="414.3" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="333.3" x2="1052" y2="333.3" class="grid"/>
<text x="52" y="337.3" font-size="11" text-anchor="end" fill="var(--muted)">325</text>
<line x1="60" y1="256.3" x2="1052" y2="256.3" class="grid"/>
<text x="52" y="260.3" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="179.2" x2="1052" y2="179.2" class="grid"/>
<text x="52" y="183.2" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="102.2" x2="1052" y2="102.2" class="grid"/>
<text x="52" y="106.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="62.0" y1="588.8" x2="62.0" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="592.7" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="65.9" y1="557.0" x2="65.9" y2="580.8" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="559.4" width="2.45" height="21.4" fill="var(--up)"/>
<line x1="69.9" y1="555.0" x2="69.9" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="558.0" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="73.8" y1="559.4" x2="73.8" y2="575.8" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="560.6" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="77.8" y1="552.1" x2="77.8" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="558.1" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="81.7" y1="545.9" x2="81.7" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="549.8" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="85.7" y1="546.6" x2="85.7" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="550.7" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="89.6" y1="550.9" x2="89.6" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="555.0" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="93.6" y1="557.1" x2="93.6" y2="575.3" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="559.3" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="97.5" y1="575.2" x2="97.5" y2="592.9" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="577.3" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="101.5" y1="566.2" x2="101.5" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="573.4" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="105.5" y1="560.8" x2="105.5" y2="586.7" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="571.0" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="109.4" y1="585.1" x2="109.4" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="585.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="113.4" y1="575.8" x2="113.4" y2="599.5" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="580.1" width="2.45" height="12.8" fill="var(--up)"/>
<line x1="117.3" y1="574.2" x2="117.3" y2="588.1" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="577.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="121.3" y1="575.8" x2="121.3" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="578.7" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="125.2" y1="560.3" x2="125.2" y2="581.1" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="563.1" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="129.2" y1="563.0" x2="129.2" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="569.7" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="133.1" y1="576.7" x2="133.1" y2="583.4" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="579.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="137.1" y1="580.5" x2="137.1" y2="597.8" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="581.4" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="141.0" y1="582.6" x2="141.0" y2="608.0" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="590.8" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="145.0" y1="581.3" x2="145.0" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="582.4" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="148.9" y1="573.3" x2="148.9" y2="593.6" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="578.4" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="152.9" y1="557.9" x2="152.9" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="561.2" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="156.8" y1="542.9" x2="156.8" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="558.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="160.8" y1="551.4" x2="160.8" y2="571.1" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="554.2" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="164.7" y1="541.8" x2="164.7" y2="551.3" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="544.2" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="168.7" y1="549.3" x2="168.7" y2="582.4" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="549.8" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="172.6" y1="544.8" x2="172.6" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="550.9" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="176.6" y1="548.8" x2="176.6" y2="558.7" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="554.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="180.5" y1="528.4" x2="180.5" y2="548.0" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="533.8" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="184.5" y1="502.3" x2="184.5" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="505.0" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="188.4" y1="500.5" x2="188.4" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="503.7" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="192.4" y1="486.3" x2="192.4" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="488.7" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="196.4" y1="436.2" x2="196.4" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="436.2" width="2.45" height="31.1" fill="var(--down)"/>
<line x1="200.3" y1="453.5" x2="200.3" y2="481.1" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="462.1" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="204.3" y1="454.9" x2="204.3" y2="472.6" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="460.5" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="208.2" y1="468.0" x2="208.2" y2="483.5" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="479.5" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="212.2" y1="452.2" x2="212.2" y2="480.1" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="458.7" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="216.1" y1="446.2" x2="216.1" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="455.5" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="220.1" y1="460.3" x2="220.1" y2="486.8" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="462.1" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="224.0" y1="438.7" x2="224.0" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="440.8" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="228.0" y1="435.2" x2="228.0" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="437.1" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="231.9" y1="434.9" x2="231.9" y2="460.6" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="436.0" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="235.9" y1="463.2" x2="235.9" y2="480.4" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="464.7" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="239.8" y1="476.4" x2="239.8" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="483.0" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="243.8" y1="429.0" x2="243.8" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="454.1" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="247.7" y1="444.8" x2="247.7" y2="477.5" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="447.5" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="251.7" y1="398.6" x2="251.7" y2="451.5" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="432.5" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="255.6" y1="390.5" x2="255.6" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="396.3" width="2.45" height="46.5" fill="var(--down)"/>
<line x1="259.6" y1="398.2" x2="259.6" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="411.4" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="263.5" y1="350.3" x2="263.5" y2="380.7" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="353.1" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="267.5" y1="321.5" x2="267.5" y2="355.9" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="329.6" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="271.4" y1="334.8" x2="271.4" y2="358.6" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="346.6" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="275.4" y1="327.6" x2="275.4" y2="358.6" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="338.3" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="279.3" y1="349.2" x2="279.3" y2="367.5" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="355.8" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="283.3" y1="353.7" x2="283.3" y2="367.5" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="358.7" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="287.3" y1="343.8" x2="287.3" y2="366.9" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="349.8" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="291.2" y1="341.4" x2="291.2" y2="365.0" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="341.8" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="295.2" y1="339.0" x2="295.2" y2="351.3" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="344.8" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="299.1" y1="347.3" x2="299.1" y2="375.8" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="348.5" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="303.1" y1="354.9" x2="303.1" y2="373.7" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="357.7" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="307.0" y1="344.7" x2="307.0" y2="365.1" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="348.1" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="311.0" y1="345.3" x2="311.0" y2="383.8" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="348.5" width="2.45" height="23.6" fill="var(--down)"/>
<line x1="314.9" y1="364.5" x2="314.9" y2="393.2" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="368.1" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="318.9" y1="375.1" x2="318.9" y2="395.3" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="375.4" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="322.8" y1="377.1" x2="322.8" y2="402.3" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="390.1" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="326.8" y1="385.4" x2="326.8" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="385.6" width="2.45" height="34.8" fill="var(--down)"/>
<line x1="330.7" y1="398.1" x2="330.7" y2="412.7" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="402.7" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="334.7" y1="388.0" x2="334.7" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="388.3" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="338.6" y1="379.1" x2="338.6" y2="394.0" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="379.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="342.6" y1="364.3" x2="342.6" y2="381.6" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="366.1" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="346.5" y1="363.9" x2="346.5" y2="373.6" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="364.8" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="350.5" y1="363.8" x2="350.5" y2="372.5" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="365.7" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="354.4" y1="367.1" x2="354.4" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="368.5" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="358.4" y1="358.1" x2="358.4" y2="371.9" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="367.7" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="362.3" y1="365.4" x2="362.3" y2="375.1" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="370.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="366.3" y1="341.0" x2="366.3" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="358.3" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="370.2" y1="351.7" x2="370.2" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="355.9" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="374.2" y1="345.8" x2="374.2" y2="374.0" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="359.8" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="378.2" y1="329.8" x2="378.2" y2="366.6" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="342.6" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="382.1" y1="316.9" x2="382.1" y2="344.1" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="321.1" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="386.1" y1="315.3" x2="386.1" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="322.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="390.0" y1="305.4" x2="390.0" y2="333.3" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="312.2" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="394.0" y1="285.6" x2="394.0" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="299.5" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="397.9" y1="297.8" x2="397.9" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="299.9" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="401.9" y1="294.2" x2="401.9" y2="315.6" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="294.3" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="405.8" y1="303.6" x2="405.8" y2="325.0" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="304.3" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="409.8" y1="324.9" x2="409.8" y2="347.4" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="342.5" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="413.7" y1="310.3" x2="413.7" y2="350.7" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="322.9" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="417.7" y1="302.0" x2="417.7" y2="321.7" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="304.2" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="421.6" y1="306.5" x2="421.6" y2="325.7" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="310.2" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="425.6" y1="299.9" x2="425.6" y2="327.1" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="307.8" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="429.5" y1="293.5" x2="429.5" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="301.3" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="433.5" y1="294.7" x2="433.5" y2="311.9" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="299.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="437.4" y1="280.0" x2="437.4" y2="328.6" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="286.2" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="441.4" y1="287.1" x2="441.4" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="287.1" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="445.3" y1="272.2" x2="445.3" y2="300.5" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="275.7" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="449.3" y1="259.4" x2="449.3" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="264.5" width="2.45" height="23.5" fill="var(--down)"/>
<line x1="453.2" y1="276.9" x2="453.2" y2="322.5" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="278.0" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="457.2" y1="309.6" x2="457.2" y2="390.4" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="314.0" width="2.45" height="58.6" fill="var(--up)"/>
<line x1="461.1" y1="316.7" x2="461.1" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="326.6" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="465.1" y1="325.0" x2="465.1" y2="357.1" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="335.4" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="469.1" y1="343.6" x2="469.1" y2="365.3" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="345.7" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="473.0" y1="345.4" x2="473.0" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="351.9" width="2.45" height="24.7" fill="var(--down)"/>
<line x1="477.0" y1="360.3" x2="477.0" y2="388.1" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="373.1" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="480.9" y1="383.7" x2="480.9" y2="398.9" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="386.5" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="484.9" y1="396.6" x2="484.9" y2="421.9" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="404.1" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="488.8" y1="393.7" x2="488.8" y2="406.5" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="400.1" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="492.8" y1="393.5" x2="492.8" y2="410.2" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="401.5" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="496.7" y1="359.5" x2="496.7" y2="398.3" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="364.2" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="500.7" y1="350.2" x2="500.7" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="351.6" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="504.6" y1="372.5" x2="504.6" y2="392.1" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="376.7" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="508.6" y1="368.3" x2="508.6" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="370.6" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="512.5" y1="369.8" x2="512.5" y2="403.1" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="371.4" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="516.5" y1="372.2" x2="516.5" y2="398.6" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="374.1" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="520.4" y1="384.2" x2="520.4" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="390.2" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="524.4" y1="398.2" x2="524.4" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="399.3" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="528.3" y1="393.5" x2="528.3" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="400.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="532.3" y1="400.2" x2="532.3" y2="416.5" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="401.0" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="536.2" y1="408.7" x2="536.2" y2="425.2" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="414.9" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="540.2" y1="389.4" x2="540.2" y2="428.6" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="390.7" width="2.45" height="37.0" fill="var(--up)"/>
<line x1="544.1" y1="381.0" x2="544.1" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="388.6" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="548.1" y1="375.1" x2="548.1" y2="392.1" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="383.5" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="552.0" y1="382.8" x2="552.0" y2="407.2" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="389.3" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="556.0" y1="386.6" x2="556.0" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="388.7" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="560.0" y1="390.3" x2="560.0" y2="401.0" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="393.2" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="563.9" y1="375.1" x2="563.9" y2="393.4" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="376.7" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="567.9" y1="371.9" x2="567.9" y2="389.0" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="381.8" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="571.8" y1="385.5" x2="571.8" y2="403.1" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="388.4" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="575.8" y1="391.8" x2="575.8" y2="415.7" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="393.5" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="579.7" y1="391.9" x2="579.7" y2="407.5" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="403.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="583.7" y1="410.6" x2="583.7" y2="440.1" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="412.8" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="587.6" y1="422.6" x2="587.6" y2="443.5" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="430.5" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="591.6" y1="447.5" x2="591.6" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="447.6" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="595.5" y1="473.9" x2="595.5" y2="490.6" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="480.3" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="599.5" y1="480.9" x2="599.5" y2="496.3" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="483.0" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="603.4" y1="447.1" x2="603.4" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="448.7" width="2.45" height="29.3" fill="var(--up)"/>
<line x1="607.4" y1="408.7" x2="607.4" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="418.4" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="611.3" y1="416.2" x2="611.3" y2="442.8" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="423.4" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="615.3" y1="408.4" x2="615.3" y2="425.2" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="410.4" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="619.2" y1="393.0" x2="619.2" y2="417.3" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="393.5" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="623.2" y1="342.3" x2="623.2" y2="364.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="347.3" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="627.1" y1="350.1" x2="627.1" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="353.4" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="631.1" y1="343.1" x2="631.1" y2="360.0" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="348.6" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="635.0" y1="343.7" x2="635.0" y2="362.7" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="344.7" width="2.45" height="12.8" fill="var(--up)"/>
<line x1="639.0" y1="307.8" x2="639.0" y2="337.1" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="308.9" width="2.45" height="25.0" fill="var(--up)"/>
<line x1="642.9" y1="294.8" x2="642.9" y2="315.1" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="296.0" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="646.9" y1="287.5" x2="646.9" y2="304.0" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="290.9" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="650.9" y1="279.9" x2="650.9" y2="298.7" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="281.9" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="654.8" y1="282.8" x2="654.8" y2="297.5" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="284.7" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="658.8" y1="289.1" x2="658.8" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="294.2" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="662.7" y1="287.6" x2="662.7" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="289.2" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="666.7" y1="281.0" x2="666.7" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="283.4" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="670.6" y1="270.8" x2="670.6" y2="301.3" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="273.5" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="674.6" y1="246.5" x2="674.6" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="255.2" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="678.5" y1="248.8" x2="678.5" y2="268.2" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="256.9" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="682.5" y1="238.4" x2="682.5" y2="274.1" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="256.5" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="686.4" y1="145.8" x2="686.4" y2="207.5" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="149.0" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="690.4" y1="143.0" x2="690.4" y2="166.8" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="146.3" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="694.3" y1="141.1" x2="694.3" y2="164.5" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="146.5" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="698.3" y1="124.3" x2="698.3" y2="151.5" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="137.9" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="702.2" y1="102.7" x2="702.2" y2="124.5" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="108.3" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="706.2" y1="101.9" x2="706.2" y2="124.8" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="102.5" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="710.1" y1="96.1" x2="710.1" y2="113.4" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="99.8" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="714.1" y1="110.1" x2="714.1" y2="137.7" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="121.8" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="718.0" y1="137.6" x2="718.0" y2="155.3" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="141.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="722.0" y1="90.8" x2="722.0" y2="148.4" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="94.1" width="2.45" height="52.4" fill="var(--up)"/>
<line x1="725.9" y1="93.2" x2="725.9" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="98.9" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="729.9" y1="103.6" x2="729.9" y2="123.2" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="112.1" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="733.8" y1="75.7" x2="733.8" y2="119.1" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="111.6" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="737.8" y1="111.0" x2="737.8" y2="145.0" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="111.6" width="2.45" height="28.7" fill="var(--down)"/>
<line x1="741.8" y1="121.1" x2="741.8" y2="154.9" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="136.4" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="745.7" y1="125.3" x2="745.7" y2="154.5" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="140.2" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="749.7" y1="136.9" x2="749.7" y2="158.4" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="141.2" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="753.6" y1="135.3" x2="753.6" y2="155.8" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="136.5" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="757.6" y1="121.1" x2="757.6" y2="145.7" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="136.6" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="761.5" y1="127.3" x2="761.5" y2="147.9" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="132.6" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="765.5" y1="147.7" x2="765.5" y2="168.6" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="147.7" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="769.4" y1="168.3" x2="769.4" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="174.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="773.4" y1="183.7" x2="773.4" y2="230.3" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="205.2" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="777.3" y1="205.6" x2="777.3" y2="231.4" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="219.2" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="781.3" y1="184.6" x2="781.3" y2="231.0" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="187.9" width="2.45" height="40.9" fill="var(--up)"/>
<line x1="785.2" y1="188.2" x2="785.2" y2="212.8" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="199.2" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="789.2" y1="206.4" x2="789.2" y2="223.8" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="209.5" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="793.1" y1="188.2" x2="793.1" y2="233.8" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="203.6" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="797.1" y1="199.1" x2="797.1" y2="240.2" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="215.6" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="801.0" y1="229.2" x2="801.0" y2="267.5" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="232.3" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="805.0" y1="205.2" x2="805.0" y2="241.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="217.4" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="808.9" y1="185.4" x2="808.9" y2="205.3" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="196.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="812.9" y1="176.2" x2="812.9" y2="203.7" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="184.6" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="816.8" y1="187.5" x2="816.8" y2="219.2" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="197.3" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="820.8" y1="196.3" x2="820.8" y2="229.6" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="200.7" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="824.7" y1="228.8" x2="824.7" y2="281.8" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="231.8" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="828.7" y1="258.5" x2="828.7" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="268.2" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="832.7" y1="245.5" x2="832.7" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="259.2" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="836.6" y1="269.9" x2="836.6" y2="299.9" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="275.7" width="2.45" height="21.5" fill="var(--up)"/>
<line x1="840.6" y1="267.5" x2="840.6" y2="317.3" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="279.2" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="844.5" y1="242.9" x2="844.5" y2="285.0" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="245.0" width="2.45" height="36.4" fill="var(--up)"/>
<line x1="848.5" y1="229.7" x2="848.5" y2="255.0" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="233.6" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="852.4" y1="216.3" x2="852.4" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="221.7" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="856.4" y1="212.5" x2="856.4" y2="245.7" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="225.7" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="860.3" y1="201.0" x2="860.3" y2="233.5" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="205.6" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="864.3" y1="184.9" x2="864.3" y2="208.5" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="197.5" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="868.2" y1="201.3" x2="868.2" y2="231.6" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="210.8" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="872.2" y1="226.5" x2="872.2" y2="252.9" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="228.9" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="876.1" y1="232.2" x2="876.1" y2="247.8" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="233.1" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="880.1" y1="231.2" x2="880.1" y2="250.9" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="237.2" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="884.0" y1="225.0" x2="884.0" y2="252.9" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="227.0" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="888.0" y1="183.4" x2="888.0" y2="232.4" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="191.8" width="2.45" height="39.9" fill="var(--up)"/>
<line x1="891.9" y1="178.4" x2="891.9" y2="249.2" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="185.2" width="2.45" height="57.3" fill="var(--down)"/>
<line x1="895.9" y1="260.8" x2="895.9" y2="282.9" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="266.2" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="899.8" y1="226.4" x2="899.8" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="250.1" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="903.8" y1="252.2" x2="903.8" y2="265.5" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="252.2" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="907.7" y1="256.5" x2="907.7" y2="281.8" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="261.9" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="911.7" y1="334.9" x2="911.7" y2="364.4" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="345.2" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="915.6" y1="335.8" x2="915.6" y2="357.0" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="349.5" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="919.6" y1="316.6" x2="919.6" y2="335.0" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="328.5" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="923.6" y1="299.8" x2="923.6" y2="335.0" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="306.5" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="927.5" y1="279.4" x2="927.5" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="297.2" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="931.5" y1="297.8" x2="931.5" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="305.0" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="935.4" y1="229.8" x2="935.4" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="237.4" width="2.45" height="47.1" fill="var(--up)"/>
<line x1="939.4" y1="174.0" x2="939.4" y2="215.1" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="183.8" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="943.3" y1="162.2" x2="943.3" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="171.1" width="2.45" height="29.1" fill="var(--up)"/>
<line x1="947.3" y1="150.0" x2="947.3" y2="235.4" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="153.5" width="2.45" height="64.4" fill="var(--down)"/>
<line x1="951.2" y1="212.7" x2="951.2" y2="235.1" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="223.1" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="955.2" y1="228.8" x2="955.2" y2="244.6" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="235.6" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="959.1" y1="232.8" x2="959.1" y2="247.9" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="233.1" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="963.1" y1="235.3" x2="963.1" y2="276.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="238.1" width="2.45" height="37.3" fill="var(--down)"/>
<line x1="967.0" y1="267.1" x2="967.0" y2="284.4" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="267.6" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="971.0" y1="262.6" x2="971.0" y2="275.5" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="267.5" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="974.9" y1="254.9" x2="974.9" y2="273.2" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="266.1" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="978.9" y1="264.7" x2="978.9" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="267.8" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="982.8" y1="272.1" x2="982.8" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="274.1" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="986.8" y1="266.3" x2="986.8" y2="285.0" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="272.5" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="990.7" y1="275.1" x2="990.7" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="277.7" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="994.7" y1="268.0" x2="994.7" y2="285.8" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="272.2" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="998.6" y1="251.3" x2="998.6" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="262.2" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="1002.6" y1="255.8" x2="1002.6" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="257.4" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="1006.5" y1="265.9" x2="1006.5" y2="286.5" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="266.7" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="1010.5" y1="281.9" x2="1010.5" y2="291.6" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="285.1" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="1014.5" y1="258.9" x2="1014.5" y2="286.2" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="266.8" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="1018.4" y1="272.9" x2="1018.4" y2="295.8" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="275.3" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="1022.4" y1="295.7" x2="1022.4" y2="308.5" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="299.4" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="1026.3" y1="287.1" x2="1026.3" y2="309.2" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="296.0" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="1030.3" y1="272.7" x2="1030.3" y2="286.9" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="279.4" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="1034.2" y1="276.2" x2="1034.2" y2="296.0" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="279.5" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="1038.2" y1="288.1" x2="1038.2" y2="308.0" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="292.1" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="1042.1" y1="312.2" x2="1042.1" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="312.8" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="1046.1" y1="307.9" x2="1046.1" y2="324.9" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="309.9" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="1050.0" y1="277.9" x2="1050.0" y2="302.4" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="291.7" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="60" y1="265.4" x2="1052" y2="265.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="268.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$347 R1</text>
<text x="1058" y="280.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="179.8" x2="1052" y2="179.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="183.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$375 R2</text>
<text x="1058" y="195.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="377.8" x2="1052" y2="377.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="371.8" font-size="11.5" fill="var(--support)" font-weight="600">$311 S1</text>
<text x="1058" y="383.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="424.2" x2="1052" y2="424.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="418.2" font-size="11.5" fill="var(--support)" font-weight="600">$295 S2</text>
<text x="1058" y="430.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="498.4" x2="1052" y2="498.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="492.4" font-size="11.5" fill="var(--support)" font-weight="600">$271 S3</text>
<text x="1058" y="504.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="291.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="283.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $338 (2026-09-11)</text>
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
| R2 | $375 | 3 | 2026-06-16·07-07·07-16 — 2분기 실적 발표(07-22) 직전까지 형성된 고점대 |
| R1 | $347 | 3 | 2026-01-13·02-03·08-24 — 연초 고점대가 8월 하락 국면의 반등 상단으로 재확인됐다 |
| **현재가** | **$338.50** (2026-09-11 종가) | — | R1과 S1 사이. R1까지 +2.5%, S1까지 −8.1% |
| S1 | $311 | 3 | 2026-01-02·02-05·07-23 — 2026년 내내 반복된 지지대. 07-23은 실적 발표 직후 |
| S2 | $295 | 3 | 2025-12-17·2026-02-17·03-09 |
| S3 | $271 | 2 | 2025-11-14·2026-03-30 — 터치 2회로 표본이 얕다 |
| 참고선 | $408.61 | — | 최근 1년 최고가. 2026년 8월 하락 이전의 고점이며 R2($375)와 33달러 떨어져 있어 근시일 저항으로는 R2를 본다 |
| 참고선 | $235.84 | — | 최근 1년 최저가. S3($271)보다 13% 아래이고 그 사이에 터치 2회 이상 클러스터가 없다 |

> 유효 클러스터가 저항 2개·지지 3개로 비대칭이다 — 8월 하락으로 현재가 위쪽 스윙 포인트가 R2($375)와 52주 최고($408.61) 두 덩어리로 흩어졌고, 후자는 터치 횟수가 기준 미달이라 참고선으로 내렸다.

---

## 3. 관측된 특이 구간 — 2026년 8월 하락

- 계기는 실적이 아니라 AI 경쟁력에 대한 의심이었다 — Gemini 플래그십 모델 출시 지연, DeepMind 인력 이탈이 겹치며 고점 대비 약 15% 하락하고 시가총액 약 $700B이 사라졌다. **2015년 이후 최장 월간 연속 하락**이었다([최근 뉴스 / 이슈](./08_news.md) 2026-08 항목).
- 9월 초 반등 계기도 실적 밖에 있었다 — 09-02 애드테크 반독점 구제안에서 AdX 강제 매각이 기각되고 같은 주 Gemini 3.8 Flash가 공개됐다.
- 이 구간 때문에 현재가 위쪽 스윙 구조가 끊겼다. 52주 최고($408.61) 부근의 고점은 하락 이전 레짐의 것이라 위 표에서 저항이 아닌 참고선으로 처리했고, 대신 8월 하락 중 반등 상단이었던 R1($347)이 연초 고점대와 같은 클러스터로 묶였다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-12~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py GOOGL --name "Alphabet" --close-on 2026-09-11 --emit all` (기본 옵션, `--force-level`·`--event` 미사용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 8월 하락으로 현재가 위쪽 레벨의 표본이 얕다 — R2·R1은 각각 터치 3회지만 세 시점이 서로 다른 레짐(하락 전·하락 중)에 걸쳐 있어 같은 강도로 읽으면 안 된다.
    - 이 1년 구간에는 주식분할·대규모 유상증자가 없었다. 2026년 6월 보통주·우선주 발행($49.6B)이 있었으나 기존 주식의 가격 연속성을 깨지 않았다. 기간 내 배당이 4회 있었고 원주가를 썼으므로 배당 재투자 수익은 반영되지 않았다.

---

*작성일: 2026-09-12*
