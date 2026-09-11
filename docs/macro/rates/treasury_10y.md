# 미국 10년물 국채금리

::: info
최근 5년간 미국 10년물 국채 수익률(`^TNX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. DCF 밸류에이션에서 "위험이 거의 없는 이자율(무위험이자율)"의 대표적인 기준으로 쓰이며, 금리가 어떤 국면인지에 따라 성장주의 밸류에이션 배수가 크게 달라진다.

:::
---

## 1. 차트 — 최근 5년 주봉

<div class="tnx-chart">
<style>
.tnx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .tnx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .tnx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tnx-chart svg { width:100%; height:auto; display:block; }
.tnx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tnx-chart .title { fill: var(--ink); font-weight:600; }
.tnx-chart .grid { stroke: var(--grid); stroke-width:1; }
.tnx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 10년물 금리(^TNX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 10년물 금리 (^TNX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-10 · 마지막 종가 4.94% (2026-09-10) · 단위 %</text>
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
<line x1="61.9" y1="590.1" x2="61.9" y2="595.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="592.1" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="65.7" y1="585.7" x2="65.7" y2="603.5" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="588.0" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="69.4" y1="574.5" x2="69.4" y2="598.3" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="575.3" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="73.2" y1="560.3" x2="73.2" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="570.3" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="77.0" y1="553.2" x2="77.0" y2="574.9" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="554.9" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="80.7" y1="553.5" x2="80.7" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="553.7" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="84.5" y1="542.8" x2="84.5" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="547.9" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="88.3" y1="545.4" x2="88.3" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="548.0" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="92.1" y1="554.9" x2="92.1" y2="576.7" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="557.5" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="95.8" y1="556.8" x2="95.8" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="558.2" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="99.6" y1="549.2" x2="99.6" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="562.2" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="103.4" y1="542.5" x2="103.4" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="559.1" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="107.1" y1="560.6" x2="107.1" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="563.1" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="110.9" y1="564.5" x2="110.9" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="571.3" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="114.7" y1="572.0" x2="114.7" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="574.2" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="118.5" y1="569.6" x2="118.5" y2="587.3" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="570.7" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="122.2" y1="561.5" x2="122.2" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="568.0" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="126.0" y1="527.3" x2="126.0" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="531.6" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="129.8" y1="526.4" x2="129.8" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="531.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="133.6" y1="517.1" x2="133.6" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="523.7" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="137.3" y1="519.5" x2="137.3" y2="540.6" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="530.0" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="141.1" y1="508.3" x2="141.1" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="509.2" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="144.9" y1="490.5" x2="144.9" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="505.7" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="148.6" y1="490.2" x2="148.6" y2="510.9" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="504.5" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="152.4" y1="497.8" x2="152.4" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="501.3" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="156.2" y1="510.6" x2="156.2" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="511.0" width="2.34" height="27.2" fill="var(--down)"/>
<line x1="160.0" y1="496.4" x2="160.0" y2="538.9" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="498.8" width="2.34" height="32.5" fill="var(--up)"/>
<line x1="163.7" y1="464.7" x2="163.7" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="478.5" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="167.5" y1="428.5" x2="167.5" y2="470.2" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="430.1" width="2.34" height="40.1" fill="var(--up)"/>
<line x1="171.3" y1="429.5" x2="171.3" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="434.0" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="175.0" y1="396.9" x2="175.0" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="399.0" width="2.34" height="43.5" fill="var(--up)"/>
<line x1="178.8" y1="381.8" x2="178.8" y2="408.4" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="382.8" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="182.6" y1="365.1" x2="182.6" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="371.8" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="186.4" y1="367.9" x2="186.4" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="374.5" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="190.1" y1="340.2" x2="190.1" y2="371.7" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="341.3" width="2.34" height="28.3" fill="var(--up)"/>
<line x1="193.9" y1="335.1" x2="193.9" y2="384.3" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="335.7" width="2.34" height="32.1" fill="var(--down)"/>
<line x1="197.7" y1="356.6" x2="197.7" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="368.6" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="201.4" y1="377.2" x2="201.4" y2="399.7" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="382.2" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="205.2" y1="360.6" x2="205.2" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="364.6" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="209.0" y1="333.5" x2="209.0" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="336.6" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="212.8" y1="290.6" x2="212.8" y2="330.9" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="318.9" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="216.5" y1="314.0" x2="216.5" y2="357.9" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="318.8" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="220.3" y1="323.0" x2="220.3" y2="388.0" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="332.8" width="2.34" height="41.4" fill="var(--down)"/>
<line x1="224.1" y1="344.4" x2="224.1" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="344.4" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="227.8" y1="348.6" x2="227.8" y2="372.8" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="351.7" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="231.6" y1="347.2" x2="231.6" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="364.2" width="2.34" height="24.9" fill="var(--down)"/>
<line x1="235.4" y1="380.4" x2="235.4" y2="412.4" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="384.8" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="239.2" y1="377.0" x2="239.2" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="381.1" width="2.34" height="25.6" fill="var(--up)"/>
<line x1="242.9" y1="372.4" x2="242.9" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="379.8" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="246.7" y1="358.9" x2="246.7" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="360.1" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="250.5" y1="340.6" x2="250.5" y2="363.5" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="353.7" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="254.3" y1="317.1" x2="254.3" y2="349.2" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="331.4" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="258.0" y1="308.9" x2="258.0" y2="329.2" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="313.4" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="261.8" y1="289.6" x2="261.8" y2="321.7" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="295.5" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="265.6" y1="249.8" x2="265.6" y2="293.4" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="260.5" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="269.3" y1="219.0" x2="269.3" y2="262.0" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="245.4" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="273.1" y1="230.5" x2="273.1" y2="279.2" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="234.3" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="276.9" y1="206.6" x2="276.9" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="216.4" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="280.7" y1="171.0" x2="280.7" y2="230.5" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="187.9" width="2.34" height="38.6" fill="var(--up)"/>
<line x1="284.4" y1="176.9" x2="284.4" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="190.8" width="2.34" height="25.6" fill="var(--down)"/>
<line x1="288.2" y1="186.5" x2="288.2" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="195.9" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="292.0" y1="187.2" x2="292.0" y2="244.2" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="197.9" width="2.34" height="46.3" fill="var(--down)"/>
<line x1="295.7" y1="231.8" x2="295.7" y2="261.2" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="234.2" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="299.5" y1="240.9" x2="299.5" y2="262.7" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="244.0" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="303.3" y1="246.3" x2="303.3" y2="287.7" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="262.5" width="2.34" height="24.9" fill="var(--down)"/>
<line x1="307.1" y1="272.5" x2="307.1" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="278.8" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="310.8" y1="269.9" x2="310.8" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="282.2" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="314.6" y1="252.6" x2="314.6" y2="280.9" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="252.9" width="2.34" height="27.0" fill="var(--up)"/>
<line x1="318.4" y1="231.2" x2="318.4" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="234.9" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="322.1" y1="244.6" x2="322.1" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="251.9" width="2.34" height="26.6" fill="var(--down)"/>
<line x1="325.9" y1="268.7" x2="325.9" y2="298.1" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="275.7" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="329.7" y1="277.1" x2="329.7" y2="306.1" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="277.7" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="333.5" y1="280.3" x2="333.5" y2="299.2" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="285.7" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="337.2" y1="277.8" x2="337.2" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="280.8" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="341.0" y1="253.5" x2="341.0" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="253.9" width="2.34" height="20.4" fill="var(--up)"/>
<line x1="344.8" y1="231.9" x2="344.8" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="242.1" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="348.5" y1="220.9" x2="348.5" y2="237.1" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="225.0" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="352.3" y1="205.0" x2="352.3" y2="232.3" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="222.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="215.5" x2="356.1" y2="263.7" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="231.2" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="359.9" y1="262.2" x2="359.9" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="287.5" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="363.6" y1="268.0" x2="363.6" y2="317.1" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="303.0" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="367.4" y1="272.7" x2="367.4" y2="292.7" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="289.1" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="371.2" y1="284.8" x2="371.2" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="285.8" width="2.34" height="32.2" fill="var(--down)"/>
<line x1="375.0" y1="283.2" x2="375.0" y2="310.5" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="285.1" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="378.7" y1="268.7" x2="378.7" y2="287.9" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="278.4" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="382.5" y1="281.9" x2="382.5" y2="305.8" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="281.9" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="386.3" y1="277.5" x2="386.3" y2="316.9" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="288.1" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="390.0" y1="283.7" x2="390.0" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="289.6" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="393.8" y1="257.1" x2="393.8" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="261.2" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="397.6" y1="237.7" x2="397.6" y2="265.0" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="244.6" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="401.4" y1="252.5" x2="401.4" y2="278.4" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="258.4" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="405.1" y1="243.0" x2="405.1" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="252.6" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="408.9" y1="238.8" x2="408.9" y2="262.6" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="250.4" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="412.7" y1="244.6" x2="412.7" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="254.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="416.4" y1="235.9" x2="416.4" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="243.3" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="420.2" y1="204.6" x2="420.2" y2="249.1" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="210.8" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="424.0" y1="204.9" x2="424.0" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="210.5" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="427.8" y1="235.6" x2="427.8" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="240.8" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="431.5" y1="214.8" x2="431.5" y2="246.3" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="222.2" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="435.3" y1="188.9" x2="435.3" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="209.4" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="439.1" y1="194.2" x2="439.1" y2="223.9" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="194.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="442.8" y1="171.7" x2="442.8" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="182.5" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="446.6" y1="166.9" x2="446.6" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="176.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="450.4" y1="183.7" x2="450.4" y2="209.4" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="185.2" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="454.2" y1="174.5" x2="454.2" y2="188.0" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="181.5" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="457.9" y1="169.4" x2="457.9" y2="186.5" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="172.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="461.7" y1="148.9" x2="461.7" y2="174.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="156.2" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="465.5" y1="121.0" x2="465.5" y2="149.9" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="137.2" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="469.2" y1="93.0" x2="469.2" y2="129.6" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="107.5" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="473.0" y1="105.7" x2="473.0" y2="143.0" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="105.7" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="476.8" y1="77.7" x2="476.8" y2="124.1" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="87.8" width="2.34" height="32.8" fill="var(--up)"/>
<line x1="480.6" y1="77.5" x2="480.6" y2="101.5" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="77.5" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="484.3" y1="88.1" x2="484.3" y2="149.7" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="91.7" width="2.34" height="47.6" fill="var(--down)"/>
<line x1="488.1" y1="123.8" x2="488.1" y2="147.1" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="129.5" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="491.9" y1="119.9" x2="491.9" y2="161.0" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="127.5" width="2.34" height="28.3" fill="var(--down)"/>
<line x1="495.7" y1="148.6" x2="495.7" y2="166.5" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="151.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="499.4" y1="153.0" x2="499.4" y2="188.2" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="153.5" width="2.34" height="32.5" fill="var(--down)"/>
<line x1="503.2" y1="175.8" x2="503.2" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="183.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="507.0" y1="176.6" x2="507.0" y2="234.0" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="179.3" width="2.34" height="48.7" fill="var(--down)"/>
<line x1="510.7" y1="221.9" x2="510.7" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="229.5" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="514.5" y1="230.8" x2="514.5" y2="248.1" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="230.8" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="518.3" y1="203.9" x2="518.3" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="211.9" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="522.1" y1="208.3" x2="522.1" y2="229.7" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="209.5" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="525.8" y1="190.0" x2="525.8" y2="219.3" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="197.3" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="529.6" y1="191.4" x2="529.6" y2="207.3" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="195.3" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="533.4" y1="200.7" x2="533.4" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="202.7" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="537.1" y1="190.7" x2="537.1" y2="208.7" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="191.5" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="540.9" y1="171.7" x2="540.9" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="176.3" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="544.7" y1="168.0" x2="544.7" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="178.0" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="548.5" y1="172.7" x2="548.5" y2="192.8" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="183.5" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="552.2" y1="184.8" x2="552.2" y2="212.5" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="187.0" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="556.0" y1="172.8" x2="556.0" y2="207.3" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="175.1" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="559.8" y1="168.9" x2="559.8" y2="189.7" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="173.7" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="563.5" y1="179.4" x2="563.5" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="185.2" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="567.3" y1="157.5" x2="567.3" y2="184.9" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="164.7" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="571.1" y1="134.7" x2="571.1" y2="169.4" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="147.6" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="574.9" y1="119.9" x2="574.9" y2="136.9" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="131.3" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="578.6" y1="114.1" x2="578.6" y2="137.9" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="123.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="582.4" y1="121.3" x2="582.4" y2="154.1" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="129.7" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="586.2" y1="145.2" x2="586.2" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="146.9" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="589.9" y1="143.0" x2="589.9" y2="173.0" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="149.3" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="593.7" y1="147.2" x2="593.7" y2="161.8" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="152.1" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="597.5" y1="128.1" x2="597.5" y2="154.7" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="145.5" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="601.3" y1="151.3" x2="601.3" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="151.3" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="605.0" y1="150.4" x2="605.0" y2="191.4" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="154.1" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="608.8" y1="176.3" x2="608.8" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="180.6" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="612.6" y1="167.3" x2="612.6" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="169.6" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="616.3" y1="148.5" x2="616.3" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="158.2" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="620.1" y1="171.5" x2="620.1" y2="194.2" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="174.8" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="623.9" y1="182.8" x2="623.9" y2="197.6" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="184.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="627.7" y1="176.8" x2="627.7" y2="190.8" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="186.2" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="631.4" y1="191.7" x2="631.4" y2="247.1" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="194.9" width="2.34" height="52.2" fill="var(--down)"/>
<line x1="635.2" y1="214.8" x2="635.2" y2="264.4" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="226.0" width="2.34" height="34.5" fill="var(--up)"/>
<line x1="639.0" y1="222.5" x2="639.0" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="226.3" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="642.8" y1="231.9" x2="642.8" y2="251.2" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="237.6" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="646.5" y1="229.8" x2="646.5" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="230.4" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="650.3" y1="228.7" x2="650.3" y2="267.4" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="229.8" width="2.34" height="28.9" fill="var(--down)"/>
<line x1="654.1" y1="253.3" x2="654.1" y2="272.2" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="253.3" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="657.8" y1="250.5" x2="657.8" y2="273.7" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="256.1" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="661.6" y1="243.0" x2="661.6" y2="256.1" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="251.9" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="665.4" y1="220.5" x2="665.4" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="220.5" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="669.2" y1="201.0" x2="669.2" y2="217.3" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="207.6" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="672.9" y1="202.4" x2="672.9" y2="218.6" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="204.1" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="676.7" y1="181.5" x2="676.7" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="185.2" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="680.5" y1="166.5" x2="680.5" y2="190.0" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="167.0" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="684.2" y1="150.7" x2="684.2" y2="180.8" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="174.8" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="688.0" y1="146.8" x2="688.0" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="157.6" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="691.8" y1="148.7" x2="691.8" y2="170.4" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="150.2" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="695.6" y1="171.1" x2="695.6" y2="193.6" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="173.1" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="699.3" y1="178.3" x2="699.3" y2="200.1" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="188.7" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="703.1" y1="161.1" x2="703.1" y2="194.8" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="161.7" width="2.34" height="30.5" fill="var(--up)"/>
<line x1="706.9" y1="134.3" x2="706.9" y2="167.0" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="144.1" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="710.6" y1="127.6" x2="710.6" y2="142.7" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="130.7" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="714.4" y1="133.4" x2="714.4" y2="145.1" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="134.0" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="718.2" y1="106.7" x2="718.2" y2="136.4" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="108.6" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="722.0" y1="104.0" x2="722.0" y2="137.9" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="109.8" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="725.7" y1="124.4" x2="725.7" y2="140.2" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="129.7" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="729.5" y1="134.7" x2="729.5" y2="149.2" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="137.8" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="733.3" y1="133.7" x2="733.3" y2="161.8" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="146.6" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="737.0" y1="125.0" x2="737.0" y2="154.9" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="148.7" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="740.8" y1="136.8" x2="740.8" y2="160.7" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="144.8" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="744.6" y1="154.4" x2="744.6" y2="187.7" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="156.3" width="2.34" height="29.0" fill="var(--down)"/>
<line x1="748.4" y1="169.4" x2="748.4" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="173.2" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="752.1" y1="168.2" x2="752.1" y2="191.4" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="174.5" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="755.9" y1="170.1" x2="755.9" y2="193.4" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="178.6" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="759.7" y1="163.4" x2="759.7" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="175.3" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="763.5" y1="181.4" x2="763.5" y2="233.9" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="189.3" width="2.34" height="30.7" fill="var(--down)"/>
<line x1="767.2" y1="134.5" x2="767.2" y2="221.8" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="148.5" width="2.34" height="72.6" fill="var(--up)"/>
<line x1="771.0" y1="153.4" x2="771.0" y2="179.1" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="156.2" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="774.8" y1="160.6" x2="774.8" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="162.0" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="778.5" y1="171.1" x2="778.5" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="172.5" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="782.3" y1="161.8" x2="782.3" y2="181.3" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="165.1" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="786.1" y1="141.6" x2="786.1" y2="163.2" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="153.0" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="789.9" y1="129.3" x2="789.9" y2="152.4" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="140.6" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="793.6" y1="147.3" x2="793.6" y2="162.4" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="151.8" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="797.4" y1="145.8" x2="797.4" y2="173.1" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="146.1" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="801.2" y1="144.9" x2="801.2" y2="170.0" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="147.2" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="804.9" y1="154.0" x2="804.9" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="155.6" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="808.7" y1="165.6" x2="808.7" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="167.0" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="812.5" y1="166.6" x2="812.5" y2="189.0" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="168.9" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="816.3" y1="156.6" x2="816.3" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="158.3" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="820.0" y1="148.5" x2="820.0" y2="162.1" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="156.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="823.8" y1="155.6" x2="823.8" y2="171.7" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="163.5" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="827.6" y1="158.7" x2="827.6" y2="187.5" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="161.6" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="831.3" y1="177.2" x2="831.3" y2="191.4" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="177.7" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="835.1" y1="171.1" x2="835.1" y2="189.1" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="171.7" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="838.9" y1="168.5" x2="838.9" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="175.9" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="842.7" y1="176.3" x2="842.7" y2="189.3" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="178.3" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="846.4" y1="174.8" x2="846.4" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="175.9" width="2.34" height="29.8" fill="var(--down)"/>
<line x1="850.2" y1="205.0" x2="850.2" y2="218.4" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="207.7" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="854.0" y1="197.7" x2="854.0" y2="219.0" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="198.3" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="857.7" y1="189.6" x2="857.7" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="191.5" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="861.5" y1="194.2" x2="861.5" y2="206.5" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="196.7" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="865.3" y1="193.8" x2="865.3" y2="211.7" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="195.1" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="869.1" y1="210.7" x2="869.1" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="210.7" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="872.8" y1="215.6" x2="872.8" y2="225.3" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="217.1" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="876.6" y1="201.5" x2="876.6" y2="222.1" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="203.6" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="880.4" y1="195.2" x2="880.4" y2="208.6" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="202.9" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="884.2" y1="197.0" x2="884.2" y2="210.0" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="197.0" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="887.9" y1="195.1" x2="887.9" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="198.3" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="891.7" y1="209.3" x2="891.7" y2="219.5" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="210.0" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="895.5" y1="197.4" x2="895.5" y2="210.8" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="198.3" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="899.2" y1="189.1" x2="899.2" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="190.5" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="903.0" y1="190.3" x2="903.0" y2="202.7" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="193.9" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="906.8" y1="189.4" x2="906.8" y2="202.4" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="194.3" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="910.6" y1="190.1" x2="910.6" y2="202.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="191.5" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="914.3" y1="188.2" x2="914.3" y2="200.4" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="192.1" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="918.1" y1="185.1" x2="918.1" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="185.3" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="921.9" y1="174.1" x2="921.9" y2="185.1" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="178.6" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="925.6" y1="179.7" x2="925.6" y2="189.3" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="183.9" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="929.4" y1="175.6" x2="929.4" y2="190.5" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="184.6" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="933.2" y1="184.4" x2="933.2" y2="211.4" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="184.4" width="2.34" height="25.6" fill="var(--down)"/>
<line x1="937.0" y1="202.9" x2="937.0" y2="214.3" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="205.7" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="940.7" y1="207.3" x2="940.7" y2="224.0" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="207.3" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="944.5" y1="191.5" x2="944.5" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="199.1" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="948.3" y1="177.0" x2="948.3" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="177.7" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="952.0" y1="162.4" x2="952.0" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="162.8" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="955.8" y1="149.7" x2="955.8" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="155.9" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="959.6" y1="164.4" x2="959.6" y2="177.5" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="165.2" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="963.4" y1="164.4" x2="963.4" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="167.2" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="967.1" y1="168.5" x2="967.1" y2="186.0" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="168.7" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="970.9" y1="168.2" x2="970.9" y2="183.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="174.2" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="974.7" y1="157.1" x2="974.7" y2="174.2" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="164.7" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="978.4" y1="152.5" x2="978.4" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="161.6" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="982.2" y1="133.5" x2="982.2" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="134.1" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="986.0" y1="121.2" x2="986.0" y2="143.5" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="133.5" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="989.8" y1="145.8" x2="989.8" y2="157.9" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="149.0" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="993.5" y1="139.9" x2="993.5" y2="157.6" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="142.4" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="997.3" y1="139.0" x2="997.3" y2="153.5" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="141.9" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="1001.1" y1="150.4" x2="1001.1" y2="158.7" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="153.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1004.9" y1="145.4" x2="1004.9" y2="166.8" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="148.2" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="1008.6" y1="146.8" x2="1008.6" y2="166.2" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="149.6" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="1012.4" y1="133.8" x2="1012.4" y2="153.5" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="137.8" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="1016.2" y1="130.9" x2="1016.2" y2="145.9" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="135.5" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="1019.9" y1="117.4" x2="1019.9" y2="139.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="122.3" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="1023.7" y1="112.7" x2="1023.7" y2="135.1" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="113.0" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="1027.5" y1="119.1" x2="1027.5" y2="133.0" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="123.4" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="1031.3" y1="118.9" x2="1031.3" y2="131.6" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="119.9" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="1035.0" y1="112.9" x2="1035.0" y2="128.2" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="114.0" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="1038.8" y1="115.1" x2="1038.8" y2="130.5" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="116.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1042.6" y1="103.6" x2="1042.6" y2="115.7" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="107.5" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="1046.3" y1="83.9" x2="1046.3" y2="110.9" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="85.0" width="2.34" height="21.1" fill="var(--up)"/>
<line x1="1050.1" y1="83.9" x2="1050.1" y2="94.1" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="85.0" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="60" y1="194.6" x2="1052" y2="194.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="188.6" font-size="11.5" fill="var(--support)" font-weight="600">4.17% S1</text>
<text x="1058" y="200.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="220.6" x2="1052" y2="220.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.6" font-size="11.5" fill="var(--support)" font-weight="600">3.98% S2</text>
<text x="1058" y="226.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="241.9" x2="1052" y2="241.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="235.9" font-size="11.5" fill="var(--support)" font-weight="600">3.83% S3</text>
<text x="1058" y="247.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="85.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="77.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 4.94% (2026-09-10)</text>
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

*작성일: 2026-09-11*
