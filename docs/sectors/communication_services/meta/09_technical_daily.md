# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$648.03**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치한다**. 세 문서 모두 배당 미반영 원주가를 쓴다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-12 ~ 2026-09-11)

<style>
.meta-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .meta-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.meta-chart svg { width:100%; height:auto; display:block; }
.meta-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.meta-chart .title { fill: var(--ink); font-weight:600; }
.meta-chart .grid { stroke: var(--grid); stroke-width:1; }
.meta-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="meta-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Meta Platforms(META) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Meta Platforms (META) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-12 ~ 2026-09-11 · 마지막 종가 $648.03 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="547.4" x2="1052" y2="547.4" class="grid"/>
<text x="52" y="551.4" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="449.1" x2="1052" y2="449.1" class="grid"/>
<text x="52" y="453.1" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="350.8" x2="1052" y2="350.8" class="grid"/>
<text x="52" y="354.8" font-size="11" text-anchor="end" fill="var(--muted)">650</text>
<line x1="60" y1="252.6" x2="1052" y2="252.6" class="grid"/>
<text x="52" y="256.6" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="154.3" x2="1052" y2="154.3" class="grid"/>
<text x="52" y="158.3" font-size="11" text-anchor="end" fill="var(--muted)">750</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">800</text>
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
<line x1="62.0" y1="139.4" x2="62.0" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="143.3" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="65.9" y1="107.0" x2="65.9" y2="150.4" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="125.4" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="69.9" y1="92.6" x2="69.9" y2="124.6" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="97.3" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="73.8" y1="88.8" x2="73.8" y2="122.2" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="95.3" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="77.8" y1="78.1" x2="77.8" y2="108.4" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="93.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="81.7" y1="74.1" x2="81.7" y2="116.6" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="82.7" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="85.7" y1="84.0" x2="85.7" y2="125.8" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="91.7" width="2.45" height="32.8" fill="var(--down)"/>
<line x1="89.6" y1="113.8" x2="89.6" y2="152.2" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="116.4" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="93.6" y1="132.4" x2="93.6" y2="149.3" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="133.3" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="97.5" y1="141.0" x2="97.5" y2="165.0" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="147.5" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="101.5" y1="150.5" x2="101.5" y2="179.1" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="154.3" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="105.5" y1="152.7" x2="105.5" y2="175.6" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="156.8" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="109.4" y1="168.1" x2="109.4" y2="200.9" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="169.5" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="113.4" y1="209.6" x2="113.4" y2="232.5" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="210.3" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="117.3" y1="198.0" x2="117.3" y2="216.9" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="199.4" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="121.3" y1="191.6" x2="121.3" y2="232.5" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="194.3" width="2.45" height="37.5" fill="var(--down)"/>
<line x1="125.2" y1="219.4" x2="125.2" y2="271.2" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="221.8" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="129.2" y1="216.2" x2="129.2" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="217.7" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="133.1" y1="213.9" x2="133.1" y2="237.2" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="217.5" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="137.1" y1="186.7" x2="137.1" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="186.7" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="141.0" y1="183.2" x2="141.0" y2="243.7" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="191.8" width="2.45" height="50.4" fill="var(--down)"/>
<line x1="145.0" y1="213.4" x2="145.0" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="221.7" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="148.9" y1="222.0" x2="148.9" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="235.5" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="152.9" y1="205.6" x2="152.9" y2="233.9" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="218.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="156.8" y1="202.5" x2="156.8" y2="244.9" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="218.1" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="160.8" y1="216.1" x2="160.8" y2="240.5" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="219.3" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="164.7" y1="186.2" x2="164.7" y2="212.9" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="189.3" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="168.7" y1="176.9" x2="168.7" y2="196.0" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="181.8" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="172.6" y1="172.8" x2="172.6" y2="205.3" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="186.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="176.6" y1="169.2" x2="176.6" y2="187.5" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="184.3" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="180.5" y1="171.6" x2="180.5" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="177.2" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="184.5" y1="143.0" x2="184.5" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="152.7" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="188.4" y1="137.8" x2="188.4" y2="163.1" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="149.1" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="192.4" y1="136.3" x2="192.4" y2="169.0" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="144.9" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="196.4" y1="290.0" x2="196.4" y2="350.5" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="313.2" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="200.3" y1="301.9" x2="200.3" y2="359.5" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="302.7" width="2.45" height="51.4" fill="var(--down)"/>
<line x1="204.3" y1="332.5" x2="204.3" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="339.0" width="2.45" height="35.9" fill="var(--down)"/>
<line x1="208.2" y1="367.1" x2="208.2" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="394.0" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="212.2" y1="366.1" x2="212.2" y2="396.9" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="378.4" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="216.1" y1="378.3" x2="216.1" y2="413.7" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="378.6" width="2.45" height="33.2" fill="var(--down)"/>
<line x1="220.1" y1="405.6" x2="220.1" y2="446.7" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="406.4" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="224.0" y1="380.3" x2="224.0" y2="413.5" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="386.7" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="228.0" y1="391.0" x2="228.0" y2="411.0" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="394.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="231.9" y1="392.1" x2="231.9" y2="433.8" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="393.8" width="2.45" height="37.6" fill="var(--down)"/>
<line x1="235.9" y1="414.4" x2="235.9" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="423.4" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="239.8" y1="422.2" x2="239.8" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="430.5" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="243.8" y1="426.1" x2="243.8" y2="458.1" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="431.3" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="247.7" y1="441.9" x2="247.7" y2="481.0" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="453.6" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="251.7" y1="458.3" x2="251.7" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="461.4" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="255.6" y1="435.9" x2="255.6" y2="481.8" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="442.2" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="259.6" y1="452.8" x2="259.6" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="460.4" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="263.5" y1="416.3" x2="263.5" y2="453.8" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="423.5" width="2.45" height="28.2" fill="var(--up)"/>
<line x1="267.5" y1="376.3" x2="267.5" y2="413.1" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="377.9" width="2.45" height="24.0" fill="var(--up)"/>
<line x1="271.4" y1="373.7" x2="271.4" y2="386.9" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="375.0" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="275.4" y1="354.7" x2="275.4" y2="379.3" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="354.9" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="279.3" y1="360.0" x2="279.3" y2="374.9" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="368.8" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="283.3" y1="355.0" x2="283.3" y2="374.3" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="356.5" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="287.3" y1="353.1" x2="287.3" y2="375.3" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="361.8" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="291.2" y1="299.5" x2="291.2" y2="331.1" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="299.7" width="2.45" height="28.4" fill="var(--down)"/>
<line x1="295.2" y1="302.3" x2="295.2" y2="326.5" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="304.8" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="299.1" y1="298.3" x2="299.1" y2="321.2" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="312.8" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="303.1" y1="322.4" x2="303.1" y2="344.3" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="323.8" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="307.0" y1="342.0" x2="307.0" y2="363.8" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="350.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="311.0" y1="340.4" x2="311.0" y2="368.9" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="345.5" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="314.9" y1="230.9" x2="314.9" y2="373.2" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="351.2" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="318.9" y1="344.9" x2="318.9" y2="373.0" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="355.7" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="322.8" y1="326.2" x2="322.8" y2="364.2" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="336.8" width="2.45" height="26.8" fill="var(--up)"/>
<line x1="326.8" y1="328.8" x2="326.8" y2="352.4" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="339.8" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="330.7" y1="310.4" x2="330.7" y2="338.1" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="322.4" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="334.7" y1="309.6" x2="334.7" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="318.6" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="338.6" y1="304.5" x2="338.6" y2="337.8" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="327.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="342.6" y1="319.4" x2="342.6" y2="334.6" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="321.5" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="346.5" y1="315.1" x2="346.5" y2="326.8" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="316.3" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="350.5" y1="313.6" x2="350.5" y2="328.6" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="315.3" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="354.4" y1="330.7" x2="354.4" y2="342.2" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="333.7" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="358.4" y1="307.2" x2="358.4" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="319.5" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="362.3" y1="321.3" x2="362.3" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="321.8" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="366.3" y1="322.5" x2="366.3" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="325.8" width="2.45" height="24.2" fill="var(--down)"/>
<line x1="370.2" y1="322.2" x2="370.2" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="333.6" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="374.2" y1="320.3" x2="374.2" y2="347.1" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="330.0" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="378.2" y1="332.8" x2="378.2" y2="361.0" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="339.7" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="382.1" y1="356.5" x2="382.1" y2="378.9" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="358.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="386.1" y1="341.1" x2="386.1" y2="364.9" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="344.8" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="390.0" y1="343.0" x2="390.0" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="345.9" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="394.0" y1="366.0" x2="394.0" y2="401.7" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="366.0" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="397.9" y1="393.2" x2="397.9" y2="420.0" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="397.0" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="401.9" y1="401.6" x2="401.9" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="408.2" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="405.8" y1="391.9" x2="405.8" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="401.6" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="409.8" y1="426.7" x2="409.8" y2="449.1" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="433.6" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="413.7" y1="413.2" x2="413.7" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="423.6" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="417.7" y1="330.1" x2="417.7" y2="396.9" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="355.5" width="2.45" height="35.9" fill="var(--up)"/>
<line x1="421.6" y1="318.4" x2="421.6" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="333.6" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="425.6" y1="301.1" x2="425.6" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="306.9" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="429.5" y1="298.1" x2="429.5" y2="322.0" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="302.5" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="433.5" y1="296.4" x2="433.5" y2="319.2" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="302.7" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="437.4" y1="166.1" x2="437.4" y2="227.9" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="177.3" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="441.4" y1="189.3" x2="441.4" y2="225.8" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="198.5" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="445.3" y1="210.7" x2="445.3" y2="245.6" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="223.9" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="449.3" y1="219.1" x2="449.3" y2="279.3" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="238.1" width="2.45" height="30.8" fill="var(--down)"/>
<line x1="453.2" y1="274.5" x2="453.2" y2="316.5" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="276.7" width="2.45" height="36.8" fill="var(--down)"/>
<line x1="457.2" y1="288.9" x2="457.2" y2="343.9" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="311.1" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="461.1" y1="307.6" x2="461.1" y2="357.7" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="320.4" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="465.1" y1="285.4" x2="465.1" y2="333.6" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="297.3" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="469.1" y1="290.6" x2="469.1" y2="311.9" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="296.6" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="473.0" y1="293.3" x2="473.0" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="303.7" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="477.0" y1="299.7" x2="477.0" y2="360.1" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="311.6" width="2.45" height="39.6" fill="var(--down)"/>
<line x1="480.9" y1="348.0" x2="480.9" y2="381.2" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="360.5" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="484.9" y1="365.4" x2="484.9" y2="392.5" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="371.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="488.8" y1="360.7" x2="488.8" y2="393.8" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="364.2" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="492.8" y1="356.4" x2="492.8" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="361.1" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="496.7" y1="324.6" x2="496.7" y2="372.9" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="339.7" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="500.7" y1="335.7" x2="500.7" y2="378.3" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="345.8" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="504.6" y1="368.3" x2="504.6" y2="392.1" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="371.9" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="508.6" y1="343.2" x2="508.6" y2="366.3" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="343.6" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="512.5" y1="329.2" x2="512.5" y2="355.7" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="337.0" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="516.5" y1="351.9" x2="516.5" y2="374.2" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="354.4" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="520.4" y1="331.3" x2="520.4" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="343.8" width="2.45" height="32.2" fill="var(--up)"/>
<line x1="524.4" y1="333.1" x2="524.4" y2="372.8" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="340.8" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="528.3" y1="306.1" x2="528.3" y2="335.8" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="316.0" width="2.45" height="19.2" fill="var(--up)"/>
<line x1="532.3" y1="310.1" x2="532.3" y2="350.2" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="327.4" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="536.2" y1="351.9" x2="536.2" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="355.0" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="540.2" y1="355.2" x2="540.2" y2="396.5" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="356.0" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="544.1" y1="330.6" x2="544.1" y2="352.8" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="342.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="548.1" y1="332.9" x2="548.1" y2="354.1" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="341.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="552.0" y1="343.9" x2="552.0" y2="376.6" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="353.3" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="556.0" y1="391.8" x2="556.0" y2="430.3" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="402.1" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="560.0" y1="380.8" x2="560.0" y2="403.7" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="386.2" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="563.9" y1="377.3" x2="563.9" y2="406.5" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="394.1" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="567.9" y1="404.6" x2="567.9" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="417.0" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="571.8" y1="423.6" x2="571.8" y2="444.7" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="425.2" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="575.8" y1="441.3" x2="575.8" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="442.2" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="579.7" y1="432.1" x2="579.7" y2="451.0" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="437.7" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="583.7" y1="447.1" x2="583.7" y2="466.8" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="450.9" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="587.6" y1="441.9" x2="587.6" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="451.6" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="591.6" y1="482.5" x2="591.6" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="483.5" width="2.45" height="68.7" fill="var(--down)"/>
<line x1="595.5" y1="560.0" x2="595.5" y2="605.8" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="566.8" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="599.5" y1="567.9" x2="599.5" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="574.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="603.4" y1="500.8" x2="603.4" y2="553.7" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="503.9" width="2.45" height="43.5" fill="var(--up)"/>
<line x1="607.4" y1="463.7" x2="607.4" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="488.2" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="611.3" y1="491.4" x2="611.3" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="499.3" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="615.3" y1="482.9" x2="615.3" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="493.0" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="619.2" y1="497.8" x2="619.2" y2="518.4" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="498.1" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="623.2" y1="390.2" x2="623.2" y2="465.2" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="424.7" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="627.1" y1="375.4" x2="627.1" y2="403.9" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="393.3" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="631.1" y1="373.3" x2="631.1" y2="401.3" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="381.4" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="635.0" y1="380.3" x2="635.0" y2="401.1" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="381.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="639.0" y1="318.9" x2="639.0" y2="371.7" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="326.3" width="2.45" height="37.9" fill="var(--up)"/>
<line x1="642.9" y1="294.8" x2="642.9" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="308.4" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="646.9" y1="296.6" x2="646.9" y2="315.9" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="298.0" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="650.9" y1="269.2" x2="650.9" y2="301.4" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="275.1" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="654.8" y1="285.2" x2="654.8" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="289.2" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="658.8" y1="299.3" x2="658.8" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="309.6" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="662.7" y1="295.0" x2="662.7" y2="312.0" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="302.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="666.7" y1="312.4" x2="666.7" y2="344.8" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="323.9" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="670.6" y1="290.5" x2="670.6" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="301.6" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="674.6" y1="286.9" x2="674.6" y2="309.9" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="294.6" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="678.5" y1="295.4" x2="678.5" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="303.2" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="682.5" y1="303.2" x2="682.5" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="313.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="686.4" y1="408.1" x2="686.4" y2="449.1" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="411.1" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="690.4" y1="412.0" x2="690.4" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="420.2" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="694.3" y1="421.6" x2="694.3" y2="443.7" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="428.6" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="698.3" y1="420.9" x2="698.3" y2="448.4" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="422.9" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="702.2" y1="409.9" x2="702.2" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="423.8" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="706.2" y1="400.0" x2="706.2" y2="422.5" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="416.1" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="710.1" y1="416.1" x2="710.1" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="419.2" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="714.1" y1="439.5" x2="714.1" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="440.1" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="718.0" y1="441.7" x2="718.0" y2="463.6" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="443.2" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="722.0" y1="410.0" x2="722.0" y2="455.7" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="416.4" width="2.45" height="35.0" fill="var(--up)"/>
<line x1="725.9" y1="402.5" x2="725.9" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="412.9" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="729.9" y1="407.4" x2="729.9" y2="430.8" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="421.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="733.8" y1="418.5" x2="733.8" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="427.1" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="737.8" y1="421.7" x2="737.8" y2="448.0" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="431.6" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="741.8" y1="433.4" x2="741.8" y2="453.4" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="439.2" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="745.7" y1="430.2" x2="745.7" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="434.6" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="749.7" y1="420.0" x2="749.7" y2="435.4" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="428.9" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="753.6" y1="420.7" x2="753.6" y2="438.7" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="424.8" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="757.6" y1="373.4" x2="757.6" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="379.8" width="2.45" height="50.8" fill="var(--up)"/>
<line x1="761.5" y1="364.6" x2="761.5" y2="391.5" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="371.5" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="765.5" y1="381.3" x2="765.5" y2="403.2" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="383.3" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="769.4" y1="378.8" x2="769.4" y2="450.0" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="389.4" width="2.45" height="58.8" fill="var(--down)"/>
<line x1="773.4" y1="431.6" x2="773.4" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="442.7" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="777.3" y1="401.6" x2="777.3" y2="448.6" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="403.9" width="2.45" height="39.3" fill="var(--up)"/>
<line x1="781.3" y1="365.8" x2="781.3" y2="405.0" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="394.9" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="785.2" y1="391.8" x2="785.2" y2="482.7" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="403.0" width="2.45" height="59.9" fill="var(--down)"/>
<line x1="789.2" y1="464.8" x2="789.2" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="464.8" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="793.1" y1="453.8" x2="793.1" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="466.8" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="797.1" y1="466.2" x2="797.1" y2="506.9" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="487.0" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="801.0" y1="503.8" x2="801.0" y2="533.6" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="511.2" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="805.0" y1="496.1" x2="805.0" y2="526.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="502.3" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="808.9" y1="446.6" x2="808.9" y2="489.8" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="461.9" width="2.45" height="26.7" fill="var(--up)"/>
<line x1="812.9" y1="437.7" x2="812.9" y2="464.8" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="448.7" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="816.8" y1="461.3" x2="816.8" y2="515.6" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="464.8" width="2.45" height="48.0" fill="var(--down)"/>
<line x1="820.8" y1="488.0" x2="820.8" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="493.9" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="824.7" y1="496.6" x2="824.7" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="504.1" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="828.7" y1="503.7" x2="828.7" y2="525.7" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="523.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="832.7" y1="510.0" x2="832.7" y2="536.5" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="524.0" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="836.6" y1="534.9" x2="836.6" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="536.5" width="2.45" height="24.9" fill="var(--down)"/>
<line x1="840.6" y1="533.9" x2="840.6" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="546.9" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="844.5" y1="506.3" x2="844.5" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="522.6" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="848.5" y1="516.8" x2="848.5" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="521.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="852.4" y1="393.5" x2="852.4" y2="458.7" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="423.7" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="856.4" y1="429.4" x2="856.4" y2="487.6" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="433.6" width="2.45" height="49.1" fill="var(--down)"/>
<line x1="860.3" y1="442.1" x2="860.3" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="448.5" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="864.3" y1="399.2" x2="864.3" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="418.5" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="868.2" y1="417.7" x2="868.2" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="420.8" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="872.2" y1="383.7" x2="872.2" y2="494.2" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="387.2" width="2.45" height="93.3" fill="var(--up)"/>
<line x1="876.1" y1="296.1" x2="876.1" y2="335.1" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="313.1" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="880.1" y1="298.5" x2="880.1" y2="342.6" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="328.5" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="884.0" y1="318.4" x2="884.0" y2="352.7" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="329.1" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="888.0" y1="279.9" x2="888.0" y2="337.7" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="289.3" width="2.45" height="34.8" fill="var(--up)"/>
<line x1="891.9" y1="288.1" x2="891.9" y2="330.9" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="297.2" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="895.9" y1="346.5" x2="895.9" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="355.3" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="899.8" y1="344.3" x2="899.8" y2="378.3" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="357.3" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="903.8" y1="339.3" x2="903.8" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="342.6" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="907.7" y1="352.8" x2="907.7" y2="401.9" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="355.3" width="2.45" height="40.4" fill="var(--down)"/>
<line x1="911.7" y1="420.3" x2="911.7" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="432.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="915.6" y1="429.5" x2="915.6" y2="460.0" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="438.7" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="919.6" y1="427.0" x2="919.6" y2="462.6" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="434.9" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="923.6" y1="447.1" x2="923.6" y2="474.7" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="455.4" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="927.5" y1="449.2" x2="927.5" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="462.4" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="931.5" y1="567.3" x2="931.5" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="568.9" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="935.4" y1="531.0" x2="935.4" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="534.2" width="2.45" height="25.8" fill="var(--up)"/>
<line x1="939.4" y1="454.0" x2="939.4" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="468.3" width="2.45" height="55.0" fill="var(--up)"/>
<line x1="943.3" y1="463.3" x2="943.3" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="472.8" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="947.3" y1="447.1" x2="947.3" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="448.2" width="2.45" height="23.0" fill="var(--down)"/>
<line x1="951.2" y1="458.3" x2="951.2" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="469.0" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="955.2" y1="451.6" x2="955.2" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="464.6" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="959.1" y1="433.0" x2="959.1" y2="464.8" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="450.8" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="963.1" y1="424.7" x2="963.1" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="450.8" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="967.0" y1="440.3" x2="967.0" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="447.0" width="2.45" height="43.7" fill="var(--down)"/>
<line x1="971.0" y1="457.3" x2="971.0" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="459.0" width="2.45" height="28.0" fill="var(--up)"/>
<line x1="974.9" y1="445.4" x2="974.9" y2="470.2" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="455.0" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="978.9" y1="468.3" x2="978.9" y2="518.4" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="469.2" width="2.45" height="40.8" fill="var(--down)"/>
<line x1="982.8" y1="526.4" x2="982.8" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="532.7" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="986.8" y1="539.4" x2="986.8" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="555.2" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="990.7" y1="547.4" x2="990.7" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="553.4" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="994.7" y1="539.8" x2="994.7" y2="560.7" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="547.6" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="998.6" y1="524.9" x2="998.6" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="529.7" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="1002.6" y1="506.5" x2="1002.6" y2="525.0" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="508.0" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="1006.5" y1="462.2" x2="1006.5" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="468.1" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="1010.5" y1="471.9" x2="1010.5" y2="512.7" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="495.3" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="1014.5" y1="470.4" x2="1014.5" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="492.3" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="1018.4" y1="491.0" x2="1018.4" y2="509.8" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="493.1" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="1022.4" y1="478.7" x2="1022.4" y2="535.4" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="491.3" width="2.45" height="39.7" fill="var(--up)"/>
<line x1="1026.3" y1="448.4" x2="1026.3" y2="494.3" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="463.2" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="1030.3" y1="410.9" x2="1030.3" y2="440.6" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="428.1" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="1034.2" y1="414.8" x2="1034.2" y2="438.7" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="416.1" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="1038.2" y1="400.4" x2="1038.2" y2="430.0" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="417.2" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="1042.1" y1="335.4" x2="1042.1" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="343.6" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="1046.1" y1="324.3" x2="1046.1" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="343.5" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="1050.0" y1="322.8" x2="1050.0" y2="358.3" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="343.9" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="60" y1="289.9" x2="1052" y2="289.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="293.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$681 R1</text>
<text x="1058" y="305.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="174.6" x2="1052" y2="174.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="178.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$740 R2</text>
<text x="1058" y="190.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="383.5" x2="1052" y2="383.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="377.5" font-size="11.5" fill="var(--support)" font-weight="600">$633 S1</text>
<text x="1058" y="389.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="470.4" x2="1052" y2="470.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="464.4" font-size="11.5" fill="var(--support)" font-weight="600">$589 S2</text>
<text x="1058" y="476.4" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="534.5" x2="1052" y2="534.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="528.5" font-size="11.5" fill="var(--support)" font-weight="600">$557 S3</text>
<text x="1058" y="540.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="354.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="346.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $648 (2026-09-11)</text>
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
| R2 | $740 | 2 | 2025-10-10·2026-01-29 — 최근 1년 최고가($790.80) 아래의 상단 고점대. 터치 2회로 표본이 얕다 |
| R1 | $681 | 4 | 2025-12-22·2026-03-04·04-17·07-15 — **터치 4회로 이 표에서 두 번째로 두껍다.** 2026년 내내 반복적으로 막힌 자리이고, 마지막 터치(07-15)는 2분기 실적 발표(07-29) 직전이다 |
| **현재가** | **$648.03** (2026-09-11 종가) | — | R1과 S1 사이. R1까지 +5.1%, S1까지 −2.3% |
| S1 | $633 | 2 | 2025-12-12·2026-02-18 — 현재가에 가장 근접한 지지(−2.3%). 터치 2회로 얕다 |
| S2 | $589 | 5 | 2025-11-19·2026-01-20·05-12·05-21·07-09 — **터치 5회로 이 표에서 가장 두꺼운 레벨.** 다섯 시점이 9개월에 걸쳐 흩어져 있다 |
| S3 | $557 | 2 | 2026-06-11·2026-09-01 — 최근(09-01) 터치가 포함돼 있어 아직 유효한 레짐의 레벨이다 |
| 참고선 | $790.80 | — | 최근 1년 최고가. R2($740)와 7% 떨어져 있고 터치 2회 기준을 채우지 못해 근시일 저항으로는 R2를 본다 |
| 참고선 | $520.26 | — | 최근 1년 최저가. S3($557)보다 7% 아래이며 그 사이에 터치 2회 이상 클러스터가 없다 |

> 이 표의 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)과 달리 **현재가 양쪽에 레벨이 고르게 있다** — 최근 1년간 $520~790 박스 안에서 움직였기 때문이다. 동종사 [Alphabet](../alphabet/09_technical_daily.md)의 같은 표가 상단 비대칭(신고가 부근)인 것과 대비된다.

---

## 3. 관측된 특이 구간 — 2026-07-29 2분기 실적 발표 이후

- 계기는 매출이 아니라 **가이던스와 줄어드는 잉여현금흐름**이었다 — 매출은 +28% YoY였지만 영업이익이 −8% YoY로 꺾이고 FY2026 총비용 가이던스가 $165~169B로 상향됐다([최근 뉴스 / 이슈](./08_news.md) 2026-07-29 항목).
- 발표 직전 07-15에 R1($681)을 마지막으로 터치한 뒤 아래쪽으로 이동했고, 07-09의 S2($589) 터치와 09-01의 S3($557) 터치가 그 이후 구간에서 나왔다. **즉 실적 발표 전후로 거래 중심이 R1 부근에서 S2~S3 부근으로 내려앉았다.**
- 8월 26일 아동 안전 소송 합의(최대 $17.1B)도 이 구간에 들어 있다. 09-01 S3 터치가 그 직후다.
- 이 재설정 때문에 R2($740)와 52주 최고($790.80)는 **실적 발표 이전 레짐의 가격대**로 읽어야 하며, 위 표에서 후자를 참고선으로 내린 이유다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-12~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py META --name "Meta Platforms" --close-on 2026-09-11 --emit all` (기본 옵션, `--force-level`·`--event` 미사용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **터치 횟수 편차가 크다** — S2는 5회인데 R2·S1·S3은 2회다. 2회 레벨은 표본이 얕아 같은 강도로 읽으면 안 된다.
    - 3. 관측된 특이 구간의 실적 발표 이후 레짐 변화로, 현재가 위쪽 레벨(R1·R2)은 발표 이전에 형성된 터치가 대부분이다.
    - 이 1년 구간에는 주식분할·유상증자가 없었다(Meta는 2012년 상장 이후 분할이 없다). 2026년 5월 선순위 무담보채 $25.0B 발행은 주식 가격 연속성에 영향이 없다. 기간 내 배당이 4회 있었고 원주가를 썼으므로 배당 재투자 수익은 반영되지 않았다.

---

*작성일: 2026-09-12*
