# 코스닥 — 기술적 참고 (주봉 5년)

> 최근 5년 코스닥 지수(한국거래소 코스닥시장, 중소형·성장주 중심, `^KQ11`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. [`kospi.md`](./kospi.md)가 대형주 위주라면, 이 지수는 [`russell2000.md`](./russell2000.md)처럼 중소형·성장주 성격이 강해 국내 경기·위험선호에 더 민감하게 반응하는 편이다.

---

## 1. 차트 — 최근 5년 주봉

<div class="kq11-chart">
<style>
.kq11-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .kq11-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .kq11-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.kq11-chart svg { width:100%; height:auto; display:block; }
.kq11-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.kq11-chart .title { fill: var(--ink); font-weight:600; }
.kq11-chart .grid { stroke: var(--grid); stroke-width:1; }
.kq11-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코스닥(^KQ11) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코스닥 (^KQ11) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 840.89 (2026-08-20) · 단위 지수</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="538.3" x2="1052" y2="538.3" class="grid"/>
<text x="52" y="542.3" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="450.6" x2="1052" y2="450.6" class="grid"/>
<text x="52" y="454.6" font-size="11" text-anchor="end" fill="var(--muted)">800</text>
<line x1="60" y1="362.9" x2="1052" y2="362.9" class="grid"/>
<text x="52" y="366.9" font-size="11" text-anchor="end" fill="var(--muted)">900</text>
<line x1="60" y1="275.2" x2="1052" y2="275.2" class="grid"/>
<text x="52" y="279.2" font-size="11" text-anchor="end" fill="var(--muted)">1,000</text>
<line x1="60" y1="187.5" x2="1052" y2="187.5" class="grid"/>
<text x="52" y="191.5" font-size="11" text-anchor="end" fill="var(--muted)">1,100</text>
<line x1="60" y1="99.8" x2="1052" y2="99.8" class="grid"/>
<text x="52" y="103.8" font-size="11" text-anchor="end" fill="var(--muted)">1,200</text>
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
<line x1="61.9" y1="274.6" x2="61.9" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="277.8" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="65.7" y1="251.3" x2="65.7" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="254.6" width="2.34" height="40.0" fill="var(--up)"/>
<line x1="69.4" y1="227.4" x2="69.4" y2="252.1" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="228.0" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="73.2" y1="225.9" x2="73.2" y2="251.6" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="225.9" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="77.0" y1="232.8" x2="77.0" y2="254.2" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="234.8" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="80.7" y1="235.6" x2="80.7" y2="244.7" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="239.8" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="84.5" y1="240.5" x2="84.5" y2="290.8" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="242.6" width="2.34" height="47.4" fill="var(--down)"/>
<line x1="88.3" y1="297.8" x2="88.3" y2="343.3" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="297.8" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="92.1" y1="282.1" x2="92.1" y2="330.5" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="283.5" width="2.34" height="34.6" fill="var(--up)"/>
<line x1="95.8" y1="265.1" x2="95.8" y2="288.3" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="279.6" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="99.6" y1="263.7" x2="99.6" y2="287.0" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="279.8" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="103.4" y1="261.4" x2="103.4" y2="280.2" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="274.0" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="107.1" y1="265.8" x2="107.1" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="267.3" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="110.9" y1="238.0" x2="110.9" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="238.5" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="114.7" y1="235.5" x2="114.7" y2="275.8" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="237.0" width="2.34" height="33.0" fill="var(--down)"/>
<line x1="118.5" y1="271.0" x2="118.5" y2="319.2" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="276.6" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="122.2" y1="255.2" x2="122.2" y2="292.0" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="265.1" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="126.0" y1="260.9" x2="126.0" y2="278.8" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="262.7" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="129.8" y1="265.6" x2="129.8" y2="290.6" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="268.7" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="133.6" y1="244.7" x2="133.6" y2="269.2" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="245.4" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="137.3" y1="239.0" x2="137.3" y2="292.9" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="241.1" width="2.34" height="38.4" fill="var(--down)"/>
<line x1="141.1" y1="280.0" x2="141.1" y2="307.8" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="281.8" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="144.9" y1="300.0" x2="144.9" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="300.0" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="148.6" y1="332.1" x2="148.6" y2="419.4" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="332.1" width="2.34" height="54.6" fill="var(--down)"/>
<line x1="152.4" y1="360.4" x2="152.4" y2="374.4" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="360.4" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="156.2" y1="349.8" x2="156.2" y2="382.8" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="357.7" width="2.34" height="25.0" fill="var(--down)"/>
<line x1="160.0" y1="371.0" x2="160.0" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="379.0" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="163.7" y1="376.7" x2="163.7" y2="408.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="386.6" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="167.5" y1="352.1" x2="167.5" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="362.1" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="171.3" y1="367.3" x2="171.3" y2="393.9" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="370.2" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="175.0" y1="342.8" x2="175.0" y2="392.3" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="342.8" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="178.8" y1="329.9" x2="178.8" y2="350.4" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="332.5" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="182.6" y1="323.5" x2="182.6" y2="339.6" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="327.3" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="186.4" y1="316.4" x2="186.4" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="327.4" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="190.1" y1="332.6" x2="190.1" y2="358.4" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="334.4" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="193.9" y1="332.9" x2="193.9" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="342.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="197.7" y1="351.3" x2="197.7" y2="372.6" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="354.6" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="201.4" y1="351.8" x2="201.4" y2="377.6" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="368.2" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="205.2" y1="379.8" x2="205.2" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="380.2" width="2.34" height="23.9" fill="var(--down)"/>
<line x1="209.0" y1="380.3" x2="209.0" y2="407.1" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="380.6" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="212.8" y1="376.0" x2="212.8" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="377.1" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="216.5" y1="363.8" x2="216.5" y2="379.2" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="370.4" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="220.3" y1="372.5" x2="220.3" y2="392.8" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="372.5" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="224.1" y1="404.4" x2="224.1" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="404.4" width="2.34" height="47.4" fill="var(--down)"/>
<line x1="227.8" y1="446.3" x2="227.8" y2="525.7" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="446.7" width="2.34" height="47.5" fill="var(--down)"/>
<line x1="231.6" y1="472.7" x2="231.6" y2="517.1" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="487.4" width="2.34" height="25.0" fill="var(--down)"/>
<line x1="235.4" y1="476.1" x2="235.4" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="480.0" width="2.34" height="29.1" fill="var(--up)"/>
<line x1="239.2" y1="473.1" x2="239.2" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="478.8" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="242.9" y1="450.0" x2="242.9" y2="479.7" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="459.6" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="246.7" y1="443.8" x2="246.7" y2="464.8" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="447.4" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="250.5" y1="422.3" x2="250.5" y2="451.2" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="422.9" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="254.3" y1="420.0" x2="254.3" y2="432.8" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="422.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="258.0" y1="418.6" x2="258.0" y2="438.2" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="419.7" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="261.8" y1="439.2" x2="261.8" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="444.6" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="265.6" y1="444.3" x2="265.6" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="463.0" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="269.3" y1="462.4" x2="269.3" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="463.9" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="273.1" y1="453.4" x2="273.1" y2="478.1" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="458.6" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="276.9" y1="474.8" x2="276.9" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="475.6" width="2.34" height="37.0" fill="var(--down)"/>
<line x1="280.7" y1="521.1" x2="280.7" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="521.1" width="2.34" height="41.2" fill="var(--down)"/>
<line x1="284.4" y1="531.7" x2="284.4" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="539.6" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="288.2" y1="551.2" x2="288.2" y2="581.8" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="551.2" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="292.0" y1="533.2" x2="292.0" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="560.7" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="295.7" y1="541.9" x2="295.7" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="549.2" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="299.5" y1="538.2" x2="299.5" y2="552.6" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="543.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="303.3" y1="510.1" x2="303.3" y2="542.6" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="510.9" width="2.34" height="30.7" fill="var(--up)"/>
<line x1="307.1" y1="497.4" x2="307.1" y2="513.0" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="510.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="310.8" y1="504.4" x2="310.8" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="508.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="314.6" y1="499.2" x2="314.6" y2="526.7" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="509.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="318.4" y1="503.4" x2="318.4" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="506.3" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="322.1" y1="511.6" x2="322.1" y2="529.4" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="523.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="325.9" y1="518.6" x2="325.9" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="523.6" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="329.7" y1="534.6" x2="329.7" y2="559.5" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="545.4" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="333.5" y1="546.1" x2="333.5" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="548.0" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="337.2" y1="525.4" x2="337.2" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="527.9" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="341.0" y1="521.7" x2="341.0" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="522.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="344.8" y1="501.4" x2="344.8" y2="516.2" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="502.1" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="348.5" y1="478.7" x2="348.5" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="479.7" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="352.3" y1="464.1" x2="352.3" y2="485.1" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="474.8" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="356.1" y1="464.0" x2="356.1" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="472.0" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="359.9" y1="456.4" x2="359.9" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="469.1" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="363.6" y1="448.5" x2="363.6" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="448.5" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="367.4" y1="434.3" x2="367.4" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="441.3" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="371.2" y1="451.8" x2="371.2" y2="487.4" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="452.9" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="375.0" y1="429.4" x2="375.0" y2="458.1" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="429.5" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="378.7" y1="404.5" x2="378.7" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="408.9" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="382.5" y1="380.4" x2="382.5" y2="408.8" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="380.4" width="2.34" height="25.6" fill="var(--up)"/>
<line x1="386.3" y1="357.1" x2="386.3" y2="384.5" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="359.6" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="390.0" y1="350.7" x2="390.0" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="358.2" width="2.34" height="32.0" fill="var(--down)"/>
<line x1="393.8" y1="389.2" x2="393.8" y2="430.3" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="391.5" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="397.6" y1="401.8" x2="397.6" y2="416.3" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="411.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="401.4" y1="403.0" x2="401.4" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="405.4" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="405.1" y1="413.6" x2="405.1" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="414.0" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="408.9" y1="396.9" x2="408.9" y2="417.7" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="412.7" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="412.7" y1="390.8" x2="412.7" y2="411.6" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="390.9" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="416.4" y1="374.7" x2="416.4" y2="393.5" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="377.2" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="420.2" y1="363.1" x2="420.2" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="373.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="424.0" y1="370.8" x2="424.0" y2="389.4" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="373.0" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="427.8" y1="379.4" x2="427.8" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="385.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="431.5" y1="366.8" x2="431.5" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="385.8" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="435.3" y1="363.2" x2="435.3" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="366.2" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="439.1" y1="330.2" x2="439.1" y2="370.7" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="332.6" width="2.34" height="34.9" fill="var(--up)"/>
<line x1="442.8" y1="313.5" x2="442.8" y2="382.3" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="332.2" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="446.6" y1="317.2" x2="446.6" y2="364.8" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="342.7" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="450.4" y1="347.0" x2="450.4" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="351.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="454.2" y1="355.8" x2="454.2" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="356.4" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="457.9" y1="360.5" x2="457.9" y2="380.6" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="363.5" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="461.7" y1="336.2" x2="461.7" y2="361.3" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="345.6" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="465.5" y1="339.0" x2="465.5" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="347.0" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="469.2" y1="346.3" x2="469.2" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="346.8" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="473.0" y1="366.1" x2="473.0" y2="408.9" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="369.8" width="2.34" height="30.5" fill="var(--down)"/>
<line x1="476.8" y1="398.8" x2="476.8" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="400.8" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="480.6" y1="422.3" x2="480.6" y2="450.3" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="422.3" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="484.3" y1="419.2" x2="484.3" y2="456.8" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="430.6" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="488.1" y1="428.4" x2="488.1" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="439.6" width="2.34" height="38.0" fill="var(--down)"/>
<line x1="491.9" y1="461.1" x2="491.9" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="479.9" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="495.7" y1="465.9" x2="495.7" y2="508.3" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="466.4" width="2.34" height="30.5" fill="var(--up)"/>
<line x1="499.4" y1="409.1" x2="499.4" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="455.4" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="503.2" y1="436.7" x2="503.2" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="451.4" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="507.0" y1="433.2" x2="507.0" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="437.5" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="510.7" y1="422.8" x2="510.7" y2="442.5" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="426.7" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="514.5" y1="417.3" x2="514.5" y2="441.4" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="424.0" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="518.3" y1="409.7" x2="518.3" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="417.0" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="522.1" y1="391.6" x2="522.1" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="402.7" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="525.8" y1="392.2" x2="525.8" y2="410.0" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="392.2" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="529.6" y1="381.4" x2="529.6" y2="397.6" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="381.9" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="533.4" y1="371.6" x2="533.4" y2="392.9" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="380.3" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="537.1" y1="389.5" x2="537.1" y2="424.3" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="393.2" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="540.9" y1="407.4" x2="540.9" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="407.8" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="544.7" y1="414.5" x2="544.7" y2="462.6" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="414.5" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="548.5" y1="426.0" x2="548.5" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="427.3" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="552.2" y1="394.3" x2="552.2" y2="423.7" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="400.1" width="2.34" height="23.2" fill="var(--up)"/>
<line x1="556.0" y1="384.3" x2="556.0" y2="403.7" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="390.5" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="559.8" y1="387.0" x2="559.8" y2="406.1" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="390.0" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="563.5" y1="384.6" x2="563.5" y2="398.3" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="386.4" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="567.3" y1="367.8" x2="567.3" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="380.1" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="571.1" y1="357.4" x2="571.1" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="359.4" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="574.9" y1="343.1" x2="574.9" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="357.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="578.6" y1="345.3" x2="578.6" y2="391.5" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="354.5" width="2.34" height="32.7" fill="var(--down)"/>
<line x1="582.4" y1="385.9" x2="582.4" y2="408.9" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="385.9" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="586.2" y1="401.5" x2="586.2" y2="428.7" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="406.6" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="589.9" y1="393.5" x2="589.9" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="400.8" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="593.7" y1="384.3" x2="593.7" y2="397.5" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="393.1" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="597.5" y1="383.1" x2="597.5" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="385.1" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="601.3" y1="385.0" x2="601.3" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="392.2" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="605.0" y1="400.2" x2="605.0" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="401.3" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="608.8" y1="404.6" x2="608.8" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="412.2" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="612.6" y1="392.3" x2="612.6" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="392.6" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="616.3" y1="380.9" x2="616.3" y2="398.3" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="396.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="620.1" y1="392.6" x2="620.1" y2="408.1" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="397.9" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="623.9" y1="404.6" x2="623.9" y2="418.9" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="404.8" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="627.7" y1="407.4" x2="627.7" y2="425.6" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="409.0" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="631.4" y1="394.4" x2="631.4" y2="411.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="406.4" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="635.2" y1="404.2" x2="635.2" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="404.5" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="639.0" y1="426.0" x2="639.0" y2="455.7" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="426.1" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="642.8" y1="437.2" x2="642.8" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="450.1" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="646.5" y1="478.5" x2="646.5" y2="562.4" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="480.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="650.3" y1="460.4" x2="650.3" y2="488.2" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="462.6" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="654.1" y1="460.4" x2="654.1" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="461.7" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="657.8" y1="470.0" x2="657.8" y2="491.0" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="470.8" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="661.6" y1="474.2" x2="661.6" y2="533.3" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="477.1" width="2.34" height="55.5" fill="var(--down)"/>
<line x1="665.4" y1="508.2" x2="665.4" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="509.2" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="669.2" y1="493.8" x2="669.2" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="495.9" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="672.9" y1="467.4" x2="672.9" y2="496.4" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="473.0" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="676.7" y1="470.6" x2="676.7" y2="490.6" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="470.7" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="680.5" y1="464.6" x2="680.5" y2="477.2" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="472.7" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="684.2" y1="470.8" x2="684.2" y2="494.9" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="476.2" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="688.0" y1="484.3" x2="688.0" y2="516.1" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="490.6" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="691.8" y1="497.8" x2="691.8" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="512.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="695.6" y1="484.8" x2="695.6" y2="514.5" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="500.3" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="699.3" y1="498.5" x2="699.3" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="499.0" width="2.34" height="52.1" fill="var(--down)"/>
<line x1="703.1" y1="540.5" x2="703.1" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="552.8" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="706.9" y1="538.6" x2="706.9" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="552.9" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="710.6" y1="544.6" x2="710.6" y2="587.1" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="552.2" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="714.4" y1="542.0" x2="714.4" y2="602.3" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="543.8" width="2.34" height="38.9" fill="var(--up)"/>
<line x1="718.2" y1="536.8" x2="718.2" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="538.5" width="2.34" height="27.6" fill="var(--down)"/>
<line x1="722.0" y1="550.7" x2="722.0" y2="572.3" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="560.9" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="725.7" y1="532.6" x2="725.7" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="533.3" width="2.34" height="37.8" fill="var(--up)"/>
<line x1="729.5" y1="517.5" x2="729.5" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="522.6" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="733.3" y1="515.7" x2="733.3" y2="531.6" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="516.7" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="737.0" y1="508.6" x2="737.0" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="513.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="740.8" y1="513.4" x2="740.8" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="513.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="744.6" y1="499.1" x2="744.6" y2="537.8" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="500.7" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="748.4" y1="486.8" x2="748.4" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="488.9" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="752.1" y1="466.8" x2="752.1" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="472.8" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="755.9" y1="471.2" x2="755.9" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="479.6" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="759.7" y1="494.1" x2="759.7" y2="515.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="503.5" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="763.5" y1="505.6" x2="763.5" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="508.3" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="767.2" y1="496.2" x2="767.2" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="503.1" width="2.34" height="18.2" fill="var(--down)"/>
<line x1="771.0" y1="515.6" x2="771.0" y2="545.5" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="519.6" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="774.8" y1="540.3" x2="774.8" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="549.4" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="778.5" y1="542.2" x2="778.5" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="542.2" width="2.34" height="25.1" fill="var(--up)"/>
<line x1="782.3" y1="522.7" x2="782.3" y2="539.6" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="522.7" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="786.1" y1="509.5" x2="786.1" y2="528.6" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="512.3" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="789.9" y1="509.9" x2="789.9" y2="526.0" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="511.5" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="793.6" y1="511.1" x2="793.6" y2="525.3" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="518.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="797.4" y1="504.1" x2="797.4" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="516.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="801.2" y1="514.9" x2="801.2" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="519.7" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="804.9" y1="505.5" x2="804.9" y2="523.5" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="508.2" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="808.7" y1="484.7" x2="808.7" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="489.0" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="812.5" y1="456.6" x2="812.5" y2="488.1" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="477.9" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="816.3" y1="458.0" x2="816.3" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="458.0" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="820.0" y1="447.2" x2="820.0" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="466.8" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="823.8" y1="456.1" x2="823.8" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="465.1" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="827.6" y1="445.4" x2="827.6" y2="475.6" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="450.2" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="831.3" y1="430.6" x2="831.3" y2="454.5" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="432.5" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="835.1" y1="426.2" x2="835.1" y2="448.6" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="433.2" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="838.9" y1="440.5" x2="838.9" y2="474.6" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="440.7" width="2.34" height="33.7" fill="var(--down)"/>
<line x1="842.7" y1="439.7" x2="842.7" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="442.5" width="2.34" height="31.1" fill="var(--up)"/>
<line x1="846.4" y1="432.8" x2="846.4" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="437.2" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="850.2" y1="439.7" x2="850.2" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="440.5" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="854.0" y1="445.4" x2="854.0" y2="457.9" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="453.3" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="857.7" y1="440.3" x2="857.7" y2="465.9" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="440.6" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="861.5" y1="409.1" x2="861.5" y2="438.8" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="409.3" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="865.3" y1="395.3" x2="865.3" y2="412.5" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="395.3" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="869.1" y1="382.6" x2="869.1" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="390.1" width="2.34" height="29.7" fill="var(--down)"/>
<line x1="872.8" y1="402.5" x2="872.8" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="403.0" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="876.6" y1="398.0" x2="876.6" y2="407.1" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="398.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="880.4" y1="388.3" x2="880.4" y2="416.2" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="398.4" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="884.2" y1="376.9" x2="884.2" y2="396.2" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="377.8" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="887.9" y1="357.0" x2="887.9" y2="377.2" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="362.6" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="891.7" y1="334.7" x2="891.7" y2="393.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="357.5" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="895.5" y1="345.3" x2="895.5" y2="387.4" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="364.8" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="899.2" y1="358.2" x2="899.2" y2="403.1" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="359.3" width="2.34" height="35.3" fill="var(--down)"/>
<line x1="903.0" y1="351.8" x2="903.0" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="351.8" width="2.34" height="34.5" fill="var(--up)"/>
<line x1="906.8" y1="329.7" x2="906.8" y2="350.1" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="341.2" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="910.6" y1="325.0" x2="910.6" y2="343.5" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="330.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="914.3" y1="328.4" x2="914.3" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="340.5" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="918.1" y1="334.4" x2="918.1" y2="351.3" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="341.9" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="921.9" y1="323.0" x2="921.9" y2="344.9" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="323.0" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="925.6" y1="310.0" x2="925.6" y2="331.8" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="320.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="929.4" y1="312.6" x2="929.4" y2="329.8" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="315.1" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="933.2" y1="276.7" x2="933.2" y2="333.7" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="280.6" width="2.34" height="36.0" fill="var(--up)"/>
<line x1="937.0" y1="116.6" x2="937.0" y2="271.9" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="144.2" width="2.34" height="127.6" fill="var(--up)"/>
<line x1="940.7" y1="136.0" x2="940.7" y2="232.9" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="162.5" width="2.34" height="41.9" fill="var(--down)"/>
<line x1="944.5" y1="151.0" x2="944.5" y2="187.9" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="178.8" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="948.3" y1="131.7" x2="948.3" y2="177.6" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="140.2" width="2.34" height="27.9" fill="var(--up)"/>
<line x1="952.0" y1="98.2" x2="952.0" y2="149.5" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="106.2" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="955.8" y1="86.1" x2="955.8" y2="295.8" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="126.3" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="959.6" y1="128.6" x2="959.6" y2="216.3" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="141.1" width="2.34" height="49.5" fill="var(--up)"/>
<line x1="963.4" y1="129.7" x2="963.4" y2="165.6" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="133.6" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="967.1" y1="126.6" x2="967.1" y2="192.2" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="151.1" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="970.9" y1="159.1" x2="970.9" y2="240.1" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="186.0" width="2.34" height="33.3" fill="var(--down)"/>
<line x1="974.7" y1="188.9" x2="974.7" y2="251.6" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="193.1" width="2.34" height="22.2" fill="var(--up)"/>
<line x1="978.4" y1="125.6" x2="978.4" y2="209.6" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="126.1" width="2.34" height="81.7" fill="var(--up)"/>
<line x1="982.2" y1="96.5" x2="982.2" y2="141.6" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="96.5" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="986.0" y1="74.0" x2="986.0" y2="109.0" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="88.3" width="2.34" height="18.2" fill="var(--down)"/>
<line x1="989.8" y1="80.0" x2="989.8" y2="104.6" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="89.1" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="993.5" y1="77.7" x2="993.5" y2="178.6" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="88.6" width="2.34" height="72.8" fill="var(--down)"/>
<line x1="997.3" y1="129.8" x2="997.3" y2="241.7" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="133.9" width="2.34" height="33.8" fill="var(--up)"/>
<line x1="1001.1" y1="95.4" x2="1001.1" y2="224.3" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="109.2" width="2.34" height="100.4" fill="var(--down)"/>
<line x1="1004.9" y1="202.7" x2="1004.9" y2="281.5" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="211.4" width="2.34" height="61.7" fill="var(--down)"/>
<line x1="1008.6" y1="231.6" x2="1008.6" y2="355.5" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="249.8" width="2.34" height="60.9" fill="var(--up)"/>
<line x1="1012.4" y1="227.6" x2="1012.4" y2="322.5" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="233.0" width="2.34" height="71.6" fill="var(--down)"/>
<line x1="1016.2" y1="293.1" x2="1016.2" y2="416.8" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="312.5" width="2.34" height="93.1" fill="var(--down)"/>
<line x1="1019.9" y1="314.3" x2="1019.9" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="344.9" width="2.34" height="45.7" fill="var(--down)"/>
<line x1="1023.7" y1="387.4" x2="1023.7" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="392.4" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="1027.5" y1="391.5" x2="1027.5" y2="494.7" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="415.8" width="2.34" height="42.0" fill="var(--down)"/>
<line x1="1031.3" y1="459.1" x2="1031.3" y2="511.3" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="474.1" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="1035.0" y1="467.8" x2="1035.0" y2="598.8" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="485.2" width="2.34" height="35.8" fill="var(--down)"/>
<line x1="1038.8" y1="437.6" x2="1038.8" y2="533.9" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="451.7" width="2.34" height="77.9" fill="var(--up)"/>
<line x1="1042.6" y1="381.1" x2="1042.6" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="393.9" width="2.34" height="50.0" fill="var(--up)"/>
<line x1="1046.3" y1="387.0" x2="1046.3" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="392.2" width="2.34" height="36.9" fill="var(--down)"/>
<line x1="1050.1" y1="406.1" x2="1050.1" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="412.0" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="60" y1="374.7" x2="1052" y2="374.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="378.2" font-size="11.5" fill="var(--resistance)" font-weight="600">887 R1</text>
<text x="1058" y="390.2" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="346.9" x2="1052" y2="346.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="350.4" font-size="11.5" fill="var(--resistance)" font-weight="600">918 R2</text>
<text x="1058" y="362.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="314.9" x2="1052" y2="314.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="318.4" font-size="11.5" fill="var(--resistance)" font-weight="600">955 R3</text>
<text x="1058" y="330.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="428.1" x2="1052" y2="428.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="422.1" font-size="11.5" fill="var(--support)" font-weight="600">826 S1</text>
<text x="1058" y="434.1" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="483.7" x2="1052" y2="483.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.7" font-size="11.5" fill="var(--support)" font-weight="600">762 S2</text>
<text x="1058" y="489.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="534.5" x2="1052" y2="534.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="528.5" font-size="11.5" fill="var(--support)" font-weight="600">704 S3</text>
<text x="1058" y="540.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="414.8" r="3" fill="var(--ink)"/>
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

- **상승**: 국내 위험선호 확대, 중소형·성장주로의 자금 유입 신호로 흔히 해석된다.
- **하락**: 국내 위험회피 심리, 유동성 위축 신호로 흔히 해석된다.
- [코스피](./kospi.md) 대비 상대 강도로 보면 국내 자금이 대형주와 중소형주 중 어느 쪽으로 쏠리는지 가늠하는 실마리가 된다.

---

## 갱신 방법

이 문서는 시점이 지나면 낡는 스냅샷이라, 정기적으로(예: 분기 1회) 재생성해 §1을 교체하는 것을 전제로 한다(§2는 손으로 갱신). 손으로 만들지 말고 아래 명령으로 생성할 것:

```bash
uv run python scripts/gen_technical_chart.py "^KQ11" --name "코스닥" --interval 1wk \
  --symbol "" --unit-label "지수" \
  --adj-note "지수 원자료(조정 없음)" --close-on <YYYY-MM-DD> --emit chart
```

커맨드 문법은 [`../../authoring-guide.md`](../../authoring-guide.md) "주가가 아닌 시계열에 쓰기" 참고.

---

## 관련 문서

- [코스피](./kospi.md) — 대형주 위주 비교군
- [러셀2000](./russell2000.md) — 미국 중소형주 비교군
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — KOSDAQ Composite Index (^KQ11)](https://finance.yahoo.com/quote/%5EKQ11/)

---

*작성일: 2026-08-20*
