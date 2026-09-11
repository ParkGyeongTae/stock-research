# 미국 30년물 국채금리

::: info
최근 5년간 미국 30년물 국채 수익률(`^TYX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 13주물 국채금리·10년물 국채금리와 함께 보면 **수익률곡선에서 가장 만기가 긴 구간**까지 채워서 볼 수 있다.

**왜 따로 다루나**: 30년물은 가장 먼 미래의 성장·물가 기대와 기간 프리미엄(만기가 길어질수록 투자자가 추가로 요구하는 보상)을 반영한다. 그래서 단기물과 달리 연준의 당장 정책보다는 장기적인 재정건전성이나 인플레이션 기대에 더 민감하게 움직이는 편이다.

:::
---

## 1. 차트 — 최근 5년 주봉

<div class="tyx-chart">
<style>
.tyx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .tyx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .tyx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tyx-chart svg { width:100%; height:auto; display:block; }
.tyx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tyx-chart .title { fill: var(--ink); font-weight:600; }
.tyx-chart .grid { stroke: var(--grid); stroke-width:1; }
.tyx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 30년물 금리(^TYX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 30년물 금리 (^TYX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-10 · 마지막 종가 5.36% (2026-09-10) · 단위 %</text>
<line x1="60" y1="561.1" x2="1052" y2="561.1" class="grid"/>
<text x="52" y="565.1" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="488.9" x2="1052" y2="488.9" class="grid"/>
<text x="52" y="492.9" font-size="11" text-anchor="end" fill="var(--muted)">2.50</text>
<line x1="60" y1="416.8" x2="1052" y2="416.8" class="grid"/>
<text x="52" y="420.8" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="344.6" x2="1052" y2="344.6" class="grid"/>
<text x="52" y="348.6" font-size="11" text-anchor="end" fill="var(--muted)">3.50</text>
<line x1="60" y1="272.5" x2="1052" y2="272.5" class="grid"/>
<text x="52" y="276.5" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="200.3" x2="1052" y2="200.3" class="grid"/>
<text x="52" y="204.3" font-size="11" text-anchor="end" fill="var(--muted)">4.50</text>
<line x1="60" y1="128.2" x2="1052" y2="128.2" class="grid"/>
<text x="52" y="132.2" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">5.50</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="126.0" y1="56.0" x2="126.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="126.0" y1="626.0" x2="126.0" y2="631.0" class="axis"/>
<text x="126.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.1" y1="56.0" x2="322.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.1" y1="626.0" x2="322.1" y2="631.0" class="axis"/>
<text x="322.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="518.3" y1="56.0" x2="518.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="518.3" y1="626.0" x2="518.3" y2="631.0" class="axis"/>
<text x="518.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="718.2" y1="56.0" x2="718.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="718.2" y1="626.0" x2="718.2" y2="631.0" class="axis"/>
<text x="718.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="914.3" y1="56.0" x2="914.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="914.3" y1="626.0" x2="914.3" y2="631.0" class="axis"/>
<text x="914.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="568.9" x2="61.9" y2="574.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="570.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="65.7" y1="569.3" x2="65.7" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="572.6" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="69.4" y1="562.2" x2="69.4" y2="585.6" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="562.8" width="2.34" height="20.8" fill="var(--up)"/>
<line x1="73.2" y1="546.2" x2="73.2" y2="562.9" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="552.7" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="77.0" y1="535.5" x2="77.0" y2="556.2" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="537.7" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="80.7" y1="537.1" x2="80.7" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="537.1" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="84.5" y1="539.4" x2="84.5" y2="559.8" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="547.9" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="88.3" y1="543.5" x2="88.3" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="546.5" width="2.34" height="22.9" fill="var(--down)"/>
<line x1="92.1" y1="557.5" x2="92.1" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="564.5" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="95.8" y1="563.5" x2="95.8" y2="590.6" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="567.6" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="99.6" y1="554.0" x2="99.6" y2="575.3" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="570.9" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="103.4" y1="555.9" x2="103.4" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="569.7" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="107.1" y1="574.1" x2="107.1" y2="607.5" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="576.8" width="2.34" height="30.7" fill="var(--down)"/>
<line x1="110.9" y1="576.4" x2="110.9" y2="605.7" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="577.8" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="114.7" y1="574.8" x2="114.7" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="581.7" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="118.5" y1="571.6" x2="118.5" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="574.8" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="122.2" y1="565.2" x2="122.2" y2="582.1" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="574.8" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="126.0" y1="539.4" x2="126.0" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="544.0" width="2.34" height="28.9" fill="var(--up)"/>
<line x1="129.8" y1="539.3" x2="129.8" y2="554.3" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="543.2" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="133.6" y1="533.4" x2="133.6" y2="553.6" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="540.0" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="137.3" y1="536.0" x2="137.3" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="549.1" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="141.1" y1="526.9" x2="141.1" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="527.4" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="144.9" y1="510.1" x2="144.9" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="524.0" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="148.6" y1="505.2" x2="148.6" y2="526.6" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="523.3" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="152.4" y1="516.0" x2="152.4" y2="537.1" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="518.3" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="156.2" y1="522.4" x2="156.2" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="525.9" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="160.0" y1="501.2" x2="160.0" y2="542.0" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="508.5" width="2.34" height="25.7" fill="var(--up)"/>
<line x1="163.7" y1="483.0" x2="163.7" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="499.6" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="167.5" y1="468.1" x2="167.5" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="474.0" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="171.3" y1="476.8" x2="171.3" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="478.8" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="175.0" y1="451.4" x2="175.0" y2="497.7" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="453.4" width="2.34" height="38.8" fill="var(--up)"/>
<line x1="178.8" y1="427.0" x2="178.8" y2="452.7" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="428.4" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="182.6" y1="414.2" x2="182.6" y2="436.2" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="423.7" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="186.4" y1="418.2" x2="186.4" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="424.4" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="190.1" y1="384.6" x2="190.1" y2="421.4" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="384.9" width="2.34" height="32.9" fill="var(--up)"/>
<line x1="193.9" y1="376.8" x2="193.9" y2="420.5" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="377.2" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="197.7" y1="387.6" x2="197.7" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="402.2" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="201.4" y1="406.4" x2="201.4" y2="427.7" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="412.0" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="205.2" y1="394.0" x2="205.2" y2="413.0" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="400.3" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="209.0" y1="382.4" x2="209.0" y2="402.6" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="388.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="212.8" y1="348.6" x2="212.8" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="374.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="216.5" y1="359.8" x2="216.5" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="365.5" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="220.3" y1="364.4" x2="220.3" y2="412.7" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="372.0" width="2.34" height="28.0" fill="var(--down)"/>
<line x1="224.1" y1="376.6" x2="224.1" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="377.9" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="227.8" y1="383.4" x2="227.8" y2="407.8" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="384.0" width="2.34" height="19.2" fill="var(--down)"/>
<line x1="231.6" y1="386.7" x2="231.6" y2="423.7" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="398.9" width="2.34" height="18.2" fill="var(--down)"/>
<line x1="235.4" y1="403.2" x2="235.4" y2="423.7" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="409.5" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="239.2" y1="401.5" x2="239.2" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="407.4" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="242.9" y1="389.5" x2="242.9" y2="425.0" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="399.7" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="246.7" y1="382.7" x2="246.7" y2="409.1" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="384.3" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="250.5" y1="369.1" x2="250.5" y2="390.2" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="384.6" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="254.3" y1="357.3" x2="254.3" y2="387.3" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="367.1" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="258.0" y1="345.9" x2="258.0" y2="364.2" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="351.0" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="261.8" y1="334.2" x2="261.8" y2="357.2" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="341.9" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="265.6" y1="319.1" x2="265.6" y2="346.5" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="328.4" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="269.3" y1="294.5" x2="269.3" y2="328.4" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="306.4" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="273.1" y1="290.2" x2="273.1" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="295.4" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="276.9" y1="270.7" x2="276.9" y2="294.7" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="275.6" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="280.7" y1="217.2" x2="280.7" y2="283.1" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="228.4" width="2.34" height="51.8" fill="var(--up)"/>
<line x1="284.4" y1="211.1" x2="284.4" y2="263.8" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="227.1" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="288.2" y1="233.9" x2="288.2" y2="264.7" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="237.0" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="292.0" y1="224.3" x2="292.0" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="241.1" width="2.34" height="22.9" fill="var(--down)"/>
<line x1="295.7" y1="259.9" x2="295.7" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="261.9" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="299.5" y1="284.7" x2="299.5" y2="310.4" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="286.6" width="2.34" height="21.8" fill="var(--down)"/>
<line x1="303.3" y1="294.5" x2="303.3" y2="336.2" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="313.1" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="307.1" y1="323.0" x2="307.1" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="335.5" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="310.8" y1="330.5" x2="310.8" y2="351.2" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="339.8" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="314.6" y1="297.1" x2="314.6" y2="328.3" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="297.4" width="2.34" height="28.7" fill="var(--up)"/>
<line x1="318.4" y1="273.9" x2="318.4" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="276.1" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="322.1" y1="285.2" x2="322.1" y2="319.1" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="292.4" width="2.34" height="24.5" fill="var(--down)"/>
<line x1="325.9" y1="304.9" x2="325.9" y2="336.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="312.3" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="329.7" y1="316.3" x2="329.7" y2="341.4" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="317.8" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="333.5" y1="313.1" x2="333.5" y2="332.8" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="318.5" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="337.2" y1="318.1" x2="337.2" y2="344.9" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="321.5" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="341.0" y1="296.0" x2="341.0" y2="326.0" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="297.4" width="2.34" height="24.4" fill="var(--up)"/>
<line x1="344.8" y1="279.4" x2="344.8" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="288.6" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="348.5" y1="275.2" x2="348.5" y2="293.5" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="281.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="352.3" y1="265.7" x2="352.3" y2="289.2" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="277.2" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="356.1" y1="282.3" x2="356.1" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="296.8" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="359.9" y1="301.7" x2="359.9" y2="340.9" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="330.5" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="363.6" y1="305.6" x2="363.6" y2="328.3" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="323.8" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="367.4" y1="299.2" x2="367.4" y2="317.5" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="314.7" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="371.2" y1="315.6" x2="371.2" y2="340.7" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="316.3" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="375.0" y1="308.0" x2="375.0" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="310.1" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="378.7" y1="296.6" x2="378.7" y2="312.3" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="304.5" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="382.5" y1="305.9" x2="382.5" y2="325.8" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="308.0" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="386.3" y1="298.3" x2="386.3" y2="321.1" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="306.8" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="390.0" y1="293.4" x2="390.0" y2="313.3" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="300.9" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="393.8" y1="278.2" x2="393.8" y2="301.3" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="280.0" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="397.6" y1="271.2" x2="397.6" y2="284.1" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="276.9" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="401.4" y1="281.4" x2="401.4" y2="301.0" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="287.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="405.1" y1="275.3" x2="405.1" y2="292.4" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="281.3" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="408.9" y1="280.4" x2="408.9" y2="301.0" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="291.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="412.7" y1="289.8" x2="412.7" y2="303.2" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="296.1" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="416.4" y1="283.0" x2="416.4" y2="305.8" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="293.4" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="420.2" y1="263.7" x2="420.2" y2="299.6" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="267.5" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="424.0" y1="260.2" x2="424.0" y2="289.9" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="264.5" width="2.34" height="19.0" fill="var(--down)"/>
<line x1="427.8" y1="280.0" x2="427.8" y2="295.8" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="285.9" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="431.5" y1="262.5" x2="431.5" y2="289.9" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="268.1" width="2.34" height="21.1" fill="var(--up)"/>
<line x1="435.3" y1="225.4" x2="435.3" y2="274.0" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="241.6" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="439.1" y1="230.5" x2="439.1" y2="251.5" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="233.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="442.8" y1="211.0" x2="442.8" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="217.8" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="446.6" y1="204.1" x2="446.6" y2="234.2" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="209.7" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="450.4" y1="227.3" x2="450.4" y2="246.5" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="231.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="454.2" y1="216.9" x2="454.2" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="223.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="457.9" y1="211.6" x2="457.9" y2="225.3" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="213.1" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="461.7" y1="190.2" x2="461.7" y2="217.2" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="197.3" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="465.5" y1="155.9" x2="465.5" y2="185.9" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="169.9" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="469.2" y1="120.5" x2="469.2" y2="166.0" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="136.7" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="473.0" y1="133.2" x2="473.0" y2="173.6" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="133.2" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="476.8" y1="107.4" x2="476.8" y2="152.8" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="115.3" width="2.34" height="33.6" fill="var(--up)"/>
<line x1="480.6" y1="106.2" x2="480.6" y2="133.5" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="106.2" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="484.3" y1="114.4" x2="484.3" y2="175.2" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="119.6" width="2.34" height="44.3" fill="var(--down)"/>
<line x1="488.1" y1="151.7" x2="488.1" y2="181.1" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="158.2" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="491.9" y1="155.9" x2="491.9" y2="189.8" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="163.7" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="495.7" y1="180.5" x2="495.7" y2="197.7" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="182.1" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="499.4" y1="186.0" x2="499.4" y2="215.0" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="186.3" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="503.2" y1="206.2" x2="503.2" y2="242.0" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="212.6" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="507.0" y1="218.5" x2="507.0" y2="271.6" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="221.7" width="2.34" height="46.9" fill="var(--down)"/>
<line x1="510.7" y1="260.2" x2="510.7" y2="275.8" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="264.7" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="514.5" y1="263.9" x2="514.5" y2="280.7" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="263.9" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="518.3" y1="238.8" x2="518.3" y2="265.7" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="243.6" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="522.1" y1="236.7" x2="522.1" y2="251.7" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="240.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="525.8" y1="214.3" x2="525.8" y2="239.1" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="221.5" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="529.6" y1="211.1" x2="529.6" y2="230.9" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="216.2" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="533.4" y1="220.1" x2="533.4" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="222.4" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="537.1" y1="216.8" x2="537.1" y2="231.8" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="217.5" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="540.9" y1="202.3" x2="540.9" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="207.8" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="544.7" y1="199.6" x2="544.7" y2="219.1" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="207.2" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="548.5" y1="208.1" x2="548.5" y2="225.4" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="219.9" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="552.2" y1="217.5" x2="552.2" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="219.6" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="556.0" y1="207.5" x2="556.0" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="210.7" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="559.8" y1="201.7" x2="559.8" y2="219.6" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="208.5" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="563.5" y1="209.7" x2="563.5" y2="225.3" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="214.2" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="567.3" y1="190.2" x2="567.3" y2="215.9" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="195.7" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="571.1" y1="173.6" x2="571.1" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="185.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="574.9" y1="156.3" x2="574.9" y2="175.1" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="169.9" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="578.6" y1="150.4" x2="578.6" y2="172.7" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="159.8" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="582.4" y1="158.2" x2="582.4" y2="180.8" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="165.5" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="586.2" y1="174.9" x2="586.2" y2="190.3" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="179.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="589.9" y1="175.8" x2="589.9" y2="205.1" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="181.1" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="593.7" y1="185.3" x2="593.7" y2="198.9" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="189.8" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="597.5" y1="163.4" x2="597.5" y2="190.8" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="178.4" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="601.3" y1="183.1" x2="601.3" y2="210.7" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="183.1" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="605.0" y1="185.0" x2="605.0" y2="224.5" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="188.8" width="2.34" height="33.0" fill="var(--down)"/>
<line x1="608.8" y1="209.8" x2="608.8" y2="221.8" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="213.9" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="612.6" y1="198.0" x2="612.6" y2="223.0" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="200.0" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="616.3" y1="177.9" x2="616.3" y2="205.4" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="188.5" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="620.1" y1="197.7" x2="620.1" y2="218.2" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="200.6" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="623.9" y1="204.2" x2="623.9" y2="220.7" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="204.6" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="627.7" y1="192.8" x2="627.7" y2="212.7" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="206.7" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="631.4" y1="209.1" x2="631.4" y2="257.3" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="212.6" width="2.34" height="44.2" fill="var(--down)"/>
<line x1="635.2" y1="227.1" x2="635.2" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="240.0" width="2.34" height="27.4" fill="var(--up)"/>
<line x1="639.0" y1="236.8" x2="639.0" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="240.0" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="642.8" y1="250.7" x2="642.8" y2="266.7" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="256.4" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="646.5" y1="243.2" x2="646.5" y2="262.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="244.2" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="650.3" y1="242.7" x2="650.3" y2="278.9" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="244.2" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="654.1" y1="265.1" x2="654.1" y2="282.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="265.1" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="657.8" y1="259.5" x2="657.8" y2="286.0" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="262.2" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="661.6" y1="248.5" x2="661.6" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="257.2" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="665.4" y1="232.9" x2="665.4" y2="267.5" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="233.9" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="669.2" y1="211.8" x2="669.2" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="217.2" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="672.9" y1="213.0" x2="672.9" y2="232.5" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="213.4" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="676.7" y1="195.1" x2="676.7" y2="209.8" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="200.4" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="680.5" y1="188.3" x2="680.5" y2="210.3" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="191.9" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="684.2" y1="176.3" x2="684.2" y2="208.4" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="203.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="688.0" y1="177.8" x2="688.0" y2="203.9" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="185.7" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="691.8" y1="174.8" x2="691.8" y2="195.7" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="175.6" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="695.6" y1="197.7" x2="695.6" y2="220.4" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="199.3" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="699.3" y1="207.4" x2="699.3" y2="228.7" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="217.6" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="703.1" y1="183.3" x2="703.1" y2="221.8" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="183.7" width="2.34" height="35.6" fill="var(--up)"/>
<line x1="706.9" y1="160.6" x2="706.9" y2="190.8" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="169.1" width="2.34" height="19.3" fill="var(--up)"/>
<line x1="710.6" y1="154.3" x2="710.6" y2="167.3" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="155.4" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="714.4" y1="154.4" x2="714.4" y2="166.4" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="155.0" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="718.2" y1="127.6" x2="718.2" y2="157.2" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="133.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="722.0" y1="127.4" x2="722.0" y2="156.7" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="135.8" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="725.7" y1="143.7" x2="725.7" y2="160.8" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="150.1" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="729.5" y1="154.1" x2="729.5" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="155.1" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="733.3" y1="152.4" x2="733.3" y2="182.7" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="166.4" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="737.0" y1="147.9" x2="737.0" y2="176.6" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="170.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="740.8" y1="157.3" x2="740.8" y2="178.5" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="166.1" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="744.6" y1="171.3" x2="744.6" y2="199.6" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="173.3" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="748.4" y1="181.0" x2="748.4" y2="209.4" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="183.6" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="752.1" y1="175.6" x2="752.1" y2="198.3" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="183.7" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="755.9" y1="179.8" x2="755.9" y2="201.7" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="186.5" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="759.7" y1="165.1" x2="759.7" y2="182.4" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="180.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="763.5" y1="182.0" x2="763.5" y2="223.2" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="188.8" width="2.34" height="27.7" fill="var(--down)"/>
<line x1="767.2" y1="129.6" x2="767.2" y2="209.7" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="145.9" width="2.34" height="63.3" fill="var(--up)"/>
<line x1="771.0" y1="147.8" x2="771.0" y2="166.2" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="150.2" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="774.8" y1="140.4" x2="774.8" y2="169.9" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="144.3" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="778.5" y1="156.6" x2="778.5" y2="185.4" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="157.7" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="782.3" y1="146.5" x2="782.3" y2="162.9" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="152.3" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="786.1" y1="128.2" x2="786.1" y2="149.7" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="142.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="789.9" y1="106.1" x2="789.9" y2="137.7" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="123.7" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="793.6" y1="126.9" x2="793.6" y2="142.3" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="131.3" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="797.4" y1="127.9" x2="797.4" y2="152.1" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="131.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="801.2" y1="129.5" x2="801.2" y2="153.1" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="132.5" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="804.9" y1="134.5" x2="804.9" y2="149.8" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="137.7" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="808.7" y1="139.4" x2="808.7" y2="158.5" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="145.3" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="812.5" y1="144.0" x2="812.5" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="148.1" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="816.3" y1="131.9" x2="816.3" y2="148.5" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="134.4" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="820.0" y1="117.0" x2="820.0" y2="137.8" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="128.0" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="823.8" y1="129.6" x2="823.8" y2="143.7" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="137.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="827.6" y1="133.1" x2="827.6" y2="156.9" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="135.9" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="831.3" y1="146.5" x2="831.3" y2="161.9" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="149.1" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="835.1" y1="137.7" x2="835.1" y2="158.0" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="138.8" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="838.9" y1="134.8" x2="838.9" y2="147.9" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="143.4" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="842.7" y1="133.9" x2="842.7" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="140.1" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="846.4" y1="128.4" x2="846.4" y2="161.6" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="130.0" width="2.34" height="30.6" fill="var(--down)"/>
<line x1="850.2" y1="161.6" x2="850.2" y2="180.4" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="163.7" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="854.0" y1="162.6" x2="854.0" y2="185.0" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="163.4" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="857.7" y1="159.2" x2="857.7" y2="169.0" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="161.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="861.5" y1="166.1" x2="861.5" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="168.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="865.3" y1="162.4" x2="865.3" y2="182.1" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="163.2" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="869.1" y1="179.1" x2="869.1" y2="188.8" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="181.4" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="872.8" y1="183.1" x2="872.8" y2="196.3" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="186.5" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="876.6" y1="175.6" x2="876.6" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="175.8" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="880.4" y1="165.1" x2="880.4" y2="176.9" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="171.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="884.2" y1="164.1" x2="884.2" y2="178.9" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="164.7" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="887.9" y1="160.3" x2="887.9" y2="171.6" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="165.2" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="891.7" y1="171.9" x2="891.7" y2="180.7" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="172.7" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="895.5" y1="157.0" x2="895.5" y2="170.6" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="158.2" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="899.2" y1="147.3" x2="899.2" y2="164.4" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="148.6" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="903.0" y1="146.8" x2="903.0" y2="158.9" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="152.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="906.8" y1="147.8" x2="906.8" y2="159.8" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="150.8" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="910.6" y1="146.2" x2="910.6" y2="157.9" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="147.8" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="914.3" y1="144.5" x2="914.3" y2="156.0" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="146.3" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="918.1" y1="148.2" x2="918.1" y2="161.1" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="148.5" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="921.9" y1="135.8" x2="921.9" y2="154.3" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="140.6" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="925.6" y1="143.3" x2="925.6" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="146.6" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="929.4" y1="138.5" x2="929.4" y2="149.9" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="146.8" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="933.2" y1="144.0" x2="933.2" y2="172.7" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="144.2" width="2.34" height="27.6" fill="var(--down)"/>
<line x1="937.0" y1="163.7" x2="937.0" y2="176.6" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="167.8" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="940.7" y1="167.8" x2="940.7" y2="182.0" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="167.8" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="944.5" y1="156.9" x2="944.5" y2="177.6" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="163.5" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="948.3" y1="140.3" x2="948.3" y2="167.3" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="141.4" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="952.0" y1="133.6" x2="952.0" y2="152.8" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="133.9" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="955.8" y1="128.3" x2="955.8" y2="144.6" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="130.7" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="959.6" y1="136.5" x2="959.6" y2="145.9" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="138.8" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="963.4" y1="135.8" x2="963.4" y2="151.8" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="139.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="967.1" y1="136.2" x2="967.1" y2="148.2" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="136.5" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="970.9" y1="136.2" x2="970.9" y2="145.9" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="140.3" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="974.7" y1="128.7" x2="974.7" y2="140.0" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="133.1" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="978.4" y1="123.1" x2="978.4" y2="140.1" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="130.7" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="982.2" y1="109.2" x2="982.2" y2="134.4" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="109.7" width="2.34" height="23.2" fill="var(--up)"/>
<line x1="986.0" y1="99.7" x2="986.0" y2="120.1" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="109.5" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="989.8" y1="120.5" x2="989.8" y2="132.9" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="126.7" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="993.5" y1="124.3" x2="993.5" y2="135.8" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="128.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="997.3" y1="122.5" x2="997.3" y2="135.9" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="127.0" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="1001.1" y1="131.8" x2="1001.1" y2="148.4" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="134.5" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="1004.9" y1="134.5" x2="1004.9" y2="153.7" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="138.0" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="1008.6" y1="128.6" x2="1008.6" y2="149.7" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="130.3" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="1012.4" y1="114.9" x2="1012.4" y2="132.3" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="117.9" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="1016.2" y1="109.4" x2="1016.2" y2="121.7" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="115.9" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="1019.9" y1="100.3" x2="1019.9" y2="116.5" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="104.8" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="1023.7" y1="87.6" x2="1023.7" y2="115.9" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="88.5" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="1027.5" y1="93.1" x2="1027.5" y2="105.5" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="97.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1031.3" y1="88.8" x2="1031.3" y2="102.0" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="89.9" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="1035.0" y1="81.1" x2="1035.0" y2="101.7" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="88.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1038.8" y1="92.5" x2="1038.8" y2="105.8" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="93.1" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="1042.6" y1="88.2" x2="1042.6" y2="96.4" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="92.7" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="1046.3" y1="75.3" x2="1046.3" y2="97.0" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="76.1" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="1050.1" y1="75.3" x2="1050.1" y2="81.8" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="76.1" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="60" y1="160.1" x2="1052" y2="160.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="154.1" font-size="11.5" fill="var(--support)" font-weight="600">4.78% S1</text>
<text x="1058" y="166.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="189.1" x2="1052" y2="189.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="183.1" font-size="11.5" fill="var(--support)" font-weight="600">4.58% S2</text>
<text x="1058" y="195.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="225.5" x2="1052" y2="225.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="219.5" font-size="11.5" fill="var(--support)" font-weight="600">4.33% S3</text>
<text x="1058" y="231.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="76.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="68.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 5.36% (2026-09-10)</text>
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

## 2. 해석

- **상승**: 장기적인 재정건전성 우려, 장기 인플레이션 기대 확대 신호로 흔히 해석한다 — 단기물보다 당장의 연준 정책보다는 먼 미래에 대한 기대에 더 민감하다.
- **하락**: 장기 성장·인플레이션 기대 둔화, 안전자산 수요 확대 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 30년물 수익률은 "앞으로 30년간 평균 단기금리가 어떻게 움직일지에 대한 기대"보다 **기간 프리미엄**(만기가 길어질수록 투자자가 추가로 요구하는 보상) 비중이 더 크다. 그래서 당장의 통화정책보다는 장기 국채 발행량(재정 전망), 장기 성장·인플레이션 기대에 더 민감하게 움직인다. 연기금·보험사처럼 오랫동안 갚아야 할 부채를 가진 기관들이 구조적으로 사들이는 수요도 가격에 영향을 준다.
- 밸류에이션(DCF 무위험이자율)의 표준 근거로는 쓰지 않는다 — 표준은 10년물이다. 이 문서는 수익률곡선의 모양을 보기 위한 보조 자료다.

---

*작성일: 2026-09-11*
