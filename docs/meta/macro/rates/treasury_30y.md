# 미국 30년물 국채금리

!!! note ""
    최근 5년 미 국채 30년물 수익률(`^TYX`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 13주 단기금리·5년물·10년물 국채금리와 함께 **수익률곡선의 최장기 구간**을 채운다.

    **왜 별도로 두는가**: 30년물은 가장 먼 미래의 성장·물가 기대와 기간 프리미엄을 반영해, 단기물보다 연준의 당장 정책보다는 장기 재정건전성·인플레이션 기대에 더 민감하게 움직이는 편이다.

---

## 1. 차트 — 최근 5년 주봉

<div class="tyx-chart">
<style>
.tyx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .tyx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .tyx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tyx-chart svg { width:100%; height:auto; display:block; }
.tyx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tyx-chart .title { fill: var(--ink); font-weight:600; }
.tyx-chart .grid { stroke: var(--grid); stroke-width:1; }
.tyx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 30년물 금리(^TYX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 30년물 금리 (^TYX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-17 · 마지막 종가 5.19% (2026-08-17) · 단위 %</text>
<line x1="60" y1="560.2" x2="1052" y2="560.2" class="grid"/>
<text x="52" y="564.2" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="487.2" x2="1052" y2="487.2" class="grid"/>
<text x="52" y="491.2" font-size="11" text-anchor="end" fill="var(--muted)">2.50</text>
<line x1="60" y1="414.1" x2="1052" y2="414.1" class="grid"/>
<text x="52" y="418.1" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">3.50</text>
<line x1="60" y1="267.9" x2="1052" y2="267.9" class="grid"/>
<text x="52" y="271.9" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="194.8" x2="1052" y2="194.8" class="grid"/>
<text x="52" y="198.8" font-size="11" text-anchor="end" fill="var(--muted)">4.50</text>
<line x1="60" y1="121.8" x2="1052" y2="121.8" class="grid"/>
<text x="52" y="125.8" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
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
<line x1="61.9" y1="576.0" x2="61.9" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="578.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="563.6" x2="65.7" y2="578.9" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="572.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="69.5" y1="567.0" x2="69.5" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="568.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="73.3" y1="560.5" x2="73.3" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="563.3" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="77.0" y1="568.6" x2="77.0" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="571.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="80.8" y1="561.4" x2="80.8" y2="585.1" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="562.0" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="84.6" y1="545.2" x2="84.6" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="551.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="88.4" y1="534.4" x2="88.4" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="536.6" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="92.2" y1="536.0" x2="92.2" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="536.0" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="96.0" y1="538.3" x2="96.0" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="546.9" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="99.8" y1="542.4" x2="99.8" y2="571.3" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="545.5" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="103.5" y1="556.6" x2="103.5" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="563.7" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="107.3" y1="562.7" x2="107.3" y2="590.2" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="566.8" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="111.1" y1="553.1" x2="111.1" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="570.2" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="114.9" y1="555.0" x2="114.9" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="569.0" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="118.7" y1="573.4" x2="118.7" y2="607.3" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="576.2" width="2.35" height="31.1" fill="var(--down)"/>
<line x1="122.5" y1="575.7" x2="122.5" y2="605.4" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="577.2" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="126.3" y1="574.1" x2="126.3" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="581.1" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="130.0" y1="570.9" x2="130.0" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="574.1" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="133.8" y1="564.5" x2="133.8" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="574.1" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="137.6" y1="538.3" x2="137.6" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="543.0" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="141.4" y1="538.2" x2="141.4" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="542.1" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="145.2" y1="532.2" x2="145.2" y2="552.6" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="538.9" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="149.0" y1="534.8" x2="149.0" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="548.1" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="152.8" y1="525.6" x2="152.8" y2="551.3" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="526.2" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="156.5" y1="508.6" x2="156.5" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="522.7" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="160.3" y1="503.7" x2="160.3" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="521.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="164.1" y1="514.6" x2="164.1" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="517.0" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="167.9" y1="521.1" x2="167.9" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="524.6" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="171.7" y1="499.6" x2="171.7" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="507.0" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="175.5" y1="481.2" x2="175.5" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="498.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="179.3" y1="466.1" x2="179.3" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="472.1" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="183.1" y1="474.9" x2="183.1" y2="499.6" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="476.9" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="186.8" y1="449.2" x2="186.8" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="451.2" width="2.35" height="39.3" fill="var(--up)"/>
<line x1="190.6" y1="424.5" x2="190.6" y2="450.5" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="425.9" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="194.4" y1="411.4" x2="194.4" y2="433.8" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="421.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="198.2" y1="415.5" x2="198.2" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="421.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="202.0" y1="381.5" x2="202.0" y2="418.8" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="381.8" width="2.35" height="33.3" fill="var(--up)"/>
<line x1="205.8" y1="373.6" x2="205.8" y2="417.9" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="374.0" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="209.6" y1="384.6" x2="209.6" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="399.3" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="213.3" y1="403.6" x2="213.3" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="409.3" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="217.1" y1="391.0" x2="217.1" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="397.4" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="220.9" y1="379.3" x2="220.9" y2="399.8" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="385.4" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="224.7" y1="345.1" x2="224.7" y2="378.1" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="371.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="228.5" y1="356.3" x2="228.5" y2="392.6" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="362.2" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="232.3" y1="361.0" x2="232.3" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="368.8" width="2.35" height="28.4" fill="var(--down)"/>
<line x1="236.1" y1="373.4" x2="236.1" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="374.8" width="2.35" height="24.8" fill="var(--up)"/>
<line x1="239.8" y1="380.3" x2="239.8" y2="405.0" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="380.9" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="243.6" y1="383.7" x2="243.6" y2="421.1" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="396.0" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="247.4" y1="400.3" x2="247.4" y2="421.1" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="406.8" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="251.2" y1="398.6" x2="251.2" y2="435.3" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="404.6" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="255.0" y1="386.5" x2="255.0" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="396.8" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="258.8" y1="379.6" x2="258.8" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="381.2" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="262.6" y1="365.8" x2="262.6" y2="387.2" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="381.5" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="266.4" y1="353.9" x2="266.4" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="363.8" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="270.1" y1="342.3" x2="270.1" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="347.4" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="273.9" y1="330.5" x2="273.9" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="338.2" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="277.7" y1="315.1" x2="277.7" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="324.6" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="281.5" y1="290.3" x2="281.5" y2="324.6" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="302.3" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="285.3" y1="285.9" x2="285.3" y2="320.7" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="291.2" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="289.1" y1="266.2" x2="289.1" y2="290.4" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="271.1" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="292.9" y1="211.9" x2="292.9" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="223.3" width="2.35" height="52.5" fill="var(--up)"/>
<line x1="296.6" y1="205.8" x2="296.6" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="222.0" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="300.4" y1="228.9" x2="300.4" y2="260.0" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="232.0" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="304.2" y1="219.1" x2="304.2" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="236.2" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="308.0" y1="255.2" x2="308.0" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="257.3" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="311.8" y1="280.3" x2="311.8" y2="306.4" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="282.2" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="315.6" y1="290.3" x2="315.6" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="309.1" width="2.35" height="22.8" fill="var(--down)"/>
<line x1="319.4" y1="319.1" x2="319.4" y2="353.7" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="331.8" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="323.1" y1="326.7" x2="323.1" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="336.2" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="326.9" y1="292.9" x2="326.9" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="293.2" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="330.7" y1="269.4" x2="330.7" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="271.6" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="334.5" y1="280.8" x2="334.5" y2="315.1" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="288.1" width="2.35" height="24.8" fill="var(--down)"/>
<line x1="338.3" y1="300.8" x2="338.3" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="308.3" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="342.1" y1="312.4" x2="342.1" y2="337.8" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="313.8" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="345.9" y1="309.1" x2="345.9" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="314.5" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="349.6" y1="314.1" x2="349.6" y2="341.3" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="317.6" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="353.4" y1="291.7" x2="353.4" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="293.2" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="357.2" y1="274.9" x2="357.2" y2="308.1" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="284.3" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="361.0" y1="270.7" x2="361.0" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="277.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="364.8" y1="261.1" x2="364.8" y2="284.9" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="272.7" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="368.6" y1="277.9" x2="368.6" y2="314.7" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="292.6" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="372.4" y1="297.6" x2="372.4" y2="337.2" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="326.7" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="376.2" y1="301.5" x2="376.2" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="320.0" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="379.9" y1="295.0" x2="379.9" y2="313.5" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="310.7" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="383.7" y1="311.6" x2="383.7" y2="337.1" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="312.4" width="2.35" height="22.8" fill="var(--down)"/>
<line x1="387.5" y1="303.9" x2="387.5" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="306.1" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="391.3" y1="292.3" x2="391.3" y2="308.3" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="300.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="395.1" y1="301.8" x2="395.1" y2="322.0" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="303.9" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="398.9" y1="294.1" x2="398.9" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="302.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="402.7" y1="289.1" x2="402.7" y2="309.3" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="296.7" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="406.4" y1="273.8" x2="406.4" y2="297.2" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="275.5" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="410.2" y1="266.6" x2="410.2" y2="279.8" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="272.5" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="414.0" y1="277.0" x2="414.0" y2="296.9" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="283.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="417.8" y1="270.8" x2="417.8" y2="288.1" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="276.8" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="421.6" y1="276.0" x2="421.6" y2="296.9" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="287.2" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="425.4" y1="285.5" x2="425.4" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="291.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="429.2" y1="278.6" x2="429.2" y2="301.7" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="289.1" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="432.9" y1="259.0" x2="432.9" y2="295.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="263.0" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="436.7" y1="255.5" x2="436.7" y2="285.6" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="259.9" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="440.5" y1="275.5" x2="440.5" y2="291.6" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="281.5" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="444.3" y1="257.8" x2="444.3" y2="285.6" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="263.5" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="448.1" y1="220.3" x2="448.1" y2="269.5" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="236.6" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="451.9" y1="225.4" x2="451.9" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="228.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="455.7" y1="205.7" x2="455.7" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="212.5" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="459.5" y1="198.6" x2="459.5" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="204.3" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="463.2" y1="222.2" x2="463.2" y2="241.6" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="226.3" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="467.0" y1="211.7" x2="467.0" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="218.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="470.8" y1="206.2" x2="470.8" y2="220.1" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="207.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="474.6" y1="184.6" x2="474.6" y2="211.9" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="191.8" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="478.4" y1="149.8" x2="478.4" y2="180.2" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="164.0" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="482.2" y1="114.0" x2="482.2" y2="160.1" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="130.4" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="486.0" y1="126.9" x2="486.0" y2="167.8" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="126.9" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="489.7" y1="100.7" x2="489.7" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="108.8" width="2.35" height="34.1" fill="var(--up)"/>
<line x1="493.5" y1="99.6" x2="493.5" y2="127.2" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="99.6" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="497.3" y1="107.9" x2="497.3" y2="169.4" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="113.1" width="2.35" height="44.9" fill="var(--down)"/>
<line x1="501.1" y1="145.6" x2="501.1" y2="175.4" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="152.2" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="504.9" y1="149.8" x2="504.9" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="157.7" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="508.7" y1="174.8" x2="508.7" y2="192.2" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="176.4" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="512.5" y1="180.4" x2="512.5" y2="209.8" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="180.7" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="516.2" y1="200.8" x2="516.2" y2="237.1" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="207.3" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="520.0" y1="213.3" x2="520.0" y2="267.0" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="216.5" width="2.35" height="47.5" fill="var(--down)"/>
<line x1="523.8" y1="255.5" x2="523.8" y2="271.3" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="260.0" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="527.6" y1="259.3" x2="527.6" y2="276.3" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="259.3" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="531.4" y1="233.9" x2="531.4" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="238.7" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="535.2" y1="231.7" x2="535.2" y2="246.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="235.5" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="539.0" y1="209.0" x2="539.0" y2="234.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="216.3" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="542.7" y1="205.8" x2="542.7" y2="225.8" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="210.9" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="546.5" y1="214.9" x2="546.5" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="217.2" width="2.35" height="17.5" fill="var(--down)"/>
<line x1="550.3" y1="211.5" x2="550.3" y2="226.7" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="212.2" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="554.1" y1="196.9" x2="554.1" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="202.4" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="557.9" y1="194.1" x2="557.9" y2="213.8" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="201.9" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="561.7" y1="202.7" x2="561.7" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="214.7" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="565.5" y1="212.2" x2="565.5" y2="240.2" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="214.4" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="569.3" y1="202.2" x2="569.3" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="205.4" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="573.0" y1="196.3" x2="573.0" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="203.2" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="576.8" y1="204.3" x2="576.8" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="208.9" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="580.6" y1="184.6" x2="580.6" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="190.2" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="584.4" y1="167.8" x2="584.4" y2="197.5" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="179.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="588.2" y1="150.3" x2="588.2" y2="169.3" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="164.0" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="592.0" y1="144.3" x2="592.0" y2="166.9" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="153.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="595.8" y1="152.2" x2="595.8" y2="175.1" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="159.6" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="599.5" y1="169.1" x2="599.5" y2="184.8" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="173.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="603.3" y1="170.0" x2="603.3" y2="199.7" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="175.4" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="607.1" y1="179.6" x2="607.1" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="184.2" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="610.9" y1="157.4" x2="610.9" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="172.6" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="614.7" y1="177.5" x2="614.7" y2="205.4" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="177.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="618.5" y1="179.4" x2="618.5" y2="219.4" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="183.2" width="2.35" height="33.5" fill="var(--down)"/>
<line x1="622.3" y1="204.5" x2="622.3" y2="216.6" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="208.6" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="626.0" y1="192.5" x2="626.0" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="194.6" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="629.8" y1="172.2" x2="629.8" y2="200.0" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="182.9" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="633.6" y1="192.2" x2="633.6" y2="213.0" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="195.1" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="637.4" y1="198.8" x2="637.4" y2="215.5" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="199.2" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="641.2" y1="187.2" x2="641.2" y2="207.4" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="201.3" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="645.0" y1="203.8" x2="645.0" y2="252.6" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="207.3" width="2.35" height="44.7" fill="var(--down)"/>
<line x1="648.8" y1="222.0" x2="648.8" y2="268.1" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="235.0" width="2.35" height="27.8" fill="var(--up)"/>
<line x1="652.5" y1="231.8" x2="652.5" y2="252.7" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="235.0" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="656.3" y1="245.9" x2="656.3" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="251.7" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="660.1" y1="238.3" x2="660.1" y2="257.5" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="239.3" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="663.9" y1="237.8" x2="663.9" y2="274.5" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="239.3" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="667.7" y1="260.5" x2="667.7" y2="278.2" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="260.5" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="671.5" y1="254.8" x2="671.5" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="257.5" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="675.3" y1="243.7" x2="675.3" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="252.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="679.1" y1="227.9" x2="679.1" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="228.9" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="682.8" y1="206.5" x2="682.8" y2="227.6" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="211.9" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="686.6" y1="207.7" x2="686.6" y2="227.4" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="208.1" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="690.4" y1="189.6" x2="690.4" y2="204.5" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="195.0" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="694.2" y1="182.7" x2="694.2" y2="204.9" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="186.4" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="698.0" y1="170.6" x2="698.0" y2="203.0" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="198.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="701.8" y1="172.0" x2="701.8" y2="198.5" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="180.1" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="705.6" y1="169.0" x2="705.6" y2="190.2" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="169.9" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="709.3" y1="192.2" x2="709.3" y2="215.2" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="193.8" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="713.1" y1="202.0" x2="713.1" y2="223.6" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="212.4" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="716.9" y1="177.6" x2="716.9" y2="216.6" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="178.0" width="2.35" height="36.1" fill="var(--up)"/>
<line x1="720.7" y1="154.7" x2="720.7" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="163.3" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="724.5" y1="148.2" x2="724.5" y2="161.4" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="149.4" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="728.3" y1="148.4" x2="728.3" y2="160.5" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="149.0" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="732.1" y1="121.2" x2="732.1" y2="151.1" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="126.9" width="2.35" height="23.4" fill="var(--up)"/>
<line x1="735.8" y1="121.0" x2="735.8" y2="150.7" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="129.5" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="739.6" y1="137.6" x2="739.6" y2="154.8" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="144.0" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="743.4" y1="148.1" x2="743.4" y2="160.6" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="149.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="747.2" y1="146.3" x2="747.2" y2="177.0" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="160.5" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="751.0" y1="141.8" x2="751.0" y2="170.9" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="165.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="754.8" y1="151.3" x2="754.8" y2="172.8" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="160.2" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="758.6" y1="165.5" x2="758.6" y2="194.1" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="167.5" width="2.35" height="25.0" fill="var(--down)"/>
<line x1="762.4" y1="175.3" x2="762.4" y2="204.1" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="177.9" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="766.1" y1="169.9" x2="766.1" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="178.0" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="769.9" y1="174.1" x2="769.9" y2="196.3" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="180.8" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="773.7" y1="159.2" x2="773.7" y2="176.7" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="174.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="777.5" y1="176.3" x2="777.5" y2="218.1" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="183.2" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="781.3" y1="123.2" x2="781.3" y2="204.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="139.7" width="2.35" height="64.2" fill="var(--up)"/>
<line x1="785.1" y1="141.6" x2="785.1" y2="160.4" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="144.1" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="788.9" y1="134.2" x2="788.9" y2="164.0" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="138.1" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="792.6" y1="150.6" x2="792.6" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="151.7" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="796.4" y1="140.3" x2="796.4" y2="157.0" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="146.2" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="800.2" y1="121.8" x2="800.2" y2="143.5" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="136.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="804.0" y1="99.4" x2="804.0" y2="131.4" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="117.2" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="807.8" y1="120.5" x2="807.8" y2="136.1" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="125.0" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="811.6" y1="121.5" x2="811.6" y2="146.0" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="125.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="815.4" y1="123.1" x2="815.4" y2="147.1" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="126.2" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="819.1" y1="128.2" x2="819.1" y2="143.7" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="131.4" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="822.9" y1="133.2" x2="822.9" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="139.2" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="826.7" y1="137.8" x2="826.7" y2="158.7" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="141.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="830.5" y1="125.6" x2="830.5" y2="142.4" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="128.1" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="834.3" y1="110.5" x2="834.3" y2="131.6" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="121.6" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="838.1" y1="123.2" x2="838.1" y2="137.6" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="131.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="841.9" y1="126.7" x2="841.9" y2="150.9" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="129.7" width="2.35" height="20.3" fill="var(--down)"/>
<line x1="845.6" y1="140.3" x2="845.6" y2="156.0" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="143.0" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="849.4" y1="131.4" x2="849.4" y2="152.0" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="132.6" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="853.2" y1="128.5" x2="853.2" y2="141.8" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="137.3" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="857.0" y1="127.6" x2="857.0" y2="140.6" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="133.9" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="860.8" y1="122.1" x2="860.8" y2="155.7" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="123.7" width="2.35" height="31.0" fill="var(--down)"/>
<line x1="864.6" y1="155.7" x2="864.6" y2="174.7" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="157.7" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="868.4" y1="156.7" x2="868.4" y2="179.4" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="157.4" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="872.2" y1="153.2" x2="872.2" y2="163.1" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="156.0" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="875.9" y1="160.2" x2="875.9" y2="169.1" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="162.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="879.7" y1="156.4" x2="879.7" y2="176.4" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="157.3" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="883.5" y1="173.4" x2="883.5" y2="183.2" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="175.7" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="887.3" y1="177.5" x2="887.3" y2="190.8" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="180.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="891.1" y1="169.9" x2="891.1" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="170.0" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="894.9" y1="159.2" x2="894.9" y2="171.2" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="165.6" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="898.7" y1="158.2" x2="898.7" y2="173.2" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="158.7" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="902.4" y1="154.4" x2="902.4" y2="165.8" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="159.3" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="906.2" y1="166.1" x2="906.2" y2="175.0" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="166.9" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="910.0" y1="151.0" x2="910.0" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="152.2" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="913.8" y1="141.2" x2="913.8" y2="158.5" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="142.5" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="917.6" y1="140.6" x2="917.6" y2="152.9" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="145.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="921.4" y1="141.6" x2="921.4" y2="153.8" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="144.7" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="925.2" y1="140.0" x2="925.2" y2="151.9" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="141.6" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="928.9" y1="138.3" x2="928.9" y2="150.0" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="140.2" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="932.7" y1="142.1" x2="932.7" y2="155.1" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="142.4" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="936.5" y1="129.5" x2="936.5" y2="148.2" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="134.3" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="940.3" y1="137.1" x2="940.3" y2="152.2" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="140.5" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="944.1" y1="132.3" x2="944.1" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="140.6" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="947.9" y1="137.8" x2="947.9" y2="166.9" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="138.0" width="2.35" height="27.9" fill="var(--down)"/>
<line x1="951.7" y1="157.7" x2="951.7" y2="170.9" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="162.0" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="955.5" y1="162.0" x2="955.5" y2="176.3" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="162.0" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="959.2" y1="150.9" x2="959.2" y2="171.9" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="157.6" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="963.0" y1="134.0" x2="963.0" y2="161.4" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="135.2" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="966.8" y1="127.3" x2="966.8" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="127.6" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="970.6" y1="121.9" x2="970.6" y2="138.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="124.4" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="974.4" y1="130.2" x2="974.4" y2="139.7" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="132.6" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="978.2" y1="129.5" x2="978.2" y2="145.7" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="133.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="982.0" y1="130.0" x2="982.0" y2="142.1" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="130.2" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="985.7" y1="130.0" x2="985.7" y2="139.7" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="134.0" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="989.5" y1="122.4" x2="989.5" y2="133.8" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="126.7" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="993.3" y1="116.7" x2="993.3" y2="133.9" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="124.4" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="997.1" y1="102.6" x2="997.1" y2="128.1" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="103.1" width="2.35" height="23.5" fill="var(--up)"/>
<line x1="1000.9" y1="93.0" x2="1000.9" y2="113.6" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="102.9" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="1004.7" y1="114.0" x2="1004.7" y2="126.6" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="120.3" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="1008.5" y1="117.8" x2="1008.5" y2="129.5" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="121.9" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="1012.2" y1="116.1" x2="1012.2" y2="129.7" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="120.6" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="1016.0" y1="125.4" x2="1016.0" y2="142.2" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="128.2" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="1019.8" y1="128.2" x2="1019.8" y2="147.6" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="131.7" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="1023.6" y1="122.2" x2="1023.6" y2="143.5" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="124.0" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="1027.4" y1="108.3" x2="1027.4" y2="126.0" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="111.4" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="1031.2" y1="102.8" x2="1031.2" y2="115.2" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="109.3" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="1035.0" y1="93.6" x2="1035.0" y2="109.9" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="98.1" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="1038.7" y1="80.7" x2="1038.7" y2="109.3" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="81.6" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="1042.5" y1="86.3" x2="1042.5" y2="98.8" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="90.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1046.3" y1="81.9" x2="1046.3" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="83.0" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="1050.1" y1="74.1" x2="1050.1" y2="95.0" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="82.5" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="60" y1="154.1" x2="1052" y2="154.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="148.1" font-size="11.5" fill="var(--support)" font-weight="600">4.78% S1</text>
<text x="1058" y="160.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="183.5" x2="1052" y2="183.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="177.5" font-size="11.5" fill="var(--support)" font-weight="600">4.58% S2</text>
<text x="1058" y="189.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="220.4" x2="1052" y2="220.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.4" font-size="11.5" fill="var(--support)" font-weight="600">4.33% S3</text>
<text x="1058" y="226.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="93.4" r="3" fill="var(--ink)"/>
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

- **상승**: 장기 재정건전성 우려, 장기 인플레이션 기대 확대 신호로 흔히 해석된다 — 단기물보다 당장의 연준 정책보다는 먼 미래 기대에 더 민감하다.
- **하락**: 장기 성장·인플레이션 기대 둔화, 안전자산 수요 확대 신호로 흔히 해석된다.
- **왜 이런 신호로 읽히나**: 30년물 수익률은 기대가설(향후 30년간 평균 단기금리 경로)보다 **기간 프리미엄**(만기가 길어질수록 투자자가 추가로 요구하는 보상) 비중이 커서, 당장의 통화정책보다 장기 국채 발행량(재정 전망)·장기 성장·인플레 기대에 더 민감하다. 연기금·보험사 등 장기부채를 지닌 기관의 구조적 매수 수요도 가격에 영향을 준다.
- 이 레포 밸류에이션(DCF 무위험이자율)의 표준 근거로 쓰지 않는다 — 표준은 10년물이다. 이 문서는 수익률곡선 형태를 보기 위한 보조 자료다.

---

## 관련 문서

- [13주 단기금리](./short_rate.md)
- [미국 5년물 국채금리](./treasury_5y.md)
- [미국 10년물 국채금리](./treasury_10y.md) — DCF 무위험이자율의 표준 근거
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — "수익률곡선" 절
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Treasury Yield 30 Years (^TYX)](https://finance.yahoo.com/quote/%5ETYX/)
- [미 재무부 금리 (원출처)](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
