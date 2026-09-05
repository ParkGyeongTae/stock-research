# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-03 종가 $55.61은 [핵심 지표](./04_metrics.md) A.2 "올해(현재)" 열과 [밸류에이션 / 적정주가](./06_valuation.md) 5절이 쓰는 기준 종가와 같은 값이다** — 세 문서가 같은 날짜·같은 값을 쓴다.
    - **주봉 문서와 1거래일 차이가 있다**: [주봉 문서](./10_technical_weekly.md)의 마지막 종가는 $55.17(2026-09-04)로, 수집 시점에 주봉 시리즈만 하루 더 반영돼 있었다. 밸류에이션에 쓰는 기준 종가는 **일봉 기준 $55.61**로 통일했다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-03)

<div class="eqt-chart">
<style>
.eqt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eqt-chart svg { width:100%; height:auto; display:block; }
.eqt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eqt-chart .title { fill: var(--ink); font-weight:600; }
.eqt-chart .grid { stroke: var(--grid); stroke-width:1; }
.eqt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="EQT Corporation(EQT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">EQT Corporation (EQT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-03 · 마지막 종가 $55.61 (2026-09-03) · 단위 USD</text>
<line x1="60" y1="548.3" x2="1052" y2="548.3" class="grid"/>
<text x="52" y="552.3" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="418.7" x2="1052" y2="418.7" class="grid"/>
<text x="52" y="422.7" font-size="11" text-anchor="end" fill="var(--muted)">55</text>
<line x1="60" y1="289.2" x2="1052" y2="289.2" class="grid"/>
<text x="52" y="293.2" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="159.6" x2="1052" y2="159.6" class="grid"/>
<text x="52" y="163.6" font-size="11" text-anchor="end" fill="var(--muted)">65</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="133.1" y1="626.0" x2="133.1" y2="631.0" class="axis"/>
<text x="133.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="224.0" y1="626.0" x2="224.0" y2="631.0" class="axis"/>
<text x="224.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="299.1" y1="626.0" x2="299.1" y2="631.0" class="axis"/>
<text x="299.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="386.1" y1="626.0" x2="386.1" y2="631.0" class="axis"/>
<text x="386.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="465.1" y1="626.0" x2="465.1" y2="631.0" class="axis"/>
<text x="465.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="540.2" y1="626.0" x2="540.2" y2="631.0" class="axis"/>
<text x="540.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="627.1" y1="626.0" x2="627.1" y2="631.0" class="axis"/>
<text x="627.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="710.1" y1="626.0" x2="710.1" y2="631.0" class="axis"/>
<text x="710.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="789.2" y1="626.0" x2="789.2" y2="631.0" class="axis"/>
<text x="789.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="872.2" y1="626.0" x2="872.2" y2="631.0" class="axis"/>
<text x="872.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="959.1" y1="626.0" x2="959.1" y2="631.0" class="axis"/>
<text x="959.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1042.1" y1="626.0" x2="1042.1" y2="631.0" class="axis"/>
<text x="1042.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="497.0" x2="62.0" y2="535.1" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="506.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="65.9" y1="481.9" x2="65.9" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="486.4" width="2.45" height="42.2" fill="var(--down)"/>
<line x1="69.9" y1="512.0" x2="69.9" y2="547.2" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="527.5" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="73.8" y1="496.5" x2="73.8" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="518.0" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="77.8" y1="516.7" x2="77.8" y2="536.4" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="523.4" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="81.7" y1="496.2" x2="81.7" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="511.7" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="85.7" y1="520.8" x2="85.7" y2="550.3" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="527.3" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="89.6" y1="535.3" x2="89.6" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="543.1" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="93.6" y1="522.6" x2="93.6" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="548.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="97.5" y1="542.8" x2="97.5" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="544.6" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="101.5" y1="560.7" x2="101.5" y2="586.9" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="566.4" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="105.5" y1="541.0" x2="105.5" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="549.0" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="109.4" y1="512.8" x2="109.4" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="523.7" width="2.45" height="21.5" fill="var(--up)"/>
<line x1="113.4" y1="456.0" x2="113.4" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="468.5" width="2.45" height="48.7" fill="var(--up)"/>
<line x1="117.3" y1="419.8" x2="117.3" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="446.4" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="121.3" y1="420.0" x2="121.3" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="443.1" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="125.2" y1="419.5" x2="125.2" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="432.7" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="129.2" y1="410.7" x2="129.2" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="433.5" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="133.1" y1="364.8" x2="133.1" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="388.7" width="2.45" height="49.5" fill="var(--up)"/>
<line x1="137.1" y1="357.8" x2="137.1" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="393.9" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="141.0" y1="380.4" x2="141.0" y2="417.7" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="392.0" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="145.0" y1="359.1" x2="145.0" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="362.0" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="148.9" y1="352.7" x2="148.9" y2="384.8" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="362.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="152.9" y1="362.8" x2="152.9" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="362.8" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="156.8" y1="364.3" x2="156.8" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="364.3" width="2.45" height="56.5" fill="var(--down)"/>
<line x1="160.8" y1="409.4" x2="160.8" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="426.5" width="2.45" height="40.9" fill="var(--down)"/>
<line x1="164.7" y1="448.8" x2="164.7" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="453.4" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="168.7" y1="449.0" x2="168.7" y2="505.3" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="463.0" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="172.6" y1="405.0" x2="172.6" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="407.3" width="2.45" height="38.9" fill="var(--up)"/>
<line x1="176.6" y1="386.9" x2="176.6" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="402.4" width="2.45" height="61.9" fill="var(--down)"/>
<line x1="180.5" y1="430.9" x2="180.5" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="442.6" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="184.5" y1="365.6" x2="184.5" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="381.2" width="2.45" height="28.5" fill="var(--up)"/>
<line x1="188.4" y1="370.0" x2="188.4" y2="403.7" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="396.4" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="192.4" y1="367.4" x2="192.4" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="411.0" width="2.45" height="46.9" fill="var(--down)"/>
<line x1="196.4" y1="425.5" x2="196.4" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="435.6" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="200.3" y1="444.4" x2="200.3" y2="472.9" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="451.1" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="204.3" y1="435.6" x2="204.3" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="448.8" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="208.2" y1="457.3" x2="208.2" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="457.3" width="2.45" height="34.5" fill="var(--down)"/>
<line x1="212.2" y1="460.2" x2="212.2" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="484.3" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="216.1" y1="463.3" x2="216.1" y2="509.2" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="484.8" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="220.1" y1="447.5" x2="220.1" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="455.5" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="224.0" y1="395.2" x2="224.0" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="396.4" width="2.45" height="54.9" fill="var(--up)"/>
<line x1="228.0" y1="374.2" x2="228.0" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="396.7" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="231.9" y1="364.3" x2="231.9" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="393.1" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="235.9" y1="342.6" x2="235.9" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="372.3" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="239.8" y1="341.3" x2="239.8" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="341.8" width="2.45" height="46.6" fill="var(--up)"/>
<line x1="243.8" y1="307.6" x2="243.8" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="316.6" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="247.7" y1="261.7" x2="247.7" y2="308.9" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="271.3" width="2.45" height="33.4" fill="var(--up)"/>
<line x1="251.7" y1="258.9" x2="251.7" y2="288.4" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="267.4" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="255.6" y1="256.5" x2="255.6" y2="285.3" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="267.2" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="259.6" y1="276.2" x2="259.6" y2="343.6" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="291.8" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="263.5" y1="272.1" x2="263.5" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="299.8" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="267.5" y1="314.8" x2="267.5" y2="349.3" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="321.6" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="271.4" y1="310.2" x2="271.4" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="317.9" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="275.4" y1="276.0" x2="275.4" y2="385.6" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="307.6" width="2.45" height="76.2" fill="var(--down)"/>
<line x1="279.3" y1="357.3" x2="279.3" y2="415.4" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="366.1" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="283.3" y1="348.5" x2="283.3" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="352.9" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="287.3" y1="344.1" x2="287.3" y2="390.0" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="369.5" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="291.2" y1="306.3" x2="291.2" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="315.1" width="2.45" height="42.2" fill="var(--up)"/>
<line x1="295.2" y1="258.9" x2="295.2" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="266.9" width="2.45" height="37.1" fill="var(--up)"/>
<line x1="299.1" y1="257.8" x2="299.1" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="272.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="303.1" y1="277.0" x2="303.1" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="277.0" width="2.45" height="48.5" fill="var(--down)"/>
<line x1="307.0" y1="249.8" x2="307.0" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="258.9" width="2.45" height="53.9" fill="var(--up)"/>
<line x1="311.0" y1="237.4" x2="311.0" y2="309.4" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="261.2" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="314.9" y1="231.4" x2="314.9" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="269.8" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="318.9" y1="276.5" x2="318.9" y2="330.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="278.3" width="2.45" height="45.6" fill="var(--down)"/>
<line x1="322.8" y1="310.4" x2="322.8" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="322.1" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="326.8" y1="320.5" x2="326.8" y2="367.2" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="321.8" width="2.45" height="38.6" fill="var(--down)"/>
<line x1="330.7" y1="370.3" x2="330.7" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="370.3" width="2.45" height="20.7" fill="var(--down)"/>
<line x1="334.7" y1="383.0" x2="334.7" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="385.3" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="338.6" y1="403.7" x2="338.6" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="404.0" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="342.6" y1="427.5" x2="342.6" y2="477.3" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="427.5" width="2.45" height="34.7" fill="var(--down)"/>
<line x1="346.5" y1="431.7" x2="346.5" y2="463.5" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="435.3" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="350.5" y1="408.1" x2="350.5" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="438.9" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="354.4" y1="429.3" x2="354.4" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="448.0" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="358.4" y1="435.1" x2="358.4" y2="467.2" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="448.8" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="362.3" y1="425.5" x2="362.3" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="431.2" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="366.3" y1="430.6" x2="366.3" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="443.9" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="370.2" y1="434.0" x2="370.2" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="437.4" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="374.2" y1="425.7" x2="374.2" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="430.6" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="378.2" y1="413.5" x2="378.2" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="418.7" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="382.1" y1="435.8" x2="382.1" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="443.6" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="386.1" y1="453.7" x2="386.1" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="458.6" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="390.0" y1="457.1" x2="390.0" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="461.5" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="394.0" y1="459.7" x2="394.0" y2="490.8" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="459.9" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="397.9" y1="426.8" x2="397.9" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="431.9" width="2.45" height="29.8" fill="var(--up)"/>
<line x1="401.9" y1="429.6" x2="401.9" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="436.6" width="2.45" height="54.7" fill="var(--down)"/>
<line x1="405.8" y1="479.4" x2="405.8" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="493.6" width="2.45" height="26.4" fill="var(--down)"/>
<line x1="409.8" y1="484.8" x2="409.8" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="492.6" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="413.7" y1="466.9" x2="413.7" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="478.6" width="2.45" height="28.5" fill="var(--down)"/>
<line x1="417.7" y1="522.4" x2="417.7" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="526.5" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="421.6" y1="524.2" x2="421.6" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="550.3" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="425.6" y1="522.1" x2="425.6" y2="560.7" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="534.3" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="429.5" y1="460.2" x2="429.5" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="474.9" width="2.45" height="35.0" fill="var(--down)"/>
<line x1="433.5" y1="415.1" x2="433.5" y2="475.7" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="423.1" width="2.45" height="46.1" fill="var(--up)"/>
<line x1="437.4" y1="400.6" x2="437.4" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="405.8" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="441.4" y1="381.7" x2="441.4" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="400.6" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="445.3" y1="369.5" x2="445.3" y2="421.8" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="382.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="449.3" y1="388.4" x2="449.3" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="392.6" width="2.45" height="41.5" fill="var(--down)"/>
<line x1="453.2" y1="392.6" x2="453.2" y2="452.4" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="393.9" width="2.45" height="33.2" fill="var(--up)"/>
<line x1="457.2" y1="361.7" x2="457.2" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="362.0" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="461.1" y1="333.7" x2="461.1" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="348.0" width="2.45" height="32.4" fill="var(--up)"/>
<line x1="465.1" y1="393.3" x2="465.1" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="405.8" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="469.1" y1="402.7" x2="469.1" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="403.2" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="473.0" y1="378.3" x2="473.0" y2="422.1" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="387.4" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="477.0" y1="401.1" x2="477.0" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="410.2" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="480.9" y1="367.2" x2="480.9" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="372.3" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="484.9" y1="373.6" x2="484.9" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="389.4" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="488.8" y1="386.3" x2="488.8" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="388.7" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="492.8" y1="358.1" x2="492.8" y2="398.5" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="368.7" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="496.7" y1="344.6" x2="496.7" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="362.2" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="500.7" y1="314.8" x2="500.7" y2="381.9" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="322.9" width="2.45" height="52.6" fill="var(--up)"/>
<line x1="504.6" y1="317.9" x2="504.6" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="321.8" width="2.45" height="25.7" fill="var(--down)"/>
<line x1="508.6" y1="300.8" x2="508.6" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="324.7" width="2.45" height="60.9" fill="var(--up)"/>
<line x1="512.5" y1="257.1" x2="512.5" y2="314.8" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="295.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="516.5" y1="266.1" x2="516.5" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="276.2" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="520.4" y1="256.8" x2="520.4" y2="324.7" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="276.0" width="2.45" height="38.3" fill="var(--down)"/>
<line x1="524.4" y1="312.2" x2="524.4" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="316.4" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="528.3" y1="299.5" x2="528.3" y2="328.0" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="305.2" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="532.3" y1="289.4" x2="532.3" y2="327.5" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="295.9" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="536.2" y1="243.3" x2="536.2" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="252.4" width="2.45" height="25.9" fill="var(--up)"/>
<line x1="540.2" y1="224.7" x2="540.2" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="229.8" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="544.1" y1="209.9" x2="544.1" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="236.1" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="548.1" y1="251.4" x2="548.1" y2="286.1" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="255.2" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="552.0" y1="227.3" x2="552.0" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="245.9" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="556.0" y1="211.5" x2="556.0" y2="244.9" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="230.4" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="560.0" y1="213.3" x2="560.0" y2="250.1" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="228.6" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="563.9" y1="228.0" x2="563.9" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="240.0" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="567.9" y1="189.7" x2="567.9" y2="241.3" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="189.9" width="2.45" height="46.1" fill="var(--up)"/>
<line x1="571.8" y1="151.3" x2="571.8" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="169.0" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="575.8" y1="150.8" x2="575.8" y2="184.0" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="174.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="579.7" y1="159.9" x2="579.7" y2="186.8" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="177.5" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="583.7" y1="142.0" x2="583.7" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="164.6" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="587.6" y1="170.0" x2="587.6" y2="234.5" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="174.4" width="2.45" height="23.6" fill="var(--down)"/>
<line x1="591.6" y1="103.9" x2="591.6" y2="189.4" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="167.9" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="595.5" y1="126.7" x2="595.5" y2="174.4" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="159.6" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="599.5" y1="121.0" x2="599.5" y2="211.2" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="153.7" width="2.45" height="49.2" fill="var(--up)"/>
<line x1="603.4" y1="101.1" x2="603.4" y2="154.5" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="141.5" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="607.4" y1="82.2" x2="607.4" y2="149.3" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="83.7" width="2.45" height="62.7" fill="var(--up)"/>
<line x1="611.3" y1="85.0" x2="611.3" y2="115.1" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="85.0" width="2.45" height="26.4" fill="var(--down)"/>
<line x1="615.3" y1="75.7" x2="615.3" y2="100.6" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="93.6" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="619.2" y1="88.6" x2="619.2" y2="189.2" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="95.9" width="2.45" height="78.2" fill="var(--down)"/>
<line x1="623.2" y1="144.9" x2="623.2" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="159.4" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="627.1" y1="205.2" x2="627.1" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="224.4" width="2.45" height="36.5" fill="var(--down)"/>
<line x1="631.1" y1="233.0" x2="631.1" y2="304.7" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="235.0" width="2.45" height="61.9" fill="var(--down)"/>
<line x1="635.0" y1="265.6" x2="635.0" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="278.8" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="639.0" y1="249.0" x2="639.0" y2="283.7" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="271.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="642.9" y1="279.1" x2="642.9" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="284.5" width="2.45" height="32.6" fill="var(--up)"/>
<line x1="646.9" y1="266.9" x2="646.9" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="283.5" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="650.9" y1="302.4" x2="650.9" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="317.4" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="654.8" y1="315.9" x2="654.8" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="320.8" width="2.45" height="28.0" fill="var(--down)"/>
<line x1="658.8" y1="344.6" x2="658.8" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="354.7" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="662.7" y1="362.5" x2="662.7" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="373.1" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="666.7" y1="328.0" x2="666.7" y2="373.1" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="330.9" width="2.45" height="36.3" fill="var(--up)"/>
<line x1="670.6" y1="325.2" x2="670.6" y2="383.0" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="328.6" width="2.45" height="44.6" fill="var(--up)"/>
<line x1="674.6" y1="327.8" x2="674.6" y2="373.1" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="351.4" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="678.5" y1="356.0" x2="678.5" y2="386.1" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="367.4" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="682.5" y1="308.4" x2="682.5" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="322.3" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="686.4" y1="302.1" x2="686.4" y2="344.1" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="316.9" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="690.4" y1="313.8" x2="690.4" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="317.4" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="694.3" y1="268.5" x2="694.3" y2="330.6" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="300.6" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="698.3" y1="287.6" x2="698.3" y2="307.6" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="303.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="702.2" y1="281.4" x2="702.2" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="300.6" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="706.2" y1="272.1" x2="706.2" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="287.1" width="2.45" height="35.2" fill="var(--up)"/>
<line x1="710.1" y1="288.4" x2="710.1" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="289.2" width="2.45" height="34.7" fill="var(--down)"/>
<line x1="714.1" y1="293.6" x2="714.1" y2="323.1" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="313.0" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="718.0" y1="304.5" x2="718.0" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="322.3" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="722.0" y1="334.0" x2="722.0" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="354.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="725.9" y1="374.4" x2="725.9" y2="410.7" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="377.8" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="729.9" y1="374.2" x2="729.9" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="383.0" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="733.8" y1="366.9" x2="733.8" y2="388.9" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="379.9" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="737.8" y1="373.9" x2="737.8" y2="407.1" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="378.8" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="741.8" y1="393.6" x2="741.8" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="394.6" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="745.7" y1="366.9" x2="745.7" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="378.1" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="749.7" y1="361.2" x2="749.7" y2="390.0" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="363.3" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="753.6" y1="347.0" x2="753.6" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="355.2" width="2.45" height="28.5" fill="var(--up)"/>
<line x1="757.6" y1="294.4" x2="757.6" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="295.1" width="2.45" height="50.8" fill="var(--up)"/>
<line x1="761.5" y1="299.8" x2="761.5" y2="348.8" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="307.1" width="2.45" height="38.3" fill="var(--down)"/>
<line x1="765.5" y1="321.8" x2="765.5" y2="351.9" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="324.9" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="769.4" y1="338.9" x2="769.4" y2="366.7" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="343.1" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="773.4" y1="342.8" x2="773.4" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="349.6" width="2.45" height="37.8" fill="var(--down)"/>
<line x1="777.3" y1="389.7" x2="777.3" y2="417.2" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="398.5" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="781.3" y1="402.7" x2="781.3" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="409.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="785.2" y1="404.7" x2="785.2" y2="430.9" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="406.0" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="789.2" y1="400.9" x2="789.2" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="412.0" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="793.1" y1="405.8" x2="793.1" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="419.0" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="797.1" y1="418.2" x2="797.1" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="420.5" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="801.0" y1="400.1" x2="801.0" y2="425.5" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="412.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="805.0" y1="405.5" x2="805.0" y2="453.2" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="413.8" width="2.45" height="37.3" fill="var(--down)"/>
<line x1="808.9" y1="444.1" x2="808.9" y2="477.5" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="457.6" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="812.9" y1="469.0" x2="812.9" y2="489.2" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="471.1" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="816.8" y1="456.6" x2="816.8" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="467.4" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="820.8" y1="458.9" x2="820.8" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="469.5" width="2.45" height="47.7" fill="var(--down)"/>
<line x1="824.7" y1="488.9" x2="824.7" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="498.0" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="828.7" y1="492.1" x2="828.7" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="528.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="832.7" y1="499.3" x2="832.7" y2="541.8" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="512.8" width="2.45" height="22.3" fill="var(--up)"/>
<line x1="836.6" y1="501.4" x2="836.6" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="519.0" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="840.6" y1="510.7" x2="840.6" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="527.5" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="844.5" y1="500.3" x2="844.5" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="500.6" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="848.5" y1="501.6" x2="848.5" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="505.3" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="852.4" y1="492.1" x2="852.4" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="509.9" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="856.4" y1="501.6" x2="856.4" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="505.5" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="860.3" y1="455.0" x2="860.3" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="478.3" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="864.3" y1="472.6" x2="864.3" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="482.2" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="868.2" y1="451.4" x2="868.2" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="466.1" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="872.2" y1="464.1" x2="872.2" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="470.5" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="876.1" y1="465.9" x2="876.1" y2="491.5" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="475.5" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="880.1" y1="477.8" x2="880.1" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="481.9" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="884.0" y1="494.9" x2="884.0" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="502.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="888.0" y1="495.4" x2="888.0" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="499.6" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="891.9" y1="515.6" x2="891.9" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="516.1" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="895.9" y1="542.1" x2="895.9" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="545.4" width="2.45" height="32.6" fill="var(--down)"/>
<line x1="899.8" y1="549.6" x2="899.8" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="555.5" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="903.8" y1="539.7" x2="903.8" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="553.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="907.7" y1="538.4" x2="907.7" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="553.2" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="911.7" y1="553.5" x2="911.7" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="559.9" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="915.6" y1="535.3" x2="915.6" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="546.2" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="919.6" y1="562.0" x2="919.6" y2="585.6" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="564.1" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="923.6" y1="551.4" x2="923.6" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="553.5" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="927.5" y1="443.1" x2="927.5" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="444.4" width="2.45" height="75.4" fill="var(--up)"/>
<line x1="931.5" y1="423.6" x2="931.5" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="434.5" width="2.45" height="25.9" fill="var(--down)"/>
<line x1="935.4" y1="436.1" x2="935.4" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="453.7" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="939.4" y1="476.0" x2="939.4" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="485.3" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="943.3" y1="471.8" x2="943.3" y2="516.7" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="493.9" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="947.3" y1="465.9" x2="947.3" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="481.7" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="951.2" y1="477.0" x2="951.2" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="478.1" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="955.2" y1="461.5" x2="955.2" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="463.0" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="959.1" y1="451.4" x2="959.1" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="456.0" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="963.1" y1="465.9" x2="963.1" y2="496.5" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="476.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="967.0" y1="463.8" x2="967.0" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="470.5" width="2.45" height="45.9" fill="var(--down)"/>
<line x1="971.0" y1="485.8" x2="971.0" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="493.3" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="974.9" y1="497.0" x2="974.9" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="504.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="978.9" y1="440.7" x2="978.9" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="442.6" width="2.45" height="42.5" fill="var(--up)"/>
<line x1="982.8" y1="429.3" x2="982.8" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="435.1" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="986.8" y1="426.0" x2="986.8" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="436.9" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="990.7" y1="440.0" x2="990.7" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="442.6" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="994.7" y1="414.8" x2="994.7" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="433.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="998.6" y1="433.8" x2="998.6" y2="486.6" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="435.1" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="1002.6" y1="446.7" x2="1002.6" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="451.6" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="1006.5" y1="443.3" x2="1006.5" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="451.6" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="1010.5" y1="427.3" x2="1010.5" y2="467.4" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="447.5" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="1014.5" y1="431.7" x2="1014.5" y2="456.3" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="445.2" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="1018.4" y1="436.3" x2="1018.4" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="445.7" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="1022.4" y1="431.4" x2="1022.4" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="444.6" width="2.45" height="27.2" fill="var(--up)"/>
<line x1="1026.3" y1="380.6" x2="1026.3" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="424.2" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="1030.3" y1="418.0" x2="1030.3" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="424.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1034.2" y1="407.6" x2="1034.2" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="419.0" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="1038.2" y1="393.1" x2="1038.2" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="394.1" width="2.45" height="45.9" fill="var(--down)"/>
<line x1="1042.1" y1="399.6" x2="1042.1" y2="436.9" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="403.4" width="2.45" height="31.1" fill="var(--up)"/>
<line x1="1046.1" y1="393.3" x2="1046.1" y2="420.3" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="399.3" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="1050.0" y1="379.3" x2="1050.0" y2="404.0" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="395.2" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="60" y1="358.2" x2="1052" y2="358.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="361.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$57 R1</text>
<text x="1058" y="373.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="273.1" x2="1052" y2="273.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="276.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$61 R2</text>
<text x="1058" y="288.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="220.7" x2="1052" y2="220.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="224.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$63 R3</text>
<text x="1058" y="236.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="425.2" x2="1052" y2="425.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="419.2" font-size="11.5" fill="var(--support)" font-weight="600">$55 S1</text>
<text x="1058" y="431.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="479.5" x2="1052" y2="479.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="473.5" font-size="11.5" fill="var(--support)" font-weight="600">$53 S2</text>
<text x="1058" y="485.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="523.0" x2="1052" y2="523.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="517.0" font-size="11.5" fill="var(--support)" font-weight="600">$51 S3</text>
<text x="1058" y="529.0" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="402.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="394.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $56 (2026-09-03)</text>
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
| R3 | $63 | 2 | 2025-12·2026-03 두 차례 고점대 — 2026-03 고점 $68.24로 가는 길목 |
| R2 | $61 | 3 | 2025-11·2026-04·2026-05 고점대 — 하락 전환 직전 구간 |
| R1 | $57 | 4 | 2025-10(2회)·2026-01·2026-08 — **현재가 바로 위, 최근에도 닿은 유효 저항** |
| **현재가** | **$55.61** (2026-09-03 종가) | — | R1과 S1 사이 |
| S1 | $55 | 3 | 2025-11·2026-02·2026-05 저점대 — 현재가에 가장 근접한 지지 |
| S2 | $53 | 2 | 2025-12·2026-08 — 2026-08 중순 횡보의 바닥 |
| S3 | $51 | 4 | 2025-10(2회)·2026-06·2026-08 — 1년 내내 반복 확인된 최하단 지지 |
| 참고선 | $68.24 / $47.94 | — | 52주 최고(2026-03-27) / 최저(2026-07-10). 각각 한 번만 닿은 극단값이라 클러스터를 이루지 못해 지지·저항으로 쓰지 않는다 |

**현재가 $55.61은 S1($55)과 R1($57) 사이의 좁은 구간에 있다.** 위아래 레벨까지 거리가 각각 +2.5% · −1.1%뿐이라 이 차트만으로는 방향을 말할 수 없다. 눈여겨볼 것은 오히려 **R1이 1년 중 가장 여러 번(4회) 확인된 저항이고 그중 한 번이 2026-08-26으로 최근**이라는 점이다.

---

## 3. 관측된 특이 구간 — 2026-07-22 Q2 2026 실적 발표 갭업

- 계기는 전일(2026-07-21) 장 마감 후 발표된 **Q2 2026 실적과 가이던스 상향, 그리고 판매계약 3건 동시 공시**다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **+8.45%** ($49.80 → $54.01), 거래량은 평소(일 822만 주 내외) 대비 약 **2.2배**인 **1,785만 주**로 1년 중 최대였다.
- **이 갭이 가격대를 재설정했다.** 직전 2주간 주가는 52주 최저($47.94, 2026-07-10) 부근에 머물러 있었는데, 이 하루로 $54대에 올라선 뒤 8월 내내 $53~$55 구간에서 횡보했다. 위 표의 S1($55)·S2($53)가 모두 이 갭 이후 형성된 좁은 박스의 상·하단이며, **갭 이전 구간의 스윙 저점들(S3 $51)과는 성격이 다르다** — 같은 표에 있지만 서로 다른 레짐의 레벨이라는 점을 감안해 읽을 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-05~2026-09-03. 수집 시점: 2026-09-05. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py EQT --name "EQT Corporation" --close-on 2026-09-03 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨을 기본값 3개가 아니라 6개(R 3 · S 3)로 뽑았다** — 터치 2회 이상 조건을 만족하는 클러스터가 실제로 6개였고, 억지로 줄이면 최근 레짐(3절 갭 이후)과 이전 레짐의 레벨이 뒤섞인다.
    - **3절의 2026-07-22 갭 때문에 레벨 해석이 두 구간으로 나뉜다.** S1·S2는 갭 이후 8주치 데이터로만 만들어진 레벨이라 표본이 얕다.
    - 기간 내 주식분할은 없었다. 다만 **분기배당이 4회 있었고 원주가라 배당은 반영되지 않았다** — 배당수익률이 연 1.2% 수준이라 레벨에 미치는 영향은 제한적이다. 이 기간의 주식수 증가(Olympus Energy 인수 대가)는 2025년 7월로 차트 구간 시작 이전이다.

---

*작성일: 2026-09-05*
