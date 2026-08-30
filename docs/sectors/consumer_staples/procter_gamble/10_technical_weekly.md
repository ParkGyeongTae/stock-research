# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 단기 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 이 차트의 마지막 종가는 **2026-08-28 $143.78**로, [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 **2026-08-27 $143.14**보다 한 거래일 뒤다. 일봉 원자료에 2026-08-28이 아직 들어오지 않아 생긴 차이이며(0.45% 차이), **다른 문서의 밸류에이션 수치는 모두 일봉 기준 $143.14를 쓴다.** 두 값은 배당·분할 조정 여부의 차이가 아니다 — 둘 다 원주가다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

<div class="pg-chart">
<style>
.pg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .pg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .pg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.pg-chart svg { width:100%; height:auto; display:block; }
.pg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.pg-chart .title { fill: var(--ink); font-weight:600; }
.pg-chart .grid { stroke: var(--grid); stroke-width:1; }
.pg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="프록터 앤 갬블(PG) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">프록터 앤 갬블 (PG) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $143.78 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="535.5" x2="1052" y2="535.5" class="grid"/>
<text x="52" y="539.5" font-size="11" text-anchor="end" fill="var(--muted)">130</text>
<line x1="60" y1="445.0" x2="1052" y2="445.0" class="grid"/>
<text x="52" y="449.0" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="354.6" x2="1052" y2="354.6" class="grid"/>
<text x="52" y="358.6" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="264.1" x2="1052" y2="264.1" class="grid"/>
<text x="52" y="268.1" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="173.6" x2="1052" y2="173.6" class="grid"/>
<text x="52" y="177.6" font-size="11" text-anchor="end" fill="var(--muted)">170</text>
<line x1="60" y1="83.1" x2="1052" y2="83.1" class="grid"/>
<text x="52" y="87.1" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.0" y1="56.0" x2="130.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.0" y1="626.0" x2="130.0" y2="631.0" class="axis"/>
<text x="130.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="326.9" y1="56.0" x2="326.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="326.9" y1="626.0" x2="326.9" y2="631.0" class="axis"/>
<text x="326.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="523.8" y1="56.0" x2="523.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="523.8" y1="626.0" x2="523.8" y2="631.0" class="axis"/>
<text x="523.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="724.5" y1="56.0" x2="724.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="724.5" y1="626.0" x2="724.5" y2="631.0" class="axis"/>
<text x="724.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.4" y1="56.0" x2="921.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.4" y1="626.0" x2="921.4" y2="631.0" class="axis"/>
<text x="921.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="402.3" x2="61.9" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="408.4" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="65.7" y1="400.4" x2="65.7" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="406.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="69.5" y1="379.6" x2="69.5" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="401.2" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="73.3" y1="401.2" x2="73.3" y2="427.2" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="406.9" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="77.0" y1="416.4" x2="77.0" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="416.5" width="2.35" height="32.3" fill="var(--down)"/>
<line x1="80.8" y1="417.6" x2="80.8" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="429.4" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="84.6" y1="401.0" x2="84.6" y2="435.7" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="405.1" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="88.4" y1="411.6" x2="88.4" y2="455.9" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="412.9" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="92.2" y1="411.8" x2="92.2" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="418.0" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="96.0" y1="387.4" x2="96.0" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="390.4" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="99.8" y1="378.9" x2="99.8" y2="408.7" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="385.7" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="103.5" y1="367.3" x2="103.5" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="381.4" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="107.3" y1="357.1" x2="107.3" y2="383.3" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="377.5" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="111.1" y1="354.6" x2="111.1" y2="407.8" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="355.7" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="114.9" y1="302.1" x2="114.9" y2="352.9" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="305.2" width="2.35" height="47.7" fill="var(--up)"/>
<line x1="118.7" y1="248.5" x2="118.7" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="287.1" width="2.35" height="19.5" fill="var(--up)"/>
<line x1="122.5" y1="255.8" x2="122.5" y2="295.1" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="263.2" width="2.35" height="31.7" fill="var(--up)"/>
<line x1="126.3" y1="219.0" x2="126.3" y2="258.6" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="231.7" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="130.0" y1="216.0" x2="130.0" y2="265.2" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="239.3" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="133.8" y1="235.9" x2="133.8" y2="292.1" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="241.4" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="137.6" y1="215.7" x2="137.6" y2="299.9" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="240.4" width="2.35" height="37.0" fill="var(--up)"/>
<line x1="141.4" y1="226.8" x2="141.4" y2="296.8" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="233.1" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="145.2" y1="219.0" x2="145.2" y2="284.6" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="250.3" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="149.0" y1="243.6" x2="149.0" y2="304.1" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="247.2" width="2.35" height="50.5" fill="var(--down)"/>
<line x1="152.8" y1="254.5" x2="152.8" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="265.0" width="2.35" height="34.0" fill="var(--up)"/>
<line x1="156.5" y1="256.1" x2="156.5" y2="349.5" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="263.1" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="160.3" y1="289.5" x2="160.3" y2="333.4" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="297.7" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="164.1" y1="313.7" x2="164.1" y2="417.6" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="313.9" width="2.35" height="102.0" fill="var(--down)"/>
<line x1="167.9" y1="338.4" x2="167.9" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="353.2" width="2.35" height="51.6" fill="var(--up)"/>
<line x1="171.7" y1="319.1" x2="171.7" y2="361.4" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="329.0" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="175.5" y1="296.0" x2="175.5" y2="337.0" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="308.5" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="179.3" y1="259.3" x2="179.3" y2="343.2" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="263.2" width="2.35" height="56.9" fill="var(--up)"/>
<line x1="183.1" y1="253.1" x2="183.1" y2="278.1" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="264.5" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="186.8" y1="219.8" x2="186.8" y2="297.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="252.8" width="2.35" height="25.1" fill="var(--up)"/>
<line x1="190.6" y1="230.5" x2="190.6" y2="272.1" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="248.7" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="194.4" y1="246.0" x2="194.4" y2="326.2" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="249.6" width="2.35" height="50.7" fill="var(--down)"/>
<line x1="198.2" y1="293.4" x2="198.2" y2="355.7" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="318.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="202.0" y1="293.5" x2="202.0" y2="452.5" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="323.2" width="2.35" height="105.7" fill="var(--down)"/>
<line x1="205.8" y1="366.2" x2="205.8" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="366.2" width="2.35" height="53.2" fill="var(--up)"/>
<line x1="209.6" y1="363.7" x2="209.6" y2="421.3" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="379.1" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="213.3" y1="375.9" x2="213.3" y2="450.0" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="378.4" width="2.35" height="49.0" fill="var(--down)"/>
<line x1="217.1" y1="440.6" x2="217.1" y2="540.0" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="449.6" width="2.35" height="64.6" fill="var(--down)"/>
<line x1="220.9" y1="397.6" x2="220.9" y2="504.5" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="405.7" width="2.35" height="88.0" fill="var(--up)"/>
<line x1="224.7" y1="388.5" x2="224.7" y2="439.8" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="389.8" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="228.5" y1="377.3" x2="228.5" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="399.6" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="232.3" y1="382.1" x2="232.3" y2="413.7" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="398.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="236.1" y1="399.0" x2="236.1" y2="454.5" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="400.4" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="239.8" y1="367.1" x2="239.8" y2="461.1" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="419.7" width="2.35" height="35.2" fill="var(--down)"/>
<line x1="243.6" y1="386.6" x2="243.6" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="402.3" width="2.35" height="57.7" fill="var(--up)"/>
<line x1="247.4" y1="379.1" x2="247.4" y2="404.4" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="384.7" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="251.2" y1="348.9" x2="251.2" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="357.0" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="255.0" y1="353.4" x2="255.0" y2="426.8" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="363.8" width="2.35" height="60.5" fill="var(--down)"/>
<line x1="258.8" y1="420.7" x2="258.8" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="433.3" width="2.35" height="37.5" fill="var(--down)"/>
<line x1="262.6" y1="435.2" x2="262.6" y2="487.7" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="445.4" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="266.4" y1="428.8" x2="266.4" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="450.4" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="270.1" y1="459.0" x2="270.1" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="461.3" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="273.9" y1="472.7" x2="273.9" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="485.0" width="2.35" height="84.4" fill="var(--down)"/>
<line x1="277.7" y1="527.7" x2="277.7" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="560.4" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="281.5" y1="562.5" x2="281.5" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="580.0" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="285.3" y1="508.4" x2="285.3" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="548.4" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="289.1" y1="485.7" x2="289.1" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="488.3" width="2.35" height="51.8" fill="var(--up)"/>
<line x1="292.9" y1="476.4" x2="292.9" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="488.5" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="296.6" y1="430.3" x2="296.6" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="436.3" width="2.35" height="50.8" fill="var(--up)"/>
<line x1="300.4" y1="412.8" x2="300.4" y2="447.8" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="421.8" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="304.2" y1="379.9" x2="304.2" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="384.2" width="2.35" height="33.1" fill="var(--up)"/>
<line x1="308.0" y1="347.6" x2="308.0" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="349.1" width="2.35" height="38.2" fill="var(--up)"/>
<line x1="311.8" y1="336.9" x2="311.8" y2="370.2" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="346.2" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="315.6" y1="314.4" x2="315.6" y2="363.4" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="343.5" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="319.4" y1="328.2" x2="319.4" y2="361.4" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="330.9" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="323.1" y1="312.5" x2="323.1" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="330.1" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="326.9" y1="314.2" x2="326.9" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="319.1" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="330.7" y1="311.1" x2="330.7" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="323.4" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="334.5" y1="335.3" x2="334.5" y2="443.7" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="347.4" width="2.35" height="70.8" fill="var(--down)"/>
<line x1="338.3" y1="411.6" x2="338.3" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="414.6" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="342.1" y1="408.0" x2="342.1" y2="442.5" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="421.4" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="345.9" y1="421.2" x2="345.9" y2="482.8" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="426.9" width="2.35" height="33.9" fill="var(--down)"/>
<line x1="349.6" y1="441.0" x2="349.6" y2="476.3" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="445.0" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="353.4" y1="430.8" x2="353.4" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="451.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="357.2" y1="433.8" x2="357.2" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="436.5" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="361.0" y1="434.7" x2="361.0" y2="480.3" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="438.4" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="364.8" y1="414.4" x2="364.8" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="418.5" width="2.35" height="53.3" fill="var(--up)"/>
<line x1="368.6" y1="383.9" x2="368.6" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="384.2" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="372.4" y1="366.4" x2="372.4" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="366.4" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="376.2" y1="327.8" x2="376.2" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="334.5" width="2.35" height="34.3" fill="var(--up)"/>
<line x1="379.9" y1="332.8" x2="379.9" y2="359.0" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="339.6" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="383.7" y1="281.2" x2="383.7" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="299.7" width="2.35" height="44.3" fill="var(--up)"/>
<line x1="387.5" y1="282.7" x2="387.5" y2="315.3" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="296.8" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="391.3" y1="286.1" x2="391.3" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="300.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="395.1" y1="299.8" x2="395.1" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="300.6" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="398.9" y1="292.0" x2="398.9" y2="340.1" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="294.8" width="2.35" height="31.1" fill="var(--down)"/>
<line x1="402.7" y1="331.0" x2="402.7" y2="405.7" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="332.0" width="2.35" height="64.2" fill="var(--down)"/>
<line x1="406.4" y1="384.6" x2="406.4" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="386.1" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="410.2" y1="374.0" x2="410.2" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="385.7" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="414.0" y1="353.8" x2="414.0" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="358.7" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="417.8" y1="344.6" x2="417.8" y2="373.8" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="356.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="421.6" y1="335.8" x2="421.6" y2="384.2" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="338.8" width="2.35" height="32.9" fill="var(--up)"/>
<line x1="425.4" y1="331.7" x2="425.4" y2="365.9" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="341.2" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="429.2" y1="348.9" x2="429.2" y2="382.1" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="354.1" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="432.9" y1="321.4" x2="432.9" y2="371.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="328.1" width="2.35" height="29.7" fill="var(--up)"/>
<line x1="436.7" y1="286.9" x2="436.7" y2="337.2" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="296.6" width="2.35" height="32.3" fill="var(--up)"/>
<line x1="440.5" y1="284.6" x2="440.5" y2="308.8" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="296.7" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="444.3" y1="278.8" x2="444.3" y2="304.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="291.1" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="448.1" y1="286.4" x2="448.1" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="290.1" width="2.35" height="41.5" fill="var(--down)"/>
<line x1="451.9" y1="312.2" x2="451.9" y2="346.2" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="322.5" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="455.7" y1="306.8" x2="455.7" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="313.8" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="459.5" y1="310.7" x2="459.5" y2="340.6" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="320.2" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="463.2" y1="306.4" x2="463.2" y2="340.4" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="323.2" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="467.0" y1="311.3" x2="467.0" y2="342.1" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="314.3" width="2.35" height="26.0" fill="var(--down)"/>
<line x1="470.8" y1="343.0" x2="470.8" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="343.9" width="2.35" height="48.1" fill="var(--down)"/>
<line x1="474.6" y1="386.3" x2="474.6" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="401.8" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="478.4" y1="394.7" x2="478.4" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="402.6" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="482.2" y1="342.8" x2="482.2" y2="397.6" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="372.2" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="486.0" y1="342.1" x2="486.0" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="373.9" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="489.7" y1="333.9" x2="489.7" y2="376.8" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="353.9" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="493.5" y1="341.5" x2="493.5" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="341.8" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="497.3" y1="322.9" x2="497.3" y2="351.1" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="341.5" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="501.1" y1="338.8" x2="501.1" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="342.1" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="504.9" y1="321.7" x2="504.9" y2="353.8" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="330.5" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="508.7" y1="331.0" x2="508.7" y2="404.2" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="338.6" width="2.35" height="59.9" fill="var(--down)"/>
<line x1="512.5" y1="366.8" x2="512.5" y2="422.4" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="401.6" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="516.2" y1="377.3" x2="516.2" y2="416.7" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="397.3" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="520.0" y1="382.1" x2="520.0" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="385.9" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="523.8" y1="359.9" x2="523.8" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="377.9" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="527.6" y1="342.8" x2="527.6" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="349.1" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="531.4" y1="341.0" x2="531.4" y2="382.4" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="353.2" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="535.2" y1="296.7" x2="535.2" y2="388.2" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="299.0" width="2.35" height="83.0" fill="var(--up)"/>
<line x1="539.0" y1="267.7" x2="539.0" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="281.4" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="542.7" y1="265.6" x2="542.7" y2="291.6" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="280.7" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="546.5" y1="273.4" x2="546.5" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="286.6" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="550.3" y1="248.4" x2="550.3" y2="281.0" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="254.8" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="554.1" y1="253.5" x2="554.1" y2="285.7" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="254.8" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="557.9" y1="252.8" x2="557.9" y2="285.2" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="260.9" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="561.7" y1="239.4" x2="561.7" y2="261.4" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="251.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="565.5" y1="239.5" x2="565.5" y2="255.0" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="249.1" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="569.3" y1="235.7" x2="569.3" y2="266.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="243.7" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="573.0" y1="245.4" x2="573.0" y2="312.1" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="248.0" width="2.35" height="51.4" fill="var(--down)"/>
<line x1="576.8" y1="285.8" x2="576.8" y2="311.7" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="300.6" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="580.6" y1="280.6" x2="580.6" y2="322.7" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="280.9" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="584.4" y1="225.0" x2="584.4" y2="289.0" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="252.4" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="588.2" y1="221.5" x2="588.2" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="223.7" width="2.35" height="29.8" fill="var(--up)"/>
<line x1="592.0" y1="197.5" x2="592.0" y2="234.6" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="202.1" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="595.8" y1="188.6" x2="595.8" y2="228.4" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="195.0" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="599.5" y1="186.8" x2="599.5" y2="217.5" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="195.8" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="603.3" y1="220.9" x2="603.3" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="223.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="607.1" y1="182.9" x2="607.1" y2="231.3" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="200.2" width="2.35" height="28.3" fill="var(--up)"/>
<line x1="610.9" y1="194.2" x2="610.9" y2="225.9" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="202.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="614.7" y1="183.8" x2="614.7" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="189.4" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="618.5" y1="179.0" x2="618.5" y2="222.7" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="184.8" width="2.35" height="34.7" fill="var(--down)"/>
<line x1="622.3" y1="207.9" x2="622.3" y2="248.6" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="213.5" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="626.0" y1="195.0" x2="626.0" y2="220.8" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="204.3" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="629.8" y1="165.3" x2="629.8" y2="223.7" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="192.1" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="633.6" y1="172.8" x2="633.6" y2="213.6" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="181.7" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="637.4" y1="168.7" x2="637.4" y2="281.8" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="172.9" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="641.2" y1="158.1" x2="641.2" y2="203.7" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="165.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="645.0" y1="176.5" x2="645.0" y2="211.4" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="179.0" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="648.8" y1="156.5" x2="648.8" y2="190.7" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="181.1" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="652.5" y1="156.6" x2="652.5" y2="186.5" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="159.7" width="2.35" height="25.7" fill="var(--up)"/>
<line x1="656.3" y1="109.9" x2="656.3" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="123.0" width="2.35" height="41.3" fill="var(--up)"/>
<line x1="660.1" y1="101.8" x2="660.1" y2="151.5" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="123.5" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="663.9" y1="107.5" x2="663.9" y2="170.2" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="131.0" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="667.7" y1="126.7" x2="667.7" y2="161.3" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="137.3" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="671.5" y1="137.4" x2="671.5" y2="189.4" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="139.9" width="2.35" height="43.9" fill="var(--down)"/>
<line x1="675.3" y1="160.9" x2="675.3" y2="207.4" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="163.8" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="679.1" y1="129.2" x2="679.1" y2="187.6" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="162.0" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="682.8" y1="160.2" x2="682.8" y2="191.4" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="164.8" width="2.35" height="25.0" fill="var(--down)"/>
<line x1="686.6" y1="176.7" x2="686.6" y2="218.9" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="180.1" width="2.35" height="37.8" fill="var(--down)"/>
<line x1="690.4" y1="194.0" x2="690.4" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="194.3" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="694.2" y1="168.5" x2="694.2" y2="213.7" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="177.8" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="698.0" y1="106.7" x2="698.0" y2="184.2" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="116.8" width="2.35" height="64.9" fill="var(--up)"/>
<line x1="701.8" y1="79.3" x2="701.8" y2="111.2" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="89.8" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="705.6" y1="81.7" x2="705.6" y2="142.3" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="91.1" width="2.35" height="48.0" fill="var(--down)"/>
<line x1="709.3" y1="139.6" x2="709.3" y2="174.3" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="140.7" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="713.1" y1="148.5" x2="713.1" y2="197.6" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="160.5" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="716.9" y1="166.7" x2="716.9" y2="206.6" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="177.9" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="720.7" y1="182.8" x2="720.7" y2="225.6" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="185.7" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="724.5" y1="232.4" x2="724.5" y2="287.0" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="238.7" width="2.35" height="38.5" fill="var(--down)"/>
<line x1="728.3" y1="248.3" x2="728.3" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="253.9" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="732.1" y1="190.4" x2="732.1" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="226.8" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="735.8" y1="174.2" x2="735.8" y2="217.0" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="203.3" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="739.6" y1="174.3" x2="739.6" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="192.0" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="743.4" y1="161.1" x2="743.4" y2="243.3" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="194.5" width="2.35" height="43.4" fill="var(--down)"/>
<line x1="747.2" y1="168.6" x2="747.2" y2="244.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="171.5" width="2.35" height="62.2" fill="var(--up)"/>
<line x1="751.0" y1="131.5" x2="751.0" y2="175.5" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="138.9" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="754.8" y1="83.2" x2="754.8" y2="147.9" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="119.8" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="758.6" y1="83.2" x2="758.6" y2="204.2" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="112.5" width="2.35" height="79.5" fill="var(--down)"/>
<line x1="762.4" y1="163.8" x2="762.4" y2="226.8" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="188.4" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="766.1" y1="176.2" x2="766.1" y2="244.2" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="191.4" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="769.9" y1="130.2" x2="769.9" y2="232.7" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="190.8" width="2.35" height="39.4" fill="var(--down)"/>
<line x1="773.7" y1="191.5" x2="773.7" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="201.6" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="777.5" y1="158.7" x2="777.5" y2="211.8" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="167.9" width="2.35" height="32.5" fill="var(--up)"/>
<line x1="781.3" y1="174.1" x2="781.3" y2="295.0" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="174.6" width="2.35" height="80.3" fill="var(--down)"/>
<line x1="785.1" y1="235.5" x2="785.1" y2="272.7" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="254.7" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="788.9" y1="255.9" x2="788.9" y2="287.5" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="256.0" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="792.6" y1="233.1" x2="792.6" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="234.4" width="2.35" height="52.9" fill="var(--up)"/>
<line x1="796.4" y1="206.5" x2="796.4" y2="233.2" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="211.1" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="800.2" y1="164.7" x2="800.2" y2="216.4" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="174.6" width="2.35" height="41.8" fill="var(--up)"/>
<line x1="804.0" y1="182.3" x2="804.0" y2="241.4" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="182.5" width="2.35" height="45.2" fill="var(--down)"/>
<line x1="807.8" y1="227.7" x2="807.8" y2="264.9" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="233.4" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="811.6" y1="246.5" x2="811.6" y2="285.3" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="256.1" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="815.4" y1="248.4" x2="815.4" y2="289.7" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="265.4" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="819.1" y1="241.2" x2="819.1" y2="281.0" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="256.6" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="822.9" y1="253.4" x2="822.9" y2="300.7" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="256.0" width="2.35" height="34.7" fill="var(--down)"/>
<line x1="826.7" y1="302.1" x2="826.7" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="304.1" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="830.5" y1="273.0" x2="830.5" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="279.5" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="834.3" y1="276.3" x2="834.3" y2="355.4" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="285.5" width="2.35" height="63.2" fill="var(--down)"/>
<line x1="838.1" y1="318.3" x2="838.1" y2="354.4" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="322.8" width="2.35" height="29.5" fill="var(--up)"/>
<line x1="841.9" y1="291.1" x2="841.9" y2="325.0" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="315.1" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="845.6" y1="254.8" x2="845.6" y2="316.8" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="276.1" width="2.35" height="38.5" fill="var(--up)"/>
<line x1="849.4" y1="275.9" x2="849.4" y2="309.1" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="278.7" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="853.2" y1="259.0" x2="853.2" y2="295.8" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="263.9" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="857.0" y1="261.7" x2="857.0" y2="301.3" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="267.6" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="860.8" y1="249.0" x2="860.8" y2="300.6" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="283.3" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="864.6" y1="299.6" x2="864.6" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="299.6" width="2.35" height="32.4" fill="var(--down)"/>
<line x1="868.4" y1="314.9" x2="868.4" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="332.7" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="872.2" y1="325.9" x2="872.2" y2="359.5" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="341.0" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="875.9" y1="336.2" x2="875.9" y2="382.0" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="341.9" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="879.7" y1="287.6" x2="879.7" y2="349.3" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="332.0" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="883.5" y1="325.9" x2="883.5" y2="368.4" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="340.0" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="887.3" y1="352.6" x2="887.3" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="353.7" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="891.1" y1="360.2" x2="891.1" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="375.7" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="894.9" y1="341.0" x2="894.9" y2="399.7" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="346.2" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="898.7" y1="350.9" x2="898.7" y2="385.9" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="353.7" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="902.4" y1="364.6" x2="902.4" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="371.8" width="2.35" height="42.1" fill="var(--down)"/>
<line x1="906.2" y1="416.9" x2="906.2" y2="461.9" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="418.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="910.0" y1="368.6" x2="910.0" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="404.7" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="913.8" y1="394.0" x2="913.8" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="402.2" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="917.6" y1="399.2" x2="917.6" y2="433.8" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="401.6" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="921.4" y1="424.0" x2="921.4" y2="466.6" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="428.1" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="925.2" y1="382.6" x2="925.2" y2="429.6" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="404.1" width="2.35" height="20.4" fill="var(--up)"/>
<line x1="928.9" y1="339.6" x2="928.9" y2="407.8" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="353.2" width="2.35" height="51.5" fill="var(--up)"/>
<line x1="932.7" y1="336.7" x2="932.7" y2="383.6" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="338.6" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="936.5" y1="264.2" x2="936.5" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="271.6" width="2.35" height="61.1" fill="var(--up)"/>
<line x1="940.3" y1="235.7" x2="940.3" y2="300.1" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="263.5" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="944.1" y1="244.5" x2="944.1" y2="302.4" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="257.0" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="947.9" y1="198.5" x2="947.9" y2="261.4" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="199.0" width="2.35" height="62.2" fill="var(--up)"/>
<line x1="951.7" y1="204.8" x2="951.7" y2="337.5" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="216.2" width="2.35" height="105.5" fill="var(--down)"/>
<line x1="955.5" y1="289.9" x2="955.5" y2="352.9" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="326.1" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="959.2" y1="323.3" x2="959.2" y2="406.6" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="337.7" width="2.35" height="68.6" fill="var(--down)"/>
<line x1="963.0" y1="389.4" x2="963.0" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="389.4" width="2.35" height="31.1" fill="var(--down)"/>
<line x1="966.8" y1="394.7" x2="966.8" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="416.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="970.6" y1="382.3" x2="970.6" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="398.4" width="2.35" height="19.5" fill="var(--up)"/>
<line x1="974.4" y1="376.4" x2="974.4" y2="424.6" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="382.3" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="978.2" y1="332.7" x2="978.2" y2="425.0" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="371.0" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="982.0" y1="343.8" x2="982.0" y2="391.8" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="377.9" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="985.7" y1="364.1" x2="985.7" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="387.0" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="989.5" y1="391.2" x2="989.5" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="392.7" width="2.35" height="38.2" fill="var(--down)"/>
<line x1="993.3" y1="403.1" x2="993.3" y2="444.2" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="404.9" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="997.1" y1="367.8" x2="997.1" y2="422.2" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="404.2" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="1000.9" y1="370.6" x2="1000.9" y2="455.4" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="385.9" width="2.35" height="45.4" fill="var(--up)"/>
<line x1="1004.7" y1="350.7" x2="1004.7" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="358.1" width="2.35" height="34.6" fill="var(--up)"/>
<line x1="1008.5" y1="327.2" x2="1008.5" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="351.1" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="1012.2" y1="324.3" x2="1012.2" y2="376.6" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="353.6" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="1016.0" y1="339.5" x2="1016.0" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="341.8" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="1019.8" y1="323.0" x2="1019.8" y2="394.4" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="348.4" width="2.35" height="32.9" fill="var(--down)"/>
<line x1="1023.6" y1="315.5" x2="1023.6" y2="402.9" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="354.8" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="1027.4" y1="350.4" x2="1027.4" y2="396.2" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="358.6" width="2.35" height="19.5" fill="var(--down)"/>
<line x1="1031.2" y1="321.3" x2="1031.2" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="374.0" width="2.35" height="30.4" fill="var(--down)"/>
<line x1="1035.0" y1="368.1" x2="1035.0" y2="410.8" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="392.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1038.7" y1="386.6" x2="1038.7" y2="414.1" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="402.3" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="1042.5" y1="388.7" x2="1042.5" y2="425.7" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="402.7" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="1046.3" y1="383.5" x2="1046.3" y2="420.5" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="397.6" width="2.35" height="19.0" fill="var(--down)"/>
<line x1="1050.1" y1="405.2" x2="1050.1" y2="417.8" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="410.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="60" y1="326.0" x2="1052" y2="326.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="329.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$153 R1</text>
<text x="1058" y="341.5" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="274.1" x2="1052" y2="274.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="277.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$159 R2</text>
<text x="1058" y="289.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="211.3" x2="1052" y2="211.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$166 R3</text>
<text x="1058" y="226.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="446.7" x2="1052" y2="446.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="440.7" font-size="11.5" fill="var(--support)" font-weight="600">$140 S1</text>
<text x="1058" y="452.7" font-size="9.5" fill="var(--muted)">터치 11회</text>
<circle cx="1052.0" cy="410.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="402.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $144 (2026-08-28)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $166 | 3 | 2022-01-17·2022-04-18·2026-02-23 — **4년 간격으로 세 번 닿은 뒤 매번 되밀린 레벨.** 5년 최고($180.43)와는 다른 가격대다 |
| R2 | $159 | 4 | 2023-04-17·2023-08-07·2025-09-15·2025-10-20 — 2023년 상단과 2025년 가을 고점이 같은 가격대에서 겹친다 |
| R1 | $153 | 5 | 2022-08-15·2023-01-09·2023-11-27·2026-04-20·2026-07-13 — 5년에 걸쳐 반복 터치. 현재가에서 가장 가까운 저항이다 |
| **현재가** | **$143.78** (2026-08-28 종가)[^t1] | — | R1($153)과 S1($140) 사이. R1까지 +6.4%, S1까지 −2.6% |
| S1 | $140 | 11 | 2021-10-04·2022-03-07·2022-07-25·2023-02-06·2023-05-29·2023-10-02·2023-12-11·2026-01-05·2026-04-06·2026-06-01·2026-07-27 — **5년 내내 11번 터치된 이 차트의 중심축.** 2021년부터 2026년까지 매년 최소 한 번씩 닿았다 |
| 참고선 | $180.43 | — | 5년 최고가(2024년 하반기 형성). 현재가 대비 +25%로 멀고 이후 되돌리지 못해 근시일 저항으로 보지 않는다 |
| 참고선 | $122.18 | — | 5년 최저가(2022년 하락 국면). 현재가 대비 −15%로, S1이 뚫렸을 때 다음으로 볼 구간이다 |

[^t1]: 이 표의 현재가만 2026-08-28 기준이다. 위 `???` 블록의 대조 결과 참고 — 회사 폴더의 다른 문서는 모두 2026-08-27 종가 $143.14를 쓴다.

**$140이 5년 내내 같은 자리를 지켜온 것이 이 차트의 핵심이다.** 2021년 10월부터 2026년 7월까지 11번 터치됐고, 그 사이 주가는 $122까지 빠졌다가 $180까지 올랐다가 다시 돌아왔다. 즉 **지금 가격($143.78)은 5년 밴드의 상단도 하단도 아니라 그 축 바로 위**에 있다. 반대로 저항은 $153·$159·$166으로 촘촘하게 겹쳐 있어, 위로는 6% 안에서 첫 저항을 만난다.

---

## 3. 관측된 특이 구간 — 2026년 상반기 고점 이탈

- 2026-02-23 주에 R3($166) 클러스터를 세 번째로 터치한 뒤(종가 기준 최고 $167.20, 2026-02-27) **6개월에 걸쳐 −14.4% 밀려 내려와** 2026-07-27 주에 S1($140)을 다시 터치했다. 같은 기간의 실적 흐름(FY2026 유기적 성장 +1%, FY26 Q4 0%)은 [핵심 지표](./04_metrics.md) C절에 있다.
- **주봉 기준으로도 갭 수준의 불연속은 없었다.** 단일 주간 변동폭이 이례적으로 컸던 구간이 나타나지 않아, 특정 사건이 가격대를 재설정한 것이 아니라 배수가 완만하게 눌린 흐름으로 본다.
- 그래서 2021~2023년에 형성된 레벨($140·$153·$159·$166)을 지금도 유효한 것으로 그대로 뒀다 — 5년 전 스윙대가 2026년에도 반복 터치되고 있다는 점이 그 근거다(R3는 2022-01·2022-04·2026-02, S1은 2021-10~2026-07).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PG --name "프록터 앤 갬블" --interval 1wk --close-on 2026-08-27 --emit all` (기본 옵션 그대로, `--force-level`·`--levels` 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 일봉과 마찬가지로 **지지 클러스터가 S1 하나뿐**이다. 5년 최저($122.18)를 참고선으로 남겨 S1 하향 이탈 시 볼 구간을 표시했다.
    - 기간 내 주식분할·유상증자는 없었다. **배당은 20회 지급됐고 이 차트는 원주가라 배당이 반영되지 않았다** — 5년 총수익률은 이 차트가 보여주는 가격 변화보다 연 2~3%p 높다.
    - `--close-on 2026-08-27`을 지정했으나 주봉 원자료가 2026-08-28을 포함해 마지막 종가가 하루 뒤로 잡혔다. 레벨 계산에는 영향이 없다.

---

*작성일: 2026-08-30*
