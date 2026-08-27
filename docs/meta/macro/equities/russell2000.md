# 러셀2000

!!! note ""
    최근 5년간 러셀2000 지수(미국 중소형주 2,000종목, `^RUT`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. S&P 500·나스닥종합지수·필라델피아 반도체지수는 모두 대형주 위주 지수인 반면, 러셀2000은 **미국 국내 경기에 더 민감하게 반응하는 중소형주**를 담고 있어서 다른 신호를 준다 — 대형주 지수는 오르는데 러셀2000만 약하다면, 시장 상승세가 소수의 대형주에만 쏠려 있다는 신호로 읽히곤 한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="rut-chart">
<style>
.rut-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .rut-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 3,017.87 (2026-08-21) · 단위 지수</text>
<line x1="60" y1="616.8" x2="1052" y2="616.8" class="grid"/>
<text x="52" y="620.8" font-size="11" text-anchor="end" fill="var(--muted)">1,600.00</text>
<line x1="60" y1="543.3" x2="1052" y2="543.3" class="grid"/>
<text x="52" y="547.3" font-size="11" text-anchor="end" fill="var(--muted)">1,800.00</text>
<line x1="60" y1="469.7" x2="1052" y2="469.7" class="grid"/>
<text x="52" y="473.7" font-size="11" text-anchor="end" fill="var(--muted)">2,000.00</text>
<line x1="60" y1="396.2" x2="1052" y2="396.2" class="grid"/>
<text x="52" y="400.2" font-size="11" text-anchor="end" fill="var(--muted)">2,200.00</text>
<line x1="60" y1="322.6" x2="1052" y2="322.6" class="grid"/>
<text x="52" y="326.6" font-size="11" text-anchor="end" fill="var(--muted)">2,400.00</text>
<line x1="60" y1="249.1" x2="1052" y2="249.1" class="grid"/>
<text x="52" y="253.1" font-size="11" text-anchor="end" fill="var(--muted)">2,600.00</text>
<line x1="60" y1="175.5" x2="1052" y2="175.5" class="grid"/>
<text x="52" y="179.5" font-size="11" text-anchor="end" fill="var(--muted)">2,800.00</text>
<line x1="60" y1="102.0" x2="1052" y2="102.0" class="grid"/>
<text x="52" y="106.0" font-size="11" text-anchor="end" fill="var(--muted)">3,000.00</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="133.8" y1="56.0" x2="133.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.8" y1="626.0" x2="133.8" y2="631.0" class="axis"/>
<text x="133.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="330.7" y1="56.0" x2="330.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="330.7" y1="626.0" x2="330.7" y2="631.0" class="axis"/>
<text x="330.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="527.6" y1="56.0" x2="527.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="527.6" y1="626.0" x2="527.6" y2="631.0" class="axis"/>
<text x="527.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="728.3" y1="56.0" x2="728.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="728.3" y1="626.0" x2="728.3" y2="631.0" class="axis"/>
<text x="728.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.2" y1="56.0" x2="925.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="925.2" y1="626.0" x2="925.2" y2="631.0" class="axis"/>
<text x="925.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="366.1" x2="61.9" y2="407.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="367.8" width="2.35" height="39.7" fill="var(--up)"/>
<line x1="65.7" y1="355.7" x2="65.7" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="362.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="69.5" y1="359.2" x2="69.5" y2="386.0" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="362.3" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="73.3" y1="377.8" x2="73.3" y2="394.6" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="382.6" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="77.0" y1="372.0" x2="77.0" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="378.5" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="80.8" y1="361.8" x2="80.8" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="378.5" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="84.6" y1="372.2" x2="84.6" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="381.1" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="88.4" y1="357.1" x2="88.4" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="372.0" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="92.2" y1="357.9" x2="92.2" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="362.6" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="96.0" y1="351.5" x2="96.0" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="360.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="99.8" y1="304.5" x2="99.8" y2="360.1" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="309.0" width="2.35" height="51.1" fill="var(--up)"/>
<line x1="103.5" y1="301.0" x2="103.5" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="308.5" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="107.3" y1="314.9" x2="107.3" y2="344.1" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="318.2" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="111.1" y1="333.8" x2="111.1" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="343.3" width="2.35" height="35.9" fill="var(--down)"/>
<line x1="114.9" y1="366.3" x2="114.9" y2="417.1" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="378.2" width="2.35" height="32.9" fill="var(--down)"/>
<line x1="118.7" y1="367.9" x2="118.7" y2="412.8" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="391.8" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="122.5" y1="390.2" x2="122.5" y2="423.8" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="391.9" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="126.3" y1="378.6" x2="126.3" y2="430.1" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="380.9" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="130.0" y1="368.7" x2="130.0" y2="385.0" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="379.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="133.8" y1="363.7" x2="133.8" y2="403.8" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="379.0" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="137.6" y1="392.4" x2="137.6" y2="423.3" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="403.9" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="141.4" y1="410.7" x2="141.4" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="410.7" width="2.35" height="63.4" fill="var(--down)"/>
<line x1="145.2" y1="451.9" x2="145.2" y2="506.0" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="474.7" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="149.0" y1="449.6" x2="149.0" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="468.8" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="152.8" y1="431.0" x2="152.8" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="458.6" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="156.5" y1="438.5" x2="156.5" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="458.6" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="160.3" y1="454.7" x2="160.3" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="454.7" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="164.1" y1="445.0" x2="164.1" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="454.9" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="167.9" y1="459.6" x2="167.9" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="469.3" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="171.7" y1="437.5" x2="171.7" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="438.0" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="175.5" y1="433.8" x2="175.5" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="438.2" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="179.3" y1="418.8" x2="179.3" y2="451.5" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="436.2" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="183.1" y1="431.7" x2="183.1" y2="475.5" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="436.1" width="2.35" height="35.7" fill="var(--down)"/>
<line x1="186.8" y1="457.1" x2="186.8" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="467.9" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="190.6" y1="447.6" x2="190.6" y2="492.0" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="468.5" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="194.4" y1="486.5" x2="194.4" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="494.3" width="2.35" height="25.4" fill="var(--down)"/>
<line x1="198.2" y1="487.1" x2="198.2" y2="535.5" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="519.8" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="202.0" y1="530.9" x2="202.0" y2="579.6" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="530.9" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="205.8" y1="528.4" x2="205.8" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="546.7" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="209.6" y1="510.9" x2="209.6" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="510.9" width="2.35" height="37.3" fill="var(--up)"/>
<line x1="213.3" y1="507.3" x2="213.3" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="512.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="217.1" y1="499.2" x2="217.1" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="508.9" width="2.35" height="34.3" fill="var(--down)"/>
<line x1="220.9" y1="554.1" x2="220.9" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="554.1" width="2.35" height="38.5" fill="var(--down)"/>
<line x1="224.7" y1="555.9" x2="224.7" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="555.9" width="2.35" height="31.1" fill="var(--up)"/>
<line x1="228.5" y1="546.0" x2="228.5" y2="587.2" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="553.2" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="232.3" y1="550.6" x2="232.3" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="554.5" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="236.1" y1="555.9" x2="236.1" y2="585.6" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="555.9" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="239.8" y1="527.7" x2="239.8" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="540.7" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="243.6" y1="510.8" x2="243.6" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="511.9" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="247.4" y1="498.2" x2="247.4" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="498.5" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="251.2" y1="463.6" x2="251.2" y2="504.7" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="463.6" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="255.0" y1="458.7" x2="255.0" y2="487.2" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="467.0" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="258.8" y1="482.5" x2="258.8" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="494.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="262.6" y1="507.0" x2="262.6" y2="543.6" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="513.6" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="266.4" y1="512.0" x2="266.4" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="512.8" width="2.35" height="25.6" fill="var(--up)"/>
<line x1="270.1" y1="504.2" x2="270.1" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="510.2" width="2.35" height="33.7" fill="var(--down)"/>
<line x1="273.9" y1="538.1" x2="273.9" y2="595.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="548.5" width="2.35" height="39.0" fill="var(--down)"/>
<line x1="277.7" y1="570.7" x2="277.7" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="589.5" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="281.5" y1="552.2" x2="281.5" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="579.2" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="285.3" y1="562.4" x2="285.3" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="577.8" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="289.1" y1="549.9" x2="289.1" y2="580.0" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="564.5" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="292.9" y1="525.5" x2="292.9" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="526.0" width="2.35" height="36.5" fill="var(--up)"/>
<line x1="296.6" y1="518.0" x2="296.6" y2="558.7" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="528.9" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="300.4" y1="506.5" x2="300.4" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="512.8" width="2.35" height="27.5" fill="var(--up)"/>
<line x1="304.2" y1="504.3" x2="304.2" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="515.4" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="308.0" y1="516.2" x2="308.0" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="517.8" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="311.8" y1="507.1" x2="311.8" y2="535.4" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="509.1" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="315.6" y1="511.6" x2="315.6" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="511.6" width="2.35" height="32.9" fill="var(--down)"/>
<line x1="319.4" y1="513.6" x2="319.4" y2="563.0" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="543.7" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="323.1" y1="549.1" x2="323.1" y2="570.2" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="556.5" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="326.9" y1="555.1" x2="326.9" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="557.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="330.7" y1="544.9" x2="330.7" y2="566.3" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="545.9" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="334.5" y1="510.5" x2="334.5" y2="545.8" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="511.3" width="2.35" height="31.6" fill="var(--up)"/>
<line x1="338.3" y1="505.1" x2="338.3" y2="533.9" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="511.4" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="342.1" y1="499.6" x2="342.1" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="502.3" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="345.9" y1="467.0" x2="345.9" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="475.0" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="349.6" y1="478.5" x2="349.6" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="478.5" width="2.35" height="21.1" fill="var(--down)"/>
<line x1="353.4" y1="483.5" x2="353.4" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="489.4" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="357.2" y1="492.9" x2="357.2" y2="515.4" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="492.9" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="361.0" y1="494.8" x2="361.0" y2="514.7" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="496.1" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="364.8" y1="495.9" x2="364.8" y2="559.1" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="496.2" width="2.35" height="57.1" fill="var(--down)"/>
<line x1="368.6" y1="542.5" x2="368.6" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="559.8" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="372.4" y1="547.5" x2="372.4" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="567.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="376.2" y1="542.3" x2="376.2" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="542.3" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="379.9" y1="538.7" x2="379.9" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="541.8" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="383.7" y1="541.4" x2="383.7" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="550.2" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="387.5" y1="539.7" x2="387.5" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="546.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="391.3" y1="544.1" x2="391.3" y2="570.5" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="546.8" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="395.1" y1="548.7" x2="395.1" y2="578.3" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="556.0" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="398.9" y1="553.2" x2="398.9" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="555.6" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="402.7" y1="543.1" x2="402.7" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="552.9" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="406.4" y1="537.2" x2="406.4" y2="564.9" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="551.5" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="410.2" y1="531.6" x2="410.2" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="531.9" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="414.0" y1="508.9" x2="414.0" y2="544.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="519.1" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="417.8" y1="504.0" x2="417.8" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="515.5" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="421.6" y1="516.1" x2="421.6" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="517.0" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="425.4" y1="507.1" x2="425.4" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="510.6" width="2.35" height="24.8" fill="var(--up)"/>
<line x1="429.2" y1="507.0" x2="429.2" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="511.3" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="432.9" y1="487.2" x2="432.9" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="495.1" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="436.7" y1="473.3" x2="436.7" y2="496.7" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="484.3" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="440.5" y1="471.6" x2="440.5" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="476.5" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="444.3" y1="468.4" x2="444.3" y2="488.6" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="475.3" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="448.1" y1="483.9" x2="448.1" y2="501.3" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="484.7" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="451.9" y1="498.8" x2="451.9" y2="531.9" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="499.1" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="455.7" y1="516.2" x2="455.7" y2="531.5" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="521.1" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="459.5" y1="496.6" x2="459.5" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="498.8" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="463.2" y1="500.5" x2="463.2" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="500.5" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="467.0" y1="518.2" x2="467.0" y2="529.4" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="520.0" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="470.8" y1="525.7" x2="470.8" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="525.7" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="474.6" y1="539.7" x2="474.6" y2="557.4" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="548.7" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="478.4" y1="549.9" x2="478.4" y2="576.5" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="550.3" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="482.2" y1="548.2" x2="482.2" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="565.9" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="486.0" y1="550.7" x2="486.0" y2="587.4" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="567.5" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="489.7" y1="583.6" x2="489.7" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="590.4" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="493.5" y1="554.1" x2="493.5" y2="603.8" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="557.7" width="2.35" height="42.0" fill="var(--up)"/>
<line x1="497.3" y1="557.7" x2="497.3" y2="585.8" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="557.9" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="501.1" y1="532.2" x2="501.1" y2="583.4" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="544.1" width="2.35" height="36.4" fill="var(--up)"/>
<line x1="504.9" y1="539.5" x2="504.9" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="540.5" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="508.7" y1="519.8" x2="508.7" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="520.2" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="512.5" y1="510.6" x2="512.5" y2="525.3" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="513.5" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="516.2" y1="466.4" x2="516.2" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="475.2" width="2.35" height="38.8" fill="var(--up)"/>
<line x1="520.0" y1="454.1" x2="520.0" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="457.2" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="523.8" y1="443.3" x2="523.8" y2="459.8" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="453.8" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="527.6" y1="457.8" x2="527.6" y2="491.1" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="465.0" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="531.4" y1="473.8" x2="531.4" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="487.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="535.2" y1="490.2" x2="535.2" y2="507.1" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="490.2" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="539.0" y1="469.3" x2="539.0" y2="484.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="477.7" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="542.7" y1="465.4" x2="542.7" y2="493.2" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="477.7" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="546.5" y1="465.7" x2="546.5" y2="498.6" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="466.0" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="550.3" y1="446.6" x2="550.3" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="453.1" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="554.1" y1="460.0" x2="554.1" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="463.6" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="557.9" y1="441.0" x2="557.9" y2="465.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="441.6" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="561.7" y1="427.1" x2="561.7" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="437.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="565.5" y1="440.2" x2="565.5" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="441.9" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="569.3" y1="430.6" x2="569.3" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="443.2" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="573.0" y1="419.9" x2="573.0" y2="444.0" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="423.9" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="576.8" y1="423.4" x2="576.8" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="423.4" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="580.6" y1="438.8" x2="580.6" y2="471.6" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="442.2" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="584.4" y1="463.6" x2="584.4" y2="494.9" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="465.7" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="588.2" y1="465.9" x2="588.2" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="469.0" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="592.0" y1="449.5" x2="592.0" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="456.6" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="595.8" y1="439.5" x2="595.8" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="447.7" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="599.5" y1="428.4" x2="599.5" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="434.5" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="603.3" y1="429.4" x2="603.3" y2="454.7" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="434.2" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="607.1" y1="438.0" x2="607.1" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="441.9" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="610.9" y1="437.3" x2="610.9" y2="461.2" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="439.4" width="2.35" height="20.5" fill="var(--down)"/>
<line x1="614.7" y1="437.2" x2="614.7" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="465.2" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="618.5" y1="457.4" x2="618.5" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="461.6" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="622.3" y1="448.6" x2="622.3" y2="465.9" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="452.2" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="626.0" y1="450.1" x2="626.0" y2="462.7" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="451.1" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="629.8" y1="409.5" x2="629.8" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="415.2" width="2.35" height="40.4" fill="var(--up)"/>
<line x1="633.6" y1="367.4" x2="633.6" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="401.9" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="637.4" y1="371.2" x2="637.4" y2="404.8" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="374.1" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="641.2" y1="359.4" x2="641.2" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="372.0" width="2.35" height="57.5" fill="var(--down)"/>
<line x1="645.0" y1="434.8" x2="645.0" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="440.0" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="648.8" y1="414.6" x2="648.8" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="417.5" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="652.5" y1="387.8" x2="652.5" y2="418.9" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="389.3" width="2.35" height="27.5" fill="var(--up)"/>
<line x1="656.3" y1="382.3" x2="656.3" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="385.1" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="660.1" y1="393.8" x2="660.1" y2="437.4" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="393.8" width="2.35" height="42.3" fill="var(--down)"/>
<line x1="663.9" y1="402.2" x2="663.9" y2="448.1" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="402.6" width="2.35" height="32.9" fill="var(--up)"/>
<line x1="667.7" y1="374.4" x2="667.7" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="385.9" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="671.5" y1="380.1" x2="671.5" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="384.8" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="675.3" y1="383.6" x2="675.3" y2="406.0" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="390.1" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="679.1" y1="383.3" x2="679.1" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="383.5" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="682.8" y1="363.3" x2="682.8" y2="385.8" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="368.2" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="686.6" y1="368.4" x2="686.6" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="368.5" width="2.35" height="24.8" fill="var(--down)"/>
<line x1="690.4" y1="373.9" x2="690.4" y2="397.4" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="389.7" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="694.2" y1="321.7" x2="694.2" y2="396.1" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="322.7" width="2.35" height="71.0" fill="var(--up)"/>
<line x1="698.0" y1="307.3" x2="698.0" y2="360.3" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="318.3" width="2.35" height="39.7" fill="var(--down)"/>
<line x1="701.8" y1="319.2" x2="701.8" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="320.2" width="2.35" height="36.8" fill="var(--up)"/>
<line x1="705.6" y1="298.2" x2="705.6" y2="316.8" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="309.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="709.3" y1="306.9" x2="709.3" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="308.9" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="713.1" y1="312.3" x2="713.1" y2="346.0" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="315.7" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="716.9" y1="333.5" x2="716.9" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="342.9" width="2.35" height="37.7" fill="var(--down)"/>
<line x1="720.7" y1="366.1" x2="720.7" y2="389.0" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="379.8" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="724.5" y1="370.8" x2="724.5" y2="395.2" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="371.0" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="728.3" y1="362.2" x2="728.3" y2="405.0" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="368.3" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="732.1" y1="363.1" x2="732.1" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="368.3" width="2.35" height="36.5" fill="var(--up)"/>
<line x1="735.8" y1="351.2" x2="735.8" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="356.5" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="739.6" y1="351.2" x2="739.6" y2="370.7" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="363.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="743.4" y1="349.5" x2="743.4" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="366.8" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="747.2" y1="360.2" x2="747.2" y2="381.3" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="363.3" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="751.0" y1="361.4" x2="751.0" y2="398.3" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="366.2" width="2.35" height="31.7" fill="var(--down)"/>
<line x1="754.8" y1="395.4" x2="754.8" y2="423.3" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="395.9" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="758.6" y1="405.9" x2="758.6" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="407.9" width="2.35" height="34.0" fill="var(--down)"/>
<line x1="762.4" y1="448.3" x2="762.4" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="448.3" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="766.1" y1="435.9" x2="766.1" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="448.8" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="769.9" y1="429.1" x2="769.9" y2="464.9" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="442.0" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="773.7" y1="452.0" x2="773.7" y2="549.5" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="470.5" width="2.35" height="62.9" fill="var(--down)"/>
<line x1="777.5" y1="495.2" x2="777.5" y2="567.9" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="521.1" width="2.35" height="31.3" fill="var(--up)"/>
<line x1="781.3" y1="505.6" x2="781.3" y2="527.8" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="509.9" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="785.1" y1="481.5" x2="785.1" y2="534.7" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="485.3" width="2.35" height="34.9" fill="var(--up)"/>
<line x1="788.9" y1="460.0" x2="788.9" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="462.1" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="792.6" y1="454.8" x2="792.6" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="461.2" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="796.4" y1="427.4" x2="796.4" y2="444.2" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="428.1" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="800.2" y1="428.8" x2="800.2" y2="465.6" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="439.5" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="804.0" y1="435.7" x2="804.0" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="445.3" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="807.8" y1="421.0" x2="807.8" y2="453.7" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="421.1" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="811.6" y1="407.0" x2="811.6" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="416.7" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="815.4" y1="420.2" x2="815.4" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="427.4" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="819.1" y1="400.1" x2="819.1" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="406.3" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="822.9" y1="378.1" x2="822.9" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="378.1" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="826.7" y1="368.3" x2="826.7" y2="394.6" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="382.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="830.5" y1="370.6" x2="830.5" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="381.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="834.3" y1="365.6" x2="834.3" y2="387.2" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="373.7" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="838.1" y1="369.2" x2="838.1" y2="417.0" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="371.3" width="2.35" height="37.1" fill="var(--down)"/>
<line x1="841.9" y1="380.3" x2="841.9" y2="404.6" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="389.4" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="845.6" y1="348.6" x2="845.6" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="364.3" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="849.4" y1="334.9" x2="849.4" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="336.6" width="2.35" height="27.5" fill="var(--up)"/>
<line x1="853.2" y1="328.5" x2="853.2" y2="345.0" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="335.0" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="857.0" y1="319.9" x2="857.0" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="325.9" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="860.8" y1="314.4" x2="860.8" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="323.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="864.6" y1="296.0" x2="864.6" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="304.7" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="868.4" y1="289.9" x2="868.4" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="305.7" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="872.2" y1="286.8" x2="872.2" y2="317.7" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="294.6" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="875.9" y1="285.1" x2="875.9" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="289.8" width="2.35" height="34.8" fill="var(--down)"/>
<line x1="879.7" y1="270.5" x2="879.7" y2="316.1" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="303.4" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="883.5" y1="276.0" x2="883.5" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="280.9" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="887.3" y1="271.2" x2="887.3" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="275.8" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="891.1" y1="292.8" x2="891.1" y2="329.9" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="292.8" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="894.9" y1="293.9" x2="894.9" y2="342.8" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="303.6" width="2.35" height="23.4" fill="var(--down)"/>
<line x1="898.7" y1="321.1" x2="898.7" y2="358.1" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="329.3" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="902.4" y1="284.8" x2="902.4" y2="332.8" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="285.7" width="2.35" height="46.9" fill="var(--up)"/>
<line x1="906.2" y1="271.1" x2="906.2" y2="298.7" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="277.9" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="910.0" y1="250.5" x2="910.0" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="266.9" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="913.8" y1="261.0" x2="913.8" y2="290.3" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="262.9" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="917.6" y1="259.0" x2="917.6" y2="275.8" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="271.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="921.4" y1="273.5" x2="921.4" y2="292.9" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="276.7" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="925.2" y1="235.9" x2="925.2" y2="279.7" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="240.2" width="2.35" height="39.5" fill="var(--up)"/>
<line x1="928.9" y1="215.1" x2="928.9" y2="246.5" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="220.5" width="2.35" height="23.4" fill="var(--up)"/>
<line x1="932.7" y1="199.4" x2="932.7" y2="237.2" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="223.6" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="936.5" y1="217.5" x2="936.5" y2="249.2" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="222.5" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="940.3" y1="221.0" x2="940.3" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="223.2" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="944.1" y1="210.0" x2="944.1" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="224.3" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="947.9" y1="217.2" x2="947.9" y2="244.9" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="225.6" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="951.7" y1="219.8" x2="951.7" y2="248.7" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="228.9" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="955.5" y1="227.5" x2="955.5" y2="279.1" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="245.8" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="959.2" y1="252.3" x2="959.2" y2="299.3" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="284.7" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="963.0" y1="273.1" x2="963.0" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="286.0" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="966.8" y1="268.2" x2="966.8" y2="306.6" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="298.6" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="970.6" y1="270.9" x2="970.6" y2="320.8" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="274.8" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="974.4" y1="232.0" x2="974.4" y2="280.1" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="237.8" width="2.35" height="37.8" fill="var(--up)"/>
<line x1="978.2" y1="178.0" x2="978.2" y2="240.9" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="184.0" width="2.35" height="55.6" fill="var(--up)"/>
<line x1="982.0" y1="168.9" x2="982.0" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="180.3" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="985.7" y1="169.7" x2="985.7" y2="203.0" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="170.8" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="989.5" y1="142.9" x2="989.5" y2="182.0" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="153.0" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="993.3" y1="143.1" x2="993.3" y2="178.6" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="151.9" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="997.1" y1="146.6" x2="997.1" y2="203.9" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="150.1" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="1000.9" y1="123.1" x2="1000.9" y2="141.6" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="131.6" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="1004.7" y1="122.6" x2="1004.7" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="139.1" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="1008.5" y1="113.2" x2="1008.5" y2="177.2" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="122.6" width="2.35" height="29.9" fill="var(--up)"/>
<line x1="1012.2" y1="103.3" x2="1012.2" y2="134.7" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="108.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1016.0" y1="89.6" x2="1016.0" y2="119.9" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="98.3" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="1019.8" y1="84.8" x2="1019.8" y2="113.0" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="101.6" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="1023.6" y1="93.0" x2="1023.6" y2="128.8" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="103.1" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="1027.4" y1="103.3" x2="1027.4" y2="126.2" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="111.3" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="1031.2" y1="106.2" x2="1031.2" y2="129.8" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="113.7" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="1035.0" y1="112.1" x2="1035.0" y2="137.8" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="122.3" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="1038.7" y1="84.0" x2="1038.7" y2="125.8" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="89.3" width="2.35" height="36.5" fill="var(--up)"/>
<line x1="1042.5" y1="76.3" x2="1042.5" y2="97.1" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="76.8" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="1046.3" y1="79.3" x2="1046.3" y2="105.9" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="79.8" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="1050.1" y1="94.5" x2="1050.1" y2="101.9" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="95.4" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="60" y1="413.6" x2="1052" y2="413.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="407.6" font-size="11.5" fill="var(--support)" font-weight="600">2,152.47 S1</text>
<text x="1058" y="419.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="472.2" x2="1052" y2="472.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="466.2" font-size="11.5" fill="var(--support)" font-weight="600">1,993.25 S2</text>
<text x="1058" y="478.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="503.5" x2="1052" y2="503.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="497.5" font-size="11.5" fill="var(--support)" font-weight="600">1,908.08 S3</text>
<text x="1058" y="509.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="95.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="87.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 3,017.87 (2026-08-21)</text>
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

- **상승**: 미국 국내 경기가 확장될 것이라는 기대, 위험을 더 감수하려는 심리 확대 신호로 흔히 해석한다 — 특히 금리 인하 기대가 커지는 국면에서 대형주보다 더 민감하게 반응하는 경향이 있다.
- **하락**: 국내 경기 둔화 우려, 또는 자금을 조달하는 부담(중소형주는 대형주보다 돈을 빌리는 데 더 많이 의존하는 경우가 많다) 신호로 흔히 해석한다.
- **왜 경기에 더 민감한가**: 중소형주는 대체로 미국 내수 비중이 크고 해외 매출 비중은 낮다. 또 대형주만큼 회사채 시장에서 쉽게 돈을 빌리지 못해서, 금리에 따라 이자율이 바뀌는 은행 대출에 더 많이 의존하는 편이다. 그래서 금리나 대출 여건이 바뀌면 이익과 자금 조달 비용에 더 빨리, 더 크게 반영된다.
- 지수의 절대적인 수준보다 S&P 500·나스닥종합지수 대비 상대적으로 강한지 약한지가 더 자주 인용된다 — 대형주 지수는 오르는데 이 지수만 약하면, 시장 상승세가 소수 대형주에만 쏠려 있다는 신호로 읽히곤 한다.

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
