# 우라늄 실물 신탁 (SRUUF)

::: info
최근 5년간 Sprott Physical Uranium Trust(SRUUF) 주간 가격을 지지선·저항선과 함께 정리한 참고 자료다. 우라늄은 별도의 공개 선물시장이 없어(대부분 장기 계약 기반의 비공개 시장에서 거래) 금·구리처럼 원자재 선물 가격을 바로 쓸 수 없다. 대신 이 신탁은 채굴기업 주식이 아니라 **실물 우라늄(U3O8)을 직접 매입해 보관**하는 폐쇄형 신탁이라, 채굴기업 ETF(예: URA)보다 실제 우라늄 가격에 더 가깝게 움직인다.

⚠️ **정확한 우라늄 현물가가 아니다** — 이 신탁의 시장가는 보유한 우라늄의 순자산가치(NAV)와 정확히 일치하지 않고, 수급에 따라 NAV 대비 **프리미엄(더 비싸게)** 또는 **디스카운트(더 싸게)** 거래될 수 있다. 정밀한 우라늄 현물가가 필요하면 UxC·TradeTech 같은 원출처를 따로 확인한다.

:::
---

## 1. 차트 — 최근 5년 주봉

<style>
.sruuf-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .sruuf-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.sruuf-chart svg { width:100%; height:auto; display:block; }
.sruuf-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.sruuf-chart .title { fill: var(--ink); font-weight:600; }
.sruuf-chart .grid { stroke: var(--grid); stroke-width:1; }
.sruuf-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="sruuf-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sprott Physical Uranium Trust(SRUUF) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Sprott Physical Uranium Trust (SRUUF) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-10 · 마지막 종가 $19.67 (2026-09-10) · 단위 USD</text>
<line x1="60" y1="584.1" x2="1052" y2="584.1" class="grid"/>
<text x="52" y="588.1" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="500.3" x2="1052" y2="500.3" class="grid"/>
<text x="52" y="504.3" font-size="11" text-anchor="end" fill="var(--muted)">12.50</text>
<line x1="60" y1="416.4" x2="1052" y2="416.4" class="grid"/>
<text x="52" y="420.4" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="332.6" x2="1052" y2="332.6" class="grid"/>
<text x="52" y="336.6" font-size="11" text-anchor="end" fill="var(--muted)">17.50</text>
<line x1="60" y1="248.8" x2="1052" y2="248.8" class="grid"/>
<text x="52" y="252.8" font-size="11" text-anchor="end" fill="var(--muted)">20.00</text>
<line x1="60" y1="165.0" x2="1052" y2="165.0" class="grid"/>
<text x="52" y="169.0" font-size="11" text-anchor="end" fill="var(--muted)">22.50</text>
<line x1="60" y1="81.1" x2="1052" y2="81.1" class="grid"/>
<text x="52" y="85.1" font-size="11" text-anchor="end" fill="var(--muted)">25.00</text>
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
<line x1="61.9" y1="458.4" x2="61.9" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="491.9" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="65.7" y1="413.1" x2="65.7" y2="507.4" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="413.1" width="2.34" height="70.4" fill="var(--down)"/>
<line x1="69.4" y1="453.7" x2="69.4" y2="550.2" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="500.3" width="2.34" height="33.9" fill="var(--down)"/>
<line x1="73.2" y1="514.0" x2="73.2" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="535.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="77.0" y1="526.8" x2="77.0" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="530.6" width="2.34" height="41.7" fill="var(--down)"/>
<line x1="80.7" y1="507.0" x2="80.7" y2="604.2" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="522.1" width="2.34" height="49.3" fill="var(--up)"/>
<line x1="84.5" y1="467.4" x2="84.5" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="497.9" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="88.3" y1="495.2" x2="88.3" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="501.9" width="2.34" height="44.0" fill="var(--down)"/>
<line x1="92.1" y1="496.2" x2="92.1" y2="558.3" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="531.8" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="95.8" y1="498.6" x2="95.8" y2="533.8" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="505.0" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="99.6" y1="498.3" x2="99.6" y2="533.5" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="501.9" width="2.34" height="26.8" fill="var(--down)"/>
<line x1="103.4" y1="511.0" x2="103.4" y2="546.9" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="518.4" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="107.1" y1="521.1" x2="107.1" y2="561.6" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="521.1" width="2.34" height="34.5" fill="var(--down)"/>
<line x1="110.9" y1="520.4" x2="110.9" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="555.6" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="114.7" y1="545.2" x2="114.7" y2="590.8" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="557.3" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="118.5" y1="547.2" x2="118.5" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="549.7" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="122.2" y1="538.2" x2="122.2" y2="567.3" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="549.9" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="126.0" y1="517.4" x2="126.0" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="517.7" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="129.8" y1="513.7" x2="129.8" y2="537.1" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="513.7" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="133.6" y1="514.0" x2="133.6" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="523.7" width="2.34" height="29.5" fill="var(--down)"/>
<line x1="137.3" y1="534.3" x2="137.3" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="542.5" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="141.1" y1="535.5" x2="141.1" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="543.2" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="144.9" y1="539.5" x2="144.9" y2="557.9" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="550.2" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="148.6" y1="537.1" x2="148.6" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="551.2" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="152.4" y1="497.8" x2="152.4" y2="556.9" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="502.3" width="2.34" height="54.3" fill="var(--up)"/>
<line x1="156.2" y1="479.5" x2="156.2" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="490.2" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="160.0" y1="416.1" x2="160.0" y2="488.5" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="444.3" width="2.34" height="42.2" fill="var(--up)"/>
<line x1="163.7" y1="419.8" x2="163.7" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="448.3" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="167.5" y1="413.1" x2="167.5" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="419.5" width="2.34" height="25.5" fill="var(--up)"/>
<line x1="171.3" y1="408.7" x2="171.3" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="410.7" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="175.0" y1="361.1" x2="175.0" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="387.3" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="178.8" y1="382.2" x2="178.8" y2="415.8" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="386.3" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="182.6" y1="366.1" x2="182.6" y2="493.6" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="392.6" width="2.34" height="83.2" fill="var(--down)"/>
<line x1="186.4" y1="466.1" x2="186.4" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="477.1" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="190.1" y1="458.4" x2="190.1" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="487.9" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="193.9" y1="496.9" x2="193.9" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="496.9" width="2.34" height="33.2" fill="var(--down)"/>
<line x1="197.7" y1="493.9" x2="197.7" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="530.1" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="201.4" y1="466.7" x2="201.4" y2="537.1" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="522.1" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="205.2" y1="475.1" x2="205.2" y2="529.4" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="500.9" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="209.0" y1="470.8" x2="209.0" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="489.2" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="212.8" y1="515.4" x2="212.8" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="517.0" width="2.34" height="55.7" fill="var(--down)"/>
<line x1="216.5" y1="550.6" x2="216.5" y2="589.8" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="559.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="220.3" y1="536.5" x2="220.3" y2="578.7" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="536.5" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="224.1" y1="542.8" x2="224.1" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="552.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="227.8" y1="558.1" x2="227.8" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="559.0" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="231.6" y1="543.2" x2="231.6" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="567.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="235.4" y1="519.4" x2="235.4" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="527.4" width="2.34" height="33.9" fill="var(--up)"/>
<line x1="239.2" y1="517.0" x2="239.2" y2="555.4" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="526.4" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="242.9" y1="518.0" x2="242.9" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="540.8" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="246.7" y1="541.8" x2="246.7" y2="580.1" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="567.3" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="250.5" y1="510.0" x2="250.5" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="524.7" width="2.34" height="50.6" fill="var(--up)"/>
<line x1="254.3" y1="489.5" x2="254.3" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="509.7" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="258.0" y1="479.8" x2="258.0" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="483.5" width="2.34" height="25.1" fill="var(--up)"/>
<line x1="261.8" y1="478.5" x2="261.8" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="480.1" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="265.6" y1="517.0" x2="265.6" y2="563.6" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="521.1" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="269.3" y1="521.1" x2="269.3" y2="567.3" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="525.4" width="2.34" height="41.9" fill="var(--up)"/>
<line x1="273.1" y1="501.9" x2="273.1" y2="534.1" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="524.4" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="276.9" y1="499.8" x2="276.9" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="506.0" width="2.34" height="34.2" fill="var(--up)"/>
<line x1="280.7" y1="479.1" x2="280.7" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="482.2" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="284.4" y1="475.1" x2="284.4" y2="503.6" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="478.5" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="288.2" y1="471.8" x2="288.2" y2="514.0" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="488.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="292.0" y1="474.4" x2="292.0" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="490.2" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="295.7" y1="483.5" x2="295.7" y2="546.5" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="486.9" width="2.34" height="51.0" fill="var(--down)"/>
<line x1="299.5" y1="528.8" x2="299.5" y2="546.5" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="537.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="303.3" y1="529.1" x2="303.3" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="530.4" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="307.1" y1="538.3" x2="307.1" y2="568.3" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="538.3" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="310.8" y1="546.2" x2="310.8" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="559.3" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="314.6" y1="543.5" x2="314.6" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="545.9" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="318.4" y1="526.1" x2="318.4" y2="555.6" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="527.1" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="322.1" y1="505.6" x2="322.1" y2="530.2" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="507.0" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="325.9" y1="500.3" x2="325.9" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="513.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="329.7" y1="496.9" x2="329.7" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="496.9" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="333.5" y1="485.2" x2="333.5" y2="515.7" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="486.5" width="2.34" height="28.0" fill="var(--up)"/>
<line x1="337.2" y1="481.8" x2="337.2" y2="512.7" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="487.3" width="2.34" height="19.0" fill="var(--down)"/>
<line x1="341.0" y1="487.2" x2="341.0" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="491.9" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="344.8" y1="481.2" x2="344.8" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="483.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="348.5" y1="481.8" x2="348.5" y2="518.0" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="481.8" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="352.3" y1="492.9" x2="352.3" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="498.6" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="356.1" y1="496.9" x2="356.1" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="498.3" width="2.34" height="35.2" fill="var(--down)"/>
<line x1="359.9" y1="527.3" x2="359.9" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="528.8" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="363.6" y1="533.1" x2="363.6" y2="553.9" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="548.2" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="367.4" y1="523.7" x2="367.4" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="526.4" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="371.2" y1="523.8" x2="371.2" y2="552.2" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="530.4" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="375.0" y1="525.1" x2="375.0" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="531.8" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="378.7" y1="530.4" x2="378.7" y2="553.9" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="530.4" width="2.34" height="18.8" fill="var(--down)"/>
<line x1="382.5" y1="511.0" x2="382.5" y2="549.9" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="517.4" width="2.34" height="32.5" fill="var(--up)"/>
<line x1="386.3" y1="514.7" x2="386.3" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="516.0" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="390.0" y1="495.2" x2="390.0" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="505.3" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="393.8" y1="499.9" x2="393.8" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="508.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="397.6" y1="503.6" x2="397.6" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="518.0" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="401.4" y1="473.1" x2="401.4" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="482.2" width="2.34" height="35.9" fill="var(--up)"/>
<line x1="405.1" y1="474.1" x2="405.1" y2="498.6" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="481.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="408.9" y1="461.0" x2="408.9" y2="485.2" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="467.7" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="412.7" y1="468.4" x2="412.7" y2="486.9" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="468.4" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="416.4" y1="477.5" x2="416.4" y2="496.6" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="484.5" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="420.2" y1="492.1" x2="420.2" y2="518.0" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="495.9" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="424.0" y1="492.7" x2="424.0" y2="514.8" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="510.0" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="427.8" y1="494.6" x2="427.8" y2="511.0" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="503.6" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="431.5" y1="486.2" x2="431.5" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="492.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="435.3" y1="460.7" x2="435.3" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="462.7" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="439.1" y1="450.3" x2="439.1" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="460.0" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="442.8" y1="459.4" x2="442.8" y2="490.5" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="459.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="446.6" y1="436.5" x2="446.6" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="441.6" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="450.4" y1="419.8" x2="450.4" y2="448.0" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="424.5" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="454.2" y1="408.7" x2="454.2" y2="429.2" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="413.1" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="457.9" y1="361.5" x2="457.9" y2="424.2" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="370.2" width="2.34" height="46.3" fill="var(--up)"/>
<line x1="461.7" y1="341.0" x2="461.7" y2="372.5" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="341.6" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="465.5" y1="303.4" x2="465.5" y2="353.1" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="337.3" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="469.2" y1="332.6" x2="469.2" y2="399.3" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="332.6" width="2.34" height="20.5" fill="var(--down)"/>
<line x1="473.0" y1="341.7" x2="473.0" y2="381.9" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="357.8" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="476.8" y1="329.3" x2="476.8" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="332.6" width="2.34" height="36.6" fill="var(--up)"/>
<line x1="480.6" y1="306.1" x2="480.6" y2="344.7" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="332.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="484.3" y1="304.1" x2="484.3" y2="340.0" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="328.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="488.1" y1="319.2" x2="488.1" y2="351.4" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="321.9" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="491.9" y1="277.3" x2="491.9" y2="321.6" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="282.3" width="2.34" height="38.6" fill="var(--up)"/>
<line x1="495.7" y1="270.9" x2="495.7" y2="292.0" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="272.6" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="499.4" y1="259.5" x2="499.4" y2="304.1" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="263.2" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="503.2" y1="246.1" x2="503.2" y2="277.6" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="257.2" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="507.0" y1="224.7" x2="507.0" y2="267.2" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="235.0" width="2.34" height="25.5" fill="var(--up)"/>
<line x1="510.7" y1="206.9" x2="510.7" y2="239.7" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="213.4" width="2.34" height="20.4" fill="var(--up)"/>
<line x1="514.5" y1="193.5" x2="514.5" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="205.0" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="518.3" y1="205.2" x2="518.3" y2="237.6" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="205.5" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="522.1" y1="114.7" x2="522.1" y2="231.4" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="116.0" width="2.34" height="99.2" fill="var(--up)"/>
<line x1="525.8" y1="79.8" x2="525.8" y2="143.5" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="95.6" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="529.6" y1="81.8" x2="529.6" y2="181.7" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="97.9" width="2.34" height="77.5" fill="var(--down)"/>
<line x1="533.4" y1="77.8" x2="533.4" y2="176.7" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="79.1" width="2.34" height="94.2" fill="var(--up)"/>
<line x1="537.1" y1="79.8" x2="537.1" y2="146.1" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="79.8" width="2.34" height="56.6" fill="var(--down)"/>
<line x1="540.9" y1="114.7" x2="540.9" y2="159.9" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="114.7" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="544.7" y1="141.3" x2="544.7" y2="241.8" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="141.5" width="2.34" height="99.8" fill="var(--down)"/>
<line x1="548.5" y1="199.3" x2="548.5" y2="257.5" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="222.6" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="552.2" y1="198.5" x2="552.2" y2="267.2" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="228.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="556.0" y1="223.6" x2="556.0" y2="287.0" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="228.7" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="559.8" y1="195.1" x2="559.8" y2="248.5" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="215.3" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="563.5" y1="195.0" x2="563.5" y2="228.7" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="207.7" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="567.3" y1="186.4" x2="567.3" y2="228.7" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="205.2" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="571.1" y1="183.7" x2="571.1" y2="224.7" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="190.1" width="2.34" height="30.5" fill="var(--up)"/>
<line x1="574.9" y1="179.4" x2="574.9" y2="254.4" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="188.8" width="2.34" height="37.2" fill="var(--down)"/>
<line x1="578.6" y1="193.5" x2="578.6" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="209.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="582.4" y1="147.4" x2="582.4" y2="213.6" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="154.6" width="2.34" height="40.6" fill="var(--up)"/>
<line x1="586.2" y1="136.5" x2="586.2" y2="171.3" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="148.7" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="589.9" y1="137.1" x2="589.9" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="137.1" width="2.34" height="27.8" fill="var(--down)"/>
<line x1="593.7" y1="139.8" x2="593.7" y2="213.9" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="160.9" width="2.34" height="33.2" fill="var(--down)"/>
<line x1="597.5" y1="176.0" x2="597.5" y2="232.0" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="193.5" width="2.34" height="35.2" fill="var(--down)"/>
<line x1="601.3" y1="215.3" x2="601.3" y2="296.4" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="232.0" width="2.34" height="63.0" fill="var(--down)"/>
<line x1="605.0" y1="258.5" x2="605.0" y2="307.8" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="282.3" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="608.8" y1="228.7" x2="608.8" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="252.5" width="2.34" height="22.8" fill="var(--up)"/>
<line x1="612.6" y1="248.8" x2="612.6" y2="300.9" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="248.8" width="2.34" height="47.9" fill="var(--down)"/>
<line x1="616.3" y1="252.5" x2="616.3" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="258.9" width="2.34" height="38.6" fill="var(--up)"/>
<line x1="620.1" y1="227.0" x2="620.1" y2="268.9" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="231.4" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="623.9" y1="234.0" x2="623.9" y2="314.8" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="240.4" width="2.34" height="66.6" fill="var(--down)"/>
<line x1="627.7" y1="295.7" x2="627.7" y2="353.4" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="303.8" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="631.4" y1="262.2" x2="631.4" y2="353.4" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="311.2" width="2.34" height="28.8" fill="var(--down)"/>
<line x1="635.2" y1="300.8" x2="635.2" y2="372.9" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="325.9" width="2.34" height="34.5" fill="var(--up)"/>
<line x1="639.0" y1="309.5" x2="639.0" y2="348.7" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="333.3" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="642.8" y1="283.3" x2="642.8" y2="361.5" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="291.7" width="2.34" height="57.3" fill="var(--up)"/>
<line x1="646.5" y1="274.6" x2="646.5" y2="321.6" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="282.3" width="2.34" height="23.8" fill="var(--down)"/>
<line x1="650.3" y1="307.8" x2="650.3" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="325.9" width="2.34" height="28.5" fill="var(--down)"/>
<line x1="654.1" y1="299.1" x2="654.1" y2="354.1" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="331.9" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="657.8" y1="284.0" x2="657.8" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="288.3" width="2.34" height="43.8" fill="var(--up)"/>
<line x1="661.6" y1="240.4" x2="661.6" y2="288.0" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="258.5" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="665.4" y1="237.7" x2="665.4" y2="273.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="238.4" width="2.34" height="29.1" fill="var(--up)"/>
<line x1="669.2" y1="233.7" x2="669.2" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="238.7" width="2.34" height="22.8" fill="var(--down)"/>
<line x1="672.9" y1="231.7" x2="672.9" y2="271.6" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="246.4" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="676.7" y1="234.4" x2="676.7" y2="285.0" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="236.1" width="2.34" height="44.9" fill="var(--down)"/>
<line x1="680.5" y1="256.8" x2="680.5" y2="321.8" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="256.8" width="2.34" height="60.7" fill="var(--down)"/>
<line x1="684.2" y1="302.4" x2="684.2" y2="343.0" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="316.0" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="688.0" y1="261.2" x2="688.0" y2="356.7" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="290.7" width="2.34" height="51.3" fill="var(--up)"/>
<line x1="691.8" y1="256.8" x2="691.8" y2="304.1" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="256.8" width="2.34" height="35.5" fill="var(--down)"/>
<line x1="695.6" y1="292.4" x2="695.6" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="304.1" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="699.3" y1="291.4" x2="699.3" y2="331.3" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="299.1" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="703.1" y1="294.1" x2="703.1" y2="336.0" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="297.7" width="2.34" height="29.8" fill="var(--down)"/>
<line x1="706.9" y1="314.8" x2="706.9" y2="386.3" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="332.3" width="2.34" height="37.2" fill="var(--down)"/>
<line x1="710.6" y1="356.1" x2="710.6" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="369.5" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="714.4" y1="311.8" x2="714.4" y2="377.9" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="320.5" width="2.34" height="47.3" fill="var(--up)"/>
<line x1="718.2" y1="309.1" x2="718.2" y2="375.5" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="320.9" width="2.34" height="35.7" fill="var(--down)"/>
<line x1="722.0" y1="331.9" x2="722.0" y2="374.9" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="353.4" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="725.7" y1="314.5" x2="725.7" y2="367.8" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="349.7" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="729.5" y1="362.8" x2="729.5" y2="412.7" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="371.2" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="733.3" y1="359.8" x2="733.3" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="387.6" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="737.0" y1="386.3" x2="737.0" y2="418.8" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="391.0" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="740.8" y1="408.9" x2="740.8" y2="431.5" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="412.8" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="744.6" y1="409.7" x2="744.6" y2="450.0" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="427.5" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="748.4" y1="419.1" x2="748.4" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="433.0" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="752.1" y1="438.2" x2="752.1" y2="468.1" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="449.1" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="755.9" y1="404.7" x2="755.9" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="422.5" width="2.34" height="35.9" fill="var(--up)"/>
<line x1="759.7" y1="409.7" x2="759.7" y2="451.3" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="429.9" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="763.5" y1="430.2" x2="763.5" y2="481.8" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="460.0" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="767.2" y1="446.6" x2="767.2" y2="498.6" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="454.0" width="2.34" height="36.9" fill="var(--up)"/>
<line x1="771.0" y1="436.6" x2="771.0" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="436.6" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="774.8" y1="421.5" x2="774.8" y2="470.1" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="423.5" width="2.34" height="36.7" fill="var(--up)"/>
<line x1="778.5" y1="397.7" x2="778.5" y2="430.2" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="399.7" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="782.3" y1="372.9" x2="782.3" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="393.6" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="786.1" y1="364.5" x2="786.1" y2="393.7" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="374.5" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="789.9" y1="346.4" x2="789.9" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="353.7" width="2.34" height="35.9" fill="var(--up)"/>
<line x1="793.6" y1="343.7" x2="793.6" y2="377.9" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="346.0" width="2.34" height="30.8" fill="var(--down)"/>
<line x1="797.4" y1="356.1" x2="797.4" y2="389.3" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="369.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="801.2" y1="343.3" x2="801.2" y2="375.9" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="351.4" width="2.34" height="20.8" fill="var(--up)"/>
<line x1="804.9" y1="304.5" x2="804.9" y2="352.1" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="317.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="808.7" y1="284.8" x2="808.7" y2="319.2" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="293.5" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="812.5" y1="287.0" x2="812.5" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="297.7" width="2.34" height="23.1" fill="var(--down)"/>
<line x1="816.3" y1="320.9" x2="816.3" y2="373.5" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="322.6" width="2.34" height="38.6" fill="var(--down)"/>
<line x1="820.0" y1="345.7" x2="820.0" y2="378.9" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="361.1" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="823.8" y1="336.0" x2="823.8" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="359.8" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="827.6" y1="354.4" x2="827.6" y2="388.9" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="366.1" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="831.3" y1="339.3" x2="831.3" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="363.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="835.1" y1="352.7" x2="835.1" y2="379.9" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="361.1" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="838.9" y1="344.4" x2="838.9" y2="382.6" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="344.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="842.7" y1="299.9" x2="842.7" y2="344.7" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="306.8" width="2.34" height="37.6" fill="var(--up)"/>
<line x1="846.4" y1="286.7" x2="846.4" y2="315.9" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="299.1" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="850.2" y1="292.0" x2="850.2" y2="339.3" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="294.7" width="2.34" height="38.2" fill="var(--down)"/>
<line x1="854.0" y1="283.0" x2="854.0" y2="334.3" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="284.0" width="2.34" height="48.6" fill="var(--up)"/>
<line x1="857.7" y1="236.9" x2="857.7" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="244.1" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="861.5" y1="232.0" x2="861.5" y2="275.3" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="236.7" width="2.34" height="37.2" fill="var(--down)"/>
<line x1="865.3" y1="256.2" x2="865.3" y2="326.2" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="277.3" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="869.1" y1="245.4" x2="869.1" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="294.1" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="872.8" y1="300.1" x2="872.8" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="303.1" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="876.6" y1="248.8" x2="876.6" y2="303.4" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="255.2" width="2.34" height="36.5" fill="var(--up)"/>
<line x1="880.4" y1="255.5" x2="880.4" y2="342.3" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="257.2" width="2.34" height="44.6" fill="var(--down)"/>
<line x1="884.2" y1="290.7" x2="884.2" y2="340.3" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="299.1" width="2.34" height="23.8" fill="var(--down)"/>
<line x1="887.9" y1="290.7" x2="887.9" y2="368.8" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="324.9" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="891.7" y1="314.8" x2="891.7" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="316.5" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="895.5" y1="299.6" x2="895.5" y2="330.9" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="300.4" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="899.2" y1="286.0" x2="899.2" y2="323.9" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="300.4" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="903.0" y1="265.6" x2="903.0" y2="320.9" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="285.3" width="2.34" height="28.5" fill="var(--up)"/>
<line x1="906.8" y1="257.2" x2="906.8" y2="286.7" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="261.2" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="910.6" y1="248.8" x2="910.6" y2="272.3" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="253.5" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="914.3" y1="244.8" x2="914.3" y2="266.0" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="249.1" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="918.1" y1="178.4" x2="918.1" y2="247.1" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="196.2" width="2.34" height="39.9" fill="var(--up)"/>
<line x1="921.9" y1="148.5" x2="921.9" y2="199.5" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="155.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="925.6" y1="88.9" x2="925.6" y2="204.8" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="121.4" width="2.34" height="43.3" fill="var(--down)"/>
<line x1="929.4" y1="152.2" x2="929.4" y2="251.1" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="185.1" width="2.34" height="43.3" fill="var(--down)"/>
<line x1="933.2" y1="201.2" x2="933.2" y2="239.4" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="210.2" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="937.0" y1="187.1" x2="937.0" y2="245.8" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="200.5" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="940.7" y1="195.1" x2="940.7" y2="244.4" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="199.5" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="944.5" y1="215.3" x2="944.5" y2="265.6" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="242.1" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="948.3" y1="223.6" x2="948.3" y2="266.9" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="256.2" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="952.0" y1="220.6" x2="952.0" y2="303.1" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="250.8" width="2.34" height="44.3" fill="var(--down)"/>
<line x1="955.8" y1="256.8" x2="955.8" y2="312.2" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="274.7" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="959.6" y1="232.0" x2="959.6" y2="280.0" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="238.5" width="2.34" height="35.8" fill="var(--up)"/>
<line x1="963.4" y1="227.0" x2="963.4" y2="264.2" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="237.4" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="967.1" y1="215.9" x2="967.1" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="218.6" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="970.9" y1="214.7" x2="970.9" y2="235.4" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="215.3" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="974.7" y1="214.9" x2="974.7" y2="244.4" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="230.7" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="978.4" y1="221.0" x2="978.4" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="225.7" width="2.34" height="30.8" fill="var(--down)"/>
<line x1="982.2" y1="226.3" x2="982.2" y2="271.6" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="242.1" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="986.0" y1="252.5" x2="986.0" y2="271.6" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="259.9" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="989.8" y1="246.4" x2="989.8" y2="268.2" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="256.2" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="993.5" y1="241.3" x2="993.5" y2="288.7" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="257.2" width="2.34" height="27.5" fill="var(--down)"/>
<line x1="997.3" y1="261.9" x2="997.3" y2="304.1" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="284.7" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="1001.1" y1="266.2" x2="1001.1" y2="300.8" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="276.6" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="1004.9" y1="285.0" x2="1004.9" y2="308.5" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="285.3" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="1008.6" y1="272.6" x2="1008.6" y2="309.1" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="277.0" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="1012.4" y1="272.3" x2="1012.4" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="276.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="1016.2" y1="274.6" x2="1016.2" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="274.6" width="2.34" height="29.8" fill="var(--down)"/>
<line x1="1019.9" y1="282.3" x2="1019.9" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="288.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1023.7" y1="274.6" x2="1023.7" y2="308.1" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="283.7" width="2.34" height="21.8" fill="var(--down)"/>
<line x1="1027.5" y1="254.5" x2="1027.5" y2="302.4" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="269.9" width="2.34" height="30.5" fill="var(--up)"/>
<line x1="1031.3" y1="255.8" x2="1031.3" y2="280.6" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="258.9" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="1035.0" y1="235.8" x2="1035.0" y2="278.6" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="241.8" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="1038.8" y1="209.9" x2="1038.8" y2="249.8" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="237.2" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="1042.6" y1="227.0" x2="1042.6" y2="264.9" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="232.0" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="1046.3" y1="220.6" x2="1046.3" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="250.5" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="1050.1" y1="251.5" x2="1050.1" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="252.1" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="60" y1="226.3" x2="1052" y2="226.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="229.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$20.67 R1</text>
<text x="1058" y="241.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="83.3" x2="1052" y2="83.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="86.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$24.94 R2</text>
<text x="1058" y="98.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="311.2" x2="1052" y2="311.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="305.2" font-size="11.5" fill="var(--support)" font-weight="600">$18.14 S1</text>
<text x="1058" y="317.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="370.8" x2="1052" y2="370.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="364.8" font-size="11.5" fill="var(--support)" font-weight="600">$16.36 S2</text>
<text x="1058" y="376.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="387.6" x2="1052" y2="387.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="381.6" font-size="11.5" fill="var(--support)" font-weight="600">$15.86 S3</text>
<text x="1058" y="393.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="259.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="251.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $19.67 (2026-09-10)</text>
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

- **상승**: 우라늄 현물 수급 타이트화, 원자력발전 확대 기대(전력 수요 증가, 탈탄소화 정책, 데이터센터 전력 수요 증가 등이 원전 재조명의 배경으로 거론된다) 신호로 흔히 해석한다.
- **하락**: 우라늄 공급 확대, 원자력 정책 후퇴, 신탁 지분 자체의 수급 약화(디스카운트 확대) 신호로 흔히 해석한다.
- **왜 NAV와 괴리가 생기나**: 이 신탁은 신규 자금이 들어오면 그 돈으로 실물 우라늄을 추가 매입해 유닛을 늘리는 구조다. 그런데 신탁 지분 자체도 주식처럼 시장에서 매매되기 때문에, 지분 수요가 우라늄 실물 수요보다 더 빨리 늘거나 줄면 지분 가격이 NAV보다 비싸지거나(프리미엄) 싸지는(디스카운트) 괴리가 생긴다 — 신탁 지분 가격의 변동폭이 실제 우라늄 가격 변동폭보다 더 클 수 있다는 뜻이다.
- **공급이 소수 국가에 집중돼 있다**: 전 세계 우라늄 채굴은 카자흐스탄 비중이 압도적으로 크고, 농축은 러시아 의존도가 높은 편이다. 이런 공급 집중 때문에 지정학적 리스크(수출 제한, 제재 등)가 다른 원자재보다 가격에 더 직접적으로 반영되는 경향이 있다.
- 이 문서는 지지선·저항선을 다루지만, 우라늄은 원유·천연가스와 달리 정책·인허가(원전 건설·재가동 승인, 안전 규제)의 영향을 크게 받는 시장이라 순수 수급 논리만으로 해석하기 어려운 구간이 있다.

---

*작성일: 2026-09-11*
