# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 단기 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 일봉 문서와 같은 원자료를 주 단위로 집계한 것이라 마지막 종가는 동일하다.
- **대조 결과**: 2026-09-11 종가 **$293.11**은 핵심 지표·밸류에이션 / 적정주가에 인용된 기준 종가와 일치한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-11)

<style>
.apd-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .apd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.apd-chart svg { width:100%; height:auto; display:block; }
.apd-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.apd-chart .title { fill: var(--ink); font-weight:600; }
.apd-chart .grid { stroke: var(--grid); stroke-width:1; }
.apd-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="apd-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Air Products(APD) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Air Products (APD) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $293.11 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="575.1" x2="1052" y2="575.1" class="grid"/>
<text x="52" y="579.1" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
<line x1="60" y1="493.7" x2="1052" y2="493.7" class="grid"/>
<text x="52" y="497.7" font-size="11" text-anchor="end" fill="var(--muted)">240</text>
<line x1="60" y1="412.2" x2="1052" y2="412.2" class="grid"/>
<text x="52" y="416.2" font-size="11" text-anchor="end" fill="var(--muted)">260</text>
<line x1="60" y1="330.8" x2="1052" y2="330.8" class="grid"/>
<text x="52" y="334.8" font-size="11" text-anchor="end" fill="var(--muted)">280</text>
<line x1="60" y1="249.4" x2="1052" y2="249.4" class="grid"/>
<text x="52" y="253.4" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="168.0" x2="1052" y2="168.0" class="grid"/>
<text x="52" y="172.0" font-size="11" text-anchor="end" fill="var(--muted)">320</text>
<line x1="60" y1="86.5" x2="1052" y2="86.5" class="grid"/>
<text x="52" y="90.5" font-size="11" text-anchor="end" fill="var(--muted)">340</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.5" y1="56.0" x2="122.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.5" y1="626.0" x2="122.5" y2="631.0" class="axis"/>
<text x="122.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="319.4" y1="56.0" x2="319.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="319.4" y1="626.0" x2="319.4" y2="631.0" class="axis"/>
<text x="319.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="516.2" y1="56.0" x2="516.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="516.2" y1="626.0" x2="516.2" y2="631.0" class="axis"/>
<text x="516.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.9" y1="56.0" x2="716.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.9" y1="626.0" x2="716.9" y2="631.0" class="axis"/>
<text x="716.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.8" y1="56.0" x2="913.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.8" y1="626.0" x2="913.8" y2="631.0" class="axis"/>
<text x="913.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="363.3" x2="61.9" y2="413.8" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="370.1" width="2.35" height="34.7" fill="var(--down)"/>
<line x1="65.7" y1="405.3" x2="65.7" y2="437.0" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="414.0" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="69.5" y1="375.6" x2="69.5" y2="437.0" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="375.6" width="2.35" height="47.1" fill="var(--down)"/>
<line x1="73.3" y1="385.7" x2="73.3" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="390.1" width="2.35" height="34.6" fill="var(--up)"/>
<line x1="77.0" y1="270.4" x2="77.0" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="279.1" width="2.35" height="101.7" fill="var(--up)"/>
<line x1="80.8" y1="264.8" x2="80.8" y2="288.7" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="282.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="84.6" y1="243.4" x2="84.6" y2="284.6" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="250.2" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="88.4" y1="209.8" x2="88.4" y2="281.9" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="211.5" width="2.35" height="39.5" fill="var(--up)"/>
<line x1="92.2" y1="182.7" x2="92.2" y2="218.9" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="208.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="96.0" y1="214.3" x2="96.0" y2="271.9" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="214.8" width="2.35" height="43.8" fill="var(--down)"/>
<line x1="99.8" y1="239.5" x2="99.8" y2="287.3" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="251.6" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="103.5" y1="266.8" x2="103.5" y2="311.3" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="269.7" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="107.3" y1="258.5" x2="107.3" y2="288.7" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="268.3" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="111.1" y1="219.1" x2="111.1" y2="273.5" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="256.2" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="114.9" y1="247.1" x2="114.9" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="251.5" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="118.7" y1="223.0" x2="118.7" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="232.0" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="122.5" y1="211.6" x2="122.5" y2="273.2" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="231.0" width="2.35" height="28.9" fill="var(--down)"/>
<line x1="126.3" y1="248.7" x2="126.3" y2="293.4" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="268.5" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="130.0" y1="287.0" x2="130.0" y2="322.8" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="294.5" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="133.8" y1="314.5" x2="133.8" y2="363.1" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="334.3" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="137.6" y1="304.3" x2="137.6" y2="409.5" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="344.3" width="2.35" height="55.4" fill="var(--down)"/>
<line x1="141.4" y1="408.3" x2="141.4" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="421.7" width="2.35" height="54.1" fill="var(--down)"/>
<line x1="145.2" y1="457.4" x2="145.2" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="473.1" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="149.0" y1="485.8" x2="149.0" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="485.8" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="152.8" y1="497.7" x2="152.8" y2="554.2" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="504.6" width="2.35" height="36.2" fill="var(--down)"/>
<line x1="156.5" y1="530.9" x2="156.5" y2="590.4" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="537.3" width="2.35" height="40.3" fill="var(--down)"/>
<line x1="160.3" y1="524.4" x2="160.3" y2="589.7" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="527.6" width="2.35" height="46.8" fill="var(--up)"/>
<line x1="164.1" y1="463.5" x2="164.1" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="467.0" width="2.35" height="38.9" fill="var(--up)"/>
<line x1="167.9" y1="438.6" x2="167.9" y2="470.7" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="457.1" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="171.7" y1="435.5" x2="171.7" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="448.1" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="175.5" y1="440.2" x2="175.5" y2="468.5" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="448.1" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="179.3" y1="435.1" x2="179.3" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="470.6" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="183.1" y1="476.0" x2="183.1" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="484.6" width="2.35" height="33.2" fill="var(--down)"/>
<line x1="186.8" y1="436.7" x2="186.8" y2="533.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="510.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="190.6" y1="506.6" x2="190.6" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="519.3" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="194.4" y1="493.9" x2="194.4" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="503.5" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="198.2" y1="450.3" x2="198.2" y2="520.3" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="450.3" width="2.35" height="42.5" fill="var(--up)"/>
<line x1="202.0" y1="435.4" x2="202.0" y2="488.1" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="443.7" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="205.8" y1="403.8" x2="205.8" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="432.6" width="2.35" height="27.7" fill="var(--down)"/>
<line x1="209.6" y1="473.9" x2="209.6" y2="532.3" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="476.7" width="2.35" height="33.4" fill="var(--down)"/>
<line x1="213.3" y1="442.4" x2="213.3" y2="513.1" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="444.5" width="2.35" height="55.7" fill="var(--up)"/>
<line x1="217.1" y1="442.0" x2="217.1" y2="518.8" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="447.2" width="2.35" height="35.3" fill="var(--down)"/>
<line x1="220.9" y1="492.6" x2="220.9" y2="528.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="501.8" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="224.7" y1="512.6" x2="224.7" y2="579.7" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="529.0" width="2.35" height="25.0" fill="var(--down)"/>
<line x1="228.5" y1="509.9" x2="228.5" y2="563.7" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="515.8" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="232.3" y1="454.2" x2="232.3" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="460.2" width="2.35" height="52.3" fill="var(--up)"/>
<line x1="236.1" y1="400.3" x2="236.1" y2="492.0" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="401.5" width="2.35" height="63.7" fill="var(--up)"/>
<line x1="239.8" y1="364.6" x2="239.8" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="368.0" width="2.35" height="28.0" fill="var(--up)"/>
<line x1="243.6" y1="351.6" x2="243.6" y2="402.5" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="368.0" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="247.4" y1="379.8" x2="247.4" y2="415.2" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="403.2" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="251.2" y1="400.0" x2="251.2" y2="469.9" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="412.3" width="2.35" height="54.8" fill="var(--down)"/>
<line x1="255.0" y1="423.0" x2="255.0" y2="474.6" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="424.6" width="2.35" height="36.3" fill="var(--up)"/>
<line x1="258.8" y1="395.9" x2="258.8" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="416.3" width="2.35" height="47.4" fill="var(--down)"/>
<line x1="262.6" y1="454.4" x2="262.6" y2="520.5" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="474.1" width="2.35" height="31.5" fill="var(--down)"/>
<line x1="266.4" y1="508.0" x2="266.4" y2="541.1" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="512.9" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="270.1" y1="457.8" x2="270.1" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="514.4" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="273.9" y1="490.3" x2="273.9" y2="555.8" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="521.4" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="277.7" y1="472.4" x2="277.7" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="488.4" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="281.5" y1="430.9" x2="281.5" y2="486.0" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="434.9" width="2.35" height="45.0" fill="var(--up)"/>
<line x1="285.3" y1="345.2" x2="285.3" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="346.9" width="2.35" height="96.0" fill="var(--up)"/>
<line x1="289.1" y1="280.1" x2="289.1" y2="347.8" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="296.4" width="2.35" height="43.3" fill="var(--up)"/>
<line x1="292.9" y1="257.9" x2="292.9" y2="298.2" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="263.7" width="2.35" height="34.5" fill="var(--up)"/>
<line x1="296.6" y1="204.1" x2="296.6" y2="273.1" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="209.0" width="2.35" height="62.5" fill="var(--up)"/>
<line x1="300.4" y1="165.4" x2="300.4" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="174.3" width="2.35" height="43.6" fill="var(--up)"/>
<line x1="304.2" y1="164.1" x2="304.2" y2="209.2" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="185.3" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="308.0" y1="133.1" x2="308.0" y2="201.6" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="182.5" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="311.8" y1="179.6" x2="311.8" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="189.5" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="315.6" y1="191.6" x2="315.6" y2="230.3" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="195.4" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="319.4" y1="201.5" x2="319.4" y2="248.1" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="207.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="323.1" y1="181.8" x2="323.1" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="203.0" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="326.9" y1="200.5" x2="326.9" y2="256.8" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="200.5" width="2.35" height="30.9" fill="var(--down)"/>
<line x1="330.7" y1="180.6" x2="330.7" y2="238.3" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="191.8" width="2.35" height="41.9" fill="var(--up)"/>
<line x1="334.5" y1="164.3" x2="334.5" y2="317.6" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="194.2" width="2.35" height="116.2" fill="var(--down)"/>
<line x1="338.3" y1="285.9" x2="338.3" y2="330.1" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="299.0" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="342.1" y1="292.8" x2="342.1" y2="341.0" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="295.3" width="2.35" height="36.7" fill="var(--down)"/>
<line x1="345.9" y1="321.5" x2="345.9" y2="355.6" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="326.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="349.6" y1="270.2" x2="349.6" y2="320.9" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="270.6" width="2.35" height="50.2" fill="var(--up)"/>
<line x1="353.4" y1="267.3" x2="353.4" y2="330.8" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="279.1" width="2.35" height="46.6" fill="var(--down)"/>
<line x1="357.2" y1="290.1" x2="357.2" y2="355.9" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="322.7" width="2.35" height="29.5" fill="var(--down)"/>
<line x1="361.0" y1="317.8" x2="361.0" y2="396.4" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="345.2" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="364.8" y1="300.1" x2="364.8" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="301.5" width="2.35" height="65.8" fill="var(--up)"/>
<line x1="368.6" y1="292.9" x2="368.6" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="304.1" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="372.4" y1="289.6" x2="372.4" y2="332.9" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="305.5" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="376.2" y1="275.8" x2="376.2" y2="314.7" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="287.8" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="379.9" y1="269.0" x2="379.9" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="272.4" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="383.7" y1="257.9" x2="383.7" y2="294.5" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="262.8" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="387.5" y1="249.9" x2="387.5" y2="353.7" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="257.6" width="2.35" height="81.4" fill="var(--down)"/>
<line x1="391.3" y1="329.3" x2="391.3" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="335.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="395.1" y1="325.4" x2="395.1" y2="375.6" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="333.1" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="398.9" y1="323.3" x2="398.9" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="326.6" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="402.7" y1="314.9" x2="402.7" y2="353.3" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="317.2" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="406.4" y1="271.4" x2="406.4" y2="343.8" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="277.2" width="2.35" height="55.7" fill="var(--up)"/>
<line x1="410.2" y1="288.4" x2="410.2" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="290.3" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="414.0" y1="247.3" x2="414.0" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="251.3" width="2.35" height="50.5" fill="var(--up)"/>
<line x1="417.8" y1="252.6" x2="417.8" y2="323.6" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="256.9" width="2.35" height="46.0" fill="var(--down)"/>
<line x1="421.6" y1="249.8" x2="421.6" y2="303.9" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="255.0" width="2.35" height="48.0" fill="var(--up)"/>
<line x1="425.4" y1="236.3" x2="425.4" y2="266.0" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="238.2" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="429.2" y1="222.6" x2="429.2" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="235.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="432.9" y1="225.7" x2="432.9" y2="325.5" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="237.2" width="2.35" height="75.6" fill="var(--down)"/>
<line x1="436.7" y1="294.3" x2="436.7" y2="327.7" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="295.0" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="440.5" y1="283.0" x2="440.5" y2="324.8" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="299.0" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="444.3" y1="292.6" x2="444.3" y2="319.5" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="297.0" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="448.1" y1="246.9" x2="448.1" y2="295.6" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="257.5" width="2.35" height="36.8" fill="var(--up)"/>
<line x1="451.9" y1="250.0" x2="451.9" y2="287.5" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="255.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="455.7" y1="218.0" x2="455.7" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="240.8" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="459.5" y1="241.7" x2="459.5" y2="307.0" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="242.8" width="2.35" height="61.0" fill="var(--down)"/>
<line x1="463.2" y1="288.2" x2="463.2" y2="320.2" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="309.0" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="467.0" y1="305.0" x2="467.0" y2="348.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="325.4" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="470.8" y1="279.8" x2="470.8" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="308.6" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="474.6" y1="279.7" x2="474.6" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="299.8" width="2.35" height="36.9" fill="var(--down)"/>
<line x1="478.4" y1="331.8" x2="478.4" y2="354.2" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="343.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="482.2" y1="265.8" x2="482.2" y2="343.0" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="277.1" width="2.35" height="61.9" fill="var(--up)"/>
<line x1="486.0" y1="273.2" x2="486.0" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="277.1" width="2.35" height="112.9" fill="var(--down)"/>
<line x1="489.7" y1="353.4" x2="489.7" y2="403.3" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="371.6" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="493.5" y1="341.1" x2="493.5" y2="375.0" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="353.2" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="497.3" y1="350.7" x2="497.3" y2="388.9" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="356.5" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="501.1" y1="361.1" x2="501.1" y2="411.1" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="367.7" width="2.35" height="31.2" fill="var(--down)"/>
<line x1="504.9" y1="357.7" x2="504.9" y2="402.2" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="368.0" width="2.35" height="31.0" fill="var(--up)"/>
<line x1="508.7" y1="351.4" x2="508.7" y2="379.6" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="357.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="512.5" y1="347.8" x2="512.5" y2="363.4" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="356.1" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="516.2" y1="351.7" x2="516.2" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="362.0" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="520.0" y1="359.6" x2="520.0" y2="400.0" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="377.4" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="523.8" y1="396.0" x2="523.8" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="401.9" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="527.6" y1="387.1" x2="527.6" y2="424.0" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="404.5" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="531.4" y1="403.0" x2="531.4" y2="430.9" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="404.5" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="535.2" y1="542.4" x2="535.2" y2="606.7" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="546.6" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="539.0" y1="540.7" x2="539.0" y2="590.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="547.2" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="542.7" y1="521.0" x2="542.7" y2="553.7" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="523.0" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="546.5" y1="503.2" x2="546.5" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="510.0" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="550.3" y1="461.1" x2="550.3" y2="512.4" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="487.1" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="554.1" y1="455.7" x2="554.1" y2="483.8" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="474.8" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="557.9" y1="457.6" x2="557.9" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="475.1" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="561.7" y1="479.6" x2="561.7" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="484.4" width="2.35" height="25.7" fill="var(--up)"/>
<line x1="565.5" y1="474.7" x2="565.5" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="481.7" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="569.3" y1="490.3" x2="569.3" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="495.6" width="2.35" height="32.5" fill="var(--down)"/>
<line x1="573.0" y1="511.1" x2="573.0" y2="544.4" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="521.6" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="576.8" y1="500.2" x2="576.8" y2="537.7" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="509.6" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="580.6" y1="463.6" x2="580.6" y2="539.2" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="469.8" width="2.35" height="36.1" fill="var(--up)"/>
<line x1="584.4" y1="441.1" x2="584.4" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="450.7" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="588.2" y1="400.1" x2="588.2" y2="459.6" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="401.3" width="2.35" height="45.3" fill="var(--up)"/>
<line x1="592.0" y1="382.7" x2="592.0" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="393.5" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="595.8" y1="384.0" x2="595.8" y2="419.1" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="385.0" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="599.5" y1="325.9" x2="599.5" y2="389.0" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="332.7" width="2.35" height="54.0" fill="var(--up)"/>
<line x1="603.3" y1="303.9" x2="603.3" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="327.0" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="607.1" y1="346.2" x2="607.1" y2="378.3" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="357.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="610.9" y1="355.5" x2="610.9" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="355.5" width="2.35" height="64.7" fill="var(--down)"/>
<line x1="614.7" y1="420.8" x2="614.7" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="426.4" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="618.5" y1="397.1" x2="618.5" y2="437.5" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="406.9" width="2.35" height="29.5" fill="var(--up)"/>
<line x1="622.3" y1="360.3" x2="622.3" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="400.4" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="626.0" y1="398.1" x2="626.0" y2="461.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="400.6" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="629.8" y1="265.7" x2="629.8" y2="408.2" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="323.7" width="2.35" height="82.3" fill="var(--up)"/>
<line x1="633.6" y1="317.3" x2="633.6" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="338.0" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="637.4" y1="339.0" x2="637.4" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="340.4" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="641.2" y1="341.5" x2="641.2" y2="363.9" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="347.7" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="645.0" y1="331.6" x2="645.0" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="335.5" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="648.8" y1="334.9" x2="648.8" y2="382.3" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="344.9" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="652.5" y1="304.4" x2="652.5" y2="377.8" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="314.0" width="2.35" height="60.8" fill="var(--up)"/>
<line x1="656.3" y1="282.0" x2="656.3" y2="307.5" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="298.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="660.1" y1="241.1" x2="660.1" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="247.9" width="2.35" height="45.7" fill="var(--up)"/>
<line x1="663.9" y1="242.9" x2="663.9" y2="314.7" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="249.4" width="2.35" height="59.0" fill="var(--down)"/>
<line x1="667.7" y1="152.2" x2="667.7" y2="244.1" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="181.6" width="2.35" height="43.4" fill="var(--up)"/>
<line x1="671.5" y1="118.4" x2="671.5" y2="184.2" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="118.7" width="2.35" height="62.0" fill="var(--up)"/>
<line x1="675.3" y1="117.4" x2="675.3" y2="176.6" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="125.5" width="2.35" height="50.5" fill="var(--down)"/>
<line x1="679.1" y1="168.1" x2="679.1" y2="220.4" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="168.1" width="2.35" height="43.8" fill="var(--down)"/>
<line x1="682.8" y1="173.5" x2="682.8" y2="242.0" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="196.5" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="686.6" y1="174.5" x2="686.6" y2="213.3" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="179.8" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="690.4" y1="116.3" x2="690.4" y2="169.6" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="119.8" width="2.35" height="45.8" fill="var(--up)"/>
<line x1="694.2" y1="101.1" x2="694.2" y2="125.7" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="109.6" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="698.0" y1="98.8" x2="698.0" y2="198.1" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="103.2" width="2.35" height="64.3" fill="var(--down)"/>
<line x1="701.8" y1="158.0" x2="701.8" y2="219.3" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="158.0" width="2.35" height="41.3" fill="var(--down)"/>
<line x1="705.6" y1="200.4" x2="705.6" y2="279.9" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="203.3" width="2.35" height="66.5" fill="var(--down)"/>
<line x1="709.3" y1="264.9" x2="709.3" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="276.2" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="713.1" y1="282.0" x2="713.1" y2="320.6" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="282.0" width="2.35" height="32.9" fill="var(--down)"/>
<line x1="716.9" y1="268.9" x2="716.9" y2="322.8" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="277.6" width="2.35" height="35.7" fill="var(--up)"/>
<line x1="720.7" y1="175.7" x2="720.7" y2="278.2" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="176.9" width="2.35" height="97.9" fill="var(--up)"/>
<line x1="724.5" y1="127.5" x2="724.5" y2="191.2" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="130.3" width="2.35" height="42.1" fill="var(--up)"/>
<line x1="728.3" y1="94.7" x2="728.3" y2="166.2" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="105.8" width="2.35" height="39.0" fill="var(--up)"/>
<line x1="732.1" y1="81.9" x2="732.1" y2="218.8" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="123.7" width="2.35" height="83.2" fill="var(--down)"/>
<line x1="735.8" y1="174.4" x2="735.8" y2="233.4" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="183.8" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="739.6" y1="177.3" x2="739.6" y2="223.0" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="184.2" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="743.4" y1="175.1" x2="743.4" y2="226.2" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="183.6" width="2.35" height="29.6" fill="var(--up)"/>
<line x1="747.2" y1="162.0" x2="747.2" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="171.8" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="751.0" y1="182.7" x2="751.0" y2="289.7" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="196.7" width="2.35" height="85.6" fill="var(--down)"/>
<line x1="754.8" y1="261.5" x2="754.8" y2="300.9" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="283.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="758.6" y1="259.9" x2="758.6" y2="285.8" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="274.6" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="762.4" y1="264.1" x2="762.4" y2="401.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="287.3" width="2.35" height="110.8" fill="var(--down)"/>
<line x1="766.1" y1="366.6" x2="766.1" y2="478.7" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="375.6" width="2.35" height="40.6" fill="var(--up)"/>
<line x1="769.9" y1="353.2" x2="769.9" y2="416.3" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="363.1" width="2.35" height="37.3" fill="var(--down)"/>
<line x1="773.7" y1="356.9" x2="773.7" y2="436.5" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="383.3" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="777.5" y1="324.2" x2="777.5" y2="436.6" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="340.5" width="2.35" height="40.6" fill="var(--up)"/>
<line x1="781.3" y1="343.7" x2="781.3" y2="400.1" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="354.6" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="785.1" y1="323.7" x2="785.1" y2="379.1" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="335.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="788.9" y1="336.4" x2="788.9" y2="389.6" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="346.3" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="792.6" y1="333.1" x2="792.6" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="335.3" width="2.35" height="29.7" fill="var(--up)"/>
<line x1="796.4" y1="310.9" x2="796.4" y2="348.9" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="331.7" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="800.2" y1="310.3" x2="800.2" y2="340.1" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="329.3" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="804.0" y1="314.5" x2="804.0" y2="369.6" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="318.3" width="2.35" height="51.2" fill="var(--down)"/>
<line x1="807.8" y1="311.5" x2="807.8" y2="385.6" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="321.3" width="2.35" height="50.3" fill="var(--up)"/>
<line x1="811.6" y1="279.2" x2="811.6" y2="345.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="282.6" width="2.35" height="43.6" fill="var(--up)"/>
<line x1="815.4" y1="260.1" x2="815.4" y2="300.1" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="282.1" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="819.1" y1="265.4" x2="819.1" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="268.5" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="822.9" y1="247.3" x2="822.9" y2="275.4" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="252.5" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="826.7" y1="258.1" x2="826.7" y2="337.3" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="258.2" width="2.35" height="65.5" fill="var(--down)"/>
<line x1="830.5" y1="276.8" x2="830.5" y2="321.5" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="295.2" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="834.3" y1="272.8" x2="834.3" y2="327.7" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="288.2" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="838.1" y1="244.9" x2="838.1" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="252.2" width="2.35" height="45.6" fill="var(--up)"/>
<line x1="841.9" y1="249.4" x2="841.9" y2="278.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="254.2" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="845.6" y1="276.0" x2="845.6" y2="305.5" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="281.4" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="849.4" y1="256.3" x2="849.4" y2="315.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="278.6" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="853.2" y1="262.9" x2="853.2" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="273.6" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="857.0" y1="286.2" x2="857.0" y2="391.5" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="298.6" width="2.35" height="86.0" fill="var(--down)"/>
<line x1="860.8" y1="351.9" x2="860.8" y2="388.2" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="365.6" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="864.6" y1="356.8" x2="864.6" y2="424.6" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="366.0" width="2.35" height="58.1" fill="var(--down)"/>
<line x1="868.4" y1="387.4" x2="868.4" y2="448.2" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="414.6" width="2.35" height="25.4" fill="var(--down)"/>
<line x1="872.2" y1="424.9" x2="872.2" y2="445.9" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="433.0" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="875.9" y1="422.6" x2="875.9" y2="497.6" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="429.6" width="2.35" height="53.6" fill="var(--down)"/>
<line x1="879.7" y1="394.7" x2="879.7" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="413.3" width="2.35" height="72.6" fill="var(--up)"/>
<line x1="883.5" y1="388.7" x2="883.5" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="410.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="887.3" y1="417.8" x2="887.3" y2="456.2" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="419.3" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="891.1" y1="402.9" x2="891.1" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="408.0" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="894.9" y1="389.8" x2="894.9" y2="427.6" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="409.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="898.7" y1="425.6" x2="898.7" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="432.5" width="2.35" height="48.9" fill="var(--down)"/>
<line x1="902.4" y1="456.3" x2="902.4" y2="499.4" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="489.9" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="906.2" y1="461.4" x2="906.2" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="463.5" width="2.35" height="30.4" fill="var(--up)"/>
<line x1="910.0" y1="447.1" x2="910.0" y2="484.2" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="451.1" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="913.8" y1="389.0" x2="913.8" y2="463.3" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="397.1" width="2.35" height="64.8" fill="var(--up)"/>
<line x1="917.6" y1="368.0" x2="917.6" y2="405.0" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="381.6" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="921.4" y1="382.9" x2="921.4" y2="426.1" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="396.0" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="925.2" y1="355.7" x2="925.2" y2="436.9" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="361.4" width="2.35" height="38.7" fill="var(--up)"/>
<line x1="928.9" y1="299.0" x2="928.9" y2="380.0" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="318.1" width="2.35" height="53.4" fill="var(--up)"/>
<line x1="932.7" y1="263.8" x2="932.7" y2="354.9" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="322.4" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="936.5" y1="315.4" x2="936.5" y2="348.2" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="323.7" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="940.3" y1="311.2" x2="940.3" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="324.7" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="944.1" y1="338.4" x2="944.1" y2="379.2" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="355.7" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="947.9" y1="262.3" x2="947.9" y2="369.3" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="298.3" width="2.35" height="59.0" fill="var(--up)"/>
<line x1="951.7" y1="281.9" x2="951.7" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="289.3" width="2.35" height="37.4" fill="var(--down)"/>
<line x1="955.5" y1="268.7" x2="955.5" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="281.2" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="959.2" y1="263.8" x2="959.2" y2="312.9" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="273.4" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="963.0" y1="244.3" x2="963.0" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="254.6" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="966.8" y1="245.3" x2="966.8" y2="295.6" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="253.0" width="2.35" height="29.7" fill="var(--down)"/>
<line x1="970.6" y1="230.8" x2="970.6" y2="276.0" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="242.2" width="2.35" height="27.6" fill="var(--up)"/>
<line x1="974.4" y1="219.7" x2="974.4" y2="273.3" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="227.0" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="978.2" y1="227.4" x2="978.2" y2="283.9" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="249.3" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="982.0" y1="217.0" x2="982.0" y2="279.5" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="259.7" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="985.7" y1="262.9" x2="985.7" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="268.9" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="989.5" y1="286.4" x2="989.5" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="294.1" width="2.35" height="42.3" fill="var(--down)"/>
<line x1="993.3" y1="299.9" x2="993.3" y2="350.4" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="321.3" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="997.1" y1="302.0" x2="997.1" y2="353.7" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="323.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="1000.9" y1="311.1" x2="1000.9" y2="344.4" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="330.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1004.7" y1="311.0" x2="1004.7" y2="349.1" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="333.4" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="1008.5" y1="191.3" x2="1008.5" y2="371.1" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="191.6" width="2.35" height="149.7" fill="var(--up)"/>
<line x1="1012.2" y1="188.9" x2="1012.2" y2="278.1" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="191.2" width="2.35" height="60.1" fill="var(--down)"/>
<line x1="1016.0" y1="220.4" x2="1016.0" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="245.6" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="1019.8" y1="241.4" x2="1019.8" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="258.1" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="1023.6" y1="204.3" x2="1023.6" y2="284.5" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="263.6" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="1027.4" y1="234.5" x2="1027.4" y2="298.2" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="235.4" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="1031.2" y1="202.5" x2="1031.2" y2="243.9" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="212.9" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="1035.0" y1="204.6" x2="1035.0" y2="258.1" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="217.3" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="1038.7" y1="213.4" x2="1038.7" y2="241.5" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="216.5" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="1042.5" y1="192.7" x2="1042.5" y2="248.5" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="208.8" width="2.35" height="35.4" fill="var(--down)"/>
<line x1="1046.3" y1="237.9" x2="1046.3" y2="280.0" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="254.0" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="1050.1" y1="267.6" x2="1050.1" y2="281.7" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="273.5" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="60" y1="258.7" x2="1052" y2="258.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="262.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$298 R1</text>
<text x="1058" y="274.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="206.8" x2="1052" y2="206.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="210.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$310 R2</text>
<text x="1058" y="222.3" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="148.7" x2="1052" y2="148.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="152.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$325 R3</text>
<text x="1058" y="164.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="315.0" x2="1052" y2="315.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="309.0" font-size="11.5" fill="var(--support)" font-weight="600">$284 S1</text>
<text x="1058" y="321.0" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="383.6" x2="1052" y2="383.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="377.6" font-size="11.5" fill="var(--support)" font-weight="600">$267 S2</text>
<text x="1058" y="389.6" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="474.0" x2="1052" y2="474.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="468.0" font-size="11.5" fill="var(--support)" font-weight="600">$245 S3</text>
<text x="1058" y="480.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="277.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="269.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $293 (2026-09-11)</text>
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
| R3 | $325 | 2 | 2022-12-12·2023-01-30 — 3년 반 전 고점대. 청정수소 투자 서사가 정점이던 구간이라 현 레짐과 단절돼 있다 |
| R2 | $310 | 6 | 2021-11-08·2022-01-03·2023-07-24·2023-09-11·2026-05-11·2026-07-06 — 5년에 걸쳐 여섯 번 되밀린 가장 두꺼운 상단대 |
| R1 | $298 | 5 | 2023-03-06·05-08·10-30·2024-07-29·2025-08-18 — 최근 3년간 반복된 중단 대역. 현재가 바로 위 |
| **현재가** | **$293.11** (2026-09-11 종가) | — | R1과 S1 사이 |
| S1 | $284 | 4 | 2021-11-29·2023-08-07·2025-01-06·2026-08-03 — 현재가에 가장 근접한 지지 |
| S2 | $267 | 5 | 2023-03-20·05-29·2024-09-02·2025-06-23·2026-06-29 — 5년 내내 반복 확인된 두꺼운 하단대 |
| S3 | $245 | 2 | 2024-07-01·2025-04-07 — 최근 2년 저점권. 5년 최저($262.47)보다 낮은 것은 클러스터 중심이 종가가 아닌 스윙 저가 기준이기 때문이다 |

> **5년 구조가 말하는 것은 "박스권"이다.** 2021년 9월 이후 이 종목은 대체로 $267~$310 사이에서 움직였고, 그 위(R3 $325)와 아래(5년 최저 $262.47)를 벗어난 기간은 짧았다. 같은 5년간 매출은 $12.7B → $12.0B로 정체했고 GAAP 이익은 두 차례 일회성으로 튀었다 — **가격이 박스권이었던 것과 펀더멘털이 제자리였던 것이 같은 이야기**다.

---

## 3. 관측된 특이 구간 — 2026년 2분기 이후 레짐 변화

- 2026-06-30 청정에너지 프로젝트 철수 발표와 2026-07-30 가이던스 상향을 계기로, 3년 가까이 $267~$298 하단부에 머물던 가격이 $293~$314 구간으로 올라섰다(일봉 문서 3. 관측된 특이 구간 참고).
- 주봉 기준으로 보면 이 이동은 아직 **R2($310) 돌파로 확정되지 않았다** — 2026-05-11·07-06 두 차례 이 대역에서 되밀렸다. 즉 5년 박스의 상단을 시험 중인 상태이지 벗어난 상태가 아니다.
- 이 구간의 해석은 [투자 판단](./07_investment.md)의 논거와 같은 방향이다 — 이익 회복은 시작됐지만 확인은 덜 됐다는 것이 가격 구조에도 그대로 나타나 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py APD --name "Air Products" --interval 1wk --close-on 2026-09-11 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - R3($325)는 2022~2023년 초에만 형성된 레벨이라 현재 레짐과 3년 이상 떨어져 있다 — 근시일 저항으로 읽지 말고 "과거에 도달해본 상단" 정도로만 본다.
    - 기간 내 주식분할·유상증자는 없었다. 5년간 분기배당이 계속 있었으나 원주가(배당 미반영) 기준이라 누적 배당수익률(연 2.4% 안팎)만큼 실제 총수익과 차이가 난다.

---

*작성일: 2026-09-12*
