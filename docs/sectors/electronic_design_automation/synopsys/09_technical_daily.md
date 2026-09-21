# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-18 종가 $384.97은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치**한다.
- **마지막 봉 주의**: 원자료를 수집 시점(2026-09-21 장중)까지 받으므로 **차트의 마지막 봉은 아직 끝나지 않은 구간**이다. 아래 표의 현재가 행은 그 미완성 봉이 아니라 **마지막 완료 거래일(2026-09-18)의 확정 종가**를 쓴다(4. 방법론 · 한계 참고).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-22 ~ 2026-09-21)

<style>
.snps-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.snps-chart svg { width:100%; height:auto; display:block; }
.snps-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.snps-chart .title { fill: var(--ink); font-weight:600; }
.snps-chart .grid { stroke: var(--grid); stroke-width:1; }
.snps-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="snps-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synopsys(SNPS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Synopsys (SNPS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-22 ~ 2026-09-21 · 마지막 종가 $396.49 (2026-09-21) · 단위 USD</text>
<line x1="60" y1="566.0" x2="1052" y2="566.0" class="grid"/>
<text x="52" y="570.0" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="491.0" x2="1052" y2="491.0" class="grid"/>
<text x="52" y="495.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="416.0" x2="1052" y2="416.0" class="grid"/>
<text x="52" y="420.0" font-size="11" text-anchor="end" fill="var(--muted)">425</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="266.0" x2="1052" y2="266.0" class="grid"/>
<text x="52" y="270.0" font-size="11" text-anchor="end" fill="var(--muted)">475</text>
<line x1="60" y1="191.0" x2="1052" y2="191.0" class="grid"/>
<text x="52" y="195.0" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="116.0" x2="1052" y2="116.0" class="grid"/>
<text x="52" y="120.0" font-size="11" text-anchor="end" fill="var(--muted)">525</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="89.6" y1="626.0" x2="89.6" y2="631.0" class="axis"/>
<text x="89.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="180.5" y1="626.0" x2="180.5" y2="631.0" class="axis"/>
<text x="180.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="255.6" y1="626.0" x2="255.6" y2="631.0" class="axis"/>
<text x="255.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="342.6" y1="626.0" x2="342.6" y2="631.0" class="axis"/>
<text x="342.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="421.6" y1="626.0" x2="421.6" y2="631.0" class="axis"/>
<text x="421.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="496.7" y1="626.0" x2="496.7" y2="631.0" class="axis"/>
<text x="496.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="583.7" y1="626.0" x2="583.7" y2="631.0" class="axis"/>
<text x="583.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="666.7" y1="626.0" x2="666.7" y2="631.0" class="axis"/>
<text x="666.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="745.7" y1="626.0" x2="745.7" y2="631.0" class="axis"/>
<text x="745.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="828.7" y1="626.0" x2="828.7" y2="631.0" class="axis"/>
<text x="828.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="915.6" y1="626.0" x2="915.6" y2="631.0" class="axis"/>
<text x="915.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="998.6" y1="626.0" x2="998.6" y2="631.0" class="axis"/>
<text x="998.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="144.1" x2="62.0" y2="246.6" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="146.6" width="2.45" height="74.4" fill="var(--up)"/>
<line x1="65.9" y1="152.0" x2="65.9" y2="225.3" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="156.6" width="2.45" height="63.4" fill="var(--down)"/>
<line x1="69.9" y1="217.0" x2="69.9" y2="298.3" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="218.0" width="2.45" height="68.7" fill="var(--down)"/>
<line x1="73.8" y1="228.2" x2="73.8" y2="305.0" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="229.4" width="2.45" height="74.1" fill="var(--up)"/>
<line x1="77.8" y1="212.0" x2="77.8" y2="259.6" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="227.7" width="2.45" height="31.9" fill="var(--up)"/>
<line x1="81.7" y1="215.1" x2="81.7" y2="256.2" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="227.0" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="85.7" y1="205.4" x2="85.7" y2="248.6" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="210.8" width="2.45" height="34.0" fill="var(--up)"/>
<line x1="89.6" y1="203.8" x2="89.6" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="224.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="93.6" y1="223.1" x2="93.6" y2="279.9" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="236.9" width="2.45" height="40.7" fill="var(--down)"/>
<line x1="97.5" y1="263.6" x2="97.5" y2="291.2" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="270.5" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="101.5" y1="247.3" x2="101.5" y2="282.4" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="256.3" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="105.5" y1="238.7" x2="105.5" y2="285.7" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="238.7" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="109.4" y1="213.9" x2="109.4" y2="260.8" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="222.9" width="2.45" height="37.6" fill="var(--up)"/>
<line x1="113.4" y1="226.8" x2="113.4" y2="248.9" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="228.5" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="117.3" y1="228.3" x2="117.3" y2="379.2" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="237.8" width="2.45" height="136.5" fill="var(--down)"/>
<line x1="121.3" y1="329.6" x2="121.3" y2="371.0" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="342.6" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="125.2" y1="332.6" x2="125.2" y2="390.9" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="359.7" width="2.45" height="22.1" fill="var(--up)"/>
<line x1="129.2" y1="344.3" x2="129.2" y2="395.0" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="352.2" width="2.45" height="31.1" fill="var(--down)"/>
<line x1="133.1" y1="354.4" x2="133.1" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="370.4" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="137.1" y1="320.5" x2="137.1" y2="385.2" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="348.1" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="141.0" y1="317.5" x2="141.0" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="330.9" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="145.0" y1="311.9" x2="145.0" y2="356.0" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="313.9" width="2.45" height="32.4" fill="var(--up)"/>
<line x1="148.9" y1="293.8" x2="148.9" y2="357.9" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="321.6" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="152.9" y1="309.8" x2="152.9" y2="339.5" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="322.7" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="156.8" y1="270.5" x2="156.8" y2="316.6" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="298.5" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="160.8" y1="264.7" x2="160.8" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="277.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="164.7" y1="303.8" x2="164.7" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="306.0" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="168.7" y1="319.6" x2="168.7" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="325.0" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="172.6" y1="332.7" x2="172.6" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="341.0" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="176.6" y1="322.3" x2="176.6" y2="362.9" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="329.5" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="180.5" y1="333.5" x2="180.5" y2="378.3" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="335.5" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="184.5" y1="379.7" x2="184.5" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="386.0" width="2.45" height="55.9" fill="var(--down)"/>
<line x1="188.4" y1="440.2" x2="188.4" y2="482.9" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="441.5" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="192.4" y1="456.3" x2="192.4" y2="516.4" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="458.0" width="2.45" height="44.6" fill="var(--down)"/>
<line x1="196.4" y1="490.1" x2="196.4" y2="530.3" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="508.0" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="200.3" y1="487.2" x2="200.3" y2="525.7" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="488.7" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="204.3" y1="491.9" x2="204.3" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="496.6" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="208.2" y1="479.8" x2="208.2" y2="507.7" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="489.1" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="212.2" y1="480.1" x2="212.2" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="502.2" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="216.1" y1="497.4" x2="216.1" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="521.5" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="220.1" y1="493.7" x2="220.1" y2="527.0" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="520.3" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="224.0" y1="522.2" x2="224.0" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="527.0" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="228.0" y1="489.2" x2="228.0" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="532.1" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="231.9" y1="474.4" x2="231.9" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="485.6" width="2.45" height="48.6" fill="var(--down)"/>
<line x1="235.9" y1="514.6" x2="235.9" y2="560.9" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="525.9" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="239.8" y1="473.3" x2="239.8" y2="516.1" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="477.1" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="243.8" y1="474.1" x2="243.8" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="486.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="247.7" y1="456.1" x2="247.7" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="462.0" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="251.7" y1="434.3" x2="251.7" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="437.0" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="255.6" y1="350.0" x2="255.6" y2="403.4" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="353.0" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="259.6" y1="330.4" x2="259.6" y2="370.7" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="342.9" width="2.45" height="23.4" fill="var(--up)"/>
<line x1="263.5" y1="286.1" x2="263.5" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="291.7" width="2.45" height="63.5" fill="var(--up)"/>
<line x1="267.5" y1="293.9" x2="267.5" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="299.8" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="271.4" y1="277.6" x2="271.4" y2="297.9" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="290.7" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="275.4" y1="284.5" x2="275.4" y2="310.6" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="287.7" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="279.3" y1="276.1" x2="279.3" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="285.7" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="283.3" y1="255.1" x2="283.3" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="263.5" width="2.45" height="36.5" fill="var(--up)"/>
<line x1="287.3" y1="244.3" x2="287.3" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="259.2" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="291.2" y1="258.5" x2="291.2" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="262.3" width="2.45" height="69.9" fill="var(--down)"/>
<line x1="295.2" y1="278.8" x2="295.2" y2="330.5" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="317.0" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="299.1" y1="296.0" x2="299.1" y2="333.5" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="301.0" width="2.45" height="28.4" fill="var(--up)"/>
<line x1="303.1" y1="290.0" x2="303.1" y2="332.1" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="293.3" width="2.45" height="38.5" fill="var(--down)"/>
<line x1="307.0" y1="287.5" x2="307.0" y2="326.9" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="310.0" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="311.0" y1="282.3" x2="311.0" y2="312.2" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="299.8" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="314.9" y1="239.3" x2="314.9" y2="287.5" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="247.3" width="2.45" height="39.0" fill="var(--up)"/>
<line x1="318.9" y1="256.4" x2="318.9" y2="281.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="258.4" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="322.8" y1="262.1" x2="322.8" y2="274.3" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="263.8" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="326.8" y1="255.2" x2="326.8" y2="274.0" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="259.6" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="330.7" y1="237.2" x2="330.7" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="254.1" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="334.7" y1="254.7" x2="334.7" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="266.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="338.6" y1="267.0" x2="338.6" y2="283.8" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="271.6" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="342.6" y1="233.3" x2="342.6" y2="276.6" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="249.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="346.5" y1="172.1" x2="346.5" y2="254.1" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="208.4" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="350.5" y1="162.6" x2="350.5" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="164.7" width="2.45" height="39.5" fill="var(--up)"/>
<line x1="354.4" y1="116.1" x2="354.4" y2="179.4" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="131.9" width="2.45" height="35.1" fill="var(--up)"/>
<line x1="358.4" y1="136.8" x2="358.4" y2="162.7" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="147.5" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="362.3" y1="104.2" x2="362.3" y2="157.7" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="115.5" width="2.45" height="29.1" fill="var(--up)"/>
<line x1="366.3" y1="85.4" x2="366.3" y2="119.7" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="90.7" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="370.2" y1="108.5" x2="370.2" y2="156.6" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="127.5" width="2.45" height="28.1" fill="var(--down)"/>
<line x1="374.2" y1="168.9" x2="374.2" y2="195.3" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="175.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="378.2" y1="133.7" x2="378.2" y2="185.0" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="161.0" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="382.1" y1="130.3" x2="382.1" y2="167.0" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="142.1" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="386.1" y1="152.5" x2="386.1" y2="213.2" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="158.1" width="2.45" height="35.5" fill="var(--up)"/>
<line x1="390.0" y1="114.5" x2="390.0" y2="180.4" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="125.1" width="2.45" height="36.5" fill="var(--up)"/>
<line x1="394.0" y1="115.9" x2="394.0" y2="191.0" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="122.8" width="2.45" height="39.8" fill="var(--down)"/>
<line x1="397.9" y1="161.9" x2="397.9" y2="200.7" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="168.6" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="401.9" y1="167.0" x2="401.9" y2="211.2" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="182.0" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="405.8" y1="173.6" x2="405.8" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="180.5" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="409.8" y1="143.6" x2="409.8" y2="176.5" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="156.9" width="2.45" height="19.5" fill="var(--up)"/>
<line x1="413.7" y1="158.9" x2="413.7" y2="266.3" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="175.0" width="2.45" height="76.0" fill="var(--down)"/>
<line x1="417.7" y1="265.4" x2="417.7" y2="301.4" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="267.3" width="2.45" height="28.4" fill="var(--down)"/>
<line x1="421.6" y1="277.4" x2="421.6" y2="318.2" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="308.9" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="425.6" y1="320.0" x2="425.6" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="323.9" width="2.45" height="109.6" fill="var(--down)"/>
<line x1="429.5" y1="414.5" x2="429.5" y2="473.9" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="434.1" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="433.5" y1="413.5" x2="433.5" y2="472.4" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="433.7" width="2.45" height="26.0" fill="var(--down)"/>
<line x1="437.4" y1="397.6" x2="437.4" y2="442.5" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="410.4" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="441.4" y1="362.1" x2="441.4" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="374.3" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="445.3" y1="335.0" x2="445.3" y2="383.0" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="371.3" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="449.3" y1="361.2" x2="449.3" y2="416.0" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="364.7" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="453.2" y1="375.4" x2="453.2" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="376.1" width="2.45" height="44.8" fill="var(--down)"/>
<line x1="457.2" y1="366.7" x2="457.2" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="379.7" width="2.45" height="41.2" fill="var(--up)"/>
<line x1="461.1" y1="410.5" x2="461.1" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="414.2" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="465.1" y1="350.3" x2="465.1" y2="391.4" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="364.1" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="469.1" y1="361.5" x2="469.1" y2="390.7" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="363.7" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="473.0" y1="339.8" x2="473.0" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="371.2" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="477.0" y1="390.8" x2="477.0" y2="439.2" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="402.8" width="2.45" height="25.7" fill="var(--down)"/>
<line x1="480.9" y1="360.8" x2="480.9" y2="445.9" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="368.8" width="2.45" height="64.0" fill="var(--up)"/>
<line x1="484.9" y1="328.5" x2="484.9" y2="371.5" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="343.5" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="488.8" y1="360.2" x2="488.8" y2="420.9" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="401.4" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="492.8" y1="439.6" x2="492.8" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="449.0" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="496.7" y1="412.3" x2="496.7" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="417.0" width="2.45" height="33.9" fill="var(--up)"/>
<line x1="500.7" y1="397.2" x2="500.7" y2="459.1" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="418.0" width="2.45" height="35.5" fill="var(--up)"/>
<line x1="504.6" y1="372.5" x2="504.6" y2="430.0" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="398.1" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="508.6" y1="347.9" x2="508.6" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="364.1" width="2.45" height="49.6" fill="var(--up)"/>
<line x1="512.5" y1="354.9" x2="512.5" y2="395.6" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="378.8" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="516.5" y1="368.3" x2="516.5" y2="402.1" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="379.3" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="520.4" y1="374.0" x2="520.4" y2="407.0" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="379.8" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="524.4" y1="381.8" x2="524.4" y2="415.0" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="392.1" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="528.3" y1="381.9" x2="528.3" y2="435.9" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="395.4" width="2.45" height="39.4" fill="var(--down)"/>
<line x1="532.3" y1="414.5" x2="532.3" y2="460.7" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="434.0" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="536.2" y1="405.7" x2="536.2" y2="438.2" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="413.4" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="540.2" y1="384.6" x2="540.2" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="403.1" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="544.1" y1="383.9" x2="544.1" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="405.0" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="548.1" y1="391.3" x2="548.1" y2="423.4" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="406.2" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="552.0" y1="401.3" x2="552.0" y2="434.0" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="413.3" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="556.0" y1="365.7" x2="556.0" y2="402.1" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="393.6" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="560.0" y1="403.2" x2="560.0" y2="461.5" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="411.0" width="2.45" height="33.2" fill="var(--down)"/>
<line x1="563.9" y1="413.2" x2="563.9" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="423.5" width="2.45" height="37.1" fill="var(--down)"/>
<line x1="567.9" y1="450.4" x2="567.9" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="475.2" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="571.8" y1="486.4" x2="571.8" y2="552.5" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="491.0" width="2.45" height="58.6" fill="var(--down)"/>
<line x1="575.8" y1="518.7" x2="575.8" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="541.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="579.7" y1="498.6" x2="579.7" y2="529.4" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="501.6" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="583.7" y1="480.6" x2="583.7" y2="507.5" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="481.1" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="587.6" y1="487.8" x2="587.6" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="503.1" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="591.6" y1="495.2" x2="591.6" y2="520.6" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="499.8" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="595.5" y1="496.6" x2="595.5" y2="524.4" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="497.3" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="599.5" y1="445.5" x2="599.5" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="455.8" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="603.4" y1="458.0" x2="603.4" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="461.2" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="607.4" y1="479.2" x2="607.4" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="486.2" width="2.45" height="28.1" fill="var(--down)"/>
<line x1="611.3" y1="435.7" x2="611.3" y2="526.8" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="437.7" width="2.45" height="75.8" fill="var(--up)"/>
<line x1="615.3" y1="400.6" x2="615.3" y2="436.4" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="416.5" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="619.2" y1="371.4" x2="619.2" y2="426.7" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="375.6" width="2.45" height="42.6" fill="var(--up)"/>
<line x1="623.2" y1="342.1" x2="623.2" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="351.9" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="627.1" y1="313.9" x2="627.1" y2="349.5" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="333.4" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="631.1" y1="301.5" x2="631.1" y2="348.7" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="308.1" width="2.45" height="38.6" fill="var(--up)"/>
<line x1="635.0" y1="250.2" x2="635.0" y2="305.0" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="288.3" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="639.0" y1="254.8" x2="639.0" y2="278.3" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="259.2" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="642.9" y1="289.1" x2="642.9" y2="340.6" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="292.7" width="2.45" height="27.8" fill="var(--down)"/>
<line x1="646.9" y1="184.2" x2="646.9" y2="283.4" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="188.5" width="2.45" height="94.3" fill="var(--up)"/>
<line x1="650.9" y1="188.0" x2="650.9" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="195.4" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="654.8" y1="197.0" x2="654.8" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="200.0" width="2.45" height="39.3" fill="var(--down)"/>
<line x1="658.8" y1="246.1" x2="658.8" y2="275.9" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="247.3" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="662.7" y1="240.0" x2="662.7" y2="276.1" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="243.2" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="666.7" y1="197.2" x2="666.7" y2="234.7" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="217.5" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="670.6" y1="190.2" x2="670.6" y2="226.0" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="198.5" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="674.6" y1="153.4" x2="674.6" y2="191.0" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="183.5" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="678.5" y1="169.0" x2="678.5" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="177.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="682.5" y1="140.0" x2="682.5" y2="180.5" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="172.1" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="686.4" y1="133.7" x2="686.4" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="141.6" width="2.45" height="36.3" fill="var(--up)"/>
<line x1="690.4" y1="131.9" x2="690.4" y2="155.0" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="142.4" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="694.3" y1="139.5" x2="694.3" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="151.4" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="698.3" y1="146.8" x2="698.3" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="147.2" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="702.2" y1="150.0" x2="702.2" y2="177.1" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="160.9" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="706.2" y1="164.0" x2="706.2" y2="217.9" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="183.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="710.1" y1="185.5" x2="710.1" y2="223.7" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="193.5" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="714.1" y1="188.0" x2="714.1" y2="219.3" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="208.0" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="718.0" y1="193.3" x2="718.0" y2="269.7" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="194.2" width="2.45" height="58.8" fill="var(--up)"/>
<line x1="722.0" y1="176.8" x2="722.0" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="179.1" width="2.45" height="38.2" fill="var(--up)"/>
<line x1="725.9" y1="88.7" x2="725.9" y2="165.5" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="116.8" width="2.45" height="44.2" fill="var(--up)"/>
<line x1="729.9" y1="72.6" x2="729.9" y2="118.5" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="87.3" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="733.8" y1="87.1" x2="733.8" y2="121.5" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="87.3" width="2.45" height="25.9" fill="var(--down)"/>
<line x1="737.8" y1="112.7" x2="737.8" y2="275.9" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="161.0" width="2.45" height="88.1" fill="var(--down)"/>
<line x1="741.8" y1="237.5" x2="741.8" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="249.0" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="745.7" y1="208.2" x2="745.7" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="214.1" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="749.7" y1="164.8" x2="749.7" y2="234.1" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="165.9" width="2.45" height="68.2" fill="var(--up)"/>
<line x1="753.6" y1="178.6" x2="753.6" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="182.7" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="757.6" y1="189.9" x2="757.6" y2="236.0" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="189.9" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="761.5" y1="224.1" x2="761.5" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="227.1" width="2.45" height="69.4" fill="var(--down)"/>
<line x1="765.5" y1="255.5" x2="765.5" y2="300.9" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="270.6" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="769.4" y1="228.4" x2="769.4" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="263.6" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="773.4" y1="273.7" x2="773.4" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="309.4" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="777.3" y1="297.9" x2="777.3" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="317.7" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="781.3" y1="307.7" x2="781.3" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="319.7" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="785.2" y1="300.5" x2="785.2" y2="331.9" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="304.1" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="789.2" y1="324.5" x2="789.2" y2="356.5" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="335.0" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="793.1" y1="255.4" x2="793.1" y2="352.5" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="305.8" width="2.45" height="40.2" fill="var(--up)"/>
<line x1="797.1" y1="292.8" x2="797.1" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="305.0" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="801.0" y1="282.8" x2="801.0" y2="332.6" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="297.3" width="2.45" height="27.1" fill="var(--up)"/>
<line x1="805.0" y1="251.6" x2="805.0" y2="306.6" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="296.0" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="808.9" y1="271.5" x2="808.9" y2="316.6" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="299.2" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="812.9" y1="294.4" x2="812.9" y2="343.0" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="301.6" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="816.8" y1="316.9" x2="816.8" y2="375.4" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="328.0" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="820.8" y1="310.0" x2="820.8" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="317.2" width="2.45" height="32.0" fill="var(--down)"/>
<line x1="824.7" y1="342.3" x2="824.7" y2="367.1" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="352.8" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="828.7" y1="297.6" x2="828.7" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="327.4" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="832.7" y1="330.6" x2="832.7" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="337.6" width="2.45" height="41.9" fill="var(--down)"/>
<line x1="836.6" y1="360.9" x2="836.6" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="364.2" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="840.6" y1="336.2" x2="840.6" y2="399.9" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="347.4" width="2.45" height="33.7" fill="var(--down)"/>
<line x1="844.5" y1="381.4" x2="844.5" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="382.6" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="848.5" y1="360.5" x2="848.5" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="360.9" width="2.45" height="40.6" fill="var(--up)"/>
<line x1="852.4" y1="347.3" x2="852.4" y2="375.6" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="354.5" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="856.4" y1="329.3" x2="856.4" y2="392.8" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="344.5" width="2.45" height="45.1" fill="var(--down)"/>
<line x1="860.3" y1="387.4" x2="860.3" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="412.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="864.3" y1="393.9" x2="864.3" y2="428.0" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="401.4" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="868.2" y1="414.1" x2="868.2" y2="442.0" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="414.1" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="872.2" y1="482.8" x2="872.2" y2="593.0" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="486.2" width="2.45" height="51.9" fill="var(--down)"/>
<line x1="876.1" y1="535.5" x2="876.1" y2="569.4" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="545.0" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="880.1" y1="517.9" x2="880.1" y2="560.5" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="523.8" width="2.45" height="35.6" fill="var(--up)"/>
<line x1="884.0" y1="520.8" x2="884.0" y2="569.5" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="525.1" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="888.0" y1="554.2" x2="888.0" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="560.3" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="891.9" y1="551.5" x2="891.9" y2="583.9" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="557.0" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="895.9" y1="503.4" x2="895.9" y2="541.0" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="524.0" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="899.8" y1="484.2" x2="899.8" y2="551.5" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="513.3" width="2.45" height="26.3" fill="var(--down)"/>
<line x1="903.8" y1="528.1" x2="903.8" y2="570.7" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="534.5" width="2.45" height="35.4" fill="var(--down)"/>
<line x1="907.7" y1="547.9" x2="907.7" y2="580.4" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="563.0" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="911.7" y1="522.1" x2="911.7" y2="564.5" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="524.7" width="2.45" height="32.6" fill="var(--up)"/>
<line x1="915.6" y1="502.8" x2="915.6" y2="533.0" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="508.3" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="919.6" y1="478.0" x2="919.6" y2="509.0" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="479.4" width="2.45" height="26.9" fill="var(--up)"/>
<line x1="923.6" y1="455.0" x2="923.6" y2="489.0" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="462.0" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="927.5" y1="461.3" x2="927.5" y2="502.2" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="473.1" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="931.5" y1="441.7" x2="931.5" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="443.0" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="935.4" y1="426.9" x2="935.4" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="443.0" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="939.4" y1="454.0" x2="939.4" y2="484.5" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="455.0" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="943.3" y1="435.9" x2="943.3" y2="460.5" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="449.8" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="947.3" y1="440.3" x2="947.3" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="454.0" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="951.2" y1="419.1" x2="951.2" y2="462.8" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="426.5" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="955.2" y1="413.7" x2="955.2" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="438.2" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="959.1" y1="452.4" x2="959.1" y2="483.7" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="458.6" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="963.1" y1="466.3" x2="963.1" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="475.3" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="967.0" y1="486.7" x2="967.0" y2="507.3" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="492.2" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="971.0" y1="485.1" x2="971.0" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="489.0" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="974.9" y1="503.0" x2="974.9" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="505.4" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="978.9" y1="458.2" x2="978.9" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="464.6" width="2.45" height="37.4" fill="var(--up)"/>
<line x1="982.8" y1="432.2" x2="982.8" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="461.0" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="986.8" y1="296.1" x2="986.8" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="296.3" width="2.45" height="135.7" fill="var(--up)"/>
<line x1="990.7" y1="303.6" x2="990.7" y2="369.2" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="305.4" width="2.45" height="57.7" fill="var(--down)"/>
<line x1="994.7" y1="353.4" x2="994.7" y2="387.6" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="372.2" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="998.6" y1="398.4" x2="998.6" y2="449.1" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="406.4" width="2.45" height="40.2" fill="var(--down)"/>
<line x1="1002.6" y1="434.8" x2="1002.6" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="443.1" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="1006.5" y1="431.5" x2="1006.5" y2="451.7" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="433.7" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="1010.5" y1="436.6" x2="1010.5" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="436.6" width="2.45" height="72.8" fill="var(--down)"/>
<line x1="1014.5" y1="473.6" x2="1014.5" y2="516.6" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="500.5" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="1018.4" y1="495.8" x2="1018.4" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="511.3" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="1022.4" y1="486.6" x2="1022.4" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="499.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="1026.3" y1="488.5" x2="1026.3" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="492.5" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="1030.3" y1="506.0" x2="1030.3" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="509.3" width="2.45" height="37.4" fill="var(--down)"/>
<line x1="1034.2" y1="546.6" x2="1034.2" y2="603.4" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="555.9" width="2.45" height="32.0" fill="var(--down)"/>
<line x1="1038.2" y1="551.2" x2="1038.2" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="555.6" width="2.45" height="32.9" fill="var(--up)"/>
<line x1="1042.1" y1="531.0" x2="1042.1" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="537.6" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="1046.1" y1="532.2" x2="1046.1" y2="549.9" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="536.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1050.0" y1="491.0" x2="1050.0" y2="533.2" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="501.5" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="60" y1="342.8" x2="1052" y2="342.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="346.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$449 R1</text>
<text x="1058" y="358.3" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="264.2" x2="1052" y2="264.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="267.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$476 R2</text>
<text x="1058" y="279.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="194.0" x2="1052" y2="194.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="197.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$499 R3</text>
<text x="1058" y="209.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="526.7" x2="1052" y2="526.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="520.7" font-size="11.5" fill="var(--support)" font-weight="600">$388 S1</text>
<text x="1058" y="532.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="557.5" x2="1052" y2="557.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="551.5" font-size="11.5" fill="var(--support)" font-weight="600">$378 S2</text>
<text x="1058" y="563.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="501.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="493.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $396 (2026-09-21)</text>
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
| R3 | $499 | 2 | 2025-10-01·2026-04-24의 스윙 고점대 |
| R2 | $476 | 4 | 2025-10-27·2025-12-11·2026-06-23·2026-08-27의 스윙 고점대. **마지막 터치가 FY2026 Q3 실적 급등일($464.89)** 직후다 |
| R1 | $449 | 4 | 2026-02-25·03-05·03-23·07-13의 스윙 고점대. 2026년 상반기 거래 레인지의 상단 |
| **현재가** | **$384.97** (2026-09-18 종가) | — | S1 바로 아래 — R1까지 +16.6%, S2까지 −1.8% |
| S1 | $388 | 2 | 2026-04-13·2026-08-24의 스윙 저점대. **현재가가 이 지지대 아래로 내려와 있다**(−0.8%) |
| S2 | $378 | 2 | 2025-11-18·2026-03-27의 스윙 저점대. 현재가 바로 아래의 유효 지지 |
| 참고선 | $362.55 | — | 최근 1년 장중 최저(종가 기준 최저는 **$367.70, 2026-09-15**). 현재가 대비 −5.8%로, 이 구간이 깨지면 1년 신저가가 된다 |

---

## 3. 관측된 특이 구간 — 2026-08-27 실적 급등과 3주 만의 전량 반납

- **2026-08-26~27** — FY2026 3분기 실적 발표(Ansys 비용 시너지 조기 실현, 연간 가이던스 상향) 다음날 종가가 $410.00 → **$464.89로 +13.39%** 급등했다([최근 뉴스 / 이슈](./08_news.md)). 이 급등이 R2 $476 클러스터의 마지막 터치를 만들었다.
- **2026-08-28 ~ 09-15** — 그 상승분을 3주 만에 전부 반납했다. 회사 고유 악재 없이 국채 금리 상승發 디레이팅이 이어지며 **9월 15일 종가 $367.70으로 52주 최저**를 새로 찍었다(장중 최저 $362.55). 실적 발표 **전** 수준($410.00)마저 밑돈 것이라, 시장이 Q3 실적의 내용을 되물린 셈이다.
- **2026-07-17** — 중국 Moonshot AI의 오픈소스 EDA 자율설계 시연 당일 종가 −7.85%($417.03 → $384.28), 거래량 504만 주로 평소(일 208만 주 내외)의 **2.4배**였다. [Cadence](../cadence_design_systems/09_technical_daily.md)도 같은 날 −9.47%로, **개별 악재가 아니라 업종 재평가**였다.
- 그 결과 현재가 $384.97은 **S1 $388 아래**에 놓여 있다. 위로는 R1 $449까지 16.6%가 비어 있고, 아래로는 S2 $378과 1년 최저 구간($362~368)이 5% 이내에 몰려 있다 — **좁은 구간에 하방 레벨이 밀집한 자리**다.

> 세 구간 모두 [Cadence](../cadence_design_systems/09_technical_daily.md)와 시점이 겹친다. 다만 Synopsys만 9월에 **52주 최저를 갱신**했다 — Cadence의 1년 최저는 2026년 4월이고 9월 저점은 그보다 위였다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-22~2026-09-21. 수집 시점: 2026-09-21. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `uv run python scripts/gen_technical_chart.py SNPS --name Synopsys --close-on 2026-09-18 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **마지막 봉이 미완성이다.** 스크립트는 종료일을 고정하는 옵션이 없어 원자료를 수집 시점(2026-09-21 장중)까지 받는다(`scripts/gen_technical_chart.py` docstring "한계"). 그래서 차트의 맨 오른쪽 봉과 스크립트가 자동 생성한 현재가 행($396.49, 2026-09-21)은 **확정 종가가 아니다** — 위 2절 표의 현재가는 `--close-on 2026-09-18`로 지정한 **마지막 완료 거래일 종가 $384.97**로 바꿔 적었고, 문서 전체가 이 값을 기준으로 한다.
    - **현재가가 S1 아래에 있어 "지지"라는 표현이 성립하지 않는다.** S1 $388은 2026-04-13·08-24에 지지로 작동했으나 9월에 하향 이탈했으므로, 지금 레짐에서는 **저항으로 바뀐 레벨**로 읽는 것이 맞다. 3. 관측된 특이 구간의 급등·반납 구간이 이 레벨을 가로지른다.
    - 해당 기간에 **주식분할·병합은 없다.** 희석주식수 증가(+16.10%)는 Ansys 인수 대가 신주 발행 때문이며([핵심 지표](./04_metrics.md) A.4), 발행은 2025-07-17로 이 차트 구간의 시작(2025-09-22)보다 앞서므로 구간 내 가격 연속성은 깨지지 않는다.

---

*작성일: 2026-09-21*
