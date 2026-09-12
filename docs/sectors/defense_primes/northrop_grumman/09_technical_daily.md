# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트를 볼 때 주의할 점
**현재가 아래에 유효한 지지 클러스터가 하나도 없다.** 최근 1년 중 가장 낮은 구간에 있어, 아래쪽 스윙 저점들이 ±2.5% 안에 묶이지 않았기 때문이다(터치 2회 미만). 지지가 "없다"는 뜻이 아니라 **이 방법론으로는 식별되지 않는다**는 뜻이며, 하방 참고선으로는 최근 1년 최저 $479.02를 쓰는 편이 낫다.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$518.97**은 [핵심 지표](./04_metrics.md) A.2. 밸류에이션 지표와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 현재가와 일치한다.
- **최근 1년 범위**: 최고 $774.00 · 최저 $479.02 · 일평균 거래량 854,612주.

:::

---

## 1. 차트 — 최근 1년 일봉 (2025-09-12 ~ 2026-09-11)

<div class="noc-chart">
<style>
.noc-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.noc-chart svg { width:100%; height:auto; display:block; }
.noc-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.noc-chart .title { fill: var(--ink); font-weight:600; }
.noc-chart .grid { stroke: var(--grid); stroke-width:1; }
.noc-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="노스롭 그루먼(NOC) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">노스롭 그루먼 (NOC) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-12 ~ 2026-09-11 · 마지막 종가 $518.97 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="571.7" x2="1052" y2="571.7" class="grid"/>
<text x="52" y="575.7" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="481.2" x2="1052" y2="481.2" class="grid"/>
<text x="52" y="485.2" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="390.8" x2="1052" y2="390.8" class="grid"/>
<text x="52" y="394.8" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="300.3" x2="1052" y2="300.3" class="grid"/>
<text x="52" y="304.3" font-size="11" text-anchor="end" fill="var(--muted)">650</text>
<line x1="60" y1="209.8" x2="1052" y2="209.8" class="grid"/>
<text x="52" y="213.8" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="119.3" x2="1052" y2="119.3" class="grid"/>
<text x="52" y="123.3" font-size="11" text-anchor="end" fill="var(--muted)">750</text>
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
<line x1="62.0" y1="421.3" x2="62.0" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="422.7" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="65.9" y1="433.3" x2="65.9" y2="443.0" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="436.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="413.9" x2="69.9" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="428.1" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="73.8" y1="417.9" x2="73.8" y2="433.5" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="428.6" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="77.8" y1="432.4" x2="77.8" y2="448.1" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="438.3" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="81.7" y1="433.9" x2="81.7" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="439.6" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="85.7" y1="431.2" x2="85.7" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="433.9" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="89.6" y1="425.7" x2="89.6" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="432.2" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="93.6" y1="409.6" x2="93.6" y2="432.4" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="415.6" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="97.5" y1="402.1" x2="97.5" y2="422.4" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="408.9" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="101.5" y1="399.9" x2="101.5" y2="414.6" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="400.7" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="105.5" y1="383.3" x2="105.5" y2="406.1" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="393.8" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="109.4" y1="372.4" x2="109.4" y2="403.2" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="373.9" width="2.45" height="29.4" fill="var(--up)"/>
<line x1="113.4" y1="371.1" x2="113.4" y2="385.3" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="377.7" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="117.3" y1="377.6" x2="117.3" y2="387.2" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="381.7" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="121.3" y1="371.5" x2="121.3" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="373.5" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="125.2" y1="355.1" x2="125.2" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="357.2" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="129.2" y1="340.4" x2="129.2" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="349.4" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="133.1" y1="321.0" x2="133.1" y2="344.5" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="322.1" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="137.1" y1="316.8" x2="137.1" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="322.0" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="141.0" y1="327.0" x2="141.0" y2="355.6" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="330.4" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="145.0" y1="347.2" x2="145.0" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="354.6" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="148.9" y1="341.2" x2="148.9" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="342.0" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="152.9" y1="341.8" x2="152.9" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="345.4" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="156.8" y1="369.4" x2="156.8" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="370.9" width="2.45" height="21.8" fill="var(--down)"/>
<line x1="160.8" y1="387.8" x2="160.8" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="396.2" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="164.7" y1="385.5" x2="164.7" y2="397.6" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="387.1" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="168.7" y1="381.9" x2="168.7" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="391.9" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="172.6" y1="380.0" x2="172.6" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="396.1" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="176.6" y1="373.0" x2="176.6" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="380.4" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="180.5" y1="375.4" x2="180.5" y2="396.0" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="379.3" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="184.5" y1="380.5" x2="184.5" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="381.9" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="188.4" y1="392.7" x2="188.4" y2="406.6" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="399.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="192.4" y1="401.2" x2="192.4" y2="422.4" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="408.9" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="196.4" y1="405.7" x2="196.4" y2="431.0" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="416.2" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="200.3" y1="415.0" x2="200.3" y2="434.5" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="420.7" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="204.3" y1="424.8" x2="204.3" y2="442.0" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="426.2" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="208.2" y1="427.7" x2="208.2" y2="447.9" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="432.1" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="212.2" y1="427.8" x2="212.2" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="440.0" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="216.1" y1="430.5" x2="216.1" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="441.5" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="220.1" y1="441.5" x2="220.1" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="441.5" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="224.0" y1="450.4" x2="224.0" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="454.5" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="228.0" y1="443.6" x2="228.0" y2="465.0" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="450.9" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="231.9" y1="446.6" x2="231.9" y2="466.0" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="453.8" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="235.9" y1="457.0" x2="235.9" y2="468.9" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="457.3" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="239.8" y1="459.5" x2="239.8" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="466.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="243.8" y1="457.6" x2="243.8" y2="469.9" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="457.7" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="247.7" y1="439.1" x2="247.7" y2="455.6" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="450.9" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="251.7" y1="450.1" x2="251.7" y2="467.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="454.1" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="255.6" y1="439.1" x2="255.6" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="443.5" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="259.6" y1="442.0" x2="259.6" y2="457.6" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="448.2" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="263.5" y1="451.8" x2="263.5" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="453.1" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="267.5" y1="436.9" x2="267.5" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="446.1" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="271.4" y1="422.2" x2="271.4" y2="450.3" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="445.8" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="275.4" y1="438.4" x2="275.4" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="441.0" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="279.3" y1="447.8" x2="279.3" y2="492.7" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="449.2" width="2.45" height="40.2" fill="var(--down)"/>
<line x1="283.3" y1="478.9" x2="283.3" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="486.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="287.3" y1="473.1" x2="287.3" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="475.2" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="291.2" y1="463.1" x2="291.2" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="475.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="295.2" y1="477.1" x2="295.2" y2="491.8" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="478.5" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="299.1" y1="474.7" x2="299.1" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="474.8" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="303.1" y1="467.2" x2="303.1" y2="480.8" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="473.8" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="307.0" y1="465.7" x2="307.0" y2="487.5" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="471.5" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="311.0" y1="447.5" x2="311.0" y2="468.7" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="463.1" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="314.9" y1="442.2" x2="314.9" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="445.5" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="318.9" y1="434.6" x2="318.9" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="434.6" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="322.8" y1="437.4" x2="322.8" y2="452.6" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="438.7" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="326.8" y1="440.9" x2="326.8" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="455.6" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="330.7" y1="445.2" x2="330.7" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="455.9" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="334.7" y1="443.3" x2="334.7" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="447.8" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="338.6" y1="417.4" x2="338.6" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="418.5" width="2.45" height="28.5" fill="var(--up)"/>
<line x1="342.6" y1="416.1" x2="342.6" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="417.4" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="346.5" y1="413.8" x2="346.5" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="422.7" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="350.5" y1="422.0" x2="350.5" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="422.0" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="354.4" y1="425.6" x2="354.4" y2="432.6" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="430.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="358.4" y1="426.7" x2="358.4" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="429.0" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="362.3" y1="432.4" x2="362.3" y2="445.0" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="435.6" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="366.3" y1="416.4" x2="366.3" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="416.7" width="2.45" height="29.1" fill="var(--up)"/>
<line x1="370.2" y1="370.2" x2="370.2" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="370.3" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="374.2" y1="356.0" x2="374.2" y2="378.4" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="364.4" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="378.2" y1="358.2" x2="378.2" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="361.0" width="2.45" height="71.3" fill="var(--down)"/>
<line x1="382.1" y1="320.5" x2="382.1" y2="416.2" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="358.4" width="2.45" height="49.0" fill="var(--down)"/>
<line x1="386.1" y1="355.0" x2="386.1" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="356.7" width="2.45" height="50.9" fill="var(--up)"/>
<line x1="390.0" y1="326.1" x2="390.0" y2="348.5" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="337.7" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="394.0" y1="318.8" x2="394.0" y2="355.2" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="319.9" width="2.45" height="24.7" fill="var(--down)"/>
<line x1="397.9" y1="292.1" x2="397.9" y2="345.8" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="294.6" width="2.45" height="50.9" fill="var(--up)"/>
<line x1="401.9" y1="285.1" x2="401.9" y2="331.1" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="291.9" width="2.45" height="25.8" fill="var(--up)"/>
<line x1="405.8" y1="264.7" x2="405.8" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="269.7" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="409.8" y1="255.5" x2="409.8" y2="294.8" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="271.5" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="413.7" y1="264.8" x2="413.7" y2="291.9" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="274.7" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="417.7" y1="262.1" x2="417.7" y2="282.2" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="263.3" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="421.6" y1="250.9" x2="421.6" y2="266.8" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="256.5" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="425.6" y1="261.5" x2="425.6" y2="283.8" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="264.1" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="429.5" y1="240.6" x2="429.5" y2="325.6" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="248.3" width="2.45" height="52.6" fill="var(--up)"/>
<line x1="433.5" y1="226.6" x2="433.5" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="229.5" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="437.4" y1="199.9" x2="437.4" y2="235.1" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="218.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="441.4" y1="214.0" x2="441.4" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="223.8" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="445.3" y1="227.1" x2="445.3" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="236.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="449.3" y1="195.9" x2="449.3" y2="236.0" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="200.8" width="2.45" height="19.5" fill="var(--up)"/>
<line x1="453.2" y1="192.8" x2="453.2" y2="250.7" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="199.4" width="2.45" height="29.0" fill="var(--down)"/>
<line x1="457.2" y1="202.2" x2="457.2" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="216.1" width="2.45" height="29.4" fill="var(--up)"/>
<line x1="461.1" y1="188.3" x2="461.1" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="193.3" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="465.1" y1="181.6" x2="465.1" y2="213.4" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="187.8" width="2.45" height="25.6" fill="var(--down)"/>
<line x1="469.1" y1="205.6" x2="469.1" y2="238.1" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="205.6" width="2.45" height="31.3" fill="var(--down)"/>
<line x1="473.0" y1="231.3" x2="473.0" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="241.8" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="477.0" y1="215.7" x2="477.0" y2="246.1" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="218.7" width="2.45" height="25.9" fill="var(--up)"/>
<line x1="480.9" y1="193.5" x2="480.9" y2="216.6" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="205.2" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="484.9" y1="195.3" x2="484.9" y2="212.1" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="205.2" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="488.8" y1="163.6" x2="488.8" y2="205.3" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="164.9" width="2.45" height="26.9" fill="var(--up)"/>
<line x1="492.8" y1="127.4" x2="492.8" y2="160.5" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="143.1" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="496.7" y1="141.5" x2="496.7" y2="177.2" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="146.5" width="2.45" height="20.7" fill="var(--down)"/>
<line x1="500.7" y1="152.9" x2="500.7" y2="174.7" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="163.9" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="504.6" y1="147.2" x2="504.6" y2="190.9" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="159.6" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="508.6" y1="158.2" x2="508.6" y2="226.0" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="160.2" width="2.45" height="43.0" fill="var(--down)"/>
<line x1="512.5" y1="184.8" x2="512.5" y2="209.5" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="190.1" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="516.5" y1="160.4" x2="516.5" y2="183.0" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="165.7" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="520.4" y1="86.4" x2="520.4" y2="137.8" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="86.7" width="2.45" height="41.7" fill="var(--up)"/>
<line x1="524.4" y1="75.9" x2="524.4" y2="115.9" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="85.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="528.3" y1="104.4" x2="528.3" y2="141.5" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="105.8" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="532.3" y1="115.8" x2="532.3" y2="147.6" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="120.0" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="536.2" y1="103.6" x2="536.2" y2="141.0" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="108.2" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="540.2" y1="91.1" x2="540.2" y2="129.2" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="95.8" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="544.1" y1="128.4" x2="544.1" y2="155.2" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="141.0" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="548.1" y1="133.6" x2="548.1" y2="158.1" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="149.8" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="552.0" y1="126.2" x2="552.0" y2="161.7" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="143.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="556.0" y1="125.0" x2="556.0" y2="158.5" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="137.5" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="560.0" y1="142.1" x2="560.0" y2="162.5" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="144.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="563.9" y1="143.1" x2="563.9" y2="172.2" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="147.5" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="567.9" y1="153.4" x2="567.9" y2="173.6" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="155.5" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="571.8" y1="159.1" x2="571.8" y2="197.1" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="175.3" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="575.8" y1="178.4" x2="575.8" y2="208.0" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="183.2" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="579.7" y1="197.6" x2="579.7" y2="248.3" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="199.2" width="2.45" height="46.8" fill="var(--down)"/>
<line x1="583.7" y1="229.2" x2="583.7" y2="267.4" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="242.1" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="587.6" y1="222.9" x2="587.6" y2="242.7" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="225.7" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="591.6" y1="215.4" x2="591.6" y2="232.5" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="224.3" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="595.5" y1="220.9" x2="595.5" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="223.8" width="2.45" height="24.0" fill="var(--down)"/>
<line x1="599.5" y1="222.5" x2="599.5" y2="275.1" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="229.6" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="603.4" y1="236.0" x2="603.4" y2="269.0" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="241.9" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="607.4" y1="205.9" x2="607.4" y2="237.4" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="215.2" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="611.3" y1="194.3" x2="611.3" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="205.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="615.3" y1="204.3" x2="615.3" y2="231.6" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="208.0" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="619.2" y1="215.6" x2="619.2" y2="234.4" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="227.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="623.2" y1="226.5" x2="623.2" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="232.5" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="627.1" y1="212.5" x2="627.1" y2="237.0" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="226.9" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="631.1" y1="233.3" x2="631.1" y2="273.1" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="236.3" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="635.0" y1="239.0" x2="635.0" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="243.6" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="639.0" y1="243.0" x2="639.0" y2="255.9" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="245.8" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="642.9" y1="240.8" x2="642.9" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="244.8" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="646.9" y1="245.3" x2="646.9" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="247.6" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="650.9" y1="250.1" x2="650.9" y2="276.7" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="262.2" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="654.8" y1="258.1" x2="654.8" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="269.5" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="658.8" y1="294.9" x2="658.8" y2="372.0" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="318.4" width="2.45" height="52.2" fill="var(--down)"/>
<line x1="662.7" y1="363.6" x2="662.7" y2="420.6" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="370.7" width="2.45" height="38.9" fill="var(--down)"/>
<line x1="666.7" y1="397.1" x2="666.7" y2="421.1" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="404.2" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="670.6" y1="421.9" x2="670.6" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="422.8" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="674.6" y1="412.0" x2="674.6" y2="445.8" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="432.4" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="678.5" y1="421.5" x2="678.5" y2="443.9" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="423.4" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="682.5" y1="423.1" x2="682.5" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="430.6" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="686.4" y1="425.6" x2="686.4" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="427.9" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="690.4" y1="425.4" x2="690.4" y2="448.5" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="429.2" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="694.3" y1="431.5" x2="694.3" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="449.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="698.3" y1="444.1" x2="698.3" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="445.0" width="2.45" height="20.7" fill="var(--down)"/>
<line x1="702.2" y1="462.0" x2="702.2" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="463.9" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="706.2" y1="460.8" x2="706.2" y2="484.3" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="464.5" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="710.1" y1="472.1" x2="710.1" y2="491.7" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="472.2" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="714.1" y1="473.5" x2="714.1" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="484.5" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="718.0" y1="464.1" x2="718.0" y2="487.4" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="466.2" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="722.0" y1="473.4" x2="722.0" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="473.4" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="725.9" y1="470.4" x2="725.9" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="474.8" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="729.9" y1="476.2" x2="729.9" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="483.6" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="733.8" y1="476.3" x2="733.8" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="481.2" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="737.8" y1="468.4" x2="737.8" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="469.8" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="741.8" y1="470.3" x2="741.8" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="470.3" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="745.7" y1="470.5" x2="745.7" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="474.7" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="749.7" y1="467.3" x2="749.7" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="471.1" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="753.6" y1="465.0" x2="753.6" y2="480.6" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="467.3" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="757.6" y1="471.3" x2="757.6" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="477.0" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="761.5" y1="462.1" x2="761.5" y2="478.8" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="464.4" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="765.5" y1="456.0" x2="765.5" y2="479.4" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="456.5" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="769.4" y1="463.3" x2="769.4" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="463.3" width="2.45" height="37.5" fill="var(--down)"/>
<line x1="773.4" y1="502.2" x2="773.4" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="505.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="777.3" y1="502.2" x2="777.3" y2="525.2" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="511.0" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="781.3" y1="489.5" x2="781.3" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="490.0" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="785.2" y1="477.7" x2="785.2" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="481.2" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="789.2" y1="486.9" x2="789.2" y2="514.7" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="495.7" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="793.1" y1="483.5" x2="793.1" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="483.6" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="797.1" y1="476.0" x2="797.1" y2="497.5" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="476.0" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="801.0" y1="463.7" x2="801.0" y2="496.8" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="476.7" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="805.0" y1="473.9" x2="805.0" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="475.8" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="808.9" y1="488.3" x2="808.9" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="490.8" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="812.9" y1="473.6" x2="812.9" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="479.0" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="816.8" y1="465.3" x2="816.8" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="481.0" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="820.8" y1="474.9" x2="820.8" y2="543.9" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="477.4" width="2.45" height="55.4" fill="var(--down)"/>
<line x1="824.7" y1="542.6" x2="824.7" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="543.5" width="2.45" height="14.9" fill="var(--down)"/>
<line x1="828.7" y1="536.2" x2="828.7" y2="554.6" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="537.2" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="832.7" y1="540.7" x2="832.7" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="544.3" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="836.6" y1="549.2" x2="836.6" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="569.9" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="840.6" y1="558.5" x2="840.6" y2="575.1" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="568.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="844.5" y1="564.8" x2="844.5" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="568.1" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="848.5" y1="554.4" x2="848.5" y2="580.6" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="554.9" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="852.4" y1="525.9" x2="852.4" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="535.6" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="856.4" y1="483.0" x2="856.4" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="483.0" width="2.45" height="38.2" fill="var(--up)"/>
<line x1="860.3" y1="483.9" x2="860.3" y2="504.1" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="485.3" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="864.3" y1="476.5" x2="864.3" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="479.4" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="868.2" y1="484.6" x2="868.2" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="488.4" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="872.2" y1="500.0" x2="872.2" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="503.8" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="876.1" y1="497.4" x2="876.1" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="500.0" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="880.1" y1="489.3" x2="880.1" y2="505.0" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="496.0" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="884.0" y1="491.9" x2="884.0" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="505.0" width="2.45" height="14.9" fill="var(--down)"/>
<line x1="888.0" y1="506.7" x2="888.0" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="514.0" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="891.9" y1="518.4" x2="891.9" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="525.0" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="895.9" y1="501.2" x2="895.9" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="526.3" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="899.8" y1="511.9" x2="899.8" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="528.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="903.8" y1="546.1" x2="903.8" y2="609.7" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="549.5" width="2.45" height="40.3" fill="var(--up)"/>
<line x1="907.7" y1="507.2" x2="907.7" y2="538.3" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="526.0" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="911.7" y1="487.1" x2="911.7" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="504.4" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="915.6" y1="490.9" x2="915.6" y2="509.4" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="495.3" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="919.6" y1="477.6" x2="919.6" y2="495.3" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="485.6" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="923.6" y1="453.3" x2="923.6" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="466.8" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="927.5" y1="472.3" x2="927.5" y2="509.8" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="473.4" width="2.45" height="34.9" fill="var(--down)"/>
<line x1="931.5" y1="508.3" x2="931.5" y2="535.9" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="508.7" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="935.4" y1="489.9" x2="935.4" y2="517.3" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="494.8" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="939.4" y1="467.5" x2="939.4" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="484.0" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="943.3" y1="472.2" x2="943.3" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="478.4" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="947.3" y1="467.5" x2="947.3" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="467.7" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="951.2" y1="447.4" x2="951.2" y2="465.0" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="449.1" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="955.2" y1="440.1" x2="955.2" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="442.2" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="959.1" y1="424.1" x2="959.1" y2="439.4" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="430.8" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="963.1" y1="425.6" x2="963.1" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="434.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="967.0" y1="426.9" x2="967.0" y2="445.9" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="431.8" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="971.0" y1="427.1" x2="971.0" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="429.3" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="974.9" y1="415.4" x2="974.9" y2="437.0" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="416.3" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="978.9" y1="418.0" x2="978.9" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="423.6" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="982.8" y1="400.7" x2="982.8" y2="433.8" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="410.4" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="986.8" y1="406.1" x2="986.8" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="420.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="990.7" y1="416.1" x2="990.7" y2="456.9" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="425.6" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="994.7" y1="449.6" x2="994.7" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="452.0" width="2.45" height="27.3" fill="var(--down)"/>
<line x1="998.6" y1="475.8" x2="998.6" y2="487.6" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="475.8" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="1002.6" y1="481.6" x2="1002.6" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="485.2" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="1006.5" y1="474.7" x2="1006.5" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="481.3" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="1010.5" y1="484.3" x2="1010.5" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="486.6" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="1014.5" y1="485.4" x2="1014.5" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="486.0" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="1018.4" y1="497.0" x2="1018.4" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="499.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1022.4" y1="481.7" x2="1022.4" y2="517.2" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="493.7" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="1026.3" y1="506.8" x2="1026.3" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="508.7" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="1030.3" y1="508.9" x2="1030.3" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="518.9" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="1034.2" y1="525.5" x2="1034.2" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="525.5" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="1038.2" y1="528.9" x2="1038.2" y2="544.5" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="538.1" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="1042.1" y1="523.0" x2="1042.1" y2="543.6" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="532.5" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="1046.1" y1="529.4" x2="1046.1" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="537.4" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="1050.0" y1="530.1" x2="1050.0" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="531.9" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="60" y1="462.4" x2="1052" y2="462.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="465.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$560 R1</text>
<text x="1058" y="477.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="412.2" x2="1052" y2="412.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="415.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$588 R2</text>
<text x="1058" y="427.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="188.0" x2="1052" y2="188.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="191.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$712 R3</text>
<text x="1058" y="203.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="537.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="529.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $519 (2026-09-11)</text>
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

각 레벨은 "전후 일정 기간 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $712 | 2 | 2026-02-09·2026-04-02 — 2026년 상반기 고점대. 3월 최고 $774.00 직전·직후의 두 스윙 |
| R2 | $588 | 3 | 2025-11-26·2025-12-24·2026-08-18 — 2025년 말 박스권 상단이자, 2026-08월 반등이 멈춘 자리 |
| R1 | $560 | 4 | 2026-05-29·2026-06-11·2026-07-07·2026-07-28 — 6·7월 반등 시도가 네 번 막힌 대역. 현재가에서 가장 가까운 저항 |
| **현재가** | **$518.97** (2026-09-11 종가) | — | 기간 내 하단 지지 클러스터 없음(위 `::: warning` 참고) — 가장 가까운 레벨은 위쪽 R1 $560 |

---

## 3. 관측된 특이 구간

### 2026-04-21 — 2026 Q1 실적 발표 후 갭다운

- 매출·EPS는 컨센서스를 웃돌았으나 **FY2026 CapEx를 $1.85B로 상향**하고 가이던스를 유지하는 데 그친 것이 계기였다([최근 뉴스 / 이슈](./08_news.md)).
- 종가 기준 전일 대비 **−6.98%** ($656.98 → $611.13), 거래량은 평소(일 85만 주 내외) 대비 약 1.9배.
- 이 갭 이후 $650 위의 가격대는 한 번도 회복되지 않았다 — 2026년 상반기의 $712 대역(R3)이 **현재 레짐에서는 유효한 저항이라기보다 이전 레짐의 잔상**에 가깝다.

### 2026-06-18 — 지정학 프리미엄 축소에 따른 섹터 동반 급락

- 미·이란 잠정 합의 보도로 방산 섹터 전반의 위험 프리미엄이 축소된 것이 계기로 전해진다(**2차 출처 기반, 1차 확인 못 함** — [최근 뉴스 / 이슈](./08_news.md)).
- 종가 기준 전일 대비 **−5.21%** ($550.15 → $521.50), 거래량은 평소 대비 약 2.8배인 **240만 주**.
- 이후 6영업일간 추가 하락해 6/29 $496.02로 최근 1년 저점권에 닿았다. **이 구간 이후 $560(R1)이 네 차례 저항으로 작동**했고, 현재가는 그 아래에 머물러 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-12~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `uv run python scripts/gen_technical_chart.py NOC --name "노스롭 그루먼" --close-on 2026-09-11 --emit all`

- **한계**: 위 `::: warning`대로 하단 클러스터가 식별되지 않아 **지지 레벨이 0개**다. 터치 2회 기준을 완화(`--min-touches 1`)하면 레벨이 나오지만 통계적 의미가 없어 그렇게 하지 않았다. 또한 원주가 기준이라 기간 내 배당 4회가 반영돼 있지 않다 — 배당 재투자 기준으로 보면 실제 총수익률은 표시된 가격 하락폭보다 약 1.9%p 덜 나쁘다.

---

*작성일: 2026-09-12*
