# 미국 10년물 국채금리

!!! note ""
    최근 5년간 미국 10년물 국채 수익률(`^TNX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. DCF 밸류에이션에서 "위험이 거의 없는 이자율(무위험이자율)"의 대표적인 기준으로 쓰이며, 금리가 어떤 국면인지에 따라 성장주의 밸류에이션 배수가 크게 달라진다.

---

## 1. 차트 — 최근 5년 주봉

<div class="tnx-chart">
<style>
.tnx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .tnx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-24 · 마지막 종가 4.67% (2026-08-24) · 단위 %</text>
<line x1="60" y1="499.3" x2="1052" y2="499.3" class="grid"/>
<text x="52" y="503.3" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="358.6" x2="1052" y2="358.6" class="grid"/>
<text x="52" y="362.6" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="217.9" x2="1052" y2="217.9" class="grid"/>
<text x="52" y="221.9" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="77.1" x2="1052" y2="77.1" class="grid"/>
<text x="52" y="81.1" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.3" y1="56.0" x2="130.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.3" y1="626.0" x2="130.3" y2="631.0" class="axis"/>
<text x="130.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="328.0" y1="56.0" x2="328.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="328.0" y1="626.0" x2="328.0" y2="631.0" class="axis"/>
<text x="328.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="525.6" y1="56.0" x2="525.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="525.6" y1="626.0" x2="525.6" y2="631.0" class="axis"/>
<text x="525.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="727.0" y1="56.0" x2="727.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="727.0" y1="626.0" x2="727.0" y2="631.0" class="axis"/>
<text x="727.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="924.7" y1="56.0" x2="924.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="924.7" y1="626.0" x2="924.7" y2="631.0" class="axis"/>
<text x="924.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="592.8" x2="61.9" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="594.8" width="2.36" height="1.7" fill="var(--up)"/>
<line x1="65.7" y1="585.9" x2="65.7" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="64.52" y="588.6" width="2.36" height="3.5" fill="var(--down)"/>
<line x1="69.5" y1="585.7" x2="69.5" y2="603.5" stroke="var(--up)" class="wick"/>
<rect x="68.32" y="588.0" width="2.36" height="4.5" fill="var(--up)"/>
<line x1="73.3" y1="574.5" x2="73.3" y2="598.3" stroke="var(--up)" class="wick"/>
<rect x="72.12" y="575.3" width="2.36" height="21.3" fill="var(--up)"/>
<line x1="77.1" y1="560.3" x2="77.1" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="75.93" y="570.3" width="2.36" height="2.4" fill="var(--down)"/>
<line x1="80.9" y1="553.2" x2="80.9" y2="574.9" stroke="var(--up)" class="wick"/>
<rect x="79.73" y="554.9" width="2.36" height="16.7" fill="var(--up)"/>
<line x1="84.7" y1="553.5" x2="84.7" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="83.53" y="553.7" width="2.36" height="5.3" fill="var(--down)"/>
<line x1="88.5" y1="542.8" x2="88.5" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="87.33" y="547.9" width="2.36" height="7.9" fill="var(--up)"/>
<line x1="92.3" y1="545.4" x2="92.3" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="91.13" y="548.0" width="2.36" height="13.7" fill="var(--down)"/>
<line x1="96.1" y1="554.9" x2="96.1" y2="576.7" stroke="var(--down)" class="wick"/>
<rect x="94.93" y="557.5" width="2.36" height="18.9" fill="var(--down)"/>
<line x1="99.9" y1="556.8" x2="99.9" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="98.73" y="558.2" width="2.36" height="13.9" fill="var(--up)"/>
<line x1="103.7" y1="549.2" x2="103.7" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="102.53" y="562.2" width="2.36" height="2.4" fill="var(--down)"/>
<line x1="107.5" y1="542.5" x2="107.5" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="106.33" y="559.1" width="2.36" height="13.1" fill="var(--down)"/>
<line x1="111.3" y1="560.6" x2="111.3" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="110.13" y="563.1" width="2.36" height="28.7" fill="var(--down)"/>
<line x1="115.1" y1="564.5" x2="115.1" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="113.93" y="571.3" width="2.36" height="13.9" fill="var(--up)"/>
<line x1="118.9" y1="572.0" x2="118.9" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="117.73" y="574.2" width="2.36" height="9.3" fill="var(--down)"/>
<line x1="122.7" y1="569.6" x2="122.7" y2="587.3" stroke="var(--up)" class="wick"/>
<rect x="121.53" y="570.7" width="2.36" height="14.9" fill="var(--up)"/>
<line x1="126.5" y1="561.5" x2="126.5" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="125.34" y="568.0" width="2.36" height="3.2" fill="var(--up)"/>
<line x1="130.3" y1="527.3" x2="130.3" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="129.14" y="531.6" width="2.36" height="33.4" fill="var(--up)"/>
<line x1="134.1" y1="526.4" x2="134.1" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="132.94" y="531.0" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="137.9" y1="517.1" x2="137.9" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="136.74" y="523.7" width="2.36" height="11.3" fill="var(--down)"/>
<line x1="141.7" y1="519.5" x2="141.7" y2="540.6" stroke="var(--up)" class="wick"/>
<rect x="140.54" y="530.0" width="2.36" height="7.0" fill="var(--up)"/>
<line x1="145.5" y1="508.3" x2="145.5" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="144.34" y="509.2" width="2.36" height="17.9" fill="var(--up)"/>
<line x1="149.3" y1="490.5" x2="149.3" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="148.14" y="505.7" width="2.36" height="4.8" fill="var(--up)"/>
<line x1="153.1" y1="490.2" x2="153.1" y2="510.9" stroke="var(--down)" class="wick"/>
<rect x="151.94" y="504.5" width="2.36" height="4.4" fill="var(--down)"/>
<line x1="156.9" y1="497.8" x2="156.9" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="155.74" y="501.3" width="2.36" height="5.9" fill="var(--up)"/>
<line x1="160.7" y1="510.6" x2="160.7" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="159.54" y="511.0" width="2.36" height="27.2" fill="var(--down)"/>
<line x1="164.5" y1="496.4" x2="164.5" y2="538.9" stroke="var(--up)" class="wick"/>
<rect x="163.34" y="498.8" width="2.36" height="32.5" fill="var(--up)"/>
<line x1="168.3" y1="464.7" x2="168.3" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="167.14" y="478.5" width="2.36" height="9.9" fill="var(--up)"/>
<line x1="172.1" y1="428.5" x2="172.1" y2="470.2" stroke="var(--up)" class="wick"/>
<rect x="170.94" y="430.1" width="2.36" height="40.1" fill="var(--up)"/>
<line x1="175.9" y1="429.5" x2="175.9" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="174.75" y="434.0" width="2.36" height="12.2" fill="var(--down)"/>
<line x1="179.7" y1="396.9" x2="179.7" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="178.55" y="399.0" width="2.36" height="43.5" fill="var(--up)"/>
<line x1="183.5" y1="381.8" x2="183.5" y2="408.4" stroke="var(--up)" class="wick"/>
<rect x="182.35" y="382.8" width="2.36" height="8.3" fill="var(--up)"/>
<line x1="187.3" y1="365.1" x2="187.3" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="186.15" y="371.8" width="2.36" height="6.2" fill="var(--up)"/>
<line x1="191.1" y1="367.9" x2="191.1" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="189.95" y="374.5" width="2.36" height="7.0" fill="var(--up)"/>
<line x1="194.9" y1="340.2" x2="194.9" y2="371.7" stroke="var(--up)" class="wick"/>
<rect x="193.75" y="341.3" width="2.36" height="28.3" fill="var(--up)"/>
<line x1="198.7" y1="335.1" x2="198.7" y2="384.3" stroke="var(--down)" class="wick"/>
<rect x="197.55" y="335.7" width="2.36" height="32.1" fill="var(--down)"/>
<line x1="202.5" y1="356.6" x2="202.5" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="201.35" y="368.6" width="2.36" height="20.0" fill="var(--down)"/>
<line x1="206.3" y1="377.2" x2="206.3" y2="399.7" stroke="var(--down)" class="wick"/>
<rect x="205.15" y="382.2" width="2.36" height="12.5" fill="var(--down)"/>
<line x1="210.1" y1="360.6" x2="210.1" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="208.95" y="364.6" width="2.36" height="17.9" fill="var(--up)"/>
<line x1="213.9" y1="333.5" x2="213.9" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="212.75" y="336.6" width="2.36" height="26.2" fill="var(--up)"/>
<line x1="217.7" y1="290.6" x2="217.7" y2="330.9" stroke="var(--down)" class="wick"/>
<rect x="216.55" y="318.9" width="2.36" height="6.1" fill="var(--down)"/>
<line x1="221.5" y1="314.0" x2="221.5" y2="357.9" stroke="var(--down)" class="wick"/>
<rect x="220.35" y="318.8" width="2.36" height="22.2" fill="var(--down)"/>
<line x1="225.3" y1="323.0" x2="225.3" y2="388.0" stroke="var(--down)" class="wick"/>
<rect x="224.16" y="332.8" width="2.36" height="41.4" fill="var(--down)"/>
<line x1="229.1" y1="344.4" x2="229.1" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="227.96" y="344.4" width="2.36" height="32.4" fill="var(--up)"/>
<line x1="232.9" y1="348.6" x2="232.9" y2="372.8" stroke="var(--down)" class="wick"/>
<rect x="231.76" y="351.7" width="2.36" height="16.7" fill="var(--down)"/>
<line x1="236.7" y1="347.2" x2="236.7" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="235.56" y="364.2" width="2.36" height="24.9" fill="var(--down)"/>
<line x1="240.5" y1="380.4" x2="240.5" y2="412.4" stroke="var(--down)" class="wick"/>
<rect x="239.36" y="384.8" width="2.36" height="24.2" fill="var(--down)"/>
<line x1="244.3" y1="377.0" x2="244.3" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="243.16" y="381.1" width="2.36" height="25.6" fill="var(--up)"/>
<line x1="248.1" y1="372.4" x2="248.1" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="246.96" y="379.8" width="2.36" height="8.0" fill="var(--up)"/>
<line x1="251.9" y1="358.9" x2="251.9" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="250.76" y="360.1" width="2.36" height="26.0" fill="var(--up)"/>
<line x1="255.7" y1="340.6" x2="255.7" y2="363.5" stroke="var(--up)" class="wick"/>
<rect x="254.56" y="353.7" width="2.36" height="7.6" fill="var(--up)"/>
<line x1="259.5" y1="317.1" x2="259.5" y2="349.2" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="331.4" width="2.36" height="13.2" fill="var(--up)"/>
<line x1="263.3" y1="308.9" x2="263.3" y2="329.2" stroke="var(--up)" class="wick"/>
<rect x="262.16" y="313.4" width="2.36" height="10.0" fill="var(--up)"/>
<line x1="267.1" y1="289.6" x2="267.1" y2="321.7" stroke="var(--up)" class="wick"/>
<rect x="265.96" y="295.5" width="2.36" height="25.3" fill="var(--up)"/>
<line x1="270.9" y1="249.8" x2="270.9" y2="293.4" stroke="var(--up)" class="wick"/>
<rect x="269.76" y="260.5" width="2.36" height="26.3" fill="var(--up)"/>
<line x1="274.7" y1="219.0" x2="274.7" y2="262.0" stroke="var(--up)" class="wick"/>
<rect x="273.57" y="245.4" width="2.36" height="3.0" fill="var(--up)"/>
<line x1="278.5" y1="230.5" x2="278.5" y2="279.2" stroke="var(--up)" class="wick"/>
<rect x="277.37" y="234.3" width="2.36" height="24.1" fill="var(--up)"/>
<line x1="282.3" y1="206.6" x2="282.3" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="281.17" y="216.4" width="2.36" height="17.2" fill="var(--up)"/>
<line x1="286.1" y1="171.0" x2="286.1" y2="230.5" stroke="var(--up)" class="wick"/>
<rect x="284.97" y="187.9" width="2.36" height="38.6" fill="var(--up)"/>
<line x1="289.9" y1="176.9" x2="289.9" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="288.77" y="190.8" width="2.36" height="25.6" fill="var(--down)"/>
<line x1="293.7" y1="186.5" x2="293.7" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="292.57" y="195.9" width="2.36" height="17.6" fill="var(--up)"/>
<line x1="297.5" y1="187.2" x2="297.5" y2="244.2" stroke="var(--down)" class="wick"/>
<rect x="296.37" y="197.9" width="2.36" height="46.3" fill="var(--down)"/>
<line x1="301.3" y1="231.8" x2="301.3" y2="261.2" stroke="var(--down)" class="wick"/>
<rect x="300.17" y="234.2" width="2.36" height="9.3" fill="var(--down)"/>
<line x1="305.1" y1="240.9" x2="305.1" y2="262.7" stroke="var(--down)" class="wick"/>
<rect x="303.97" y="244.0" width="2.36" height="17.3" fill="var(--down)"/>
<line x1="309.0" y1="246.3" x2="309.0" y2="287.7" stroke="var(--down)" class="wick"/>
<rect x="307.77" y="262.5" width="2.36" height="24.9" fill="var(--down)"/>
<line x1="312.8" y1="272.5" x2="312.8" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="311.57" y="278.8" width="2.36" height="5.2" fill="var(--up)"/>
<line x1="316.6" y1="269.9" x2="316.6" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="315.37" y="282.2" width="2.36" height="8.6" fill="var(--down)"/>
<line x1="320.4" y1="252.6" x2="320.4" y2="280.9" stroke="var(--up)" class="wick"/>
<rect x="319.17" y="252.9" width="2.36" height="27.0" fill="var(--up)"/>
<line x1="324.2" y1="231.2" x2="324.2" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="322.98" y="234.9" width="2.36" height="12.9" fill="var(--up)"/>
<line x1="328.0" y1="244.6" x2="328.0" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="326.78" y="251.9" width="2.36" height="26.6" fill="var(--down)"/>
<line x1="331.8" y1="268.7" x2="331.8" y2="298.1" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="275.7" width="2.36" height="11.0" fill="var(--down)"/>
<line x1="335.6" y1="277.1" x2="335.6" y2="306.1" stroke="var(--down)" class="wick"/>
<rect x="334.38" y="277.7" width="2.36" height="12.8" fill="var(--down)"/>
<line x1="339.4" y1="280.3" x2="339.4" y2="299.2" stroke="var(--up)" class="wick"/>
<rect x="338.18" y="285.7" width="2.36" height="2.1" fill="var(--up)"/>
<line x1="343.2" y1="277.8" x2="343.2" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="341.98" y="280.8" width="2.36" height="3.0" fill="var(--down)"/>
<line x1="347.0" y1="253.5" x2="347.0" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="345.78" y="253.9" width="2.36" height="20.4" fill="var(--up)"/>
<line x1="350.8" y1="231.9" x2="350.8" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="349.58" y="242.1" width="2.36" height="11.4" fill="var(--up)"/>
<line x1="354.6" y1="220.9" x2="354.6" y2="237.1" stroke="var(--up)" class="wick"/>
<rect x="353.38" y="225.0" width="2.36" height="7.7" fill="var(--up)"/>
<line x1="358.4" y1="205.0" x2="358.4" y2="232.3" stroke="var(--down)" class="wick"/>
<rect x="357.18" y="222.5" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="362.2" y1="215.5" x2="362.2" y2="263.7" stroke="var(--down)" class="wick"/>
<rect x="360.98" y="231.2" width="2.36" height="29.6" fill="var(--down)"/>
<line x1="366.0" y1="262.2" x2="366.0" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="364.78" y="287.5" width="2.36" height="15.5" fill="var(--down)"/>
<line x1="369.8" y1="268.0" x2="369.8" y2="317.1" stroke="var(--down)" class="wick"/>
<rect x="368.58" y="303.0" width="2.36" height="2.1" fill="var(--down)"/>
<line x1="373.6" y1="272.7" x2="373.6" y2="292.7" stroke="var(--up)" class="wick"/>
<rect x="372.38" y="289.1" width="2.36" height="3.4" fill="var(--up)"/>
<line x1="377.4" y1="284.8" x2="377.4" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="376.19" y="285.8" width="2.36" height="32.2" fill="var(--down)"/>
<line x1="381.2" y1="283.2" x2="381.2" y2="310.5" stroke="var(--up)" class="wick"/>
<rect x="379.99" y="285.1" width="2.36" height="22.0" fill="var(--up)"/>
<line x1="385.0" y1="268.7" x2="385.0" y2="287.9" stroke="var(--up)" class="wick"/>
<rect x="383.79" y="278.4" width="2.36" height="3.0" fill="var(--up)"/>
<line x1="388.8" y1="281.9" x2="388.8" y2="305.8" stroke="var(--down)" class="wick"/>
<rect x="387.59" y="281.9" width="2.36" height="13.1" fill="var(--down)"/>
<line x1="392.6" y1="277.5" x2="392.6" y2="316.9" stroke="var(--down)" class="wick"/>
<rect x="391.39" y="288.1" width="2.36" height="7.7" fill="var(--down)"/>
<line x1="396.4" y1="283.7" x2="396.4" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="395.19" y="289.6" width="2.36" height="3.8" fill="var(--down)"/>
<line x1="400.2" y1="257.1" x2="400.2" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="398.99" y="261.2" width="2.36" height="26.7" fill="var(--up)"/>
<line x1="404.0" y1="237.7" x2="404.0" y2="265.0" stroke="var(--up)" class="wick"/>
<rect x="402.79" y="244.6" width="2.36" height="16.9" fill="var(--up)"/>
<line x1="407.8" y1="252.5" x2="407.8" y2="278.4" stroke="var(--down)" class="wick"/>
<rect x="406.59" y="258.4" width="2.36" height="3.0" fill="var(--down)"/>
<line x1="411.6" y1="243.0" x2="411.6" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="410.39" y="252.6" width="2.36" height="1.1" fill="var(--down)"/>
<line x1="415.4" y1="238.8" x2="415.4" y2="262.6" stroke="var(--up)" class="wick"/>
<rect x="414.19" y="250.4" width="2.36" height="4.9" fill="var(--up)"/>
<line x1="419.2" y1="244.6" x2="419.2" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="417.99" y="254.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="423.0" y1="235.9" x2="423.0" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="421.79" y="243.3" width="2.36" height="16.5" fill="var(--up)"/>
<line x1="426.8" y1="204.6" x2="426.8" y2="249.1" stroke="var(--up)" class="wick"/>
<rect x="425.60" y="210.8" width="2.36" height="26.2" fill="var(--up)"/>
<line x1="430.6" y1="204.9" x2="430.6" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="429.40" y="210.5" width="2.36" height="32.8" fill="var(--down)"/>
<line x1="434.4" y1="235.6" x2="434.4" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="433.20" y="240.8" width="2.36" height="8.2" fill="var(--up)"/>
<line x1="438.2" y1="214.8" x2="438.2" y2="246.3" stroke="var(--up)" class="wick"/>
<rect x="437.00" y="222.2" width="2.36" height="22.9" fill="var(--up)"/>
<line x1="442.0" y1="188.9" x2="442.0" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="440.80" y="209.4" width="2.36" height="13.1" fill="var(--up)"/>
<line x1="445.8" y1="194.2" x2="445.8" y2="223.9" stroke="var(--up)" class="wick"/>
<rect x="444.60" y="194.2" width="2.36" height="7.7" fill="var(--up)"/>
<line x1="449.6" y1="171.7" x2="449.6" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="448.40" y="182.5" width="2.36" height="10.6" fill="var(--up)"/>
<line x1="453.4" y1="166.9" x2="453.4" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="452.20" y="176.5" width="2.36" height="7.7" fill="var(--down)"/>
<line x1="457.2" y1="183.7" x2="457.2" y2="209.4" stroke="var(--down)" class="wick"/>
<rect x="456.00" y="185.2" width="2.36" height="8.3" fill="var(--down)"/>
<line x1="461.0" y1="174.5" x2="461.0" y2="188.0" stroke="var(--up)" class="wick"/>
<rect x="459.80" y="181.5" width="2.36" height="4.2" fill="var(--up)"/>
<line x1="464.8" y1="169.4" x2="464.8" y2="186.5" stroke="var(--up)" class="wick"/>
<rect x="463.60" y="172.5" width="2.36" height="5.3" fill="var(--up)"/>
<line x1="468.6" y1="148.9" x2="468.6" y2="174.1" stroke="var(--up)" class="wick"/>
<rect x="467.40" y="156.2" width="2.36" height="14.2" fill="var(--up)"/>
<line x1="472.4" y1="121.0" x2="472.4" y2="149.9" stroke="var(--up)" class="wick"/>
<rect x="471.20" y="137.2" width="2.36" height="9.6" fill="var(--up)"/>
<line x1="476.2" y1="93.0" x2="476.2" y2="129.6" stroke="var(--up)" class="wick"/>
<rect x="475.01" y="107.5" width="2.36" height="21.5" fill="var(--up)"/>
<line x1="480.0" y1="105.7" x2="480.0" y2="143.0" stroke="var(--down)" class="wick"/>
<rect x="478.81" y="105.7" width="2.36" height="23.6" fill="var(--down)"/>
<line x1="483.8" y1="77.7" x2="483.8" y2="124.1" stroke="var(--up)" class="wick"/>
<rect x="482.61" y="87.8" width="2.36" height="32.8" fill="var(--up)"/>
<line x1="487.6" y1="77.5" x2="487.6" y2="101.5" stroke="var(--down)" class="wick"/>
<rect x="486.41" y="77.5" width="2.36" height="21.4" fill="var(--down)"/>
<line x1="491.4" y1="88.1" x2="491.4" y2="149.7" stroke="var(--down)" class="wick"/>
<rect x="490.21" y="91.7" width="2.36" height="47.6" fill="var(--down)"/>
<line x1="495.2" y1="123.8" x2="495.2" y2="147.1" stroke="var(--up)" class="wick"/>
<rect x="494.01" y="129.5" width="2.36" height="2.5" fill="var(--up)"/>
<line x1="499.0" y1="119.9" x2="499.0" y2="161.0" stroke="var(--down)" class="wick"/>
<rect x="497.81" y="127.5" width="2.36" height="28.3" fill="var(--down)"/>
<line x1="502.8" y1="148.6" x2="502.8" y2="166.5" stroke="var(--down)" class="wick"/>
<rect x="501.61" y="151.3" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="506.6" y1="153.0" x2="506.6" y2="188.2" stroke="var(--down)" class="wick"/>
<rect x="505.41" y="153.5" width="2.36" height="32.5" fill="var(--down)"/>
<line x1="510.4" y1="175.8" x2="510.4" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="509.21" y="183.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="514.2" y1="176.6" x2="514.2" y2="234.0" stroke="var(--down)" class="wick"/>
<rect x="513.01" y="179.3" width="2.36" height="48.7" fill="var(--down)"/>
<line x1="518.0" y1="221.9" x2="518.0" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="516.81" y="229.5" width="2.36" height="2.3" fill="var(--down)"/>
<line x1="521.8" y1="230.8" x2="521.8" y2="248.1" stroke="var(--down)" class="wick"/>
<rect x="520.61" y="230.8" width="2.36" height="5.9" fill="var(--down)"/>
<line x1="525.6" y1="203.9" x2="525.6" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="524.42" y="211.9" width="2.36" height="10.3" fill="var(--up)"/>
<line x1="529.4" y1="208.3" x2="529.4" y2="229.7" stroke="var(--down)" class="wick"/>
<rect x="528.22" y="209.5" width="2.36" height="15.3" fill="var(--down)"/>
<line x1="533.2" y1="190.0" x2="533.2" y2="219.3" stroke="var(--up)" class="wick"/>
<rect x="532.02" y="197.3" width="2.36" height="20.1" fill="var(--up)"/>
<line x1="537.0" y1="191.4" x2="537.0" y2="207.3" stroke="var(--up)" class="wick"/>
<rect x="535.82" y="195.3" width="2.36" height="8.7" fill="var(--up)"/>
<line x1="540.8" y1="200.7" x2="540.8" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="539.62" y="202.7" width="2.36" height="10.6" fill="var(--down)"/>
<line x1="544.6" y1="190.7" x2="544.6" y2="208.7" stroke="var(--up)" class="wick"/>
<rect x="543.42" y="191.5" width="2.36" height="10.6" fill="var(--up)"/>
<line x1="548.4" y1="171.7" x2="548.4" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="547.22" y="176.3" width="2.36" height="20.1" fill="var(--up)"/>
<line x1="552.2" y1="168.0" x2="552.2" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="551.02" y="178.0" width="2.36" height="3.2" fill="var(--down)"/>
<line x1="556.0" y1="172.7" x2="556.0" y2="192.8" stroke="var(--down)" class="wick"/>
<rect x="554.82" y="183.5" width="2.36" height="9.0" fill="var(--down)"/>
<line x1="559.8" y1="184.8" x2="559.8" y2="212.5" stroke="var(--down)" class="wick"/>
<rect x="558.62" y="187.0" width="2.36" height="18.3" fill="var(--down)"/>
<line x1="563.6" y1="172.8" x2="563.6" y2="207.3" stroke="var(--up)" class="wick"/>
<rect x="562.42" y="175.1" width="2.36" height="31.9" fill="var(--up)"/>
<line x1="567.4" y1="168.9" x2="567.4" y2="189.7" stroke="var(--down)" class="wick"/>
<rect x="566.22" y="173.7" width="2.36" height="13.5" fill="var(--down)"/>
<line x1="571.2" y1="179.4" x2="571.2" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="570.02" y="185.2" width="2.36" height="3.7" fill="var(--down)"/>
<line x1="575.0" y1="157.5" x2="575.0" y2="184.9" stroke="var(--up)" class="wick"/>
<rect x="573.83" y="164.7" width="2.36" height="20.3" fill="var(--up)"/>
<line x1="578.8" y1="134.7" x2="578.8" y2="169.4" stroke="var(--up)" class="wick"/>
<rect x="577.63" y="147.6" width="2.36" height="5.8" fill="var(--up)"/>
<line x1="582.6" y1="119.9" x2="582.6" y2="136.9" stroke="var(--up)" class="wick"/>
<rect x="581.43" y="131.3" width="2.36" height="4.2" fill="var(--up)"/>
<line x1="586.4" y1="114.1" x2="586.4" y2="137.9" stroke="var(--up)" class="wick"/>
<rect x="585.23" y="123.7" width="2.36" height="2.4" fill="var(--up)"/>
<line x1="590.2" y1="121.3" x2="590.2" y2="154.1" stroke="var(--down)" class="wick"/>
<rect x="589.03" y="129.7" width="2.36" height="17.7" fill="var(--down)"/>
<line x1="594.0" y1="145.2" x2="594.0" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="592.83" y="146.9" width="2.36" height="2.4" fill="var(--up)"/>
<line x1="597.8" y1="143.0" x2="597.8" y2="173.0" stroke="var(--down)" class="wick"/>
<rect x="596.63" y="149.3" width="2.36" height="9.4" fill="var(--down)"/>
<line x1="601.6" y1="147.2" x2="601.6" y2="161.8" stroke="var(--up)" class="wick"/>
<rect x="600.43" y="152.1" width="2.36" height="6.3" fill="var(--up)"/>
<line x1="605.4" y1="128.1" x2="605.4" y2="154.7" stroke="var(--up)" class="wick"/>
<rect x="604.23" y="145.5" width="2.36" height="8.6" fill="var(--up)"/>
<line x1="609.2" y1="151.3" x2="609.2" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="608.03" y="151.3" width="2.36" height="6.1" fill="var(--down)"/>
<line x1="613.0" y1="150.4" x2="613.0" y2="191.4" stroke="var(--down)" class="wick"/>
<rect x="611.83" y="154.1" width="2.36" height="33.8" fill="var(--down)"/>
<line x1="616.8" y1="176.3" x2="616.8" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="615.63" y="180.6" width="2.36" height="1.1" fill="var(--down)"/>
<line x1="620.6" y1="167.3" x2="620.6" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="619.43" y="169.6" width="2.36" height="9.6" fill="var(--up)"/>
<line x1="624.4" y1="148.5" x2="624.4" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="623.24" y="158.2" width="2.36" height="21.4" fill="var(--down)"/>
<line x1="628.2" y1="171.5" x2="628.2" y2="194.2" stroke="var(--down)" class="wick"/>
<rect x="627.04" y="174.8" width="2.36" height="16.5" fill="var(--down)"/>
<line x1="632.0" y1="182.8" x2="632.0" y2="197.6" stroke="var(--up)" class="wick"/>
<rect x="630.84" y="184.2" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="635.8" y1="176.8" x2="635.8" y2="190.8" stroke="var(--down)" class="wick"/>
<rect x="634.64" y="186.2" width="2.36" height="3.5" fill="var(--down)"/>
<line x1="639.6" y1="191.7" x2="639.6" y2="247.1" stroke="var(--down)" class="wick"/>
<rect x="638.44" y="194.9" width="2.36" height="52.2" fill="var(--down)"/>
<line x1="643.4" y1="214.8" x2="643.4" y2="264.4" stroke="var(--up)" class="wick"/>
<rect x="642.24" y="226.0" width="2.36" height="34.5" fill="var(--up)"/>
<line x1="647.2" y1="222.5" x2="647.2" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="646.04" y="226.3" width="2.36" height="6.8" fill="var(--down)"/>
<line x1="651.0" y1="231.9" x2="651.0" y2="251.2" stroke="var(--down)" class="wick"/>
<rect x="649.84" y="237.6" width="2.36" height="7.5" fill="var(--down)"/>
<line x1="654.8" y1="229.8" x2="654.8" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="653.64" y="230.4" width="2.36" height="14.2" fill="var(--up)"/>
<line x1="658.6" y1="228.7" x2="658.6" y2="267.4" stroke="var(--down)" class="wick"/>
<rect x="657.44" y="229.8" width="2.36" height="28.9" fill="var(--down)"/>
<line x1="662.4" y1="253.3" x2="662.4" y2="272.2" stroke="var(--down)" class="wick"/>
<rect x="661.24" y="253.3" width="2.36" height="13.8" fill="var(--down)"/>
<line x1="666.2" y1="250.5" x2="666.2" y2="273.7" stroke="var(--up)" class="wick"/>
<rect x="665.04" y="256.1" width="2.36" height="12.7" fill="var(--up)"/>
<line x1="670.0" y1="243.0" x2="670.0" y2="256.1" stroke="var(--down)" class="wick"/>
<rect x="668.84" y="251.9" width="2.36" height="1.3" fill="var(--down)"/>
<line x1="673.8" y1="220.5" x2="673.8" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="672.65" y="220.5" width="2.36" height="26.9" fill="var(--up)"/>
<line x1="677.6" y1="201.0" x2="677.6" y2="217.3" stroke="var(--up)" class="wick"/>
<rect x="676.45" y="207.6" width="2.36" height="9.4" fill="var(--up)"/>
<line x1="681.4" y1="202.4" x2="681.4" y2="218.6" stroke="var(--down)" class="wick"/>
<rect x="680.25" y="204.1" width="2.36" height="3.5" fill="var(--down)"/>
<line x1="685.2" y1="181.5" x2="685.2" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="684.05" y="185.2" width="2.36" height="13.2" fill="var(--up)"/>
<line x1="689.0" y1="166.5" x2="689.0" y2="190.0" stroke="var(--up)" class="wick"/>
<rect x="687.85" y="167.0" width="2.36" height="15.9" fill="var(--up)"/>
<line x1="692.8" y1="150.7" x2="692.8" y2="180.8" stroke="var(--up)" class="wick"/>
<rect x="691.65" y="174.8" width="2.36" height="3.5" fill="var(--up)"/>
<line x1="696.6" y1="146.8" x2="696.6" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="695.45" y="157.6" width="2.36" height="16.9" fill="var(--up)"/>
<line x1="700.4" y1="148.7" x2="700.4" y2="170.4" stroke="var(--down)" class="wick"/>
<rect x="699.25" y="150.2" width="2.36" height="10.0" fill="var(--down)"/>
<line x1="704.2" y1="171.1" x2="704.2" y2="193.6" stroke="var(--down)" class="wick"/>
<rect x="703.05" y="173.1" width="2.36" height="19.7" fill="var(--down)"/>
<line x1="708.0" y1="178.3" x2="708.0" y2="200.1" stroke="var(--down)" class="wick"/>
<rect x="706.85" y="188.7" width="2.36" height="7.9" fill="var(--down)"/>
<line x1="711.8" y1="161.1" x2="711.8" y2="194.8" stroke="var(--up)" class="wick"/>
<rect x="710.65" y="161.7" width="2.36" height="30.5" fill="var(--up)"/>
<line x1="715.6" y1="134.3" x2="715.6" y2="167.0" stroke="var(--up)" class="wick"/>
<rect x="714.45" y="144.1" width="2.36" height="21.8" fill="var(--up)"/>
<line x1="719.4" y1="127.6" x2="719.4" y2="142.7" stroke="var(--up)" class="wick"/>
<rect x="718.25" y="130.7" width="2.36" height="9.7" fill="var(--up)"/>
<line x1="723.2" y1="133.4" x2="723.2" y2="145.1" stroke="var(--up)" class="wick"/>
<rect x="722.06" y="134.0" width="2.36" height="2.7" fill="var(--up)"/>
<line x1="727.0" y1="106.7" x2="727.0" y2="136.4" stroke="var(--up)" class="wick"/>
<rect x="725.86" y="108.6" width="2.36" height="26.9" fill="var(--up)"/>
<line x1="730.8" y1="104.0" x2="730.8" y2="137.9" stroke="var(--down)" class="wick"/>
<rect x="729.66" y="109.8" width="2.36" height="22.4" fill="var(--down)"/>
<line x1="734.6" y1="124.4" x2="734.6" y2="140.2" stroke="var(--up)" class="wick"/>
<rect x="733.46" y="129.7" width="2.36" height="7.3" fill="var(--up)"/>
<line x1="738.4" y1="134.7" x2="738.4" y2="149.2" stroke="var(--up)" class="wick"/>
<rect x="737.26" y="137.8" width="2.36" height="5.2" fill="var(--up)"/>
<line x1="742.2" y1="133.7" x2="742.2" y2="161.8" stroke="var(--down)" class="wick"/>
<rect x="741.06" y="146.6" width="2.36" height="2.7" fill="var(--down)"/>
<line x1="746.0" y1="125.0" x2="746.0" y2="154.9" stroke="var(--down)" class="wick"/>
<rect x="744.86" y="148.7" width="2.36" height="2.7" fill="var(--down)"/>
<line x1="749.8" y1="136.8" x2="749.8" y2="160.7" stroke="var(--down)" class="wick"/>
<rect x="748.66" y="144.8" width="2.36" height="13.9" fill="var(--down)"/>
<line x1="753.6" y1="154.4" x2="753.6" y2="187.7" stroke="var(--down)" class="wick"/>
<rect x="752.46" y="156.3" width="2.36" height="29.0" fill="var(--down)"/>
<line x1="757.4" y1="169.4" x2="757.4" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="756.26" y="173.2" width="2.36" height="8.9" fill="var(--up)"/>
<line x1="761.2" y1="168.2" x2="761.2" y2="191.4" stroke="var(--up)" class="wick"/>
<rect x="760.06" y="174.5" width="2.36" height="10.7" fill="var(--up)"/>
<line x1="765.0" y1="170.1" x2="765.0" y2="193.4" stroke="var(--down)" class="wick"/>
<rect x="763.86" y="178.6" width="2.36" height="3.8" fill="var(--down)"/>
<line x1="768.8" y1="163.4" x2="768.8" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="767.66" y="175.3" width="2.36" height="6.6" fill="var(--down)"/>
<line x1="772.6" y1="181.4" x2="772.6" y2="233.9" stroke="var(--down)" class="wick"/>
<rect x="771.47" y="189.3" width="2.36" height="30.7" fill="var(--down)"/>
<line x1="776.4" y1="134.5" x2="776.4" y2="221.8" stroke="var(--up)" class="wick"/>
<rect x="775.27" y="148.5" width="2.36" height="72.6" fill="var(--up)"/>
<line x1="780.2" y1="153.4" x2="780.2" y2="179.1" stroke="var(--down)" class="wick"/>
<rect x="779.07" y="156.2" width="2.36" height="14.8" fill="var(--down)"/>
<line x1="784.0" y1="160.6" x2="784.0" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="782.87" y="162.0" width="2.36" height="18.4" fill="var(--down)"/>
<line x1="787.8" y1="171.1" x2="787.8" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="786.67" y="172.5" width="2.36" height="5.9" fill="var(--up)"/>
<line x1="791.6" y1="161.8" x2="791.6" y2="181.3" stroke="var(--up)" class="wick"/>
<rect x="790.47" y="165.1" width="2.36" height="10.4" fill="var(--up)"/>
<line x1="795.4" y1="141.6" x2="795.4" y2="163.2" stroke="var(--down)" class="wick"/>
<rect x="794.27" y="153.0" width="2.36" height="2.8" fill="var(--down)"/>
<line x1="799.2" y1="129.3" x2="799.2" y2="152.4" stroke="var(--down)" class="wick"/>
<rect x="798.07" y="140.6" width="2.36" height="5.6" fill="var(--down)"/>
<line x1="803.0" y1="147.3" x2="803.0" y2="162.4" stroke="var(--down)" class="wick"/>
<rect x="801.87" y="151.8" width="2.36" height="7.5" fill="var(--down)"/>
<line x1="806.9" y1="145.8" x2="806.9" y2="173.1" stroke="var(--up)" class="wick"/>
<rect x="805.67" y="146.1" width="2.36" height="10.1" fill="var(--up)"/>
<line x1="810.7" y1="144.9" x2="810.7" y2="170.0" stroke="var(--down)" class="wick"/>
<rect x="809.47" y="147.2" width="2.36" height="11.0" fill="var(--down)"/>
<line x1="814.5" y1="154.0" x2="814.5" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="813.27" y="155.6" width="2.36" height="9.4" fill="var(--down)"/>
<line x1="818.3" y1="165.6" x2="818.3" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="817.07" y="167.0" width="2.36" height="11.0" fill="var(--down)"/>
<line x1="822.1" y1="166.6" x2="822.1" y2="189.0" stroke="var(--up)" class="wick"/>
<rect x="820.88" y="168.9" width="2.36" height="13.4" fill="var(--up)"/>
<line x1="825.9" y1="156.6" x2="825.9" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="824.68" y="158.3" width="2.36" height="8.3" fill="var(--up)"/>
<line x1="829.7" y1="148.5" x2="829.7" y2="162.1" stroke="var(--down)" class="wick"/>
<rect x="828.48" y="156.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="833.5" y1="155.6" x2="833.5" y2="171.7" stroke="var(--up)" class="wick"/>
<rect x="832.28" y="163.5" width="2.36" height="2.5" fill="var(--up)"/>
<line x1="837.3" y1="158.7" x2="837.3" y2="187.5" stroke="var(--down)" class="wick"/>
<rect x="836.08" y="161.6" width="2.36" height="25.3" fill="var(--down)"/>
<line x1="841.1" y1="177.2" x2="841.1" y2="191.4" stroke="var(--up)" class="wick"/>
<rect x="839.88" y="177.7" width="2.36" height="8.6" fill="var(--up)"/>
<line x1="844.9" y1="171.1" x2="844.9" y2="189.1" stroke="var(--up)" class="wick"/>
<rect x="843.68" y="171.7" width="2.36" height="8.3" fill="var(--up)"/>
<line x1="848.7" y1="168.5" x2="848.7" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="847.48" y="175.9" width="2.36" height="5.3" fill="var(--down)"/>
<line x1="852.5" y1="176.3" x2="852.5" y2="189.3" stroke="var(--down)" class="wick"/>
<rect x="851.28" y="178.3" width="2.36" height="7.6" fill="var(--down)"/>
<line x1="856.3" y1="174.8" x2="856.3" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="855.08" y="175.9" width="2.36" height="29.8" fill="var(--down)"/>
<line x1="860.1" y1="205.0" x2="860.1" y2="218.4" stroke="var(--down)" class="wick"/>
<rect x="858.88" y="207.7" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="863.9" y1="197.7" x2="863.9" y2="219.0" stroke="var(--up)" class="wick"/>
<rect x="862.68" y="198.3" width="2.36" height="11.3" fill="var(--up)"/>
<line x1="867.7" y1="189.6" x2="867.7" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="866.48" y="191.5" width="2.36" height="7.9" fill="var(--up)"/>
<line x1="871.5" y1="194.2" x2="871.5" y2="206.5" stroke="var(--down)" class="wick"/>
<rect x="870.29" y="196.7" width="2.36" height="4.4" fill="var(--down)"/>
<line x1="875.3" y1="193.8" x2="875.3" y2="211.7" stroke="var(--down)" class="wick"/>
<rect x="874.09" y="195.1" width="2.36" height="15.6" fill="var(--down)"/>
<line x1="879.1" y1="210.7" x2="879.1" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="877.89" y="210.7" width="2.36" height="6.2" fill="var(--down)"/>
<line x1="882.9" y1="215.6" x2="882.9" y2="225.3" stroke="var(--down)" class="wick"/>
<rect x="881.69" y="217.1" width="2.36" height="1.1" fill="var(--down)"/>
<line x1="886.7" y1="201.5" x2="886.7" y2="222.1" stroke="var(--up)" class="wick"/>
<rect x="885.49" y="203.6" width="2.36" height="11.4" fill="var(--up)"/>
<line x1="890.5" y1="195.2" x2="890.5" y2="208.6" stroke="var(--down)" class="wick"/>
<rect x="889.29" y="202.9" width="2.36" height="1.8" fill="var(--down)"/>
<line x1="894.3" y1="197.0" x2="894.3" y2="210.0" stroke="var(--up)" class="wick"/>
<rect x="893.09" y="197.0" width="2.36" height="1.7" fill="var(--up)"/>
<line x1="898.1" y1="195.1" x2="898.1" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="896.89" y="198.3" width="2.36" height="10.7" fill="var(--down)"/>
<line x1="901.9" y1="209.3" x2="901.9" y2="219.5" stroke="var(--down)" class="wick"/>
<rect x="900.69" y="210.0" width="2.36" height="5.5" fill="var(--down)"/>
<line x1="905.7" y1="197.4" x2="905.7" y2="210.8" stroke="var(--up)" class="wick"/>
<rect x="904.49" y="198.3" width="2.36" height="12.5" fill="var(--up)"/>
<line x1="909.5" y1="189.1" x2="909.5" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="908.29" y="190.5" width="2.36" height="7.2" fill="var(--up)"/>
<line x1="913.3" y1="190.3" x2="913.3" y2="202.7" stroke="var(--down)" class="wick"/>
<rect x="912.09" y="193.9" width="2.36" height="2.7" fill="var(--down)"/>
<line x1="917.1" y1="189.4" x2="917.1" y2="202.4" stroke="var(--down)" class="wick"/>
<rect x="915.89" y="194.3" width="2.36" height="4.4" fill="var(--down)"/>
<line x1="920.9" y1="190.1" x2="920.9" y2="202.7" stroke="var(--up)" class="wick"/>
<rect x="919.70" y="191.5" width="2.36" height="10.0" fill="var(--up)"/>
<line x1="924.7" y1="188.2" x2="924.7" y2="200.4" stroke="var(--down)" class="wick"/>
<rect x="923.50" y="192.1" width="2.36" height="1.7" fill="var(--down)"/>
<line x1="928.5" y1="185.1" x2="928.5" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="927.30" y="185.3" width="2.36" height="4.8" fill="var(--up)"/>
<line x1="932.3" y1="174.1" x2="932.3" y2="185.1" stroke="var(--down)" class="wick"/>
<rect x="931.10" y="178.6" width="2.36" height="5.6" fill="var(--down)"/>
<line x1="936.1" y1="179.7" x2="936.1" y2="189.3" stroke="var(--up)" class="wick"/>
<rect x="934.90" y="183.9" width="2.36" height="3.9" fill="var(--up)"/>
<line x1="939.9" y1="175.6" x2="939.9" y2="190.5" stroke="var(--down)" class="wick"/>
<rect x="938.70" y="184.6" width="2.36" height="4.2" fill="var(--down)"/>
<line x1="943.7" y1="184.4" x2="943.7" y2="211.4" stroke="var(--down)" class="wick"/>
<rect x="942.50" y="184.4" width="2.36" height="25.6" fill="var(--down)"/>
<line x1="947.5" y1="202.9" x2="947.5" y2="214.3" stroke="var(--up)" class="wick"/>
<rect x="946.30" y="205.7" width="2.36" height="7.7" fill="var(--up)"/>
<line x1="951.3" y1="207.3" x2="951.3" y2="224.0" stroke="var(--down)" class="wick"/>
<rect x="950.10" y="207.3" width="2.36" height="15.9" fill="var(--down)"/>
<line x1="955.1" y1="191.5" x2="955.1" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="953.90" y="199.1" width="2.36" height="19.0" fill="var(--up)"/>
<line x1="958.9" y1="177.0" x2="958.9" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="957.70" y="177.7" width="2.36" height="15.8" fill="var(--up)"/>
<line x1="962.7" y1="162.4" x2="962.7" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="961.50" y="162.8" width="2.36" height="21.8" fill="var(--up)"/>
<line x1="966.5" y1="149.7" x2="966.5" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="965.30" y="155.9" width="2.36" height="9.0" fill="var(--up)"/>
<line x1="970.3" y1="164.4" x2="970.3" y2="177.5" stroke="var(--down)" class="wick"/>
<rect x="969.11" y="165.2" width="2.36" height="8.6" fill="var(--down)"/>
<line x1="974.1" y1="164.4" x2="974.1" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="972.91" y="167.2" width="2.36" height="6.1" fill="var(--down)"/>
<line x1="977.9" y1="168.5" x2="977.9" y2="186.0" stroke="var(--down)" class="wick"/>
<rect x="976.71" y="168.7" width="2.36" height="14.5" fill="var(--down)"/>
<line x1="981.7" y1="168.2" x2="981.7" y2="183.5" stroke="var(--up)" class="wick"/>
<rect x="980.51" y="174.2" width="2.36" height="6.8" fill="var(--up)"/>
<line x1="985.5" y1="157.1" x2="985.5" y2="174.2" stroke="var(--up)" class="wick"/>
<rect x="984.31" y="164.7" width="2.36" height="9.3" fill="var(--up)"/>
<line x1="989.3" y1="152.5" x2="989.3" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="988.11" y="161.6" width="2.36" height="5.1" fill="var(--down)"/>
<line x1="993.1" y1="133.5" x2="993.1" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="991.91" y="134.1" width="2.36" height="28.6" fill="var(--up)"/>
<line x1="996.9" y1="121.2" x2="996.9" y2="143.5" stroke="var(--down)" class="wick"/>
<rect x="995.71" y="133.5" width="2.36" height="5.8" fill="var(--down)"/>
<line x1="1000.7" y1="145.8" x2="1000.7" y2="157.9" stroke="var(--down)" class="wick"/>
<rect x="999.51" y="149.0" width="2.36" height="5.1" fill="var(--down)"/>
<line x1="1004.5" y1="139.9" x2="1004.5" y2="157.6" stroke="var(--up)" class="wick"/>
<rect x="1003.31" y="142.4" width="2.36" height="11.1" fill="var(--up)"/>
<line x1="1008.3" y1="139.0" x2="1008.3" y2="153.5" stroke="var(--down)" class="wick"/>
<rect x="1007.11" y="141.9" width="2.36" height="7.5" fill="var(--down)"/>
<line x1="1012.1" y1="150.4" x2="1012.1" y2="158.7" stroke="var(--down)" class="wick"/>
<rect x="1010.91" y="153.8" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="1015.9" y1="145.4" x2="1015.9" y2="166.8" stroke="var(--down)" class="wick"/>
<rect x="1014.71" y="148.2" width="2.36" height="17.3" fill="var(--down)"/>
<line x1="1019.7" y1="146.8" x2="1019.7" y2="166.2" stroke="var(--up)" class="wick"/>
<rect x="1018.52" y="149.6" width="2.36" height="15.1" fill="var(--up)"/>
<line x1="1023.5" y1="133.8" x2="1023.5" y2="153.5" stroke="var(--up)" class="wick"/>
<rect x="1022.32" y="137.8" width="2.36" height="15.8" fill="var(--up)"/>
<line x1="1027.3" y1="130.9" x2="1027.3" y2="145.9" stroke="var(--down)" class="wick"/>
<rect x="1026.12" y="135.5" width="2.36" height="6.2" fill="var(--down)"/>
<line x1="1031.1" y1="117.4" x2="1031.1" y2="139.0" stroke="var(--up)" class="wick"/>
<rect x="1029.92" y="122.3" width="2.36" height="15.9" fill="var(--up)"/>
<line x1="1034.9" y1="112.7" x2="1034.9" y2="135.1" stroke="var(--up)" class="wick"/>
<rect x="1033.72" y="113.0" width="2.36" height="13.8" fill="var(--up)"/>
<line x1="1038.7" y1="119.1" x2="1038.7" y2="133.0" stroke="var(--down)" class="wick"/>
<rect x="1037.52" y="123.4" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="1042.5" y1="118.9" x2="1042.5" y2="131.6" stroke="var(--up)" class="wick"/>
<rect x="1041.32" y="119.9" width="2.36" height="4.8" fill="var(--up)"/>
<line x1="1046.3" y1="112.9" x2="1046.3" y2="128.2" stroke="var(--up)" class="wick"/>
<rect x="1045.12" y="114.0" width="2.36" height="6.2" fill="var(--up)"/>
<line x1="1050.1" y1="116.5" x2="1050.1" y2="130.5" stroke="var(--down)" class="wick"/>
<rect x="1048.92" y="117.4" width="2.36" height="5.9" fill="var(--down)"/>
<line x1="60" y1="113.0" x2="1052" y2="113.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="116.5" font-size="11.5" fill="var(--resistance)" font-weight="600">4.75% R1</text>
<text x="1058" y="128.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="194.6" x2="1052" y2="194.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="188.6" font-size="11.5" fill="var(--support)" font-weight="600">4.17% S1</text>
<text x="1058" y="200.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="220.6" x2="1052" y2="220.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.6" font-size="11.5" fill="var(--support)" font-weight="600">3.98% S2</text>
<text x="1058" y="226.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="241.9" x2="1052" y2="241.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="235.9" font-size="11.5" fill="var(--support)" font-weight="600">3.83% S3</text>
<text x="1058" y="247.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="123.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="115.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 4.67% (2026-08-24)</text>
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

- **상승**: 성장·인플레이션에 대한 기대가 커지거나, 재정적자 우려, 연준의 긴축 기대 신호로 흔히 해석한다 — DCF에서 쓰는 무위험이자율이 오르면 할인율도 함께 올라가 밸류에이션에는 하방 압력으로 작용한다.
- **하락**: 성장·인플레이션 기대가 둔화되거나, 안전자산 수요가 늘거나, 연준의 완화 기대 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 10년물 국채는 발행량·거래량이 가장 많아 사고팔기 쉽고(유동성이 좋고), 주택담보대출 같은 실물경제 금리를 정할 때도 기준으로 널리 쓰여서 DCF 무위험이자율의 표준으로 자리 잡았다. 재정적자 우려가 반영되는 경로도 직접적이다 — 국채를 더 많이 찍어낼 것이라는 기대는, 만기가 긴 채권일수록(그만큼 더 오래 그 부담을 떠안아야 하므로) 가격에 더 크게 반영된다(기간 프리미엄).
- 국채금리는 연준의 정책, 인플레이션 기대, 재정정책 등 여러 요인이 겹쳐서 움직인다 — 이 차트 하나만 보고 방향을 미리 단정하지 않는다.

---

*작성일: 2026-08-29*
