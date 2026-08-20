# 미국 5년물 국채금리 — 기술적 참고 (주봉 5년)

!!! note ""
    최근 5년 미 국채 5년물 수익률(`^FVX`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. `short_rate.md`(13주)·`treasury_10y.md`(10년)·`treasury_30y.md`(30년)와 함께 **수익률곡선의 중간 구간**을 채운다.

    **왜 별도로 두는가**: `concepts/macroeconomics.md` "수익률곡선"에 따르면 만기가 짧을수록 정책금리 기대를, 길수록 장기 성장·물가 기대를 반영한다 — 5년물은 그 중간 지점으로, 단기(13주)만큼 정책에 즉각 반응하지도, 장기(10년·30년)만큼 먼 미래 기대에만 좌우되지도 않는다.

---

## 1. 차트 — 최근 5년 주봉

<div class="fvx-chart">
<style>
.fvx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .fvx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .fvx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.fvx-chart svg { width:100%; height:auto; display:block; }
.fvx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fvx-chart .title { fill: var(--ink); font-weight:600; }
.fvx-chart .grid { stroke: var(--grid); stroke-width:1; }
.fvx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 5년물 금리(^FVX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 5년물 금리 (^FVX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-17 · 마지막 종가 4.35% (2026-08-17) · 단위 %</text>
<line x1="60" y1="575.9" x2="1052" y2="575.9" class="grid"/>
<text x="52" y="579.9" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="450.6" x2="1052" y2="450.6" class="grid"/>
<text x="52" y="454.6" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="325.3" x2="1052" y2="325.3" class="grid"/>
<text x="52" y="329.3" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="200.1" x2="1052" y2="200.1" class="grid"/>
<text x="52" y="204.1" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="74.8" x2="1052" y2="74.8" class="grid"/>
<text x="52" y="78.8" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
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
<line x1="61.9" y1="601.9" x2="61.9" y2="608.1" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="602.8" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="65.7" y1="592.9" x2="65.7" y2="604.6" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="600.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="69.5" y1="600.9" x2="69.5" y2="607.8" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="601.6" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="73.3" y1="597.3" x2="73.3" y2="604.2" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="598.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="77.0" y1="590.5" x2="77.0" y2="605.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="592.7" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="80.8" y1="580.5" x2="80.8" y2="599.7" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="581.3" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="84.6" y1="570.6" x2="84.6" y2="584.2" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="577.8" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="88.4" y1="568.4" x2="88.4" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="569.9" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="92.2" y1="560.0" x2="92.2" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="560.6" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="96.0" y1="544.9" x2="96.0" y2="559.5" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="549.5" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="99.8" y1="544.4" x2="99.8" y2="559.6" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="550.7" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="103.5" y1="547.5" x2="103.5" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="548.5" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="107.3" y1="545.3" x2="107.3" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="546.3" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="111.1" y1="540.4" x2="111.1" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="549.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="114.9" y1="528.5" x2="114.9" y2="555.5" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="544.8" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="118.7" y1="546.6" x2="118.7" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="547.0" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="122.5" y1="538.1" x2="122.5" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="544.3" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="126.3" y1="538.7" x2="126.3" y2="558.1" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="544.3" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="130.0" y1="544.8" x2="130.0" y2="560.2" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="545.4" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="133.8" y1="537.1" x2="133.8" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="542.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="137.6" y1="510.1" x2="137.6" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="512.6" width="2.35" height="25.7" fill="var(--up)"/>
<line x1="141.4" y1="506.0" x2="141.4" y2="516.8" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="507.2" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="145.2" y1="493.7" x2="145.2" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="498.1" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="149.0" y1="489.3" x2="149.0" y2="514.0" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="497.7" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="152.8" y1="476.9" x2="152.8" y2="503.2" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="477.2" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="156.5" y1="454.1" x2="156.5" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="467.2" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="160.3" y1="455.8" x2="160.3" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="465.0" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="164.1" y1="460.8" x2="164.1" y2="480.2" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="465.0" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="167.9" y1="475.3" x2="167.9" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="475.7" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="171.7" y1="454.4" x2="171.7" y2="494.1" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="455.6" width="2.35" height="35.3" fill="var(--up)"/>
<line x1="175.5" y1="420.8" x2="175.5" y2="448.0" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="432.7" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="179.3" y1="378.6" x2="179.3" y2="423.6" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="378.8" width="2.35" height="44.7" fill="var(--up)"/>
<line x1="183.1" y1="374.7" x2="183.1" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="381.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="186.8" y1="351.5" x2="186.8" y2="385.1" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="355.9" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="190.6" y1="347.6" x2="190.6" y2="379.0" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="348.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="194.4" y1="321.7" x2="194.4" y2="355.7" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="331.7" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="198.2" y1="329.7" x2="198.2" y2="358.0" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="336.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="202.0" y1="314.8" x2="202.0" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="320.0" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="205.8" y1="316.7" x2="205.8" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="317.1" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="209.6" y1="325.6" x2="209.6" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="340.0" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="213.3" y1="340.0" x2="213.3" y2="365.8" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="346.0" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="217.1" y1="328.1" x2="217.1" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="331.5" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="220.9" y1="292.9" x2="220.9" y2="330.0" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="294.0" width="2.35" height="35.1" fill="var(--up)"/>
<line x1="224.7" y1="250.7" x2="224.7" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="273.0" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="228.5" y1="275.4" x2="228.5" y2="320.5" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="278.2" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="232.3" y1="287.6" x2="232.3" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="296.3" width="2.35" height="43.6" fill="var(--down)"/>
<line x1="236.1" y1="305.4" x2="236.1" y2="358.5" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="307.6" width="2.35" height="34.8" fill="var(--up)"/>
<line x1="239.8" y1="305.8" x2="239.8" y2="330.5" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="313.9" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="243.6" y1="298.8" x2="243.6" y2="349.0" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="317.1" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="247.4" y1="335.5" x2="247.4" y2="368.8" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="339.5" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="251.2" y1="326.8" x2="251.2" y2="377.5" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="328.3" width="2.35" height="37.2" fill="var(--up)"/>
<line x1="255.0" y1="319.7" x2="255.0" y2="350.5" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="328.2" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="258.8" y1="309.6" x2="258.8" y2="340.6" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="310.8" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="262.6" y1="293.3" x2="262.6" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="300.9" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="266.4" y1="270.0" x2="266.4" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="288.0" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="270.1" y1="267.5" x2="270.1" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="269.5" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="273.9" y1="239.8" x2="273.9" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="246.9" width="2.35" height="29.8" fill="var(--up)"/>
<line x1="277.7" y1="199.3" x2="277.7" y2="241.9" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="202.1" width="2.35" height="35.8" fill="var(--up)"/>
<line x1="281.5" y1="170.1" x2="281.5" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="190.7" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="285.3" y1="178.3" x2="285.3" y2="227.4" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="183.2" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="289.1" y1="157.0" x2="289.1" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="166.4" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="292.9" y1="137.6" x2="292.9" y2="182.7" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="155.7" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="296.6" y1="149.7" x2="296.6" y2="192.0" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="159.6" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="300.4" y1="143.4" x2="300.4" y2="187.3" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="159.2" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="304.2" y1="149.7" x2="304.2" y2="208.7" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="157.2" width="2.35" height="50.6" fill="var(--down)"/>
<line x1="308.0" y1="195.7" x2="308.0" y2="220.4" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="199.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="311.8" y1="197.3" x2="311.8" y2="217.7" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="200.6" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="315.6" y1="200.2" x2="315.6" y2="243.7" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="215.7" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="319.4" y1="224.9" x2="319.4" y2="249.3" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="230.5" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="323.1" y1="223.0" x2="323.1" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="232.8" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="326.9" y1="215.7" x2="326.9" y2="241.0" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="217.4" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="330.7" y1="195.7" x2="330.7" y2="213.8" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="200.1" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="334.5" y1="203.1" x2="334.5" y2="236.8" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="212.7" width="2.35" height="23.4" fill="var(--down)"/>
<line x1="338.3" y1="230.4" x2="338.3" y2="259.7" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="235.8" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="342.1" y1="241.7" x2="342.1" y2="271.2" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="242.2" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="345.9" y1="242.7" x2="345.9" y2="260.1" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="247.5" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="349.6" y1="238.9" x2="349.6" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="241.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="353.4" y1="209.3" x2="353.4" y2="232.3" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="209.6" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="357.2" y1="185.9" x2="357.2" y2="223.2" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="195.6" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="361.0" y1="169.6" x2="361.0" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="173.8" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="364.8" y1="156.2" x2="364.8" y2="180.8" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="168.4" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="368.6" y1="155.2" x2="368.6" y2="209.1" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="175.3" width="2.35" height="30.6" fill="var(--down)"/>
<line x1="372.4" y1="211.5" x2="372.4" y2="269.6" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="242.3" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="376.2" y1="225.1" x2="376.2" y2="294.5" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="271.2" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="379.9" y1="234.3" x2="379.9" y2="258.6" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="248.8" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="383.7" y1="244.0" x2="383.7" y2="291.6" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="245.5" width="2.35" height="35.1" fill="var(--down)"/>
<line x1="387.5" y1="247.0" x2="387.5" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="248.8" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="391.3" y1="231.4" x2="391.3" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="242.5" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="395.1" y1="245.5" x2="395.1" y2="273.0" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="245.5" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="398.9" y1="246.0" x2="398.9" y2="299.7" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="253.4" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="402.7" y1="256.2" x2="402.7" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="265.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="406.4" y1="226.9" x2="406.4" y2="270.7" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="231.6" width="2.35" height="33.1" fill="var(--up)"/>
<line x1="410.2" y1="201.3" x2="410.2" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="207.8" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="414.0" y1="213.8" x2="414.0" y2="242.0" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="219.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="205.1" x2="417.8" y2="226.1" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="210.1" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="421.6" y1="188.3" x2="421.6" y2="223.0" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="201.1" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="425.4" y1="193.7" x2="425.4" y2="210.2" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="200.7" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="429.2" y1="179.0" x2="429.2" y2="209.2" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="183.4" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="432.9" y1="138.1" x2="432.9" y2="188.7" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="157.8" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="436.7" y1="155.2" x2="436.7" y2="208.5" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="160.4" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="440.5" y1="184.2" x2="440.5" y2="209.6" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="188.4" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="444.3" y1="167.5" x2="444.3" y2="193.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="175.6" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="448.1" y1="149.7" x2="448.1" y2="181.5" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="176.3" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="451.9" y1="161.2" x2="451.9" y2="191.7" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="161.5" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="455.7" y1="141.6" x2="455.7" y2="161.6" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="152.2" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="459.5" y1="137.6" x2="459.5" y2="156.8" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="145.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="463.2" y1="143.8" x2="463.2" y2="179.4" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="143.8" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="467.0" y1="143.8" x2="467.0" y2="159.2" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="150.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="470.8" y1="137.8" x2="470.8" y2="156.0" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="143.3" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="474.6" y1="118.4" x2="474.6" y2="143.8" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="128.8" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="478.4" y1="106.5" x2="478.4" y2="130.7" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="124.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="482.2" y1="94.1" x2="482.2" y2="116.3" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="106.4" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="486.0" y1="105.5" x2="486.0" y2="131.5" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="105.5" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="489.7" y1="76.3" x2="489.7" y2="117.1" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="92.1" width="2.35" height="22.8" fill="var(--up)"/>
<line x1="493.5" y1="83.7" x2="493.5" y2="103.6" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="83.9" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="497.3" y1="95.0" x2="497.3" y2="145.6" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="97.1" width="2.35" height="41.8" fill="var(--down)"/>
<line x1="501.1" y1="116.4" x2="501.1" y2="137.1" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="116.6" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="504.9" y1="109.5" x2="504.9" y2="150.8" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="115.8" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="508.7" y1="135.9" x2="508.7" y2="153.6" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="138.4" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="512.5" y1="139.8" x2="512.5" y2="183.3" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="140.7" width="2.35" height="39.8" fill="var(--down)"/>
<line x1="516.2" y1="164.1" x2="516.2" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="168.1" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="520.0" y1="162.4" x2="520.0" y2="218.5" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="164.0" width="2.35" height="44.8" fill="var(--down)"/>
<line x1="523.8" y1="205.8" x2="523.8" y2="223.5" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="212.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="527.6" y1="212.2" x2="527.6" y2="226.5" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="213.3" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="531.4" y1="188.4" x2="531.4" y2="214.8" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="199.1" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="535.2" y1="197.1" x2="535.2" y2="225.1" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="197.4" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="539.0" y1="186.2" x2="539.0" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="191.0" width="2.35" height="21.9" fill="var(--up)"/>
<line x1="542.7" y1="187.8" x2="542.7" y2="201.4" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="192.4" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="546.5" y1="195.9" x2="546.5" y2="231.5" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="198.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="550.3" y1="179.6" x2="550.3" y2="199.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="181.1" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="554.1" y1="157.2" x2="554.1" y2="186.0" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="164.0" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="557.9" y1="155.6" x2="557.9" y2="172.6" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="164.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="561.7" y1="158.0" x2="561.7" y2="181.0" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="165.9" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="565.5" y1="172.8" x2="565.5" y2="200.8" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="175.4" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="569.3" y1="157.5" x2="569.3" y2="192.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="159.7" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="573.0" y1="154.0" x2="573.0" y2="176.1" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="158.3" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="576.8" y1="167.2" x2="576.8" y2="178.0" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="172.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="580.6" y1="148.2" x2="580.6" y2="171.0" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="154.0" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="584.4" y1="118.9" x2="584.4" y2="156.0" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="133.3" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="588.2" y1="109.2" x2="588.2" y2="124.7" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="117.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="592.0" y1="105.7" x2="592.0" y2="125.2" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="113.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="595.8" y1="109.5" x2="595.8" y2="148.3" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="118.4" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="599.5" y1="134.4" x2="599.5" y2="145.7" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="135.2" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="603.3" y1="130.9" x2="603.3" y2="157.7" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="137.2" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="607.1" y1="130.2" x2="607.1" y2="147.5" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="133.9" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="610.9" y1="117.9" x2="610.9" y2="138.2" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="133.9" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="614.7" y1="138.8" x2="614.7" y2="163.9" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="139.4" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="618.5" y1="138.3" x2="618.5" y2="175.5" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="141.4" width="2.35" height="30.3" fill="var(--down)"/>
<line x1="622.3" y1="161.0" x2="622.3" y2="172.0" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="165.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="626.0" y1="155.3" x2="626.0" y2="170.4" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="158.9" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="629.8" y1="143.2" x2="629.8" y2="173.1" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="149.6" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="633.6" y1="165.2" x2="633.6" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="168.1" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="637.4" y1="178.8" x2="637.4" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="179.6" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="641.2" y1="175.3" x2="641.2" y2="191.2" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="180.1" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="645.0" y1="189.5" x2="645.0" y2="251.7" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="193.7" width="2.35" height="54.6" fill="var(--down)"/>
<line x1="648.8" y1="217.5" x2="648.8" y2="268.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="225.6" width="2.35" height="38.3" fill="var(--up)"/>
<line x1="652.5" y1="223.0" x2="652.5" y2="244.3" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="226.5" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="656.3" y1="227.9" x2="656.3" y2="248.0" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="232.5" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="660.1" y1="235.8" x2="660.1" y2="248.2" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="235.8" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="663.9" y1="234.0" x2="663.9" y2="270.8" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="234.9" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="667.7" y1="258.6" x2="667.7" y2="275.7" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="258.6" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="671.5" y1="257.6" x2="671.5" y2="276.2" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="264.7" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="675.3" y1="252.8" x2="675.3" y2="266.2" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="261.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="679.1" y1="223.4" x2="679.1" y2="266.1" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="223.5" width="2.35" height="32.3" fill="var(--up)"/>
<line x1="682.8" y1="204.5" x2="682.8" y2="219.4" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="215.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="686.6" y1="210.7" x2="686.6" y2="222.2" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="212.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="690.4" y1="192.0" x2="690.4" y2="210.2" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="193.7" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="694.2" y1="172.8" x2="694.2" y2="194.4" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="173.9" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="698.0" y1="160.2" x2="698.0" y2="185.5" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="176.0" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="701.8" y1="152.1" x2="701.8" y2="175.6" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="162.7" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="705.6" y1="157.0" x2="705.6" y2="174.8" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="157.8" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="709.3" y1="171.1" x2="709.3" y2="194.1" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="172.8" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="713.1" y1="180.0" x2="713.1" y2="199.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="187.9" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="716.9" y1="168.5" x2="716.9" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="169.0" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="720.7" y1="144.6" x2="720.7" y2="173.0" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="152.5" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="724.5" y1="138.6" x2="724.5" y2="151.5" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="142.9" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="728.3" y1="148.2" x2="728.3" y2="158.9" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="148.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="732.1" y1="125.8" x2="732.1" y2="151.3" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="125.8" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="735.8" y1="122.4" x2="735.8" y2="153.8" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="126.2" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="739.6" y1="140.7" x2="739.6" y2="153.3" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="146.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="743.4" y1="150.2" x2="743.4" y2="163.5" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="154.5" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="747.2" y1="150.2" x2="747.2" y2="172.5" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="158.2" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="751.0" y1="137.9" x2="751.0" y2="162.4" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="158.3" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="754.8" y1="148.3" x2="754.8" y2="168.9" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="154.0" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="758.6" y1="163.7" x2="758.6" y2="199.2" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="165.0" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="762.4" y1="185.2" x2="762.4" y2="215.1" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="188.4" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="766.1" y1="186.3" x2="766.1" y2="207.6" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="189.8" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="769.9" y1="184.7" x2="769.9" y2="205.8" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="191.9" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="773.7" y1="185.0" x2="773.7" y2="203.1" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="192.7" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="777.5" y1="200.6" x2="777.5" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="209.2" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="781.3" y1="172.1" x2="781.3" y2="244.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="180.0" width="2.35" height="63.4" fill="var(--up)"/>
<line x1="785.1" y1="186.0" x2="785.1" y2="213.1" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="188.0" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="788.9" y1="197.3" x2="788.9" y2="216.2" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="205.0" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="792.6" y1="207.0" x2="792.6" y2="239.9" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="208.6" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="796.4" y1="199.3" x2="796.4" y2="218.7" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="201.7" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="800.2" y1="179.6" x2="800.2" y2="198.6" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="187.7" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="804.0" y1="178.8" x2="804.0" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="182.2" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="807.8" y1="189.3" x2="807.8" y2="205.3" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="193.1" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="811.6" y1="184.0" x2="811.6" y2="213.3" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="184.3" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="815.4" y1="184.5" x2="815.4" y2="208.2" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="186.3" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="819.1" y1="195.3" x2="819.1" y2="209.1" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="195.3" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="822.9" y1="207.3" x2="822.9" y2="225.5" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="207.3" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="826.7" y1="202.8" x2="826.7" y2="227.4" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="207.7" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="830.5" y1="200.2" x2="830.5" y2="210.5" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="201.1" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="834.3" y1="193.6" x2="834.3" y2="207.2" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="201.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="838.1" y1="200.6" x2="838.1" y2="216.2" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="206.1" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="841.9" y1="200.9" x2="841.9" y2="229.1" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="204.7" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="845.6" y1="220.7" x2="845.6" y2="233.3" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="221.4" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="849.4" y1="218.9" x2="849.4" y2="233.4" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="219.5" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="853.2" y1="216.5" x2="853.2" y2="231.8" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="222.1" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="857.0" y1="224.7" x2="857.0" y2="238.8" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="227.0" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="860.8" y1="229.0" x2="860.8" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="229.9" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="864.6" y1="244.4" x2="864.6" y2="258.9" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="247.0" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="868.4" y1="238.4" x2="868.4" y2="256.2" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="238.8" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="872.2" y1="227.1" x2="872.2" y2="241.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="228.9" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="875.9" y1="229.8" x2="875.9" y2="242.3" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="232.1" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="879.7" y1="231.1" x2="879.7" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="232.0" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="883.5" y1="244.4" x2="883.5" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="244.4" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="887.3" y1="244.4" x2="887.3" y2="257.3" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="249.9" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="891.1" y1="231.5" x2="891.1" y2="249.8" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="235.5" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="894.9" y1="229.3" x2="894.9" y2="243.8" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="235.8" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="898.7" y1="233.3" x2="898.7" y2="244.3" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="233.3" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="902.4" y1="232.6" x2="902.4" y2="249.0" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="234.9" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="906.2" y1="246.0" x2="906.2" y2="256.1" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="246.4" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="910.0" y1="235.1" x2="910.0" y2="248.7" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="235.8" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="913.8" y1="224.4" x2="913.8" y2="240.3" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="231.3" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="917.6" y1="232.9" x2="917.6" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="234.4" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="921.4" y1="229.4" x2="921.4" y2="239.9" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="236.3" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="925.2" y1="231.6" x2="925.2" y2="241.7" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="232.8" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="928.9" y1="227.3" x2="928.9" y2="240.8" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="230.5" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="932.7" y1="221.5" x2="932.7" y2="236.8" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="221.6" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="936.5" y1="216.1" x2="936.5" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="219.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="940.3" y1="216.0" x2="940.3" y2="226.0" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="222.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="944.1" y1="217.5" x2="944.1" y2="233.6" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="226.9" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="947.9" y1="227.3" x2="947.9" y2="250.2" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="227.9" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="951.7" y1="239.0" x2="951.7" y2="252.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="243.9" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="955.5" y1="245.7" x2="955.5" y2="261.8" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="245.7" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="959.2" y1="228.1" x2="959.2" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="235.8" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="963.0" y1="214.6" x2="963.0" y2="239.9" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="215.9" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="966.8" y1="196.2" x2="966.8" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="198.6" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="970.6" y1="181.7" x2="970.6" y2="210.0" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="191.3" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="974.4" y1="198.3" x2="974.4" y2="212.0" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="199.2" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="978.2" y1="197.2" x2="978.2" y2="217.5" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="199.1" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="982.0" y1="203.2" x2="982.0" y2="223.0" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="203.7" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="985.7" y1="202.6" x2="985.7" y2="219.7" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="210.1" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="989.5" y1="189.3" x2="989.5" y2="209.6" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="197.4" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="993.3" y1="185.0" x2="993.3" y2="206.1" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="194.3" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="997.1" y1="167.1" x2="997.1" y2="196.4" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="167.7" width="2.35" height="26.6" fill="var(--up)"/>
<line x1="1000.9" y1="156.1" x2="1000.9" y2="175.0" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="167.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1004.7" y1="173.0" x2="1004.7" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="176.8" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="1008.5" y1="162.9" x2="1008.5" y2="182.4" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="165.0" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="1012.2" y1="163.2" x2="1012.2" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="165.5" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="1016.0" y1="168.7" x2="1016.0" y2="182.5" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="171.9" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="1019.8" y1="163.9" x2="1019.8" y2="185.0" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="165.6" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="1023.6" y1="167.0" x2="1023.6" y2="183.5" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="171.3" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="1027.4" y1="157.2" x2="1027.4" y2="176.3" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="161.5" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="1031.2" y1="153.2" x2="1031.2" y2="171.9" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="158.6" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="1035.0" y1="140.7" x2="1035.0" y2="163.9" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="146.7" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="1038.7" y1="142.4" x2="1038.7" y2="157.5" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="142.4" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="1042.5" y1="147.8" x2="1042.5" y2="162.0" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="152.2" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="1046.3" y1="148.7" x2="1046.3" y2="164.6" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="153.1" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="1050.1" y1="150.1" x2="1050.1" y2="160.2" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="155.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="60" y1="146.6" x2="1052" y2="146.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="150.1" font-size="11.5" fill="var(--resistance)" font-weight="600">4.43% R1</text>
<text x="1058" y="162.1" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="199.9" x2="1052" y2="199.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="193.9" font-size="11.5" fill="var(--support)" font-weight="600">4.00% S1</text>
<text x="1058" y="205.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="229.0" x2="1052" y2="229.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="223.0" font-size="11.5" fill="var(--support)" font-weight="600">3.77% S2</text>
<text x="1058" y="235.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="258.0" x2="1052" y2="258.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="252.0" font-size="11.5" fill="var(--support)" font-weight="600">3.54% S3</text>
<text x="1058" y="264.0" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="155.8" r="3" fill="var(--ink)"/>
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

- **상승**: 중기 성장·정책금리 기대 확대 신호로 흔히 해석된다 — 단기(13주)만큼 정책에 즉각 반응하지도, 장기(10·30년)만큼 먼 미래 기대에만 좌우되지도 않는 중간 지점이다.
- **하락**: 중기 성장·정책금리 기대 둔화 신호로 흔히 해석된다.
- 이 레포 밸류에이션(DCF 무위험이자율)의 표준 근거로 쓰지 않는다 — 표준은 10년물이다. 이 문서는 수익률곡선 형태를 보기 위한 보조 자료다.

---

## 관련 문서

- [13주 단기금리](./short_rate.md)
- [미국 10년물 국채금리](./treasury_10y.md) — DCF 무위험이자율의 표준 근거
- [미국 30년물 국채금리](./treasury_30y.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — "수익률곡선" 절
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Treasury Yield 5 Years (^FVX)](https://finance.yahoo.com/quote/%5EFVX/)
- [미 재무부 금리 (원출처)](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
