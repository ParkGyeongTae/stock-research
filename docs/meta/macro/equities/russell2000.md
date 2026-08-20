# 러셀2000

!!! note ""
    최근 5년 러셀2000 지수(미국 중소형주 2,000종목, `^RUT`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. S&P 500·나스닥종합지수·필라델피아 반도체지수가 전부 대형주 위주 지수인 것과 달리, 이 지수는 **미국 국내 경기에 더 민감한 중소형주**를 담아 다른 신호를 준다 — 대형주 지수는 오르는데 러셀2000이 약하면 시장 강세가 소수 대형주에 쏠려 있다는 신호로 읽히곤 한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="rut-chart">
<style>
.rut-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .rut-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .rut-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.rut-chart svg { width:100%; height:auto; display:block; }
.rut-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.rut-chart .title { fill: var(--ink); font-weight:600; }
.rut-chart .grid { stroke: var(--grid); stroke-width:1; }
.rut-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="러셀2000(^RUT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">러셀2000 (^RUT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-19 · 마지막 종가 3,032.94 (2026-08-19) · 단위 지수</text>
<line x1="60" y1="616.8" x2="1052" y2="616.8" class="grid"/>
<text x="52" y="620.8" font-size="11" text-anchor="end" fill="var(--muted)">1,600</text>
<line x1="60" y1="543.3" x2="1052" y2="543.3" class="grid"/>
<text x="52" y="547.3" font-size="11" text-anchor="end" fill="var(--muted)">1,800</text>
<line x1="60" y1="469.7" x2="1052" y2="469.7" class="grid"/>
<text x="52" y="473.7" font-size="11" text-anchor="end" fill="var(--muted)">2,000</text>
<line x1="60" y1="396.2" x2="1052" y2="396.2" class="grid"/>
<text x="52" y="400.2" font-size="11" text-anchor="end" fill="var(--muted)">2,200</text>
<line x1="60" y1="322.6" x2="1052" y2="322.6" class="grid"/>
<text x="52" y="326.6" font-size="11" text-anchor="end" fill="var(--muted)">2,400</text>
<line x1="60" y1="249.1" x2="1052" y2="249.1" class="grid"/>
<text x="52" y="253.1" font-size="11" text-anchor="end" fill="var(--muted)">2,600</text>
<line x1="60" y1="175.5" x2="1052" y2="175.5" class="grid"/>
<text x="52" y="179.5" font-size="11" text-anchor="end" fill="var(--muted)">2,800</text>
<line x1="60" y1="102.0" x2="1052" y2="102.0" class="grid"/>
<text x="52" y="106.0" font-size="11" text-anchor="end" fill="var(--muted)">3,000</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.3" y1="626.0" x2="137.3" y2="631.0" class="axis"/>
<text x="137.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="333.5" y1="626.0" x2="333.5" y2="631.0" class="axis"/>
<text x="333.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="529.6" y1="626.0" x2="529.6" y2="631.0" class="axis"/>
<text x="529.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="729.5" y1="626.0" x2="729.5" y2="631.0" class="axis"/>
<text x="729.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.6" y1="626.0" x2="925.6" y2="631.0" class="axis"/>
<text x="925.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="407.3" x2="61.9" y2="424.8" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="408.1" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="65.7" y1="366.1" x2="65.7" y2="407.5" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="367.8" width="2.34" height="39.7" fill="var(--up)"/>
<line x1="69.4" y1="355.7" x2="69.4" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="362.3" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="73.2" y1="359.2" x2="73.2" y2="386.0" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="362.3" width="2.34" height="23.8" fill="var(--down)"/>
<line x1="77.0" y1="377.8" x2="77.0" y2="394.6" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="382.6" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="80.7" y1="372.0" x2="80.7" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="378.5" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="84.5" y1="361.8" x2="84.5" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="378.5" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="88.3" y1="372.2" x2="88.3" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="381.1" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="92.1" y1="357.1" x2="92.1" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="372.0" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="95.8" y1="357.9" x2="95.8" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="362.6" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="99.6" y1="351.5" x2="99.6" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="360.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="103.4" y1="304.5" x2="103.4" y2="360.1" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="309.0" width="2.34" height="51.1" fill="var(--up)"/>
<line x1="107.1" y1="301.0" x2="107.1" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="308.5" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="110.9" y1="314.9" x2="110.9" y2="344.1" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="318.2" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="114.7" y1="333.8" x2="114.7" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="343.3" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="118.5" y1="366.3" x2="118.5" y2="417.1" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="378.2" width="2.34" height="32.9" fill="var(--down)"/>
<line x1="122.2" y1="367.9" x2="122.2" y2="412.8" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="391.8" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="126.0" y1="390.2" x2="126.0" y2="423.8" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="391.9" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="129.8" y1="378.6" x2="129.8" y2="430.1" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="380.9" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="133.6" y1="368.7" x2="133.6" y2="385.0" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="379.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="137.3" y1="363.7" x2="137.3" y2="403.8" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="379.0" width="2.34" height="24.6" fill="var(--down)"/>
<line x1="141.1" y1="392.4" x2="141.1" y2="423.3" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="403.9" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="144.9" y1="410.7" x2="144.9" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="410.7" width="2.34" height="63.4" fill="var(--down)"/>
<line x1="148.6" y1="451.9" x2="148.6" y2="506.0" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="474.7" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="152.4" y1="449.6" x2="152.4" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="468.8" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="156.2" y1="431.0" x2="156.2" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="458.6" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="160.0" y1="438.5" x2="160.0" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="458.6" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="163.7" y1="454.7" x2="163.7" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="454.7" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="167.5" y1="445.0" x2="167.5" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="454.9" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="171.3" y1="459.6" x2="171.3" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="469.3" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="175.0" y1="437.5" x2="175.0" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="438.0" width="2.34" height="39.1" fill="var(--up)"/>
<line x1="178.8" y1="433.8" x2="178.8" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="438.2" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="182.6" y1="418.8" x2="182.6" y2="451.5" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="436.2" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="186.4" y1="431.7" x2="186.4" y2="475.5" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="436.1" width="2.34" height="35.7" fill="var(--down)"/>
<line x1="190.1" y1="457.1" x2="190.1" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="467.9" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="193.9" y1="447.6" x2="193.9" y2="492.0" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="468.5" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="197.7" y1="486.5" x2="197.7" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="494.3" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="201.4" y1="487.1" x2="201.4" y2="535.5" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="519.8" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="205.2" y1="530.9" x2="205.2" y2="579.6" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="530.9" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="209.0" y1="528.4" x2="209.0" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="546.7" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="212.8" y1="510.9" x2="212.8" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="510.9" width="2.34" height="37.3" fill="var(--up)"/>
<line x1="216.5" y1="507.3" x2="216.5" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="512.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="220.3" y1="499.2" x2="220.3" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="508.9" width="2.34" height="34.3" fill="var(--down)"/>
<line x1="224.1" y1="554.1" x2="224.1" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="554.1" width="2.34" height="38.5" fill="var(--down)"/>
<line x1="227.8" y1="555.9" x2="227.8" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="555.9" width="2.34" height="31.1" fill="var(--up)"/>
<line x1="231.6" y1="546.0" x2="231.6" y2="587.2" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="553.2" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="235.4" y1="550.6" x2="235.4" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="554.5" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="239.2" y1="555.9" x2="239.2" y2="585.6" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="555.9" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="242.9" y1="527.7" x2="242.9" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="540.7" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="246.7" y1="510.8" x2="246.7" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="511.9" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="250.5" y1="498.2" x2="250.5" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="498.5" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="254.3" y1="463.6" x2="254.3" y2="504.7" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="463.6" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="258.0" y1="458.7" x2="258.0" y2="487.2" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="467.0" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="261.8" y1="482.5" x2="261.8" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="494.8" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="265.6" y1="507.0" x2="265.6" y2="543.6" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="513.6" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="269.3" y1="512.0" x2="269.3" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="512.8" width="2.34" height="25.6" fill="var(--up)"/>
<line x1="273.1" y1="504.2" x2="273.1" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="510.2" width="2.34" height="33.7" fill="var(--down)"/>
<line x1="276.9" y1="538.1" x2="276.9" y2="595.2" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="548.5" width="2.34" height="39.0" fill="var(--down)"/>
<line x1="280.7" y1="570.7" x2="280.7" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="589.5" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="284.4" y1="552.2" x2="284.4" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="579.2" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="288.2" y1="562.4" x2="288.2" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="577.8" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="292.0" y1="549.9" x2="292.0" y2="580.0" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="564.5" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="295.7" y1="525.5" x2="295.7" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="526.0" width="2.34" height="36.5" fill="var(--up)"/>
<line x1="299.5" y1="518.0" x2="299.5" y2="558.7" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="528.9" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="303.3" y1="506.5" x2="303.3" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="512.8" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="307.1" y1="504.3" x2="307.1" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="515.4" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="310.8" y1="516.2" x2="310.8" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="517.8" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="314.6" y1="507.1" x2="314.6" y2="535.4" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="509.1" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="318.4" y1="511.6" x2="318.4" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="511.6" width="2.34" height="32.9" fill="var(--down)"/>
<line x1="322.1" y1="513.6" x2="322.1" y2="563.0" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="543.7" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="325.9" y1="549.1" x2="325.9" y2="570.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="556.5" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="329.7" y1="555.1" x2="329.7" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="557.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="333.5" y1="544.9" x2="333.5" y2="566.3" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="545.9" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="337.2" y1="510.5" x2="337.2" y2="545.8" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="511.3" width="2.34" height="31.6" fill="var(--up)"/>
<line x1="341.0" y1="505.1" x2="341.0" y2="533.9" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="511.4" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="344.8" y1="499.6" x2="344.8" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="502.3" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="348.5" y1="467.0" x2="348.5" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="475.0" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="352.3" y1="478.5" x2="352.3" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="478.5" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="356.1" y1="483.5" x2="356.1" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="489.4" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="359.9" y1="492.9" x2="359.9" y2="515.4" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="492.9" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="363.6" y1="494.8" x2="363.6" y2="514.7" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="496.1" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="367.4" y1="495.9" x2="367.4" y2="559.1" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="496.2" width="2.34" height="57.1" fill="var(--down)"/>
<line x1="371.2" y1="542.5" x2="371.2" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="559.8" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="375.0" y1="547.5" x2="375.0" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="567.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="378.7" y1="542.3" x2="378.7" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="542.3" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="382.5" y1="538.7" x2="382.5" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="541.8" width="2.34" height="18.2" fill="var(--down)"/>
<line x1="386.3" y1="541.4" x2="386.3" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="550.2" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="390.0" y1="539.7" x2="390.0" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="546.4" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="393.8" y1="544.1" x2="393.8" y2="570.5" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="546.8" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="397.6" y1="548.7" x2="397.6" y2="578.3" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="556.0" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="401.4" y1="553.2" x2="401.4" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="555.6" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="405.1" y1="543.1" x2="405.1" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="552.9" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="408.9" y1="537.2" x2="408.9" y2="564.9" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="551.5" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="412.7" y1="531.6" x2="412.7" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="531.9" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="416.4" y1="508.9" x2="416.4" y2="544.3" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="519.1" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="420.2" y1="504.0" x2="420.2" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="515.5" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="424.0" y1="516.1" x2="424.0" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="517.0" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="427.8" y1="507.1" x2="427.8" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="510.6" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="431.5" y1="507.0" x2="431.5" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="511.3" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="435.3" y1="487.2" x2="435.3" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="495.1" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="439.1" y1="473.3" x2="439.1" y2="496.7" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="484.3" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="442.8" y1="471.6" x2="442.8" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="476.5" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="446.6" y1="468.4" x2="446.6" y2="488.6" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="475.3" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="450.4" y1="483.9" x2="450.4" y2="501.3" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="484.7" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="454.2" y1="498.8" x2="454.2" y2="531.9" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="499.1" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="457.9" y1="516.2" x2="457.9" y2="531.5" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="521.1" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="461.7" y1="496.6" x2="461.7" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="498.8" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="465.5" y1="500.5" x2="465.5" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="500.5" width="2.34" height="23.8" fill="var(--down)"/>
<line x1="469.2" y1="518.2" x2="469.2" y2="529.4" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="520.0" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="473.0" y1="525.7" x2="473.0" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="525.7" width="2.34" height="26.2" fill="var(--down)"/>
<line x1="476.8" y1="539.7" x2="476.8" y2="557.4" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="548.7" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="480.6" y1="549.9" x2="480.6" y2="576.5" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="550.3" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="484.3" y1="548.2" x2="484.3" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="565.9" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="488.1" y1="550.7" x2="488.1" y2="587.4" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="567.5" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="491.9" y1="583.6" x2="491.9" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="590.4" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="495.7" y1="554.1" x2="495.7" y2="603.8" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="557.7" width="2.34" height="42.0" fill="var(--up)"/>
<line x1="499.4" y1="557.7" x2="499.4" y2="585.8" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="557.9" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="503.2" y1="532.2" x2="503.2" y2="583.4" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="544.1" width="2.34" height="36.4" fill="var(--up)"/>
<line x1="507.0" y1="539.5" x2="507.0" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="540.5" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="510.7" y1="519.8" x2="510.7" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="520.2" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="514.5" y1="510.6" x2="514.5" y2="525.3" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="513.5" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="518.3" y1="466.4" x2="518.3" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="475.2" width="2.34" height="38.8" fill="var(--up)"/>
<line x1="522.1" y1="454.1" x2="522.1" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="457.2" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="525.8" y1="443.3" x2="525.8" y2="459.8" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="453.8" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="529.6" y1="457.8" x2="529.6" y2="491.1" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="465.0" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="533.4" y1="473.8" x2="533.4" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="487.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="537.1" y1="490.2" x2="537.1" y2="507.1" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="490.2" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="540.9" y1="469.3" x2="540.9" y2="484.2" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="477.7" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="544.7" y1="465.4" x2="544.7" y2="493.2" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="477.7" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="548.5" y1="465.7" x2="548.5" y2="498.6" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="466.0" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="552.2" y1="446.6" x2="552.2" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="453.1" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="556.0" y1="460.0" x2="556.0" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="463.6" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="559.8" y1="441.0" x2="559.8" y2="465.3" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="441.6" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="563.5" y1="427.1" x2="563.5" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="437.5" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="567.3" y1="440.2" x2="567.3" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="441.9" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="571.1" y1="430.6" x2="571.1" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="443.2" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="574.9" y1="419.9" x2="574.9" y2="444.0" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="423.9" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="578.6" y1="423.4" x2="578.6" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="423.4" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="582.4" y1="438.8" x2="582.4" y2="471.6" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="442.2" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="586.2" y1="463.6" x2="586.2" y2="494.9" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="465.7" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="589.9" y1="465.9" x2="589.9" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="469.0" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="593.7" y1="449.5" x2="593.7" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="456.6" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="597.5" y1="439.5" x2="597.5" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="447.7" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="601.3" y1="428.4" x2="601.3" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="434.5" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="605.0" y1="429.4" x2="605.0" y2="454.7" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="434.2" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="608.8" y1="438.0" x2="608.8" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="441.9" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="612.6" y1="437.3" x2="612.6" y2="461.2" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="439.4" width="2.34" height="20.5" fill="var(--down)"/>
<line x1="616.3" y1="437.2" x2="616.3" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="465.2" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="620.1" y1="457.4" x2="620.1" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="461.6" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="623.9" y1="448.6" x2="623.9" y2="465.9" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="452.2" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="627.7" y1="450.1" x2="627.7" y2="462.7" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="451.1" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="631.4" y1="409.5" x2="631.4" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="415.2" width="2.34" height="40.4" fill="var(--up)"/>
<line x1="635.2" y1="367.4" x2="635.2" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="401.9" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="639.0" y1="371.2" x2="639.0" y2="404.8" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="374.1" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="642.8" y1="359.4" x2="642.8" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="372.0" width="2.34" height="57.5" fill="var(--down)"/>
<line x1="646.5" y1="434.8" x2="646.5" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="440.0" width="2.34" height="21.7" fill="var(--up)"/>
<line x1="650.3" y1="414.6" x2="650.3" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="417.5" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="654.1" y1="387.8" x2="654.1" y2="418.9" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="389.3" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="657.8" y1="382.3" x2="657.8" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="385.1" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="661.6" y1="393.8" x2="661.6" y2="437.4" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="393.8" width="2.34" height="42.3" fill="var(--down)"/>
<line x1="665.4" y1="402.2" x2="665.4" y2="448.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="402.6" width="2.34" height="32.9" fill="var(--up)"/>
<line x1="669.2" y1="374.4" x2="669.2" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="385.9" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="672.9" y1="380.1" x2="672.9" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="384.8" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="676.7" y1="383.6" x2="676.7" y2="406.0" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="390.1" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="680.5" y1="383.3" x2="680.5" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="383.5" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="684.2" y1="363.3" x2="684.2" y2="385.8" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="368.2" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="688.0" y1="368.4" x2="688.0" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="368.5" width="2.34" height="24.8" fill="var(--down)"/>
<line x1="691.8" y1="373.9" x2="691.8" y2="397.4" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="389.7" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="695.6" y1="321.7" x2="695.6" y2="396.1" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="322.7" width="2.34" height="71.0" fill="var(--up)"/>
<line x1="699.3" y1="307.3" x2="699.3" y2="360.3" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="318.3" width="2.34" height="39.7" fill="var(--down)"/>
<line x1="703.1" y1="319.2" x2="703.1" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="320.2" width="2.34" height="36.8" fill="var(--up)"/>
<line x1="706.9" y1="298.2" x2="706.9" y2="316.8" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="309.8" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="710.6" y1="306.9" x2="710.6" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="308.9" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="714.4" y1="312.3" x2="714.4" y2="346.0" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="315.7" width="2.34" height="26.5" fill="var(--down)"/>
<line x1="718.2" y1="333.5" x2="718.2" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="342.9" width="2.34" height="37.7" fill="var(--down)"/>
<line x1="722.0" y1="366.1" x2="722.0" y2="389.0" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="379.8" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="725.7" y1="370.8" x2="725.7" y2="395.2" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="371.0" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="729.5" y1="362.2" x2="729.5" y2="405.0" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="368.3" width="2.34" height="31.8" fill="var(--down)"/>
<line x1="733.3" y1="363.1" x2="733.3" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="368.3" width="2.34" height="36.5" fill="var(--up)"/>
<line x1="737.0" y1="351.2" x2="737.0" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="356.5" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="740.8" y1="351.2" x2="740.8" y2="370.7" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="363.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="744.6" y1="349.5" x2="744.6" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="366.8" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="748.4" y1="360.2" x2="748.4" y2="381.3" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="363.3" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="752.1" y1="361.4" x2="752.1" y2="398.3" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="366.2" width="2.34" height="31.7" fill="var(--down)"/>
<line x1="755.9" y1="395.4" x2="755.9" y2="423.3" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="395.9" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="759.7" y1="405.9" x2="759.7" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="407.9" width="2.34" height="34.0" fill="var(--down)"/>
<line x1="763.5" y1="448.3" x2="763.5" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="448.3" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="767.2" y1="435.9" x2="767.2" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="448.8" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="771.0" y1="429.1" x2="771.0" y2="464.9" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="442.0" width="2.34" height="19.2" fill="var(--down)"/>
<line x1="774.8" y1="452.0" x2="774.8" y2="549.5" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="470.5" width="2.34" height="62.9" fill="var(--down)"/>
<line x1="778.5" y1="495.2" x2="778.5" y2="567.9" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="521.1" width="2.34" height="31.3" fill="var(--up)"/>
<line x1="782.3" y1="505.6" x2="782.3" y2="527.8" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="509.9" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="786.1" y1="481.5" x2="786.1" y2="534.7" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="485.3" width="2.34" height="34.9" fill="var(--up)"/>
<line x1="789.9" y1="460.0" x2="789.9" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="462.1" width="2.34" height="22.2" fill="var(--up)"/>
<line x1="793.6" y1="454.8" x2="793.6" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="461.2" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="797.4" y1="427.4" x2="797.4" y2="444.2" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="428.1" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="801.2" y1="428.8" x2="801.2" y2="465.6" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="439.5" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="804.9" y1="435.7" x2="804.9" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="445.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="808.7" y1="421.0" x2="808.7" y2="453.7" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="421.1" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="812.5" y1="407.0" x2="812.5" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="416.7" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="816.3" y1="420.2" x2="816.3" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="427.4" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="820.0" y1="400.1" x2="820.0" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="406.3" width="2.34" height="24.6" fill="var(--up)"/>
<line x1="823.8" y1="378.1" x2="823.8" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="378.1" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="827.6" y1="368.3" x2="827.6" y2="394.6" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="382.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="831.3" y1="370.6" x2="831.3" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="381.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="835.1" y1="365.6" x2="835.1" y2="387.2" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="373.7" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="838.9" y1="369.2" x2="838.9" y2="417.0" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="371.3" width="2.34" height="37.1" fill="var(--down)"/>
<line x1="842.7" y1="380.3" x2="842.7" y2="404.6" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="389.4" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="846.4" y1="348.6" x2="846.4" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="364.3" width="2.34" height="23.8" fill="var(--up)"/>
<line x1="850.2" y1="334.9" x2="850.2" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="336.6" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="854.0" y1="328.5" x2="854.0" y2="345.0" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="335.0" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="857.7" y1="319.9" x2="857.7" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="325.9" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="861.5" y1="314.4" x2="861.5" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="323.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="865.3" y1="296.0" x2="865.3" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="304.7" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="869.1" y1="289.9" x2="869.1" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="305.7" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="872.8" y1="286.8" x2="872.8" y2="317.7" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="294.6" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="876.6" y1="285.1" x2="876.6" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="289.8" width="2.34" height="34.8" fill="var(--down)"/>
<line x1="880.4" y1="270.5" x2="880.4" y2="316.1" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="303.4" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="884.2" y1="276.0" x2="884.2" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="280.9" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="887.9" y1="271.2" x2="887.9" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="275.8" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="891.7" y1="292.8" x2="891.7" y2="329.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="292.8" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="895.5" y1="293.9" x2="895.5" y2="342.8" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="303.6" width="2.34" height="23.4" fill="var(--down)"/>
<line x1="899.2" y1="321.1" x2="899.2" y2="358.1" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="329.3" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="903.0" y1="284.8" x2="903.0" y2="332.8" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="285.7" width="2.34" height="46.9" fill="var(--up)"/>
<line x1="906.8" y1="271.1" x2="906.8" y2="298.7" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="277.9" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="910.6" y1="250.5" x2="910.6" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="266.9" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="914.3" y1="261.0" x2="914.3" y2="290.3" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="262.9" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="918.1" y1="259.0" x2="918.1" y2="275.8" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="271.6" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="921.9" y1="273.5" x2="921.9" y2="292.9" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="276.7" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="925.6" y1="235.9" x2="925.6" y2="279.7" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="240.2" width="2.34" height="39.5" fill="var(--up)"/>
<line x1="929.4" y1="215.1" x2="929.4" y2="246.5" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="220.5" width="2.34" height="23.4" fill="var(--up)"/>
<line x1="933.2" y1="199.4" x2="933.2" y2="237.2" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="223.6" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="937.0" y1="217.5" x2="937.0" y2="249.2" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="222.5" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="940.7" y1="221.0" x2="940.7" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="223.2" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="944.5" y1="210.0" x2="944.5" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="224.3" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="948.3" y1="217.2" x2="948.3" y2="244.9" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="225.6" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="952.0" y1="219.8" x2="952.0" y2="248.7" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="228.9" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="955.8" y1="227.5" x2="955.8" y2="279.1" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="245.8" width="2.34" height="30.7" fill="var(--down)"/>
<line x1="959.6" y1="252.3" x2="959.6" y2="299.3" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="284.7" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="963.4" y1="273.1" x2="963.4" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="286.0" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="967.1" y1="268.2" x2="967.1" y2="306.6" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="298.6" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="970.9" y1="270.9" x2="970.9" y2="320.8" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="274.8" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="974.7" y1="232.0" x2="974.7" y2="280.1" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="237.8" width="2.34" height="37.8" fill="var(--up)"/>
<line x1="978.4" y1="178.0" x2="978.4" y2="240.9" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="184.0" width="2.34" height="55.6" fill="var(--up)"/>
<line x1="982.2" y1="168.9" x2="982.2" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="180.3" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="986.0" y1="169.7" x2="986.0" y2="203.0" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="170.8" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="989.8" y1="142.9" x2="989.8" y2="182.0" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="153.0" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="993.5" y1="143.1" x2="993.5" y2="178.6" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="151.9" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="997.3" y1="146.6" x2="997.3" y2="203.9" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="150.1" width="2.34" height="27.9" fill="var(--up)"/>
<line x1="1001.1" y1="123.1" x2="1001.1" y2="141.6" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="131.6" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="1004.9" y1="122.6" x2="1004.9" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="139.1" width="2.34" height="24.1" fill="var(--down)"/>
<line x1="1008.6" y1="113.2" x2="1008.6" y2="177.2" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="122.6" width="2.34" height="29.9" fill="var(--up)"/>
<line x1="1012.4" y1="103.3" x2="1012.4" y2="134.7" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="108.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1016.2" y1="89.6" x2="1016.2" y2="119.9" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="98.3" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="1019.9" y1="84.8" x2="1019.9" y2="113.0" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="101.6" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="1023.7" y1="93.0" x2="1023.7" y2="128.8" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="103.1" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="1027.5" y1="103.3" x2="1027.5" y2="126.2" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="111.3" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="1031.3" y1="106.2" x2="1031.3" y2="129.8" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="113.7" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="1035.0" y1="112.1" x2="1035.0" y2="137.8" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="122.3" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="1038.8" y1="84.0" x2="1038.8" y2="125.8" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="89.3" width="2.34" height="36.5" fill="var(--up)"/>
<line x1="1042.6" y1="76.3" x2="1042.6" y2="97.1" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="76.8" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="1046.3" y1="79.3" x2="1046.3" y2="95.5" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="79.8" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="1050.1" y1="83.5" x2="1050.1" y2="90.9" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="88.7" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="60" y1="413.6" x2="1052" y2="413.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="407.6" font-size="11.5" fill="var(--support)" font-weight="600">2,152 S1</text>
<text x="1058" y="419.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="472.2" x2="1052" y2="472.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="466.2" font-size="11.5" fill="var(--support)" font-weight="600">1,993 S2</text>
<text x="1058" y="478.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="503.5" x2="1052" y2="503.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="497.5" font-size="11.5" fill="var(--support)" font-weight="600">1,908 S3</text>
<text x="1058" y="509.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="89.9" r="3" fill="var(--ink)"/>
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

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **상승**: 미국 국내 경기 확장 기대, 위험선호 확대 신호로 흔히 해석된다 — 특히 금리 인하 기대 국면에서 대형주보다 민감하게 반응하는 경향이 있다.
- **하락**: 국내 경기 둔화 우려, 조달금리 부담(중소형주는 대형주보다 차입 의존도가 높은 경우가 많다) 신호로 흔히 해석된다.
- **왜 경기에 더 민감한가**: 중소형주는 대체로 내수 비중이 크고 해외 매출 비중이 낮으며, 대형주보다 회사채 시장 접근성이 제한적이라 변동금리 은행 대출 의존도가 높은 편이다 — 금리·신용 여건 변화가 이익과 조달비용에 더 빠르게 반영된다.
- 절대 수준보다 S&P 500·나스닥종합지수 대비 상대 강도가 더 자주 인용된다 — 대형주 지수는 오르는데 이 지수가 약하면 시장 강세가 소수 대형주에 쏠려 있다는 신호로 읽히곤 한다.

---

## 관련 문서

- [S&P 500](./sp500.md) · [나스닥종합지수](./nasdaq.md) — 대형주 위주 비교군
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Russell 2000 (^RUT)](https://finance.yahoo.com/quote/%5ERUT/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
