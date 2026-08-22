# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 Yahoo Finance 일봉 API에서 직접 수집했다(1년 일봉은 핵심 지표가 다루는 범위 밖). 두 문서의 특정 시점 종가가 겹치면 서로 검증용으로 대조할 수 있다 — 예: 2026-08-13 종가 $411.75는 이번 갱신 전 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 stockanalysis.com 값과 일치했다. ⚠️ **이후 갱신 참고**: 개요·핵심 지표·밸류에이션 / 적정주가·투자 판단·최종 보고서는 2026-08-21 종가($397.87) 기준으로 갱신됐으나(2026-08-22), 이 일봉 차트 자체는 아직 2026-08-14까지의 데이터만 반영한다 — 차트를 최신 가격까지 재생성하기 전까지는 이 문서의 "현재가"($421.50)가 다른 문서보다 며칠 뒤처져 있다는 점에 유의할 것.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="snps-chart">
<style>
.snps-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.snps-chart svg { width:100%; height:auto; display:block; }
.snps-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.snps-chart .title { fill: var(--ink); font-weight:600; }
.snps-chart .grid { stroke: var(--grid); stroke-width:1; }
.snps-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synopsys(SNPS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Synopsys (SNPS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $421.50 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="534.4" x2="1052" y2="534.4" class="grid"/>
<text x="52" y="538.4" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="432.6" x2="1052" y2="432.6" class="grid"/>
<text x="52" y="436.6" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="330.8" x2="1052" y2="330.8" class="grid"/>
<text x="52" y="334.8" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="229.0" x2="1052" y2="229.0" class="grid"/>
<text x="52" y="233.0" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="127.3" x2="1052" y2="127.3" class="grid"/>
<text x="52" y="131.3" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="105.5" y1="626.0" x2="105.5" y2="631.0" class="axis"/>
<text x="105.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="188.4" y1="626.0" x2="188.4" y2="631.0" class="axis"/>
<text x="188.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="354.4" y1="626.0" x2="354.4" y2="631.0" class="axis"/>
<text x="354.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="441.4" y1="626.0" x2="441.4" y2="631.0" class="axis"/>
<text x="441.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="595.5" y1="626.0" x2="595.5" y2="631.0" class="axis"/>
<text x="595.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="682.5" y1="626.0" x2="682.5" y2="631.0" class="axis"/>
<text x="682.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="765.5" y1="626.0" x2="765.5" y2="631.0" class="axis"/>
<text x="765.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="844.5" y1="626.0" x2="844.5" y2="631.0" class="axis"/>
<text x="844.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="927.5" y1="626.0" x2="927.5" y2="631.0" class="axis"/>
<text x="927.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1014.5" y1="626.0" x2="1014.5" y2="631.0" class="axis"/>
<text x="1014.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="73.8" x2="1052" y2="73.8" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="76.8" font-size="10.5" fill="var(--muted)">$626 52주 최고</text>
<line x1="129.2" y1="56.0" x2="129.2" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="135.2" y="68.0" font-size="10.5" fill="var(--down)">2025-09-10 실적발표 갭다운 (시가 -29%, 종가 -35.8%)</text>
<line x1="62.0" y1="86.5" x2="62.0" y2="114.4" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="90.8" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="65.9" y1="73.8" x2="65.9" y2="96.5" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="75.7" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="69.9" y1="76.7" x2="69.9" y2="104.9" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="85.3" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="73.8" y1="99.1" x2="73.8" y2="137.2" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="104.7" width="2.45" height="20.3" fill="var(--down)"/>
<line x1="77.8" y1="119.2" x2="77.8" y2="141.4" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="131.0" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="81.7" y1="100.8" x2="81.7" y2="132.4" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="114.0" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="85.7" y1="116.4" x2="85.7" y2="135.2" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="117.1" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="89.6" y1="127.0" x2="89.6" y2="141.5" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="135.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="93.6" y1="119.4" x2="93.6" y2="140.8" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="120.8" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="97.5" y1="97.5" x2="97.5" y2="117.1" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="102.5" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="101.5" y1="102.8" x2="101.5" y2="123.3" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="109.0" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="105.5" y1="133.7" x2="105.5" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="143.5" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="109.4" y1="140.1" x2="109.4" y2="154.2" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="143.3" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="113.4" y1="121.4" x2="113.4" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="123.3" width="2.45" height="20.3" fill="var(--up)"/>
<line x1="117.3" y1="95.2" x2="117.3" y2="138.2" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="107.4" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="121.3" y1="95.1" x2="121.3" y2="128.8" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="108.8" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="125.2" y1="96.9" x2="125.2" y2="122.2" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="105.0" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="129.2" y1="474.1" x2="129.2" y2="573.4" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="477.8" width="2.45" height="81.5" fill="var(--down)"/>
<line x1="133.1" y1="453.6" x2="133.1" y2="523.2" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="456.8" width="2.45" height="45.1" fill="var(--up)"/>
<line x1="137.1" y1="444.4" x2="137.1" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="445.2" width="2.45" height="37.4" fill="var(--down)"/>
<line x1="141.0" y1="465.2" x2="141.0" y2="500.2" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="470.3" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="145.0" y1="478.7" x2="145.0" y2="499.8" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="481.5" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="148.9" y1="474.8" x2="148.9" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="482.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="152.9" y1="364.9" x2="152.9" y2="436.7" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="371.3" width="2.45" height="40.9" fill="var(--up)"/>
<line x1="156.8" y1="334.8" x2="156.8" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="340.0" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="160.8" y1="299.0" x2="160.8" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="300.7" width="2.45" height="50.5" fill="var(--up)"/>
<line x1="164.7" y1="304.4" x2="164.7" y2="354.1" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="307.5" width="2.45" height="43.0" fill="var(--down)"/>
<line x1="168.7" y1="348.5" x2="168.7" y2="403.6" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="349.1" width="2.45" height="46.6" fill="var(--down)"/>
<line x1="172.6" y1="356.1" x2="172.6" y2="408.2" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="356.9" width="2.45" height="50.3" fill="var(--up)"/>
<line x1="176.6" y1="345.1" x2="176.6" y2="377.4" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="355.7" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="180.5" y1="347.2" x2="180.5" y2="375.0" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="355.2" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="184.5" y1="340.6" x2="184.5" y2="369.9" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="344.3" width="2.45" height="23.1" fill="var(--up)"/>
<line x1="188.4" y1="339.5" x2="188.4" y2="362.4" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="353.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="192.4" y1="352.6" x2="192.4" y2="391.2" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="362.0" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="196.4" y1="380.1" x2="196.4" y2="398.8" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="384.8" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="200.3" y1="369.0" x2="200.3" y2="392.8" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="375.2" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="204.3" y1="363.2" x2="204.3" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="363.2" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="208.2" y1="346.4" x2="208.2" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="352.5" width="2.45" height="25.5" fill="var(--up)"/>
<line x1="212.2" y1="355.1" x2="212.2" y2="370.1" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="356.3" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="216.1" y1="356.1" x2="216.1" y2="458.5" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="362.6" width="2.45" height="92.6" fill="var(--down)"/>
<line x1="220.1" y1="424.9" x2="220.1" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="433.7" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="224.0" y1="426.9" x2="224.0" y2="466.5" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="445.3" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="228.0" y1="434.9" x2="228.0" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="440.2" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="231.9" y1="441.7" x2="231.9" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="452.6" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="235.9" y1="418.7" x2="235.9" y2="462.6" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="437.4" width="2.45" height="24.4" fill="var(--up)"/>
<line x1="239.8" y1="416.7" x2="239.8" y2="434.6" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="425.8" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="243.8" y1="412.9" x2="243.8" y2="442.8" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="414.2" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="247.7" y1="400.5" x2="247.7" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="419.4" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="251.7" y1="411.4" x2="251.7" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="420.2" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="255.6" y1="384.8" x2="255.6" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="403.7" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="259.6" y1="380.9" x2="259.6" y2="409.2" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="389.3" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="263.5" y1="407.4" x2="263.5" y2="442.8" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="408.8" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="267.5" y1="418.1" x2="267.5" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="421.7" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="271.4" y1="427.0" x2="271.4" y2="455.9" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="432.6" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="275.4" y1="419.9" x2="275.4" y2="447.5" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="424.8" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="279.3" y1="427.5" x2="279.3" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="428.9" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="283.3" y1="458.8" x2="283.3" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="463.1" width="2.45" height="38.0" fill="var(--down)"/>
<line x1="287.3" y1="499.9" x2="287.3" y2="528.9" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="500.8" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="291.2" y1="510.9" x2="291.2" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="512.0" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="295.2" y1="533.8" x2="295.2" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="546.0" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="299.1" y1="531.8" x2="299.1" y2="557.9" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="532.8" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="303.1" y1="535.0" x2="303.1" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="538.2" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="307.0" y1="526.8" x2="307.0" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="533.1" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="311.0" y1="527.0" x2="311.0" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="542.0" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="314.9" y1="538.8" x2="314.9" y2="562.4" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="555.1" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="318.9" y1="536.2" x2="318.9" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="554.3" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="322.8" y1="555.6" x2="322.8" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="558.8" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="326.8" y1="533.2" x2="326.8" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="562.3" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="330.7" y1="523.1" x2="330.7" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="530.7" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="334.7" y1="550.4" x2="334.7" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="558.1" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="338.6" y1="522.4" x2="338.6" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="525.0" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="342.6" y1="523.0" x2="342.6" y2="545.8" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="531.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="346.5" y1="510.7" x2="346.5" y2="531.8" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="514.7" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="350.5" y1="495.9" x2="350.5" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="497.7" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="354.4" y1="438.7" x2="354.4" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="440.8" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="358.4" y1="425.4" x2="358.4" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="433.9" width="2.45" height="15.9" fill="var(--up)"/>
<line x1="362.3" y1="395.4" x2="362.3" y2="446.1" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="399.1" width="2.45" height="43.1" fill="var(--up)"/>
<line x1="366.3" y1="400.6" x2="366.3" y2="411.8" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="404.6" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="370.2" y1="389.6" x2="370.2" y2="403.4" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="398.5" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="374.2" y1="394.3" x2="374.2" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="396.4" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="378.2" y1="388.6" x2="378.2" y2="411.0" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="395.1" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="382.1" y1="374.3" x2="382.1" y2="408.4" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="380.0" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="386.1" y1="367.0" x2="386.1" y2="421.2" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="377.1" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="390.0" y1="376.6" x2="390.0" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="379.2" width="2.45" height="47.4" fill="var(--down)"/>
<line x1="394.0" y1="390.4" x2="394.0" y2="425.5" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="416.3" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="397.9" y1="402.1" x2="397.9" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="405.5" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="401.9" y1="398.0" x2="401.9" y2="426.6" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="400.2" width="2.45" height="26.1" fill="var(--down)"/>
<line x1="405.8" y1="396.3" x2="405.8" y2="423.1" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="411.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="409.8" y1="392.7" x2="409.8" y2="413.0" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="404.7" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="413.7" y1="363.6" x2="413.7" y2="396.3" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="369.0" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="417.7" y1="375.2" x2="417.7" y2="392.1" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="376.6" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="421.6" y1="379.1" x2="421.6" y2="387.3" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="380.2" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="425.6" y1="374.4" x2="425.6" y2="387.1" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="377.4" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="429.5" y1="362.2" x2="429.5" y2="387.8" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="373.6" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="433.5" y1="374.0" x2="433.5" y2="387.7" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="382.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="437.4" y1="382.4" x2="437.4" y2="393.8" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="385.5" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="441.4" y1="359.5" x2="441.4" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="370.7" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="445.3" y1="318.0" x2="445.3" y2="373.7" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="342.6" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="449.3" y1="311.5" x2="449.3" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="313.0" width="2.45" height="26.8" fill="var(--up)"/>
<line x1="453.2" y1="280.0" x2="453.2" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="290.7" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="457.2" y1="294.1" x2="457.2" y2="311.6" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="301.3" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="461.1" y1="271.9" x2="461.1" y2="308.2" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="279.6" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="465.1" y1="259.2" x2="465.1" y2="282.4" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="262.8" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="469.1" y1="274.8" x2="469.1" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="287.7" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="473.0" y1="315.8" x2="473.0" y2="333.7" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="320.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="477.0" y1="291.9" x2="477.0" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="310.5" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="480.9" y1="289.6" x2="480.9" y2="314.5" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="297.6" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="484.9" y1="304.7" x2="484.9" y2="345.9" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="308.5" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="488.8" y1="278.9" x2="488.8" y2="323.6" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="286.1" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="492.8" y1="279.8" x2="492.8" y2="330.8" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="284.5" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="496.7" y1="311.1" x2="496.7" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="315.6" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="500.7" y1="314.5" x2="500.7" y2="344.5" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="324.7" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="504.6" y1="319.0" x2="504.6" y2="338.9" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="323.7" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="508.6" y1="298.7" x2="508.6" y2="321.0" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="307.7" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="512.5" y1="309.0" x2="512.5" y2="381.9" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="320.0" width="2.45" height="51.6" fill="var(--down)"/>
<line x1="516.5" y1="381.3" x2="516.5" y2="405.7" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="382.6" width="2.45" height="19.3" fill="var(--down)"/>
<line x1="520.4" y1="389.4" x2="520.4" y2="417.1" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="410.8" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="524.4" y1="418.4" x2="524.4" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="421.0" width="2.45" height="74.4" fill="var(--down)"/>
<line x1="528.3" y1="482.5" x2="528.3" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="495.8" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="532.3" y1="481.8" x2="532.3" y2="521.8" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="495.5" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="536.2" y1="471.0" x2="536.2" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="479.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="540.2" y1="447.0" x2="540.2" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="455.2" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="544.1" y1="428.5" x2="544.1" y2="461.1" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="453.1" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="548.1" y1="446.3" x2="548.1" y2="483.5" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="448.7" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="552.0" y1="456.0" x2="552.0" y2="506.5" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="456.4" width="2.45" height="30.4" fill="var(--down)"/>
<line x1="556.0" y1="450.0" x2="556.0" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="458.9" width="2.45" height="28.0" fill="var(--up)"/>
<line x1="560.0" y1="479.8" x2="560.0" y2="509.3" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="482.3" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="563.9" y1="438.9" x2="563.9" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="448.3" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="567.9" y1="446.5" x2="567.9" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="448.0" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="571.8" y1="431.8" x2="571.8" y2="458.7" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="453.1" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="575.8" y1="466.4" x2="575.8" y2="499.2" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="474.6" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="579.7" y1="446.1" x2="579.7" y2="503.8" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="451.5" width="2.45" height="43.4" fill="var(--up)"/>
<line x1="583.7" y1="424.1" x2="583.7" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="434.3" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="587.6" y1="445.6" x2="587.6" y2="486.8" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="473.6" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="591.6" y1="499.5" x2="591.6" y2="525.2" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="505.9" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="595.5" y1="481.0" x2="595.5" y2="523.2" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="484.2" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="599.5" y1="470.8" x2="599.5" y2="512.8" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="484.9" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="603.4" y1="454.0" x2="603.4" y2="493.0" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="471.3" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="607.4" y1="437.3" x2="607.4" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="448.3" width="2.45" height="33.7" fill="var(--up)"/>
<line x1="611.3" y1="442.1" x2="611.3" y2="469.7" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="458.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="615.3" y1="451.1" x2="615.3" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="458.6" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="619.2" y1="455.0" x2="619.2" y2="477.4" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="458.9" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="623.2" y1="460.3" x2="623.2" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="467.3" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="627.1" y1="460.4" x2="627.1" y2="497.0" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="469.5" width="2.45" height="26.8" fill="var(--down)"/>
<line x1="631.1" y1="482.5" x2="631.1" y2="513.9" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="495.7" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="635.0" y1="476.5" x2="635.0" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="481.7" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="639.0" y1="462.2" x2="639.0" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="474.8" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="642.9" y1="461.7" x2="642.9" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="476.0" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="646.9" y1="466.7" x2="646.9" y2="488.5" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="476.9" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="650.9" y1="473.5" x2="650.9" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="481.7" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="654.8" y1="449.4" x2="654.8" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="468.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="658.8" y1="474.8" x2="658.8" y2="514.4" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="480.1" width="2.45" height="22.5" fill="var(--down)"/>
<line x1="662.7" y1="481.6" x2="662.7" y2="527.6" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="488.6" width="2.45" height="25.2" fill="var(--down)"/>
<line x1="666.7" y1="506.8" x2="666.7" y2="533.6" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="523.6" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="670.6" y1="531.3" x2="670.6" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="534.4" width="2.45" height="39.8" fill="var(--down)"/>
<line x1="674.6" y1="553.2" x2="674.6" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="568.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="678.5" y1="539.5" x2="678.5" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="541.6" width="2.45" height="12.8" fill="var(--up)"/>
<line x1="682.5" y1="527.3" x2="682.5" y2="545.6" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="527.7" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="686.4" y1="532.2" x2="686.4" y2="561.7" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="542.6" width="2.45" height="12.8" fill="var(--up)"/>
<line x1="690.4" y1="537.2" x2="690.4" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="540.4" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="694.3" y1="538.2" x2="694.3" y2="557.0" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="538.7" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="698.3" y1="503.5" x2="698.3" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="510.5" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="702.2" y1="512.0" x2="702.2" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="514.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="706.2" y1="526.4" x2="706.2" y2="556.5" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="531.1" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="710.1" y1="496.9" x2="710.1" y2="558.7" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="498.2" width="2.45" height="51.4" fill="var(--up)"/>
<line x1="714.1" y1="473.0" x2="714.1" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="483.8" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="718.0" y1="453.2" x2="718.0" y2="490.8" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="456.1" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="722.0" y1="433.4" x2="722.0" y2="460.1" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="440.0" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="725.9" y1="414.2" x2="725.9" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="427.4" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="729.9" y1="405.8" x2="729.9" y2="437.8" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="410.3" width="2.45" height="26.2" fill="var(--up)"/>
<line x1="733.8" y1="371.0" x2="733.8" y2="408.2" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="396.8" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="737.8" y1="374.1" x2="737.8" y2="390.1" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="377.1" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="741.8" y1="397.4" x2="741.8" y2="432.3" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="399.8" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="745.7" y1="326.2" x2="745.7" y2="393.5" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="329.2" width="2.45" height="64.0" fill="var(--up)"/>
<line x1="749.7" y1="328.8" x2="749.7" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="333.8" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="753.6" y1="334.9" x2="753.6" y2="373.6" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="336.9" width="2.45" height="26.7" fill="var(--down)"/>
<line x1="757.6" y1="368.2" x2="757.6" y2="388.4" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="369.1" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="761.5" y1="364.0" x2="761.5" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="366.2" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="765.5" y1="335.0" x2="765.5" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="348.8" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="769.4" y1="330.3" x2="769.4" y2="354.6" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="335.9" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="773.4" y1="305.3" x2="773.4" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="325.7" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="777.3" y1="315.9" x2="777.3" y2="335.9" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="321.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="781.3" y1="296.2" x2="781.3" y2="323.7" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="318.0" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="785.2" y1="291.9" x2="785.2" y2="329.6" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="297.3" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="789.2" y1="290.7" x2="789.2" y2="306.4" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="297.9" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="793.1" y1="295.9" x2="793.1" y2="314.2" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="303.9" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="797.1" y1="300.8" x2="797.1" y2="326.2" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="301.1" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="801.0" y1="303.0" x2="801.0" y2="321.4" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="310.4" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="805.0" y1="312.5" x2="805.0" y2="349.0" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="325.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="808.9" y1="327.1" x2="808.9" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="332.5" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="812.9" y1="328.8" x2="812.9" y2="350.0" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="342.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="816.8" y1="332.4" x2="816.8" y2="384.2" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="333.0" width="2.45" height="39.9" fill="var(--up)"/>
<line x1="820.8" y1="321.2" x2="820.8" y2="353.8" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="322.7" width="2.45" height="25.9" fill="var(--up)"/>
<line x1="824.7" y1="261.4" x2="824.7" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="280.5" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="828.7" y1="250.5" x2="828.7" y2="281.6" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="260.5" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="832.7" y1="260.3" x2="832.7" y2="283.7" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="260.5" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="836.6" y1="277.7" x2="836.6" y2="388.5" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="310.5" width="2.45" height="59.8" fill="var(--down)"/>
<line x1="840.6" y1="362.4" x2="840.6" y2="393.2" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="370.2" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="844.5" y1="342.5" x2="844.5" y2="390.4" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="346.5" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="848.5" y1="313.1" x2="848.5" y2="360.1" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="313.8" width="2.45" height="46.3" fill="var(--up)"/>
<line x1="852.4" y1="322.4" x2="852.4" y2="348.7" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="325.2" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="856.4" y1="330.1" x2="856.4" y2="361.4" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="330.1" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="860.3" y1="353.3" x2="860.3" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="355.3" width="2.45" height="47.1" fill="var(--down)"/>
<line x1="864.3" y1="374.6" x2="864.3" y2="405.4" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="384.8" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="868.2" y1="356.2" x2="868.2" y2="430.6" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="380.1" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="872.2" y1="386.9" x2="872.2" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="411.2" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="876.1" y1="403.3" x2="876.1" y2="442.8" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="416.8" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="880.1" y1="410.0" x2="880.1" y2="442.8" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="418.2" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="884.0" y1="405.1" x2="884.0" y2="426.5" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="407.6" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="888.0" y1="421.4" x2="888.0" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="428.5" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="891.9" y1="374.5" x2="891.9" y2="440.4" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="408.7" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="895.9" y1="399.9" x2="895.9" y2="427.9" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="408.2" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="899.8" y1="393.1" x2="899.8" y2="426.9" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="402.9" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="903.8" y1="371.9" x2="903.8" y2="409.2" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="402.1" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="907.7" y1="385.4" x2="907.7" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="404.2" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="911.7" y1="401.0" x2="911.7" y2="434.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="405.9" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="915.6" y1="416.3" x2="915.6" y2="455.9" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="423.8" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="919.6" y1="411.6" x2="919.6" y2="456.0" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="416.5" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="923.6" y1="433.5" x2="923.6" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="440.6" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="927.5" y1="403.2" x2="927.5" y2="425.7" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="423.4" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="931.5" y1="425.5" x2="931.5" y2="464.7" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="430.3" width="2.45" height="28.5" fill="var(--down)"/>
<line x1="935.4" y1="446.1" x2="935.4" y2="468.0" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="448.3" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="939.4" y1="429.4" x2="939.4" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="437.0" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="943.3" y1="460.0" x2="943.3" y2="481.9" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="460.8" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="947.3" y1="445.9" x2="947.3" y2="480.0" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="446.1" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="951.2" y1="436.9" x2="951.2" y2="456.1" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="441.8" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="955.2" y1="424.6" x2="955.2" y2="467.8" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="435.0" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="959.1" y1="464.1" x2="959.1" y2="485.0" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="481.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="963.1" y1="468.5" x2="963.1" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="473.6" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="967.0" y1="482.2" x2="967.0" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="482.2" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="971.0" y1="528.9" x2="971.0" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="531.2" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="974.9" y1="564.6" x2="974.9" y2="587.6" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="571.0" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="978.9" y1="552.7" x2="978.9" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="556.6" width="2.45" height="24.2" fill="var(--up)"/>
<line x1="982.8" y1="554.6" x2="982.8" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="557.6" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="986.8" y1="577.3" x2="986.8" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="581.4" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="990.7" y1="575.4" x2="990.7" y2="597.5" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="579.2" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="994.7" y1="542.8" x2="994.7" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="556.8" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="998.6" y1="529.8" x2="998.6" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="549.5" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="1002.6" y1="559.5" x2="1002.6" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="563.9" width="2.45" height="24.0" fill="var(--down)"/>
<line x1="1006.5" y1="573.0" x2="1006.5" y2="595.1" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="583.2" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="1010.5" y1="555.5" x2="1010.5" y2="584.2" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="557.3" width="2.45" height="22.1" fill="var(--up)"/>
<line x1="1014.5" y1="542.4" x2="1014.5" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="546.2" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="1018.4" y1="525.6" x2="1018.4" y2="546.6" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="526.5" width="2.45" height="18.3" fill="var(--up)"/>
<line x1="1022.4" y1="510.0" x2="1022.4" y2="533.0" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="514.7" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="1026.3" y1="514.2" x2="1026.3" y2="542.0" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="522.2" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="1030.3" y1="500.9" x2="1030.3" y2="523.0" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="501.8" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="1034.2" y1="490.9" x2="1034.2" y2="511.4" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="501.8" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="1038.2" y1="509.3" x2="1038.2" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="510.0" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="1042.1" y1="497.0" x2="1042.1" y2="513.7" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="506.4" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="1046.1" y1="500.0" x2="1046.1" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="509.3" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="1050.0" y1="485.6" x2="1050.0" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="490.6" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="60" y1="433.9" x2="1052" y2="433.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="437.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$449 R1</text>
<text x="1058" y="449.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="373.3" x2="1052" y2="373.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="376.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$479 R2</text>
<text x="1058" y="388.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="332.9" x2="1052" y2="332.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="336.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$499 R3</text>
<text x="1058" y="348.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="517.8" x2="1052" y2="517.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="511.8" font-size="11.5" fill="var(--support)" font-weight="600">$408 S1</text>
<text x="1058" y="523.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="572.8" x2="1052" y2="572.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="566.8" font-size="11.5" fill="var(--support)" font-weight="600">$381 S2</text>
<text x="1058" y="578.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="603.6" x2="1052" y2="603.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="597.6" font-size="11.5" fill="var(--support)" font-weight="600">$366 S3 (52주 최저)</text>
<text x="1058" y="609.6" font-size="9.5" fill="var(--muted)">터치 1회</text>
<circle cx="1052.0" cy="490.6" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $499 | 2 | 2025-10·2026-04 스윙 고점대 |
| R2 | $479 | 3 | 2025-10·2025-12·2026-06 반복 저항 |
| R1 | $449 | 4 | 2026-02~2026-07 구간에서 가장 자주 되돌림 |
| **현재가** | **$421.50** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $408 | 4 | 현재가에 가장 근접한 지지, 2026-02~2026-03 반복 저점 |
| S2 | $381 | 4 | 2025-11·2026-03~04 저점대 |
| S3 | $366 | 1 | 52주 최저(2026-07-17), 이후 반등 기점 |
| 참고선 | $626 | — | 52주 최고(2025-09-08) — 아래 §3 갭다운 이전 레짐, 현재 가격대와 단절되어 있어 근시일 저항으로 보지 않음 |

> 표시 기준은 "현재가에서 가까운 순으로 각 방향 3개"다(§4 생성 스크립트 기본값). R3 위로도 터치 2회 클러스터가 $518(2025-09·2026-05), $537(2026-01·2026-05) 두 개 더 있으나 현재가에서 20% 이상 떨어져 있어 표시하지 않았다 — 필요하면 `--levels`로 늘려 재생성할 수 있다. S3($366)는 터치 1회로 기준에 못 미치지만 52주 최저이자 반등 기점이라 예외로 포함했다.

---

## 3. 관측된 특이 구간 — 2025-09-10 갭다운

- 2025-09-09 장 마감 후 FY2025 3분기 실적 발표([최근 뉴스 / 이슈](./08_news.md) 로그 참고) 이후 다음 거래일(2025-09-10) 시가부터 갭다운.
- 종가 기준 전일 대비 **-35.8%** ($604.37 → $387.78), 거래량은 평소(일 1~2백만 주 내외) 대비 약 10배인 **2,116만 주**로 급증.
- 이 사건 이후 가격대가 구조적으로 재설정되어(약 $600대 → $370~540대), 갭다운 이전 스윙 레벨(예: $626 52주 최고)은 현재 거래 레짐과 직접 연결되지 않는 참고선으로만 표시했다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-15. 원주가(과거 분할은 소급 반영, 배당은 미반영) — 조사 기간 중 Synopsys의 주식분할 이력은 확인되지 않음.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 각주).
- **생성**: `scripts/gen_technical_chart.py SNPS --name Synopsys --event 2025-09-10:"실적발표 갭다운 (시가 -29%, 종가 -35.8%)" --ref-line 626.24:"52주 최고" --force-level '366:(52주 최저)'`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - 2025-09-10 갭다운처럼 뉴스 이벤트로 인한 불연속 구간은 통상적인 지지/저항 해석이 적용되기 어렵다(§3).

---

## 관련 문서

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Yahoo Finance — SNPS Chart API](https://query1.finance.yahoo.com/v8/finance/chart/SNPS) (일봉 OHLCV 원자료, 2026-08-15 수집)
- [stockanalysis.com — SNPS Price History](https://stockanalysis.com/stocks/snps/history/)

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-22)*
