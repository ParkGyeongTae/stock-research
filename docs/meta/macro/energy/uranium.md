# 우라늄 실물 신탁 (SRUUF)

!!! note ""
    최근 5년간 Sprott Physical Uranium Trust(SRUUF) 주간 가격을 지지선·저항선과 함께 정리한 참고 자료다. 우라늄은 별도의 공개 선물시장이 없어(대부분 장기 계약 기반의 비공개 시장에서 거래) 금·구리처럼 원자재 선물 가격을 바로 쓸 수 없다. 대신 이 신탁은 채굴기업 주식이 아니라 **실물 우라늄(U3O8)을 직접 매입해 보관**하는 폐쇄형 신탁이라, 채굴기업 ETF(예: URA)보다 실제 우라늄 가격에 더 가깝게 움직인다.

    ⚠️ **정확한 우라늄 현물가가 아니다** — 이 신탁의 시장가는 보유한 우라늄의 순자산가치(NAV)와 정확히 일치하지 않고, 수급에 따라 NAV 대비 **프리미엄(더 비싸게)** 또는 **디스카운트(더 싸게)** 거래될 수 있다. 정밀한 우라늄 현물가가 필요하면 UxC·TradeTech 같은 원출처를 따로 확인한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="sruuf-chart">
<style>
.sruuf-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .sruuf-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .sruuf-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.sruuf-chart svg { width:100%; height:auto; display:block; }
.sruuf-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.sruuf-chart .title { fill: var(--ink); font-weight:600; }
.sruuf-chart .grid { stroke: var(--grid); stroke-width:1; }
.sruuf-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sprott Physical Uranium Trust(SRUUF) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Sprott Physical Uranium Trust (SRUUF) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 $19.17 (2026-08-20) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">7.50</text>
<line x1="60" y1="547.9" x2="1052" y2="547.9" class="grid"/>
<text x="52" y="551.9" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="469.8" x2="1052" y2="469.8" class="grid"/>
<text x="52" y="473.8" font-size="11" text-anchor="end" fill="var(--muted)">12.50</text>
<line x1="60" y1="391.8" x2="1052" y2="391.8" class="grid"/>
<text x="52" y="395.8" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="313.7" x2="1052" y2="313.7" class="grid"/>
<text x="52" y="317.7" font-size="11" text-anchor="end" fill="var(--muted)">17.50</text>
<line x1="60" y1="235.6" x2="1052" y2="235.6" class="grid"/>
<text x="52" y="239.6" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="157.5" x2="1052" y2="157.5" class="grid"/>
<text x="52" y="161.5" font-size="11" text-anchor="end" fill="var(--muted)">22</text>
<line x1="60" y1="79.4" x2="1052" y2="79.4" class="grid"/>
<text x="52" y="83.4" font-size="11" text-anchor="end" fill="var(--muted)">25</text>
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
<line x1="61.9" y1="576.7" x2="61.9" y2="608.8" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="593.2" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="65.7" y1="578.6" x2="65.7" y2="592.3" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="582.3" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="69.4" y1="507.3" x2="69.4" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="516.1" width="2.34" height="61.4" fill="var(--up)"/>
<line x1="73.2" y1="427.7" x2="73.2" y2="516.7" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="462.0" width="2.34" height="39.0" fill="var(--up)"/>
<line x1="77.0" y1="388.6" x2="77.0" y2="476.5" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="388.6" width="2.34" height="65.6" fill="var(--down)"/>
<line x1="80.7" y1="426.4" x2="80.7" y2="516.4" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="469.8" width="2.34" height="31.5" fill="var(--down)"/>
<line x1="84.5" y1="482.6" x2="84.5" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="502.5" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="88.3" y1="494.6" x2="88.3" y2="547.9" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="498.1" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="92.1" y1="476.1" x2="92.1" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="490.1" width="2.34" height="45.9" fill="var(--up)"/>
<line x1="95.8" y1="439.2" x2="95.8" y2="490.4" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="467.6" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="99.6" y1="465.2" x2="99.6" y2="513.4" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="471.3" width="2.34" height="41.0" fill="var(--down)"/>
<line x1="103.4" y1="466.1" x2="103.4" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="499.2" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="107.1" y1="468.3" x2="107.1" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="474.2" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="110.9" y1="468.0" x2="110.9" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="471.4" width="2.34" height="25.0" fill="var(--down)"/>
<line x1="114.7" y1="479.8" x2="114.7" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="486.7" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="118.5" y1="489.2" x2="118.5" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="489.2" width="2.34" height="32.2" fill="var(--down)"/>
<line x1="122.2" y1="488.6" x2="122.2" y2="532.3" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="521.4" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="126.0" y1="511.7" x2="126.0" y2="554.2" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="522.9" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="129.8" y1="513.6" x2="129.8" y2="546.4" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="515.9" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="133.6" y1="505.1" x2="133.6" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="516.1" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="137.3" y1="485.8" x2="137.3" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="486.1" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="141.1" y1="482.3" x2="141.1" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="482.3" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="144.9" y1="482.6" x2="144.9" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="491.7" width="2.34" height="27.5" fill="var(--down)"/>
<line x1="148.6" y1="501.5" x2="148.6" y2="543.9" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="509.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="152.4" y1="502.6" x2="152.4" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="509.8" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="156.2" y1="506.4" x2="156.2" y2="523.6" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="516.4" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="160.0" y1="504.2" x2="160.0" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="517.3" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="163.7" y1="467.5" x2="163.7" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="471.7" width="2.34" height="50.6" fill="var(--up)"/>
<line x1="167.5" y1="450.5" x2="167.5" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="460.4" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="171.3" y1="391.4" x2="171.3" y2="458.9" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="417.7" width="2.34" height="39.4" fill="var(--up)"/>
<line x1="175.0" y1="394.9" x2="175.0" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="421.4" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="178.8" y1="388.6" x2="178.8" y2="418.3" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="394.6" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="182.6" y1="384.6" x2="182.6" y2="433.3" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="386.4" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="186.4" y1="340.2" x2="186.4" y2="397.1" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="364.6" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="190.1" y1="359.9" x2="190.1" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="363.6" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="193.9" y1="344.9" x2="193.9" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="369.6" width="2.34" height="77.5" fill="var(--down)"/>
<line x1="197.7" y1="438.0" x2="197.7" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="448.3" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="201.4" y1="430.8" x2="201.4" y2="476.1" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="458.3" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="205.2" y1="466.7" x2="205.2" y2="532.0" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="466.7" width="2.34" height="30.9" fill="var(--down)"/>
<line x1="209.0" y1="463.9" x2="209.0" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="497.6" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="212.8" y1="438.6" x2="212.8" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="490.1" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="216.5" y1="446.4" x2="216.5" y2="497.0" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="470.5" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="220.3" y1="442.4" x2="220.3" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="459.5" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="224.1" y1="483.9" x2="224.1" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="485.5" width="2.34" height="51.8" fill="var(--down)"/>
<line x1="227.8" y1="516.7" x2="227.8" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="525.4" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="231.6" y1="503.6" x2="231.6" y2="542.9" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="503.6" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="235.4" y1="509.5" x2="235.4" y2="551.4" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="518.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="239.2" y1="523.7" x2="239.2" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="524.6" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="242.9" y1="509.8" x2="242.9" y2="547.9" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="532.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="246.7" y1="487.6" x2="246.7" y2="538.5" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="495.1" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="250.5" y1="485.5" x2="250.5" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="494.2" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="254.3" y1="486.4" x2="254.3" y2="532.3" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="507.6" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="258.0" y1="508.6" x2="258.0" y2="544.2" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="532.3" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="261.8" y1="478.9" x2="261.8" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="492.6" width="2.34" height="47.2" fill="var(--up)"/>
<line x1="265.6" y1="459.8" x2="265.6" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="478.6" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="269.3" y1="450.8" x2="269.3" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="454.2" width="2.34" height="23.4" fill="var(--up)"/>
<line x1="273.1" y1="449.5" x2="273.1" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="451.1" width="2.34" height="36.2" fill="var(--down)"/>
<line x1="276.9" y1="485.5" x2="276.9" y2="528.9" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="489.2" width="2.34" height="36.2" fill="var(--down)"/>
<line x1="280.7" y1="489.2" x2="280.7" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="493.3" width="2.34" height="39.0" fill="var(--up)"/>
<line x1="284.4" y1="471.4" x2="284.4" y2="501.4" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="492.3" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="288.2" y1="469.4" x2="288.2" y2="513.6" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="475.1" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="292.0" y1="450.2" x2="292.0" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="453.0" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="295.7" y1="446.4" x2="295.7" y2="473.0" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="449.5" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="299.5" y1="443.3" x2="299.5" y2="482.6" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="458.9" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="303.3" y1="445.8" x2="303.3" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="460.5" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="307.1" y1="454.2" x2="307.1" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="457.3" width="2.34" height="47.5" fill="var(--down)"/>
<line x1="310.8" y1="496.4" x2="310.8" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="504.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="314.6" y1="496.7" x2="314.6" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="497.9" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="318.4" y1="505.3" x2="318.4" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="505.3" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="322.1" y1="512.6" x2="322.1" y2="531.1" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="524.8" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="325.9" y1="510.1" x2="325.9" y2="532.3" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="512.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="329.7" y1="493.9" x2="329.7" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="494.8" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="333.5" y1="474.8" x2="333.5" y2="497.7" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="476.1" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="337.2" y1="469.8" x2="337.2" y2="488.6" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="482.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="341.0" y1="466.7" x2="341.0" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="466.7" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="344.8" y1="455.8" x2="344.8" y2="484.2" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="457.0" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="348.5" y1="452.7" x2="348.5" y2="481.4" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="457.7" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="352.3" y1="457.7" x2="352.3" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="462.0" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="356.1" y1="452.0" x2="356.1" y2="471.4" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="453.9" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="359.9" y1="452.7" x2="359.9" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="452.7" width="2.34" height="24.8" fill="var(--down)"/>
<line x1="363.6" y1="463.0" x2="363.6" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="468.3" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="367.4" y1="466.7" x2="367.4" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="468.0" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="371.2" y1="495.0" x2="371.2" y2="527.6" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="496.4" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="375.0" y1="500.4" x2="375.0" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="514.5" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="378.7" y1="491.7" x2="378.7" y2="517.6" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="494.2" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="382.5" y1="491.8" x2="382.5" y2="518.2" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="497.9" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="386.3" y1="492.9" x2="386.3" y2="509.5" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="499.2" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="390.0" y1="497.9" x2="390.0" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="497.9" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="393.8" y1="479.8" x2="393.8" y2="516.1" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="485.8" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="397.6" y1="483.3" x2="397.6" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="484.5" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="401.4" y1="465.2" x2="401.4" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="474.5" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="405.1" y1="469.5" x2="405.1" y2="488.6" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="477.5" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="408.9" y1="473.0" x2="408.9" y2="495.4" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="486.4" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="412.7" y1="444.5" x2="412.7" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="453.0" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="416.4" y1="445.5" x2="416.4" y2="468.3" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="452.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="420.2" y1="433.3" x2="420.2" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="439.5" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="424.0" y1="440.2" x2="424.0" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="440.2" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="427.8" y1="448.6" x2="427.8" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="455.2" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="431.5" y1="462.2" x2="431.5" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="465.8" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="435.3" y1="462.8" x2="435.3" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="478.9" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="439.1" y1="464.5" x2="439.1" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="473.0" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="442.8" y1="456.7" x2="442.8" y2="479.2" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="463.0" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="446.6" y1="433.0" x2="446.6" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="434.9" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="450.4" y1="423.3" x2="450.4" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="432.4" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="454.2" y1="431.7" x2="454.2" y2="460.8" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="431.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="457.9" y1="410.4" x2="457.9" y2="435.5" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="415.2" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="461.7" y1="394.9" x2="461.7" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="399.2" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="465.5" y1="384.6" x2="465.5" y2="403.6" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="388.6" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="469.2" y1="340.5" x2="469.2" y2="398.9" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="348.7" width="2.34" height="43.1" fill="var(--up)"/>
<line x1="473.0" y1="321.5" x2="473.0" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="322.1" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="476.8" y1="286.5" x2="476.8" y2="332.7" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="318.0" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="480.6" y1="313.7" x2="480.6" y2="375.8" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="313.7" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="484.3" y1="322.1" x2="484.3" y2="359.6" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="337.1" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="488.1" y1="310.5" x2="488.1" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="313.6" width="2.34" height="34.1" fill="var(--up)"/>
<line x1="491.9" y1="289.0" x2="491.9" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="313.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="495.7" y1="287.1" x2="495.7" y2="320.5" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="310.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="499.4" y1="301.2" x2="499.4" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="303.7" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="503.2" y1="262.1" x2="503.2" y2="303.4" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="266.8" width="2.34" height="35.9" fill="var(--up)"/>
<line x1="507.0" y1="256.2" x2="507.0" y2="275.9" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="257.8" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="510.7" y1="245.6" x2="510.7" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="249.0" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="514.5" y1="233.1" x2="514.5" y2="262.4" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="243.4" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="518.3" y1="213.1" x2="518.3" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="222.8" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="522.1" y1="196.5" x2="522.1" y2="227.2" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="202.6" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="525.8" y1="184.1" x2="525.8" y2="213.9" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="194.8" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="529.6" y1="195.0" x2="529.6" y2="225.1" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="195.3" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="533.4" y1="110.7" x2="533.4" y2="219.3" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="111.9" width="2.34" height="92.4" fill="var(--up)"/>
<line x1="537.1" y1="78.2" x2="537.1" y2="137.5" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="92.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="540.9" y1="80.0" x2="540.9" y2="173.1" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="95.0" width="2.34" height="72.1" fill="var(--down)"/>
<line x1="544.7" y1="76.3" x2="544.7" y2="168.4" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="77.6" width="2.34" height="87.8" fill="var(--up)"/>
<line x1="548.5" y1="78.2" x2="548.5" y2="140.0" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="78.2" width="2.34" height="52.8" fill="var(--down)"/>
<line x1="552.2" y1="110.7" x2="552.2" y2="152.8" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="110.7" width="2.34" height="26.2" fill="var(--down)"/>
<line x1="556.0" y1="135.5" x2="556.0" y2="229.0" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="135.6" width="2.34" height="93.0" fill="var(--down)"/>
<line x1="559.8" y1="189.5" x2="559.8" y2="243.7" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="211.2" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="563.5" y1="188.7" x2="563.5" y2="252.8" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="216.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="567.3" y1="212.2" x2="567.3" y2="271.2" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="216.8" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="571.1" y1="185.6" x2="571.1" y2="235.3" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="204.4" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="574.9" y1="185.5" x2="574.9" y2="216.8" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="197.3" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="578.6" y1="177.5" x2="578.6" y2="216.8" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="195.0" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="582.4" y1="175.0" x2="582.4" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="180.9" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="586.2" y1="170.9" x2="586.2" y2="240.8" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="179.7" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="589.9" y1="184.1" x2="589.9" y2="223.1" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="199.4" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="593.7" y1="141.1" x2="593.7" y2="202.8" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="147.8" width="2.34" height="37.8" fill="var(--up)"/>
<line x1="597.5" y1="131.0" x2="597.5" y2="163.4" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="142.4" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="601.3" y1="131.6" x2="601.3" y2="182.8" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="131.6" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="605.0" y1="134.1" x2="605.0" y2="203.1" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="153.8" width="2.34" height="30.9" fill="var(--down)"/>
<line x1="608.8" y1="167.8" x2="608.8" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="184.1" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="612.6" y1="204.4" x2="612.6" y2="279.9" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="220.0" width="2.34" height="58.7" fill="var(--down)"/>
<line x1="616.3" y1="244.6" x2="616.3" y2="290.6" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="266.8" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="620.1" y1="216.8" x2="620.1" y2="265.3" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="239.0" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="623.9" y1="235.6" x2="623.9" y2="284.1" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="235.6" width="2.34" height="44.7" fill="var(--down)"/>
<line x1="627.7" y1="239.0" x2="627.7" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="245.0" width="2.34" height="35.9" fill="var(--up)"/>
<line x1="631.4" y1="215.3" x2="631.4" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="219.3" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="635.2" y1="221.8" x2="635.2" y2="297.1" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="227.8" width="2.34" height="62.0" fill="var(--down)"/>
<line x1="639.0" y1="279.3" x2="639.0" y2="333.0" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="286.8" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="642.8" y1="248.1" x2="642.8" y2="333.0" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="293.7" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="646.5" y1="284.0" x2="646.5" y2="351.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="307.4" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="650.3" y1="292.1" x2="650.3" y2="328.7" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="314.3" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="654.1" y1="267.8" x2="654.1" y2="340.6" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="275.6" width="2.34" height="53.4" fill="var(--up)"/>
<line x1="657.8" y1="259.6" x2="657.8" y2="303.4" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="266.8" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="661.6" y1="290.6" x2="661.6" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="307.4" width="2.34" height="26.5" fill="var(--down)"/>
<line x1="665.4" y1="282.4" x2="665.4" y2="333.7" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="313.0" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="669.2" y1="268.4" x2="669.2" y2="319.3" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="272.4" width="2.34" height="40.8" fill="var(--up)"/>
<line x1="672.9" y1="227.8" x2="672.9" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="244.6" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="676.7" y1="225.3" x2="676.7" y2="258.2" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="225.9" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="680.5" y1="221.5" x2="680.5" y2="255.9" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="226.2" width="2.34" height="21.2" fill="var(--down)"/>
<line x1="684.2" y1="219.7" x2="684.2" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="233.4" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="688.0" y1="222.2" x2="688.0" y2="269.3" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="223.7" width="2.34" height="41.9" fill="var(--down)"/>
<line x1="691.8" y1="243.1" x2="691.8" y2="303.6" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="243.1" width="2.34" height="56.5" fill="var(--down)"/>
<line x1="695.6" y1="285.6" x2="695.6" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="298.2" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="699.3" y1="247.1" x2="699.3" y2="336.1" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="274.6" width="2.34" height="47.8" fill="var(--up)"/>
<line x1="703.1" y1="243.1" x2="703.1" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="243.1" width="2.34" height="33.1" fill="var(--down)"/>
<line x1="706.9" y1="276.2" x2="706.9" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="287.1" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="710.6" y1="275.3" x2="710.6" y2="312.4" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="282.4" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="714.4" y1="277.8" x2="714.4" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="281.2" width="2.34" height="27.8" fill="var(--down)"/>
<line x1="718.2" y1="297.1" x2="718.2" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="313.4" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="722.0" y1="335.5" x2="722.0" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="348.0" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="725.7" y1="294.3" x2="725.7" y2="355.8" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="302.4" width="2.34" height="44.0" fill="var(--up)"/>
<line x1="729.5" y1="291.8" x2="729.5" y2="353.6" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="302.7" width="2.34" height="33.3" fill="var(--down)"/>
<line x1="733.3" y1="313.0" x2="733.3" y2="353.0" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="333.0" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="737.0" y1="296.8" x2="737.0" y2="346.5" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="329.6" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="740.8" y1="341.8" x2="740.8" y2="388.3" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="349.6" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="744.6" y1="339.0" x2="744.6" y2="373.0" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="364.9" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="748.4" y1="363.6" x2="748.4" y2="393.9" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="368.0" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="752.1" y1="384.7" x2="752.1" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="388.3" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="755.9" y1="385.5" x2="755.9" y2="423.0" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="402.1" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="759.7" y1="394.3" x2="759.7" y2="445.0" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="407.2" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="763.5" y1="412.1" x2="763.5" y2="439.9" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="422.2" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="767.2" y1="380.8" x2="767.2" y2="433.3" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="397.4" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="771.0" y1="385.5" x2="771.0" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="404.2" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="774.8" y1="404.6" x2="774.8" y2="452.7" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="432.4" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="778.5" y1="419.9" x2="778.5" y2="468.3" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="426.7" width="2.34" height="34.4" fill="var(--up)"/>
<line x1="782.3" y1="410.5" x2="782.3" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="410.5" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="786.1" y1="396.4" x2="786.1" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="398.3" width="2.34" height="34.2" fill="var(--up)"/>
<line x1="789.9" y1="374.3" x2="789.9" y2="404.6" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="376.1" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="793.6" y1="351.2" x2="793.6" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="370.5" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="797.4" y1="343.3" x2="797.4" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="352.7" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="801.2" y1="326.5" x2="801.2" y2="391.4" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="333.3" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="804.9" y1="324.0" x2="804.9" y2="355.8" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="326.2" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="808.7" y1="335.5" x2="808.7" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="348.0" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="812.5" y1="323.7" x2="812.5" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="331.2" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="816.3" y1="287.4" x2="816.3" y2="331.8" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="299.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="820.0" y1="269.2" x2="820.0" y2="301.2" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="277.2" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="823.8" y1="271.2" x2="823.8" y2="305.9" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="281.2" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="827.6" y1="302.7" x2="827.6" y2="351.8" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="304.3" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="831.3" y1="325.9" x2="831.3" y2="356.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="340.2" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="835.1" y1="316.8" x2="835.1" y2="356.1" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="339.0" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="838.9" y1="334.0" x2="838.9" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="344.9" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="842.7" y1="319.9" x2="842.7" y2="354.0" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="342.4" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="846.4" y1="332.4" x2="846.4" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="340.2" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="850.2" y1="324.6" x2="850.2" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="324.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="854.0" y1="283.2" x2="854.0" y2="324.9" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="289.6" width="2.34" height="35.0" fill="var(--up)"/>
<line x1="857.7" y1="270.9" x2="857.7" y2="298.1" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="282.4" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="861.5" y1="275.9" x2="861.5" y2="319.9" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="278.4" width="2.34" height="35.6" fill="var(--down)"/>
<line x1="865.3" y1="267.4" x2="865.3" y2="315.2" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="268.4" width="2.34" height="45.3" fill="var(--up)"/>
<line x1="869.1" y1="224.5" x2="869.1" y2="268.5" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="231.2" width="2.34" height="29.3" fill="var(--up)"/>
<line x1="872.8" y1="220.0" x2="872.8" y2="260.3" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="224.3" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="876.6" y1="242.5" x2="876.6" y2="307.7" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="262.1" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="880.4" y1="232.5" x2="880.4" y2="310.5" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="277.8" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="884.2" y1="283.4" x2="884.2" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="286.2" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="887.9" y1="235.6" x2="887.9" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="241.5" width="2.34" height="34.0" fill="var(--up)"/>
<line x1="891.7" y1="241.8" x2="891.7" y2="322.7" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="243.4" width="2.34" height="41.5" fill="var(--down)"/>
<line x1="895.5" y1="274.6" x2="895.5" y2="320.9" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="282.4" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="899.2" y1="274.6" x2="899.2" y2="347.4" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="306.5" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="903.0" y1="297.1" x2="903.0" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="298.7" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="906.8" y1="282.9" x2="906.8" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="283.7" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="910.6" y1="270.3" x2="910.6" y2="305.6" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="283.7" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="914.3" y1="251.2" x2="914.3" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="269.6" width="2.34" height="26.5" fill="var(--up)"/>
<line x1="918.1" y1="243.4" x2="918.1" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="247.1" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="921.9" y1="235.6" x2="921.9" y2="257.5" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="240.0" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="925.6" y1="231.8" x2="925.6" y2="251.6" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="235.9" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="929.4" y1="170.0" x2="929.4" y2="234.0" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="186.6" width="2.34" height="37.2" fill="var(--up)"/>
<line x1="933.2" y1="142.2" x2="933.2" y2="189.7" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="148.4" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="937.0" y1="86.6" x2="937.0" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="116.9" width="2.34" height="40.3" fill="var(--down)"/>
<line x1="940.7" y1="145.6" x2="940.7" y2="237.8" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="176.2" width="2.34" height="40.3" fill="var(--down)"/>
<line x1="944.5" y1="191.2" x2="944.5" y2="226.8" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="199.7" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="948.3" y1="178.1" x2="948.3" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="190.6" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="952.0" y1="185.6" x2="952.0" y2="231.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="189.7" width="2.34" height="36.2" fill="var(--down)"/>
<line x1="955.8" y1="204.4" x2="955.8" y2="251.2" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="229.3" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="959.6" y1="212.2" x2="959.6" y2="252.5" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="242.5" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="963.4" y1="209.4" x2="963.4" y2="286.2" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="237.5" width="2.34" height="41.2" fill="var(--down)"/>
<line x1="967.1" y1="243.1" x2="967.1" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="259.7" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="970.9" y1="220.0" x2="970.9" y2="264.6" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="226.0" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="974.7" y1="215.3" x2="974.7" y2="250.0" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="225.0" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="978.4" y1="205.0" x2="978.4" y2="243.1" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="207.5" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="982.2" y1="203.8" x2="982.2" y2="223.1" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="204.4" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="986.0" y1="204.0" x2="986.0" y2="231.5" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="218.7" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="989.8" y1="209.7" x2="989.8" y2="243.7" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="214.0" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="993.5" y1="214.7" x2="993.5" y2="256.8" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="229.3" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="997.3" y1="239.0" x2="997.3" y2="256.8" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="245.9" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="1001.1" y1="233.4" x2="1001.1" y2="253.7" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="242.5" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="1004.9" y1="228.6" x2="1004.9" y2="272.8" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="243.4" width="2.34" height="25.6" fill="var(--down)"/>
<line x1="1008.6" y1="247.8" x2="1008.6" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="269.0" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="1012.4" y1="251.8" x2="1012.4" y2="284.0" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="261.5" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="1016.2" y1="269.3" x2="1016.2" y2="291.2" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="269.6" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="1019.9" y1="257.8" x2="1019.9" y2="291.8" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="261.8" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="1023.7" y1="257.5" x2="1023.7" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="261.2" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="1027.5" y1="259.6" x2="1027.5" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="259.6" width="2.34" height="27.8" fill="var(--down)"/>
<line x1="1031.3" y1="266.8" x2="1031.3" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="272.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1035.0" y1="259.6" x2="1035.0" y2="290.9" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="268.1" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="1038.8" y1="240.9" x2="1038.8" y2="285.6" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="255.3" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="1042.6" y1="242.1" x2="1042.6" y2="265.3" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="245.0" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="1046.3" y1="242.1" x2="1046.3" y2="263.4" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="243.7" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="1050.1" y1="247.5" x2="1050.1" y2="263.1" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="247.5" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="60" y1="214.7" x2="1052" y2="214.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="218.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$21 R1</text>
<text x="1058" y="230.2" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="81.5" x2="1052" y2="81.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="85.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$25 R2</text>
<text x="1058" y="97.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="293.8" x2="1052" y2="293.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="287.8" font-size="11.5" fill="var(--support)" font-weight="600">$18.14 S1</text>
<text x="1058" y="299.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="349.3" x2="1052" y2="349.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="343.3" font-size="11.5" fill="var(--support)" font-weight="600">$16.36 S2</text>
<text x="1058" y="355.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="364.9" x2="1052" y2="364.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="358.9" font-size="11.5" fill="var(--support)" font-weight="600">$15.86 S3</text>
<text x="1058" y="370.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="261.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="253.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $19.17 (2026-08-20)</text>
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

- **상승**: 우라늄 현물 수급 타이트화, 원자력발전 확대 기대(전력 수요 증가, 탈탄소화 정책, 최근에는 AI 데이터센터의 전력 수요 증가까지 원전 재조명의 배경으로 자주 거론된다) 신호로 흔히 해석한다.
- **하락**: 우라늄 공급 확대, 원자력 정책 후퇴, 신탁 지분 자체의 수급 약화(디스카운트 확대) 신호로 흔히 해석한다.
- **왜 NAV와 괴리가 생기나**: 이 신탁은 신규 자금이 들어오면 그 돈으로 실물 우라늄을 추가 매입해 유닛을 늘리는 구조다. 그런데 신탁 지분 자체도 주식처럼 시장에서 매매되기 때문에, 지분 수요가 우라늄 실물 수요보다 더 빨리 늘거나 줄면 지분 가격이 NAV보다 비싸지거나(프리미엄) 싸지는(디스카운트) 괴리가 생긴다 — 신탁 지분 가격의 변동폭이 실제 우라늄 가격 변동폭보다 더 클 수 있다는 뜻이다.
- **공급이 소수 국가에 집중돼 있다**: 전 세계 우라늄 채굴은 카자흐스탄 비중이 압도적으로 크고, 농축은 러시아 의존도가 높은 편이다. 이런 공급 집중 때문에 지정학적 리스크(수출 제한, 제재 등)가 다른 원자재보다 가격에 더 직접적으로 반영되는 경향이 있다.
- 이 문서는 지지선·저항선을 다루지만, 우라늄은 원유·천연가스와 달리 정책·인허가(원전 건설·재가동 승인, 안전 규제)의 영향을 크게 받는 시장이라 순수 수급 논리만으로 해석하기 어려운 구간이 있다.

---

## 관련 문서

- [WTI 원유](./oil_wti.md)
- [천연가스](./natural_gas.md)
- [에너지 3종 비교 (지수화)](./comparison.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Sprott Physical Uranium Trust (SRUUF)](https://finance.yahoo.com/quote/SRUUF/)
- [Sprott Physical Uranium Trust — 공식 사이트](https://sprott.com/investment-strategies/physical-commodity-funds/uranium/)

---

*작성일: 2026-08-21 (최종 수정일: 2026-08-21)*
