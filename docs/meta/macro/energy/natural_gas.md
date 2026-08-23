# 천연가스

!!! note ""
    최근 5년간 헨리허브 천연가스 선물(연속월물, `NG=F`) 주간 가격을 지지선·저항선과 함께 정리한 참고 자료다. 원유와 같은 에너지 원자재이지만, 천연가스는 겨울철 난방 수요처럼 계절 영향을 훨씬 많이 받아서 가격이 출렁이는 패턴이 원유와는 다르다.

---

## 1. 차트 — 최근 5년 주봉

<div class="ng-f-chart">
<style>
.ng-f-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ng-f-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ng-f-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ng-f-chart svg { width:100%; height:auto; display:block; }
.ng-f-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ng-f-chart .title { fill: var(--ink); font-weight:600; }
.ng-f-chart .grid { stroke: var(--grid); stroke-width:1; }
.ng-f-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="천연가스(NG=F) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">천연가스 (NG=F) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $2.81 (2026-08-21) · 단위 USD/MMBtu</text>
<line x1="60" y1="576.4" x2="1052" y2="576.4" class="grid"/>
<text x="52" y="580.4" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="452.5" x2="1052" y2="452.5" class="grid"/>
<text x="52" y="456.5" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="328.6" x2="1052" y2="328.6" class="grid"/>
<text x="52" y="332.6" font-size="11" text-anchor="end" fill="var(--muted)">6.00</text>
<line x1="60" y1="204.7" x2="1052" y2="204.7" class="grid"/>
<text x="52" y="208.7" font-size="11" text-anchor="end" fill="var(--muted)">8.00</text>
<line x1="60" y1="80.8" x2="1052" y2="80.8" class="grid"/>
<text x="52" y="84.8" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
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
<line x1="61.9" y1="427.9" x2="61.9" y2="462.6" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="429.6" width="2.35" height="31.5" fill="var(--up)"/>
<line x1="65.7" y1="407.5" x2="65.7" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="408.4" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="69.5" y1="387.0" x2="69.5" y2="418.0" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="394.4" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="73.3" y1="350.3" x2="73.3" y2="398.1" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="384.1" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="77.0" y1="379.2" x2="77.0" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="381.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="80.8" y1="311.3" x2="80.8" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="352.2" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="84.6" y1="299.7" x2="84.6" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="351.7" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="88.4" y1="330.8" x2="88.4" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="347.5" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="92.2" y1="367.1" x2="92.2" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="372.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="96.0" y1="310.6" x2="96.0" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="361.6" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="99.8" y1="336.3" x2="99.8" y2="383.4" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="358.6" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="103.5" y1="349.5" x2="103.5" y2="407.6" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="353.1" width="2.35" height="50.4" fill="var(--down)"/>
<line x1="107.3" y1="366.2" x2="107.3" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="386.5" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="111.1" y1="355.7" x2="111.1" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="362.9" width="2.35" height="33.3" fill="var(--up)"/>
<line x1="114.9" y1="378.2" x2="114.9" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="378.2" width="2.35" height="66.1" fill="var(--down)"/>
<line x1="118.7" y1="454.7" x2="118.7" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="457.2" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="122.5" y1="447.3" x2="122.5" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="454.1" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="126.3" y1="450.0" x2="126.3" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="469.2" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="130.0" y1="436.4" x2="130.0" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="455.1" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="133.8" y1="453.8" x2="133.8" y2="474.9" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="457.7" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="137.6" y1="398.1" x2="137.6" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="436.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="141.4" y1="428.4" x2="141.4" y2="466.1" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="430.5" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="145.2" y1="245.2" x2="145.2" y2="460.2" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="412.9" width="2.35" height="44.9" fill="var(--up)"/>
<line x1="149.0" y1="355.1" x2="149.0" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="398.8" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="152.8" y1="423.5" x2="152.8" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="428.7" width="2.35" height="27.4" fill="var(--down)"/>
<line x1="156.5" y1="403.4" x2="156.5" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="425.8" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="160.3" y1="394.3" x2="160.3" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="415.7" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="164.1" y1="387.8" x2="164.1" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="389.6" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="167.9" y1="379.2" x2="167.9" y2="424.6" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="388.0" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="171.7" y1="390.5" x2="171.7" y2="424.1" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="399.1" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="175.5" y1="354.8" x2="175.5" y2="406.2" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="355.2" width="2.35" height="41.0" fill="var(--up)"/>
<line x1="179.3" y1="339.0" x2="179.3" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="346.0" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="183.1" y1="295.3" x2="183.1" y2="350.3" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="311.4" width="2.35" height="33.0" fill="var(--up)"/>
<line x1="186.8" y1="245.2" x2="186.8" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="248.1" width="2.35" height="56.1" fill="var(--up)"/>
<line x1="190.6" y1="200.7" x2="190.6" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="243.9" width="2.35" height="51.6" fill="var(--down)"/>
<line x1="194.4" y1="240.5" x2="194.4" y2="307.2" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="251.5" width="2.35" height="51.4" fill="var(--up)"/>
<line x1="198.2" y1="143.0" x2="198.2" y2="253.1" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="202.0" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="202.0" y1="186.9" x2="202.0" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="214.4" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="205.8" y1="170.7" x2="205.8" y2="225.6" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="199.6" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="209.6" y1="117.9" x2="209.6" y2="213.9" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="159.7" width="2.35" height="40.1" fill="var(--up)"/>
<line x1="213.3" y1="139.2" x2="213.3" y2="197.4" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="150.5" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="217.1" y1="101.6" x2="217.1" y2="203.7" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="152.0" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="220.9" y1="145.8" x2="220.9" y2="274.0" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="147.7" width="2.35" height="122.4" fill="var(--down)"/>
<line x1="224.7" y1="268.1" x2="224.7" y2="327.3" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="279.0" width="2.35" height="35.9" fill="var(--down)"/>
<line x1="228.5" y1="277.0" x2="228.5" y2="368.4" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="320.8" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="232.3" y1="305.0" x2="232.3" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="326.5" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="236.1" y1="257.7" x2="236.1" y2="327.7" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="265.7" width="2.35" height="35.3" fill="var(--up)"/>
<line x1="239.8" y1="178.9" x2="239.8" y2="261.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="186.2" width="2.35" height="70.1" fill="var(--up)"/>
<line x1="243.6" y1="96.1" x2="243.6" y2="204.1" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="180.5" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="247.4" y1="175.0" x2="247.4" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="200.7" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="251.2" y1="143.1" x2="251.2" y2="233.7" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="157.1" width="2.35" height="55.3" fill="var(--up)"/>
<line x1="255.0" y1="100.8" x2="255.0" y2="179.7" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="121.9" width="2.35" height="40.7" fill="var(--up)"/>
<line x1="258.8" y1="79.0" x2="258.8" y2="139.6" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="124.4" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="262.6" y1="100.5" x2="262.6" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="101.2" width="2.35" height="54.8" fill="var(--down)"/>
<line x1="266.4" y1="134.9" x2="266.4" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="141.0" width="2.35" height="63.9" fill="var(--down)"/>
<line x1="270.1" y1="128.0" x2="270.1" y2="222.2" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="203.1" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="273.9" y1="197.1" x2="273.9" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="221.0" width="2.35" height="56.3" fill="var(--down)"/>
<line x1="277.7" y1="258.0" x2="277.7" y2="300.4" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="276.3" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="281.5" y1="255.0" x2="281.5" y2="309.7" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="279.0" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="285.3" y1="272.8" x2="285.3" y2="307.7" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="288.5" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="289.1" y1="309.2" x2="289.1" y2="396.6" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="312.3" width="2.35" height="80.8" fill="var(--down)"/>
<line x1="292.9" y1="335.4" x2="292.9" y2="406.1" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="348.2" width="2.35" height="44.2" fill="var(--up)"/>
<line x1="296.6" y1="297.0" x2="296.6" y2="352.5" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="303.8" width="2.35" height="35.2" fill="var(--up)"/>
<line x1="300.4" y1="253.0" x2="300.4" y2="346.3" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="267.9" width="2.35" height="68.2" fill="var(--down)"/>
<line x1="304.2" y1="294.7" x2="304.2" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="309.8" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="308.0" y1="229.2" x2="308.0" y2="319.6" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="265.2" width="2.35" height="42.8" fill="var(--up)"/>
<line x1="311.8" y1="240.6" x2="311.8" y2="314.9" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="274.7" width="2.35" height="36.5" fill="var(--down)"/>
<line x1="315.6" y1="304.4" x2="315.6" y2="369.7" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="313.4" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="319.4" y1="260.1" x2="319.4" y2="315.0" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="269.8" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="323.1" y1="311.6" x2="323.1" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="319.1" width="2.35" height="66.6" fill="var(--down)"/>
<line x1="326.9" y1="367.8" x2="326.9" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="373.0" width="2.35" height="50.1" fill="var(--down)"/>
<line x1="330.7" y1="428.1" x2="330.7" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="428.2" width="2.35" height="42.3" fill="var(--down)"/>
<line x1="334.5" y1="444.6" x2="334.5" y2="490.7" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="464.3" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="338.3" y1="465.6" x2="338.3" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="480.0" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="342.1" y1="477.6" x2="342.1" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="486.6" width="2.35" height="21.1" fill="var(--down)"/>
<line x1="345.9" y1="528.1" x2="345.9" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="531.8" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="349.6" y1="535.7" x2="349.6" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="544.6" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="353.4" y1="537.8" x2="353.4" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="540.5" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="357.2" y1="540.7" x2="357.2" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="548.5" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="361.0" y1="512.8" x2="361.0" y2="542.1" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="513.9" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="364.8" y1="525.0" x2="364.8" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="525.0" width="2.35" height="24.8" fill="var(--down)"/>
<line x1="368.6" y1="534.7" x2="368.6" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="550.0" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="372.4" y1="550.0" x2="372.4" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="554.9" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="376.2" y1="561.5" x2="376.2" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="563.1" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="379.9" y1="564.2" x2="379.9" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="571.2" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="383.7" y1="561.1" x2="383.7" y2="579.8" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="569.4" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="387.5" y1="552.6" x2="387.5" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="562.0" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="391.3" y1="543.7" x2="391.3" y2="570.2" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="551.0" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="395.1" y1="551.0" x2="395.1" y2="574.5" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="551.8" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="398.9" y1="555.7" x2="398.9" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="560.0" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="402.7" y1="534.0" x2="402.7" y2="560.9" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="540.2" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="406.4" y1="541.2" x2="406.4" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="541.2" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="410.2" y1="548.7" x2="410.2" y2="568.0" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="550.6" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="414.0" y1="552.9" x2="414.0" y2="565.7" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="560.7" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="417.8" y1="536.0" x2="417.8" y2="563.7" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="537.3" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="421.6" y1="530.6" x2="421.6" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="531.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="425.4" y1="524.5" x2="425.4" y2="539.7" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="527.0" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="429.2" y1="527.3" x2="429.2" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="531.3" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="432.9" y1="530.0" x2="432.9" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="541.1" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="436.7" y1="527.6" x2="436.7" y2="546.4" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="532.3" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="440.5" y1="528.9" x2="440.5" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="531.8" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="444.3" y1="533.5" x2="444.3" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="535.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="448.1" y1="513.4" x2="448.1" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="528.7" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="451.9" y1="523.0" x2="451.9" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="528.4" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="455.7" y1="535.5" x2="455.7" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="541.7" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="459.5" y1="522.8" x2="459.5" y2="544.5" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="529.0" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="463.2" y1="532.6" x2="463.2" y2="545.5" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="533.1" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="467.0" y1="525.4" x2="467.0" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="536.5" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="470.8" y1="522.4" x2="470.8" y2="539.6" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="537.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="474.6" y1="514.7" x2="474.6" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="518.9" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="478.4" y1="491.9" x2="478.4" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="493.5" width="2.35" height="23.5" fill="var(--up)"/>
<line x1="482.2" y1="485.3" x2="482.2" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="492.8" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="486.0" y1="503.0" x2="486.0" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="503.0" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="489.7" y1="489.6" x2="489.7" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="504.3" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="493.5" y1="475.4" x2="493.5" y2="494.8" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="482.6" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="497.3" y1="489.3" x2="497.3" y2="515.2" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="491.4" width="2.35" height="21.1" fill="var(--down)"/>
<line x1="501.1" y1="497.4" x2="501.1" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="510.5" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="504.9" y1="517.1" x2="504.9" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="517.1" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="508.7" y1="522.5" x2="508.7" y2="535.0" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="526.0" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="512.5" y1="527.7" x2="512.5" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="531.3" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="516.2" y1="542.7" x2="516.2" y2="561.9" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="546.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="520.0" y1="538.0" x2="520.0" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="538.6" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="523.8" y1="531.7" x2="523.8" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="542.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="527.6" y1="520.3" x2="527.6" y2="544.0" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="521.1" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="531.4" y1="490.2" x2="531.4" y2="533.4" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="495.1" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="535.2" y1="502.8" x2="535.2" y2="544.6" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="507.5" width="2.35" height="36.8" fill="var(--down)"/>
<line x1="539.0" y1="521.7" x2="539.0" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="532.3" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="542.7" y1="529.3" x2="542.7" y2="575.1" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="534.3" width="2.35" height="37.2" fill="var(--down)"/>
<line x1="546.5" y1="568.6" x2="546.5" y2="587.8" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="569.6" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="550.3" y1="584.9" x2="550.3" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="588.5" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="554.1" y1="589.3" x2="554.1" y2="606.1" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="601.0" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="557.9" y1="581.5" x2="557.9" y2="606.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="586.7" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="561.7" y1="575.9" x2="561.7" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="584.3" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="565.5" y1="586.3" x2="565.5" y2="598.6" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="588.5" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="569.3" y1="590.7" x2="569.3" y2="598.3" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="595.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="573.0" y1="589.5" x2="573.0" y2="608.6" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="591.1" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="576.8" y1="582.3" x2="576.8" y2="594.7" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="589.8" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="580.6" y1="580.0" x2="580.6" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="590.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="584.4" y1="588.5" x2="584.4" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="590.6" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="588.2" y1="585.9" x2="588.2" y2="608.5" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="591.0" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="592.0" y1="566.5" x2="592.0" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="567.6" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="595.8" y1="555.1" x2="595.8" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="560.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="599.5" y1="535.9" x2="599.5" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="537.7" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="603.3" y1="519.2" x2="603.3" y2="545.9" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="535.6" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="607.1" y1="534.2" x2="607.1" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="540.1" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="610.9" y1="516.5" x2="610.9" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="519.6" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="614.7" y1="504.6" x2="614.7" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="515.7" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="618.5" y1="517.7" x2="618.5" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="524.0" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="622.3" y1="524.1" x2="622.3" y2="539.6" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="534.9" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="626.0" y1="539.1" x2="626.0" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="540.7" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="629.8" y1="548.7" x2="629.8" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="556.1" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="633.6" y1="558.8" x2="633.6" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="559.5" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="637.4" y1="559.7" x2="637.4" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="570.0" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="641.2" y1="567.2" x2="641.2" y2="585.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="575.4" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="645.0" y1="564.8" x2="645.0" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="567.6" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="648.8" y1="557.8" x2="648.8" y2="569.6" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="565.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="652.5" y1="559.2" x2="652.5" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="568.7" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="656.3" y1="565.8" x2="656.3" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="568.6" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="660.1" y1="558.2" x2="660.1" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="559.4" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="663.9" y1="551.2" x2="663.9" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="557.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="667.7" y1="547.9" x2="667.7" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="549.5" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="671.5" y1="518.7" x2="671.5" y2="548.1" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="520.6" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="675.3" y1="513.3" x2="675.3" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="520.7" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="679.1" y1="524.5" x2="679.1" y2="540.0" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="525.2" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="682.8" y1="537.7" x2="682.8" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="537.8" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="686.6" y1="540.4" x2="686.6" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="541.7" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="690.4" y1="519.5" x2="690.4" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="535.4" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="694.2" y1="525.8" x2="694.2" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="535.0" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="698.0" y1="513.2" x2="698.0" y2="533.8" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="525.4" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="701.8" y1="479.6" x2="701.8" y2="524.9" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="506.5" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="705.6" y1="483.5" x2="705.6" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="492.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="709.3" y1="497.2" x2="709.3" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="500.8" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="713.1" y1="479.8" x2="713.1" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="497.1" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="716.9" y1="463.2" x2="716.9" y2="508.8" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="468.1" width="2.35" height="33.3" fill="var(--up)"/>
<line x1="720.7" y1="451.9" x2="720.7" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="460.6" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="724.5" y1="440.1" x2="724.5" y2="494.0" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="473.8" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="728.3" y1="451.4" x2="728.3" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="453.2" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="732.1" y1="429.7" x2="732.1" y2="468.9" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="431.0" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="735.8" y1="449.4" x2="735.8" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="450.8" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="739.6" y1="463.2" x2="739.6" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="465.8" width="2.35" height="45.9" fill="var(--down)"/>
<line x1="743.4" y1="487.5" x2="743.4" y2="504.5" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="495.3" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="747.2" y1="464.9" x2="747.2" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="469.6" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="751.0" y1="423.0" x2="751.0" y2="480.2" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="438.0" width="2.35" height="38.4" fill="var(--up)"/>
<line x1="754.8" y1="439.4" x2="754.8" y2="464.0" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="448.5" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="758.6" y1="418.4" x2="758.6" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="427.8" width="2.35" height="38.4" fill="var(--up)"/>
<line x1="762.4" y1="396.7" x2="762.4" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="423.6" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="766.1" y1="436.5" x2="766.1" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="444.8" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="769.9" y1="446.3" x2="769.9" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="448.5" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="773.7" y1="436.8" x2="773.7" y2="464.2" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="441.6" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="777.5" y1="456.3" x2="777.5" y2="493.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="464.2" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="781.3" y1="476.5" x2="781.3" y2="502.6" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="483.5" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="785.1" y1="500.5" x2="785.1" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="502.2" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="788.9" y1="472.8" x2="788.9" y2="523.2" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="475.4" width="2.35" height="46.2" fill="var(--up)"/>
<line x1="792.6" y1="464.0" x2="792.6" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="465.2" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="796.4" y1="462.4" x2="796.4" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="466.5" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="800.2" y1="482.7" x2="800.2" y2="508.4" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="493.8" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="804.0" y1="478.8" x2="804.0" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="486.8" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="807.8" y1="463.9" x2="807.8" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="465.9" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="811.6" y1="466.8" x2="811.6" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="469.9" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="815.4" y1="443.4" x2="815.4" y2="475.2" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="462.0" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="819.1" y1="455.7" x2="819.1" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="455.7" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="822.9" y1="468.8" x2="822.9" y2="496.3" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="468.9" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="826.7" y1="485.2" x2="826.7" y2="505.2" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="493.2" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="830.5" y1="475.5" x2="830.5" y2="490.7" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="479.5" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="834.3" y1="485.0" x2="834.3" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="485.7" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="838.1" y1="503.0" x2="838.1" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="508.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="841.9" y1="505.3" x2="841.9" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="510.5" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="845.6" y1="514.5" x2="845.6" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="519.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="849.4" y1="519.3" x2="849.4" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="522.1" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="853.2" y1="513.1" x2="853.2" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="514.7" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="857.0" y1="506.4" x2="857.0" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="511.5" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="860.8" y1="502.2" x2="860.8" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="509.1" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="864.6" y1="504.1" x2="864.6" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="517.5" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="868.4" y1="516.5" x2="868.4" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="520.1" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="872.2" y1="478.2" x2="872.2" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="494.4" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="875.9" y1="480.4" x2="875.9" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="495.9" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="879.7" y1="505.9" x2="879.7" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="508.3" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="883.5" y1="479.0" x2="883.5" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="495.6" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="887.3" y1="442.8" x2="887.3" y2="502.5" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="444.8" width="2.35" height="44.2" fill="var(--up)"/>
<line x1="891.1" y1="426.5" x2="891.1" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="433.0" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="894.9" y1="409.9" x2="894.9" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="417.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="898.7" y1="410.7" x2="898.7" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="416.6" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="902.4" y1="398.6" x2="902.4" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="399.9" width="2.35" height="23.9" fill="var(--up)"/>
<line x1="906.2" y1="359.8" x2="906.2" y2="405.6" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="372.7" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="910.0" y1="377.9" x2="910.0" y2="448.5" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="384.4" width="2.35" height="61.2" fill="var(--down)"/>
<line x1="913.8" y1="439.0" x2="913.8" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="441.9" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="917.6" y1="415.8" x2="917.6" y2="465.1" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="429.8" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="921.4" y1="407.9" x2="921.4" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="424.6" width="2.35" height="51.5" fill="var(--down)"/>
<line x1="925.2" y1="475.2" x2="925.2" y2="506.4" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="483.1" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="928.9" y1="483.6" x2="928.9" y2="514.1" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="496.5" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="932.7" y1="350.3" x2="932.7" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="373.5" width="2.35" height="110.0" fill="var(--up)"/>
<line x1="936.5" y1="215.4" x2="936.5" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="341.6" width="2.35" height="89.0" fill="var(--down)"/>
<line x1="940.3" y1="468.9" x2="940.3" y2="504.9" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="470.6" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="944.1" y1="494.9" x2="944.1" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="499.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="947.9" y1="503.9" x2="947.9" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="511.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="951.7" y1="498.8" x2="951.7" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="499.6" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="955.5" y1="497.1" x2="955.5" y2="522.7" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="503.0" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="959.2" y1="483.9" x2="959.2" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="495.6" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="963.0" y1="497.8" x2="963.0" y2="519.2" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="503.3" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="966.8" y1="505.0" x2="966.8" y2="522.9" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="507.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="970.6" y1="510.9" x2="970.6" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="511.1" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="974.4" y1="521.4" x2="974.4" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="524.5" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="978.2" y1="531.6" x2="978.2" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="533.6" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="982.0" y1="529.2" x2="982.0" y2="545.8" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="533.8" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="985.7" y1="525.6" x2="985.7" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="528.1" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="989.5" y1="521.7" x2="989.5" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="527.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="993.3" y1="515.6" x2="993.3" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="517.0" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="997.1" y1="505.9" x2="997.1" y2="521.4" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="514.9" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="1000.9" y1="490.4" x2="1000.9" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="496.5" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="1004.7" y1="489.9" x2="1004.7" y2="508.3" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="493.7" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="1008.5" y1="499.1" x2="1008.5" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="503.0" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="1012.2" y1="496.0" x2="1012.2" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="502.2" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="1016.0" y1="487.2" x2="1016.0" y2="506.1" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="497.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="1019.8" y1="494.2" x2="1019.8" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="497.1" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="1023.6" y1="492.5" x2="1023.6" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="501.7" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="1027.4" y1="516.5" x2="1027.4" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="518.8" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="1031.2" y1="515.0" x2="1031.2" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="522.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1035.0" y1="524.6" x2="1035.0" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="525.6" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="1038.7" y1="526.3" x2="1038.7" y2="538.3" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="530.3" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="1042.5" y1="525.0" x2="1042.5" y2="532.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="531.0" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="1046.3" y1="522.2" x2="1046.3" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="528.5" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="1050.1" y1="527.0" x2="1050.1" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="526.2" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="60" y1="513.2" x2="1052" y2="513.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="516.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$3.02 R1</text>
<text x="1058" y="528.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="487.1" x2="1052" y2="487.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="490.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$3.44 R2</text>
<text x="1058" y="502.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="548.3" x2="1052" y2="548.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="542.3" font-size="11.5" fill="var(--support)" font-weight="600">$2.45 S1</text>
<text x="1058" y="554.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="563.0" x2="1052" y2="563.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="557.0" font-size="11.5" fill="var(--support)" font-weight="600">$2.22 S2</text>
<text x="1058" y="569.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="579.2" x2="1052" y2="579.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="573.2" font-size="11.5" fill="var(--support)" font-weight="600">$1.96 S3</text>
<text x="1058" y="585.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="526.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="518.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $2.81 (2026-08-21)</text>
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

- **상승**: 난방·발전용 수요가 계절적으로 급증했거나, 파이프라인 문제나 LNG(액화천연가스) 수출 확대로 국내에 남는 공급이 줄어드는 등 공급에 차질이 생겼다는 신호로 흔히 해석한다.
- **하락**: 날씨가 따뜻해 수요가 줄었거나, 생산이 늘고 재고가 쌓여 공급이 넘친다는 신호로 흔히 해석한다.
- 계절성이 워낙 강해서, 같은 방향으로 움직여도 시기(겨울철인지 여름철인지)에 따라 의미가 다르다 — 가격 자체보다 그 계절 기준으로 재고가 많은지 적은지를 함께 봐야 한다.
- **왜 원유보다 지역별로 가격이 다른가**: 천연가스는 파이프라인이나 LNG 터미널 같은 운송 설비가 있어야만 옮길 수 있어서, 원유만큼 세계 어디로든 자유롭게 옮겨 팔기가 어렵다. 그래서 미국(헨리허브)·유럽(TTF)·아시아(JKM)의 가격이 서로 크게 벌어지는 일이 흔하고, 이 문서의 가격은 어디까지나 미국 시장 기준이다.

---

## 관련 문서

- [WTI 원유](./oil_wti.md)
- [우라늄 실물 신탁 (SRUUF)](./uranium.md)
- [에너지 3종 비교 (지수화)](./comparison.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Natural Gas (NG=F)](https://finance.yahoo.com/quote/NG=F/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
