# 닛케이225

!!! note ""
    최근 5년간 닛케이225 지수(일본, `^N225`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 엔/달러 환율 문서와 함께 보면 일본 증시와 엔화가 지금 어떤 상태인지 종합적으로 확인할 수 있다 — 엔화가 약세일 때는 일본 수출기업의 실적 기대가 좋아져서 닛케이지수도 함께 강세를 보이는 경우가 많다.

---

## 1. 차트 — 최근 5년 주봉

<div class="n225-chart">
<style>
.n225-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .n225-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .n225-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.n225-chart svg { width:100%; height:auto; display:block; }
.n225-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.n225-chart .title { fill: var(--ink); font-weight:600; }
.n225-chart .grid { stroke: var(--grid); stroke-width:1; }
.n225-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="닛케이225(^N225) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">닛케이225 (^N225) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 66,405.56 (2026-08-28) · 단위 지수</text>
<line x1="60" y1="548.5" x2="1052" y2="548.5" class="grid"/>
<text x="52" y="552.5" font-size="11" text-anchor="end" fill="var(--muted)">30,000.00</text>
<line x1="60" y1="437.8" x2="1052" y2="437.8" class="grid"/>
<text x="52" y="441.8" font-size="11" text-anchor="end" fill="var(--muted)">40,000.00</text>
<line x1="60" y1="327.2" x2="1052" y2="327.2" class="grid"/>
<text x="52" y="331.2" font-size="11" text-anchor="end" fill="var(--muted)">50,000.00</text>
<line x1="60" y1="216.5" x2="1052" y2="216.5" class="grid"/>
<text x="52" y="220.5" font-size="11" text-anchor="end" fill="var(--muted)">60,000.00</text>
<line x1="60" y1="105.8" x2="1052" y2="105.8" class="grid"/>
<text x="52" y="109.8" font-size="11" text-anchor="end" fill="var(--muted)">70,000.00</text>
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
<line x1="61.9" y1="557.9" x2="61.9" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="558.2" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="65.7" y1="544.3" x2="65.7" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="544.3" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="69.5" y1="539.7" x2="69.5" y2="546.3" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="543.0" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="73.3" y1="545.5" x2="73.3" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="545.8" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="77.0" y1="543.9" x2="77.0" y2="563.1" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="545.4" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="80.8" y1="559.1" x2="80.8" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="559.1" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="84.6" y1="558.7" x2="84.6" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="558.8" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="88.4" y1="554.2" x2="88.4" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="558.6" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="92.2" y1="557.8" x2="92.2" y2="565.4" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="560.8" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="96.0" y1="549.8" x2="96.0" y2="556.6" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="552.8" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="99.8" y1="551.3" x2="99.8" y2="559.1" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="551.5" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="103.5" y1="549.0" x2="103.5" y2="555.1" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="550.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="107.3" y1="550.7" x2="107.3" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="552.7" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="111.1" y1="562.1" x2="111.1" y2="575.2" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="566.9" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="114.9" y1="560.6" x2="114.9" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="565.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="118.7" y1="558.8" x2="118.7" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="562.9" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="122.5" y1="561.0" x2="122.5" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="562.0" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="126.3" y1="558.3" x2="126.3" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="561.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="130.0" y1="555.3" x2="130.0" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="558.5" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="133.8" y1="561.6" x2="133.8" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="566.4" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="137.6" y1="563.0" x2="137.6" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="567.0" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="141.4" y1="574.8" x2="141.4" y2="592.3" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="578.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="145.2" y1="575.5" x2="145.2" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="576.9" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="149.0" y1="572.0" x2="149.0" y2="580.8" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="574.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="152.8" y1="576.3" x2="152.8" y2="584.8" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="578.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="156.5" y1="581.7" x2="156.5" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="584.3" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="160.3" y1="581.6" x2="160.3" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="587.7" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="164.1" y1="595.9" x2="164.1" y2="607.4" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="596.8" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="167.9" y1="583.3" x2="167.9" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="583.6" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="171.7" y1="566.9" x2="171.7" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="569.0" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="175.5" y1="567.5" x2="175.5" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="569.7" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="179.3" y1="571.0" x2="179.3" y2="584.3" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="574.1" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="183.1" y1="579.5" x2="183.1" y2="589.4" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="580.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="186.8" y1="575.3" x2="186.8" y2="586.5" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="580.6" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="190.6" y1="583.1" x2="190.6" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="583.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="194.4" y1="580.9" x2="194.4" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="581.7" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="198.2" y1="584.7" x2="198.2" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="585.0" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="202.0" y1="581.1" x2="202.0" y2="591.1" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="584.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="205.8" y1="581.2" x2="205.8" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="581.8" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="209.6" y1="573.1" x2="209.6" y2="581.1" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="573.3" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="213.3" y1="566.3" x2="213.3" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="572.6" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="217.1" y1="577.4" x2="217.1" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="577.6" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="220.9" y1="587.1" x2="220.9" y2="598.1" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="587.4" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="224.7" y1="581.0" x2="224.7" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="584.6" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="228.5" y1="583.0" x2="228.5" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="587.1" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="232.3" y1="581.0" x2="232.3" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="582.9" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="236.1" y1="571.2" x2="236.1" y2="584.0" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="571.6" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="239.8" y1="570.5" x2="239.8" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="572.9" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="243.6" y1="568.6" x2="243.6" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="568.7" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="247.4" y1="564.6" x2="247.4" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="564.6" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="251.2" y1="557.1" x2="251.2" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="560.4" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="255.0" y1="561.5" x2="255.0" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="563.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="258.8" y1="568.1" x2="258.8" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="568.9" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="262.6" y1="567.5" x2="262.6" y2="578.8" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="568.3" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="266.4" y1="563.4" x2="266.4" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="565.3" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="270.1" y1="571.7" x2="270.1" y2="582.2" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="573.0" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="273.9" y1="584.2" x2="273.9" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="584.2" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="277.7" y1="577.3" x2="277.7" y2="597.0" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="580.4" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="281.5" y1="579.7" x2="281.5" y2="590.2" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="580.7" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="285.3" y1="577.6" x2="285.3" y2="585.6" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="582.9" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="289.1" y1="575.3" x2="289.1" y2="582.0" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="579.1" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="292.9" y1="574.1" x2="292.9" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="577.3" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="296.6" y1="567.0" x2="296.6" y2="577.8" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="567.7" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="300.4" y1="567.3" x2="300.4" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="567.6" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="304.2" y1="565.1" x2="304.2" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="567.5" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="308.0" y1="566.0" x2="308.0" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="568.2" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="311.8" y1="571.2" x2="311.8" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="571.8" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="315.6" y1="568.5" x2="315.6" y2="576.3" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="573.5" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="319.4" y1="577.9" x2="319.4" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="578.6" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="323.1" y1="585.9" x2="323.1" y2="593.3" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="589.5" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="326.9" y1="592.4" x2="326.9" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="593.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="330.7" y1="586.7" x2="330.7" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="590.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="334.5" y1="583.8" x2="334.5" y2="595.6" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="586.7" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="338.3" y1="576.2" x2="338.3" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="577.5" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="342.1" y1="574.9" x2="342.1" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="576.1" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="345.9" y1="572.6" x2="345.9" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="573.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="349.6" y1="573.7" x2="349.6" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="575.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="353.4" y1="575.8" x2="353.4" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="576.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="571.1" x2="357.2" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="571.5" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="361.0" y1="562.5" x2="361.0" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="568.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="364.8" y1="571.7" x2="364.8" y2="585.8" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="571.9" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="368.6" y1="576.0" x2="368.6" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="577.5" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="372.4" y1="569.3" x2="372.4" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="570.2" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="376.2" y1="567.5" x2="376.2" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="568.4" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="379.9" y1="565.0" x2="379.9" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="565.2" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="383.7" y1="562.0" x2="383.7" y2="566.1" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="564.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="387.5" y1="560.9" x2="387.5" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="561.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="391.3" y1="556.5" x2="391.3" y2="559.4" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="557.8" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="395.1" y1="554.9" x2="395.1" y2="560.3" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="555.3" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="398.9" y1="538.3" x2="398.9" y2="554.3" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="539.6" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="402.7" y1="533.6" x2="402.7" y2="542.3" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="538.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="406.4" y1="531.3" x2="406.4" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="531.7" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="410.2" y1="518.5" x2="410.2" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="523.5" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="414.0" y1="506.8" x2="414.0" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="507.5" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="417.8" y1="506.8" x2="417.8" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="506.8" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="421.6" y1="509.5" x2="421.6" y2="523.0" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="513.2" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="425.4" y1="506.9" x2="425.4" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="509.6" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="429.2" y1="517.7" x2="429.2" y2="528.7" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="522.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="432.9" y1="516.5" x2="432.9" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="521.3" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="436.7" y1="516.0" x2="436.7" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="518.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="440.5" y1="509.9" x2="440.5" y2="527.1" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="513.9" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="444.3" y1="520.4" x2="444.3" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="521.1" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="448.1" y1="519.6" x2="448.1" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="521.3" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="451.9" y1="523.1" x2="451.9" y2="532.9" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="530.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="455.7" y1="517.0" x2="455.7" y2="527.7" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="518.5" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="459.5" y1="511.8" x2="459.5" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="517.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="463.2" y1="508.3" x2="463.2" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="509.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="467.0" y1="511.6" x2="467.0" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="512.0" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="470.8" y1="518.4" x2="470.8" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="520.7" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="474.6" y1="521.9" x2="474.6" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="525.3" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="478.4" y1="520.5" x2="478.4" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="522.9" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="482.2" y1="523.5" x2="482.2" y2="536.4" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="526.6" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="486.0" y1="532.3" x2="486.0" y2="542.4" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="535.8" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="489.7" y1="525.4" x2="489.7" y2="542.6" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="526.9" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="493.5" y1="517.9" x2="493.5" y2="525.8" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="520.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="497.3" y1="508.5" x2="497.3" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="508.8" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="501.1" y1="505.9" x2="501.1" y2="513.3" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="508.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="504.9" y1="506.3" x2="504.9" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="507.5" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="508.7" y1="510.3" x2="508.7" y2="524.1" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="511.8" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="512.5" y1="513.4" x2="512.5" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="515.6" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="516.2" y1="506.2" x2="516.2" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="513.4" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="520.0" y1="507.0" x2="520.0" y2="513.3" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="510.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="509.0" x2="523.8" y2="518.7" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="511.1" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="527.6" y1="483.9" x2="527.6" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="486.8" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="531.4" y1="479.5" x2="531.4" y2="489.1" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="482.5" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="535.2" y1="471.2" x2="535.2" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="478.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="539.0" y1="477.2" x2="539.0" y2="485.4" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="480.4" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="542.7" y1="467.9" x2="542.7" y2="483.7" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="472.2" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="546.5" y1="450.4" x2="546.5" y2="469.0" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="454.6" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="550.3" y1="447.2" x2="550.3" y2="458.9" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="447.8" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="554.1" y1="438.0" x2="554.1" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="438.8" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="557.9" y1="432.6" x2="557.9" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="435.6" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="561.7" y1="446.2" x2="561.7" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="446.3" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="565.5" y1="425.8" x2="565.5" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="428.0" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="569.3" y1="427.0" x2="569.3" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="429.0" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="573.0" y1="430.1" x2="573.0" y2="451.4" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="430.7" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="576.8" y1="440.3" x2="576.8" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="443.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="580.6" y1="446.3" x2="580.6" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="448.3" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="584.4" y1="454.9" x2="584.4" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="460.7" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="588.2" y1="453.2" x2="588.2" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="456.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="592.0" y1="450.4" x2="592.0" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="452.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="595.8" y1="449.5" x2="595.8" y2="460.3" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="451.3" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="599.5" y1="444.1" x2="599.5" y2="455.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="451.5" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="603.3" y1="447.3" x2="603.3" y2="464.2" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="451.5" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="607.1" y1="448.6" x2="607.1" y2="456.2" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="451.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="610.9" y1="445.2" x2="610.9" y2="453.8" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="451.0" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="614.7" y1="451.1" x2="614.7" y2="460.5" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="453.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="618.5" y1="440.2" x2="618.5" y2="455.4" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="442.5" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="622.3" y1="425.7" x2="622.3" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="427.7" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="626.0" y1="411.0" x2="626.0" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="424.7" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="629.8" y1="421.0" x2="629.8" y2="439.8" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="422.7" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="633.6" y1="438.1" x2="633.6" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="438.4" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="637.4" y1="446.8" x2="637.4" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="458.4" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="641.2" y1="483.8" x2="641.2" y2="535.7" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="490.4" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="645.0" y1="458.4" x2="645.0" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="459.3" width="2.35" height="28.5" fill="var(--up)"/>
<line x1="648.8" y1="455.3" x2="648.8" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="455.9" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="652.5" y1="452.6" x2="652.5" y2="461.9" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="452.8" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="656.3" y1="448.0" x2="656.3" y2="479.5" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="448.6" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="660.1" y1="472.1" x2="660.1" y2="490.4" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="475.7" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="663.9" y1="460.3" x2="663.9" y2="484.0" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="463.0" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="667.7" y1="439.7" x2="667.7" y2="461.4" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="439.7" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="671.5" y1="447.5" x2="671.5" y2="463.8" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="447.6" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="675.3" y1="441.5" x2="675.3" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="442.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="679.1" y1="435.0" x2="679.1" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="437.3" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="682.8" y1="447.6" x2="682.8" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="449.4" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="686.6" y1="444.3" x2="686.6" y2="462.7" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="459.4" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="690.4" y1="439.1" x2="690.4" y2="458.2" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="443.4" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="694.2" y1="439.3" x2="694.2" y2="454.1" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="444.3" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="698.0" y1="453.8" x2="698.0" y2="460.6" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="456.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="701.8" y1="448.3" x2="701.8" y2="462.2" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="452.5" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="705.6" y1="441.9" x2="705.6" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="447.9" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="709.3" y1="436.8" x2="709.3" y2="449.2" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="443.7" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="713.1" y1="440.1" x2="713.1" y2="456.0" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="442.8" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="716.9" y1="433.4" x2="716.9" y2="450.6" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="434.7" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="720.7" y1="434.2" x2="720.7" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="434.2" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="724.5" y1="434.6" x2="724.5" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="438.4" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="728.3" y1="448.3" x2="728.3" y2="459.4" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="448.8" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="732.1" y1="434.7" x2="732.1" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="438.6" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="735.8" y1="435.0" x2="735.8" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="436.4" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="739.6" y1="446.8" x2="739.6" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="449.7" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="743.4" y1="442.5" x2="743.4" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="447.3" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="747.2" y1="443.3" x2="747.2" y2="454.9" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="447.9" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="751.0" y1="454.6" x2="751.0" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="456.0" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="754.8" y1="461.4" x2="754.8" y2="473.1" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="464.2" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="758.6" y1="467.4" x2="758.6" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="470.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="762.4" y1="458.6" x2="762.4" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="463.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="766.1" y1="457.5" x2="766.1" y2="472.5" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="461.7" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="769.9" y1="477.2" x2="769.9" y2="512.4" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="477.2" width="2.35" height="29.4" fill="var(--down)"/>
<line x1="773.7" y1="497.2" x2="773.7" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="508.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="777.5" y1="495.9" x2="777.5" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="496.2" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="781.3" y1="483.9" x2="781.3" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="485.4" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="785.1" y1="471.3" x2="785.1" y2="484.6" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="472.9" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="788.9" y1="464.9" x2="788.9" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="465.5" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="792.6" y1="454.5" x2="792.6" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="462.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="796.4" y1="460.8" x2="796.4" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="464.7" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="800.2" y1="455.0" x2="800.2" y2="469.2" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="460.4" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="804.0" y1="461.4" x2="804.0" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="462.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="807.8" y1="454.1" x2="807.8" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="459.7" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="811.6" y1="450.2" x2="811.6" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="455.5" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="815.4" y1="434.9" x2="815.4" y2="459.7" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="436.2" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="819.1" y1="428.4" x2="819.1" y2="444.0" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="431.7" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="822.9" y1="438.2" x2="822.9" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="440.8" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="826.7" y1="436.9" x2="826.7" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="439.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="830.5" y1="415.0" x2="830.5" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="421.7" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="834.3" y1="420.9" x2="834.3" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="421.1" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="838.1" y1="415.3" x2="838.1" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="417.7" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="841.9" y1="399.6" x2="841.9" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="400.5" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="845.6" y1="394.9" x2="845.6" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="399.6" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="849.4" y1="402.4" x2="849.4" y2="414.2" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="404.9" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="853.2" y1="402.2" x2="853.2" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="404.4" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="857.0" y1="383.7" x2="857.0" y2="400.8" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="385.1" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="860.8" y1="373.1" x2="860.8" y2="388.1" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="382.0" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="864.6" y1="373.4" x2="864.6" y2="380.4" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="378.6" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="868.4" y1="373.9" x2="868.4" y2="389.6" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="374.0" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="872.2" y1="342.7" x2="872.2" y2="364.9" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="348.3" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="875.9" y1="345.8" x2="875.9" y2="365.4" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="353.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="879.7" y1="327.8" x2="879.7" y2="346.5" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="334.9" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="883.5" y1="300.5" x2="883.5" y2="328.9" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="300.5" width="2.35" height="27.7" fill="var(--up)"/>
<line x1="887.3" y1="298.0" x2="887.3" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="301.8" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="891.1" y1="310.4" x2="891.1" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="320.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="894.9" y1="320.8" x2="894.9" y2="346.7" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="324.0" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="898.7" y1="323.6" x2="898.7" y2="343.6" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="324.4" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="902.4" y1="315.8" x2="902.4" y2="335.8" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="321.7" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="906.2" y1="314.7" x2="906.2" y2="328.0" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="317.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="910.0" y1="322.4" x2="910.0" y2="342.2" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="323.3" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="913.8" y1="316.7" x2="913.8" y2="327.4" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="318.9" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="917.6" y1="319.3" x2="917.6" y2="325.0" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="319.5" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="921.4" y1="299.2" x2="921.4" y2="316.1" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="305.7" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="925.2" y1="277.5" x2="925.2" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="283.6" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="928.9" y1="282.3" x2="928.9" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="284.6" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="932.7" y1="285.7" x2="932.7" y2="298.0" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="290.4" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="936.5" y1="274.2" x2="936.5" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="280.1" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="940.3" y1="238.5" x2="940.3" y2="271.6" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="250.3" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="944.1" y1="241.8" x2="944.1" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="247.3" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="947.9" y1="223.9" x2="947.9" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="229.2" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="951.7" y1="234.6" x2="951.7" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="238.9" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="955.5" y1="263.6" x2="955.5" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="276.2" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="959.2" y1="269.2" x2="959.2" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="287.0" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="963.0" y1="280.9" x2="963.0" y2="319.5" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="289.8" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="966.8" y1="280.0" x2="966.8" y2="321.0" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="292.6" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="970.6" y1="249.5" x2="970.6" y2="292.2" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="250.5" width="2.35" height="41.2" fill="var(--up)"/>
<line x1="974.4" y1="219.9" x2="974.4" y2="258.2" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="233.4" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="978.2" y1="216.3" x2="978.2" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="219.6" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="982.0" y1="206.5" x2="982.0" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="217.8" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="985.7" y1="182.3" x2="985.7" y2="214.1" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="186.5" width="2.35" height="27.4" fill="var(--up)"/>
<line x1="989.5" y1="174.4" x2="989.5" y2="206.1" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="181.0" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="993.3" y1="178.5" x2="993.3" y2="224.3" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="179.5" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="997.1" y1="144.5" x2="997.1" y2="177.1" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="146.4" width="2.35" height="29.6" fill="var(--up)"/>
<line x1="1000.9" y1="119.2" x2="1000.9" y2="155.0" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="143.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="1004.7" y1="138.3" x2="1004.7" y2="190.6" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="149.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1008.5" y1="84.2" x2="1008.5" y2="141.4" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="92.0" width="2.35" height="49.4" fill="var(--up)"/>
<line x1="1012.2" y1="74.5" x2="1012.2" y2="122.8" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="94.0" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="1016.0" y1="84.1" x2="1016.0" y2="132.3" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="108.6" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="1019.8" y1="101.5" x2="1019.8" y2="141.0" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="106.1" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="1023.6" y1="116.0" x2="1023.6" y2="186.6" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="123.4" width="2.35" height="47.3" fill="var(--down)"/>
<line x1="1027.4" y1="132.5" x2="1027.4" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="165.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1031.2" y1="157.1" x2="1031.2" y2="211.5" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="159.3" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="1035.0" y1="146.7" x2="1035.0" y2="186.6" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="154.4" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="1038.7" y1="110.1" x2="1038.7" y2="151.8" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="120.0" width="2.35" height="31.1" fill="var(--up)"/>
<line x1="1042.5" y1="114.4" x2="1042.5" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="118.2" width="2.35" height="31.7" fill="var(--down)"/>
<line x1="1046.3" y1="139.5" x2="1046.3" y2="165.5" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="148.6" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="1050.1" y1="140.7" x2="1050.1" y2="149.9" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="145.6" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="60" y1="465.9" x2="1052" y2="465.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="459.9" font-size="11.5" fill="var(--support)" font-weight="600">37,468.58 S1</text>
<text x="1058" y="471.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="538.3" x2="1052" y2="538.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="532.3" font-size="11.5" fill="var(--support)" font-weight="600">30,927.94 S2</text>
<text x="1058" y="544.3" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="579.8" x2="1052" y2="579.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="573.8" font-size="11.5" fill="var(--support)" font-weight="600">27,171.72 S3</text>
<text x="1058" y="585.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="145.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="137.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 66,405.56 (2026-08-28)</text>
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

- **상승**: 엔화가 약세를 보이면서 수출기업 실적 기대가 좋아졌거나, 일본 증시 자체의 위험선호가 커졌을 때 함께 나타나는 경우가 많다.
- **하락**: 엔화가 강세를 보이면서 수출기업 실적 우려가 커졌거나, 위험을 피하려는 심리가 커졌을 때 함께 나타나는 경우가 많다.
- 엔/달러 환율과 반대로 움직인다고 흔히 설명하지만, 항상 그런 것은 아니다 — 엔화 자체의 요인과 일본 증시 고유의 요인이 겹칠 때는 두 문서를 함께 봐야 어느 쪽이 주도했는지 가늠할 수 있다.
- **참고**: 닛케이225도 다우존스산업지수처럼 **주가 가중** 방식이라, 회사 규모(시가총액)와 상관없이 주가가 높은 종목의 비중이 크다. 일본은행(BOJ)의 정책금리가 다른 주요국보다 낮게 유지돼 온 것이 엔화가 대표적인 캐리트레이드 조달 통화로 자리 잡은 배경이고, 이 금리차가 벌어질수록 "엔화 약세 → 닛케이 강세" 흐름이 강해지는 경향이 있다.

---

*작성일: 2026-08-29*
