# 달러인덱스 (DXY)

!!! note ""
    최근 5년간 달러인덱스(주요 6개 통화 대비 달러 가치를 가중평균한 지수, 유로 비중이 가장 큼, `DX-Y.NYB`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 달러 자체가 전반적으로 강한지 약한지를 보여주는 지수로, 해외 매출 비중이 큰 회사의 환율 민감도와 직결된다.

    **원/달러 환율과의 차이**: 원/달러 환율에는 원화만의 고유한 사정(한국은행의 통화정책, 한국의 무역수지 등)까지 함께 반영된다. 반면 이 지표는 **달러 자체의 강약만** 본다. 어떤 회사의 실적 변동이 "달러가 전반적으로 강해져서"인지 "원화만 특이하게 움직여서"인지 구분하는 데 참고할 수 있다.

---

## 1. 차트 — 최근 5년 주봉

<div class="dx-y-nyb-chart">
<style>
.dx-y-nyb-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .dx-y-nyb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .dx-y-nyb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.dx-y-nyb-chart svg { width:100%; height:auto; display:block; }
.dx-y-nyb-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.dx-y-nyb-chart .title { fill: var(--ink); font-weight:600; }
.dx-y-nyb-chart .grid { stroke: var(--grid); stroke-width:1; }
.dx-y-nyb-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="달러인덱스(DX-Y.NYB) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">달러인덱스 (DX-Y.NYB) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 99.68 (2026-08-28) · 단위 지수</text>
<line x1="60" y1="532.9" x2="1052" y2="532.9" class="grid"/>
<text x="52" y="536.9" font-size="11" text-anchor="end" fill="var(--muted)">95.00</text>
<line x1="60" y1="416.6" x2="1052" y2="416.6" class="grid"/>
<text x="52" y="420.6" font-size="11" text-anchor="end" fill="var(--muted)">100.00</text>
<line x1="60" y1="300.3" x2="1052" y2="300.3" class="grid"/>
<text x="52" y="304.3" font-size="11" text-anchor="end" fill="var(--muted)">105.00</text>
<line x1="60" y1="184.0" x2="1052" y2="184.0" class="grid"/>
<text x="52" y="188.0" font-size="11" text-anchor="end" fill="var(--muted)">110.00</text>
<line x1="60" y1="67.6" x2="1052" y2="67.6" class="grid"/>
<text x="52" y="71.6" font-size="11" text-anchor="end" fill="var(--muted)">115.00</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.0" y1="56.0" x2="130.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.0" y1="626.0" x2="130.0" y2="631.0" class="axis"/>
<text x="130.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="326.9" y1="56.0" x2="326.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="326.9" y1="626.0" x2="326.9" y2="631.0" class="axis"/>
<text x="326.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="523.8" y1="56.0" x2="523.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="523.8" y1="626.0" x2="523.8" y2="631.0" class="axis"/>
<text x="523.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="724.5" y1="56.0" x2="724.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="724.5" y1="626.0" x2="724.5" y2="631.0" class="axis"/>
<text x="724.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.4" y1="56.0" x2="921.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.4" y1="626.0" x2="921.4" y2="631.0" class="axis"/>
<text x="921.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="584.4" x2="61.9" y2="603.9" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="586.9" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="65.7" y1="582.7" x2="65.7" y2="600.4" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="589.2" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="69.5" y1="573.7" x2="69.5" y2="595.3" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="574.8" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="73.3" y1="567.4" x2="73.3" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="571.8" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="77.0" y1="544.6" x2="77.0" y2="574.6" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="555.3" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="80.8" y1="545.7" x2="80.8" y2="563.6" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="554.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="84.6" y1="543.2" x2="84.6" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="553.9" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="88.4" y1="552.2" x2="88.4" y2="567.8" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="557.4" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="92.2" y1="549.2" x2="92.2" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="553.4" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="96.0" y1="541.8" x2="96.0" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="548.8" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="99.8" y1="526.7" x2="99.8" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="529.9" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="103.5" y1="504.1" x2="103.5" y2="533.6" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="508.0" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="107.3" y1="487.8" x2="107.3" y2="515.5" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="507.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="111.1" y1="494.8" x2="111.1" y2="520.8" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="506.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="114.9" y1="495.9" x2="114.9" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="506.2" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="118.7" y1="488.5" x2="118.7" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="496.4" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="122.5" y1="493.6" x2="122.5" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="494.1" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="126.3" y1="500.4" x2="126.3" y2="519.7" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="506.2" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="130.0" y1="499.0" x2="130.0" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="515.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="133.8" y1="504.3" x2="133.8" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="515.7" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="137.6" y1="512.9" x2="137.6" y2="532.0" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="518.0" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="141.4" y1="476.2" x2="141.4" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="480.1" width="2.35" height="37.9" fill="var(--up)"/>
<line x1="145.2" y1="479.4" x2="145.2" y2="529.7" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="481.3" width="2.35" height="40.5" fill="var(--down)"/>
<line x1="149.0" y1="507.1" x2="149.0" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="507.8" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="152.8" y1="499.4" x2="152.8" y2="517.1" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="508.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="156.5" y1="469.2" x2="156.5" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="495.2" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="160.3" y1="441.7" x2="160.3" y2="497.1" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="448.0" width="2.35" height="49.1" fill="var(--up)"/>
<line x1="164.1" y1="430.1" x2="164.1" y2="469.9" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="437.1" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="167.9" y1="433.1" x2="167.9" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="436.9" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="171.7" y1="440.6" x2="171.7" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="444.3" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="175.5" y1="431.3" x2="175.5" y2="470.4" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="444.3" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="179.3" y1="412.2" x2="179.3" y2="451.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="421.3" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="183.1" y1="398.9" x2="183.1" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="405.0" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="186.8" y1="385.7" x2="186.8" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="388.2" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="190.6" y1="325.2" x2="190.6" y2="392.4" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="347.7" width="2.35" height="42.8" fill="var(--up)"/>
<line x1="194.4" y1="322.2" x2="194.4" y2="361.9" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="331.5" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="198.2" y1="300.1" x2="198.2" y2="338.2" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="310.5" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="202.0" y1="308.7" x2="202.0" y2="354.7" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="312.6" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="205.8" y1="345.7" x2="205.8" y2="383.3" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="346.1" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="209.6" y1="353.1" x2="209.6" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="366.8" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="213.3" y1="318.2" x2="213.3" y2="373.6" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="320.1" width="2.35" height="46.1" fill="var(--up)"/>
<line x1="217.1" y1="281.9" x2="217.1" y2="337.0" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="307.3" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="220.9" y1="301.4" x2="220.9" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="308.4" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="224.7" y1="285.4" x2="224.7" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="297.0" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="228.5" y1="235.4" x2="228.5" y2="304.5" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="253.5" width="2.35" height="44.0" fill="var(--up)"/>
<line x1="232.3" y1="200.5" x2="232.3" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="229.1" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="236.1" y1="229.6" x2="236.1" y2="274.5" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="231.0" width="2.35" height="29.1" fill="var(--down)"/>
<line x1="239.8" y1="243.8" x2="239.8" y2="287.7" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="264.2" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="243.6" y1="255.4" x2="243.6" y2="299.1" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="262.6" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="247.4" y1="258.4" x2="247.4" y2="308.7" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="263.5" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="251.2" y1="225.4" x2="251.2" y2="287.5" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="226.5" width="2.35" height="58.2" fill="var(--up)"/>
<line x1="255.0" y1="200.9" x2="255.0" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="211.9" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="258.8" y1="184.4" x2="258.8" y2="223.7" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="194.9" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="262.6" y1="165.6" x2="262.6" y2="222.1" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="193.3" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="266.4" y1="177.9" x2="266.4" y2="237.9" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="189.5" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="270.1" y1="108.8" x2="270.1" y2="198.8" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="109.7" width="2.35" height="82.6" fill="var(--up)"/>
<line x1="273.9" y1="72.8" x2="273.9" y2="147.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="113.7" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="277.7" y1="117.0" x2="277.7" y2="182.6" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="118.8" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="281.5" y1="92.8" x2="281.5" y2="133.9" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="107.0" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="285.3" y1="92.3" x2="285.3" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="109.0" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="289.1" y1="125.1" x2="289.1" y2="194.7" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="140.2" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="292.9" y1="110.7" x2="292.9" y2="174.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="163.5" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="296.6" y1="154.4" x2="296.6" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="165.6" width="2.35" height="104.7" fill="var(--down)"/>
<line x1="300.4" y1="247.5" x2="300.4" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="255.4" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="304.2" y1="230.7" x2="304.2" y2="285.6" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="254.5" width="2.35" height="23.5" fill="var(--down)"/>
<line x1="308.0" y1="249.1" x2="308.0" y2="314.7" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="275.6" width="2.35" height="35.1" fill="var(--down)"/>
<line x1="311.8" y1="281.2" x2="311.8" y2="321.0" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="304.7" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="315.6" y1="294.5" x2="315.6" y2="336.3" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="301.9" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="319.4" y1="301.9" x2="319.4" y2="329.4" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="304.0" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="323.1" y1="310.5" x2="323.1" y2="337.7" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="320.8" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="326.9" y1="285.6" x2="326.9" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="326.3" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="330.7" y1="324.9" x2="330.7" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="325.6" width="2.35" height="39.8" fill="var(--down)"/>
<line x1="334.5" y1="349.1" x2="334.5" y2="381.0" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="365.9" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="338.3" y1="360.1" x2="338.3" y2="381.7" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="370.3" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="342.1" y1="346.6" x2="342.1" y2="397.5" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="348.7" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="345.9" y1="324.5" x2="345.9" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="332.2" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="349.6" y1="308.0" x2="349.6" y2="356.4" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="326.8" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="353.4" y1="292.8" x2="353.4" y2="329.1" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="295.4" width="2.35" height="30.9" fill="var(--up)"/>
<line x1="357.2" y1="291.9" x2="357.2" y2="321.5" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="294.2" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="361.0" y1="279.8" x2="361.0" y2="322.6" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="310.1" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="364.8" y1="298.0" x2="364.8" y2="336.6" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="314.5" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="368.6" y1="324.5" x2="368.6" y2="371.9" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="326.8" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="372.4" y1="341.5" x2="372.4" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="344.0" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="376.2" y1="345.4" x2="376.2" y2="383.6" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="356.4" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="379.9" y1="351.2" x2="379.9" y2="398.2" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="367.8" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="383.7" y1="364.7" x2="383.7" y2="381.0" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="374.3" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="387.5" y1="366.1" x2="387.5" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="376.6" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="391.3" y1="360.8" x2="391.3" y2="392.6" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="377.8" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="395.1" y1="353.6" x2="395.1" y2="392.4" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="354.3" width="2.35" height="32.6" fill="var(--up)"/>
<line x1="398.9" y1="332.4" x2="398.9" y2="365.4" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="342.2" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="402.7" y1="313.8" x2="402.7" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="318.7" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="406.4" y1="307.3" x2="406.4" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="316.6" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="410.2" y1="314.2" x2="410.2" y2="339.8" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="322.6" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="414.0" y1="329.1" x2="414.0" y2="369.8" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="334.0" width="2.35" height="29.1" fill="var(--down)"/>
<line x1="417.8" y1="342.9" x2="417.8" y2="371.9" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="349.1" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="421.6" y1="334.3" x2="421.6" y2="362.6" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="348.9" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="425.4" y1="333.6" x2="425.4" y2="364.7" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="348.7" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="429.2" y1="357.1" x2="429.2" y2="426.4" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="363.3" width="2.35" height="55.4" fill="var(--down)"/>
<line x1="432.9" y1="388.9" x2="432.9" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="391.7" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="436.7" y1="369.2" x2="436.7" y2="403.8" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="378.9" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="440.5" y1="350.5" x2="440.5" y2="381.0" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="369.6" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="444.3" y1="348.9" x2="444.3" y2="375.2" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="350.5" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="448.1" y1="331.0" x2="448.1" y2="352.2" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="338.0" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="451.9" y1="313.1" x2="451.9" y2="346.6" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="321.7" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="455.7" y1="315.2" x2="455.7" y2="348.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="318.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="459.5" y1="296.6" x2="459.5" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="298.2" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="463.2" y1="290.0" x2="463.2" y2="313.8" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="292.8" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="467.0" y1="282.1" x2="467.0" y2="308.0" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="286.8" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="470.8" y1="257.5" x2="470.8" y2="288.2" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="273.1" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="474.6" y1="245.6" x2="474.6" y2="278.2" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="273.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="478.4" y1="258.6" x2="478.4" y2="287.7" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="261.9" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="482.2" y1="261.4" x2="482.2" y2="277.5" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="263.5" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="486.0" y1="256.3" x2="486.0" y2="291.9" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="264.0" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="489.7" y1="251.2" x2="489.7" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="263.5" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="493.5" y1="276.8" x2="493.5" y2="303.8" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="280.3" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="497.3" y1="278.0" x2="497.3" y2="328.0" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="281.7" width="2.35" height="46.1" fill="var(--down)"/>
<line x1="501.1" y1="318.7" x2="501.1" y2="342.6" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="327.7" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="504.9" y1="330.1" x2="504.9" y2="359.1" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="337.0" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="508.7" y1="317.5" x2="508.7" y2="345.4" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="323.3" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="512.5" y1="317.5" x2="512.5" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="324.0" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="516.2" y1="355.4" x2="516.2" y2="383.3" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="356.4" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="520.0" y1="375.4" x2="520.0" y2="402.2" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="378.2" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="523.8" y1="344.5" x2="523.8" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="360.5" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="527.6" y1="352.4" x2="527.6" y2="368.2" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="359.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="531.4" y1="330.8" x2="531.4" y2="362.9" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="340.1" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="535.2" y1="327.7" x2="535.2" y2="352.2" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="335.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="539.0" y1="322.6" x2="539.0" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="325.4" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="542.7" y1="309.6" x2="542.7" y2="324.9" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="321.7" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="546.5" y1="300.8" x2="546.5" y2="325.9" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="317.0" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="550.3" y1="314.0" x2="550.3" y2="336.8" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="317.0" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="554.1" y1="316.8" x2="554.1" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="324.5" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="557.9" y1="324.5" x2="557.9" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="326.1" width="2.35" height="26.8" fill="var(--down)"/>
<line x1="561.7" y1="335.4" x2="561.7" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="336.8" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="565.5" y1="311.9" x2="565.5" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="313.5" width="2.35" height="22.8" fill="var(--up)"/>
<line x1="569.3" y1="306.6" x2="569.3" y2="323.3" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="310.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="573.0" y1="298.0" x2="573.0" y2="325.4" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="312.2" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="576.8" y1="274.5" x2="576.8" y2="326.3" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="276.1" width="2.35" height="40.7" fill="var(--up)"/>
<line x1="580.6" y1="264.9" x2="580.6" y2="283.1" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="273.5" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="584.4" y1="267.7" x2="584.4" y2="290.7" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="274.2" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="588.2" y1="265.6" x2="588.2" y2="311.5" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="275.2" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="592.0" y1="283.1" x2="592.0" y2="303.3" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="293.1" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="595.8" y1="289.6" x2="595.8" y2="321.7" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="293.1" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="599.5" y1="297.5" x2="599.5" y2="314.5" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="306.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="603.3" y1="296.1" x2="603.3" y2="315.6" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="308.0" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="607.1" y1="301.4" x2="607.1" y2="323.8" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="302.8" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="610.9" y1="281.4" x2="610.9" y2="317.5" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="287.5" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="614.7" y1="278.9" x2="614.7" y2="297.3" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="281.7" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="618.5" y1="274.0" x2="618.5" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="280.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="622.3" y1="275.9" x2="622.3" y2="304.2" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="280.5" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="626.0" y1="295.4" x2="626.0" y2="322.6" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="303.1" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="629.8" y1="311.7" x2="629.8" y2="331.7" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="314.2" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="633.6" y1="310.5" x2="633.6" y2="321.7" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="314.9" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="637.4" y1="304.9" x2="637.4" y2="343.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="315.9" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="641.2" y1="334.0" x2="641.2" y2="366.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="341.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="645.0" y1="339.6" x2="645.0" y2="363.8" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="343.3" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="648.8" y1="358.9" x2="648.8" y2="402.7" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="360.8" width="2.35" height="39.1" fill="var(--down)"/>
<line x1="652.5" y1="375.2" x2="652.5" y2="404.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="377.1" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="656.3" y1="371.9" x2="656.3" y2="403.1" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="378.0" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="660.1" y1="373.8" x2="660.1" y2="396.1" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="388.9" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="663.9" y1="382.4" x2="663.9" y2="411.5" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="392.4" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="667.7" y1="388.0" x2="667.7" y2="412.9" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="399.4" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="671.5" y1="354.0" x2="671.5" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="358.0" width="2.35" height="48.9" fill="var(--up)"/>
<line x1="675.3" y1="342.6" x2="675.3" y2="363.3" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="349.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="679.1" y1="326.6" x2="679.1" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="335.4" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="682.8" y1="310.3" x2="682.8" y2="337.0" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="317.5" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="686.6" y1="308.7" x2="686.6" y2="331.0" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="316.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="690.4" y1="290.0" x2="690.4" y2="338.2" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="300.3" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="694.2" y1="252.4" x2="694.2" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="261.0" width="2.35" height="40.5" fill="var(--up)"/>
<line x1="698.0" y1="228.9" x2="698.0" y2="274.5" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="242.4" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="701.8" y1="242.1" x2="701.8" y2="285.9" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="247.9" width="2.35" height="35.1" fill="var(--down)"/>
<line x1="705.6" y1="260.0" x2="705.6" y2="290.5" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="277.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="709.3" y1="249.3" x2="709.3" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="253.8" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="713.1" y1="217.9" x2="713.1" y2="260.7" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="239.3" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="716.9" y1="223.5" x2="716.9" y2="237.9" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="230.5" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="720.7" y1="194.9" x2="720.7" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="208.4" width="2.35" height="21.9" fill="var(--up)"/>
<line x1="724.5" y1="184.7" x2="724.5" y2="236.3" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="192.1" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="728.3" y1="179.8" x2="728.3" y2="216.5" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="192.3" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="732.1" y1="196.3" x2="732.1" y2="248.6" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="197.7" width="2.35" height="45.8" fill="var(--down)"/>
<line x1="735.8" y1="217.2" x2="735.8" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="221.9" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="739.6" y1="186.8" x2="739.6" y2="246.8" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="218.9" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="743.4" y1="218.4" x2="743.4" y2="263.8" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="228.2" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="747.2" y1="244.9" x2="747.2" y2="269.1" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="257.9" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="751.0" y1="238.4" x2="751.0" y2="274.0" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="239.6" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="754.8" y1="240.7" x2="754.8" y2="336.1" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="240.7" width="2.35" height="86.5" fill="var(--down)"/>
<line x1="758.6" y1="321.5" x2="758.6" y2="341.7" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="325.6" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="762.4" y1="318.4" x2="762.4" y2="342.2" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="321.5" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="766.1" y1="307.7" x2="766.1" y2="327.3" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="320.1" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="769.9" y1="314.5" x2="769.9" y2="387.1" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="323.3" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="773.7" y1="334.3" x2="773.7" y2="439.6" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="345.2" width="2.35" height="76.5" fill="var(--down)"/>
<line x1="777.5" y1="410.1" x2="777.5" y2="435.9" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="416.1" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="781.3" y1="418.0" x2="781.3" y2="465.0" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="428.9" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="785.1" y1="407.8" x2="785.1" y2="442.2" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="416.6" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="788.9" y1="396.6" x2="788.9" y2="435.9" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="408.7" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="792.6" y1="370.5" x2="792.6" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="391.3" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="796.4" y1="395.4" x2="796.4" y2="438.7" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="395.4" width="2.35" height="41.9" fill="var(--down)"/>
<line x1="800.2" y1="404.0" x2="800.2" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="432.2" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="804.0" y1="430.1" x2="804.0" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="430.3" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="807.8" y1="430.8" x2="807.8" y2="472.4" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="435.2" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="811.6" y1="439.6" x2="811.6" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="446.6" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="815.4" y1="430.1" x2="815.4" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="437.8" width="2.35" height="39.3" fill="var(--down)"/>
<line x1="819.1" y1="476.6" x2="819.1" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="482.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="822.9" y1="464.1" x2="822.9" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="466.6" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="826.7" y1="441.0" x2="826.7" y2="469.9" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="452.0" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="830.5" y1="451.3" x2="830.5" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="454.8" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="834.3" y1="410.6" x2="834.3" y2="475.0" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="447.1" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="838.1" y1="438.2" x2="838.1" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="448.0" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="841.9" y1="432.4" x2="841.9" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="457.6" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="845.6" y1="443.8" x2="845.6" y2="473.4" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="468.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="849.4" y1="446.2" x2="849.4" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="468.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="853.2" y1="448.3" x2="853.2" y2="476.4" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="468.5" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="857.0" y1="461.0" x2="857.0" y2="480.6" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="468.0" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="860.8" y1="467.6" x2="860.8" y2="504.6" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="471.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="864.6" y1="449.0" x2="864.6" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="459.7" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="868.4" y1="459.0" x2="868.4" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="459.2" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="872.2" y1="426.8" x2="872.2" y2="464.1" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="440.3" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="875.9" y1="428.7" x2="875.9" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="441.3" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="879.7" y1="436.6" x2="879.7" y2="454.1" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="441.0" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="883.5" y1="420.3" x2="883.5" y2="449.9" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="421.3" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="887.3" y1="408.2" x2="887.3" y2="430.6" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="422.4" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="891.1" y1="422.7" x2="891.1" y2="440.1" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="425.2" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="894.9" y1="407.3" x2="894.9" y2="434.1" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="412.4" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="898.7" y1="409.6" x2="898.7" y2="431.0" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="412.0" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="902.4" y1="426.6" x2="902.4" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="428.7" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="906.2" y1="432.7" x2="906.2" y2="460.1" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="440.6" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="910.0" y1="445.7" x2="910.0" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="449.2" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="913.8" y1="446.2" x2="913.8" y2="469.0" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="447.6" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="917.6" y1="451.5" x2="917.6" y2="465.0" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="453.4" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="921.4" y1="433.8" x2="921.4" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="436.9" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="925.2" y1="428.5" x2="925.2" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="430.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="928.9" y1="436.6" x2="928.9" y2="476.4" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="436.6" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="932.7" y1="478.7" x2="932.7" y2="520.1" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="485.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="936.5" y1="463.4" x2="936.5" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="471.8" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="940.3" y1="468.7" x2="940.3" y2="498.3" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="470.1" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="944.1" y1="461.3" x2="944.1" y2="489.2" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="467.8" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="947.9" y1="463.1" x2="947.9" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="470.1" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="951.7" y1="424.1" x2="951.7" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="440.1" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="955.5" y1="404.0" x2="955.5" y2="451.7" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="408.2" width="2.35" height="34.9" fill="var(--up)"/>
<line x1="959.2" y1="405.4" x2="959.2" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="406.6" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="963.0" y1="411.7" x2="963.0" y2="442.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="413.1" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="966.8" y1="401.7" x2="966.8" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="411.5" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="970.6" y1="409.9" x2="970.6" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="412.4" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="974.4" y1="435.7" x2="974.4" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="438.7" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="978.2" y1="441.3" x2="978.2" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="451.3" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="982.0" y1="432.0" x2="982.0" y2="469.7" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="432.2" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="985.7" y1="449.6" x2="985.7" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="462.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="989.5" y1="432.4" x2="989.5" y2="466.6" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="433.6" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="993.3" y1="427.8" x2="993.3" y2="441.0" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="432.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="997.1" y1="427.3" x2="997.1" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="437.1" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="1000.9" y1="414.1" x2="1000.9" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="415.0" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="1004.7" y1="409.4" x2="1004.7" y2="426.2" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="413.1" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="1008.5" y1="395.2" x2="1008.5" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="396.8" width="2.35" height="30.5" fill="var(--up)"/>
<line x1="1012.2" y1="374.7" x2="1012.2" y2="398.9" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="385.0" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="1016.0" y1="379.4" x2="1016.0" y2="403.6" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="384.7" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="1019.8" y1="386.8" x2="1019.8" y2="402.7" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="394.0" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="1023.6" y1="385.7" x2="1023.6" y2="408.5" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="392.4" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="1027.4" y1="380.8" x2="1027.4" y2="401.5" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="382.4" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="1031.2" y1="378.5" x2="1031.2" y2="423.8" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="385.9" width="2.35" height="35.4" fill="var(--down)"/>
<line x1="1035.0" y1="415.2" x2="1035.0" y2="430.6" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="423.8" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="1038.7" y1="414.8" x2="1038.7" y2="428.7" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="424.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="1042.5" y1="423.8" x2="1042.5" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="424.5" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="1046.3" y1="433.8" x2="1046.3" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="436.2" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="1050.1" y1="423.0" x2="1050.1" y2="437.6" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="424.1" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="60" y1="396.0" x2="1052" y2="396.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="399.5" font-size="11.5" fill="var(--resistance)" font-weight="600">100.89 R1</text>
<text x="1058" y="411.5" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="281.8" x2="1052" y2="281.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="285.3" font-size="11.5" fill="var(--resistance)" font-weight="600">105.80 R2</text>
<text x="1058" y="297.3" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="190.1" x2="1052" y2="190.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="193.6" font-size="11.5" fill="var(--resistance)" font-weight="600">109.74 R3</text>
<text x="1058" y="205.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="496.5" x2="1052" y2="496.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="490.5" font-size="11.5" fill="var(--support)" font-weight="600">96.57 S1</text>
<text x="1058" y="502.5" font-size="9.5" fill="var(--muted)">터치 7회</text>
<circle cx="1052.0" cy="424.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="416.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 99.68 (2026-08-28)</text>
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

- **상승**: 달러 강세 — 연준의 긴축 기대(미국 금리가 상대적으로 높아질 것이라는 예상), 안전자산 수요 확대, 유로존 등 다른 나라 경기 둔화 신호로 흔히 해석한다.
- **하락**: 달러 약세 — 연준의 완화 기대, 위험선호 확대, 다른 나라 경기 개선 신호로 흔히 해석한다.
- **왜 이렇게 계산되나**: 유로·엔·파운드·캐나다달러·스웨덴크로나·스위스프랑, 6개 통화를 묶은 바스켓을 기하평균해서 계산한다. 변동환율제가 시작된 1973년을 기준값 100으로 삼아 출발했다. 원화나 위안화처럼 그 이후 국제무역에서 비중이 커진 통화가 바스켓에 빠져 있다는 점이 이 지수의 대표적인 한계로 자주 지적된다.
- 유로 비중이 약 58%로 압도적이라 유로/달러 환율이 사실상 이 지수를 주도한다 — 두 지표를 서로 독립된 근거로 중복 인용하지 않는다.

---

*작성일: 2026-08-29*
