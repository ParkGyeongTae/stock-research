# VIX 변동성지수

!!! note ""
    최근 5년 CBOE 변동성지수(S&P 500 옵션 내재변동성 기반, `^VIX`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 특정 회사 문서가 아니라 **여러 회사 문서에서 공통으로 인용하는 거시 참고 차트**다 — 개별 종목 밸류에이션이 아니라 **시장 전체의 위험선호도**를 보여주는 지표라, Bear Case에서 "시장 전체가 리레이팅되면(밸류에이션 배수가 눌리면)" 같은 시나리오의 배경으로 인용한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="vix-chart">
<style>
.vix-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .vix-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .vix-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.vix-chart svg { width:100%; height:auto; display:block; }
.vix-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.vix-chart .title { fill: var(--ink); font-weight:600; }
.vix-chart .grid { stroke: var(--grid); stroke-width:1; }
.vix-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="VIX 변동성지수(^VIX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">VIX 변동성지수 (^VIX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 15.23 (2026-08-20) · 단위 pt</text>
<line x1="60" y1="607.0" x2="1052" y2="607.0" class="grid"/>
<text x="52" y="611.0" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="512.0" x2="1052" y2="512.0" class="grid"/>
<text x="52" y="516.0" font-size="11" text-anchor="end" fill="var(--muted)">20.00</text>
<line x1="60" y1="417.0" x2="1052" y2="417.0" class="grid"/>
<text x="52" y="421.0" font-size="11" text-anchor="end" fill="var(--muted)">30.00</text>
<line x1="60" y1="322.0" x2="1052" y2="322.0" class="grid"/>
<text x="52" y="326.0" font-size="11" text-anchor="end" fill="var(--muted)">40.00</text>
<line x1="60" y1="227.0" x2="1052" y2="227.0" class="grid"/>
<text x="52" y="231.0" font-size="11" text-anchor="end" fill="var(--muted)">50.00</text>
<line x1="60" y1="132.0" x2="1052" y2="132.0" class="grid"/>
<text x="52" y="136.0" font-size="11" text-anchor="end" fill="var(--muted)">60.00</text>
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
<line x1="61.9" y1="475.0" x2="61.9" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="486.0" width="2.34" height="39.7" fill="var(--down)"/>
<line x1="65.7" y1="518.9" x2="65.7" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="523.1" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="69.4" y1="539.8" x2="69.4" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="542.7" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="73.2" y1="501.3" x2="73.2" y2="541.5" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="503.0" width="2.34" height="38.1" fill="var(--up)"/>
<line x1="77.0" y1="497.7" x2="77.0" y2="534.3" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="504.3" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="80.7" y1="428.5" x2="80.7" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="471.6" width="2.34" height="61.8" fill="var(--down)"/>
<line x1="84.5" y1="465.5" x2="84.5" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="501.5" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="88.3" y1="468.5" x2="88.3" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="484.5" width="2.34" height="39.2" fill="var(--down)"/>
<line x1="92.1" y1="504.3" x2="92.1" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="512.7" width="2.34" height="34.5" fill="var(--down)"/>
<line x1="95.8" y1="531.7" x2="95.8" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="537.7" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="99.6" y1="530.4" x2="99.6" y2="560.5" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="547.5" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="103.4" y1="533.8" x2="103.4" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="541.9" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="107.1" y1="513.0" x2="107.1" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="538.3" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="110.9" y1="521.4" x2="110.9" y2="549.7" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="531.9" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="114.7" y1="426.6" x2="114.7" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="430.1" width="2.34" height="99.0" fill="var(--up)"/>
<line x1="118.5" y1="366.5" x2="118.5" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="410.6" width="2.34" height="50.9" fill="var(--up)"/>
<line x1="122.2" y1="409.2" x2="122.2" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="426.6" width="2.34" height="97.8" fill="var(--down)"/>
<line x1="126.0" y1="479.0" x2="126.0" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="497.1" width="2.34" height="21.7" fill="var(--up)"/>
<line x1="129.8" y1="441.8" x2="129.8" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="456.0" width="2.34" height="75.3" fill="var(--down)"/>
<line x1="133.6" y1="517.6" x2="133.6" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="518.0" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="137.3" y1="501.9" x2="137.3" y2="546.8" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="523.8" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="141.1" y1="480.4" x2="141.1" y2="537.1" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="516.0" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="144.9" y1="419.0" x2="144.9" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="427.9" width="2.34" height="72.9" fill="var(--up)"/>
<line x1="148.6" y1="332.1" x2="148.6" y2="446.5" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="434.1" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="152.4" y1="422.6" x2="152.4" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="432.6" width="2.34" height="48.8" fill="var(--down)"/>
<line x1="156.2" y1="407.6" x2="156.2" y2="512.7" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="442.1" width="2.34" height="31.1" fill="var(--up)"/>
<line x1="160.0" y1="397.6" x2="160.0" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="424.9" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="163.7" y1="343.0" x2="163.7" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="399.9" width="2.34" height="40.0" fill="var(--down)"/>
<line x1="167.5" y1="367.7" x2="167.5" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="393.8" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="171.3" y1="345.6" x2="171.3" y2="428.0" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="361.1" width="2.34" height="48.7" fill="var(--down)"/>
<line x1="175.0" y1="380.6" x2="175.0" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="407.2" width="2.34" height="68.0" fill="var(--down)"/>
<line x1="178.8" y1="461.1" x2="178.8" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="463.2" width="2.34" height="41.1" fill="var(--down)"/>
<line x1="182.6" y1="480.4" x2="182.6" y2="524.6" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="491.7" width="2.34" height="23.8" fill="var(--down)"/>
<line x1="186.4" y1="466.6" x2="186.4" y2="526.7" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="501.0" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="190.1" y1="460.9" x2="190.1" y2="503.9" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="482.6" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="193.9" y1="433.4" x2="193.9" y2="514.4" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="434.0" width="2.34" height="35.1" fill="var(--up)"/>
<line x1="197.7" y1="375.8" x2="197.7" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="384.7" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="201.4" y1="353.9" x2="201.4" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="385.2" width="2.34" height="30.0" fill="var(--down)"/>
<line x1="205.2" y1="364.9" x2="205.2" y2="428.6" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="399.0" width="2.34" height="28.8" fill="var(--down)"/>
<line x1="209.0" y1="387.5" x2="209.0" y2="459.7" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="416.9" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="212.8" y1="406.8" x2="212.8" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="426.7" width="2.34" height="31.0" fill="var(--down)"/>
<line x1="216.5" y1="432.7" x2="216.5" y2="470.9" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="441.0" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="220.3" y1="420.5" x2="220.3" y2="476.5" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="438.4" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="224.1" y1="369.0" x2="224.1" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="404.0" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="227.8" y1="402.1" x2="227.8" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="411.0" width="2.34" height="32.3" fill="var(--down)"/>
<line x1="231.6" y1="414.9" x2="231.6" y2="450.5" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="433.2" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="235.4" y1="418.7" x2="235.4" y2="469.9" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="442.0" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="239.2" y1="425.9" x2="239.2" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="451.0" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="242.9" y1="455.9" x2="242.9" y2="489.1" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="466.1" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="246.7" y1="461.6" x2="246.7" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="470.9" width="2.34" height="28.5" fill="var(--down)"/>
<line x1="250.5" y1="467.5" x2="250.5" y2="504.8" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="489.1" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="254.3" y1="489.8" x2="254.3" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="495.5" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="258.0" y1="499.9" x2="258.0" y2="517.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="505.0" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="261.8" y1="456.0" x2="261.8" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="459.2" width="2.34" height="29.9" fill="var(--up)"/>
<line x1="265.6" y1="438.9" x2="265.6" y2="481.7" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="446.8" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="269.3" y1="437.9" x2="269.3" y2="486.9" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="460.1" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="273.1" y1="431.7" x2="273.1" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="452.2" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="276.9" y1="395.1" x2="276.9" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="417.8" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="280.7" y1="370.6" x2="280.7" y2="422.8" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="400.5" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="284.4" y1="387.9" x2="284.4" y2="431.2" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="388.5" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="288.2" y1="374.0" x2="288.2" y2="406.2" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="389.2" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="292.0" y1="392.4" x2="292.0" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="395.4" width="2.34" height="24.5" fill="var(--down)"/>
<line x1="295.7" y1="408.0" x2="295.7" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="410.8" width="2.34" height="46.5" fill="var(--down)"/>
<line x1="299.5" y1="444.8" x2="299.5" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="446.4" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="303.3" y1="449.4" x2="303.3" y2="489.5" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="458.1" width="2.34" height="29.9" fill="var(--down)"/>
<line x1="307.1" y1="452.9" x2="307.1" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="474.1" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="310.8" y1="472.9" x2="310.8" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="473.5" width="2.34" height="33.7" fill="var(--down)"/>
<line x1="314.6" y1="487.0" x2="314.6" y2="522.0" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="492.1" width="2.34" height="28.8" fill="var(--down)"/>
<line x1="318.4" y1="480.8" x2="318.4" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="485.1" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="322.1" y1="456.5" x2="322.1" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="470.2" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="325.9" y1="471.2" x2="325.9" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="487.0" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="329.7" y1="485.4" x2="329.7" y2="502.9" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="496.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="333.5" y1="476.3" x2="333.5" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="482.6" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="337.2" y1="488.6" x2="337.2" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="495.4" width="2.34" height="32.3" fill="var(--down)"/>
<line x1="341.0" y1="495.8" x2="341.0" y2="524.3" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="513.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="344.8" y1="503.5" x2="344.8" y2="531.3" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="510.0" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="348.5" y1="505.3" x2="348.5" y2="539.9" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="514.3" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="352.3" y1="493.6" x2="352.3" y2="526.9" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="507.0" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="356.1" y1="495.9" x2="356.1" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="496.2" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="359.9" y1="477.5" x2="359.9" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="494.9" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="363.6" y1="492.8" x2="363.6" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="493.1" width="2.34" height="33.2" fill="var(--down)"/>
<line x1="367.4" y1="426.8" x2="367.4" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="466.4" width="2.34" height="54.6" fill="var(--up)"/>
<line x1="371.2" y1="409.3" x2="371.2" y2="490.4" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="459.7" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="375.0" y1="427.4" x2="375.0" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="438.2" width="2.34" height="57.3" fill="var(--down)"/>
<line x1="378.7" y1="484.2" x2="378.7" y2="526.1" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="492.5" width="2.34" height="31.8" fill="var(--down)"/>
<line x1="382.5" y1="511.2" x2="382.5" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="514.0" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="386.3" y1="511.5" x2="386.3" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="517.8" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="390.0" y1="533.0" x2="390.0" y2="548.4" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="535.0" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="393.8" y1="513.3" x2="393.8" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="528.9" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="397.6" y1="499.4" x2="397.6" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="538.7" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="401.4" y1="528.1" x2="401.4" y2="546.6" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="533.6" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="405.1" y1="528.2" x2="405.1" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="536.3" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="408.9" y1="504.3" x2="408.9" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="531.5" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="412.7" y1="527.2" x2="412.7" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="535.2" width="2.34" height="28.1" fill="var(--down)"/>
<line x1="416.4" y1="556.7" x2="416.4" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="556.8" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="420.2" y1="558.9" x2="420.2" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="564.8" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="424.0" y1="562.6" x2="424.0" y2="581.1" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="565.6" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="427.8" y1="562.3" x2="427.8" y2="578.9" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="564.9" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="431.5" y1="539.7" x2="431.5" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="561.1" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="435.3" y1="548.0" x2="435.3" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="549.2" width="2.34" height="26.0" fill="var(--down)"/>
<line x1="439.1" y1="566.8" x2="439.1" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="571.1" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="442.8" y1="559.3" x2="442.8" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="566.2" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="446.6" y1="536.5" x2="446.6" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="539.5" width="2.34" height="29.6" fill="var(--up)"/>
<line x1="450.4" y1="529.7" x2="450.4" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="541.5" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="454.2" y1="522.6" x2="454.2" y2="561.7" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="537.7" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="457.9" y1="530.0" x2="457.9" y2="555.2" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="530.7" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="461.7" y1="547.3" x2="461.7" y2="578.3" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="547.7" width="2.34" height="29.9" fill="var(--down)"/>
<line x1="465.5" y1="552.9" x2="465.5" y2="573.0" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="567.6" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="469.2" y1="562.5" x2="469.2" y2="581.5" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="567.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="473.0" y1="535.4" x2="473.0" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="538.6" width="2.34" height="26.6" fill="var(--up)"/>
<line x1="476.8" y1="514.8" x2="476.8" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="535.6" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="480.6" y1="503.6" x2="480.6" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="536.2" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="484.3" y1="504.6" x2="484.3" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="516.4" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="488.1" y1="494.6" x2="488.1" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="495.8" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="491.9" y1="482.7" x2="491.9" y2="524.8" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="494.6" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="495.7" y1="501.0" x2="495.7" y2="560.4" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="501.3" width="2.34" height="59.1" fill="var(--down)"/>
<line x1="499.4" y1="554.0" x2="499.4" y2="567.8" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="555.8" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="503.2" y1="557.7" x2="503.2" y2="572.1" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="558.0" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="507.0" y1="566.1" x2="507.0" y2="583.7" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="566.5" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="510.7" y1="566.1" x2="510.7" y2="583.4" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="577.2" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="514.5" y1="571.3" x2="514.5" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="575.8" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="518.3" y1="577.2" x2="518.3" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="578.0" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="522.1" y1="564.3" x2="522.1" y2="585.2" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="578.2" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="525.8" y1="570.9" x2="525.8" y2="584.6" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="571.2" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="529.6" y1="563.5" x2="529.6" y2="577.5" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="575.2" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="533.4" y1="567.3" x2="533.4" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="569.0" width="2.34" height="12.4" fill="var(--down)"/>
<line x1="537.1" y1="555.7" x2="537.1" y2="575.8" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="567.9" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="540.9" y1="568.0" x2="540.9" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="571.2" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="544.7" y1="556.2" x2="544.7" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="569.2" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="548.5" y1="564.0" x2="548.5" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="565.5" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="552.2" y1="531.6" x2="552.2" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="566.7" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="556.0" y1="548.9" x2="556.0" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="558.6" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="559.8" y1="567.1" x2="559.8" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="567.4" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="563.5" y1="554.5" x2="563.5" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="562.0" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="567.3" y1="549.6" x2="567.3" y2="574.5" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="554.7" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="571.1" y1="560.8" x2="571.1" y2="584.2" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="561.9" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="574.9" y1="572.1" x2="574.9" y2="581.7" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="572.1" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="578.6" y1="541.3" x2="578.6" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="549.7" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="582.4" y1="519.6" x2="582.4" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="537.6" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="586.2" y1="499.1" x2="586.2" y2="547.5" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="524.3" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="589.9" y1="524.2" x2="589.9" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="525.4" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="593.7" y1="547.9" x2="593.7" y2="573.9" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="556.0" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="597.5" y1="568.8" x2="597.5" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="569.2" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="601.3" y1="568.7" x2="601.3" y2="588.9" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="576.0" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="605.0" y1="575.0" x2="605.0" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="585.4" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="608.8" y1="560.6" x2="608.8" y2="584.6" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="579.3" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="612.6" y1="566.1" x2="612.6" y2="587.0" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="577.7" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="616.3" y1="574.0" x2="616.3" y2="589.1" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="577.6" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="620.1" y1="571.1" x2="620.1" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="576.6" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="623.9" y1="570.1" x2="623.9" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="570.4" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="627.7" y1="576.0" x2="627.7" y2="589.5" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="578.7" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="631.4" y1="575.4" x2="631.4" y2="587.0" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="579.4" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="635.2" y1="538.7" x2="635.2" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="545.1" width="2.34" height="35.5" fill="var(--up)"/>
<line x1="639.0" y1="518.1" x2="639.0" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="542.5" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="642.8" y1="420.2" x2="642.8" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="479.8" width="2.34" height="64.6" fill="var(--up)"/>
<line x1="646.5" y1="77.6" x2="646.5" y2="509.5" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="479.8" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="650.3" y1="500.7" x2="650.3" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="504.5" width="2.34" height="56.9" fill="var(--down)"/>
<line x1="654.1" y1="530.4" x2="654.1" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="550.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="657.8" y1="532.0" x2="657.8" y2="561.6" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="547.4" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="661.6" y1="476.3" x2="661.6" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="489.4" width="2.34" height="62.9" fill="var(--up)"/>
<line x1="665.4" y1="498.6" x2="665.4" y2="547.8" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="499.5" width="2.34" height="45.2" fill="var(--down)"/>
<line x1="669.2" y1="517.8" x2="669.2" y2="551.8" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="539.0" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="672.9" y1="540.8" x2="672.9" y2="560.5" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="540.9" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="676.7" y1="504.9" x2="676.7" y2="545.5" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="519.5" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="680.5" y1="482.2" x2="680.5" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="504.8" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="684.2" y1="502.4" x2="684.2" y2="531.1" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="503.8" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="688.0" y1="507.2" x2="688.0" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="508.9" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="691.8" y1="479.5" x2="691.8" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="494.1" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="695.6" y1="482.8" x2="695.6" y2="562.7" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="488.2" width="2.34" height="71.8" fill="var(--down)"/>
<line x1="699.3" y1="535.3" x2="699.3" y2="572.9" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="548.7" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="703.1" y1="523.5" x2="703.1" y2="557.2" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="544.3" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="706.9" y1="552.7" x2="706.9" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="557.3" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="710.6" y1="568.0" x2="710.6" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="568.2" width="2.34" height="12.4" fill="var(--down)"/>
<line x1="714.4" y1="563.9" x2="714.4" y2="576.2" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="570.8" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="718.2" y1="433.0" x2="718.2" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="527.6" width="2.34" height="37.9" fill="var(--up)"/>
<line x1="722.0" y1="511.8" x2="722.0" y2="566.4" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="530.1" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="725.7" y1="516.8" x2="725.7" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="538.5" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="729.5" y1="509.1" x2="729.5" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="516.4" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="733.3" y1="492.6" x2="733.3" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="500.8" width="2.34" height="49.5" fill="var(--down)"/>
<line x1="737.0" y1="547.2" x2="737.0" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="547.2" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="740.8" y1="488.2" x2="740.8" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="523.1" width="2.34" height="22.8" fill="var(--down)"/>
<line x1="744.6" y1="508.0" x2="744.6" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="508.6" width="2.34" height="36.3" fill="var(--down)"/>
<line x1="748.4" y1="538.8" x2="748.4" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="544.5" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="752.1" y1="521.2" x2="752.1" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="529.0" width="2.34" height="25.1" fill="var(--up)"/>
<line x1="755.9" y1="489.2" x2="755.9" y2="537.6" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="515.5" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="759.7" y1="449.7" x2="759.7" y2="519.1" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="480.0" width="2.34" height="33.6" fill="var(--up)"/>
<line x1="763.5" y1="421.1" x2="763.5" y2="497.9" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="467.3" width="2.34" height="27.8" fill="var(--down)"/>
<line x1="767.2" y1="484.0" x2="767.2" y2="520.1" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="484.5" width="2.34" height="34.3" fill="var(--down)"/>
<line x1="771.0" y1="491.3" x2="771.0" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="496.3" width="2.34" height="23.9" fill="var(--up)"/>
<line x1="774.8" y1="268.7" x2="774.8" y2="505.5" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="271.6" width="2.34" height="201.4" fill="var(--up)"/>
<line x1="778.5" y1="130.8" x2="778.5" y2="399.0" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="130.8" width="2.34" height="214.4" fill="var(--down)"/>
<line x1="782.3" y1="367.9" x2="782.3" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="371.8" width="2.34" height="48.5" fill="var(--down)"/>
<line x1="786.1" y1="362.4" x2="786.1" y2="466.0" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="390.9" width="2.34" height="75.1" fill="var(--down)"/>
<line x1="789.9" y1="434.4" x2="789.9" y2="489.8" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="457.4" width="2.34" height="29.2" fill="var(--down)"/>
<line x1="793.6" y1="458.6" x2="793.6" y2="494.6" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="471.6" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="797.4" y1="507.8" x2="797.4" y2="539.1" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="513.5" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="801.2" y1="459.5" x2="801.2" y2="533.8" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="490.2" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="804.9" y1="502.4" x2="804.9" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="506.0" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="808.7" y1="507.7" x2="808.7" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="513.8" width="2.34" height="28.9" fill="var(--down)"/>
<line x1="812.5" y1="493.0" x2="812.5" y2="547.8" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="504.2" width="2.34" height="29.7" fill="var(--up)"/>
<line x1="816.3" y1="495.0" x2="816.3" y2="524.6" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="506.1" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="820.0" y1="488.2" x2="820.0" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="501.1" width="2.34" height="45.9" fill="var(--down)"/>
<line x1="823.8" y1="535.9" x2="823.8" y2="548.7" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="538.7" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="827.6" y1="526.2" x2="827.6" y2="552.9" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="532.6" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="831.3" y1="516.9" x2="831.3" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="533.6" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="835.1" y1="535.9" x2="835.1" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="541.7" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="838.9" y1="494.0" x2="838.9" y2="562.4" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="508.4" width="2.34" height="49.7" fill="var(--up)"/>
<line x1="842.7" y1="516.0" x2="842.7" y2="558.1" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="516.2" width="2.34" height="41.9" fill="var(--down)"/>
<line x1="846.4" y1="544.7" x2="846.4" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="551.8" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="850.2" y1="538.2" x2="850.2" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="552.6" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="854.0" y1="550.3" x2="854.0" y2="567.9" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="556.1" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="857.7" y1="517.9" x2="857.7" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="543.8" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="861.5" y1="551.7" x2="861.5" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="554.0" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="865.3" y1="542.9" x2="865.3" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="555.2" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="869.1" y1="533.5" x2="869.1" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="548.7" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="872.8" y1="537.8" x2="872.8" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="543.8" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="876.6" y1="488.8" x2="876.6" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="496.2" width="2.34" height="46.7" fill="var(--up)"/>
<line x1="880.4" y1="426.6" x2="880.4" y2="525.2" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="504.6" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="884.2" y1="502.3" x2="884.2" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="507.0" width="2.34" height="39.5" fill="var(--down)"/>
<line x1="887.9" y1="525.9" x2="887.9" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="536.3" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="891.7" y1="486.2" x2="891.7" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="520.7" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="895.5" y1="483.2" x2="895.5" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="513.6" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="899.2" y1="433.4" x2="899.2" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="479.4" width="2.34" height="36.6" fill="var(--up)"/>
<line x1="903.0" y1="477.0" x2="903.0" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="486.4" width="2.34" height="60.2" fill="var(--down)"/>
<line x1="906.8" y1="527.9" x2="906.8" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="530.5" width="2.34" height="25.1" fill="var(--down)"/>
<line x1="910.6" y1="532.4" x2="910.6" y2="560.9" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="548.6" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="914.3" y1="531.0" x2="914.3" y2="560.4" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="545.2" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="918.1" y1="557.0" x2="918.1" y2="574.9" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="558.0" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="921.9" y1="555.5" x2="921.9" y2="569.1" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="562.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="925.6" y1="551.4" x2="925.6" y2="564.9" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="558.2" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="929.4" y1="530.0" x2="929.4" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="549.4" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="933.2" y1="502.6" x2="933.2" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="512.6" width="2.34" height="36.6" fill="var(--down)"/>
<line x1="937.0" y1="514.5" x2="937.0" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="536.3" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="940.7" y1="482.5" x2="940.7" y2="549.5" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="508.5" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="944.5" y1="489.2" x2="944.5" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="506.3" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="948.3" y1="483.9" x2="948.3" y2="526.4" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="495.5" width="2.34" height="25.2" fill="var(--down)"/>
<line x1="952.0" y1="492.2" x2="952.0" y2="535.8" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="507.3" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="955.8" y1="417.7" x2="955.8" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="421.8" width="2.34" height="45.9" fill="var(--up)"/>
<line x1="959.6" y1="366.7" x2="959.6" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="368.4" width="2.34" height="75.3" fill="var(--down)"/>
<line x1="963.4" y1="423.8" x2="963.4" y2="498.0" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="447.6" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="967.1" y1="401.3" x2="967.1" y2="509.3" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="407.0" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="970.9" y1="402.6" x2="970.9" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="409.5" width="2.34" height="65.7" fill="var(--down)"/>
<line x1="974.7" y1="436.0" x2="974.7" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="465.2" width="2.34" height="54.2" fill="var(--down)"/>
<line x1="978.4" y1="497.0" x2="978.4" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="500.9" width="2.34" height="35.1" fill="var(--down)"/>
<line x1="982.2" y1="497.2" x2="982.2" y2="526.6" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="516.0" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="986.0" y1="517.4" x2="986.0" y2="545.8" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="519.5" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="989.8" y1="520.7" x2="989.8" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="536.9" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="993.5" y1="518.9" x2="993.5" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="526.9" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="997.3" y1="517.3" x2="997.3" y2="545.6" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="519.1" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="1001.1" y1="538.3" x2="1001.1" y2="557.4" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="542.3" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="1004.9" y1="497.1" x2="1004.9" y2="557.8" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="497.7" width="2.34" height="53.5" fill="var(--up)"/>
<line x1="1008.6" y1="480.3" x2="1008.6" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="509.2" width="2.34" height="24.8" fill="var(--down)"/>
<line x1="1012.4" y1="523.0" x2="1012.4" y2="552.2" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="542.6" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="1016.2" y1="505.2" x2="1016.2" y2="545.3" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="527.1" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="1019.9" y1="517.2" x2="1019.9" y2="552.0" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="525.3" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="1023.7" y1="522.4" x2="1023.7" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="546.2" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="1027.5" y1="516.8" x2="1027.5" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="523.7" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="1031.3" y1="509.1" x2="1031.3" y2="543.9" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="522.5" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="1035.0" y1="503.6" x2="1035.0" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="534.6" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="1038.8" y1="526.9" x2="1038.8" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="549.7" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="1042.6" y1="552.7" x2="1042.6" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="555.7" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="1046.3" y1="549.1" x2="1046.3" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="559.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1050.1" y1="556.6" x2="1050.1" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="557.3" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="60" y1="500.7" x2="1052" y2="500.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="504.2" font-size="11.5" fill="var(--resistance)" font-weight="600">21.19 R1</text>
<text x="1058" y="516.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="486.3" x2="1052" y2="486.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="489.8" font-size="11.5" fill="var(--resistance)" font-weight="600">22.70 R2</text>
<text x="1058" y="501.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="479.9" x2="1052" y2="479.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="483.4" font-size="11.5" fill="var(--resistance)" font-weight="600">23.38 R3</text>
<text x="1058" y="495.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="581.8" x2="1052" y2="581.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="575.8" font-size="11.5" fill="var(--support)" font-weight="600">12.65 S1</text>
<text x="1058" y="587.8" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="591.2" x2="1052" y2="591.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="585.2" font-size="11.5" fill="var(--support)" font-weight="600">11.67 S2</text>
<text x="1058" y="597.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="557.3" r="3" fill="var(--ink)"/>
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

- **상승**: 시장 전체의 위험회피 심리 확대(변동성 확대), 옵션 시장이 향후 가격 변동 위험을 더 크게 반영하고 있다는 신호로 흔히 해석된다. 급등은 대개 특정 이벤트(실적 시즌, 지정학적 충격, 유동성 이벤트)에 짧게 반응하고 빠르게 되돌아가는 경우가 많다.
- **하락**: 위험선호 회복, 시장이 안정 국면에 들어섰다는 신호로 흔히 해석된다.
- **어떻게 계산되나**: VIX는 S&P 500 콜·풋 옵션 가격에서 역산한 향후 30일 내재변동성을 연율화한 지수다 — 특정 종목의 실현 변동성이 아니라 옵션 시장이 가격에 반영한 "기대" 변동성이다. 하락장에서 변동성이 더 크게 튀는 경향(레버리지 효과) 때문에 VIX와 S&P 500은 통계적으로 강한 음의 상관관계를 보인다.
- **평균회귀(mean-reversion) 성향이 강하다** — VIX는 장기적으로 특정 레인지(대략 12~20 안팎)로 되돌아가려는 성향이 알려져 있어, 개별 종목처럼 방향성을 갖고 추세를 이어가는 자산과 같은 방식으로 해석하지 않는다.

---

## 관련 문서

- [거시경제 개념 정리](../../concepts/macroeconomics.md) — 거시 지표를 이 레포에서 어디까지 쓰는지
- [리스크 · 회계 품질 개념 정리](../../concepts/risk-and-quality.md) — 체계적 위험으로서의 거시 리스크
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — CBOE Volatility Index (^VIX)](https://finance.yahoo.com/quote/%5EVIX/)
- [CBOE — VIX Index (원출처)](https://www.cboe.com/tradable_products/vix/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
