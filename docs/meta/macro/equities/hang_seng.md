# 항셍지수 — 기술적 참고 (주봉 5년)

!!! note ""
    최근 5년 항셍지수(홍콩거래소, `^HSI`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 중국 본토 규제·경기와 홍콩 금융시장 유동성이 겹쳐 반영되는 지수라, 중화권 리스크 센티먼트를 볼 때 `nikkei225.md`와 함께 아시아 시장 배경으로 참고한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="hsi-chart">
<style>
.hsi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .hsi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .hsi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.hsi-chart svg { width:100%; height:auto; display:block; }
.hsi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.hsi-chart .title { fill: var(--ink); font-weight:600; }
.hsi-chart .grid { stroke: var(--grid); stroke-width:1; }
.hsi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="항셍지수(^HSI) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">항셍지수 (^HSI) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 25,698.49 (2026-08-20) · 단위 지수</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">14,000</text>
<line x1="60" y1="547.4" x2="1052" y2="547.4" class="grid"/>
<text x="52" y="551.4" font-size="11" text-anchor="end" fill="var(--muted)">16,000</text>
<line x1="60" y1="468.8" x2="1052" y2="468.8" class="grid"/>
<text x="52" y="472.8" font-size="11" text-anchor="end" fill="var(--muted)">18,000</text>
<line x1="60" y1="390.1" x2="1052" y2="390.1" class="grid"/>
<text x="52" y="394.1" font-size="11" text-anchor="end" fill="var(--muted)">20,000</text>
<line x1="60" y1="311.5" x2="1052" y2="311.5" class="grid"/>
<text x="52" y="315.5" font-size="11" text-anchor="end" fill="var(--muted)">22,000</text>
<line x1="60" y1="232.9" x2="1052" y2="232.9" class="grid"/>
<text x="52" y="236.9" font-size="11" text-anchor="end" fill="var(--muted)">24,000</text>
<line x1="60" y1="154.3" x2="1052" y2="154.3" class="grid"/>
<text x="52" y="158.3" font-size="11" text-anchor="end" fill="var(--muted)">26,000</text>
<line x1="60" y1="75.7" x2="1052" y2="75.7" class="grid"/>
<text x="52" y="79.7" font-size="11" text-anchor="end" fill="var(--muted)">28,000</text>
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
<line x1="61.9" y1="184.0" x2="61.9" y2="210.0" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="184.1" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="65.7" y1="155.0" x2="65.7" y2="192.1" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="177.6" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="69.4" y1="140.2" x2="69.4" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="158.1" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="73.2" y1="132.3" x2="73.2" y2="169.0" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="146.2" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="77.0" y1="158.2" x2="77.0" y2="216.2" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="158.8" width="2.34" height="37.9" fill="var(--down)"/>
<line x1="80.7" y1="200.4" x2="80.7" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="207.7" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="84.5" y1="205.6" x2="84.5" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="210.3" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="88.3" y1="191.0" x2="88.3" y2="245.4" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="200.0" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="92.1" y1="176.4" x2="92.1" y2="198.9" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="180.6" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="95.8" y1="145.2" x2="95.8" y2="188.7" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="149.3" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="99.6" y1="145.0" x2="99.6" y2="181.2" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="153.5" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="103.4" y1="168.4" x2="103.4" y2="204.4" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="183.0" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="107.1" y1="172.9" x2="107.1" y2="214.0" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="180.7" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="110.9" y1="164.2" x2="110.9" y2="200.4" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="176.4" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="114.7" y1="189.7" x2="114.7" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="191.3" width="2.34" height="38.4" fill="var(--down)"/>
<line x1="118.5" y1="227.6" x2="118.5" y2="265.3" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="236.4" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="122.2" y1="220.1" x2="122.2" y2="259.8" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="233.1" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="126.0" y1="217.7" x2="126.0" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="223.4" width="2.34" height="41.3" fill="var(--down)"/>
<line x1="129.8" y1="257.1" x2="129.8" y2="285.4" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="263.4" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="133.6" y1="249.0" x2="133.6" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="256.6" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="137.3" y1="248.4" x2="137.3" y2="283.6" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="252.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="141.1" y1="210.8" x2="141.1" y2="256.5" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="217.8" width="2.34" height="33.8" fill="var(--up)"/>
<line x1="144.9" y1="194.3" x2="144.9" y2="234.8" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="194.9" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="148.6" y1="201.6" x2="148.6" y2="252.3" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="205.6" width="2.34" height="44.9" fill="var(--down)"/>
<line x1="152.4" y1="208.9" x2="152.4" y2="253.7" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="210.4" width="2.34" height="37.3" fill="var(--up)"/>
<line x1="156.2" y1="191.6" x2="156.2" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="197.3" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="160.0" y1="199.0" x2="160.0" y2="224.3" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="204.4" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="163.7" y1="223.8" x2="163.7" y2="283.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="228.6" width="2.34" height="52.8" fill="var(--down)"/>
<line x1="167.5" y1="274.7" x2="167.5" y2="317.8" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="279.4" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="171.3" y1="338.0" x2="171.3" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="338.7" width="2.34" height="29.7" fill="var(--down)"/>
<line x1="175.0" y1="325.4" x2="175.0" y2="459.5" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="334.6" width="2.34" height="47.5" fill="var(--up)"/>
<line x1="178.8" y1="294.9" x2="178.8" y2="347.0" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="318.5" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="182.6" y1="296.1" x2="182.6" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="310.0" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="186.4" y1="290.9" x2="186.4" y2="328.5" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="302.6" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="190.1" y1="323.8" x2="190.1" y2="351.3" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="323.8" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="193.9" y1="342.4" x2="193.9" y2="382.9" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="346.7" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="197.7" y1="343.9" x2="197.7" y2="403.3" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="347.3" width="2.34" height="31.6" fill="var(--up)"/>
<line x1="201.4" y1="339.4" x2="201.4" y2="391.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="353.7" width="2.34" height="36.4" fill="var(--down)"/>
<line x1="205.2" y1="386.9" x2="205.2" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="394.1" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="209.0" y1="358.9" x2="209.0" y2="399.4" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="361.9" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="212.8" y1="359.5" x2="212.8" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="362.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="216.5" y1="334.5" x2="216.5" y2="355.4" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="347.6" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="220.3" y1="305.9" x2="220.3" y2="349.6" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="319.1" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="224.1" y1="329.4" x2="224.1" y2="362.7" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="344.4" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="227.8" y1="320.8" x2="227.8" y2="357.2" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="322.6" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="231.6" y1="293.9" x2="231.6" y2="322.6" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="312.4" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="235.4" y1="303.7" x2="235.4" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="322.3" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="239.2" y1="332.3" x2="239.2" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="332.3" width="2.34" height="46.1" fill="var(--down)"/>
<line x1="242.9" y1="346.4" x2="242.9" y2="378.6" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="366.2" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="246.7" y1="352.7" x2="246.7" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="369.8" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="250.5" y1="379.0" x2="250.5" y2="409.2" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="382.2" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="254.3" y1="380.3" x2="254.3" y2="411.0" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="383.2" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="258.0" y1="379.9" x2="258.0" y2="403.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="388.6" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="261.8" y1="382.9" x2="261.8" y2="422.0" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="383.5" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="265.6" y1="383.3" x2="265.6" y2="416.0" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="391.7" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="269.3" y1="413.0" x2="269.3" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="415.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="273.1" y1="410.1" x2="273.1" y2="442.1" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="413.5" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="276.9" y1="434.9" x2="276.9" y2="471.7" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="441.4" width="2.34" height="30.0" fill="var(--down)"/>
<line x1="280.7" y1="465.7" x2="280.7" y2="507.4" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="477.3" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="284.4" y1="462.3" x2="284.4" y2="511.7" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="479.0" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="288.2" y1="490.4" x2="288.2" y2="532.1" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="490.4" width="2.34" height="33.9" fill="var(--down)"/>
<line x1="292.0" y1="511.1" x2="292.0" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="528.5" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="295.7" y1="547.6" x2="295.7" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="551.5" width="2.34" height="40.6" fill="var(--down)"/>
<line x1="299.5" y1="527.2" x2="299.5" y2="602.5" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="541.0" width="2.34" height="52.3" fill="var(--up)"/>
<line x1="303.3" y1="493.6" x2="303.3" y2="549.5" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="495.3" width="2.34" height="50.9" fill="var(--up)"/>
<line x1="307.1" y1="452.5" x2="307.1" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="468.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="310.8" y1="478.2" x2="310.8" y2="496.8" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="482.4" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="314.6" y1="420.1" x2="314.6" y2="514.6" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="442.2" width="2.34" height="65.8" fill="var(--up)"/>
<line x1="318.4" y1="393.0" x2="318.4" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="394.0" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="322.1" y1="395.7" x2="322.1" y2="424.3" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="406.1" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="325.9" y1="398.5" x2="325.9" y2="434.0" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="406.1" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="329.7" y1="386.2" x2="329.7" y2="408.2" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="398.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="333.5" y1="335.3" x2="333.5" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="351.2" width="2.34" height="55.9" fill="var(--up)"/>
<line x1="337.2" y1="320.6" x2="337.2" y2="343.4" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="321.8" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="341.0" y1="309.5" x2="341.0" y2="335.8" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="309.8" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="344.8" y1="284.0" x2="344.8" y2="298.6" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="284.4" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="348.5" y1="287.0" x2="348.5" y2="332.8" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="288.7" width="2.34" height="36.1" fill="var(--down)"/>
<line x1="352.3" y1="325.8" x2="352.3" y2="347.5" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="337.1" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="356.1" y1="338.8" x2="356.1" y2="362.5" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="354.4" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="359.9" y1="351.9" x2="359.9" y2="389.9" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="363.3" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="363.6" y1="361.5" x2="363.6" y2="398.7" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="367.8" width="2.34" height="29.3" fill="var(--up)"/>
<line x1="367.4" y1="350.6" x2="367.4" y2="418.4" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="372.9" width="2.34" height="43.9" fill="var(--down)"/>
<line x1="371.2" y1="398.3" x2="371.2" y2="425.2" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="409.1" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="375.0" y1="385.5" x2="375.0" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="393.5" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="378.7" y1="361.8" x2="378.7" y2="409.4" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="374.4" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="382.5" y1="371.4" x2="382.5" y2="386.2" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="375.2" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="386.3" y1="360.6" x2="386.3" y2="394.6" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="367.9" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="390.0" y1="356.1" x2="390.0" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="375.4" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="393.8" y1="383.5" x2="393.8" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="388.2" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="397.6" y1="378.9" x2="397.6" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="385.3" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="401.4" y1="377.5" x2="401.4" y2="407.1" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="385.1" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="405.1" y1="382.9" x2="405.1" y2="415.6" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="408.8" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="408.9" y1="397.7" x2="408.9" y2="444.4" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="410.6" width="2.34" height="28.8" fill="var(--down)"/>
<line x1="412.7" y1="428.5" x2="412.7" y2="467.0" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="431.4" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="416.4" y1="411.2" x2="416.4" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="414.1" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="420.2" y1="384.0" x2="420.2" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="388.6" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="424.0" y1="390.1" x2="424.0" y2="437.3" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="390.8" width="2.34" height="43.0" fill="var(--down)"/>
<line x1="427.8" y1="420.6" x2="427.8" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="432.7" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="431.5" y1="411.8" x2="431.5" y2="457.8" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="429.3" width="2.34" height="25.0" fill="var(--down)"/>
<line x1="435.3" y1="408.4" x2="435.3" y2="452.3" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="413.2" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="439.1" y1="416.7" x2="439.1" y2="440.8" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="416.7" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="442.8" y1="392.5" x2="442.8" y2="446.7" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="393.4" width="2.34" height="41.2" fill="var(--up)"/>
<line x1="446.6" y1="375.9" x2="446.6" y2="414.9" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="380.8" width="2.34" height="27.4" fill="var(--down)"/>
<line x1="450.4" y1="406.6" x2="450.4" y2="428.3" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="410.8" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="454.2" y1="437.6" x2="454.2" y2="472.7" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="441.3" width="2.34" height="29.3" fill="var(--down)"/>
<line x1="457.9" y1="458.0" x2="457.9" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="464.1" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="461.7" y1="439.6" x2="461.7" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="448.4" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="465.5" y1="433.4" x2="465.5" y2="461.9" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="445.5" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="469.2" y1="454.1" x2="469.2" y2="475.0" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="461.6" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="473.0" y1="464.2" x2="473.0" y2="485.5" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="466.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="476.8" y1="466.9" x2="476.8" y2="494.2" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="466.9" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="480.6" y1="484.3" x2="480.6" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="486.6" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="484.3" y1="457.3" x2="484.3" y2="490.5" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="476.1" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="488.1" y1="474.3" x2="488.1" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="476.5" width="2.34" height="24.8" fill="var(--down)"/>
<line x1="491.9" y1="488.5" x2="491.9" y2="512.8" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="492.4" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="495.7" y1="479.4" x2="495.7" y2="508.9" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="482.0" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="499.4" y1="467.3" x2="499.4" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="472.2" width="2.34" height="27.9" fill="var(--down)"/>
<line x1="503.2" y1="461.9" x2="503.2" y2="503.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="490.2" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="507.0" y1="466.5" x2="507.0" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="483.5" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="510.7" y1="481.4" x2="510.7" y2="514.7" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="481.4" width="2.34" height="33.3" fill="var(--down)"/>
<line x1="514.5" y1="510.4" x2="514.5" y2="541.2" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="511.2" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="518.3" y1="509.5" x2="518.3" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="516.2" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="522.1" y1="513.7" x2="522.1" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="521.0" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="525.8" y1="504.3" x2="525.8" y2="530.1" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="506.2" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="529.6" y1="502.8" x2="529.6" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="502.8" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="533.4" y1="524.1" x2="533.4" y2="545.9" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="524.5" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="537.1" y1="534.2" x2="537.1" y2="579.5" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="537.2" width="2.34" height="37.3" fill="var(--down)"/>
<line x1="540.9" y1="537.4" x2="540.9" y2="594.8" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="549.3" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="544.7" y1="537.2" x2="544.7" y2="570.5" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="545.6" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="548.5" y1="531.3" x2="548.5" y2="573.4" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="557.3" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="552.2" y1="531.9" x2="552.2" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="534.0" width="2.34" height="29.9" fill="var(--up)"/>
<line x1="556.0" y1="512.2" x2="556.0" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="518.8" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="559.8" y1="514.2" x2="559.8" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="520.5" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="563.5" y1="522.0" x2="563.5" y2="543.6" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="522.6" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="567.3" y1="499.6" x2="567.3" y2="531.0" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="519.0" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="571.1" y1="509.1" x2="571.1" y2="534.0" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="520.2" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="574.9" y1="518.7" x2="574.9" y2="533.8" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="526.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="578.6" y1="507.8" x2="578.6" y2="528.5" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="515.5" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="582.4" y1="500.6" x2="582.4" y2="524.6" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="519.0" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="586.2" y1="521.9" x2="586.2" y2="545.6" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="528.2" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="589.9" y1="478.3" x2="589.9" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="482.5" width="2.34" height="48.8" fill="var(--up)"/>
<line x1="593.7" y1="445.0" x2="593.7" y2="481.4" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="450.1" width="2.34" height="29.0" fill="var(--up)"/>
<line x1="597.5" y1="429.7" x2="597.5" y2="457.8" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="430.9" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="601.3" y1="405.8" x2="601.3" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="407.7" width="2.34" height="25.5" fill="var(--up)"/>
<line x1="605.0" y1="401.7" x2="605.0" y2="447.8" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="405.0" width="2.34" height="39.8" fill="var(--down)"/>
<line x1="608.8" y1="429.4" x2="608.8" y2="465.7" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="444.9" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="612.6" y1="440.3" x2="612.6" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="454.3" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="616.3" y1="458.2" x2="616.3" y2="474.7" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="462.3" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="620.1" y1="448.3" x2="620.1" y2="478.5" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="467.6" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="623.9" y1="459.7" x2="623.9" y2="485.1" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="472.4" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="627.7" y1="463.5" x2="627.7" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="476.6" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="631.4" y1="456.3" x2="631.4" y2="493.3" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="457.2" width="2.34" height="24.6" fill="var(--up)"/>
<line x1="635.2" y1="459.2" x2="635.2" y2="493.3" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="460.8" width="2.34" height="30.8" fill="var(--down)"/>
<line x1="639.0" y1="480.2" x2="639.0" y2="511.0" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="489.8" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="642.8" y1="492.0" x2="642.8" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="500.3" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="646.5" y1="498.2" x2="646.5" y2="530.0" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="504.5" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="650.3" y1="489.4" x2="650.3" y2="511.0" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="491.2" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="654.1" y1="481.1" x2="654.1" y2="498.9" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="484.0" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="657.8" y1="460.8" x2="657.8" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="469.2" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="661.6" y1="474.2" x2="661.6" y2="495.0" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="474.2" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="665.4" y1="486.8" x2="665.4" y2="509.5" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="493.6" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="669.2" y1="454.8" x2="669.2" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="458.6" width="2.34" height="39.5" fill="var(--up)"/>
<line x1="672.9" y1="360.9" x2="672.9" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="365.3" width="2.34" height="94.1" fill="var(--up)"/>
<line x1="676.7" y1="282.3" x2="676.7" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="282.6" width="2.34" height="61.4" fill="var(--up)"/>
<line x1="680.5" y1="262.7" x2="680.5" y2="382.6" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="274.2" width="2.34" height="66.7" fill="var(--down)"/>
<line x1="684.2" y1="337.1" x2="684.2" y2="391.0" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="341.8" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="688.0" y1="353.1" x2="688.0" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="361.4" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="691.8" y1="355.1" x2="691.8" y2="379.5" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="366.8" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="695.6" y1="336.9" x2="695.6" y2="375.9" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="361.5" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="699.3" y1="369.8" x2="699.3" y2="416.4" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="380.0" width="2.34" height="32.7" fill="var(--down)"/>
<line x1="703.1" y1="398.7" x2="703.1" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="406.0" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="706.9" y1="403.5" x2="706.9" y2="427.3" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="412.8" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="710.6" y1="392.7" x2="710.6" y2="414.2" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="395.4" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="714.4" y1="348.1" x2="714.4" y2="402.1" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="391.3" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="718.2" y1="388.2" x2="718.2" y2="406.2" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="392.2" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="722.0" y1="382.9" x2="722.0" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="386.6" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="725.7" y1="382.5" x2="725.7" y2="408.1" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="385.2" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="729.5" y1="396.0" x2="729.5" y2="428.0" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="396.1" width="2.34" height="30.8" fill="var(--down)"/>
<line x1="733.3" y1="403.3" x2="733.3" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="406.5" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="737.0" y1="382.1" x2="737.0" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="387.5" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="740.8" y1="376.9" x2="740.8" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="381.3" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="744.6" y1="342.4" x2="744.6" y2="399.4" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="345.6" width="2.34" height="42.6" fill="var(--up)"/>
<line x1="748.4" y1="287.1" x2="748.4" y2="342.0" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="287.1" width="2.34" height="54.9" fill="var(--up)"/>
<line x1="752.1" y1="253.4" x2="752.1" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="253.4" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="755.9" y1="229.9" x2="755.9" y2="283.4" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="253.6" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="759.7" y1="206.6" x2="759.7" y2="290.0" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="223.8" width="2.34" height="43.1" fill="var(--up)"/>
<line x1="763.5" y1="221.4" x2="763.5" y2="264.4" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="228.3" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="767.2" y1="198.5" x2="767.2" y2="249.5" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="224.0" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="771.0" y1="234.2" x2="771.0" y2="262.2" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="242.7" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="774.8" y1="254.3" x2="774.8" y2="286.4" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="264.1" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="778.5" y1="342.5" x2="778.5" y2="419.2" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="354.2" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="782.3" y1="327.1" x2="782.3" y2="356.0" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="335.3" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="786.1" y1="301.0" x2="786.1" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="312.3" width="2.34" height="26.6" fill="var(--up)"/>
<line x1="789.9" y1="290.6" x2="789.9" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="291.7" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="793.6" y1="264.4" x2="793.6" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="277.4" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="797.4" y1="244.3" x2="797.4" y2="272.9" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="258.6" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="801.2" y1="236.2" x2="801.2" y2="269.9" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="248.6" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="804.9" y1="248.5" x2="804.9" y2="265.8" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="252.3" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="808.7" y1="234.8" x2="808.7" y2="285.2" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="241.1" width="2.34" height="29.5" fill="var(--up)"/>
<line x1="812.5" y1="215.6" x2="812.5" y2="241.7" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="233.8" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="816.3" y1="227.7" x2="816.3" y2="264.9" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="241.1" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="820.0" y1="211.9" x2="820.0" y2="261.5" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="221.7" width="2.34" height="37.3" fill="var(--up)"/>
<line x1="823.8" y1="218.2" x2="823.8" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="222.1" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="827.6" y1="213.0" x2="827.6" y2="244.1" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="227.4" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="831.3" y1="198.8" x2="831.3" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="200.4" width="2.34" height="28.5" fill="var(--up)"/>
<line x1="835.1" y1="164.7" x2="835.1" y2="199.7" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="178.3" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="838.9" y1="167.4" x2="838.9" y2="212.9" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="175.5" width="2.34" height="37.4" fill="var(--down)"/>
<line x1="842.7" y1="189.1" x2="842.7" y2="218.3" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="199.1" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="846.4" y1="163.5" x2="846.4" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="183.0" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="850.2" y1="175.3" x2="850.2" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="180.3" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="854.0" y1="157.5" x2="854.0" y2="201.1" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="169.7" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="857.7" y1="162.5" x2="857.7" y2="193.1" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="173.6" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="861.5" y1="131.2" x2="861.5" y2="178.3" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="139.0" width="2.34" height="37.3" fill="var(--up)"/>
<line x1="865.3" y1="112.7" x2="865.3" y2="143.3" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="132.8" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="869.1" y1="129.1" x2="869.1" y2="154.1" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="136.2" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="872.8" y1="100.0" x2="872.8" y2="141.6" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="109.4" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="876.6" y1="109.3" x2="876.6" y2="144.6" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="114.8" width="2.34" height="28.1" fill="var(--down)"/>
<line x1="880.4" y1="150.2" x2="880.4" y2="187.9" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="168.7" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="884.2" y1="139.8" x2="884.2" y2="170.3" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="148.0" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="887.9" y1="131.1" x2="887.9" y2="157.9" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="134.8" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="891.7" y1="135.0" x2="891.7" y2="174.1" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="144.8" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="895.5" y1="107.5" x2="895.5" y2="142.4" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="131.8" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="899.2" y1="133.4" x2="899.2" y2="186.6" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="136.9" width="2.34" height="48.0" fill="var(--down)"/>
<line x1="903.0" y1="148.9" x2="903.0" y2="179.1" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="159.8" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="906.8" y1="143.9" x2="906.8" y2="168.1" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="150.9" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="910.6" y1="148.3" x2="910.6" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="151.6" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="914.3" y1="161.2" x2="914.3" y2="190.2" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="165.4" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="918.1" y1="157.1" x2="918.1" y2="167.2" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="161.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="921.9" y1="140.7" x2="921.9" y2="171.8" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="141.0" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="925.6" y1="120.5" x2="925.6" y2="155.8" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="140.1" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="929.4" y1="106.8" x2="929.4" y2="146.9" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="121.1" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="933.2" y1="119.1" x2="933.2" y2="140.0" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="124.8" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="937.0" y1="73.4" x2="937.0" y2="129.9" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="99.7" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="940.7" y1="110.0" x2="940.7" y2="142.7" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="111.1" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="944.5" y1="99.3" x2="944.5" y2="136.8" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="115.7" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="948.3" y1="125.4" x2="948.3" y2="140.2" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="134.6" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="952.0" y1="108.8" x2="952.0" y2="139.6" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="122.9" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="955.8" y1="138.4" x2="955.8" y2="195.2" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="142.3" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="959.6" y1="148.4" x2="959.6" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="175.3" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="963.4" y1="144.4" x2="963.4" y2="188.8" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="176.4" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="967.1" y1="178.2" x2="967.1" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="195.5" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="970.9" y1="176.7" x2="970.9" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="189.0" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="974.7" y1="151.4" x2="974.7" y2="167.9" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="158.5" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="978.4" y1="138.4" x2="978.4" y2="173.6" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="148.0" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="982.2" y1="133.5" x2="982.2" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="146.2" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="986.0" y1="149.0" x2="986.0" y2="169.6" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="155.2" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="989.8" y1="128.0" x2="989.8" y2="166.4" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="138.8" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="993.5" y1="121.1" x2="993.5" y2="160.3" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="142.1" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="997.3" y1="160.4" x2="997.3" y2="180.2" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="160.6" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="1001.1" y1="163.4" x2="1001.1" y2="204.3" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="169.1" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="1004.9" y1="152.5" x2="1004.9" y2="196.4" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="186.5" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="1008.6" y1="200.0" x2="1008.6" y2="232.9" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="204.7" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="1012.4" y1="191.7" x2="1012.4" y2="242.7" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="193.5" width="2.34" height="42.3" fill="var(--down)"/>
<line x1="1016.2" y1="238.3" x2="1016.2" y2="291.2" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="240.3" width="2.34" height="44.8" fill="var(--down)"/>
<line x1="1019.9" y1="251.9" x2="1019.9" y2="284.6" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="258.4" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="1023.7" y1="213.3" x2="1023.7" y2="263.2" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="226.0" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="1027.5" y1="184.9" x2="1027.5" y2="236.7" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="210.8" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="1031.3" y1="183.1" x2="1031.3" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="195.0" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="1035.0" y1="155.4" x2="1035.0" y2="196.0" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="158.8" width="2.34" height="35.0" fill="var(--up)"/>
<line x1="1038.8" y1="146.9" x2="1038.8" y2="178.3" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="154.8" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="1042.6" y1="151.9" x2="1042.6" y2="190.1" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="161.9" width="2.34" height="27.1" fill="var(--down)"/>
<line x1="1046.3" y1="170.9" x2="1046.3" y2="184.1" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="174.1" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="1050.1" y1="160.5" x2="1050.1" y2="168.7" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="163.0" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="60" y1="118.4" x2="1052" y2="118.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="121.9" font-size="11.5" fill="var(--resistance)" font-weight="600">26,913 R1</text>
<text x="1058" y="133.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="189.0" x2="1052" y2="189.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="183.0" font-size="11.5" fill="var(--support)" font-weight="600">25,116 S1</text>
<text x="1058" y="195.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="235.2" x2="1052" y2="235.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="229.2" font-size="11.5" fill="var(--support)" font-weight="600">23,942 S2</text>
<text x="1058" y="241.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="288.3" x2="1052" y2="288.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="282.3" font-size="11.5" fill="var(--support)" font-weight="600">22,592 S3</text>
<text x="1058" y="294.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="166.1" r="3" fill="var(--ink)"/>
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

- **상승**: 중화권 위험선호 회복, 중국 본토 경기·정책 기대 개선 신호로 흔히 해석된다.
- **하락**: 중국 규제 리스크 부각, 경기 둔화 우려, 자본 유출 우려 신호로 흔히 해석된다.
- 이 레포의 핵심 커버리지(미국 상장 기업)와는 별개 시장이다 — 중화권 매크로 배경 참고용으로만 쓰고, 미국 회사 문서의 밸류에이션 근거로 직접 끌어오지 않는다.

---

## 관련 문서

- [닛케이225](./nikkei225.md) — 아시아 시장 비교군
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Hang Seng Index (^HSI)](https://finance.yahoo.com/quote/%5EHSI/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
