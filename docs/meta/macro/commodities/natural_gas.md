# 천연가스 — 기술적 참고 (주봉 5년)

> 최근 5년 헨리허브 천연가스 선물(연속월물, `NG=F`) 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [`oil_wti.md`](./oil_wti.md)와 같은 에너지 원자재지만, 천연가스는 계절(난방 수요) 영향이 커서 변동성 패턴이 원유와 다르다.

---

## 1. 차트 — 최근 5년 주봉

<div class="ng-f-chart">
<style>
.ng-f-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .ng-f-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 $2.76 (2026-08-20) · 단위 USD/MMBtu</text>
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
<line x1="61.9" y1="455.6" x2="61.9" y2="462.9" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="461.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="65.7" y1="427.9" x2="65.7" y2="462.6" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="429.6" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="69.4" y1="407.5" x2="69.4" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="408.4" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="73.2" y1="387.0" x2="73.2" y2="418.0" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="394.4" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="77.0" y1="350.3" x2="77.0" y2="398.1" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="384.1" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="80.7" y1="379.2" x2="80.7" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="381.9" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="84.5" y1="311.3" x2="84.5" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="352.2" width="2.34" height="26.5" fill="var(--up)"/>
<line x1="88.3" y1="299.7" x2="88.3" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="351.7" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="92.1" y1="330.8" x2="92.1" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="347.5" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="95.8" y1="367.1" x2="95.8" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="372.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="99.6" y1="310.6" x2="99.6" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="361.6" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="103.4" y1="336.3" x2="103.4" y2="383.4" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="358.6" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="107.1" y1="349.5" x2="107.1" y2="407.6" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="353.1" width="2.34" height="50.4" fill="var(--down)"/>
<line x1="110.9" y1="366.2" x2="110.9" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="386.5" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="114.7" y1="355.7" x2="114.7" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="362.9" width="2.34" height="33.3" fill="var(--up)"/>
<line x1="118.5" y1="378.2" x2="118.5" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="378.2" width="2.34" height="66.1" fill="var(--down)"/>
<line x1="122.2" y1="454.7" x2="122.2" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="457.2" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="126.0" y1="447.3" x2="126.0" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="454.1" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="129.8" y1="450.0" x2="129.8" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="469.2" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="133.6" y1="436.4" x2="133.6" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="455.1" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="137.3" y1="453.8" x2="137.3" y2="474.9" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="457.7" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="141.1" y1="398.1" x2="141.1" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="436.3" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="144.9" y1="428.4" x2="144.9" y2="466.1" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="430.5" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="148.6" y1="245.2" x2="148.6" y2="460.2" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="412.9" width="2.34" height="44.9" fill="var(--up)"/>
<line x1="152.4" y1="355.1" x2="152.4" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="398.8" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="156.2" y1="423.5" x2="156.2" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="428.7" width="2.34" height="27.4" fill="var(--down)"/>
<line x1="160.0" y1="403.4" x2="160.0" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="425.8" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="163.7" y1="394.3" x2="163.7" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="415.7" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="167.5" y1="387.8" x2="167.5" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="389.6" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="171.3" y1="379.2" x2="171.3" y2="424.6" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="388.0" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="175.0" y1="390.5" x2="175.0" y2="424.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="399.1" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="178.8" y1="354.8" x2="178.8" y2="406.2" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="355.2" width="2.34" height="41.0" fill="var(--up)"/>
<line x1="182.6" y1="339.0" x2="182.6" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="346.0" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="186.4" y1="295.3" x2="186.4" y2="350.3" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="311.4" width="2.34" height="33.0" fill="var(--up)"/>
<line x1="190.1" y1="245.2" x2="190.1" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="248.1" width="2.34" height="56.1" fill="var(--up)"/>
<line x1="193.9" y1="200.7" x2="193.9" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="243.9" width="2.34" height="51.6" fill="var(--down)"/>
<line x1="197.7" y1="240.5" x2="197.7" y2="307.2" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="251.5" width="2.34" height="51.4" fill="var(--up)"/>
<line x1="201.4" y1="143.0" x2="201.4" y2="253.1" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="202.0" width="2.34" height="39.1" fill="var(--up)"/>
<line x1="205.2" y1="186.9" x2="205.2" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="214.4" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="209.0" y1="170.7" x2="209.0" y2="225.6" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="199.6" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="212.8" y1="117.9" x2="212.8" y2="213.9" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="159.7" width="2.34" height="40.1" fill="var(--up)"/>
<line x1="216.5" y1="139.2" x2="216.5" y2="197.4" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="150.5" width="2.34" height="21.7" fill="var(--down)"/>
<line x1="220.3" y1="101.6" x2="220.3" y2="203.7" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="152.0" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="224.1" y1="145.8" x2="224.1" y2="274.0" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="147.7" width="2.34" height="122.4" fill="var(--down)"/>
<line x1="227.8" y1="268.1" x2="227.8" y2="327.3" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="279.0" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="231.6" y1="277.0" x2="231.6" y2="368.4" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="320.8" width="2.34" height="24.5" fill="var(--down)"/>
<line x1="235.4" y1="305.0" x2="235.4" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="326.5" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="239.2" y1="257.7" x2="239.2" y2="327.7" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="265.7" width="2.34" height="35.3" fill="var(--up)"/>
<line x1="242.9" y1="178.9" x2="242.9" y2="261.8" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="186.2" width="2.34" height="70.1" fill="var(--up)"/>
<line x1="246.7" y1="96.1" x2="246.7" y2="204.1" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="180.5" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="250.5" y1="175.0" x2="250.5" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="200.7" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="254.3" y1="143.1" x2="254.3" y2="233.7" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="157.1" width="2.34" height="55.3" fill="var(--up)"/>
<line x1="258.0" y1="100.8" x2="258.0" y2="179.7" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="121.9" width="2.34" height="40.7" fill="var(--up)"/>
<line x1="261.8" y1="79.0" x2="261.8" y2="139.6" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="124.4" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="265.6" y1="100.5" x2="265.6" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="101.2" width="2.34" height="54.8" fill="var(--down)"/>
<line x1="269.3" y1="134.9" x2="269.3" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="141.0" width="2.34" height="63.9" fill="var(--down)"/>
<line x1="273.1" y1="128.0" x2="273.1" y2="222.2" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="203.1" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="276.9" y1="197.1" x2="276.9" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="221.0" width="2.34" height="56.3" fill="var(--down)"/>
<line x1="280.7" y1="258.0" x2="280.7" y2="300.4" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="276.3" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="284.4" y1="255.0" x2="284.4" y2="309.7" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="279.0" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="288.2" y1="272.8" x2="288.2" y2="307.7" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="288.5" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="292.0" y1="309.2" x2="292.0" y2="396.6" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="312.3" width="2.34" height="80.8" fill="var(--down)"/>
<line x1="295.7" y1="335.4" x2="295.7" y2="406.1" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="348.2" width="2.34" height="44.2" fill="var(--up)"/>
<line x1="299.5" y1="297.0" x2="299.5" y2="352.5" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="303.8" width="2.34" height="35.2" fill="var(--up)"/>
<line x1="303.3" y1="253.0" x2="303.3" y2="346.3" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="267.9" width="2.34" height="68.2" fill="var(--down)"/>
<line x1="307.1" y1="294.7" x2="307.1" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="309.8" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="310.8" y1="229.2" x2="310.8" y2="319.6" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="265.2" width="2.34" height="42.8" fill="var(--up)"/>
<line x1="314.6" y1="240.6" x2="314.6" y2="314.9" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="274.7" width="2.34" height="36.5" fill="var(--down)"/>
<line x1="318.4" y1="304.4" x2="318.4" y2="369.7" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="313.4" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="322.1" y1="260.1" x2="322.1" y2="315.0" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="269.8" width="2.34" height="21.7" fill="var(--down)"/>
<line x1="325.9" y1="311.6" x2="325.9" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="319.1" width="2.34" height="66.6" fill="var(--down)"/>
<line x1="329.7" y1="367.8" x2="329.7" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="373.0" width="2.34" height="50.1" fill="var(--down)"/>
<line x1="333.5" y1="428.1" x2="333.5" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="428.2" width="2.34" height="42.3" fill="var(--down)"/>
<line x1="337.2" y1="444.6" x2="337.2" y2="490.7" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="464.3" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="341.0" y1="465.6" x2="341.0" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="480.0" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="344.8" y1="477.6" x2="344.8" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="486.6" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="348.5" y1="528.1" x2="348.5" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="531.8" width="2.34" height="19.2" fill="var(--down)"/>
<line x1="352.3" y1="535.7" x2="352.3" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="544.6" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="356.1" y1="537.8" x2="356.1" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="540.5" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="359.9" y1="540.7" x2="359.9" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="548.5" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="363.6" y1="512.8" x2="363.6" y2="542.1" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="513.9" width="2.34" height="22.2" fill="var(--up)"/>
<line x1="367.4" y1="525.0" x2="367.4" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="525.0" width="2.34" height="24.8" fill="var(--down)"/>
<line x1="371.2" y1="534.7" x2="371.2" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="550.0" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="375.0" y1="550.0" x2="375.0" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="554.9" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="378.7" y1="561.5" x2="378.7" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="563.1" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="382.5" y1="564.2" x2="382.5" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="571.2" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="386.3" y1="561.1" x2="386.3" y2="579.8" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="569.4" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="390.0" y1="552.6" x2="390.0" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="562.0" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="393.8" y1="543.7" x2="393.8" y2="570.2" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="551.0" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="397.6" y1="551.0" x2="397.6" y2="574.5" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="551.8" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="401.4" y1="555.7" x2="401.4" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="560.0" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="405.1" y1="534.0" x2="405.1" y2="560.9" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="540.2" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="408.9" y1="541.2" x2="408.9" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="541.2" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="412.7" y1="548.7" x2="412.7" y2="568.0" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="550.6" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="416.4" y1="552.9" x2="416.4" y2="565.7" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="560.7" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="420.2" y1="536.0" x2="420.2" y2="563.7" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="537.3" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="424.0" y1="530.6" x2="424.0" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="531.3" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="427.8" y1="524.5" x2="427.8" y2="539.7" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="527.0" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="431.5" y1="527.3" x2="431.5" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="531.3" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="435.3" y1="530.0" x2="435.3" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="541.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="439.1" y1="527.6" x2="439.1" y2="546.4" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="532.3" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="442.8" y1="528.9" x2="442.8" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="531.8" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="446.6" y1="533.5" x2="446.6" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="535.6" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="450.4" y1="513.4" x2="450.4" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="528.7" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="454.2" y1="523.0" x2="454.2" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="528.4" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="457.9" y1="535.5" x2="457.9" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="541.7" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="461.7" y1="522.8" x2="461.7" y2="544.5" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="529.0" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="465.5" y1="532.6" x2="465.5" y2="545.5" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="533.1" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="469.2" y1="525.4" x2="469.2" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="536.5" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="473.0" y1="522.4" x2="473.0" y2="539.6" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="537.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="476.8" y1="514.7" x2="476.8" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="518.9" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="480.6" y1="491.9" x2="480.6" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="493.5" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="484.3" y1="485.3" x2="484.3" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="492.8" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="488.1" y1="503.0" x2="488.1" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="503.0" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="491.9" y1="489.6" x2="491.9" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="504.3" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="495.7" y1="475.4" x2="495.7" y2="494.8" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="482.6" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="499.4" y1="489.3" x2="499.4" y2="515.2" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="491.4" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="503.2" y1="497.4" x2="503.2" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="510.5" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="507.0" y1="517.1" x2="507.0" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="517.1" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="510.7" y1="522.5" x2="510.7" y2="535.0" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="526.0" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="514.5" y1="527.7" x2="514.5" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="531.3" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="518.3" y1="542.7" x2="518.3" y2="561.9" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="546.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="522.1" y1="538.0" x2="522.1" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="538.6" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="525.8" y1="531.7" x2="525.8" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="542.7" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="529.6" y1="520.3" x2="529.6" y2="544.0" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="521.1" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="533.4" y1="490.2" x2="533.4" y2="533.4" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="495.1" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="537.1" y1="502.8" x2="537.1" y2="544.6" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="507.5" width="2.34" height="36.8" fill="var(--down)"/>
<line x1="540.9" y1="521.7" x2="540.9" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="532.3" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="544.7" y1="529.3" x2="544.7" y2="575.1" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="534.3" width="2.34" height="37.2" fill="var(--down)"/>
<line x1="548.5" y1="568.6" x2="548.5" y2="587.8" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="569.6" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="552.2" y1="584.9" x2="552.2" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="588.5" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="556.0" y1="589.3" x2="556.0" y2="606.1" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="601.0" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="559.8" y1="581.5" x2="559.8" y2="606.7" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="586.7" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="563.5" y1="575.9" x2="563.5" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="584.3" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="567.3" y1="586.3" x2="567.3" y2="598.6" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="588.5" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="571.1" y1="590.7" x2="571.1" y2="598.3" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="595.7" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="574.9" y1="589.5" x2="574.9" y2="608.6" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="591.1" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="578.6" y1="582.3" x2="578.6" y2="594.7" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="589.8" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="582.4" y1="580.0" x2="582.4" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="590.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="586.2" y1="588.5" x2="586.2" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="590.6" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="589.9" y1="585.9" x2="589.9" y2="608.5" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="591.0" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="593.7" y1="566.5" x2="593.7" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="567.6" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="597.5" y1="555.1" x2="597.5" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="560.8" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="601.3" y1="535.9" x2="601.3" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="537.7" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="605.0" y1="519.2" x2="605.0" y2="545.9" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="535.6" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="608.8" y1="534.2" x2="608.8" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="540.1" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="612.6" y1="516.5" x2="612.6" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="519.6" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="616.3" y1="504.6" x2="616.3" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="515.7" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="620.1" y1="517.7" x2="620.1" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="524.0" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="623.9" y1="524.1" x2="623.9" y2="539.6" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="534.9" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="627.7" y1="539.1" x2="627.7" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="540.7" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="631.4" y1="548.7" x2="631.4" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="556.1" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="635.2" y1="558.8" x2="635.2" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="559.5" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="639.0" y1="559.7" x2="639.0" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="570.0" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="642.8" y1="567.2" x2="642.8" y2="585.4" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="575.4" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="646.5" y1="564.8" x2="646.5" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="567.6" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="650.3" y1="557.8" x2="650.3" y2="569.6" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="565.7" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="654.1" y1="559.2" x2="654.1" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="568.7" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="657.8" y1="565.8" x2="657.8" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="568.6" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="661.6" y1="558.2" x2="661.6" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="559.4" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="665.4" y1="551.2" x2="665.4" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="557.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="669.2" y1="547.9" x2="669.2" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="549.5" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="672.9" y1="518.7" x2="672.9" y2="548.1" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="520.6" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="676.7" y1="513.3" x2="676.7" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="520.7" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="680.5" y1="524.5" x2="680.5" y2="540.0" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="525.2" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="684.2" y1="537.7" x2="684.2" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="537.8" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="688.0" y1="540.4" x2="688.0" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="541.7" width="2.34" height="21.1" fill="var(--up)"/>
<line x1="691.8" y1="519.5" x2="691.8" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="535.4" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="695.6" y1="525.8" x2="695.6" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="535.0" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="699.3" y1="513.2" x2="699.3" y2="533.8" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="525.4" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="703.1" y1="479.6" x2="703.1" y2="524.9" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="506.5" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="706.9" y1="483.5" x2="706.9" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="492.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="710.6" y1="497.2" x2="710.6" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="500.8" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="714.4" y1="479.8" x2="714.4" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="497.1" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="718.2" y1="463.2" x2="718.2" y2="508.8" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="468.1" width="2.34" height="33.3" fill="var(--up)"/>
<line x1="722.0" y1="451.9" x2="722.0" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="460.6" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="725.7" y1="440.1" x2="725.7" y2="494.0" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="473.8" width="2.34" height="18.8" fill="var(--down)"/>
<line x1="729.5" y1="451.4" x2="729.5" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="453.2" width="2.34" height="27.0" fill="var(--up)"/>
<line x1="733.3" y1="429.7" x2="733.3" y2="468.9" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="431.0" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="737.0" y1="449.4" x2="737.0" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="450.8" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="740.8" y1="463.2" x2="740.8" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="465.8" width="2.34" height="45.9" fill="var(--down)"/>
<line x1="744.6" y1="487.5" x2="744.6" y2="504.5" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="495.3" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="748.4" y1="464.9" x2="748.4" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="469.6" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="752.1" y1="423.0" x2="752.1" y2="480.2" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="438.0" width="2.34" height="38.4" fill="var(--up)"/>
<line x1="755.9" y1="439.4" x2="755.9" y2="464.0" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="448.5" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="759.7" y1="418.4" x2="759.7" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="427.8" width="2.34" height="38.4" fill="var(--up)"/>
<line x1="763.5" y1="396.7" x2="763.5" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="423.6" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="767.2" y1="436.5" x2="767.2" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="444.8" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="771.0" y1="446.3" x2="771.0" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="448.5" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="774.8" y1="436.8" x2="774.8" y2="464.2" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="441.6" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="778.5" y1="456.3" x2="778.5" y2="493.7" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="464.2" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="782.3" y1="476.5" x2="782.3" y2="502.6" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="483.5" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="786.1" y1="500.5" x2="786.1" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="502.2" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="789.9" y1="472.8" x2="789.9" y2="523.2" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="475.4" width="2.34" height="46.2" fill="var(--up)"/>
<line x1="793.6" y1="464.0" x2="793.6" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="465.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="797.4" y1="462.4" x2="797.4" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="466.5" width="2.34" height="27.3" fill="var(--down)"/>
<line x1="801.2" y1="482.7" x2="801.2" y2="508.4" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="493.8" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="804.9" y1="478.8" x2="804.9" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="486.8" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="808.7" y1="463.9" x2="808.7" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="465.9" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="812.5" y1="466.8" x2="812.5" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="469.9" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="816.3" y1="443.4" x2="816.3" y2="475.2" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="462.0" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="820.0" y1="455.7" x2="820.0" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="455.7" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="823.8" y1="468.8" x2="823.8" y2="496.3" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="468.9" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="827.6" y1="485.2" x2="827.6" y2="505.2" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="493.2" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="831.3" y1="475.5" x2="831.3" y2="490.7" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="479.5" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="835.1" y1="485.0" x2="835.1" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="485.7" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="838.9" y1="503.0" x2="838.9" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="508.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="842.7" y1="505.3" x2="842.7" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="510.5" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="846.4" y1="514.5" x2="846.4" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="519.7" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="850.2" y1="519.3" x2="850.2" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="522.1" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="854.0" y1="513.1" x2="854.0" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="514.7" width="2.34" height="22.2" fill="var(--up)"/>
<line x1="857.7" y1="506.4" x2="857.7" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="511.5" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="861.5" y1="502.2" x2="861.5" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="509.1" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="865.3" y1="504.1" x2="865.3" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="517.5" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="869.1" y1="516.5" x2="869.1" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="520.1" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="872.8" y1="478.2" x2="872.8" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="494.4" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="876.6" y1="480.4" x2="876.6" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="495.9" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="880.4" y1="505.9" x2="880.4" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="508.3" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="884.2" y1="479.0" x2="884.2" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="495.6" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="887.9" y1="442.8" x2="887.9" y2="502.5" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="444.8" width="2.34" height="44.2" fill="var(--up)"/>
<line x1="891.7" y1="426.5" x2="891.7" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="433.0" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="895.5" y1="409.9" x2="895.5" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="417.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="899.2" y1="410.7" x2="899.2" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="416.6" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="903.0" y1="398.6" x2="903.0" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="399.9" width="2.34" height="23.9" fill="var(--up)"/>
<line x1="906.8" y1="359.8" x2="906.8" y2="405.6" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="372.7" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="910.6" y1="377.9" x2="910.6" y2="448.5" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="384.4" width="2.34" height="61.2" fill="var(--down)"/>
<line x1="914.3" y1="439.0" x2="914.3" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="441.9" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="918.1" y1="415.8" x2="918.1" y2="465.1" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="429.8" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="921.9" y1="407.9" x2="921.9" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="424.6" width="2.34" height="51.5" fill="var(--down)"/>
<line x1="925.6" y1="475.2" x2="925.6" y2="506.4" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="483.1" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="929.4" y1="483.6" x2="929.4" y2="514.1" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="496.5" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="933.2" y1="350.3" x2="933.2" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="373.5" width="2.34" height="110.0" fill="var(--up)"/>
<line x1="937.0" y1="215.4" x2="937.0" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="341.6" width="2.34" height="89.0" fill="var(--down)"/>
<line x1="940.7" y1="468.9" x2="940.7" y2="504.9" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="470.6" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="944.5" y1="494.9" x2="944.5" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="499.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="948.3" y1="503.9" x2="948.3" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="511.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="952.0" y1="498.8" x2="952.0" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="499.6" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="955.8" y1="497.1" x2="955.8" y2="522.7" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="503.0" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="959.6" y1="483.9" x2="959.6" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="495.6" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="963.4" y1="497.8" x2="963.4" y2="519.2" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="503.3" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="967.1" y1="505.0" x2="967.1" y2="522.9" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="507.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="970.9" y1="510.9" x2="970.9" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="511.1" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="974.7" y1="521.4" x2="974.7" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="524.5" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="978.4" y1="531.6" x2="978.4" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="533.6" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="982.2" y1="529.2" x2="982.2" y2="545.8" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="533.8" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="986.0" y1="525.6" x2="986.0" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="528.1" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="989.8" y1="521.7" x2="989.8" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="527.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="993.5" y1="515.6" x2="993.5" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="517.0" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="997.3" y1="505.9" x2="997.3" y2="521.4" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="514.9" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="1001.1" y1="490.4" x2="1001.1" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="496.5" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="1004.9" y1="489.9" x2="1004.9" y2="508.3" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="493.7" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="1008.6" y1="499.1" x2="1008.6" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="503.0" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="1012.4" y1="496.0" x2="1012.4" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="502.2" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="1016.2" y1="487.2" x2="1016.2" y2="506.1" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="497.1" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="1019.9" y1="494.2" x2="1019.9" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="497.1" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="1023.7" y1="492.5" x2="1023.7" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="501.7" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="1027.5" y1="516.5" x2="1027.5" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="518.8" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="1031.3" y1="515.0" x2="1031.3" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="522.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1035.0" y1="524.6" x2="1035.0" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="525.6" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="1038.8" y1="526.3" x2="1038.8" y2="538.3" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="530.3" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="1042.6" y1="525.0" x2="1042.6" y2="532.9" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="531.0" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="1046.3" y1="522.2" x2="1046.3" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="526.0" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="1050.1" y1="526.6" x2="1050.1" y2="530.6" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="528.0" width="2.34" height="1.6" fill="var(--down)"/>
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
<circle cx="1052.0" cy="529.7" r="3" fill="var(--ink)"/>
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

- **상승**: 난방·발전 수요 급증(계절 요인), 공급 차질(파이프라인 문제, LNG 수출 확대에 따른 국내 공급 축소) 신호로 흔히 해석된다.
- **하락**: 온화한 날씨로 인한 수요 둔화, 생산 증가·재고 축적에 따른 공급 과잉 신호로 흔히 해석된다.
- 계절성이 강해 같은 방향의 움직임도 시기(겨울철 vs 여름철)에 따라 의미가 다르다 — 절대가격보다 계절 대비 재고 수준을 함께 봐야 한다.

---

## 갱신 방법

이 문서는 시점이 지나면 낡는 스냅샷이라, 정기적으로(예: 분기 1회) 재생성해 §1을 교체하는 것을 전제로 한다(§2는 손으로 갱신). 손으로 만들지 말고 아래 명령으로 생성할 것:

```bash
uv run python scripts/gen_technical_chart.py "NG=F" --name "천연가스" --interval 1wk \
  --unit-label "USD/MMBtu" \
  --adj-note "선물 원자료(연속월물, 조정 없음) — 만기 롤오버 시 가격 갭 가능" --close-on <YYYY-MM-DD> --emit chart
```

`--symbol`은 기본값($)이 그대로 맞아 생략했다. 커맨드 문법은 [`../../authoring-guide.md`](../../authoring-guide.md) "주가가 아닌 시계열에 쓰기" 참고.

---

## 관련 문서

- [WTI 원유](./oil_wti.md) — 같은 에너지 원자재 짝 지표
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — "주요 지표 읽는 법 요약" 표의 유가·원자재 행
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Natural Gas (NG=F)](https://finance.yahoo.com/quote/NG=F/)

---

*작성일: 2026-08-20*
