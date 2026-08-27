# 유로/달러 환율 (EUR/USD)

!!! note ""
    최근 5년간 유로/달러 환율(1유로가 몇 달러인지, `EURUSD=X`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 달러인덱스에서 가장 큰 비중(약 58%)을 차지하는 통화쌍이 바로 이 유로/달러라서, 달러인덱스가 움직이는 이유의 대부분은 사실상 이 환율이 주도한다고 봐도 된다.

---

## 1. 차트 — 최근 5년 주봉

<div class="eurusd-x-chart">
<style>
.eurusd-x-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .eurusd-x-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eurusd-x-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eurusd-x-chart svg { width:100%; height:auto; display:block; }
.eurusd-x-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eurusd-x-chart .title { fill: var(--ink); font-weight:600; }
.eurusd-x-chart .grid { stroke: var(--grid); stroke-width:1; }
.eurusd-x-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="유로/달러 환율(EURUSD=X) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">유로/달러 환율 (EURUSD=X) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-21 · 마지막 종가 $1.17 (2026-08-21) · 단위 USD/EUR</text>
<line x1="60" y1="551.2" x2="1052" y2="551.2" class="grid"/>
<text x="52" y="555.2" font-size="11" text-anchor="end" fill="var(--muted)">0.95</text>
<line x1="60" y1="457.8" x2="1052" y2="457.8" class="grid"/>
<text x="52" y="461.8" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="364.4" x2="1052" y2="364.4" class="grid"/>
<text x="52" y="368.4" font-size="11" text-anchor="end" fill="var(--muted)">1.05</text>
<line x1="60" y1="270.9" x2="1052" y2="270.9" class="grid"/>
<text x="52" y="274.9" font-size="11" text-anchor="end" fill="var(--muted)">1.10</text>
<line x1="60" y1="177.5" x2="1052" y2="177.5" class="grid"/>
<text x="52" y="181.5" font-size="11" text-anchor="end" fill="var(--muted)">1.15</text>
<line x1="60" y1="84.0" x2="1052" y2="84.0" class="grid"/>
<text x="52" y="88.0" font-size="11" text-anchor="end" fill="var(--muted)">1.20</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.3" y1="56.0" x2="137.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="137.3" y1="626.0" x2="137.3" y2="631.0" class="axis"/>
<text x="137.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="333.5" y1="56.0" x2="333.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="333.5" y1="626.0" x2="333.5" y2="631.0" class="axis"/>
<text x="333.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="529.6" y1="56.0" x2="529.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="529.6" y1="626.0" x2="529.6" y2="631.0" class="axis"/>
<text x="529.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="729.5" y1="56.0" x2="729.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="729.5" y1="626.0" x2="729.5" y2="631.0" class="axis"/>
<text x="729.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.6" y1="56.0" x2="925.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="925.6" y1="626.0" x2="925.6" y2="631.0" class="axis"/>
<text x="925.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="139.7" x2="61.9" y2="140.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="140.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="120.7" x2="65.7" y2="140.9" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="122.1" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="69.4" y1="101.3" x2="69.4" y2="124.3" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="105.6" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="73.2" y1="105.0" x2="73.2" y2="120.8" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="105.3" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="77.0" y1="112.6" x2="77.0" y2="135.1" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="119.1" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="80.7" y1="130.6" x2="80.7" y2="143.1" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="134.7" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="84.5" y1="134.9" x2="84.5" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="136.0" width="2.34" height="23.4" fill="var(--down)"/>
<line x1="88.3" y1="151.3" x2="88.3" y2="171.8" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="157.4" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="92.1" y1="154.1" x2="92.1" y2="171.8" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="158.9" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="95.8" y1="145.7" x2="95.8" y2="163.8" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="149.8" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="99.6" y1="141.4" x2="99.6" y2="168.8" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="151.1" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="103.4" y1="155.6" x2="103.4" y2="174.8" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="166.4" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="107.1" y1="157.1" x2="107.1" y2="189.8" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="164.7" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="110.9" y1="184.2" x2="110.9" y2="223.7" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="188.3" width="2.34" height="30.0" fill="var(--down)"/>
<line x1="114.7" y1="210.7" x2="114.7" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="216.1" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="118.5" y1="199.6" x2="118.5" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="212.1" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="122.2" y1="206.3" x2="122.2" y2="227.7" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="211.7" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="126.0" y1="203.0" x2="126.0" y2="226.1" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="212.8" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="129.8" y1="206.3" x2="129.8" y2="226.6" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="207.1" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="133.6" y1="200.1" x2="133.6" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="200.8" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="137.3" y1="200.7" x2="137.3" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="201.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="141.1" y1="180.5" x2="141.1" y2="217.0" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="193.1" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="144.9" y1="189.7" x2="144.9" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="193.9" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="148.6" y1="207.2" x2="148.6" y2="247.9" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="207.2" width="2.34" height="36.0" fill="var(--down)"/>
<line x1="152.4" y1="180.5" x2="152.4" y2="243.8" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="186.7" width="2.34" height="56.0" fill="var(--up)"/>
<line x1="156.2" y1="178.5" x2="156.2" y2="205.4" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="186.0" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="160.0" y1="197.4" x2="160.0" y2="216.2" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="202.5" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="163.7" y1="198.8" x2="163.7" y2="250.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="211.6" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="167.5" y1="225.2" x2="167.5" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="237.1" width="2.34" height="43.0" fill="var(--down)"/>
<line x1="171.3" y1="249.2" x2="171.3" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="287.3" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="175.0" y1="248.9" x2="175.0" y2="289.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="258.9" width="2.34" height="24.6" fill="var(--up)"/>
<line x1="178.8" y1="258.4" x2="178.8" y2="278.1" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="263.0" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="182.6" y1="236.7" x2="182.6" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="261.6" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="186.4" y1="260.3" x2="186.4" y2="301.4" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="262.1" width="2.34" height="32.0" fill="var(--down)"/>
<line x1="190.1" y1="283.5" x2="190.1" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="292.4" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="193.9" y1="283.1" x2="193.9" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="305.4" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="197.7" y1="306.0" x2="197.7" y2="369.4" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="306.2" width="2.34" height="49.5" fill="var(--down)"/>
<line x1="201.4" y1="338.2" x2="201.4" y2="367.1" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="355.1" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="205.2" y1="348.3" x2="205.2" y2="392.0" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="358.3" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="209.0" y1="345.9" x2="209.0" y2="384.7" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="352.4" width="2.34" height="30.6" fill="var(--up)"/>
<line x1="212.8" y1="314.8" x2="212.8" y2="351.5" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="319.7" width="2.34" height="31.6" fill="var(--up)"/>
<line x1="216.5" y1="311.1" x2="216.5" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="321.1" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="220.3" y1="313.9" x2="220.3" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="322.1" width="2.34" height="38.3" fill="var(--down)"/>
<line x1="224.1" y1="354.7" x2="224.1" y2="386.3" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="365.0" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="227.8" y1="345.1" x2="227.8" y2="369.6" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="353.4" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="231.6" y1="343.0" x2="231.6" y2="388.7" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="352.0" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="235.4" y1="371.2" x2="235.4" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="376.7" width="2.34" height="46.1" fill="var(--down)"/>
<line x1="239.2" y1="426.4" x2="239.2" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="426.8" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="242.9" y1="406.3" x2="242.9" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="417.5" width="2.34" height="22.3" fill="var(--up)"/>
<line x1="246.7" y1="409.9" x2="246.7" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="415.4" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="250.5" y1="403.0" x2="250.5" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="418.9" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="254.3" y1="388.8" x2="254.3" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="408.5" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="258.0" y1="407.9" x2="258.0" y2="451.0" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="409.9" width="2.34" height="40.0" fill="var(--down)"/>
<line x1="261.8" y1="441.3" x2="261.8" y2="475.9" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="451.2" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="265.6" y1="443.3" x2="265.6" y2="473.7" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="465.4" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="269.3" y1="428.8" x2="269.3" y2="483.0" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="428.8" width="2.34" height="46.0" fill="var(--up)"/>
<line x1="273.1" y1="421.0" x2="273.1" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="444.5" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="276.9" y1="448.4" x2="276.9" y2="515.6" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="453.6" width="2.34" height="62.0" fill="var(--down)"/>
<line x1="280.7" y1="485.8" x2="280.7" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="494.3" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="284.4" y1="458.9" x2="284.4" y2="507.9" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="496.5" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="288.2" y1="494.5" x2="288.2" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="507.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="292.0" y1="481.4" x2="292.0" y2="512.5" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="483.4" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="295.7" y1="440.1" x2="295.7" y2="493.5" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="464.1" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="299.5" y1="460.6" x2="299.5" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="460.6" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="303.3" y1="387.8" x2="303.3" y2="472.9" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="387.8" width="2.34" height="83.3" fill="var(--up)"/>
<line x1="307.1" y1="368.9" x2="307.1" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="393.0" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="310.8" y1="374.0" x2="310.8" y2="415.4" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="380.1" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="314.6" y1="355.9" x2="314.6" y2="403.2" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="357.2" width="2.34" height="32.0" fill="var(--up)"/>
<line x1="318.4" y1="346.8" x2="318.4" y2="374.9" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="355.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="322.1" y1="322.2" x2="322.1" y2="363.0" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="345.5" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="325.9" y1="332.4" x2="325.9" y2="349.9" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="333.0" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="329.7" y1="321.7" x2="329.7" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="321.7" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="333.5" y1="324.7" x2="333.5" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="325.2" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="337.2" y1="295.6" x2="337.2" y2="335.8" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="299.0" width="2.34" height="36.1" fill="var(--up)"/>
<line x1="341.0" y1="292.5" x2="341.0" y2="314.5" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="293.5" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="344.8" y1="283.5" x2="344.8" y2="301.0" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="294.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="348.5" y1="266.0" x2="348.5" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="294.9" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="352.3" y1="308.2" x2="352.3" y2="332.7" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="310.0" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="356.1" y1="308.6" x2="356.1" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="323.0" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="359.9" y1="326.0" x2="359.9" y2="357.3" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="329.9" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="363.6" y1="328.7" x2="363.6" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="336.0" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="367.4" y1="327.2" x2="367.4" y2="359.4" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="334.7" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="371.2" y1="311.7" x2="371.2" y2="360.6" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="316.9" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="375.0" y1="284.2" x2="375.0" y2="339.6" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="311.5" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="378.7" y1="284.8" x2="378.7" y2="318.0" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="294.9" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="382.5" y1="271.4" x2="382.5" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="271.4" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="386.3" y1="251.3" x2="386.3" y2="302.2" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="251.3" width="2.34" height="35.8" fill="var(--up)"/>
<line x1="390.0" y1="252.5" x2="390.0" y2="287.6" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="252.5" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="393.8" y1="246.9" x2="393.8" y2="277.3" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="246.9" width="2.34" height="25.4" fill="var(--up)"/>
<line x1="397.6" y1="231.3" x2="397.6" y2="281.5" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="231.3" width="2.34" height="37.6" fill="var(--up)"/>
<line x1="401.4" y1="260.9" x2="401.4" y2="297.9" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="267.4" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="405.1" y1="288.9" x2="405.1" y2="315.6" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="298.4" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="408.9" y1="302.6" x2="408.9" y2="326.6" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="304.0" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="412.7" y1="312.2" x2="412.7" y2="336.0" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="321.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="416.4" y1="310.6" x2="416.4" y2="333.1" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="314.5" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="420.2" y1="276.3" x2="420.2" y2="320.6" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="277.9" width="2.34" height="39.5" fill="var(--up)"/>
<line x1="424.0" y1="268.8" x2="424.0" y2="299.9" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="281.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="427.8" y1="275.4" x2="427.8" y2="301.5" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="286.2" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="431.5" y1="275.5" x2="431.5" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="275.5" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="435.3" y1="224.5" x2="435.3" y2="281.3" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="224.5" width="2.34" height="52.1" fill="var(--up)"/>
<line x1="439.1" y1="219.4" x2="439.1" y2="250.4" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="228.4" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="442.8" y1="242.5" x2="442.8" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="247.5" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="446.6" y1="262.4" x2="446.6" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="266.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="450.4" y1="260.0" x2="450.4" y2="283.8" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="270.4" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="454.2" y1="278.3" x2="454.2" y2="299.6" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="281.3" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="457.9" y1="283.6" x2="457.9" y2="314.5" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="294.2" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="461.7" y1="281.1" x2="461.7" y2="311.4" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="308.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="465.5" y1="306.6" x2="465.5" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="312.8" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="469.2" y1="314.8" x2="469.2" y2="339.2" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="323.6" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="473.0" y1="321.9" x2="473.0" y2="342.8" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="331.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="476.8" y1="335.3" x2="476.8" y2="365.9" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="336.6" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="480.6" y1="345.3" x2="480.6" y2="373.7" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="345.3" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="484.3" y1="338.4" x2="484.3" y2="365.1" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="351.8" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="488.1" y1="345.0" x2="488.1" y2="361.3" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="345.0" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="491.9" y1="328.8" x2="491.9" y2="359.4" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="347.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="495.7" y1="319.7" x2="495.7" y2="360.1" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="319.7" width="2.34" height="33.0" fill="var(--up)"/>
<line x1="499.4" y1="316.3" x2="499.4" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="321.0" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="503.2" y1="286.2" x2="503.2" y2="333.4" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="286.2" width="2.34" height="42.6" fill="var(--up)"/>
<line x1="507.0" y1="277.0" x2="507.0" y2="298.1" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="280.2" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="510.7" y1="267.8" x2="510.7" y2="609.0" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="282.0" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="514.5" y1="292.0" x2="514.5" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="291.8" width="2.34" height="21.2" fill="var(--down)"/>
<line x1="518.3" y1="269.8" x2="518.3" y2="318.9" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="288.0" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="522.1" y1="263.3" x2="522.1" y2="290.6" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="266.0" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="525.8" y1="244.9" x2="525.8" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="260.5" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="529.6" y1="260.9" x2="529.6" y2="293.4" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="260.5" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="533.4" y1="272.5" x2="533.4" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="277.7" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="537.1" y1="278.6" x2="537.1" y2="299.8" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="281.1" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="540.9" y1="283.7" x2="540.9" y2="305.8" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="291.0" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="544.7" y1="290.0" x2="544.7" y2="312.0" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="300.2" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="548.5" y1="309.3" x2="548.5" y2="322.4" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="310.9" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="552.2" y1="307.3" x2="552.2" y2="327.8" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="308.6" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="556.0" y1="292.2" x2="556.0" y2="315.3" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="301.7" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="559.8" y1="295.9" x2="559.8" y2="308.5" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="298.6" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="563.5" y1="275.0" x2="563.5" y2="301.1" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="281.1" width="2.34" height="19.3" fill="var(--up)"/>
<line x1="567.3" y1="279.4" x2="567.3" y2="294.5" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="281.6" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="571.1" y1="281.3" x2="571.1" y2="306.6" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="292.9" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="574.9" y1="296.3" x2="574.9" y2="314.1" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="306.9" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="578.6" y1="294.1" x2="578.6" y2="322.2" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="299.0" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="582.4" y1="291.8" x2="582.4" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="302.6" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="586.2" y1="328.5" x2="586.2" y2="344.9" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="333.0" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="589.9" y1="317.1" x2="589.9" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="326.2" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="593.7" y1="306.5" x2="593.7" y2="336.3" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="313.2" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="597.5" y1="309.5" x2="597.5" y2="322.3" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="310.4" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="601.3" y1="290.2" x2="601.3" y2="314.6" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="290.4" width="2.34" height="23.4" fill="var(--up)"/>
<line x1="605.0" y1="292.4" x2="605.0" y2="307.1" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="294.2" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="608.8" y1="291.6" x2="608.8" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="297.5" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="612.6" y1="286.2" x2="612.6" y2="307.4" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="298.4" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="616.3" y1="298.6" x2="616.3" y2="332.9" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="312.2" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="620.1" y1="315.5" x2="620.1" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="326.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="623.9" y1="318.2" x2="623.9" y2="333.0" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="323.0" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="627.7" y1="297.9" x2="627.7" y2="325.0" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="297.9" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="631.4" y1="285.5" x2="631.4" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="285.5" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="635.2" y1="280.8" x2="635.2" y2="294.8" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="290.6" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="639.0" y1="289.3" x2="639.0" y2="303.3" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="289.8" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="642.8" y1="284.7" x2="642.8" y2="312.4" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="285.5" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="646.5" y1="269.5" x2="646.5" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="285.1" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="650.3" y1="261.9" x2="650.3" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="264.1" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="654.1" y1="231.8" x2="654.1" y2="266.5" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="231.8" width="2.34" height="34.5" fill="var(--up)"/>
<line x1="657.8" y1="233.3" x2="657.8" y2="260.8" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="235.8" width="2.34" height="23.5" fill="var(--down)"/>
<line x1="661.6" y1="243.0" x2="661.6" y2="264.6" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="253.4" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="665.4" y1="251.8" x2="665.4" y2="270.4" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="254.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="669.2" y1="237.0" x2="669.2" y2="257.7" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="238.1" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="672.9" y1="231.2" x2="672.9" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="239.3" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="676.7" y1="232.0" x2="676.7" y2="279.1" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="239.2" width="2.34" height="34.9" fill="var(--down)"/>
<line x1="680.5" y1="271.4" x2="680.5" y2="287.0" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="275.7" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="684.2" y1="282.2" x2="684.2" y2="305.7" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="284.9" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="688.0" y1="295.3" x2="688.0" y2="315.3" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="295.5" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="691.8" y1="288.8" x2="691.8" y2="313.8" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="292.9" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="695.6" y1="283.4" x2="695.6" y2="330.0" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="294.4" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="699.3" y1="321.7" x2="699.3" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="324.2" width="2.34" height="31.5" fill="var(--down)"/>
<line x1="703.1" y1="343.4" x2="703.1" y2="394.3" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="358.1" width="2.34" height="21.3" fill="var(--down)"/>
<line x1="706.9" y1="346.5" x2="706.9" y2="377.9" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="349.2" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="710.6" y1="340.7" x2="710.6" y2="371.4" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="349.9" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="714.4" y1="347.0" x2="714.4" y2="372.9" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="352.1" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="718.2" y1="358.2" x2="718.2" y2="393.5" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="362.5" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="722.0" y1="374.0" x2="722.0" y2="385.7" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="376.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="725.7" y1="372.1" x2="725.7" y2="414.5" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="377.6" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="729.5" y1="376.3" x2="729.5" y2="416.5" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="400.7" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="733.3" y1="392.3" x2="733.3" y2="423.5" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="400.6" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="737.0" y1="360.7" x2="737.0" y2="405.6" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="363.2" width="2.34" height="42.8" fill="var(--up)"/>
<line x1="740.8" y1="358.1" x2="740.8" y2="390.1" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="370.4" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="744.6" y1="376.2" x2="744.6" y2="418.0" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="395.4" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="748.4" y1="361.8" x2="748.4" y2="403.1" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="364.6" width="2.34" height="35.0" fill="var(--up)"/>
<line x1="752.1" y1="363.0" x2="752.1" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="366.4" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="755.9" y1="359.0" x2="755.9" y2="386.6" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="369.1" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="759.7" y1="292.3" x2="759.7" y2="384.8" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="301.2" width="2.34" height="79.2" fill="var(--up)"/>
<line x1="763.5" y1="283.1" x2="763.5" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="285.1" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="767.2" y1="279.4" x2="767.2" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="293.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="771.0" y1="292.0" x2="771.0" y2="319.1" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="292.0" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="774.8" y1="246.0" x2="774.8" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="278.1" width="2.34" height="25.7" fill="var(--up)"/>
<line x1="778.5" y1="182.7" x2="778.5" y2="291.1" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="203.4" width="2.34" height="70.4" fill="var(--up)"/>
<line x1="782.3" y1="191.5" x2="782.3" y2="217.5" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="196.8" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="786.1" y1="168.8" x2="786.1" y2="211.8" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="175.1" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="789.9" y1="192.5" x2="789.9" y2="221.0" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="206.8" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="793.6" y1="200.3" x2="793.6" y2="233.6" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="210.5" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="797.4" y1="221.5" x2="797.4" y2="256.9" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="228.0" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="801.2" y1="200.5" x2="801.2" y2="238.5" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="201.5" width="2.34" height="34.4" fill="var(--up)"/>
<line x1="804.9" y1="192.6" x2="804.9" y2="228.5" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="201.2" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="808.7" y1="178.5" x2="808.7" y2="204.4" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="195.0" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="812.5" y1="153.4" x2="812.5" y2="200.9" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="166.9" width="2.34" height="27.8" fill="var(--up)"/>
<line x1="816.3" y1="156.0" x2="816.3" y2="187.1" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="166.9" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="820.0" y1="130.6" x2="820.0" y2="185.8" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="136.3" width="2.34" height="41.1" fill="var(--up)"/>
<line x1="823.8" y1="115.8" x2="823.8" y2="138.4" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="124.9" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="827.6" y1="123.3" x2="827.6" y2="146.5" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="125.0" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="831.3" y1="137.0" x2="831.3" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="143.4" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="835.1" y1="123.7" x2="835.1" y2="156.0" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="131.1" width="2.34" height="21.9" fill="var(--up)"/>
<line x1="838.9" y1="126.9" x2="838.9" y2="197.2" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="129.5" width="2.34" height="30.1" fill="var(--down)"/>
<line x1="842.7" y1="141.0" x2="842.7" y2="171.9" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="149.5" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="846.4" y1="134.4" x2="846.4" y2="160.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="138.6" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="850.2" y1="134.4" x2="850.2" y2="161.9" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="135.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="854.0" y1="136.4" x2="854.0" y2="163.5" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="138.3" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="857.7" y1="129.0" x2="857.7" y2="157.0" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="135.7" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="861.5" y1="125.1" x2="861.5" y2="145.9" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="133.2" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="865.3" y1="107.8" x2="865.3" y2="136.9" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="123.1" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="869.1" y1="117.7" x2="869.1" y2="147.7" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="133.2" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="872.8" y1="125.4" x2="872.8" y2="142.8" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="132.1" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="876.6" y1="134.2" x2="876.6" y2="168.3" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="137.8" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="880.4" y1="134.8" x2="880.4" y2="169.0" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="147.2" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="884.2" y1="144.4" x2="884.2" y2="163.0" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="148.0" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="887.9" y1="146.0" x2="887.9" y2="173.0" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="152.9" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="891.7" y1="160.7" x2="891.7" y2="183.1" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="164.1" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="895.5" y1="148.8" x2="895.5" y2="169.3" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="153.3" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="899.2" y1="155.6" x2="899.2" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="156.0" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="903.0" y1="155.8" x2="903.0" y2="176.9" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="159.4" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="906.8" y1="143.4" x2="906.8" y2="160.6" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="150.0" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="910.6" y1="129.0" x2="910.6" y2="155.6" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="131.4" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="914.3" y1="120.5" x2="914.3" y2="139.3" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="133.1" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="918.1" y1="119.7" x2="918.1" y2="138.1" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="125.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="921.9" y1="123.5" x2="921.9" y2="137.6" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="126.1" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="925.6" y1="131.6" x2="925.6" y2="155.2" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="138.9" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="929.4" y1="140.4" x2="929.4" y2="161.5" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="154.1" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="933.2" y1="116.3" x2="933.2" y2="157.0" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="116.3" width="2.34" height="38.0" fill="var(--up)"/>
<line x1="937.0" y1="79.6" x2="937.0" y2="114.5" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="110.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="940.7" y1="107.4" x2="940.7" y2="127.5" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="112.0" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="944.5" y1="97.4" x2="944.5" y2="118.1" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="107.9" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="948.3" y1="108.2" x2="948.3" y2="132.1" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="108.9" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="952.0" y1="115.0" x2="952.0" y2="127.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="115.8" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="955.8" y1="122.2" x2="955.8" y2="171.5" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="128.9" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="959.6" y1="146.9" x2="959.6" y2="189.7" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="172.7" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="963.4" y1="160.1" x2="963.4" y2="193.2" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="160.1" width="2.34" height="28.9" fill="var(--up)"/>
<line x1="967.1" y1="151.7" x2="967.1" y2="180.3" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="165.6" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="970.9" y1="153.8" x2="970.9" y2="188.0" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="173.4" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="974.7" y1="132.4" x2="974.7" y2="176.2" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="134.7" width="2.34" height="40.6" fill="var(--up)"/>
<line x1="978.4" y1="111.9" x2="978.4" y2="145.4" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="126.2" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="982.2" y1="123.1" x2="982.2" y2="145.1" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="132.8" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="986.0" y1="124.3" x2="986.0" y2="148.3" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="135.0" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="989.8" y1="122.0" x2="989.8" y2="144.3" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="122.6" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="993.5" y1="123.3" x2="993.5" y2="155.4" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="127.2" width="2.34" height="27.1" fill="var(--down)"/>
<line x1="997.3" y1="147.7" x2="997.3" y2="163.0" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="155.6" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="1001.1" y1="142.8" x2="1001.1" y2="161.1" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="147.5" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="1004.9" y1="146.2" x2="1004.9" y2="172.9" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="149.8" width="2.34" height="23.1" fill="var(--down)"/>
<line x1="1008.6" y1="160.4" x2="1008.6" y2="177.3" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="163.1" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="1012.4" y1="154.6" x2="1012.4" y2="192.8" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="157.6" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="1016.2" y1="182.5" x2="1016.2" y2="210.1" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="184.3" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="1019.9" y1="182.8" x2="1019.9" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="187.9" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="1023.7" y1="184.5" x2="1023.7" y2="197.7" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="189.5" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="1027.5" y1="181.5" x2="1027.5" y2="200.1" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="188.4" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="1031.3" y1="186.9" x2="1031.3" y2="202.7" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="191.1" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="1035.0" y1="170.4" x2="1035.0" y2="204.7" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="170.4" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="1038.8" y1="162.6" x2="1038.8" y2="176.9" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="165.6" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="1042.6" y1="161.4" x2="1042.6" y2="175.1" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="164.6" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="1046.3" y1="137.8" x2="1046.3" y2="164.9" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="142.4" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="1050.1" y1="137.3" x2="1050.1" y2="145.2" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="143.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="60" y1="103.8" x2="1052" y2="103.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="107.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$1.19 R1</text>
<text x="1058" y="119.3" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="191.6" x2="1052" y2="191.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="185.6" font-size="11.5" fill="var(--support)" font-weight="600">$1.14 S1</text>
<text x="1058" y="197.6" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="266.5" x2="1052" y2="266.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="260.5" font-size="11.5" fill="var(--support)" font-weight="600">$1.10 S2</text>
<text x="1058" y="272.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="357.8" x2="1052" y2="357.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="351.8" font-size="11.5" fill="var(--support)" font-weight="600">$1.05 S3</text>
<text x="1058" y="363.8" font-size="9.5" fill="var(--muted)">터치 8회</text>
<circle cx="1052.0" cy="144.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="136.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $1.17 (2026-08-21)</text>
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

- **상승**: 유로 강세(달러 약세) — 유로존의 경기·금리에 대한 기대가 좋아졌거나, 미국이 상대적으로 약해졌다는 신호로 흔히 해석한다.
- **하락**: 유로 약세(달러 강세) — 유로존 경기가 둔화되거나, 미국이 상대적으로 강해졌다는 신호로 흔히 해석한다.
- **왜 이렇게 해석되나**: 금리평가이론(interest rate parity, 두 통화의 환율 변화율은 두 나라의 금리 차이와 대략 맞물린다는 이론)에 따르면, 유로존과 미국의 금리 수준 자체보다 그 금리가 앞으로 어떻게 바뀔지에 대한 **상대적인** 기대(ECB가 연준보다 얼마나 더 긴축적이거나 완화적인가)가 환율을 움직이는 핵심 변수다.
- 달러인덱스에서 가장 큰 비중(약 58%)을 차지하는 통화쌍이라 두 문서가 상당 부분 같은 정보를 담고 있다 — 두 문서를 각각 독립된 근거로 중복해서 인용하지 않는다.

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
