# 원/달러 환율 (USD/KRW)

!!! note ""
    최근 5년간 원/달러 환율(1달러가 몇 원인지, `KRW=X`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 해외 매출 비중이 큰 회사가 환율 변화에 얼마나 민감한지, 또는 상수통화(constant currency, 환율 변동 효과를 뺀 성장률) 기준 성장률과 실제 보고된 성장률이 왜 차이 나는지를 설명할 때 자주 쓰이는 지표다.

---

## 1. 차트 — 최근 5년 주봉

<div class="krw-x-chart">
<style>
.krw-x-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .krw-x-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .krw-x-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.krw-x-chart svg { width:100%; height:auto; display:block; }
.krw-x-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.krw-x-chart .title { fill: var(--ink); font-weight:600; }
.krw-x-chart .grid { stroke: var(--grid); stroke-width:1; }
.krw-x-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="원/달러 환율(KRW=X) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">원/달러 환율 (KRW=X) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-23 · 마지막 종가 1,383.90원 (2026-08-23) · 단위 원</text>
<line x1="60" y1="542.0" x2="1052" y2="542.0" class="grid"/>
<text x="52" y="546.0" font-size="11" text-anchor="end" fill="var(--muted)">1,200.00</text>
<line x1="60" y1="422.0" x2="1052" y2="422.0" class="grid"/>
<text x="52" y="426.0" font-size="11" text-anchor="end" fill="var(--muted)">1,300.00</text>
<line x1="60" y1="302.0" x2="1052" y2="302.0" class="grid"/>
<text x="52" y="306.0" font-size="11" text-anchor="end" fill="var(--muted)">1,400.00</text>
<line x1="60" y1="182.0" x2="1052" y2="182.0" class="grid"/>
<text x="52" y="186.0" font-size="11" text-anchor="end" fill="var(--muted)">1,500.00</text>
<line x1="60" y1="62.0" x2="1052" y2="62.0" class="grid"/>
<text x="52" y="66.0" font-size="11" text-anchor="end" fill="var(--muted)">1,600.00</text>
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
<line x1="61.9" y1="573.5" x2="61.9" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="573.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="65.7" y1="570.3" x2="65.7" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="572.6" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="69.4" y1="582.0" x2="69.4" y2="599.4" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="588.4" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="73.2" y1="573.8" x2="73.2" y2="596.4" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="578.1" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="77.0" y1="565.1" x2="77.0" y2="584.0" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="565.1" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="80.7" y1="551.7" x2="80.7" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="564.7" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="84.5" y1="555.6" x2="84.5" y2="574.1" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="561.9" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="88.3" y1="545.0" x2="88.3" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="548.4" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="92.1" y1="541.6" x2="92.1" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="547.3" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="95.8" y1="556.0" x2="95.8" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="564.3" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="99.6" y1="568.2" x2="99.6" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="570.2" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="103.4" y1="557.3" x2="103.4" y2="574.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="565.4" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="107.1" y1="542.5" x2="107.1" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="563.6" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="110.9" y1="549.6" x2="110.9" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="562.5" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="114.7" y1="545.6" x2="114.7" y2="607.9" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="548.5" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="118.5" y1="548.8" x2="118.5" y2="591.1" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="551.2" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="122.2" y1="559.8" x2="122.2" y2="576.6" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="560.5" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="126.0" y1="554.3" x2="126.0" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="558.3" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="129.8" y1="549.0" x2="129.8" y2="560.9" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="557.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="133.6" y1="551.4" x2="133.6" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="556.7" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="137.3" y1="534.5" x2="137.3" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="545.7" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="141.1" y1="540.3" x2="141.1" y2="563.4" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="544.0" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="144.9" y1="548.1" x2="144.9" y2="559.4" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="552.2" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="148.6" y1="526.1" x2="148.6" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="531.5" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="152.4" y1="527.2" x2="152.4" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="531.5" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="156.2" y1="540.1" x2="156.2" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="542.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="160.0" y1="540.6" x2="160.0" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="543.5" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="163.7" y1="528.8" x2="163.7" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="544.2" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="167.5" y1="518.3" x2="167.5" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="523.0" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="171.3" y1="495.5" x2="171.3" y2="519.0" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="497.7" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="175.0" y1="485.4" x2="175.0" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="499.7" width="2.34" height="29.8" fill="var(--down)"/>
<line x1="178.8" y1="512.1" x2="178.8" y2="529.8" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="512.7" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="182.6" y1="508.9" x2="182.6" y2="536.4" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="512.7" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="186.4" y1="504.6" x2="186.4" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="507.3" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="190.1" y1="496.2" x2="190.1" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="508.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="193.9" y1="486.2" x2="193.9" y2="508.3" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="490.0" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="197.7" y1="449.8" x2="197.7" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="465.9" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="201.4" y1="451.0" x2="201.4" y2="482.1" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="456.6" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="205.2" y1="432.2" x2="205.2" y2="457.9" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="448.0" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="209.0" y1="438.7" x2="209.0" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="448.9" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="212.8" y1="454.1" x2="212.8" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="454.1" width="2.34" height="24.6" fill="var(--down)"/>
<line x1="216.5" y1="476.7" x2="216.5" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="480.1" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="220.3" y1="443.0" x2="220.3" y2="485.2" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="448.7" width="2.34" height="32.7" fill="var(--up)"/>
<line x1="224.1" y1="426.8" x2="224.1" y2="452.1" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="433.4" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="227.8" y1="412.6" x2="227.8" y2="437.0" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="433.4" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="231.6" y1="417.5" x2="231.6" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="424.7" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="235.4" y1="403.4" x2="235.4" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="424.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="239.2" y1="387.0" x2="239.2" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="401.3" width="2.34" height="28.1" fill="var(--up)"/>
<line x1="242.9" y1="396.2" x2="242.9" y2="419.0" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="400.3" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="246.7" y1="403.4" x2="246.7" y2="427.9" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="410.8" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="250.5" y1="405.3" x2="250.5" y2="430.8" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="419.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="254.3" y1="406.6" x2="254.3" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="418.7" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="258.0" y1="375.7" x2="258.0" y2="420.3" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="380.8" width="2.34" height="39.6" fill="var(--up)"/>
<line x1="261.8" y1="366.6" x2="261.8" y2="389.2" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="371.9" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="265.6" y1="344.3" x2="265.6" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="348.9" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="269.3" y1="313.4" x2="269.3" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="327.2" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="273.1" y1="302.6" x2="273.1" y2="337.6" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="319.4" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="276.9" y1="277.0" x2="276.9" y2="321.5" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="277.7" width="2.34" height="42.0" fill="var(--up)"/>
<line x1="280.7" y1="246.3" x2="280.7" y2="280.1" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="255.0" width="2.34" height="20.8" fill="var(--up)"/>
<line x1="284.4" y1="248.3" x2="284.4" y2="306.3" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="254.9" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="288.2" y1="247.1" x2="288.2" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="253.3" width="2.34" height="29.5" fill="var(--up)"/>
<line x1="292.0" y1="248.2" x2="292.0" y2="286.3" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="253.1" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="295.7" y1="247.2" x2="295.7" y2="290.1" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="268.3" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="299.5" y1="267.1" x2="299.5" y2="299.5" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="276.0" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="303.3" y1="287.5" x2="303.3" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="299.5" width="2.34" height="106.9" fill="var(--down)"/>
<line x1="307.1" y1="360.6" x2="307.1" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="375.2" width="2.34" height="31.2" fill="var(--up)"/>
<line x1="310.8" y1="347.6" x2="310.8" y2="399.5" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="375.2" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="314.6" y1="371.4" x2="314.6" y2="444.6" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="380.5" width="2.34" height="43.9" fill="var(--down)"/>
<line x1="318.4" y1="391.0" x2="318.4" y2="435.5" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="418.2" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="322.1" y1="398.6" x2="322.1" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="411.4" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="325.9" y1="416.6" x2="325.9" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="411.4" width="2.34" height="35.5" fill="var(--down)"/>
<line x1="329.7" y1="444.2" x2="329.7" y2="481.4" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="446.9" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="333.5" y1="446.3" x2="333.5" y2="478.5" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="468.9" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="337.2" y1="478.5" x2="337.2" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="478.5" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="341.0" y1="486.4" x2="341.0" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="498.1" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="344.8" y1="497.2" x2="344.8" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="506.0" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="348.5" y1="485.8" x2="348.5" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="485.9" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="352.3" y1="459.3" x2="352.3" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="461.8" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="356.1" y1="417.8" x2="356.1" y2="472.3" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="428.2" width="2.34" height="33.5" fill="var(--up)"/>
<line x1="359.9" y1="402.5" x2="359.9" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="405.6" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="363.6" y1="390.1" x2="363.6" y2="428.3" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="405.6" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="367.4" y1="387.1" x2="367.4" y2="429.7" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="398.6" width="2.34" height="29.7" fill="var(--up)"/>
<line x1="371.2" y1="395.6" x2="371.2" y2="427.7" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="398.6" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="375.0" y1="406.0" x2="375.0" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="412.8" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="378.7" y1="412.9" x2="378.7" y2="436.1" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="414.6" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="382.5" y1="395.8" x2="382.5" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="403.5" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="386.3" y1="388.4" x2="386.3" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="403.5" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="390.0" y1="379.4" x2="390.0" y2="417.9" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="386.8" width="2.34" height="31.2" fill="var(--up)"/>
<line x1="393.8" y1="366.8" x2="393.8" y2="388.3" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="377.2" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="397.6" y1="370.2" x2="397.6" y2="404.3" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="377.4" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="401.4" y1="372.2" x2="401.4" y2="403.1" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="373.4" width="2.34" height="28.2" fill="var(--up)"/>
<line x1="405.1" y1="371.1" x2="405.1" y2="395.6" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="372.2" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="408.9" y1="385.9" x2="408.9" y2="412.1" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="392.9" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="412.7" y1="388.6" x2="412.7" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="395.1" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="416.4" y1="409.4" x2="416.4" y2="439.2" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="415.8" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="420.2" y1="429.2" x2="420.2" y2="462.6" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="438.0" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="424.0" y1="409.7" x2="424.0" y2="450.4" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="413.8" width="2.34" height="36.6" fill="var(--up)"/>
<line x1="427.8" y1="393.5" x2="427.8" y2="428.9" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="403.6" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="431.5" y1="402.7" x2="431.5" y2="431.1" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="403.6" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="435.3" y1="413.4" x2="435.3" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="425.2" width="2.34" height="35.4" fill="var(--down)"/>
<line x1="439.1" y1="434.0" x2="439.1" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="439.3" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="442.8" y1="435.6" x2="442.8" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="439.2" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="446.6" y1="408.4" x2="446.6" y2="457.8" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="418.4" width="2.34" height="36.8" fill="var(--up)"/>
<line x1="450.4" y1="384.5" x2="450.4" y2="423.6" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="386.5" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="454.2" y1="369.1" x2="454.2" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="375.0" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="457.9" y1="370.2" x2="457.9" y2="400.8" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="375.0" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="461.7" y1="387.6" x2="461.7" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="393.7" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="465.5" y1="376.0" x2="465.5" y2="403.9" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="379.6" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="469.2" y1="379.6" x2="469.2" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="379.6" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="473.0" y1="369.0" x2="473.0" y2="400.7" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="380.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="476.8" y1="353.3" x2="476.8" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="359.7" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="480.6" y1="344.3" x2="480.6" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="359.7" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="484.3" y1="356.7" x2="484.3" y2="382.3" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="359.5" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="488.1" y1="349.9" x2="488.1" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="359.5" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="491.9" y1="349.8" x2="491.9" y2="374.4" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="355.7" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="495.7" y1="351.0" x2="495.7" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="355.7" width="2.34" height="56.9" fill="var(--down)"/>
<line x1="499.4" y1="396.5" x2="499.4" y2="432.8" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="398.5" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="503.2" y1="386.2" x2="503.2" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="398.5" width="2.34" height="30.1" fill="var(--down)"/>
<line x1="507.0" y1="412.2" x2="507.0" y2="441.5" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="428.6" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="510.7" y1="400.1" x2="510.7" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="429.2" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="514.5" y1="389.5" x2="514.5" y2="433.4" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="402.2" width="2.34" height="20.8" fill="var(--up)"/>
<line x1="518.3" y1="397.1" x2="518.3" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="402.2" width="2.34" height="48.0" fill="var(--down)"/>
<line x1="522.1" y1="410.0" x2="522.1" y2="429.1" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="425.6" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="525.8" y1="419.7" x2="525.8" y2="470.6" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="425.2" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="529.6" y1="395.8" x2="529.6" y2="432.6" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="406.2" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="533.4" y1="394.1" x2="533.4" y2="420.5" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="406.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="537.1" y1="362.0" x2="537.1" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="382.1" width="2.34" height="24.4" fill="var(--up)"/>
<line x1="540.9" y1="372.9" x2="540.9" y2="392.9" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="377.9" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="544.7" y1="376.0" x2="544.7" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="376.7" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="548.5" y1="375.7" x2="548.5" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="376.7" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="552.2" y1="373.3" x2="552.2" y2="402.1" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="384.1" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="556.0" y1="375.4" x2="556.0" y2="393.8" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="384.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="559.8" y1="377.3" x2="559.8" y2="390.3" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="384.9" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="563.5" y1="377.2" x2="563.5" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="384.9" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="567.3" y1="382.4" x2="567.3" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="386.8" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="571.1" y1="365.9" x2="571.1" y2="396.2" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="369.7" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="574.9" y1="358.4" x2="574.9" y2="383.1" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="367.7" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="578.6" y1="354.8" x2="578.6" y2="370.5" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="361.1" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="582.4" y1="318.9" x2="582.4" y2="389.7" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="326.5" width="2.34" height="35.2" fill="var(--up)"/>
<line x1="586.2" y1="302.0" x2="586.2" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="326.5" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="589.9" y1="322.5" x2="589.9" y2="341.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="330.3" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="593.7" y1="316.8" x2="593.7" y2="368.6" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="329.5" width="2.34" height="27.2" fill="var(--down)"/>
<line x1="597.5" y1="335.8" x2="597.5" y2="359.2" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="337.9" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="601.3" y1="334.5" x2="601.3" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="337.9" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="605.0" y1="336.3" x2="605.0" y2="357.9" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="343.2" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="608.8" y1="317.0" x2="608.8" y2="356.2" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="323.5" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="612.6" y1="323.5" x2="612.6" y2="356.8" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="323.5" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="616.3" y1="317.8" x2="616.3" y2="345.1" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="323.3" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="620.1" y1="311.1" x2="620.1" y2="329.2" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="315.9" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="623.9" y1="308.6" x2="623.9" y2="337.0" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="315.9" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="627.7" y1="311.8" x2="627.7" y2="336.2" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="325.7" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="631.4" y1="316.7" x2="631.4" y2="348.1" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="330.1" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="635.2" y1="314.4" x2="635.2" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="315.3" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="639.0" y1="314.0" x2="639.0" y2="330.1" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="315.4" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="642.8" y1="318.6" x2="642.8" y2="360.8" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="323.5" width="2.34" height="29.9" fill="var(--down)"/>
<line x1="646.5" y1="326.4" x2="646.5" y2="357.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="345.8" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="650.3" y1="335.4" x2="650.3" y2="380.5" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="345.4" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="654.1" y1="362.6" x2="654.1" y2="405.9" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="363.2" width="2.34" height="30.2" fill="var(--down)"/>
<line x1="657.8" y1="374.6" x2="657.8" y2="402.0" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="378.1" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="661.6" y1="369.0" x2="661.6" y2="394.5" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="377.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="665.4" y1="364.9" x2="665.4" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="376.7" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="669.2" y1="377.3" x2="669.2" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="384.2" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="672.9" y1="374.4" x2="672.9" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="384.2" width="2.34" height="27.9" fill="var(--down)"/>
<line x1="676.7" y1="361.5" x2="676.7" y2="418.6" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="366.4" width="2.34" height="44.4" fill="var(--up)"/>
<line x1="680.5" y1="357.6" x2="680.5" y2="377.3" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="364.0" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="684.2" y1="334.4" x2="684.2" y2="364.0" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="339.2" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="688.0" y1="313.4" x2="688.0" y2="342.7" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="316.8" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="691.8" y1="314.8" x2="691.8" y2="335.6" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="316.8" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="695.6" y1="297.2" x2="695.6" y2="367.1" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="305.4" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="699.3" y1="288.5" x2="699.3" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="305.4" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="703.1" y1="292.2" x2="703.1" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="297.8" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="706.9" y1="292.9" x2="706.9" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="297.8" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="710.6" y1="251.3" x2="710.6" y2="332.0" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="272.9" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="714.4" y1="256.1" x2="714.4" y2="279.7" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="260.7" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="718.2" y1="238.3" x2="718.2" y2="262.4" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="247.5" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="722.0" y1="197.6" x2="722.0" y2="247.5" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="214.6" width="2.34" height="32.9" fill="var(--up)"/>
<line x1="725.7" y1="208.3" x2="725.7" y2="226.7" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="214.6" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="729.5" y1="212.2" x2="729.5" y2="252.7" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="215.3" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="733.3" y1="214.2" x2="733.3" y2="257.1" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="215.3" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="737.0" y1="233.1" x2="737.0" y2="348.5" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="233.1" width="2.34" height="35.2" fill="var(--down)"/>
<line x1="740.8" y1="233.9" x2="740.8" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="233.9" width="2.34" height="35.0" fill="var(--up)"/>
<line x1="744.6" y1="215.9" x2="744.6" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="233.9" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="748.4" y1="231.1" x2="748.4" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="241.3" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="752.1" y1="246.9" x2="752.1" y2="266.4" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="260.9" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="755.9" y1="225.4" x2="755.9" y2="273.3" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="228.6" width="2.34" height="32.3" fill="var(--up)"/>
<line x1="759.7" y1="227.6" x2="759.7" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="230.2" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="763.5" y1="231.0" x2="763.5" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="243.1" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="767.2" y1="217.1" x2="767.2" y2="253.2" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="224.3" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="771.0" y1="216.9" x2="771.0" y2="227.8" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="219.9" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="774.8" y1="209.6" x2="774.8" y2="265.6" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="218.7" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="778.5" y1="197.7" x2="778.5" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="231.8" width="2.34" height="46.1" fill="var(--down)"/>
<line x1="782.3" y1="264.1" x2="782.3" y2="285.7" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="279.1" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="786.1" y1="249.8" x2="786.1" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="257.2" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="789.9" y1="246.8" x2="789.9" y2="316.3" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="257.2" width="2.34" height="47.4" fill="var(--down)"/>
<line x1="793.6" y1="284.3" x2="793.6" y2="353.3" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="303.3" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="797.4" y1="268.2" x2="797.4" y2="330.5" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="304.9" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="801.2" y1="300.8" x2="801.2" y2="346.0" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="304.2" width="2.34" height="40.7" fill="var(--down)"/>
<line x1="804.9" y1="319.7" x2="804.9" y2="350.0" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="323.6" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="808.7" y1="323.6" x2="808.7" y2="361.4" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="323.6" width="2.34" height="27.5" fill="var(--down)"/>
<line x1="812.5" y1="331.7" x2="812.5" y2="363.1" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="343.8" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="816.3" y1="319.2" x2="816.3" y2="359.9" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="337.0" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="820.0" y1="313.6" x2="820.0" y2="360.8" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="338.6" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="823.8" y1="339.0" x2="823.8" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="345.7" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="827.6" y1="328.6" x2="827.6" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="329.4" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="831.3" y1="306.5" x2="831.3" y2="331.8" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="313.9" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="835.1" y1="310.7" x2="835.1" y2="345.2" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="313.3" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="838.9" y1="294.8" x2="838.9" y2="329.9" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="316.5" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="842.7" y1="312.1" x2="842.7" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="313.8" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="846.4" y1="310.5" x2="846.4" y2="333.5" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="316.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="850.2" y1="297.5" x2="850.2" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="316.4" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="854.0" y1="303.3" x2="854.0" y2="322.6" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="317.6" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="857.7" y1="304.2" x2="857.7" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="315.4" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="861.5" y1="307.8" x2="861.5" y2="322.5" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="312.8" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="865.3" y1="302.8" x2="865.3" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="309.6" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="869.1" y1="285.5" x2="869.1" y2="314.7" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="292.2" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="872.8" y1="287.3" x2="872.8" y2="304.7" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="291.5" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="876.6" y1="266.2" x2="876.6" y2="294.7" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="268.4" width="2.34" height="26.4" fill="var(--up)"/>
<line x1="880.4" y1="259.8" x2="880.4" y2="285.9" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="267.2" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="884.2" y1="252.4" x2="884.2" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="256.5" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="887.9" y1="255.5" x2="887.9" y2="279.3" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="257.6" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="891.7" y1="227.1" x2="891.7" y2="271.7" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="236.0" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="895.5" y1="213.0" x2="895.5" y2="246.2" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="237.2" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="899.2" y1="208.8" x2="899.2" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="219.6" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="903.0" y1="207.2" x2="903.0" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="220.7" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="906.8" y1="212.9" x2="906.8" y2="227.2" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="215.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="910.6" y1="206.4" x2="910.6" y2="226.9" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="214.3" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="914.3" y1="203.9" x2="914.3" y2="227.1" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="212.4" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="918.1" y1="200.7" x2="918.1" y2="266.4" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="213.5" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="921.9" y1="243.0" x2="921.9" y2="267.3" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="252.7" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="925.6" y1="228.3" x2="925.6" y2="253.4" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="234.4" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="929.4" y1="207.7" x2="929.4" y2="235.7" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="215.5" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="933.2" y1="206.1" x2="933.2" y2="248.8" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="216.1" width="2.34" height="32.1" fill="var(--down)"/>
<line x1="937.0" y1="240.7" x2="937.0" y2="277.9" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="242.4" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="940.7" y1="213.3" x2="940.7" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="227.1" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="944.5" y1="220.4" x2="944.5" y2="264.2" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="228.1" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="948.3" y1="239.4" x2="948.3" y2="258.6" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="249.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="952.0" y1="245.8" x2="952.0" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="254.1" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="955.8" y1="174.5" x2="955.8" y2="256.6" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="201.3" width="2.34" height="37.0" fill="var(--up)"/>
<line x1="959.6" y1="179.9" x2="959.6" y2="288.2" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="179.9" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="963.4" y1="175.6" x2="963.4" y2="203.8" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="176.9" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="967.1" y1="160.7" x2="967.1" y2="206.5" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="174.3" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="970.9" y1="137.8" x2="970.9" y2="185.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="169.7" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="974.7" y1="166.9" x2="974.7" y2="218.2" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="170.4" width="2.34" height="31.4" fill="var(--down)"/>
<line x1="978.4" y1="185.8" x2="978.4" y2="237.6" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="203.4" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="982.2" y1="199.2" x2="982.2" y2="224.6" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="212.4" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="986.0" y1="196.2" x2="986.0" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="210.3" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="989.8" y1="208.3" x2="989.8" y2="255.0" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="216.0" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="993.5" y1="175.1" x2="993.5" y2="227.3" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="186.6" width="2.34" height="40.7" fill="var(--up)"/>
<line x1="997.3" y1="159.0" x2="997.3" y2="191.7" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="159.6" width="2.34" height="23.4" fill="var(--up)"/>
<line x1="1001.1" y1="163.4" x2="1001.1" y2="190.8" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="166.6" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="1004.9" y1="111.8" x2="1004.9" y2="179.7" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="113.0" width="2.34" height="59.8" fill="var(--up)"/>
<line x1="1008.6" y1="115.5" x2="1008.6" y2="170.3" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="116.9" width="2.34" height="45.7" fill="var(--down)"/>
<line x1="1012.4" y1="133.5" x2="1012.4" y2="178.2" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="150.8" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="1016.2" y1="122.2" x2="1016.2" y2="146.5" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="142.3" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="1019.9" y1="111.3" x2="1019.9" y2="151.5" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="139.2" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="1023.7" y1="76.8" x2="1023.7" y2="185.4" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="144.1" width="2.34" height="41.3" fill="var(--down)"/>
<line x1="1027.5" y1="171.5" x2="1027.5" y2="218.0" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="184.3" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="1031.3" y1="194.8" x2="1031.3" y2="232.9" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="196.8" width="2.34" height="35.6" fill="var(--down)"/>
<line x1="1035.0" y1="215.9" x2="1035.0" y2="280.5" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="232.7" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="1038.8" y1="252.9" x2="1038.8" y2="295.0" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="259.8" width="2.34" height="35.2" fill="var(--down)"/>
<line x1="1042.6" y1="271.4" x2="1042.6" y2="293.7" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="284.0" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="1046.3" y1="282.7" x2="1046.3" y2="326.9" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="283.5" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="1050.1" y1="321.3" x2="1050.1" y2="321.3" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="321.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="60" y1="301.8" x2="1052" y2="301.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="305.3" font-size="11.5" fill="var(--resistance)" font-weight="600">1,400.16원 R1</text>
<text x="1058" y="317.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="198.7" x2="1052" y2="198.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="202.2" font-size="11.5" fill="var(--resistance)" font-weight="600">1,486.12원 R2</text>
<text x="1058" y="214.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="377.5" x2="1052" y2="377.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="371.5" font-size="11.5" fill="var(--support)" font-weight="600">1,337.11원 S1</text>
<text x="1058" y="383.5" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="449.0" x2="1052" y2="449.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="443.0" font-size="11.5" fill="var(--support)" font-weight="600">1,277.48원 S2</text>
<text x="1058" y="455.0" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="525.5" x2="1052" y2="525.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="519.5" font-size="11.5" fill="var(--support)" font-weight="600">1,213.73원 S3</text>
<text x="1058" y="531.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="321.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="313.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 1,383.90원 (2026-08-23)</text>
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

- **상승(원화 약세)**: 위험을 피하려는 심리, 외국인 자금 유출, 무역수지 악화, 한·미 금리차 확대 신호로 흔히 해석한다. 해외 매출 비중이 큰 회사는 원화로 환산한 매출이 늘어나는 효과가 있다.
- **하락(원화 강세)**: 위험선호 심리, 외국인 자금 유입, 무역수지 개선 신호로 흔히 해석한다.
- **왜 다른 통화보다 변동성이 큰가**: 원화는 달러·유로처럼 세계 어디서나 통용되는 기축통화가 아니고, 반도체·자동차 등 몇몇 품목에 수출이 집중돼 있어서 무역수지가 특정 업황에 좌우되기 쉽다. 외국인이 보유한 한국 주식·채권 비중도 높은 편이라, 위험선호가 꺾이면 짧은 기간에 자금이 한꺼번에 빠져나가는(원화 매도) 경향이 있다.
- 한국은행·연준의 통화정책, 무역수지, 위험선호 등 여러 요인이 동시에 작용하기 때문에, 한 가지 원인으로 단정하기 어렵다.

---

## 관련 문서

- [달러인덱스 (DXY)](./dxy.md)
- [코스피](../equities/kospi.md)
- [통화 4종 비교 (지수화)](./comparison.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)
- [표기 규칙 개념 정리](../../concepts/notation.md)

---

## 참고 자료

- [Yahoo Finance — USD/KRW (KRW=X)](https://finance.yahoo.com/quote/KRW=X/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
