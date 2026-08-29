# 미국 30년물 국채금리

!!! note ""
    최근 5년간 미국 30년물 국채 수익률(`^TYX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 13주물 국채금리·10년물 국채금리와 함께 보면 **수익률곡선에서 가장 만기가 긴 구간**까지 채워서 볼 수 있다.

    **왜 따로 다루나**: 30년물은 가장 먼 미래의 성장·물가 기대와 기간 프리미엄(만기가 길어질수록 투자자가 추가로 요구하는 보상)을 반영한다. 그래서 단기물과 달리 연준의 당장 정책보다는 장기적인 재정건전성이나 인플레이션 기대에 더 민감하게 움직이는 편이다.

---

## 1. 차트 — 최근 5년 주봉

<div class="tyx-chart">
<style>
.tyx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .tyx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-24 · 마지막 종가 5.19% (2026-08-24) · 단위 %</text>
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
<line x1="61.9" y1="567.0" x2="61.9" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="568.6" width="2.36" height="2.5" fill="var(--up)"/>
<line x1="65.7" y1="560.5" x2="65.7" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="64.52" y="563.3" width="2.36" height="6.6" fill="var(--down)"/>
<line x1="69.5" y1="568.6" x2="69.5" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="68.32" y="571.9" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="73.3" y1="561.4" x2="73.3" y2="585.1" stroke="var(--up)" class="wick"/>
<rect x="72.12" y="562.0" width="2.36" height="21.0" fill="var(--up)"/>
<line x1="77.1" y1="545.2" x2="77.1" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="75.93" y="551.8" width="2.36" height="6.1" fill="var(--up)"/>
<line x1="80.9" y1="534.4" x2="80.9" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="79.73" y="536.6" width="2.36" height="14.6" fill="var(--up)"/>
<line x1="84.7" y1="536.0" x2="84.7" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="83.53" y="536.0" width="2.36" height="16.8" fill="var(--down)"/>
<line x1="88.5" y1="538.3" x2="88.5" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="87.33" y="546.9" width="2.36" height="8.3" fill="var(--up)"/>
<line x1="92.3" y1="542.4" x2="92.3" y2="571.3" stroke="var(--down)" class="wick"/>
<rect x="91.13" y="545.5" width="2.36" height="23.2" fill="var(--down)"/>
<line x1="96.1" y1="556.6" x2="96.1" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="94.93" y="563.7" width="2.36" height="13.2" fill="var(--down)"/>
<line x1="99.9" y1="562.7" x2="99.9" y2="590.2" stroke="var(--up)" class="wick"/>
<rect x="98.73" y="566.8" width="2.36" height="7.0" fill="var(--up)"/>
<line x1="103.7" y1="553.1" x2="103.7" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="102.53" y="570.2" width="2.36" height="3.7" fill="var(--down)"/>
<line x1="107.5" y1="555.0" x2="107.5" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="106.33" y="569.0" width="2.36" height="16.5" fill="var(--down)"/>
<line x1="111.3" y1="573.4" x2="111.3" y2="607.3" stroke="var(--down)" class="wick"/>
<rect x="110.13" y="576.2" width="2.36" height="31.1" fill="var(--down)"/>
<line x1="115.1" y1="575.7" x2="115.1" y2="605.4" stroke="var(--up)" class="wick"/>
<rect x="113.93" y="577.2" width="2.36" height="24.3" fill="var(--up)"/>
<line x1="118.9" y1="574.1" x2="118.9" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="117.73" y="581.1" width="2.36" height="5.7" fill="var(--down)"/>
<line x1="122.7" y1="570.9" x2="122.7" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="121.53" y="574.1" width="2.36" height="13.6" fill="var(--up)"/>
<line x1="126.5" y1="564.5" x2="126.5" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="125.34" y="574.1" width="2.36" height="1.6" fill="var(--up)"/>
<line x1="130.3" y1="538.3" x2="130.3" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="129.14" y="543.0" width="2.36" height="29.2" fill="var(--up)"/>
<line x1="134.1" y1="538.2" x2="134.1" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="132.94" y="542.1" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="137.9" y1="532.2" x2="137.9" y2="552.6" stroke="var(--down)" class="wick"/>
<rect x="136.74" y="538.9" width="2.36" height="12.0" fill="var(--down)"/>
<line x1="141.7" y1="534.8" x2="141.7" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="140.54" y="548.1" width="2.36" height="4.2" fill="var(--up)"/>
<line x1="145.5" y1="525.6" x2="145.5" y2="551.3" stroke="var(--up)" class="wick"/>
<rect x="144.34" y="526.2" width="2.36" height="18.3" fill="var(--up)"/>
<line x1="149.3" y1="508.6" x2="149.3" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="148.14" y="522.7" width="2.36" height="5.0" fill="var(--up)"/>
<line x1="153.1" y1="503.7" x2="153.1" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="151.94" y="521.9" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="156.9" y1="514.6" x2="156.9" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="155.74" y="517.0" width="2.36" height="5.4" fill="var(--up)"/>
<line x1="160.7" y1="521.1" x2="160.7" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="159.54" y="524.6" width="2.36" height="13.6" fill="var(--down)"/>
<line x1="164.5" y1="499.6" x2="164.5" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="163.34" y="507.0" width="2.36" height="26.0" fill="var(--up)"/>
<line x1="168.3" y1="481.2" x2="168.3" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="167.14" y="498.0" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="172.1" y1="466.1" x2="172.1" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="170.94" y="472.1" width="2.36" height="20.5" fill="var(--up)"/>
<line x1="175.9" y1="474.9" x2="175.9" y2="499.6" stroke="var(--down)" class="wick"/>
<rect x="174.75" y="476.9" width="2.36" height="21.3" fill="var(--down)"/>
<line x1="179.7" y1="449.2" x2="179.7" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="178.55" y="451.2" width="2.36" height="39.3" fill="var(--up)"/>
<line x1="183.5" y1="424.5" x2="183.5" y2="450.5" stroke="var(--up)" class="wick"/>
<rect x="182.35" y="425.9" width="2.36" height="18.7" fill="var(--up)"/>
<line x1="187.3" y1="411.4" x2="187.3" y2="433.8" stroke="var(--down)" class="wick"/>
<rect x="186.15" y="421.1" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="191.1" y1="415.5" x2="191.1" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="189.95" y="421.8" width="2.36" height="6.1" fill="var(--up)"/>
<line x1="194.9" y1="381.5" x2="194.9" y2="418.8" stroke="var(--up)" class="wick"/>
<rect x="193.75" y="381.8" width="2.36" height="33.3" fill="var(--up)"/>
<line x1="198.7" y1="373.6" x2="198.7" y2="417.9" stroke="var(--down)" class="wick"/>
<rect x="197.55" y="374.0" width="2.36" height="26.5" fill="var(--down)"/>
<line x1="202.5" y1="384.6" x2="202.5" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="201.35" y="399.3" width="2.36" height="15.3" fill="var(--down)"/>
<line x1="206.3" y1="403.6" x2="206.3" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="205.15" y="409.3" width="2.36" height="8.9" fill="var(--down)"/>
<line x1="210.1" y1="391.0" x2="210.1" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="208.95" y="397.4" width="2.36" height="12.9" fill="var(--up)"/>
<line x1="213.9" y1="379.3" x2="213.9" y2="399.8" stroke="var(--up)" class="wick"/>
<rect x="212.75" y="385.4" width="2.36" height="9.6" fill="var(--up)"/>
<line x1="217.7" y1="345.1" x2="217.7" y2="378.1" stroke="var(--up)" class="wick"/>
<rect x="216.55" y="371.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="221.5" y1="356.3" x2="221.5" y2="392.6" stroke="var(--down)" class="wick"/>
<rect x="220.35" y="362.2" width="2.36" height="14.3" fill="var(--down)"/>
<line x1="225.3" y1="361.0" x2="225.3" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="224.16" y="368.8" width="2.36" height="28.4" fill="var(--down)"/>
<line x1="229.1" y1="373.4" x2="229.1" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="227.96" y="374.8" width="2.36" height="24.8" fill="var(--up)"/>
<line x1="232.9" y1="380.3" x2="232.9" y2="405.0" stroke="var(--down)" class="wick"/>
<rect x="231.76" y="380.9" width="2.36" height="19.4" fill="var(--down)"/>
<line x1="236.7" y1="383.7" x2="236.7" y2="421.1" stroke="var(--down)" class="wick"/>
<rect x="235.56" y="396.0" width="2.36" height="18.4" fill="var(--down)"/>
<line x1="240.5" y1="400.3" x2="240.5" y2="421.1" stroke="var(--down)" class="wick"/>
<rect x="239.36" y="406.8" width="2.36" height="11.1" fill="var(--down)"/>
<line x1="244.3" y1="398.6" x2="244.3" y2="435.3" stroke="var(--up)" class="wick"/>
<rect x="243.16" y="404.6" width="2.36" height="6.1" fill="var(--up)"/>
<line x1="248.1" y1="386.5" x2="248.1" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="246.96" y="396.8" width="2.36" height="13.2" fill="var(--up)"/>
<line x1="251.9" y1="379.6" x2="251.9" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="250.76" y="381.2" width="2.36" height="20.6" fill="var(--up)"/>
<line x1="255.7" y1="365.8" x2="255.7" y2="387.2" stroke="var(--down)" class="wick"/>
<rect x="254.56" y="381.5" width="2.36" height="2.6" fill="var(--down)"/>
<line x1="259.5" y1="353.9" x2="259.5" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="363.8" width="2.36" height="15.2" fill="var(--up)"/>
<line x1="263.3" y1="342.3" x2="263.3" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="262.16" y="347.4" width="2.36" height="9.1" fill="var(--up)"/>
<line x1="267.1" y1="330.5" x2="267.1" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="265.96" y="338.2" width="2.36" height="15.1" fill="var(--up)"/>
<line x1="270.9" y1="315.1" x2="270.9" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="269.76" y="324.6" width="2.36" height="7.3" fill="var(--up)"/>
<line x1="274.7" y1="290.3" x2="274.7" y2="324.6" stroke="var(--up)" class="wick"/>
<rect x="273.57" y="302.3" width="2.36" height="13.6" fill="var(--up)"/>
<line x1="278.5" y1="285.9" x2="278.5" y2="320.7" stroke="var(--up)" class="wick"/>
<rect x="277.37" y="291.2" width="2.36" height="21.5" fill="var(--up)"/>
<line x1="282.3" y1="266.2" x2="282.3" y2="290.4" stroke="var(--up)" class="wick"/>
<rect x="281.17" y="271.1" width="2.36" height="19.0" fill="var(--up)"/>
<line x1="286.1" y1="211.9" x2="286.1" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="284.97" y="223.3" width="2.36" height="52.5" fill="var(--up)"/>
<line x1="289.9" y1="205.8" x2="289.9" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="288.77" y="222.0" width="2.36" height="27.0" fill="var(--down)"/>
<line x1="293.7" y1="228.9" x2="293.7" y2="260.0" stroke="var(--up)" class="wick"/>
<rect x="292.57" y="232.0" width="2.36" height="17.0" fill="var(--up)"/>
<line x1="297.5" y1="219.1" x2="297.5" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="296.37" y="236.2" width="2.36" height="23.2" fill="var(--down)"/>
<line x1="301.3" y1="255.2" x2="301.3" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="300.17" y="257.3" width="2.36" height="21.3" fill="var(--down)"/>
<line x1="305.1" y1="280.3" x2="305.1" y2="306.4" stroke="var(--down)" class="wick"/>
<rect x="303.97" y="282.2" width="2.36" height="22.1" fill="var(--down)"/>
<line x1="309.0" y1="290.3" x2="309.0" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="307.77" y="309.1" width="2.36" height="22.8" fill="var(--down)"/>
<line x1="312.8" y1="319.1" x2="312.8" y2="353.7" stroke="var(--down)" class="wick"/>
<rect x="311.57" y="331.8" width="2.36" height="2.0" fill="var(--down)"/>
<line x1="316.6" y1="326.7" x2="316.6" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="315.37" y="336.2" width="2.36" height="2.6" fill="var(--up)"/>
<line x1="320.4" y1="292.9" x2="320.4" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="319.17" y="293.2" width="2.36" height="29.1" fill="var(--up)"/>
<line x1="324.2" y1="269.4" x2="324.2" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="322.98" y="271.6" width="2.36" height="15.5" fill="var(--up)"/>
<line x1="328.0" y1="280.8" x2="328.0" y2="315.1" stroke="var(--down)" class="wick"/>
<rect x="326.78" y="288.1" width="2.36" height="24.8" fill="var(--down)"/>
<line x1="331.8" y1="300.8" x2="331.8" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="308.3" width="2.36" height="14.8" fill="var(--down)"/>
<line x1="335.6" y1="312.4" x2="335.6" y2="337.8" stroke="var(--down)" class="wick"/>
<rect x="334.38" y="313.8" width="2.36" height="4.4" fill="var(--down)"/>
<line x1="339.4" y1="309.1" x2="339.4" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="338.18" y="314.5" width="2.36" height="7.0" fill="var(--down)"/>
<line x1="343.2" y1="314.1" x2="343.2" y2="341.3" stroke="var(--down)" class="wick"/>
<rect x="341.98" y="317.6" width="2.36" height="4.7" fill="var(--down)"/>
<line x1="347.0" y1="291.7" x2="347.0" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="345.78" y="293.2" width="2.36" height="24.7" fill="var(--up)"/>
<line x1="350.8" y1="274.9" x2="350.8" y2="308.1" stroke="var(--up)" class="wick"/>
<rect x="349.58" y="284.3" width="2.36" height="11.7" fill="var(--up)"/>
<line x1="354.6" y1="270.7" x2="354.6" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="353.38" y="277.0" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="358.4" y1="261.1" x2="358.4" y2="284.9" stroke="var(--down)" class="wick"/>
<rect x="357.18" y="272.7" width="2.36" height="11.7" fill="var(--down)"/>
<line x1="362.2" y1="277.9" x2="362.2" y2="314.7" stroke="var(--down)" class="wick"/>
<rect x="360.98" y="292.6" width="2.36" height="19.1" fill="var(--down)"/>
<line x1="366.0" y1="297.6" x2="366.0" y2="337.2" stroke="var(--up)" class="wick"/>
<rect x="364.78" y="326.7" width="2.36" height="2.3" fill="var(--up)"/>
<line x1="369.8" y1="301.5" x2="369.8" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="368.58" y="320.0" width="2.36" height="2.9" fill="var(--up)"/>
<line x1="373.6" y1="295.0" x2="373.6" y2="313.5" stroke="var(--down)" class="wick"/>
<rect x="372.38" y="310.7" width="2.36" height="2.6" fill="var(--down)"/>
<line x1="377.4" y1="311.6" x2="377.4" y2="337.1" stroke="var(--down)" class="wick"/>
<rect x="376.19" y="312.4" width="2.36" height="22.8" fill="var(--down)"/>
<line x1="381.2" y1="303.9" x2="381.2" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="379.99" y="306.1" width="2.36" height="22.7" fill="var(--up)"/>
<line x1="385.0" y1="292.3" x2="385.0" y2="308.3" stroke="var(--up)" class="wick"/>
<rect x="383.79" y="300.4" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="388.8" y1="301.8" x2="388.8" y2="322.0" stroke="var(--down)" class="wick"/>
<rect x="387.59" y="303.9" width="2.36" height="11.1" fill="var(--down)"/>
<line x1="392.6" y1="294.1" x2="392.6" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="391.39" y="302.7" width="2.36" height="3.2" fill="var(--up)"/>
<line x1="396.4" y1="289.1" x2="396.4" y2="309.3" stroke="var(--down)" class="wick"/>
<rect x="395.19" y="296.7" width="2.36" height="3.8" fill="var(--down)"/>
<line x1="400.2" y1="273.8" x2="400.2" y2="297.2" stroke="var(--up)" class="wick"/>
<rect x="398.99" y="275.5" width="2.36" height="18.4" fill="var(--up)"/>
<line x1="404.0" y1="266.6" x2="404.0" y2="279.8" stroke="var(--up)" class="wick"/>
<rect x="402.79" y="272.5" width="2.36" height="3.1" fill="var(--up)"/>
<line x1="407.8" y1="277.0" x2="407.8" y2="296.9" stroke="var(--down)" class="wick"/>
<rect x="406.59" y="283.6" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="411.6" y1="270.8" x2="411.6" y2="288.1" stroke="var(--down)" class="wick"/>
<rect x="410.39" y="276.8" width="2.36" height="7.6" fill="var(--down)"/>
<line x1="415.4" y1="276.0" x2="415.4" y2="296.9" stroke="var(--down)" class="wick"/>
<rect x="414.19" y="287.2" width="2.36" height="1.9" fill="var(--down)"/>
<line x1="419.2" y1="285.5" x2="419.2" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="417.99" y="291.9" width="2.36" height="2.2" fill="var(--down)"/>
<line x1="423.0" y1="278.6" x2="423.0" y2="301.7" stroke="var(--up)" class="wick"/>
<rect x="421.79" y="289.1" width="2.36" height="9.6" fill="var(--up)"/>
<line x1="426.8" y1="259.0" x2="426.8" y2="295.4" stroke="var(--up)" class="wick"/>
<rect x="425.60" y="263.0" width="2.36" height="22.7" fill="var(--up)"/>
<line x1="430.6" y1="255.5" x2="430.6" y2="285.6" stroke="var(--down)" class="wick"/>
<rect x="429.40" y="259.9" width="2.36" height="19.3" fill="var(--down)"/>
<line x1="434.4" y1="275.5" x2="434.4" y2="291.6" stroke="var(--up)" class="wick"/>
<rect x="433.20" y="281.5" width="2.36" height="1.3" fill="var(--up)"/>
<line x1="438.2" y1="257.8" x2="438.2" y2="285.6" stroke="var(--up)" class="wick"/>
<rect x="437.00" y="263.5" width="2.36" height="21.3" fill="var(--up)"/>
<line x1="442.0" y1="220.3" x2="442.0" y2="269.5" stroke="var(--up)" class="wick"/>
<rect x="440.80" y="236.6" width="2.36" height="27.9" fill="var(--up)"/>
<line x1="445.8" y1="225.4" x2="445.8" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="444.60" y="228.2" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="449.6" y1="205.7" x2="449.6" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="448.40" y="212.5" width="2.36" height="15.8" fill="var(--up)"/>
<line x1="453.4" y1="198.6" x2="453.4" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="452.20" y="204.3" width="2.36" height="20.6" fill="var(--down)"/>
<line x1="457.2" y1="222.2" x2="457.2" y2="241.6" stroke="var(--up)" class="wick"/>
<rect x="456.00" y="226.3" width="2.36" height="2.6" fill="var(--up)"/>
<line x1="461.0" y1="211.7" x2="461.0" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="459.80" y="218.5" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="464.8" y1="206.2" x2="464.8" y2="220.1" stroke="var(--up)" class="wick"/>
<rect x="463.60" y="207.9" width="2.36" height="5.4" fill="var(--up)"/>
<line x1="468.6" y1="184.6" x2="468.6" y2="211.9" stroke="var(--up)" class="wick"/>
<rect x="467.40" y="191.8" width="2.36" height="15.8" fill="var(--up)"/>
<line x1="472.4" y1="149.8" x2="472.4" y2="180.2" stroke="var(--up)" class="wick"/>
<rect x="471.20" y="164.0" width="2.36" height="14.9" fill="var(--up)"/>
<line x1="476.2" y1="114.0" x2="476.2" y2="160.1" stroke="var(--up)" class="wick"/>
<rect x="475.01" y="130.4" width="2.36" height="27.9" fill="var(--up)"/>
<line x1="480.0" y1="126.9" x2="480.0" y2="167.8" stroke="var(--down)" class="wick"/>
<rect x="478.81" y="126.9" width="2.36" height="27.0" fill="var(--down)"/>
<line x1="483.8" y1="100.7" x2="483.8" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="482.61" y="108.8" width="2.36" height="34.1" fill="var(--up)"/>
<line x1="487.6" y1="99.6" x2="487.6" y2="127.2" stroke="var(--down)" class="wick"/>
<rect x="486.41" y="99.6" width="2.36" height="18.9" fill="var(--down)"/>
<line x1="491.4" y1="107.9" x2="491.4" y2="169.4" stroke="var(--down)" class="wick"/>
<rect x="490.21" y="113.1" width="2.36" height="44.9" fill="var(--down)"/>
<line x1="495.2" y1="145.6" x2="495.2" y2="175.4" stroke="var(--down)" class="wick"/>
<rect x="494.01" y="152.2" width="2.36" height="8.6" fill="var(--down)"/>
<line x1="499.0" y1="149.8" x2="499.0" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="497.81" y="157.7" width="2.36" height="22.9" fill="var(--down)"/>
<line x1="502.8" y1="174.8" x2="502.8" y2="192.2" stroke="var(--down)" class="wick"/>
<rect x="501.61" y="176.4" width="2.36" height="3.4" fill="var(--down)"/>
<line x1="506.6" y1="180.4" x2="506.6" y2="209.8" stroke="var(--down)" class="wick"/>
<rect x="505.41" y="180.7" width="2.36" height="26.2" fill="var(--down)"/>
<line x1="510.4" y1="200.8" x2="510.4" y2="237.1" stroke="var(--down)" class="wick"/>
<rect x="509.21" y="207.3" width="2.36" height="13.2" fill="var(--down)"/>
<line x1="514.2" y1="213.3" x2="514.2" y2="267.0" stroke="var(--down)" class="wick"/>
<rect x="513.01" y="216.5" width="2.36" height="47.5" fill="var(--down)"/>
<line x1="518.0" y1="255.5" x2="518.0" y2="271.3" stroke="var(--up)" class="wick"/>
<rect x="516.81" y="260.0" width="2.36" height="3.9" fill="var(--up)"/>
<line x1="521.8" y1="259.3" x2="521.8" y2="276.3" stroke="var(--down)" class="wick"/>
<rect x="520.61" y="259.3" width="2.36" height="5.8" fill="var(--down)"/>
<line x1="525.6" y1="233.9" x2="525.6" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="524.42" y="238.7" width="2.36" height="12.3" fill="var(--up)"/>
<line x1="529.4" y1="231.7" x2="529.4" y2="246.9" stroke="var(--down)" class="wick"/>
<rect x="528.22" y="235.5" width="2.36" height="3.7" fill="var(--down)"/>
<line x1="533.2" y1="209.0" x2="533.2" y2="234.2" stroke="var(--up)" class="wick"/>
<rect x="532.02" y="216.3" width="2.36" height="17.4" fill="var(--up)"/>
<line x1="537.0" y1="205.8" x2="537.0" y2="225.8" stroke="var(--up)" class="wick"/>
<rect x="535.82" y="210.9" width="2.36" height="11.5" fill="var(--up)"/>
<line x1="540.8" y1="214.9" x2="540.8" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="539.62" y="217.2" width="2.36" height="17.5" fill="var(--down)"/>
<line x1="544.6" y1="211.5" x2="544.6" y2="226.7" stroke="var(--up)" class="wick"/>
<rect x="543.42" y="212.2" width="2.36" height="12.3" fill="var(--up)"/>
<line x1="548.4" y1="196.9" x2="548.4" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="547.22" y="202.4" width="2.36" height="13.3" fill="var(--up)"/>
<line x1="552.2" y1="194.1" x2="552.2" y2="213.8" stroke="var(--down)" class="wick"/>
<rect x="551.02" y="201.9" width="2.36" height="10.5" fill="var(--down)"/>
<line x1="556.0" y1="202.7" x2="556.0" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="554.82" y="214.7" width="2.36" height="5.6" fill="var(--down)"/>
<line x1="559.8" y1="212.2" x2="559.8" y2="240.2" stroke="var(--down)" class="wick"/>
<rect x="558.62" y="214.4" width="2.36" height="15.2" fill="var(--down)"/>
<line x1="563.6" y1="202.2" x2="563.6" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="562.42" y="205.4" width="2.36" height="26.3" fill="var(--up)"/>
<line x1="567.4" y1="196.3" x2="567.4" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="566.22" y="203.2" width="2.36" height="7.5" fill="var(--down)"/>
<line x1="571.2" y1="204.3" x2="571.2" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="570.02" y="208.9" width="2.36" height="8.0" fill="var(--down)"/>
<line x1="575.0" y1="184.6" x2="575.0" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="573.83" y="190.2" width="2.36" height="20.5" fill="var(--up)"/>
<line x1="578.8" y1="167.8" x2="578.8" y2="197.5" stroke="var(--up)" class="wick"/>
<rect x="577.63" y="179.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="582.6" y1="150.3" x2="582.6" y2="169.3" stroke="var(--up)" class="wick"/>
<rect x="581.43" y="164.0" width="2.36" height="4.5" fill="var(--up)"/>
<line x1="586.4" y1="144.3" x2="586.4" y2="166.9" stroke="var(--up)" class="wick"/>
<rect x="585.23" y="153.8" width="2.36" height="5.1" fill="var(--up)"/>
<line x1="590.2" y1="152.2" x2="590.2" y2="175.1" stroke="var(--down)" class="wick"/>
<rect x="589.03" y="159.6" width="2.36" height="11.7" fill="var(--down)"/>
<line x1="594.0" y1="169.1" x2="594.0" y2="184.8" stroke="var(--up)" class="wick"/>
<rect x="592.83" y="173.5" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="597.8" y1="170.0" x2="597.8" y2="199.7" stroke="var(--down)" class="wick"/>
<rect x="596.63" y="175.4" width="2.36" height="10.7" fill="var(--down)"/>
<line x1="601.6" y1="179.6" x2="601.6" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="600.43" y="184.2" width="2.36" height="1.8" fill="var(--up)"/>
<line x1="605.4" y1="157.4" x2="605.4" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="604.23" y="172.6" width="2.36" height="12.1" fill="var(--up)"/>
<line x1="609.2" y1="177.5" x2="609.2" y2="205.4" stroke="var(--down)" class="wick"/>
<rect x="608.03" y="177.5" width="2.36" height="10.4" fill="var(--down)"/>
<line x1="613.0" y1="179.4" x2="613.0" y2="219.4" stroke="var(--down)" class="wick"/>
<rect x="611.83" y="183.2" width="2.36" height="33.5" fill="var(--down)"/>
<line x1="616.8" y1="204.5" x2="616.8" y2="216.6" stroke="var(--down)" class="wick"/>
<rect x="615.63" y="208.6" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="620.6" y1="192.5" x2="620.6" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="619.43" y="194.6" width="2.36" height="12.6" fill="var(--up)"/>
<line x1="624.4" y1="172.2" x2="624.4" y2="200.0" stroke="var(--down)" class="wick"/>
<rect x="623.24" y="182.9" width="2.36" height="16.7" fill="var(--down)"/>
<line x1="628.2" y1="192.2" x2="628.2" y2="213.0" stroke="var(--down)" class="wick"/>
<rect x="627.04" y="195.1" width="2.36" height="14.0" fill="var(--down)"/>
<line x1="632.0" y1="198.8" x2="632.0" y2="215.5" stroke="var(--down)" class="wick"/>
<rect x="630.84" y="199.2" width="2.36" height="2.9" fill="var(--down)"/>
<line x1="635.8" y1="187.2" x2="635.8" y2="207.4" stroke="var(--up)" class="wick"/>
<rect x="634.64" y="201.3" width="2.36" height="4.5" fill="var(--up)"/>
<line x1="639.6" y1="203.8" x2="639.6" y2="252.6" stroke="var(--down)" class="wick"/>
<rect x="638.44" y="207.3" width="2.36" height="44.7" fill="var(--down)"/>
<line x1="643.4" y1="222.0" x2="643.4" y2="268.1" stroke="var(--up)" class="wick"/>
<rect x="642.24" y="235.0" width="2.36" height="27.8" fill="var(--up)"/>
<line x1="647.2" y1="231.8" x2="647.2" y2="252.7" stroke="var(--down)" class="wick"/>
<rect x="646.04" y="235.0" width="2.36" height="11.1" fill="var(--down)"/>
<line x1="651.0" y1="245.9" x2="651.0" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="649.84" y="251.7" width="2.36" height="1.3" fill="var(--down)"/>
<line x1="654.8" y1="238.3" x2="654.8" y2="257.5" stroke="var(--up)" class="wick"/>
<rect x="653.64" y="239.3" width="2.36" height="13.7" fill="var(--up)"/>
<line x1="658.6" y1="237.8" x2="658.6" y2="274.5" stroke="var(--down)" class="wick"/>
<rect x="657.44" y="239.3" width="2.36" height="25.7" fill="var(--down)"/>
<line x1="662.4" y1="260.5" x2="662.4" y2="278.2" stroke="var(--down)" class="wick"/>
<rect x="661.24" y="260.5" width="2.36" height="10.8" fill="var(--down)"/>
<line x1="666.2" y1="254.8" x2="666.2" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="665.04" y="257.5" width="2.36" height="15.3" fill="var(--up)"/>
<line x1="670.0" y1="243.7" x2="670.0" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="668.84" y="252.4" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="673.8" y1="227.9" x2="673.8" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="672.65" y="228.9" width="2.36" height="19.4" fill="var(--up)"/>
<line x1="677.6" y1="206.5" x2="677.6" y2="227.6" stroke="var(--up)" class="wick"/>
<rect x="676.45" y="211.9" width="2.36" height="15.6" fill="var(--up)"/>
<line x1="681.4" y1="207.7" x2="681.4" y2="227.4" stroke="var(--down)" class="wick"/>
<rect x="680.25" y="208.1" width="2.36" height="4.2" fill="var(--down)"/>
<line x1="685.2" y1="189.6" x2="685.2" y2="204.5" stroke="var(--up)" class="wick"/>
<rect x="684.05" y="195.0" width="2.36" height="7.6" fill="var(--up)"/>
<line x1="689.0" y1="182.7" x2="689.0" y2="204.9" stroke="var(--up)" class="wick"/>
<rect x="687.85" y="186.4" width="2.36" height="7.0" fill="var(--up)"/>
<line x1="692.8" y1="170.6" x2="692.8" y2="203.0" stroke="var(--up)" class="wick"/>
<rect x="691.65" y="198.2" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="696.6" y1="172.0" x2="696.6" y2="198.5" stroke="var(--up)" class="wick"/>
<rect x="695.45" y="180.1" width="2.36" height="18.4" fill="var(--up)"/>
<line x1="700.4" y1="169.0" x2="700.4" y2="190.2" stroke="var(--down)" class="wick"/>
<rect x="699.25" y="169.9" width="2.36" height="11.1" fill="var(--down)"/>
<line x1="704.2" y1="192.2" x2="704.2" y2="215.2" stroke="var(--down)" class="wick"/>
<rect x="703.05" y="193.8" width="2.36" height="20.6" fill="var(--down)"/>
<line x1="708.0" y1="202.0" x2="708.0" y2="223.6" stroke="var(--down)" class="wick"/>
<rect x="706.85" y="212.4" width="2.36" height="7.2" fill="var(--down)"/>
<line x1="711.8" y1="177.6" x2="711.8" y2="216.6" stroke="var(--up)" class="wick"/>
<rect x="710.65" y="178.0" width="2.36" height="36.1" fill="var(--up)"/>
<line x1="715.6" y1="154.7" x2="715.6" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="714.45" y="163.3" width="2.36" height="19.6" fill="var(--up)"/>
<line x1="719.4" y1="148.2" x2="719.4" y2="161.4" stroke="var(--up)" class="wick"/>
<rect x="718.25" y="149.4" width="2.36" height="9.4" fill="var(--up)"/>
<line x1="723.2" y1="148.4" x2="723.2" y2="160.5" stroke="var(--up)" class="wick"/>
<rect x="722.06" y="149.0" width="2.36" height="5.0" fill="var(--up)"/>
<line x1="727.0" y1="121.2" x2="727.0" y2="151.1" stroke="var(--up)" class="wick"/>
<rect x="725.86" y="126.9" width="2.36" height="23.4" fill="var(--up)"/>
<line x1="730.8" y1="121.0" x2="730.8" y2="150.7" stroke="var(--down)" class="wick"/>
<rect x="729.66" y="129.5" width="2.36" height="14.9" fill="var(--down)"/>
<line x1="734.6" y1="137.6" x2="734.6" y2="154.8" stroke="var(--up)" class="wick"/>
<rect x="733.46" y="144.0" width="2.36" height="6.6" fill="var(--up)"/>
<line x1="738.4" y1="148.1" x2="738.4" y2="160.6" stroke="var(--up)" class="wick"/>
<rect x="737.26" y="149.1" width="2.36" height="6.3" fill="var(--up)"/>
<line x1="742.2" y1="146.3" x2="742.2" y2="177.0" stroke="var(--down)" class="wick"/>
<rect x="741.06" y="160.5" width="2.36" height="6.6" fill="var(--down)"/>
<line x1="746.0" y1="141.8" x2="746.0" y2="170.9" stroke="var(--down)" class="wick"/>
<rect x="744.86" y="165.0" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="749.8" y1="151.3" x2="749.8" y2="172.8" stroke="var(--down)" class="wick"/>
<rect x="748.66" y="160.2" width="2.36" height="9.9" fill="var(--down)"/>
<line x1="753.6" y1="165.5" x2="753.6" y2="194.1" stroke="var(--down)" class="wick"/>
<rect x="752.46" y="167.5" width="2.36" height="25.0" fill="var(--down)"/>
<line x1="757.4" y1="175.3" x2="757.4" y2="204.1" stroke="var(--up)" class="wick"/>
<rect x="756.26" y="177.9" width="2.36" height="11.8" fill="var(--up)"/>
<line x1="761.2" y1="169.9" x2="761.2" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="760.06" y="178.0" width="2.36" height="11.1" fill="var(--up)"/>
<line x1="765.0" y1="174.1" x2="765.0" y2="196.3" stroke="var(--up)" class="wick"/>
<rect x="763.86" y="180.8" width="2.36" height="1.6" fill="var(--up)"/>
<line x1="768.8" y1="159.2" x2="768.8" y2="176.7" stroke="var(--down)" class="wick"/>
<rect x="767.66" y="174.5" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="772.6" y1="176.3" x2="772.6" y2="218.1" stroke="var(--down)" class="wick"/>
<rect x="771.47" y="183.2" width="2.36" height="28.1" fill="var(--down)"/>
<line x1="776.4" y1="123.2" x2="776.4" y2="204.3" stroke="var(--up)" class="wick"/>
<rect x="775.27" y="139.7" width="2.36" height="64.2" fill="var(--up)"/>
<line x1="780.2" y1="141.6" x2="780.2" y2="160.4" stroke="var(--down)" class="wick"/>
<rect x="779.07" y="144.1" width="2.36" height="5.6" fill="var(--down)"/>
<line x1="784.0" y1="134.2" x2="784.0" y2="164.0" stroke="var(--down)" class="wick"/>
<rect x="782.87" y="138.1" width="2.36" height="21.9" fill="var(--down)"/>
<line x1="787.8" y1="150.6" x2="787.8" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="786.67" y="151.7" width="2.36" height="8.0" fill="var(--up)"/>
<line x1="791.6" y1="140.3" x2="791.6" y2="157.0" stroke="var(--up)" class="wick"/>
<rect x="790.47" y="146.2" width="2.36" height="5.4" fill="var(--up)"/>
<line x1="795.4" y1="121.8" x2="795.4" y2="143.5" stroke="var(--up)" class="wick"/>
<rect x="794.27" y="136.5" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="799.2" y1="99.4" x2="799.2" y2="131.4" stroke="var(--up)" class="wick"/>
<rect x="798.07" y="117.2" width="2.36" height="1.8" fill="var(--up)"/>
<line x1="803.0" y1="120.5" x2="803.0" y2="136.1" stroke="var(--down)" class="wick"/>
<rect x="801.87" y="125.0" width="2.36" height="7.2" fill="var(--down)"/>
<line x1="806.9" y1="121.5" x2="806.9" y2="146.0" stroke="var(--down)" class="wick"/>
<rect x="805.67" y="125.6" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="810.7" y1="123.1" x2="810.7" y2="147.1" stroke="var(--down)" class="wick"/>
<rect x="809.47" y="126.2" width="2.36" height="8.0" fill="var(--down)"/>
<line x1="814.5" y1="128.2" x2="814.5" y2="143.7" stroke="var(--down)" class="wick"/>
<rect x="813.27" y="131.4" width="2.36" height="6.6" fill="var(--down)"/>
<line x1="818.3" y1="133.2" x2="818.3" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="817.07" y="139.2" width="2.36" height="5.3" fill="var(--down)"/>
<line x1="822.1" y1="137.8" x2="822.1" y2="158.7" stroke="var(--up)" class="wick"/>
<rect x="820.88" y="141.9" width="2.36" height="7.7" fill="var(--up)"/>
<line x1="825.9" y1="125.6" x2="825.9" y2="142.4" stroke="var(--up)" class="wick"/>
<rect x="824.68" y="128.1" width="2.36" height="9.1" fill="var(--up)"/>
<line x1="829.7" y1="110.5" x2="829.7" y2="131.6" stroke="var(--up)" class="wick"/>
<rect x="828.48" y="121.6" width="2.36" height="2.6" fill="var(--up)"/>
<line x1="833.5" y1="123.2" x2="833.5" y2="137.6" stroke="var(--down)" class="wick"/>
<rect x="832.28" y="131.1" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="837.3" y1="126.7" x2="837.3" y2="150.9" stroke="var(--down)" class="wick"/>
<rect x="836.08" y="129.7" width="2.36" height="20.3" fill="var(--down)"/>
<line x1="841.1" y1="140.3" x2="841.1" y2="156.0" stroke="var(--up)" class="wick"/>
<rect x="839.88" y="143.0" width="2.36" height="3.9" fill="var(--up)"/>
<line x1="844.9" y1="131.4" x2="844.9" y2="152.0" stroke="var(--up)" class="wick"/>
<rect x="843.68" y="132.6" width="2.36" height="13.7" fill="var(--up)"/>
<line x1="848.7" y1="128.5" x2="848.7" y2="141.8" stroke="var(--down)" class="wick"/>
<rect x="847.48" y="137.3" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="852.5" y1="127.6" x2="852.5" y2="140.6" stroke="var(--up)" class="wick"/>
<rect x="851.28" y="133.9" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="856.3" y1="122.1" x2="856.3" y2="155.7" stroke="var(--down)" class="wick"/>
<rect x="855.08" y="123.7" width="2.36" height="31.0" fill="var(--down)"/>
<line x1="860.1" y1="155.7" x2="860.1" y2="174.7" stroke="var(--down)" class="wick"/>
<rect x="858.88" y="157.7" width="2.36" height="11.0" fill="var(--down)"/>
<line x1="863.9" y1="156.7" x2="863.9" y2="179.4" stroke="var(--up)" class="wick"/>
<rect x="862.68" y="157.4" width="2.36" height="11.0" fill="var(--up)"/>
<line x1="867.7" y1="153.2" x2="867.7" y2="163.1" stroke="var(--up)" class="wick"/>
<rect x="866.48" y="156.0" width="2.36" height="1.6" fill="var(--up)"/>
<line x1="871.5" y1="160.2" x2="871.5" y2="169.1" stroke="var(--down)" class="wick"/>
<rect x="870.29" y="162.7" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="875.3" y1="156.4" x2="875.3" y2="176.4" stroke="var(--down)" class="wick"/>
<rect x="874.09" y="157.3" width="2.36" height="18.0" fill="var(--down)"/>
<line x1="879.1" y1="173.4" x2="879.1" y2="183.2" stroke="var(--down)" class="wick"/>
<rect x="877.89" y="175.7" width="2.36" height="4.1" fill="var(--down)"/>
<line x1="882.9" y1="177.5" x2="882.9" y2="190.8" stroke="var(--down)" class="wick"/>
<rect x="881.69" y="180.8" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="886.7" y1="169.9" x2="886.7" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="885.49" y="170.0" width="2.36" height="9.4" fill="var(--up)"/>
<line x1="890.5" y1="159.2" x2="890.5" y2="171.2" stroke="var(--up)" class="wick"/>
<rect x="889.29" y="165.6" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="894.3" y1="158.2" x2="894.3" y2="173.2" stroke="var(--up)" class="wick"/>
<rect x="893.09" y="158.7" width="2.36" height="1.8" fill="var(--up)"/>
<line x1="898.1" y1="154.4" x2="898.1" y2="165.8" stroke="var(--down)" class="wick"/>
<rect x="896.89" y="159.3" width="2.36" height="4.1" fill="var(--down)"/>
<line x1="901.9" y1="166.1" x2="901.9" y2="175.0" stroke="var(--down)" class="wick"/>
<rect x="900.69" y="166.9" width="2.36" height="3.8" fill="var(--down)"/>
<line x1="905.7" y1="151.0" x2="905.7" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="904.49" y="152.2" width="2.36" height="12.6" fill="var(--up)"/>
<line x1="909.5" y1="141.2" x2="909.5" y2="158.5" stroke="var(--up)" class="wick"/>
<rect x="908.29" y="142.5" width="2.36" height="9.6" fill="var(--up)"/>
<line x1="913.3" y1="140.6" x2="913.3" y2="152.9" stroke="var(--down)" class="wick"/>
<rect x="912.09" y="145.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="917.1" y1="141.6" x2="917.1" y2="153.8" stroke="var(--down)" class="wick"/>
<rect x="915.89" y="144.7" width="2.36" height="3.4" fill="var(--down)"/>
<line x1="920.9" y1="140.0" x2="920.9" y2="151.9" stroke="var(--up)" class="wick"/>
<rect x="919.70" y="141.6" width="2.36" height="9.5" fill="var(--up)"/>
<line x1="924.7" y1="138.3" x2="924.7" y2="150.0" stroke="var(--down)" class="wick"/>
<rect x="923.50" y="140.2" width="2.36" height="8.0" fill="var(--down)"/>
<line x1="928.5" y1="142.1" x2="928.5" y2="155.1" stroke="var(--down)" class="wick"/>
<rect x="927.30" y="142.4" width="2.36" height="2.8" fill="var(--down)"/>
<line x1="932.3" y1="129.5" x2="932.3" y2="148.2" stroke="var(--down)" class="wick"/>
<rect x="931.10" y="134.3" width="2.36" height="11.8" fill="var(--down)"/>
<line x1="936.1" y1="137.1" x2="936.1" y2="152.2" stroke="var(--up)" class="wick"/>
<rect x="934.90" y="140.5" width="2.36" height="9.6" fill="var(--up)"/>
<line x1="939.9" y1="132.3" x2="939.9" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="938.70" y="140.6" width="2.36" height="2.3" fill="var(--down)"/>
<line x1="943.7" y1="137.8" x2="943.7" y2="166.9" stroke="var(--down)" class="wick"/>
<rect x="942.50" y="138.0" width="2.36" height="27.9" fill="var(--down)"/>
<line x1="947.5" y1="157.7" x2="947.5" y2="170.9" stroke="var(--up)" class="wick"/>
<rect x="946.30" y="162.0" width="2.36" height="7.7" fill="var(--up)"/>
<line x1="951.3" y1="162.0" x2="951.3" y2="176.3" stroke="var(--down)" class="wick"/>
<rect x="950.10" y="162.0" width="2.36" height="13.4" fill="var(--down)"/>
<line x1="955.1" y1="150.9" x2="955.1" y2="171.9" stroke="var(--up)" class="wick"/>
<rect x="953.90" y="157.6" width="2.36" height="14.0" fill="var(--up)"/>
<line x1="958.9" y1="134.0" x2="958.9" y2="161.4" stroke="var(--up)" class="wick"/>
<rect x="957.70" y="135.2" width="2.36" height="17.2" fill="var(--up)"/>
<line x1="962.7" y1="127.3" x2="962.7" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="961.50" y="127.6" width="2.36" height="12.0" fill="var(--up)"/>
<line x1="966.5" y1="121.9" x2="966.5" y2="138.4" stroke="var(--up)" class="wick"/>
<rect x="965.30" y="124.4" width="2.36" height="7.5" fill="var(--up)"/>
<line x1="970.3" y1="130.2" x2="970.3" y2="139.7" stroke="var(--down)" class="wick"/>
<rect x="969.11" y="132.6" width="2.36" height="5.3" fill="var(--down)"/>
<line x1="974.1" y1="129.5" x2="974.1" y2="145.7" stroke="var(--down)" class="wick"/>
<rect x="972.91" y="133.3" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="977.9" y1="130.0" x2="977.9" y2="142.1" stroke="var(--down)" class="wick"/>
<rect x="976.71" y="130.2" width="2.36" height="8.3" fill="var(--down)"/>
<line x1="981.7" y1="130.0" x2="981.7" y2="139.7" stroke="var(--up)" class="wick"/>
<rect x="980.51" y="134.0" width="2.36" height="3.1" fill="var(--up)"/>
<line x1="985.5" y1="122.4" x2="985.5" y2="133.8" stroke="var(--up)" class="wick"/>
<rect x="984.31" y="126.7" width="2.36" height="6.6" fill="var(--up)"/>
<line x1="989.3" y1="116.7" x2="989.3" y2="133.9" stroke="var(--down)" class="wick"/>
<rect x="988.11" y="124.4" width="2.36" height="5.1" fill="var(--down)"/>
<line x1="993.1" y1="102.6" x2="993.1" y2="128.1" stroke="var(--up)" class="wick"/>
<rect x="991.91" y="103.1" width="2.36" height="23.5" fill="var(--up)"/>
<line x1="996.9" y1="93.0" x2="996.9" y2="113.6" stroke="var(--down)" class="wick"/>
<rect x="995.71" y="102.9" width="2.36" height="9.5" fill="var(--down)"/>
<line x1="1000.7" y1="114.0" x2="1000.7" y2="126.6" stroke="var(--down)" class="wick"/>
<rect x="999.51" y="120.3" width="2.36" height="2.5" fill="var(--down)"/>
<line x1="1004.5" y1="117.8" x2="1004.5" y2="129.5" stroke="var(--up)" class="wick"/>
<rect x="1003.31" y="121.9" width="2.36" height="2.6" fill="var(--up)"/>
<line x1="1008.3" y1="116.1" x2="1008.3" y2="129.7" stroke="var(--down)" class="wick"/>
<rect x="1007.11" y="120.6" width="2.36" height="4.8" fill="var(--down)"/>
<line x1="1012.1" y1="125.4" x2="1012.1" y2="142.2" stroke="var(--down)" class="wick"/>
<rect x="1010.91" y="128.2" width="2.36" height="8.0" fill="var(--down)"/>
<line x1="1015.9" y1="128.2" x2="1015.9" y2="147.6" stroke="var(--down)" class="wick"/>
<rect x="1014.71" y="131.7" width="2.36" height="9.9" fill="var(--down)"/>
<line x1="1019.7" y1="122.2" x2="1019.7" y2="143.5" stroke="var(--up)" class="wick"/>
<rect x="1018.52" y="124.0" width="2.36" height="18.0" fill="var(--up)"/>
<line x1="1023.5" y1="108.3" x2="1023.5" y2="126.0" stroke="var(--up)" class="wick"/>
<rect x="1022.32" y="111.4" width="2.36" height="13.9" fill="var(--up)"/>
<line x1="1027.3" y1="102.8" x2="1027.3" y2="115.2" stroke="var(--down)" class="wick"/>
<rect x="1026.12" y="109.3" width="2.36" height="3.1" fill="var(--down)"/>
<line x1="1031.1" y1="93.6" x2="1031.1" y2="109.9" stroke="var(--up)" class="wick"/>
<rect x="1029.92" y="98.1" width="2.36" height="11.3" fill="var(--up)"/>
<line x1="1034.9" y1="80.7" x2="1034.9" y2="109.3" stroke="var(--up)" class="wick"/>
<rect x="1033.72" y="81.6" width="2.36" height="21.5" fill="var(--up)"/>
<line x1="1038.7" y1="86.3" x2="1038.7" y2="98.8" stroke="var(--down)" class="wick"/>
<rect x="1037.52" y="90.2" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="1042.5" y1="81.9" x2="1042.5" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="1041.32" y="83.0" width="2.36" height="8.6" fill="var(--up)"/>
<line x1="1046.3" y1="74.1" x2="1046.3" y2="95.0" stroke="var(--up)" class="wick"/>
<rect x="1045.12" y="81.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="1050.1" y1="85.7" x2="1050.1" y2="98.4" stroke="var(--down)" class="wick"/>
<rect x="1048.92" y="86.3" width="2.36" height="7.6" fill="var(--down)"/>
<line x1="60" y1="154.1" x2="1052" y2="154.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="148.1" font-size="11.5" fill="var(--support)" font-weight="600">4.78% S1</text>
<text x="1058" y="160.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="183.5" x2="1052" y2="183.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="177.5" font-size="11.5" fill="var(--support)" font-weight="600">4.58% S2</text>
<text x="1058" y="189.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="220.4" x2="1052" y2="220.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.4" font-size="11.5" fill="var(--support)" font-weight="600">4.33% S3</text>
<text x="1058" y="226.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="93.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="85.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 5.19% (2026-08-24)</text>
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

*작성일: 2026-08-29*
