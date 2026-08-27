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
  body:not([data-md-color-scheme="default"]) .sruuf-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $20.21 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="561.8" x2="1052" y2="561.8" class="grid"/>
<text x="52" y="565.8" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="481.5" x2="1052" y2="481.5" class="grid"/>
<text x="52" y="485.5" font-size="11" text-anchor="end" fill="var(--muted)">12.50</text>
<line x1="60" y1="401.2" x2="1052" y2="401.2" class="grid"/>
<text x="52" y="405.2" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="320.9" x2="1052" y2="320.9" class="grid"/>
<text x="52" y="324.9" font-size="11" text-anchor="end" fill="var(--muted)">17.50</text>
<line x1="60" y1="240.6" x2="1052" y2="240.6" class="grid"/>
<text x="52" y="244.6" font-size="11" text-anchor="end" fill="var(--muted)">20.00</text>
<line x1="60" y1="160.4" x2="1052" y2="160.4" class="grid"/>
<text x="52" y="164.4" font-size="11" text-anchor="end" fill="var(--muted)">22.50</text>
<line x1="60" y1="80.1" x2="1052" y2="80.1" class="grid"/>
<text x="52" y="84.1" font-size="11" text-anchor="end" fill="var(--muted)">25.00</text>
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
<line x1="61.9" y1="593.3" x2="61.9" y2="607.4" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="597.2" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="65.7" y1="520.0" x2="65.7" y2="597.1" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="529.0" width="2.35" height="63.1" fill="var(--up)"/>
<line x1="69.5" y1="438.1" x2="69.5" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="473.5" width="2.35" height="40.1" fill="var(--up)"/>
<line x1="73.3" y1="398.0" x2="73.3" y2="488.3" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="398.0" width="2.35" height="67.4" fill="var(--down)"/>
<line x1="77.0" y1="436.9" x2="77.0" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="481.5" width="2.35" height="32.4" fill="var(--down)"/>
<line x1="80.8" y1="494.7" x2="80.8" y2="561.8" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="515.1" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="84.6" y1="506.9" x2="84.6" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="510.6" width="2.35" height="40.0" fill="var(--down)"/>
<line x1="88.4" y1="487.9" x2="88.4" y2="581.0" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="502.4" width="2.35" height="47.2" fill="var(--up)"/>
<line x1="92.2" y1="450.0" x2="92.2" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="479.2" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="96.0" y1="476.7" x2="96.0" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="483.0" width="2.35" height="42.1" fill="var(--down)"/>
<line x1="99.8" y1="477.6" x2="99.8" y2="537.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="511.7" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="103.5" y1="479.9" x2="103.5" y2="513.6" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="486.0" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="107.3" y1="479.6" x2="107.3" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="483.1" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="111.1" y1="491.8" x2="111.1" y2="526.1" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="498.8" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="114.9" y1="501.4" x2="114.9" y2="540.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="501.4" width="2.35" height="33.1" fill="var(--down)"/>
<line x1="118.7" y1="500.8" x2="118.7" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="534.5" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="122.5" y1="524.5" x2="122.5" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="536.1" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="126.3" y1="526.5" x2="126.3" y2="560.3" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="528.9" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="130.0" y1="517.8" x2="130.0" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="529.0" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="133.8" y1="497.9" x2="133.8" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="498.2" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="137.6" y1="494.3" x2="137.6" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="494.3" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="141.4" y1="494.7" x2="141.4" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="504.0" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="145.2" y1="514.1" x2="145.2" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="522.0" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="149.0" y1="515.2" x2="149.0" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="522.6" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="152.8" y1="519.1" x2="152.8" y2="536.7" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="529.3" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="156.5" y1="516.8" x2="156.5" y2="537.7" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="530.3" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="160.3" y1="479.1" x2="160.3" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="483.4" width="2.35" height="52.0" fill="var(--up)"/>
<line x1="164.1" y1="461.6" x2="164.1" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="471.8" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="167.9" y1="400.9" x2="167.9" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="427.9" width="2.35" height="40.5" fill="var(--up)"/>
<line x1="171.7" y1="404.4" x2="171.7" y2="484.4" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="431.7" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="175.5" y1="398.0" x2="175.5" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="404.1" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="179.3" y1="393.8" x2="179.3" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="395.8" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="183.1" y1="348.2" x2="183.1" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="373.3" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="186.8" y1="368.5" x2="186.8" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="372.3" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="190.6" y1="353.0" x2="190.6" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="378.4" width="2.35" height="79.6" fill="var(--down)"/>
<line x1="194.4" y1="448.7" x2="194.4" y2="489.5" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="459.3" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="198.2" y1="441.4" x2="198.2" y2="487.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="469.6" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="202.0" y1="478.3" x2="202.0" y2="545.4" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="478.3" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="205.8" y1="475.4" x2="205.8" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="510.1" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="209.6" y1="449.4" x2="209.6" y2="516.8" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="502.4" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="213.3" y1="457.4" x2="213.3" y2="509.4" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="482.1" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="217.1" y1="453.2" x2="217.1" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="470.9" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="220.9" y1="495.9" x2="220.9" y2="560.8" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="497.5" width="2.35" height="53.3" fill="var(--down)"/>
<line x1="224.7" y1="529.7" x2="224.7" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="538.7" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="228.5" y1="516.2" x2="228.5" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="516.2" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="232.3" y1="522.3" x2="232.3" y2="565.3" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="531.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="236.1" y1="536.9" x2="236.1" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="537.8" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="239.8" y1="522.6" x2="239.8" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="545.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="243.6" y1="499.8" x2="243.6" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="507.5" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="247.4" y1="497.5" x2="247.4" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="506.5" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="251.2" y1="498.5" x2="251.2" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="520.3" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="255.0" y1="521.3" x2="255.0" y2="557.9" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="545.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="258.8" y1="490.8" x2="258.8" y2="556.5" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="504.9" width="2.35" height="48.5" fill="var(--up)"/>
<line x1="262.6" y1="471.2" x2="262.6" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="490.5" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="266.4" y1="461.9" x2="266.4" y2="489.5" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="465.4" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="270.1" y1="460.6" x2="270.1" y2="509.8" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="462.2" width="2.35" height="37.3" fill="var(--down)"/>
<line x1="273.9" y1="497.5" x2="273.9" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="501.4" width="2.35" height="37.3" fill="var(--down)"/>
<line x1="277.7" y1="501.4" x2="277.7" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="505.6" width="2.35" height="40.1" fill="var(--up)"/>
<line x1="281.5" y1="483.1" x2="281.5" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="504.6" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="285.3" y1="481.0" x2="285.3" y2="526.5" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="487.0" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="289.1" y1="461.3" x2="289.1" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="464.2" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="292.9" y1="457.4" x2="292.9" y2="484.7" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="460.6" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="296.6" y1="454.2" x2="296.6" y2="494.7" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="470.3" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="300.4" y1="456.8" x2="300.4" y2="488.9" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="471.9" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="304.2" y1="465.4" x2="304.2" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="468.6" width="2.35" height="48.8" fill="var(--down)"/>
<line x1="308.0" y1="508.8" x2="308.0" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="517.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="311.8" y1="509.1" x2="311.8" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="510.4" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="315.6" y1="517.9" x2="315.6" y2="546.7" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="517.9" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="319.4" y1="525.5" x2="319.4" y2="544.4" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="538.0" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="323.1" y1="522.9" x2="323.1" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="525.2" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="326.9" y1="506.2" x2="326.9" y2="534.5" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="507.2" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="330.7" y1="486.6" x2="330.7" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="487.9" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="334.5" y1="481.5" x2="334.5" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="494.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="338.3" y1="478.3" x2="338.3" y2="509.1" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="478.3" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="342.1" y1="467.0" x2="342.1" y2="496.3" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="468.3" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="345.9" y1="463.8" x2="345.9" y2="493.4" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="469.1" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="349.6" y1="469.0" x2="349.6" y2="489.5" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="473.5" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="353.4" y1="463.2" x2="353.4" y2="483.1" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="465.1" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="357.2" y1="463.8" x2="357.2" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="463.8" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="361.0" y1="474.4" x2="361.0" y2="494.3" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="479.9" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="364.8" y1="478.3" x2="364.8" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="479.6" width="2.35" height="33.7" fill="var(--down)"/>
<line x1="368.6" y1="507.3" x2="368.6" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="508.8" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="372.4" y1="513.0" x2="372.4" y2="532.9" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="527.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="376.2" y1="504.0" x2="376.2" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="506.5" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="379.9" y1="504.0" x2="379.9" y2="531.3" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="510.4" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="383.7" y1="505.3" x2="383.7" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="511.7" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="387.5" y1="510.4" x2="387.5" y2="532.9" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="510.4" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="391.3" y1="491.8" x2="391.3" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="497.9" width="2.35" height="31.1" fill="var(--up)"/>
<line x1="395.1" y1="495.3" x2="395.1" y2="513.0" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="496.6" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="398.9" y1="476.7" x2="398.9" y2="499.8" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="486.3" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="402.7" y1="481.2" x2="402.7" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="489.4" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="406.4" y1="484.7" x2="406.4" y2="507.7" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="498.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="410.2" y1="455.5" x2="410.2" y2="504.9" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="464.2" width="2.35" height="34.4" fill="var(--up)"/>
<line x1="414.0" y1="456.4" x2="414.0" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="463.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="417.8" y1="443.9" x2="417.8" y2="467.0" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="450.3" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="421.6" y1="451.0" x2="421.6" y2="468.6" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="451.0" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="425.4" y1="459.7" x2="425.4" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="466.4" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="429.2" y1="473.6" x2="429.2" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="477.3" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="432.9" y1="474.3" x2="432.9" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="490.8" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="436.7" y1="476.0" x2="436.7" y2="491.8" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="484.7" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="440.5" y1="468.0" x2="440.5" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="474.4" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="444.3" y1="443.6" x2="444.3" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="445.5" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="448.1" y1="433.6" x2="448.1" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="443.0" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="451.9" y1="442.3" x2="451.9" y2="472.2" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="442.3" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="455.7" y1="420.4" x2="455.7" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="425.3" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="459.5" y1="404.4" x2="459.5" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="408.9" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="463.2" y1="393.8" x2="463.2" y2="413.4" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="398.0" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="467.0" y1="348.5" x2="467.0" y2="408.6" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="356.9" width="2.35" height="44.3" fill="var(--up)"/>
<line x1="470.8" y1="329.0" x2="470.8" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="329.6" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="474.6" y1="293.0" x2="474.6" y2="340.5" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="325.4" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="478.4" y1="320.9" x2="478.4" y2="384.8" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="320.9" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="482.2" y1="329.6" x2="482.2" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="345.0" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="486.0" y1="317.7" x2="486.0" y2="374.6" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="320.9" width="2.35" height="35.1" fill="var(--up)"/>
<line x1="489.7" y1="295.6" x2="489.7" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="320.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="493.5" y1="293.6" x2="493.5" y2="328.0" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="317.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="497.3" y1="308.1" x2="497.3" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="310.7" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="501.1" y1="267.9" x2="501.1" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="272.8" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="504.9" y1="261.8" x2="504.9" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="263.5" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="508.7" y1="250.9" x2="508.7" y2="293.6" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="254.5" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="512.5" y1="238.1" x2="512.5" y2="268.3" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="248.7" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="516.2" y1="217.5" x2="516.2" y2="258.3" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="227.5" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="520.0" y1="200.5" x2="520.0" y2="232.0" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="206.7" width="2.35" height="19.5" fill="var(--up)"/>
<line x1="523.8" y1="187.7" x2="523.8" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="198.7" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="527.6" y1="198.9" x2="527.6" y2="229.9" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="199.2" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="531.4" y1="112.2" x2="531.4" y2="223.9" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="113.5" width="2.35" height="95.1" fill="var(--up)"/>
<line x1="535.2" y1="78.8" x2="535.2" y2="139.8" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="93.9" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="539.0" y1="80.7" x2="539.0" y2="176.4" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="96.1" width="2.35" height="74.2" fill="var(--down)"/>
<line x1="542.7" y1="76.9" x2="542.7" y2="171.6" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="78.2" width="2.35" height="90.2" fill="var(--up)"/>
<line x1="546.5" y1="78.8" x2="546.5" y2="142.3" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="78.8" width="2.35" height="54.2" fill="var(--down)"/>
<line x1="550.3" y1="112.2" x2="550.3" y2="155.5" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="112.2" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="554.1" y1="137.7" x2="554.1" y2="233.9" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="137.9" width="2.35" height="95.6" fill="var(--down)"/>
<line x1="557.9" y1="193.2" x2="557.9" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="215.6" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="561.7" y1="192.5" x2="561.7" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="221.1" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="565.5" y1="216.6" x2="565.5" y2="277.3" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="221.4" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="569.3" y1="189.3" x2="569.3" y2="240.3" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="208.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="573.0" y1="189.2" x2="573.0" y2="221.4" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="201.3" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="576.8" y1="180.9" x2="576.8" y2="221.4" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="198.9" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="580.6" y1="178.3" x2="580.6" y2="217.5" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="184.5" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="584.4" y1="174.2" x2="584.4" y2="246.0" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="183.2" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="588.2" y1="187.7" x2="588.2" y2="227.8" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="203.4" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="592.0" y1="143.5" x2="592.0" y2="206.9" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="150.4" width="2.35" height="38.9" fill="var(--up)"/>
<line x1="595.8" y1="133.1" x2="595.8" y2="166.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="144.8" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="599.5" y1="133.7" x2="599.5" y2="186.4" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="133.7" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="603.3" y1="136.3" x2="603.3" y2="207.3" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="156.5" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="607.1" y1="171.0" x2="607.1" y2="224.6" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="187.7" width="2.35" height="33.7" fill="var(--down)"/>
<line x1="610.9" y1="208.5" x2="610.9" y2="286.2" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="224.6" width="2.35" height="60.4" fill="var(--down)"/>
<line x1="614.7" y1="250.0" x2="614.7" y2="297.2" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="272.8" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="618.5" y1="221.4" x2="618.5" y2="271.2" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="244.2" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="622.3" y1="240.6" x2="622.3" y2="290.6" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="240.6" width="2.35" height="45.9" fill="var(--down)"/>
<line x1="626.0" y1="244.2" x2="626.0" y2="288.5" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="250.3" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="629.8" y1="219.8" x2="629.8" y2="259.9" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="223.9" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="633.6" y1="226.5" x2="633.6" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="232.6" width="2.35" height="63.7" fill="var(--down)"/>
<line x1="637.4" y1="285.6" x2="637.4" y2="340.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="293.3" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="641.2" y1="253.5" x2="641.2" y2="340.8" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="300.4" width="2.35" height="27.6" fill="var(--down)"/>
<line x1="645.0" y1="290.4" x2="645.0" y2="359.5" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="314.5" width="2.35" height="33.1" fill="var(--up)"/>
<line x1="648.8" y1="298.8" x2="648.8" y2="336.3" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="321.6" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="652.5" y1="273.7" x2="652.5" y2="348.6" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="281.8" width="2.35" height="54.9" fill="var(--up)"/>
<line x1="656.3" y1="265.4" x2="656.3" y2="310.3" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="272.8" width="2.35" height="22.8" fill="var(--down)"/>
<line x1="660.1" y1="297.2" x2="660.1" y2="346.9" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="314.5" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="663.9" y1="288.8" x2="663.9" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="320.3" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="667.7" y1="274.4" x2="667.7" y2="326.7" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="278.5" width="2.35" height="41.9" fill="var(--up)"/>
<line x1="671.5" y1="232.6" x2="671.5" y2="278.2" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="250.0" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="675.3" y1="230.1" x2="675.3" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="230.7" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="679.1" y1="226.2" x2="679.1" y2="261.5" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="231.0" width="2.35" height="21.8" fill="var(--down)"/>
<line x1="682.8" y1="224.3" x2="682.8" y2="262.5" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="238.4" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="686.6" y1="226.8" x2="686.6" y2="275.3" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="228.4" width="2.35" height="43.0" fill="var(--down)"/>
<line x1="690.4" y1="248.4" x2="690.4" y2="310.6" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="248.4" width="2.35" height="58.1" fill="var(--down)"/>
<line x1="694.2" y1="292.0" x2="694.2" y2="330.9" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="305.0" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="698.0" y1="252.5" x2="698.0" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="280.8" width="2.35" height="49.1" fill="var(--up)"/>
<line x1="701.8" y1="248.4" x2="701.8" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="248.4" width="2.35" height="34.0" fill="var(--down)"/>
<line x1="705.6" y1="282.4" x2="705.6" y2="313.5" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="293.6" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="709.3" y1="281.4" x2="709.3" y2="319.6" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="288.8" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="713.1" y1="284.0" x2="713.1" y2="324.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="287.5" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="716.9" y1="303.9" x2="716.9" y2="372.3" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="320.6" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="720.7" y1="343.4" x2="720.7" y2="369.4" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="356.3" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="724.5" y1="301.0" x2="724.5" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="309.4" width="2.35" height="45.3" fill="var(--up)"/>
<line x1="728.3" y1="298.5" x2="728.3" y2="362.0" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="309.7" width="2.35" height="34.2" fill="var(--down)"/>
<line x1="732.1" y1="320.3" x2="732.1" y2="361.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="340.8" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="735.8" y1="303.6" x2="735.8" y2="354.6" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="337.3" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="739.6" y1="349.8" x2="739.6" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="357.9" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="743.4" y1="346.9" x2="743.4" y2="381.9" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="373.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="747.2" y1="372.3" x2="747.2" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="376.8" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="751.0" y1="394.0" x2="751.0" y2="415.7" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="397.7" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="754.8" y1="394.8" x2="754.8" y2="433.3" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="411.8" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="758.6" y1="403.8" x2="758.6" y2="456.0" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="417.1" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="762.4" y1="422.1" x2="762.4" y2="450.7" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="432.5" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="766.1" y1="390.0" x2="766.1" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="407.0" width="2.35" height="34.4" fill="var(--up)"/>
<line x1="769.9" y1="394.8" x2="769.9" y2="434.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="414.1" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="773.7" y1="414.4" x2="773.7" y2="463.8" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="443.0" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="777.5" y1="430.1" x2="777.5" y2="479.9" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="437.2" width="2.35" height="35.3" fill="var(--up)"/>
<line x1="781.3" y1="420.5" x2="781.3" y2="457.1" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="420.5" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="785.1" y1="406.0" x2="785.1" y2="452.6" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="408.0" width="2.35" height="35.2" fill="var(--up)"/>
<line x1="788.9" y1="383.2" x2="788.9" y2="414.4" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="385.2" width="2.35" height="25.7" fill="var(--up)"/>
<line x1="792.6" y1="359.5" x2="792.6" y2="399.6" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="379.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="796.4" y1="351.4" x2="796.4" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="361.1" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="800.2" y1="334.1" x2="800.2" y2="400.9" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="341.2" width="2.35" height="34.4" fill="var(--up)"/>
<line x1="804.0" y1="331.5" x2="804.0" y2="364.3" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="333.8" width="2.35" height="29.5" fill="var(--down)"/>
<line x1="807.8" y1="343.4" x2="807.8" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="356.3" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="811.6" y1="331.2" x2="811.6" y2="362.4" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="338.9" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="815.4" y1="294.0" x2="815.4" y2="339.6" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="306.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="819.1" y1="275.2" x2="819.1" y2="308.1" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="283.4" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="822.9" y1="277.3" x2="822.9" y2="312.9" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="287.5" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="826.7" y1="309.7" x2="826.7" y2="360.1" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="311.3" width="2.35" height="36.9" fill="var(--down)"/>
<line x1="830.5" y1="333.5" x2="830.5" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="348.2" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="834.3" y1="324.1" x2="834.3" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="346.9" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="838.1" y1="341.8" x2="838.1" y2="374.9" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="353.0" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="841.9" y1="327.4" x2="841.9" y2="362.4" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="350.5" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="845.6" y1="340.2" x2="845.6" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="348.2" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="849.4" y1="332.2" x2="849.4" y2="368.8" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="332.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="853.2" y1="289.6" x2="853.2" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="296.2" width="2.35" height="36.0" fill="var(--up)"/>
<line x1="857.0" y1="276.9" x2="857.0" y2="304.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="288.8" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="860.8" y1="282.1" x2="860.8" y2="327.4" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="284.6" width="2.35" height="36.6" fill="var(--down)"/>
<line x1="864.6" y1="273.4" x2="864.6" y2="322.5" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="274.4" width="2.35" height="46.6" fill="var(--up)"/>
<line x1="868.4" y1="229.2" x2="868.4" y2="274.5" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="236.2" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="872.2" y1="224.6" x2="872.2" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="229.1" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="875.9" y1="247.7" x2="875.9" y2="314.8" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="267.9" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="879.7" y1="237.4" x2="879.7" y2="317.7" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="284.0" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="883.5" y1="289.8" x2="883.5" y2="337.0" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="292.7" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="887.3" y1="240.6" x2="887.3" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="246.7" width="2.35" height="35.0" fill="var(--up)"/>
<line x1="891.1" y1="247.1" x2="891.1" y2="330.2" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="248.7" width="2.35" height="42.7" fill="var(--down)"/>
<line x1="894.9" y1="280.8" x2="894.9" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="288.8" width="2.35" height="22.8" fill="var(--down)"/>
<line x1="898.7" y1="280.8" x2="898.7" y2="355.6" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="313.5" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="902.4" y1="303.9" x2="902.4" y2="337.0" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="305.5" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="906.2" y1="289.3" x2="906.2" y2="319.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="290.1" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="910.0" y1="276.3" x2="910.0" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="290.1" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="913.8" y1="256.7" x2="913.8" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="275.7" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="917.6" y1="248.7" x2="917.6" y2="276.9" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="252.5" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="921.4" y1="240.6" x2="921.4" y2="263.1" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="245.1" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="925.2" y1="236.8" x2="925.2" y2="257.2" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="241.0" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="928.9" y1="173.2" x2="928.9" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="190.2" width="2.35" height="38.2" fill="var(--up)"/>
<line x1="932.7" y1="144.6" x2="932.7" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="151.1" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="936.5" y1="87.5" x2="936.5" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="118.6" width="2.35" height="41.4" fill="var(--down)"/>
<line x1="940.3" y1="148.2" x2="940.3" y2="242.9" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="179.6" width="2.35" height="41.4" fill="var(--down)"/>
<line x1="944.1" y1="195.0" x2="944.1" y2="231.7" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="203.7" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="947.9" y1="181.6" x2="947.9" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="194.4" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="951.7" y1="189.3" x2="951.7" y2="236.5" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="193.4" width="2.35" height="37.3" fill="var(--down)"/>
<line x1="955.5" y1="208.5" x2="955.5" y2="256.7" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="234.2" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="959.2" y1="216.6" x2="959.2" y2="258.0" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="247.7" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="963.0" y1="213.7" x2="963.0" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="242.6" width="2.35" height="42.4" fill="var(--down)"/>
<line x1="966.8" y1="248.4" x2="966.8" y2="301.3" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="265.5" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="970.6" y1="224.6" x2="970.6" y2="270.5" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="230.8" width="2.35" height="34.3" fill="var(--up)"/>
<line x1="974.4" y1="219.8" x2="974.4" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="229.7" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="978.2" y1="209.2" x2="978.2" y2="248.4" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="211.7" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="982.0" y1="208.0" x2="982.0" y2="227.8" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="208.5" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="985.7" y1="208.2" x2="985.7" y2="236.4" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="223.3" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="989.5" y1="214.0" x2="989.5" y2="249.0" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="218.5" width="2.35" height="29.5" fill="var(--down)"/>
<line x1="993.3" y1="219.1" x2="993.3" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="234.2" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="997.1" y1="244.2" x2="997.1" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="251.2" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="1000.9" y1="238.4" x2="1000.9" y2="259.3" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="247.7" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="1004.7" y1="233.5" x2="1004.7" y2="278.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="248.7" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="1008.5" y1="253.2" x2="1008.5" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="275.0" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="1012.2" y1="257.3" x2="1012.2" y2="290.4" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="267.3" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="1016.0" y1="275.3" x2="1016.0" y2="297.8" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="275.7" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="1019.8" y1="263.4" x2="1019.8" y2="298.5" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="267.6" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="1023.6" y1="263.1" x2="1023.6" y2="296.2" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="267.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="1027.4" y1="265.4" x2="1027.4" y2="296.2" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="265.4" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="1031.2" y1="272.8" x2="1031.2" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="278.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1035.0" y1="265.4" x2="1035.0" y2="297.5" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="274.0" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="1038.7" y1="246.1" x2="1038.7" y2="292.0" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="260.9" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="1042.5" y1="247.4" x2="1042.5" y2="271.2" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="250.3" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="1046.3" y1="228.2" x2="1046.3" y2="269.2" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="233.9" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="1050.1" y1="228.8" x2="1050.1" y2="250.3" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="233.9" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="60" y1="219.1" x2="1052" y2="219.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="222.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$20.67 R1</text>
<text x="1058" y="234.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="82.2" x2="1052" y2="82.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="85.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$24.94 R2</text>
<text x="1058" y="97.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="300.5" x2="1052" y2="300.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="294.5" font-size="11.5" fill="var(--support)" font-weight="600">$18.14 S1</text>
<text x="1058" y="306.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="357.5" x2="1052" y2="357.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="351.5" font-size="11.5" fill="var(--support)" font-weight="600">$16.36 S2</text>
<text x="1058" y="363.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="373.6" x2="1052" y2="373.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="367.6" font-size="11.5" fill="var(--support)" font-weight="600">$15.86 S3</text>
<text x="1058" y="379.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="233.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="225.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $20.21 (2026-08-21)</text>
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

*작성일: 2026-08-21 (최종 수정일: 2026-08-25)*
