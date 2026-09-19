# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **이 차트의 마지막 봉은 2026-09-17(종가 $50.35)이고, [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준 종가는 2026-09-18의 $50.00이다 — 하루 어긋난다.** 9월 18일 세션은 정상 체결됐으나 조회 시점(2026-09-19)에 Yahoo 일봉 시계열의 해당 봉 종가가 비어 있었다(시가·고가·저가는 있고 종가만 `null`). 같은 주의 [주봉 차트](./10_technical_weekly.md)는 그 세션을 포함해 종가 $50.00으로 마감돼 있어, **두 차트를 나란히 보면 값이 다른 것이 정상**이다. 수정주가가 아니라 원주가를 쓴 데서 온 차이가 아니라는 점을 분명히 해 둔다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-19 ~ 2026-09-17)

<style>
.eqt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eqt-chart svg { width:100%; height:auto; display:block; }
.eqt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eqt-chart .title { fill: var(--ink); font-weight:600; }
.eqt-chart .grid { stroke: var(--grid); stroke-width:1; }
.eqt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="eqt-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="EQT Corporation(EQT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">EQT Corporation (EQT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-19 ~ 2026-09-17 · 마지막 종가 $50.35 (2026-09-17) · 단위 USD</text>
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
<line x1="93.7" y1="626.0" x2="93.7" y2="631.0" class="axis"/>
<text x="93.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="185.0" y1="626.0" x2="185.0" y2="631.0" class="axis"/>
<text x="185.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="260.4" y1="626.0" x2="260.4" y2="631.0" class="axis"/>
<text x="260.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="347.7" y1="626.0" x2="347.7" y2="631.0" class="axis"/>
<text x="347.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="427.0" y1="626.0" x2="427.0" y2="631.0" class="axis"/>
<text x="427.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="502.4" y1="626.0" x2="502.4" y2="631.0" class="axis"/>
<text x="502.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="589.7" y1="626.0" x2="589.7" y2="631.0" class="axis"/>
<text x="589.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="673.1" y1="626.0" x2="673.1" y2="631.0" class="axis"/>
<text x="673.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="752.4" y1="626.0" x2="752.4" y2="631.0" class="axis"/>
<text x="752.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="835.7" y1="626.0" x2="835.7" y2="631.0" class="axis"/>
<text x="835.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="923.0" y1="626.0" x2="923.0" y2="631.0" class="axis"/>
<text x="923.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1006.4" y1="626.0" x2="1006.4" y2="631.0" class="axis"/>
<text x="1006.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="560.7" x2="62.0" y2="586.9" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="566.4" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="66.0" y1="541.0" x2="66.0" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="549.0" width="2.46" height="24.6" fill="var(--up)"/>
<line x1="69.9" y1="512.8" x2="69.9" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="523.7" width="2.46" height="21.5" fill="var(--up)"/>
<line x1="73.9" y1="456.0" x2="73.9" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="468.5" width="2.46" height="48.7" fill="var(--up)"/>
<line x1="77.9" y1="419.8" x2="77.9" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="446.4" width="2.46" height="26.4" fill="var(--up)"/>
<line x1="81.8" y1="420.0" x2="81.8" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="443.1" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="85.8" y1="419.5" x2="85.8" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="432.7" width="2.46" height="13.0" fill="var(--up)"/>
<line x1="89.8" y1="410.7" x2="89.8" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="88.53" y="433.5" width="2.46" height="11.4" fill="var(--up)"/>
<line x1="93.7" y1="364.8" x2="93.7" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="388.7" width="2.46" height="49.5" fill="var(--up)"/>
<line x1="97.7" y1="357.8" x2="97.7" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="96.47" y="393.9" width="2.46" height="5.2" fill="var(--down)"/>
<line x1="101.7" y1="380.4" x2="101.7" y2="417.7" stroke="var(--up)" class="wick"/>
<rect x="100.43" y="392.0" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="105.6" y1="359.1" x2="105.6" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="104.40" y="362.0" width="2.46" height="15.5" fill="var(--up)"/>
<line x1="109.6" y1="352.7" x2="109.6" y2="384.8" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="362.8" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="113.6" y1="362.8" x2="113.6" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="362.8" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="117.5" y1="364.3" x2="117.5" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="116.31" y="364.3" width="2.46" height="56.5" fill="var(--down)"/>
<line x1="121.5" y1="409.4" x2="121.5" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="120.27" y="426.5" width="2.46" height="40.9" fill="var(--down)"/>
<line x1="125.5" y1="448.8" x2="125.5" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="453.4" width="2.46" height="11.4" fill="var(--up)"/>
<line x1="129.4" y1="449.0" x2="129.4" y2="505.3" stroke="var(--up)" class="wick"/>
<rect x="128.21" y="463.0" width="2.46" height="14.2" fill="var(--up)"/>
<line x1="133.4" y1="405.0" x2="133.4" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="132.18" y="407.3" width="2.46" height="38.9" fill="var(--up)"/>
<line x1="137.4" y1="386.9" x2="137.4" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="402.4" width="2.46" height="61.9" fill="var(--down)"/>
<line x1="141.3" y1="430.9" x2="141.3" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="442.6" width="2.46" height="15.3" fill="var(--up)"/>
<line x1="145.3" y1="365.6" x2="145.3" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="381.2" width="2.46" height="28.5" fill="var(--up)"/>
<line x1="149.3" y1="370.0" x2="149.3" y2="403.7" stroke="var(--down)" class="wick"/>
<rect x="148.05" y="396.4" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="153.2" y1="367.4" x2="153.2" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="152.02" y="411.0" width="2.46" height="46.9" fill="var(--down)"/>
<line x1="157.2" y1="425.5" x2="157.2" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="155.99" y="435.6" width="2.46" height="20.5" fill="var(--down)"/>
<line x1="161.2" y1="444.4" x2="161.2" y2="472.9" stroke="var(--down)" class="wick"/>
<rect x="159.95" y="451.1" width="2.46" height="1.3" fill="var(--down)"/>
<line x1="165.2" y1="435.6" x2="165.2" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="163.92" y="448.8" width="2.46" height="2.3" fill="var(--down)"/>
<line x1="169.1" y1="457.3" x2="169.1" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="457.3" width="2.46" height="34.5" fill="var(--down)"/>
<line x1="173.1" y1="460.2" x2="173.1" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="171.86" y="484.3" width="2.46" height="17.4" fill="var(--down)"/>
<line x1="177.1" y1="463.3" x2="177.1" y2="509.2" stroke="var(--up)" class="wick"/>
<rect x="175.83" y="484.8" width="2.46" height="11.4" fill="var(--up)"/>
<line x1="181.0" y1="447.5" x2="181.0" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="455.5" width="2.46" height="14.8" fill="var(--up)"/>
<line x1="185.0" y1="395.2" x2="185.0" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="396.4" width="2.46" height="54.9" fill="var(--up)"/>
<line x1="189.0" y1="374.2" x2="189.0" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="187.73" y="396.7" width="2.46" height="21.2" fill="var(--up)"/>
<line x1="192.9" y1="364.3" x2="192.9" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="191.70" y="393.1" width="2.46" height="8.6" fill="var(--up)"/>
<line x1="196.9" y1="342.6" x2="196.9" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="195.67" y="372.3" width="2.46" height="13.2" fill="var(--down)"/>
<line x1="200.9" y1="341.3" x2="200.9" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="199.63" y="341.8" width="2.46" height="46.6" fill="var(--up)"/>
<line x1="204.8" y1="307.6" x2="204.8" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="203.60" y="316.6" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="208.8" y1="261.7" x2="208.8" y2="308.9" stroke="var(--up)" class="wick"/>
<rect x="207.57" y="271.3" width="2.46" height="33.4" fill="var(--up)"/>
<line x1="212.8" y1="258.9" x2="212.8" y2="288.4" stroke="var(--up)" class="wick"/>
<rect x="211.54" y="267.4" width="2.46" height="21.0" fill="var(--up)"/>
<line x1="216.7" y1="256.5" x2="216.7" y2="285.3" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="267.2" width="2.46" height="15.5" fill="var(--down)"/>
<line x1="220.7" y1="276.2" x2="220.7" y2="343.6" stroke="var(--up)" class="wick"/>
<rect x="219.47" y="291.8" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="224.7" y1="272.1" x2="224.7" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="299.8" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="228.6" y1="314.8" x2="228.6" y2="349.3" stroke="var(--up)" class="wick"/>
<rect x="227.41" y="321.6" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="232.6" y1="310.2" x2="232.6" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="317.9" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="236.6" y1="276.0" x2="236.6" y2="385.6" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="307.6" width="2.46" height="76.2" fill="var(--down)"/>
<line x1="240.5" y1="357.3" x2="240.5" y2="415.4" stroke="var(--up)" class="wick"/>
<rect x="239.31" y="366.1" width="2.46" height="23.8" fill="var(--up)"/>
<line x1="244.5" y1="348.5" x2="244.5" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="352.9" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="248.5" y1="344.1" x2="248.5" y2="390.0" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="369.5" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="252.4" y1="306.3" x2="252.4" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="251.22" y="315.1" width="2.46" height="42.2" fill="var(--up)"/>
<line x1="256.4" y1="258.9" x2="256.4" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="266.9" width="2.46" height="37.1" fill="var(--up)"/>
<line x1="260.4" y1="257.8" x2="260.4" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="259.15" y="272.1" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="264.4" y1="277.0" x2="264.4" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="263.12" y="277.0" width="2.46" height="48.5" fill="var(--down)"/>
<line x1="268.3" y1="249.8" x2="268.3" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="267.09" y="258.9" width="2.46" height="53.9" fill="var(--up)"/>
<line x1="272.3" y1="237.4" x2="272.3" y2="309.4" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="261.2" width="2.46" height="26.2" fill="var(--down)"/>
<line x1="276.3" y1="231.4" x2="276.3" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="269.8" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="280.2" y1="276.5" x2="280.2" y2="330.4" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="278.3" width="2.46" height="45.6" fill="var(--down)"/>
<line x1="284.2" y1="310.4" x2="284.2" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="322.1" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="288.2" y1="320.5" x2="288.2" y2="367.2" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="321.8" width="2.46" height="38.6" fill="var(--down)"/>
<line x1="292.1" y1="370.3" x2="292.1" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="370.3" width="2.46" height="20.7" fill="var(--down)"/>
<line x1="296.1" y1="383.0" x2="296.1" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="294.87" y="385.3" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="300.1" y1="403.7" x2="300.1" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="404.0" width="2.46" height="10.4" fill="var(--down)"/>
<line x1="304.0" y1="427.5" x2="304.0" y2="477.3" stroke="var(--down)" class="wick"/>
<rect x="302.80" y="427.5" width="2.46" height="34.7" fill="var(--down)"/>
<line x1="308.0" y1="431.7" x2="308.0" y2="463.5" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="435.3" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="312.0" y1="408.1" x2="312.0" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="310.74" y="438.9" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="315.9" y1="429.3" x2="315.9" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="314.71" y="448.0" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="319.9" y1="435.1" x2="319.9" y2="467.2" stroke="var(--down)" class="wick"/>
<rect x="318.67" y="448.8" width="2.46" height="8.8" fill="var(--down)"/>
<line x1="323.9" y1="425.5" x2="323.9" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="431.2" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="327.8" y1="430.6" x2="327.8" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="443.9" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="331.8" y1="434.0" x2="331.8" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="437.4" width="2.46" height="9.1" fill="var(--down)"/>
<line x1="335.8" y1="425.7" x2="335.8" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="334.55" y="430.6" width="2.46" height="14.0" fill="var(--up)"/>
<line x1="339.7" y1="413.5" x2="339.7" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="338.51" y="418.7" width="2.46" height="9.6" fill="var(--down)"/>
<line x1="343.7" y1="435.8" x2="343.7" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="342.48" y="443.6" width="2.46" height="11.4" fill="var(--down)"/>
<line x1="347.7" y1="453.7" x2="347.7" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="346.45" y="458.6" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="351.6" y1="457.1" x2="351.6" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="461.5" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="355.6" y1="459.7" x2="355.6" y2="490.8" stroke="var(--up)" class="wick"/>
<rect x="354.39" y="459.9" width="2.46" height="16.8" fill="var(--up)"/>
<line x1="359.6" y1="426.8" x2="359.6" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="431.9" width="2.46" height="29.8" fill="var(--up)"/>
<line x1="363.6" y1="429.6" x2="363.6" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="436.6" width="2.46" height="54.7" fill="var(--down)"/>
<line x1="367.5" y1="479.4" x2="367.5" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="493.6" width="2.46" height="26.4" fill="var(--down)"/>
<line x1="371.5" y1="484.8" x2="371.5" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="370.26" y="492.6" width="2.46" height="16.8" fill="var(--up)"/>
<line x1="375.5" y1="466.9" x2="375.5" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="478.6" width="2.46" height="28.5" fill="var(--down)"/>
<line x1="379.4" y1="522.4" x2="379.4" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="378.19" y="526.5" width="2.46" height="15.0" fill="var(--down)"/>
<line x1="383.4" y1="524.2" x2="383.4" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="550.3" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="387.4" y1="522.1" x2="387.4" y2="560.7" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="534.3" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="391.3" y1="460.2" x2="391.3" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="390.10" y="474.9" width="2.46" height="35.0" fill="var(--down)"/>
<line x1="395.3" y1="415.1" x2="395.3" y2="475.7" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="423.1" width="2.46" height="46.1" fill="var(--up)"/>
<line x1="399.3" y1="400.6" x2="399.3" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="405.8" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="403.2" y1="381.7" x2="403.2" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="400.6" width="2.46" height="4.7" fill="var(--down)"/>
<line x1="407.2" y1="369.5" x2="407.2" y2="421.8" stroke="var(--up)" class="wick"/>
<rect x="405.97" y="382.2" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="411.2" y1="388.4" x2="411.2" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="409.94" y="392.6" width="2.46" height="41.5" fill="var(--down)"/>
<line x1="415.1" y1="392.6" x2="415.1" y2="452.4" stroke="var(--up)" class="wick"/>
<rect x="413.91" y="393.9" width="2.46" height="33.2" fill="var(--up)"/>
<line x1="419.1" y1="361.7" x2="419.1" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="417.87" y="362.0" width="2.46" height="22.3" fill="var(--down)"/>
<line x1="423.1" y1="333.7" x2="423.1" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="348.0" width="2.46" height="32.4" fill="var(--up)"/>
<line x1="427.0" y1="393.3" x2="427.0" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="425.81" y="405.8" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="431.0" y1="402.7" x2="431.0" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="403.2" width="2.46" height="26.4" fill="var(--up)"/>
<line x1="435.0" y1="378.3" x2="435.0" y2="422.1" stroke="var(--down)" class="wick"/>
<rect x="433.75" y="387.4" width="2.46" height="21.0" fill="var(--down)"/>
<line x1="438.9" y1="401.1" x2="438.9" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="437.71" y="410.2" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="442.9" y1="367.2" x2="442.9" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="372.3" width="2.46" height="30.8" fill="var(--up)"/>
<line x1="446.9" y1="373.6" x2="446.9" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="445.65" y="389.4" width="2.46" height="14.8" fill="var(--up)"/>
<line x1="450.8" y1="386.3" x2="450.8" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="449.62" y="388.7" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="454.8" y1="358.1" x2="454.8" y2="398.5" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="368.7" width="2.46" height="23.6" fill="var(--up)"/>
<line x1="458.8" y1="344.6" x2="458.8" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="457.55" y="362.2" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="462.8" y1="314.8" x2="462.8" y2="381.9" stroke="var(--up)" class="wick"/>
<rect x="461.52" y="322.9" width="2.46" height="52.6" fill="var(--up)"/>
<line x1="466.7" y1="317.9" x2="466.7" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="321.8" width="2.46" height="25.7" fill="var(--down)"/>
<line x1="470.7" y1="300.8" x2="470.7" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="469.46" y="324.7" width="2.46" height="60.9" fill="var(--up)"/>
<line x1="474.7" y1="257.1" x2="474.7" y2="314.8" stroke="var(--up)" class="wick"/>
<rect x="473.43" y="295.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="478.6" y1="266.1" x2="478.6" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="276.2" width="2.46" height="13.0" fill="var(--up)"/>
<line x1="482.6" y1="256.8" x2="482.6" y2="324.7" stroke="var(--down)" class="wick"/>
<rect x="481.36" y="276.0" width="2.46" height="38.3" fill="var(--down)"/>
<line x1="486.6" y1="312.2" x2="486.6" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="485.33" y="316.4" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="490.5" y1="299.5" x2="490.5" y2="328.0" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="305.2" width="2.46" height="22.8" fill="var(--up)"/>
<line x1="494.5" y1="289.4" x2="494.5" y2="327.5" stroke="var(--up)" class="wick"/>
<rect x="493.27" y="295.9" width="2.46" height="29.5" fill="var(--up)"/>
<line x1="498.5" y1="243.3" x2="498.5" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="252.4" width="2.46" height="25.9" fill="var(--up)"/>
<line x1="502.4" y1="224.7" x2="502.4" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="229.8" width="2.46" height="16.8" fill="var(--down)"/>
<line x1="506.4" y1="209.9" x2="506.4" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="505.17" y="236.1" width="2.46" height="11.4" fill="var(--down)"/>
<line x1="510.4" y1="251.4" x2="510.4" y2="286.1" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="255.2" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="514.3" y1="227.3" x2="514.3" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="245.9" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="518.3" y1="211.5" x2="518.3" y2="244.9" stroke="var(--down)" class="wick"/>
<rect x="517.07" y="230.4" width="2.46" height="8.0" fill="var(--down)"/>
<line x1="522.3" y1="213.3" x2="522.3" y2="250.1" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="228.6" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="526.2" y1="228.0" x2="526.2" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="525.01" y="240.0" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="530.2" y1="189.7" x2="530.2" y2="241.3" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="189.9" width="2.46" height="46.1" fill="var(--up)"/>
<line x1="534.2" y1="151.3" x2="534.2" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="169.0" width="2.46" height="9.8" fill="var(--up)"/>
<line x1="538.1" y1="150.8" x2="538.1" y2="184.0" stroke="var(--down)" class="wick"/>
<rect x="536.91" y="174.1" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="542.1" y1="159.9" x2="542.1" y2="186.8" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="177.5" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="546.1" y1="142.0" x2="546.1" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="544.85" y="164.6" width="2.46" height="9.8" fill="var(--down)"/>
<line x1="550.0" y1="170.0" x2="550.0" y2="234.5" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="174.4" width="2.46" height="23.6" fill="var(--down)"/>
<line x1="554.0" y1="103.9" x2="554.0" y2="189.4" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="167.9" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="558.0" y1="126.7" x2="558.0" y2="174.4" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="159.6" width="2.46" height="8.6" fill="var(--down)"/>
<line x1="562.0" y1="121.0" x2="562.0" y2="211.2" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="153.7" width="2.46" height="49.2" fill="var(--up)"/>
<line x1="565.9" y1="101.1" x2="565.9" y2="154.5" stroke="var(--down)" class="wick"/>
<rect x="564.69" y="141.5" width="2.46" height="9.6" fill="var(--down)"/>
<line x1="569.9" y1="82.2" x2="569.9" y2="149.3" stroke="var(--up)" class="wick"/>
<rect x="568.66" y="83.7" width="2.46" height="62.7" fill="var(--up)"/>
<line x1="573.9" y1="85.0" x2="573.9" y2="115.1" stroke="var(--down)" class="wick"/>
<rect x="572.63" y="85.0" width="2.46" height="26.4" fill="var(--down)"/>
<line x1="577.8" y1="75.7" x2="577.8" y2="100.6" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="93.6" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="581.8" y1="88.6" x2="581.8" y2="189.2" stroke="var(--down)" class="wick"/>
<rect x="580.56" y="95.9" width="2.46" height="78.2" fill="var(--down)"/>
<line x1="585.8" y1="144.9" x2="585.8" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="159.4" width="2.46" height="35.5" fill="var(--down)"/>
<line x1="589.7" y1="205.2" x2="589.7" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="224.4" width="2.46" height="36.5" fill="var(--down)"/>
<line x1="593.7" y1="233.0" x2="593.7" y2="304.7" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="235.0" width="2.46" height="61.9" fill="var(--down)"/>
<line x1="597.7" y1="265.6" x2="597.7" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="278.8" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="601.6" y1="249.0" x2="601.6" y2="283.7" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="271.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="605.6" y1="279.1" x2="605.6" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="604.37" y="284.5" width="2.46" height="32.6" fill="var(--up)"/>
<line x1="609.6" y1="266.9" x2="609.6" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="283.5" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="613.5" y1="302.4" x2="613.5" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="317.4" width="2.46" height="6.0" fill="var(--down)"/>
<line x1="617.5" y1="315.9" x2="617.5" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="320.8" width="2.46" height="28.0" fill="var(--down)"/>
<line x1="621.5" y1="344.6" x2="621.5" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="354.7" width="2.46" height="19.7" fill="var(--down)"/>
<line x1="625.4" y1="362.5" x2="625.4" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="373.1" width="2.46" height="6.7" fill="var(--up)"/>
<line x1="629.4" y1="328.0" x2="629.4" y2="373.1" stroke="var(--up)" class="wick"/>
<rect x="628.18" y="330.9" width="2.46" height="36.3" fill="var(--up)"/>
<line x1="633.4" y1="325.2" x2="633.4" y2="383.0" stroke="var(--up)" class="wick"/>
<rect x="632.15" y="328.6" width="2.46" height="44.6" fill="var(--up)"/>
<line x1="637.3" y1="327.8" x2="637.3" y2="373.1" stroke="var(--down)" class="wick"/>
<rect x="636.11" y="351.4" width="2.46" height="15.5" fill="var(--down)"/>
<line x1="641.3" y1="356.0" x2="641.3" y2="386.1" stroke="var(--up)" class="wick"/>
<rect x="640.08" y="367.4" width="2.46" height="7.8" fill="var(--up)"/>
<line x1="645.3" y1="308.4" x2="645.3" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="322.3" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="649.2" y1="302.1" x2="649.2" y2="344.1" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="316.9" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="653.2" y1="313.8" x2="653.2" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="317.4" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="657.2" y1="268.5" x2="657.2" y2="330.6" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="300.6" width="2.46" height="23.8" fill="var(--down)"/>
<line x1="661.2" y1="287.6" x2="661.2" y2="307.6" stroke="var(--down)" class="wick"/>
<rect x="659.92" y="303.7" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="665.1" y1="281.4" x2="665.1" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="663.89" y="300.6" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="669.1" y1="272.1" x2="669.1" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="667.86" y="287.1" width="2.46" height="35.2" fill="var(--up)"/>
<line x1="673.1" y1="288.4" x2="673.1" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="289.2" width="2.46" height="34.7" fill="var(--down)"/>
<line x1="677.0" y1="293.6" x2="677.0" y2="323.1" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="313.0" width="2.46" height="7.3" fill="var(--up)"/>
<line x1="681.0" y1="304.5" x2="681.0" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="322.3" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="685.0" y1="334.0" x2="685.0" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="683.73" y="354.5" width="2.46" height="3.1" fill="var(--down)"/>
<line x1="688.9" y1="374.4" x2="688.9" y2="410.7" stroke="var(--down)" class="wick"/>
<rect x="687.70" y="377.8" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="692.9" y1="374.2" x2="692.9" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="383.0" width="2.46" height="10.9" fill="var(--down)"/>
<line x1="696.9" y1="366.9" x2="696.9" y2="388.9" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="379.9" width="2.46" height="1.3" fill="var(--down)"/>
<line x1="700.8" y1="373.9" x2="700.8" y2="407.1" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="378.8" width="2.46" height="19.7" fill="var(--down)"/>
<line x1="704.8" y1="393.6" x2="704.8" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="394.6" width="2.46" height="3.6" fill="var(--up)"/>
<line x1="708.8" y1="366.9" x2="708.8" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="707.54" y="378.1" width="2.46" height="22.8" fill="var(--up)"/>
<line x1="712.7" y1="361.2" x2="712.7" y2="390.0" stroke="var(--down)" class="wick"/>
<rect x="711.51" y="363.3" width="2.46" height="23.8" fill="var(--down)"/>
<line x1="716.7" y1="347.0" x2="716.7" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="715.47" y="355.2" width="2.46" height="28.5" fill="var(--up)"/>
<line x1="720.7" y1="294.4" x2="720.7" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="295.1" width="2.46" height="50.8" fill="var(--up)"/>
<line x1="724.6" y1="299.8" x2="724.6" y2="348.8" stroke="var(--down)" class="wick"/>
<rect x="723.41" y="307.1" width="2.46" height="38.3" fill="var(--down)"/>
<line x1="728.6" y1="321.8" x2="728.6" y2="351.9" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="324.9" width="2.46" height="22.8" fill="var(--down)"/>
<line x1="732.6" y1="338.9" x2="732.6" y2="366.7" stroke="var(--up)" class="wick"/>
<rect x="731.35" y="343.1" width="2.46" height="16.1" fill="var(--up)"/>
<line x1="736.5" y1="342.8" x2="736.5" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="735.31" y="349.6" width="2.46" height="37.8" fill="var(--down)"/>
<line x1="740.5" y1="389.7" x2="740.5" y2="417.2" stroke="var(--down)" class="wick"/>
<rect x="739.28" y="398.5" width="2.46" height="15.8" fill="var(--down)"/>
<line x1="744.5" y1="402.7" x2="744.5" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="409.4" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="748.4" y1="404.7" x2="748.4" y2="430.9" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="406.0" width="2.46" height="14.5" fill="var(--down)"/>
<line x1="752.4" y1="400.9" x2="752.4" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="751.19" y="412.0" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="756.4" y1="405.8" x2="756.4" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="755.15" y="419.0" width="2.46" height="8.0" fill="var(--down)"/>
<line x1="760.4" y1="418.2" x2="760.4" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="759.12" y="420.5" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="764.3" y1="400.1" x2="764.3" y2="425.5" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="412.5" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="768.3" y1="405.5" x2="768.3" y2="453.2" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="413.8" width="2.46" height="37.3" fill="var(--down)"/>
<line x1="772.3" y1="444.1" x2="772.3" y2="477.5" stroke="var(--down)" class="wick"/>
<rect x="771.03" y="457.6" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="776.2" y1="469.0" x2="776.2" y2="489.2" stroke="var(--down)" class="wick"/>
<rect x="774.99" y="471.1" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="780.2" y1="456.6" x2="780.2" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="778.96" y="467.4" width="2.46" height="13.2" fill="var(--down)"/>
<line x1="784.2" y1="458.9" x2="784.2" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="469.5" width="2.46" height="47.7" fill="var(--down)"/>
<line x1="788.1" y1="488.9" x2="788.1" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="498.0" width="2.46" height="10.9" fill="var(--up)"/>
<line x1="792.1" y1="492.1" x2="792.1" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="528.6" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="796.1" y1="499.3" x2="796.1" y2="541.8" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="512.8" width="2.46" height="22.3" fill="var(--up)"/>
<line x1="800.0" y1="501.4" x2="800.0" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="798.80" y="519.0" width="2.46" height="7.5" fill="var(--up)"/>
<line x1="804.0" y1="510.7" x2="804.0" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="527.5" width="2.46" height="2.1" fill="var(--down)"/>
<line x1="808.0" y1="500.3" x2="808.0" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="806.74" y="500.6" width="2.46" height="17.6" fill="var(--up)"/>
<line x1="811.9" y1="501.6" x2="811.9" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="810.71" y="505.3" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="815.9" y1="492.1" x2="815.9" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="509.9" width="2.46" height="15.5" fill="var(--up)"/>
<line x1="819.9" y1="501.6" x2="819.9" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="818.64" y="505.5" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="823.8" y1="455.0" x2="823.8" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="822.61" y="478.3" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="827.8" y1="472.6" x2="827.8" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="482.2" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="831.8" y1="451.4" x2="831.8" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="830.55" y="466.1" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="835.7" y1="464.1" x2="835.7" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="834.51" y="470.5" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="839.7" y1="465.9" x2="839.7" y2="491.5" stroke="var(--down)" class="wick"/>
<rect x="838.48" y="475.5" width="2.46" height="5.2" fill="var(--down)"/>
<line x1="843.7" y1="477.8" x2="843.7" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="842.45" y="481.9" width="2.46" height="22.0" fill="var(--down)"/>
<line x1="847.6" y1="494.9" x2="847.6" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="846.42" y="502.4" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="851.6" y1="495.4" x2="851.6" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="499.6" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="855.6" y1="515.6" x2="855.6" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="516.1" width="2.46" height="28.2" fill="var(--down)"/>
<line x1="859.6" y1="542.1" x2="859.6" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="545.4" width="2.46" height="32.6" fill="var(--down)"/>
<line x1="863.5" y1="549.6" x2="863.5" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="862.29" y="555.5" width="2.46" height="13.2" fill="var(--up)"/>
<line x1="867.5" y1="539.7" x2="867.5" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="866.26" y="553.2" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="871.5" y1="538.4" x2="871.5" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="553.2" width="2.46" height="14.5" fill="var(--down)"/>
<line x1="875.4" y1="553.5" x2="875.4" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="559.9" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="879.4" y1="535.3" x2="879.4" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="546.2" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="883.4" y1="562.0" x2="883.4" y2="585.6" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="564.1" width="2.46" height="8.8" fill="var(--down)"/>
<line x1="887.3" y1="551.4" x2="887.3" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="886.10" y="553.5" width="2.46" height="18.4" fill="var(--up)"/>
<line x1="891.3" y1="443.1" x2="891.3" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="890.07" y="444.4" width="2.46" height="75.4" fill="var(--up)"/>
<line x1="895.3" y1="423.6" x2="895.3" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="894.03" y="434.5" width="2.46" height="25.9" fill="var(--down)"/>
<line x1="899.2" y1="436.1" x2="899.2" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="453.7" width="2.46" height="16.1" fill="var(--down)"/>
<line x1="903.2" y1="476.0" x2="903.2" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="485.3" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="907.2" y1="471.8" x2="907.2" y2="516.7" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="493.9" width="2.46" height="11.4" fill="var(--down)"/>
<line x1="911.1" y1="465.9" x2="911.1" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="481.7" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="915.1" y1="477.0" x2="915.1" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="478.1" width="2.46" height="18.9" fill="var(--up)"/>
<line x1="919.1" y1="461.5" x2="919.1" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="463.0" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="923.0" y1="451.4" x2="923.0" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="921.81" y="456.0" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="927.0" y1="465.9" x2="927.0" y2="496.5" stroke="var(--up)" class="wick"/>
<rect x="925.78" y="476.5" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="931.0" y1="463.8" x2="931.0" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="929.75" y="470.5" width="2.46" height="45.9" fill="var(--down)"/>
<line x1="934.9" y1="485.8" x2="934.9" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="493.3" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="938.9" y1="497.0" x2="938.9" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="937.68" y="504.5" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="942.9" y1="440.7" x2="942.9" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="442.6" width="2.46" height="42.5" fill="var(--up)"/>
<line x1="946.8" y1="429.3" x2="946.8" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="945.62" y="435.1" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="950.8" y1="426.0" x2="950.8" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="949.59" y="436.9" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="954.8" y1="440.0" x2="954.8" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="442.6" width="2.46" height="11.9" fill="var(--up)"/>
<line x1="958.8" y1="414.8" x2="958.8" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="433.8" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="962.7" y1="433.8" x2="962.7" y2="486.6" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="435.1" width="2.46" height="35.2" fill="var(--down)"/>
<line x1="966.7" y1="446.7" x2="966.7" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="965.46" y="451.6" width="2.46" height="15.3" fill="var(--down)"/>
<line x1="970.7" y1="443.3" x2="970.7" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="451.6" width="2.46" height="2.3" fill="var(--down)"/>
<line x1="974.6" y1="427.3" x2="974.6" y2="467.4" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="447.5" width="2.46" height="8.0" fill="var(--up)"/>
<line x1="978.6" y1="431.7" x2="978.6" y2="456.3" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="445.2" width="2.46" height="6.7" fill="var(--down)"/>
<line x1="982.6" y1="436.3" x2="982.6" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="981.33" y="445.7" width="2.46" height="4.4" fill="var(--down)"/>
<line x1="986.5" y1="431.4" x2="986.5" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="985.30" y="444.6" width="2.46" height="27.2" fill="var(--up)"/>
<line x1="990.5" y1="380.6" x2="990.5" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="989.27" y="424.2" width="2.46" height="29.0" fill="var(--up)"/>
<line x1="994.5" y1="418.0" x2="994.5" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="424.7" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="998.4" y1="407.6" x2="998.4" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="997.20" y="419.0" width="2.46" height="10.9" fill="var(--down)"/>
<line x1="1002.4" y1="393.1" x2="1002.4" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="394.1" width="2.46" height="45.9" fill="var(--down)"/>
<line x1="1006.4" y1="399.6" x2="1006.4" y2="436.9" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="403.4" width="2.46" height="31.1" fill="var(--up)"/>
<line x1="1010.3" y1="393.3" x2="1010.3" y2="420.3" stroke="var(--up)" class="wick"/>
<rect x="1009.11" y="399.3" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="1014.3" y1="379.3" x2="1014.3" y2="404.0" stroke="var(--down)" class="wick"/>
<rect x="1013.07" y="395.2" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="1018.3" y1="403.7" x2="1018.3" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="406.8" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="1022.2" y1="392.8" x2="1022.2" y2="431.4" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="409.7" width="2.46" height="6.0" fill="var(--down)"/>
<line x1="1026.2" y1="407.3" x2="1026.2" y2="451.1" stroke="var(--down)" class="wick"/>
<rect x="1024.98" y="415.4" width="2.46" height="13.0" fill="var(--down)"/>
<line x1="1030.2" y1="409.1" x2="1030.2" y2="449.0" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="418.2" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="1034.1" y1="416.4" x2="1034.1" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="1032.91" y="421.3" width="2.46" height="21.5" fill="var(--down)"/>
<line x1="1038.1" y1="420.8" x2="1038.1" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="1036.88" y="431.4" width="2.46" height="33.7" fill="var(--down)"/>
<line x1="1042.1" y1="448.8" x2="1042.1" y2="483.0" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="454.0" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="1046.0" y1="473.7" x2="1046.0" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="480.6" width="2.46" height="57.0" fill="var(--down)"/>
<line x1="1050.0" y1="528.8" x2="1050.0" y2="550.3" stroke="var(--down)" class="wick"/>
<rect x="1048.79" y="533.0" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="60" y1="420.7" x2="1052" y2="420.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="424.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$55 R1</text>
<text x="1058" y="436.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="362.4" x2="1052" y2="362.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="365.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$57 R2</text>
<text x="1058" y="377.9" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="273.1" x2="1052" y2="273.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="276.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$61 R3</text>
<text x="1058" y="288.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="584.9" x2="1052" y2="584.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="578.9" font-size="11.5" fill="var(--support)" font-weight="600">$49 S1</text>
<text x="1058" y="590.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="539.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="531.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $50 (2026-09-17)</text>
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
| ------ | ------ | ----------- | ------ |
| R3 | $61 | 3 | 2025-11-13·2026-04-27·2026-05-19 고점대 — 1년 최고($68.24)와 현재가 사이의 중간 저항 |
| R2 | $57 | 5 | 2025-10-07·10-20, 2026-01-30, 2026-08-26·09-03 고점대 — 5회 터치로 이 구간에서 가장 두껍다 |
| R1 | $55 | 5 | 2025-12-30, 2026-06-04·06-30·07-23·08-14 고점대 — 2026년 여름 내내 눌린 자리 |
| **현재가** | **$50.35** (2026-09-17 종가) | — | R1($55)과 S1($49) 사이. R1까지 +9.2%, S1까지 −2.7%로 **지지선에 훨씬 가깝다** |
| S1 | $49 | 3 | 2026-01-15·07-10·07-20 저점대 — 1년 최저($47.94)와 2%밖에 떨어져 있지 않다 |
| 참고선 | $68.24 / $47.94 | — | 최근 1년 최고·최저. 최고가는 1년 전 구간이라 근시일 저항으로 보지 않고, 최저가는 S1과 사실상 같은 자리다 |

> 검출된 저항이 3개(R1~R3)인데 지지는 1개(S1)뿐이다. **아래쪽에 스윙 저점 자체가 드물기 때문**이며, 현재가가 1년 저점권($47.94)에 붙어 있어 그 아래로는 이 1년 창 안에 표본이 없다는 뜻이다. 더 아래 구조는 [주봉·5년 차트](./10_technical_weekly.md)에서 본다.

---

## 3. 관측된 특이 구간 — 2026-09-16 회사 고유 악재 없는 하락

- 2026년 9월 중순 사흘 만에 $53.12(9월 15일) → $50.41(16일) → $50.35(17일)로 밀렸고, 9월 16일 하루 낙폭이 **−3.8%**였다. 같은 기간 **EDGAR에 8-K 제출이 없었고 회사 발표도 없었다** — 경위는 [최근 뉴스 / 이슈](./08_news.md) 로그 참고.
- 9월 초 $55 부근에서 2026-09-18 종가 $50.00까지 약 열흘간 **−10.4%**다. 동종 애팔래치아 E&P(Antero·Range)가 함께 빠졌다는 점에서 종목 고유 사건이 아니라 **섹터 단위 디레이팅**으로 읽는 편이 사실에 가깝다.
- 이 하락으로 주가가 R1($55) 아래에서 S1($49) 쪽으로 내려붙었다. **다만 거래 레짐이 재설정됐다고 볼 근거(거래량 급증·갭)는 확인되지 않아, 기존 스윙 레벨을 참고선으로 격하하지 않고 그대로 뒀다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-09-19~2026-09-17. 수집 시점: 2026-09-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py EQT --name "EQT Corporation" --close-on 2026-09-17 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **마지막 봉이 2026-09-17이다.** 9월 18일 세션의 종가가 원자료에 아직 채워지지 않아 `--close-on 2026-09-17`로 고정했다 — 위 데이터 출처 블록 참고. 이 문서의 현재가($50.35)를 다른 문서의 기준 종가($50.00)로 옮겨 적지 말 것.
    - 기간 내 배당이 4회 있었으나 **원주가(배당 미반영)**라 차트에 반영되지 않았다. 배당수익률이 연 1.3% 수준이라 레벨 해석에 미치는 영향은 작다.
    - 3절의 하락 구간은 갭 없이 연속 하락이라 가격 연속성이 깨지지 않았다 — 소급 조정 대상이 아니다.

---

*작성일: 2026-09-19*
