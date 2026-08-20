# 미국 10년물 국채금리 (US 10Y Treasury Yield)

!!! note ""
    최근 5년 미 국채 10년물 수익률(`^TNX`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 특정 회사 문서가 아니라 **여러 회사 문서에서 공통으로 인용하는 거시 참고 차트**다 — DCF 무위험이자율의 근거를 인용할 때, 혹은 금리 국면이 밸류에이션 배수에 미치는 영향을 Bear Case에서 다룰 때 이 문서를 인용한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="tnx-chart">
<style>
.tnx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .tnx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .tnx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tnx-chart svg { width:100%; height:auto; display:block; }
.tnx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tnx-chart .title { fill: var(--ink); font-weight:600; }
.tnx-chart .grid { stroke: var(--grid); stroke-width:1; }
.tnx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 10년물 금리(^TNX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 10년물 금리 (^TNX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-17 · 마지막 종가 4.65% (2026-08-17) · 단위 %</text>
<line x1="60" y1="499.3" x2="1052" y2="499.3" class="grid"/>
<text x="52" y="503.3" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="358.6" x2="1052" y2="358.6" class="grid"/>
<text x="52" y="362.6" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="217.9" x2="1052" y2="217.9" class="grid"/>
<text x="52" y="221.9" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="77.1" x2="1052" y2="77.1" class="grid"/>
<text x="52" y="81.1" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.6" y1="626.0" x2="137.6" y2="631.0" class="axis"/>
<text x="137.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="334.5" y1="626.0" x2="334.5" y2="631.0" class="axis"/>
<text x="334.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="531.4" y1="626.0" x2="531.4" y2="631.0" class="axis"/>
<text x="531.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="732.1" y1="626.0" x2="732.1" y2="631.0" class="axis"/>
<text x="732.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.9" y1="626.0" x2="928.9" y2="631.0" class="axis"/>
<text x="928.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="602.5" x2="61.9" y2="608.0" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="603.5" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="65.7" y1="587.3" x2="65.7" y2="604.6" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="596.2" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="69.5" y1="592.8" x2="69.5" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="594.8" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="73.3" y1="585.9" x2="73.3" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="588.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="77.0" y1="585.7" x2="77.0" y2="603.5" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="588.0" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="80.8" y1="574.5" x2="80.8" y2="598.3" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="575.3" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="84.6" y1="560.3" x2="84.6" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="570.3" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="88.4" y1="553.2" x2="88.4" y2="574.9" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="554.9" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="92.2" y1="553.5" x2="92.2" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="553.7" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="96.0" y1="542.8" x2="96.0" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="547.9" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="99.8" y1="545.4" x2="99.8" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="548.0" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="103.5" y1="554.9" x2="103.5" y2="576.7" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="557.5" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="107.3" y1="556.8" x2="107.3" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="558.2" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="111.1" y1="549.2" x2="111.1" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="562.2" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="114.9" y1="542.5" x2="114.9" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="559.1" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="118.7" y1="560.6" x2="118.7" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="563.1" width="2.35" height="28.7" fill="var(--down)"/>
<line x1="122.5" y1="564.5" x2="122.5" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="571.3" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="126.3" y1="572.0" x2="126.3" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="574.2" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="130.0" y1="569.6" x2="130.0" y2="587.3" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="570.7" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="133.8" y1="561.5" x2="133.8" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="568.0" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="137.6" y1="527.3" x2="137.6" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="531.6" width="2.35" height="33.4" fill="var(--up)"/>
<line x1="141.4" y1="526.4" x2="141.4" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="531.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="145.2" y1="517.1" x2="145.2" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="523.7" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="149.0" y1="519.5" x2="149.0" y2="540.6" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="530.0" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="152.8" y1="508.3" x2="152.8" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="509.2" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="156.5" y1="490.5" x2="156.5" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="505.7" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="160.3" y1="490.2" x2="160.3" y2="510.9" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="504.5" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="164.1" y1="497.8" x2="164.1" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="501.3" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="167.9" y1="510.6" x2="167.9" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="511.0" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="171.7" y1="496.4" x2="171.7" y2="538.9" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="498.8" width="2.35" height="32.5" fill="var(--up)"/>
<line x1="175.5" y1="464.7" x2="175.5" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="478.5" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="179.3" y1="428.5" x2="179.3" y2="470.2" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="430.1" width="2.35" height="40.1" fill="var(--up)"/>
<line x1="183.1" y1="429.5" x2="183.1" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="434.0" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="186.8" y1="396.9" x2="186.8" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="399.0" width="2.35" height="43.5" fill="var(--up)"/>
<line x1="190.6" y1="381.8" x2="190.6" y2="408.4" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="382.8" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="194.4" y1="365.1" x2="194.4" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="371.8" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="198.2" y1="367.9" x2="198.2" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="374.5" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="202.0" y1="340.2" x2="202.0" y2="371.7" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="341.3" width="2.35" height="28.3" fill="var(--up)"/>
<line x1="205.8" y1="335.1" x2="205.8" y2="384.3" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="335.7" width="2.35" height="32.1" fill="var(--down)"/>
<line x1="209.6" y1="356.6" x2="209.6" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="368.6" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="213.3" y1="377.2" x2="213.3" y2="399.7" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="382.2" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="217.1" y1="360.6" x2="217.1" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="364.6" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="220.9" y1="333.5" x2="220.9" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="336.6" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="224.7" y1="290.6" x2="224.7" y2="330.9" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="318.9" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="228.5" y1="314.0" x2="228.5" y2="357.9" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="318.8" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="232.3" y1="323.0" x2="232.3" y2="388.0" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="332.8" width="2.35" height="41.4" fill="var(--down)"/>
<line x1="236.1" y1="344.4" x2="236.1" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="344.4" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="239.8" y1="348.6" x2="239.8" y2="372.8" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="351.7" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="243.6" y1="347.2" x2="243.6" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="364.2" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="247.4" y1="380.4" x2="247.4" y2="412.4" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="384.8" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="251.2" y1="377.0" x2="251.2" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="381.1" width="2.35" height="25.6" fill="var(--up)"/>
<line x1="255.0" y1="372.4" x2="255.0" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="379.8" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="258.8" y1="358.9" x2="258.8" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="360.1" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="262.6" y1="340.6" x2="262.6" y2="363.5" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="353.7" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="266.4" y1="317.1" x2="266.4" y2="349.2" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="331.4" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="270.1" y1="308.9" x2="270.1" y2="329.2" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="313.4" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="273.9" y1="289.6" x2="273.9" y2="321.7" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="295.5" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="277.7" y1="249.8" x2="277.7" y2="293.4" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="260.5" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="281.5" y1="219.0" x2="281.5" y2="262.0" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="245.4" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="285.3" y1="230.5" x2="285.3" y2="279.2" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="234.3" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="289.1" y1="206.6" x2="289.1" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="216.4" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="292.9" y1="171.0" x2="292.9" y2="230.5" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="187.9" width="2.35" height="38.6" fill="var(--up)"/>
<line x1="296.6" y1="176.9" x2="296.6" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="190.8" width="2.35" height="25.6" fill="var(--down)"/>
<line x1="300.4" y1="186.5" x2="300.4" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="195.9" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="304.2" y1="187.2" x2="304.2" y2="244.2" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="197.9" width="2.35" height="46.3" fill="var(--down)"/>
<line x1="308.0" y1="231.8" x2="308.0" y2="261.2" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="234.2" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="311.8" y1="240.9" x2="311.8" y2="262.7" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="244.0" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="315.6" y1="246.3" x2="315.6" y2="287.7" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="262.5" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="319.4" y1="272.5" x2="319.4" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="278.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="323.1" y1="269.9" x2="323.1" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="282.2" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="326.9" y1="252.6" x2="326.9" y2="280.9" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="252.9" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="330.7" y1="231.2" x2="330.7" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="234.9" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="334.5" y1="244.6" x2="334.5" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="251.9" width="2.35" height="26.6" fill="var(--down)"/>
<line x1="338.3" y1="268.7" x2="338.3" y2="298.1" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="275.7" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="342.1" y1="277.1" x2="342.1" y2="306.1" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="277.7" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="345.9" y1="280.3" x2="345.9" y2="299.2" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="285.7" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="349.6" y1="277.8" x2="349.6" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="280.8" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="353.4" y1="253.5" x2="353.4" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="253.9" width="2.35" height="20.4" fill="var(--up)"/>
<line x1="357.2" y1="231.9" x2="357.2" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="242.1" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="361.0" y1="220.9" x2="361.0" y2="237.1" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="225.0" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="364.8" y1="205.0" x2="364.8" y2="232.3" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="222.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="368.6" y1="215.5" x2="368.6" y2="263.7" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="231.2" width="2.35" height="29.6" fill="var(--down)"/>
<line x1="372.4" y1="262.2" x2="372.4" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="287.5" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="376.2" y1="268.0" x2="376.2" y2="317.1" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="303.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="379.9" y1="272.7" x2="379.9" y2="292.7" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="289.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="383.7" y1="284.8" x2="383.7" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="285.8" width="2.35" height="32.2" fill="var(--down)"/>
<line x1="387.5" y1="283.2" x2="387.5" y2="310.5" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="285.1" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="391.3" y1="268.7" x2="391.3" y2="287.9" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="278.4" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="395.1" y1="281.9" x2="395.1" y2="305.8" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="281.9" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="398.9" y1="277.5" x2="398.9" y2="316.9" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="288.1" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="402.7" y1="283.7" x2="402.7" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="289.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="406.4" y1="257.1" x2="406.4" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="261.2" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="410.2" y1="237.7" x2="410.2" y2="265.0" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="244.6" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="414.0" y1="252.5" x2="414.0" y2="278.4" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="258.4" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="417.8" y1="243.0" x2="417.8" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="252.6" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="421.6" y1="238.8" x2="421.6" y2="262.6" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="250.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="425.4" y1="244.6" x2="425.4" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="254.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="429.2" y1="235.9" x2="429.2" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="243.3" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="432.9" y1="204.6" x2="432.9" y2="249.1" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="210.8" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="436.7" y1="204.9" x2="436.7" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="210.5" width="2.35" height="32.8" fill="var(--down)"/>
<line x1="440.5" y1="235.6" x2="440.5" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="240.8" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="444.3" y1="214.8" x2="444.3" y2="246.3" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="222.2" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="448.1" y1="188.9" x2="448.1" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="209.4" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="451.9" y1="194.2" x2="451.9" y2="223.9" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="194.2" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="455.7" y1="171.7" x2="455.7" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="182.5" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="459.5" y1="166.9" x2="459.5" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="176.5" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="463.2" y1="183.7" x2="463.2" y2="209.4" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="185.2" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="467.0" y1="174.5" x2="467.0" y2="188.0" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="181.5" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="470.8" y1="169.4" x2="470.8" y2="186.5" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="172.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="474.6" y1="148.9" x2="474.6" y2="174.1" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="156.2" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="478.4" y1="121.0" x2="478.4" y2="149.9" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="137.2" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="482.2" y1="93.0" x2="482.2" y2="129.6" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="107.5" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="486.0" y1="105.7" x2="486.0" y2="143.0" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="105.7" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="489.7" y1="77.7" x2="489.7" y2="124.1" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="87.8" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="493.5" y1="77.5" x2="493.5" y2="101.5" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="77.5" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="497.3" y1="88.1" x2="497.3" y2="149.7" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="91.7" width="2.35" height="47.6" fill="var(--down)"/>
<line x1="501.1" y1="123.8" x2="501.1" y2="147.1" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="129.5" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="504.9" y1="119.9" x2="504.9" y2="161.0" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="127.5" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="508.7" y1="148.6" x2="508.7" y2="166.5" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="151.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="512.5" y1="153.0" x2="512.5" y2="188.2" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="153.5" width="2.35" height="32.5" fill="var(--down)"/>
<line x1="516.2" y1="175.8" x2="516.2" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="183.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="520.0" y1="176.6" x2="520.0" y2="234.0" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="179.3" width="2.35" height="48.7" fill="var(--down)"/>
<line x1="523.8" y1="221.9" x2="523.8" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="229.5" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="527.6" y1="230.8" x2="527.6" y2="248.1" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="230.8" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="531.4" y1="203.9" x2="531.4" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="211.9" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="535.2" y1="208.3" x2="535.2" y2="229.7" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="209.5" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="539.0" y1="190.0" x2="539.0" y2="219.3" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="197.3" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="542.7" y1="191.4" x2="542.7" y2="207.3" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="195.3" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="546.5" y1="200.7" x2="546.5" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="202.7" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="550.3" y1="190.7" x2="550.3" y2="208.7" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="191.5" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="554.1" y1="171.7" x2="554.1" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="176.3" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="557.9" y1="168.0" x2="557.9" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="178.0" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="561.7" y1="172.7" x2="561.7" y2="192.8" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="183.5" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="565.5" y1="184.8" x2="565.5" y2="212.5" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="187.0" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="569.3" y1="172.8" x2="569.3" y2="207.3" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="175.1" width="2.35" height="31.9" fill="var(--up)"/>
<line x1="573.0" y1="168.9" x2="573.0" y2="189.7" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="173.7" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="576.8" y1="179.4" x2="576.8" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="185.2" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="580.6" y1="157.5" x2="580.6" y2="184.9" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="164.7" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="584.4" y1="134.7" x2="584.4" y2="169.4" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="147.6" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="588.2" y1="119.9" x2="588.2" y2="136.9" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="131.3" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="592.0" y1="114.1" x2="592.0" y2="137.9" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="123.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="595.8" y1="121.3" x2="595.8" y2="154.1" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="129.7" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="599.5" y1="145.2" x2="599.5" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="146.9" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="603.3" y1="143.0" x2="603.3" y2="173.0" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="149.3" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="607.1" y1="147.2" x2="607.1" y2="161.8" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="152.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="610.9" y1="128.1" x2="610.9" y2="154.7" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="145.5" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="614.7" y1="151.3" x2="614.7" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="151.3" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="618.5" y1="150.4" x2="618.5" y2="191.4" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="154.1" width="2.35" height="33.8" fill="var(--down)"/>
<line x1="622.3" y1="176.3" x2="622.3" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="180.6" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="626.0" y1="167.3" x2="626.0" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="169.6" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="629.8" y1="148.5" x2="629.8" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="158.2" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="633.6" y1="171.5" x2="633.6" y2="194.2" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="174.8" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="637.4" y1="182.8" x2="637.4" y2="197.6" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="184.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="641.2" y1="176.8" x2="641.2" y2="190.8" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="186.2" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="645.0" y1="191.7" x2="645.0" y2="247.1" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="194.9" width="2.35" height="52.2" fill="var(--down)"/>
<line x1="648.8" y1="214.8" x2="648.8" y2="264.4" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="226.0" width="2.35" height="34.5" fill="var(--up)"/>
<line x1="652.5" y1="222.5" x2="652.5" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="226.3" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="656.3" y1="231.9" x2="656.3" y2="251.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="237.6" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="660.1" y1="229.8" x2="660.1" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="230.4" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="663.9" y1="228.7" x2="663.9" y2="267.4" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="229.8" width="2.35" height="28.9" fill="var(--down)"/>
<line x1="667.7" y1="253.3" x2="667.7" y2="272.2" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="253.3" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="671.5" y1="250.5" x2="671.5" y2="273.7" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="256.1" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="675.3" y1="243.0" x2="675.3" y2="256.1" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="251.9" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="679.1" y1="220.5" x2="679.1" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="220.5" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="682.8" y1="201.0" x2="682.8" y2="217.3" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="207.6" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="686.6" y1="202.4" x2="686.6" y2="218.6" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="204.1" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="690.4" y1="181.5" x2="690.4" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="185.2" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="694.2" y1="166.5" x2="694.2" y2="190.0" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="167.0" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="698.0" y1="150.7" x2="698.0" y2="180.8" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="174.8" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="701.8" y1="146.8" x2="701.8" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="157.6" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="705.6" y1="148.7" x2="705.6" y2="170.4" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="150.2" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="709.3" y1="171.1" x2="709.3" y2="193.6" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="173.1" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="713.1" y1="178.3" x2="713.1" y2="200.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="188.7" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="716.9" y1="161.1" x2="716.9" y2="194.8" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="161.7" width="2.35" height="30.5" fill="var(--up)"/>
<line x1="720.7" y1="134.3" x2="720.7" y2="167.0" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="144.1" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="724.5" y1="127.6" x2="724.5" y2="142.7" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="130.7" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="728.3" y1="133.4" x2="728.3" y2="145.1" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="134.0" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="732.1" y1="106.7" x2="732.1" y2="136.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="108.6" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="735.8" y1="104.0" x2="735.8" y2="137.9" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="109.8" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="739.6" y1="124.4" x2="739.6" y2="140.2" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="129.7" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="743.4" y1="134.7" x2="743.4" y2="149.2" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="137.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="747.2" y1="133.7" x2="747.2" y2="161.8" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="146.6" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="751.0" y1="125.0" x2="751.0" y2="154.9" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="148.7" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="754.8" y1="136.8" x2="754.8" y2="160.7" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="144.8" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="758.6" y1="154.4" x2="758.6" y2="187.7" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="156.3" width="2.35" height="29.0" fill="var(--down)"/>
<line x1="762.4" y1="169.4" x2="762.4" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="173.2" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="766.1" y1="168.2" x2="766.1" y2="191.4" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="174.5" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="769.9" y1="170.1" x2="769.9" y2="193.4" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="178.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="773.7" y1="163.4" x2="773.7" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="175.3" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="777.5" y1="181.4" x2="777.5" y2="233.9" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="189.3" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="781.3" y1="134.5" x2="781.3" y2="221.8" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="148.5" width="2.35" height="72.6" fill="var(--up)"/>
<line x1="785.1" y1="153.4" x2="785.1" y2="179.1" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="156.2" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="788.9" y1="160.6" x2="788.9" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="162.0" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="792.6" y1="171.1" x2="792.6" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="172.5" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="796.4" y1="161.8" x2="796.4" y2="181.3" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="165.1" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="800.2" y1="141.6" x2="800.2" y2="163.2" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="153.0" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="804.0" y1="129.3" x2="804.0" y2="152.4" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="140.6" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="807.8" y1="147.3" x2="807.8" y2="162.4" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="151.8" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="811.6" y1="145.8" x2="811.6" y2="173.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="146.1" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="815.4" y1="144.9" x2="815.4" y2="170.0" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="147.2" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="819.1" y1="154.0" x2="819.1" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="155.6" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="822.9" y1="165.6" x2="822.9" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="167.0" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="826.7" y1="166.6" x2="826.7" y2="189.0" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="168.9" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="830.5" y1="156.6" x2="830.5" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="158.3" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="834.3" y1="148.5" x2="834.3" y2="162.1" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="156.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="838.1" y1="155.6" x2="838.1" y2="171.7" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="163.5" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="841.9" y1="158.7" x2="841.9" y2="187.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="161.6" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="845.6" y1="177.2" x2="845.6" y2="191.4" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="177.7" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="849.4" y1="171.1" x2="849.4" y2="189.1" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="171.7" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="853.2" y1="168.5" x2="853.2" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="175.9" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="857.0" y1="176.3" x2="857.0" y2="189.3" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="178.3" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="860.8" y1="174.8" x2="860.8" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="175.9" width="2.35" height="29.8" fill="var(--down)"/>
<line x1="864.6" y1="205.0" x2="864.6" y2="218.4" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="207.7" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="868.4" y1="197.7" x2="868.4" y2="219.0" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="198.3" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="872.2" y1="189.6" x2="872.2" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="191.5" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="875.9" y1="194.2" x2="875.9" y2="206.5" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="196.7" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="879.7" y1="193.8" x2="879.7" y2="211.7" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="195.1" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="883.5" y1="210.7" x2="883.5" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="210.7" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="887.3" y1="215.6" x2="887.3" y2="225.3" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="217.1" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="891.1" y1="201.5" x2="891.1" y2="222.1" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="203.6" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="894.9" y1="195.2" x2="894.9" y2="208.6" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="202.9" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="898.7" y1="197.0" x2="898.7" y2="210.0" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="197.0" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="902.4" y1="195.1" x2="902.4" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="198.3" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="906.2" y1="209.3" x2="906.2" y2="219.5" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="210.0" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="910.0" y1="197.4" x2="910.0" y2="210.8" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="198.3" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="913.8" y1="189.1" x2="913.8" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="190.5" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="917.6" y1="190.3" x2="917.6" y2="202.7" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="193.9" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="921.4" y1="189.4" x2="921.4" y2="202.4" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="194.3" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="925.2" y1="190.1" x2="925.2" y2="202.7" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="191.5" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="928.9" y1="188.2" x2="928.9" y2="200.4" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="192.1" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="932.7" y1="185.1" x2="932.7" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="185.3" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="936.5" y1="174.1" x2="936.5" y2="185.1" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="178.6" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="940.3" y1="179.7" x2="940.3" y2="189.3" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="183.9" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="944.1" y1="175.6" x2="944.1" y2="190.5" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="184.6" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="947.9" y1="184.4" x2="947.9" y2="211.4" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="184.4" width="2.35" height="25.6" fill="var(--down)"/>
<line x1="951.7" y1="202.9" x2="951.7" y2="214.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="205.7" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="955.5" y1="207.3" x2="955.5" y2="224.0" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="207.3" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="959.2" y1="191.5" x2="959.2" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="199.1" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="963.0" y1="177.0" x2="963.0" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="177.7" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="966.8" y1="162.4" x2="966.8" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="162.8" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="970.6" y1="149.7" x2="970.6" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="155.9" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="974.4" y1="164.4" x2="974.4" y2="177.5" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="165.2" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="978.2" y1="164.4" x2="978.2" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="167.2" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="982.0" y1="168.5" x2="982.0" y2="186.0" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="168.7" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="985.7" y1="168.2" x2="985.7" y2="183.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="174.2" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="989.5" y1="157.1" x2="989.5" y2="174.2" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="164.7" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="993.3" y1="152.5" x2="993.3" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="161.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="997.1" y1="133.5" x2="997.1" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="134.1" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="1000.9" y1="121.2" x2="1000.9" y2="143.5" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="133.5" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="1004.7" y1="145.8" x2="1004.7" y2="157.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="149.0" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="1008.5" y1="139.9" x2="1008.5" y2="157.6" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="142.4" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="1012.2" y1="139.0" x2="1012.2" y2="153.5" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="141.9" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="1016.0" y1="150.4" x2="1016.0" y2="158.7" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="153.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1019.8" y1="145.4" x2="1019.8" y2="166.8" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="148.2" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="1023.6" y1="146.8" x2="1023.6" y2="166.2" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="149.6" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="1027.4" y1="133.8" x2="1027.4" y2="153.5" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="137.8" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="1031.2" y1="130.9" x2="1031.2" y2="145.9" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="135.5" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="1035.0" y1="117.4" x2="1035.0" y2="139.0" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="122.3" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="1038.7" y1="112.7" x2="1038.7" y2="135.1" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="113.0" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="1042.5" y1="119.1" x2="1042.5" y2="133.0" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="123.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="1046.3" y1="118.9" x2="1046.3" y2="131.6" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="119.9" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="1050.1" y1="112.9" x2="1050.1" y2="128.2" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="120.2" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="60" y1="113.1" x2="1052" y2="113.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="116.6" font-size="11.5" fill="var(--resistance)" font-weight="600">4.74% R1</text>
<text x="1058" y="128.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="194.6" x2="1052" y2="194.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="188.6" font-size="11.5" fill="var(--support)" font-weight="600">4.17% S1</text>
<text x="1058" y="200.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="220.6" x2="1052" y2="220.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.6" font-size="11.5" fill="var(--support)" font-weight="600">3.98% S2</text>
<text x="1058" y="226.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="241.9" x2="1052" y2="241.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="235.9" font-size="11.5" fill="var(--support)" font-weight="600">3.83% S3</text>
<text x="1058" y="247.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="125.9" r="3" fill="var(--ink)"/>
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

- **상승**: 성장·인플레이션 기대 확대, 재정적자 우려, 연준 긴축 기대 신호로 흔히 해석된다 — DCF 무위험이자율 상승은 할인율 상승(밸류에이션 하방 압력)으로 직결된다.
- **하락**: 성장·인플레이션 기대 둔화, 안전자산 수요 확대, 연준 완화 기대 신호로 흔히 해석된다.
- **왜 이런 신호로 읽히나**: 10년물은 발행량·거래량이 가장 많아 유동성이 좋고, 주택담보대출 등 실물경제 금리의 기준물로 널리 쓰여 DCF 무위험이자율의 표준으로 자리잡았다. 재정적자 우려가 반영되는 경로도 직접적이다 — 국채 발행 증가 기대는 만기가 길어 공급 부담을 더 크게 지는 채권일수록(기간 프리미엄) 가격에 더 크게 반영된다.
- 국채금리는 연준 정책·인플레이션 기대·재정정책 등 여러 요인이 겹쳐 움직인다 — 이 차트만으로 방향을 예단하지 않는다.

---

## 관련 문서

- [13주 단기금리](./short_rate.md) — 장단기 스프레드(수익률곡선)의 짝 지표
- [미국 5년물 국채금리](./treasury_5y.md)
- [미국 30년물 국채금리](./treasury_30y.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — 금리가 할인율·실적에 닿는 두 경로, 수익률곡선
- [밸류에이션 개념 정리](../../concepts/valuation.md) — 무위험이자율이 Ke·WACC로 들어가는 지점
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — 10 Year Treasury Yield (^TNX)](https://finance.yahoo.com/quote/%5ETNX/)
- [미 재무부 금리 (원출처)](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
