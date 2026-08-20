# 닛케이225 — 기술적 참고 (주봉 5년)

!!! note ""
    최근 5년 닛케이225 지수(일본, `^N225`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 엔/달러 환율과 함께 보면 일본 시장·엔화 국면을 종합적으로 확인할 수 있다 — 엔 약세는 대개 일본 수출기업 실적 기대를 밀어올려 닛케이 강세와 같이 나타나는 경우가 많다.

---

## 1. 차트 — 최근 5년 주봉

<div class="n225-chart">
<style>
.n225-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .n225-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 66,216.79 (2026-08-20) · 단위 지수</text>
<line x1="60" y1="548.5" x2="1052" y2="548.5" class="grid"/>
<text x="52" y="552.5" font-size="11" text-anchor="end" fill="var(--muted)">30,000</text>
<line x1="60" y1="437.8" x2="1052" y2="437.8" class="grid"/>
<text x="52" y="441.8" font-size="11" text-anchor="end" fill="var(--muted)">40,000</text>
<line x1="60" y1="327.2" x2="1052" y2="327.2" class="grid"/>
<text x="52" y="331.2" font-size="11" text-anchor="end" fill="var(--muted)">50,000</text>
<line x1="60" y1="216.5" x2="1052" y2="216.5" class="grid"/>
<text x="52" y="220.5" font-size="11" text-anchor="end" fill="var(--muted)">60,000</text>
<line x1="60" y1="105.8" x2="1052" y2="105.8" class="grid"/>
<text x="52" y="109.8" font-size="11" text-anchor="end" fill="var(--muted)">70,000</text>
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
<line x1="61.9" y1="578.2" x2="61.9" y2="582.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="579.1" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="65.7" y1="571.8" x2="65.7" y2="579.6" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="574.6" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="69.4" y1="557.9" x2="69.4" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="558.2" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="73.2" y1="544.3" x2="73.2" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="544.3" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="77.0" y1="539.7" x2="77.0" y2="546.3" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="543.0" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="80.7" y1="545.5" x2="80.7" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="545.8" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="84.5" y1="543.9" x2="84.5" y2="563.1" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="545.4" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="88.3" y1="559.1" x2="88.3" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="559.1" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="92.1" y1="558.7" x2="92.1" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="558.8" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="95.8" y1="554.2" x2="95.8" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="558.6" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="99.6" y1="557.8" x2="99.6" y2="565.4" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="560.8" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="103.4" y1="549.8" x2="103.4" y2="556.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="552.8" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="107.1" y1="551.3" x2="107.1" y2="559.1" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="551.5" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="110.9" y1="549.0" x2="110.9" y2="555.1" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="550.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="114.7" y1="550.7" x2="114.7" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="552.7" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="118.5" y1="562.1" x2="118.5" y2="575.2" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="566.9" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="122.2" y1="560.6" x2="122.2" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="565.8" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="126.0" y1="558.8" x2="126.0" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="562.9" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="129.8" y1="561.0" x2="129.8" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="562.0" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="133.6" y1="558.3" x2="133.6" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="561.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="137.3" y1="555.3" x2="137.3" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="558.5" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="141.1" y1="561.6" x2="141.1" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="566.4" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="144.9" y1="563.0" x2="144.9" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="567.0" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="148.6" y1="574.8" x2="148.6" y2="592.3" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="578.9" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="152.4" y1="575.5" x2="152.4" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="576.9" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="156.2" y1="572.0" x2="156.2" y2="580.8" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="574.0" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="160.0" y1="576.3" x2="160.0" y2="584.8" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="578.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="163.7" y1="581.7" x2="163.7" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="584.3" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="167.5" y1="581.6" x2="167.5" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="587.7" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="171.3" y1="595.9" x2="171.3" y2="607.4" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="596.8" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="175.0" y1="583.3" x2="175.0" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="583.6" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="178.8" y1="566.9" x2="178.8" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="569.0" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="182.6" y1="567.5" x2="182.6" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="569.7" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="186.4" y1="571.0" x2="186.4" y2="584.3" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="574.1" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="190.1" y1="579.5" x2="190.1" y2="589.4" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="580.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="193.9" y1="575.3" x2="193.9" y2="586.5" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="580.6" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="197.7" y1="583.1" x2="197.7" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="583.4" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="201.4" y1="580.9" x2="201.4" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="581.7" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="205.2" y1="584.7" x2="205.2" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="585.0" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="209.0" y1="581.1" x2="209.0" y2="591.1" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="584.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="212.8" y1="581.2" x2="212.8" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="581.8" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="216.5" y1="573.1" x2="216.5" y2="581.1" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="573.3" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="220.3" y1="566.3" x2="220.3" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="572.6" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="224.1" y1="577.4" x2="224.1" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="577.6" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="227.8" y1="587.1" x2="227.8" y2="598.1" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="587.4" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="231.6" y1="581.0" x2="231.6" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="584.6" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="235.4" y1="583.0" x2="235.4" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="587.1" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="239.2" y1="581.0" x2="239.2" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="582.9" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="242.9" y1="571.2" x2="242.9" y2="584.0" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="571.6" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="246.7" y1="570.5" x2="246.7" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="572.9" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="250.5" y1="568.6" x2="250.5" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="568.7" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="254.3" y1="564.6" x2="254.3" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="564.6" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="258.0" y1="557.1" x2="258.0" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="560.4" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="261.8" y1="561.5" x2="261.8" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="563.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="265.6" y1="568.1" x2="265.6" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="568.9" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="269.3" y1="567.5" x2="269.3" y2="578.8" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="568.3" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="273.1" y1="563.4" x2="273.1" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="565.3" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="276.9" y1="571.7" x2="276.9" y2="582.2" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="573.0" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="280.7" y1="584.2" x2="280.7" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="584.2" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="284.4" y1="577.3" x2="284.4" y2="597.0" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="580.4" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="288.2" y1="579.7" x2="288.2" y2="590.2" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="580.7" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="292.0" y1="577.6" x2="292.0" y2="585.6" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="582.9" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="295.7" y1="575.3" x2="295.7" y2="582.0" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="579.1" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="299.5" y1="574.1" x2="299.5" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="577.3" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="303.3" y1="567.0" x2="303.3" y2="577.8" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="567.7" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="307.1" y1="567.3" x2="307.1" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="567.6" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="310.8" y1="565.1" x2="310.8" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="567.5" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="314.6" y1="566.0" x2="314.6" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="568.2" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="318.4" y1="571.2" x2="318.4" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="571.8" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="322.1" y1="568.5" x2="322.1" y2="576.3" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="573.5" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="325.9" y1="577.9" x2="325.9" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="578.6" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="329.7" y1="585.9" x2="329.7" y2="593.3" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="589.5" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="333.5" y1="592.4" x2="333.5" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="593.1" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="337.2" y1="586.7" x2="337.2" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="590.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="341.0" y1="583.8" x2="341.0" y2="595.6" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="586.7" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="344.8" y1="576.2" x2="344.8" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="577.5" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="348.5" y1="574.9" x2="348.5" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="576.1" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="352.3" y1="572.6" x2="352.3" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="573.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="573.7" x2="356.1" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="575.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="359.9" y1="575.8" x2="359.9" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="576.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="363.6" y1="571.1" x2="363.6" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="571.5" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="367.4" y1="562.5" x2="367.4" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="568.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="371.2" y1="571.7" x2="371.2" y2="585.8" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="571.9" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="375.0" y1="576.0" x2="375.0" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="577.5" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="378.7" y1="569.3" x2="378.7" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="570.2" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="382.5" y1="567.5" x2="382.5" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="568.4" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="386.3" y1="565.0" x2="386.3" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="565.2" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="390.0" y1="562.0" x2="390.0" y2="566.1" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="564.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="393.8" y1="560.9" x2="393.8" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="561.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="397.6" y1="556.5" x2="397.6" y2="559.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="557.8" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="401.4" y1="554.9" x2="401.4" y2="560.3" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="555.3" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="405.1" y1="538.3" x2="405.1" y2="554.3" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="539.6" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="408.9" y1="533.6" x2="408.9" y2="542.3" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="538.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="412.7" y1="531.3" x2="412.7" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="531.7" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="416.4" y1="518.5" x2="416.4" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="523.5" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="420.2" y1="506.8" x2="420.2" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="507.5" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="424.0" y1="506.8" x2="424.0" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="506.8" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="427.8" y1="509.5" x2="427.8" y2="523.0" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="513.2" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="431.5" y1="506.9" x2="431.5" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="509.6" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="435.3" y1="517.7" x2="435.3" y2="528.7" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="522.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="439.1" y1="516.5" x2="439.1" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="521.3" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="442.8" y1="516.0" x2="442.8" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="518.0" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="446.6" y1="509.9" x2="446.6" y2="527.1" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="513.9" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="450.4" y1="520.4" x2="450.4" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="521.1" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="454.2" y1="519.6" x2="454.2" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="521.3" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="457.9" y1="523.1" x2="457.9" y2="532.9" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="530.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="461.7" y1="517.0" x2="461.7" y2="527.7" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="518.5" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="465.5" y1="511.8" x2="465.5" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="517.6" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="469.2" y1="508.3" x2="469.2" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="509.4" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="473.0" y1="511.6" x2="473.0" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="512.0" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="476.8" y1="518.4" x2="476.8" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="520.7" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="480.6" y1="521.9" x2="480.6" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="525.3" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="484.3" y1="520.5" x2="484.3" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="522.9" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="488.1" y1="523.5" x2="488.1" y2="536.4" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="526.6" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="491.9" y1="532.3" x2="491.9" y2="542.4" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="535.8" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="495.7" y1="525.4" x2="495.7" y2="542.6" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="526.9" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="499.4" y1="517.9" x2="499.4" y2="525.8" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="520.1" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="503.2" y1="508.5" x2="503.2" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="508.8" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="507.0" y1="505.9" x2="507.0" y2="513.3" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="508.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="506.3" x2="510.7" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="507.5" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="514.5" y1="510.3" x2="514.5" y2="524.1" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="511.8" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="518.3" y1="513.4" x2="518.3" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="515.6" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="522.1" y1="506.2" x2="522.1" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="513.4" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="525.8" y1="507.0" x2="525.8" y2="513.3" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="510.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="529.6" y1="509.0" x2="529.6" y2="518.7" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="511.1" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="533.4" y1="483.9" x2="533.4" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="486.8" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="537.1" y1="479.5" x2="537.1" y2="489.1" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="482.5" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="540.9" y1="471.2" x2="540.9" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="478.9" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="544.7" y1="477.2" x2="544.7" y2="485.4" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="480.4" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="548.5" y1="467.9" x2="548.5" y2="483.7" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="472.2" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="552.2" y1="450.4" x2="552.2" y2="469.0" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="454.6" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="556.0" y1="447.2" x2="556.0" y2="458.9" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="447.8" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="559.8" y1="438.0" x2="559.8" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="438.8" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="563.5" y1="432.6" x2="563.5" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="435.6" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="567.3" y1="446.2" x2="567.3" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="446.3" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="571.1" y1="425.8" x2="571.1" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="428.0" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="574.9" y1="427.0" x2="574.9" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="429.0" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="578.6" y1="430.1" x2="578.6" y2="451.4" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="430.7" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="582.4" y1="440.3" x2="582.4" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="443.1" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="586.2" y1="446.3" x2="586.2" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="448.3" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="589.9" y1="454.9" x2="589.9" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="460.7" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="593.7" y1="453.2" x2="593.7" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="456.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="597.5" y1="450.4" x2="597.5" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="452.9" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="601.3" y1="449.5" x2="601.3" y2="460.3" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="451.3" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="605.0" y1="444.1" x2="605.0" y2="455.9" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="451.5" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="608.8" y1="447.3" x2="608.8" y2="464.2" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="451.5" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="612.6" y1="448.6" x2="612.6" y2="456.2" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="451.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="616.3" y1="445.2" x2="616.3" y2="453.8" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="451.0" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="620.1" y1="451.1" x2="620.1" y2="460.5" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="453.4" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="623.9" y1="440.2" x2="623.9" y2="455.4" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="442.5" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="627.7" y1="425.7" x2="627.7" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="427.7" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="631.4" y1="411.0" x2="631.4" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="424.7" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="635.2" y1="421.0" x2="635.2" y2="439.8" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="422.7" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="639.0" y1="438.1" x2="639.0" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="438.4" width="2.34" height="25.2" fill="var(--down)"/>
<line x1="642.8" y1="446.8" x2="642.8" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="458.4" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="646.5" y1="483.8" x2="646.5" y2="535.7" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="490.4" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="650.3" y1="458.4" x2="650.3" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="459.3" width="2.34" height="28.5" fill="var(--up)"/>
<line x1="654.1" y1="455.3" x2="654.1" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="455.9" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="657.8" y1="452.6" x2="657.8" y2="461.9" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="452.8" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="661.6" y1="448.0" x2="661.6" y2="479.5" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="448.6" width="2.34" height="29.2" fill="var(--down)"/>
<line x1="665.4" y1="472.1" x2="665.4" y2="490.4" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="475.7" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="669.2" y1="460.3" x2="669.2" y2="484.0" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="463.0" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="672.9" y1="439.7" x2="672.9" y2="461.4" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="439.7" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="676.7" y1="447.5" x2="676.7" y2="463.8" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="447.6" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="680.5" y1="441.5" x2="680.5" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="442.2" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="684.2" y1="435.0" x2="684.2" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="437.3" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="688.0" y1="447.6" x2="688.0" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="449.4" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="691.8" y1="444.3" x2="691.8" y2="462.7" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="459.4" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="695.6" y1="439.1" x2="695.6" y2="458.2" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="443.4" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="699.3" y1="439.3" x2="699.3" y2="454.1" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="444.3" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="703.1" y1="453.8" x2="703.1" y2="460.6" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="456.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="706.9" y1="448.3" x2="706.9" y2="462.2" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="452.5" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="710.6" y1="441.9" x2="710.6" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="447.9" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="714.4" y1="436.8" x2="714.4" y2="449.2" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="443.7" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="718.2" y1="440.1" x2="718.2" y2="456.0" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="442.8" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="722.0" y1="433.4" x2="722.0" y2="450.6" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="434.7" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="725.7" y1="434.2" x2="725.7" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="434.2" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="729.5" y1="434.6" x2="729.5" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="438.4" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="733.3" y1="448.3" x2="733.3" y2="459.4" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="448.8" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="737.0" y1="434.7" x2="737.0" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="438.6" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="740.8" y1="435.0" x2="740.8" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="436.4" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="744.6" y1="446.8" x2="744.6" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="449.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="748.4" y1="442.5" x2="748.4" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="447.3" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="752.1" y1="443.3" x2="752.1" y2="454.9" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="447.9" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="755.9" y1="454.6" x2="755.9" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="456.0" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="759.7" y1="461.4" x2="759.7" y2="473.1" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="464.2" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="763.5" y1="467.4" x2="763.5" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="470.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="767.2" y1="458.6" x2="767.2" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="463.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="771.0" y1="457.5" x2="771.0" y2="472.5" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="461.7" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="774.8" y1="477.2" x2="774.8" y2="512.4" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="477.2" width="2.34" height="29.4" fill="var(--down)"/>
<line x1="778.5" y1="497.2" x2="778.5" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="508.8" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="782.3" y1="495.9" x2="782.3" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="496.2" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="786.1" y1="483.9" x2="786.1" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="485.4" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="789.9" y1="471.3" x2="789.9" y2="484.6" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="472.9" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="793.6" y1="464.9" x2="793.6" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="465.5" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="797.4" y1="454.5" x2="797.4" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="462.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="801.2" y1="460.8" x2="801.2" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="464.7" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="804.9" y1="455.0" x2="804.9" y2="469.2" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="460.4" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="808.7" y1="461.4" x2="808.7" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="462.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="812.5" y1="454.1" x2="812.5" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="459.7" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="816.3" y1="450.2" x2="816.3" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="455.5" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="820.0" y1="434.9" x2="820.0" y2="459.7" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="436.2" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="823.8" y1="428.4" x2="823.8" y2="444.0" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="431.7" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="827.6" y1="438.2" x2="827.6" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="440.8" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="831.3" y1="436.9" x2="831.3" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="439.8" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="835.1" y1="415.0" x2="835.1" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="421.7" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="838.9" y1="420.9" x2="838.9" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="421.1" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="842.7" y1="415.3" x2="842.7" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="417.7" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="846.4" y1="399.6" x2="846.4" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="400.5" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="850.2" y1="394.9" x2="850.2" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="399.6" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="854.0" y1="402.4" x2="854.0" y2="414.2" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="404.9" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="857.7" y1="402.2" x2="857.7" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="404.4" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="861.5" y1="383.7" x2="861.5" y2="400.8" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="385.1" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="865.3" y1="373.1" x2="865.3" y2="388.1" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="382.0" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="869.1" y1="373.4" x2="869.1" y2="380.4" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="378.6" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="872.8" y1="373.9" x2="872.8" y2="389.6" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="374.0" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="876.6" y1="342.7" x2="876.6" y2="364.9" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="348.3" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="880.4" y1="345.8" x2="880.4" y2="365.4" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="353.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="884.2" y1="327.8" x2="884.2" y2="346.5" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="334.9" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="887.9" y1="300.5" x2="887.9" y2="328.9" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="300.5" width="2.34" height="27.7" fill="var(--up)"/>
<line x1="891.7" y1="298.0" x2="891.7" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="301.8" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="895.5" y1="310.4" x2="895.5" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="320.0" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="899.2" y1="320.8" x2="899.2" y2="346.7" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="324.0" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="903.0" y1="323.6" x2="903.0" y2="343.6" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="324.4" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="906.8" y1="315.8" x2="906.8" y2="335.8" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="321.7" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="910.6" y1="314.7" x2="910.6" y2="328.0" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="317.9" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="914.3" y1="322.4" x2="914.3" y2="342.2" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="323.3" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="918.1" y1="316.7" x2="918.1" y2="327.4" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="318.9" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="921.9" y1="319.3" x2="921.9" y2="325.0" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="319.5" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="925.6" y1="299.2" x2="925.6" y2="316.1" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="305.7" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="929.4" y1="277.5" x2="929.4" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="283.6" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="933.2" y1="282.3" x2="933.2" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="284.6" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="937.0" y1="285.7" x2="937.0" y2="298.0" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="290.4" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="940.7" y1="274.2" x2="940.7" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="280.1" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="944.5" y1="238.5" x2="944.5" y2="271.6" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="250.3" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="948.3" y1="241.8" x2="948.3" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="247.3" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="952.0" y1="223.9" x2="952.0" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="229.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="955.8" y1="234.6" x2="955.8" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="238.9" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="959.6" y1="263.6" x2="959.6" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="276.2" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="963.4" y1="269.2" x2="963.4" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="287.0" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="967.1" y1="280.9" x2="967.1" y2="319.5" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="289.8" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="970.9" y1="280.0" x2="970.9" y2="321.0" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="292.6" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="974.7" y1="249.5" x2="974.7" y2="292.2" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="250.5" width="2.34" height="41.2" fill="var(--up)"/>
<line x1="978.4" y1="219.9" x2="978.4" y2="258.2" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="233.4" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="982.2" y1="216.3" x2="982.2" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="219.6" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="986.0" y1="206.5" x2="986.0" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="217.8" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="989.8" y1="182.3" x2="989.8" y2="214.1" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="186.5" width="2.34" height="27.4" fill="var(--up)"/>
<line x1="993.5" y1="174.4" x2="993.5" y2="206.1" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="181.0" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="997.3" y1="178.5" x2="997.3" y2="224.3" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="179.5" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="1001.1" y1="144.5" x2="1001.1" y2="177.1" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="146.4" width="2.34" height="29.6" fill="var(--up)"/>
<line x1="1004.9" y1="119.2" x2="1004.9" y2="155.0" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="143.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="1008.6" y1="138.3" x2="1008.6" y2="190.6" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="149.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1012.4" y1="84.2" x2="1012.4" y2="141.4" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="92.0" width="2.34" height="49.4" fill="var(--up)"/>
<line x1="1016.2" y1="74.5" x2="1016.2" y2="122.8" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="94.0" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="1019.9" y1="84.1" x2="1019.9" y2="132.3" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="108.6" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="1023.7" y1="101.5" x2="1023.7" y2="141.0" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="106.1" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="1027.5" y1="116.0" x2="1027.5" y2="186.6" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="123.4" width="2.34" height="47.3" fill="var(--down)"/>
<line x1="1031.3" y1="132.5" x2="1031.3" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="165.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1035.0" y1="157.1" x2="1035.0" y2="211.5" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="159.3" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="1038.8" y1="146.7" x2="1038.8" y2="186.6" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="154.4" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="1042.6" y1="110.1" x2="1042.6" y2="151.8" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="120.0" width="2.34" height="31.1" fill="var(--up)"/>
<line x1="1046.3" y1="114.4" x2="1046.3" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="118.2" width="2.34" height="39.4" fill="var(--down)"/>
<line x1="1050.1" y1="146.5" x2="1050.1" y2="153.9" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="147.7" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="60" y1="465.9" x2="1052" y2="465.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="459.9" font-size="11.5" fill="var(--support)" font-weight="600">37,469 S1</text>
<text x="1058" y="471.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="538.3" x2="1052" y2="538.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="532.3" font-size="11.5" fill="var(--support)" font-weight="600">30,928 S2</text>
<text x="1058" y="544.3" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="579.8" x2="1052" y2="579.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="573.8" font-size="11.5" fill="var(--support)" font-weight="600">27,172 S3</text>
<text x="1058" y="585.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="147.7" r="3" fill="var(--ink)"/>
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

- **상승**: 엔화 약세(수출기업 실적 기대 개선) 또는 일본 증시 자체의 위험선호 확대와 동행하는 경우가 많다.
- **하락**: 엔화 강세(수출기업 실적 우려) 또는 위험회피 심리와 동행하는 경우가 많다.
- 엔/달러와 반대 상관관계로 흔히 설명되지만 항상 그런 건 아니다 — 엔화 요인과 일본 증시 자체 요인이 겹칠 때는 두 문서를 함께 봐야 어느 쪽이 주도했는지 가늠할 수 있다.

---

## 관련 문서

- [엔/달러](../fx/jpy_usd.md) — 같은 엔화 국면과 얽히는 짝 지표
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Nikkei 225 (^N225)](https://finance.yahoo.com/quote/%5EN225/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
