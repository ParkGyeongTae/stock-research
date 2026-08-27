# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점 종가 대조**: 2026-08-17 종가는 이 문서 기준 $172.89(Yahoo Finance), 핵심 지표·밸류에이션 / 적정주가가 인용한 stockanalysis.com 기준 $172.86과 $0.03(약 0.02%) 차이로 사실상 일치 — 데이터 제공처 간 반올림·마감가 집계 시점 차이로 판단되며, 수정주가 여부를 다시 확인할 필요는 없는 수준이다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-18 ~ 2026-08-17)

<div class="bwxt-chart">
<style>
.bwxt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .bwxt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .bwxt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.bwxt-chart svg { width:100%; height:auto; display:block; }
.bwxt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.bwxt-chart .title { fill: var(--ink); font-weight:600; }
.bwxt-chart .grid { stroke: var(--grid); stroke-width:1; }
.bwxt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="BWX Technologies(BWXT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">BWX Technologies (BWXT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-18 ~ 2026-08-17 · 마지막 종가 $172.89 (2026-08-17) · 단위 USD</text>
<line x1="60" y1="588.8" x2="1052" y2="588.8" class="grid"/>
<text x="52" y="592.8" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="464.9" x2="1052" y2="464.9" class="grid"/>
<text x="52" y="468.9" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="217.1" x2="1052" y2="217.1" class="grid"/>
<text x="52" y="221.1" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
<line x1="60" y1="93.2" x2="1052" y2="93.2" class="grid"/>
<text x="52" y="97.2" font-size="11" text-anchor="end" fill="var(--muted)">240</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="101.5" y1="626.0" x2="101.5" y2="631.0" class="axis"/>
<text x="101.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="184.5" y1="626.0" x2="184.5" y2="631.0" class="axis"/>
<text x="184.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="275.4" y1="626.0" x2="275.4" y2="631.0" class="axis"/>
<text x="275.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="350.5" y1="626.0" x2="350.5" y2="631.0" class="axis"/>
<text x="350.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="437.4" y1="626.0" x2="437.4" y2="631.0" class="axis"/>
<text x="437.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="516.5" y1="626.0" x2="516.5" y2="631.0" class="axis"/>
<text x="516.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="591.6" y1="626.0" x2="591.6" y2="631.0" class="axis"/>
<text x="591.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="678.5" y1="626.0" x2="678.5" y2="631.0" class="axis"/>
<text x="678.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="761.5" y1="626.0" x2="761.5" y2="631.0" class="axis"/>
<text x="761.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="840.6" y1="626.0" x2="840.6" y2="631.0" class="axis"/>
<text x="840.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="923.6" y1="626.0" x2="923.6" y2="631.0" class="axis"/>
<text x="923.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1010.5" y1="626.0" x2="1010.5" y2="631.0" class="axis"/>
<text x="1010.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="81.9" x2="1052" y2="81.9" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="84.9" font-size="10.5" fill="var(--muted)">$242 52주 최고</text>
<line x1="62.0" y1="498.7" x2="62.0" y2="525.6" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="504.8" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="65.9" y1="529.9" x2="65.9" y2="566.3" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="529.9" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="69.9" y1="555.7" x2="69.9" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="557.2" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="73.8" y1="549.4" x2="73.8" y2="566.4" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="555.7" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="77.8" y1="540.7" x2="77.8" y2="569.9" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="552.0" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="81.7" y1="558.0" x2="81.7" y2="572.2" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="564.9" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="85.7" y1="541.8" x2="85.7" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="548.4" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="89.6" y1="546.5" x2="89.6" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="548.6" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="93.6" y1="547.4" x2="93.6" y2="559.6" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="552.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="97.5" y1="549.3" x2="97.5" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="554.1" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="101.5" y1="584.0" x2="101.5" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="588.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="105.5" y1="577.1" x2="105.5" y2="595.0" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="578.0" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="109.4" y1="563.0" x2="109.4" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="565.3" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="113.4" y1="547.0" x2="113.4" y2="597.7" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="554.8" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="117.3" y1="553.4" x2="117.3" y2="570.4" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="565.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="121.3" y1="564.1" x2="121.3" y2="589.6" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="570.2" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="125.2" y1="550.3" x2="125.2" y2="565.3" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="550.8" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="129.2" y1="515.4" x2="129.2" y2="550.1" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="526.2" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="133.1" y1="517.6" x2="133.1" y2="537.3" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="526.9" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="137.1" y1="496.3" x2="137.1" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="500.2" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="141.0" y1="470.7" x2="141.0" y2="510.1" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="485.7" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="145.0" y1="482.0" x2="145.0" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="489.7" width="2.45" height="47.2" fill="var(--down)"/>
<line x1="148.9" y1="498.0" x2="148.9" y2="539.3" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="501.9" width="2.45" height="31.2" fill="var(--up)"/>
<line x1="152.9" y1="489.3" x2="152.9" y2="514.0" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="499.0" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="156.8" y1="472.8" x2="156.8" y2="512.9" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="476.1" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="160.8" y1="452.5" x2="160.8" y2="483.3" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="477.2" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="164.7" y1="466.4" x2="164.7" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="473.3" width="2.45" height="22.5" fill="var(--down)"/>
<line x1="168.7" y1="479.5" x2="168.7" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="488.4" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="172.6" y1="458.8" x2="172.6" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="461.1" width="2.45" height="18.3" fill="var(--up)"/>
<line x1="176.6" y1="434.0" x2="176.6" y2="458.5" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="443.5" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="180.5" y1="431.5" x2="180.5" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="437.8" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="184.5" y1="412.9" x2="184.5" y2="451.9" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="420.4" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="188.4" y1="402.9" x2="188.4" y2="445.0" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="413.9" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="192.4" y1="410.3" x2="192.4" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="423.8" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="196.4" y1="382.8" x2="196.4" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="394.4" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="200.3" y1="368.3" x2="200.3" y2="405.6" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="390.4" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="204.3" y1="356.4" x2="204.3" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="359.5" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="208.2" y1="342.7" x2="208.2" y2="377.1" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="356.1" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="212.2" y1="351.9" x2="212.2" y2="403.6" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="368.3" width="2.45" height="34.2" fill="var(--down)"/>
<line x1="216.1" y1="342.4" x2="216.1" y2="384.1" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="357.3" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="220.1" y1="310.3" x2="220.1" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="325.8" width="2.45" height="46.0" fill="var(--up)"/>
<line x1="224.0" y1="254.3" x2="224.0" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="258.0" width="2.45" height="59.4" fill="var(--down)"/>
<line x1="228.0" y1="249.8" x2="228.0" y2="310.0" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="285.2" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="231.9" y1="281.6" x2="231.9" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="303.8" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="235.9" y1="286.6" x2="235.9" y2="323.3" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="293.2" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="239.8" y1="293.2" x2="239.8" y2="340.9" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="303.8" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="243.8" y1="301.2" x2="243.8" y2="399.9" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="310.0" width="2.45" height="85.7" fill="var(--down)"/>
<line x1="247.7" y1="338.3" x2="247.7" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="341.5" width="2.45" height="55.3" fill="var(--up)"/>
<line x1="251.7" y1="318.8" x2="251.7" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="320.7" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="255.6" y1="296.8" x2="255.6" y2="326.3" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="309.5" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="259.6" y1="254.3" x2="259.6" y2="300.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="258.6" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="263.5" y1="244.2" x2="263.5" y2="306.9" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="256.2" width="2.45" height="37.7" fill="var(--up)"/>
<line x1="267.5" y1="226.4" x2="267.5" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="255.5" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="271.4" y1="237.3" x2="271.4" y2="269.9" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="248.1" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="275.4" y1="236.1" x2="275.4" y2="270.5" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="242.7" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="279.3" y1="297.6" x2="279.3" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="314.4" width="2.45" height="24.2" fill="var(--down)"/>
<line x1="283.3" y1="328.6" x2="283.3" y2="372.2" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="352.6" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="287.3" y1="353.4" x2="287.3" y2="400.5" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="353.6" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="291.2" y1="380.5" x2="291.2" y2="433.9" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="381.0" width="2.45" height="26.0" fill="var(--up)"/>
<line x1="295.2" y1="346.1" x2="295.2" y2="382.5" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="348.5" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="299.1" y1="350.3" x2="299.1" y2="393.6" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="355.0" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="303.1" y1="341.0" x2="303.1" y2="375.6" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="361.0" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="307.0" y1="368.9" x2="307.0" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="369.1" width="2.45" height="108.9" fill="var(--down)"/>
<line x1="311.0" y1="447.1" x2="311.0" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="475.4" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="314.9" y1="458.7" x2="314.9" y2="506.6" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="468.4" width="2.45" height="20.2" fill="var(--down)"/>
<line x1="318.9" y1="478.7" x2="318.9" y2="516.1" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="490.3" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="322.8" y1="457.4" x2="322.8" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="466.1" width="2.45" height="22.5" fill="var(--up)"/>
<line x1="326.8" y1="421.3" x2="326.8" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="433.9" width="2.45" height="60.2" fill="var(--down)"/>
<line x1="330.7" y1="497.6" x2="330.7" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="514.4" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="334.7" y1="495.1" x2="334.7" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="498.2" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="338.6" y1="488.1" x2="338.6" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="494.3" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="342.6" y1="466.2" x2="342.6" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="476.2" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="346.5" y1="464.9" x2="346.5" y2="480.0" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="465.5" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="350.5" y1="483.7" x2="350.5" y2="500.4" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="486.5" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="354.4" y1="469.9" x2="354.4" y2="492.1" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="475.7" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="358.4" y1="491.8" x2="358.4" y2="516.4" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="491.8" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="362.3" y1="449.4" x2="362.3" y2="501.7" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="475.3" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="366.3" y1="455.7" x2="366.3" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="458.7" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="370.2" y1="462.6" x2="370.2" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="471.3" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="374.2" y1="464.9" x2="374.2" y2="482.8" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="477.5" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="378.2" y1="452.5" x2="378.2" y2="502.1" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="467.1" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="382.1" y1="440.5" x2="382.1" y2="512.9" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="444.0" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="386.1" y1="441.7" x2="386.1" y2="501.3" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="442.7" width="2.45" height="53.0" fill="var(--down)"/>
<line x1="390.0" y1="484.1" x2="390.0" y2="526.6" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="486.2" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="394.0" y1="496.6" x2="394.0" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="507.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="397.9" y1="502.1" x2="397.9" y2="545.3" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="507.0" width="2.45" height="31.5" fill="var(--down)"/>
<line x1="401.9" y1="503.9" x2="401.9" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="509.6" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="405.8" y1="484.2" x2="405.8" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="487.0" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="409.8" y1="464.9" x2="409.8" y2="479.2" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="465.8" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="413.7" y1="458.7" x2="413.7" y2="483.3" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="477.9" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="417.7" y1="476.1" x2="417.7" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="476.1" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="421.6" y1="479.8" x2="421.6" y2="497.1" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="481.6" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="425.6" y1="479.7" x2="425.6" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="492.9" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="429.5" y1="486.4" x2="429.5" y2="502.3" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="486.5" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="433.5" y1="495.5" x2="433.5" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="495.8" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="437.4" y1="452.3" x2="437.4" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="453.5" width="2.45" height="45.4" fill="var(--up)"/>
<line x1="441.4" y1="403.6" x2="441.4" y2="427.7" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="409.0" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="445.3" y1="368.9" x2="445.3" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="370.1" width="2.45" height="38.9" fill="var(--up)"/>
<line x1="449.3" y1="355.1" x2="449.3" y2="390.1" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="371.6" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="453.2" y1="340.2" x2="453.2" y2="404.9" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="355.0" width="2.45" height="28.1" fill="var(--down)"/>
<line x1="457.2" y1="322.4" x2="457.2" y2="366.0" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="332.0" width="2.45" height="31.5" fill="var(--up)"/>
<line x1="461.1" y1="295.1" x2="461.1" y2="331.7" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="300.0" width="2.45" height="31.7" fill="var(--up)"/>
<line x1="465.1" y1="269.1" x2="465.1" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="275.7" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="469.1" y1="285.2" x2="469.1" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="287.8" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="473.0" y1="224.0" x2="473.0" y2="294.5" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="258.9" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="477.0" y1="213.6" x2="477.0" y2="258.6" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="230.2" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="480.9" y1="241.9" x2="480.9" y2="314.3" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="266.0" width="2.45" height="37.4" fill="var(--down)"/>
<line x1="484.9" y1="277.4" x2="484.9" y2="322.8" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="282.0" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="488.8" y1="268.0" x2="488.8" y2="311.0" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="271.2" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="492.8" y1="291.7" x2="492.8" y2="325.5" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="293.0" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="496.7" y1="271.2" x2="496.7" y2="313.1" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="299.4" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="500.7" y1="253.5" x2="500.7" y2="321.3" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="264.2" width="2.45" height="40.0" fill="var(--up)"/>
<line x1="504.6" y1="238.6" x2="504.6" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="240.0" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="508.6" y1="218.0" x2="508.6" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="233.3" width="2.45" height="44.7" fill="var(--down)"/>
<line x1="512.5" y1="266.7" x2="512.5" y2="325.1" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="300.7" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="516.5" y1="299.2" x2="516.5" y2="334.2" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="303.6" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="520.4" y1="260.5" x2="520.4" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="273.6" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="524.4" y1="272.8" x2="524.4" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="272.8" width="2.45" height="129.5" fill="var(--down)"/>
<line x1="528.3" y1="388.8" x2="528.3" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="418.9" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="532.3" y1="348.5" x2="532.3" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="358.4" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="536.2" y1="301.0" x2="536.2" y2="362.6" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="322.4" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="540.2" y1="319.3" x2="540.2" y2="352.0" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="319.3" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="544.1" y1="312.4" x2="544.1" y2="377.4" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="322.4" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="548.1" y1="304.4" x2="548.1" y2="362.1" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="322.4" width="2.45" height="37.9" fill="var(--down)"/>
<line x1="552.0" y1="323.7" x2="552.0" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="338.5" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="556.0" y1="321.9" x2="556.0" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="334.2" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="560.0" y1="303.8" x2="560.0" y2="341.0" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="320.8" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="563.9" y1="283.9" x2="563.9" y2="333.8" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="284.8" width="2.45" height="45.8" fill="var(--up)"/>
<line x1="567.9" y1="262.3" x2="567.9" y2="323.7" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="293.0" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="571.8" y1="303.8" x2="571.8" y2="355.7" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="316.2" width="2.45" height="34.8" fill="var(--down)"/>
<line x1="575.8" y1="243.0" x2="575.8" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="269.9" width="2.45" height="44.9" fill="var(--down)"/>
<line x1="579.7" y1="272.7" x2="579.7" y2="316.3" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="289.8" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="583.7" y1="273.3" x2="583.7" y2="334.2" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="282.2" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="587.6" y1="294.0" x2="587.6" y2="324.8" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="304.0" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="591.6" y1="225.5" x2="591.6" y2="311.9" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="239.0" width="2.45" height="72.7" fill="var(--up)"/>
<line x1="595.5" y1="262.1" x2="595.5" y2="342.3" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="273.2" width="2.45" height="31.7" fill="var(--down)"/>
<line x1="599.5" y1="285.7" x2="599.5" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="305.4" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="603.4" y1="314.9" x2="603.4" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="325.5" width="2.45" height="43.4" fill="var(--down)"/>
<line x1="607.4" y1="348.7" x2="607.4" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="370.6" width="2.45" height="32.4" fill="var(--up)"/>
<line x1="611.3" y1="331.6" x2="611.3" y2="382.9" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="338.6" width="2.45" height="39.6" fill="var(--up)"/>
<line x1="615.3" y1="325.9" x2="615.3" y2="367.8" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="341.2" width="2.45" height="25.2" fill="var(--down)"/>
<line x1="619.2" y1="346.3" x2="619.2" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="365.9" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="623.2" y1="344.1" x2="623.2" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="354.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="627.1" y1="337.2" x2="627.1" y2="410.1" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="341.0" width="2.45" height="36.4" fill="var(--down)"/>
<line x1="631.1" y1="304.1" x2="631.1" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="312.1" width="2.45" height="45.6" fill="var(--up)"/>
<line x1="635.0" y1="290.6" x2="635.0" y2="322.8" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="294.7" width="2.45" height="24.2" fill="var(--up)"/>
<line x1="639.0" y1="263.4" x2="639.0" y2="300.8" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="285.4" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="642.9" y1="261.3" x2="642.9" y2="337.6" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="278.3" width="2.45" height="50.1" fill="var(--up)"/>
<line x1="646.9" y1="269.7" x2="646.9" y2="358.2" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="281.1" width="2.45" height="61.4" fill="var(--down)"/>
<line x1="650.9" y1="277.7" x2="650.9" y2="342.1" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="311.0" width="2.45" height="31.2" fill="var(--up)"/>
<line x1="654.8" y1="289.5" x2="654.8" y2="327.1" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="311.5" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="658.8" y1="202.9" x2="658.8" y2="280.5" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="203.9" width="2.45" height="66.8" fill="var(--up)"/>
<line x1="662.7" y1="218.3" x2="662.7" y2="313.1" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="231.2" width="2.45" height="78.3" fill="var(--down)"/>
<line x1="666.7" y1="291.6" x2="666.7" y2="328.6" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="323.7" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="670.6" y1="313.9" x2="670.6" y2="409.2" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="315.0" width="2.45" height="78.1" fill="var(--down)"/>
<line x1="674.6" y1="305.4" x2="674.6" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="313.2" width="2.45" height="58.2" fill="var(--up)"/>
<line x1="678.5" y1="241.4" x2="678.5" y2="300.2" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="261.6" width="2.45" height="38.5" fill="var(--up)"/>
<line x1="682.5" y1="224.2" x2="682.5" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="248.2" width="2.45" height="49.4" fill="var(--up)"/>
<line x1="686.4" y1="224.7" x2="686.4" y2="251.8" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="234.9" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="690.4" y1="228.9" x2="690.4" y2="268.5" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="243.0" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="694.3" y1="135.5" x2="694.3" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="144.1" width="2.45" height="47.6" fill="var(--up)"/>
<line x1="698.3" y1="106.2" x2="698.3" y2="153.6" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="146.5" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="702.2" y1="132.3" x2="702.2" y2="164.6" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="152.8" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="706.2" y1="128.7" x2="706.2" y2="167.5" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="137.6" width="2.45" height="23.7" fill="var(--up)"/>
<line x1="710.1" y1="95.4" x2="710.1" y2="133.3" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="103.9" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="714.1" y1="90.6" x2="714.1" y2="122.1" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="103.0" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="718.0" y1="81.9" x2="718.0" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="93.2" width="2.45" height="57.0" fill="var(--down)"/>
<line x1="722.0" y1="104.1" x2="722.0" y2="140.4" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="119.3" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="725.9" y1="115.7" x2="725.9" y2="176.9" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="124.2" width="2.45" height="41.9" fill="var(--down)"/>
<line x1="729.9" y1="155.8" x2="729.9" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="161.3" width="2.45" height="76.5" fill="var(--down)"/>
<line x1="733.8" y1="187.0" x2="733.8" y2="261.3" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="211.9" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="737.8" y1="177.1" x2="737.8" y2="229.5" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="182.9" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="741.8" y1="168.9" x2="741.8" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="179.9" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="745.7" y1="192.3" x2="745.7" y2="235.5" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="198.3" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="749.7" y1="210.2" x2="749.7" y2="266.7" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="227.2" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="753.6" y1="240.4" x2="753.6" y2="306.0" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="240.5" width="2.45" height="50.4" fill="var(--down)"/>
<line x1="757.6" y1="235.0" x2="757.6" y2="288.3" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="239.5" width="2.45" height="40.8" fill="var(--up)"/>
<line x1="761.5" y1="227.9" x2="761.5" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="235.7" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="765.5" y1="210.8" x2="765.5" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="234.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="769.4" y1="173.0" x2="769.4" y2="322.1" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="230.9" width="2.45" height="72.0" fill="var(--down)"/>
<line x1="773.4" y1="243.2" x2="773.4" y2="304.1" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="246.8" width="2.45" height="41.8" fill="var(--up)"/>
<line x1="777.3" y1="240.4" x2="777.3" y2="318.9" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="241.8" width="2.45" height="37.9" fill="var(--down)"/>
<line x1="781.3" y1="257.6" x2="781.3" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="262.1" width="2.45" height="45.8" fill="var(--down)"/>
<line x1="785.2" y1="266.0" x2="785.2" y2="345.8" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="274.1" width="2.45" height="56.7" fill="var(--up)"/>
<line x1="789.2" y1="292.9" x2="789.2" y2="333.9" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="296.8" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="793.1" y1="281.1" x2="793.1" y2="333.9" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="298.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="797.1" y1="269.3" x2="797.1" y2="309.8" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="273.2" width="2.45" height="23.4" fill="var(--up)"/>
<line x1="801.0" y1="285.2" x2="801.0" y2="327.1" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="290.1" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="805.0" y1="302.8" x2="805.0" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="302.9" width="2.45" height="26.1" fill="var(--down)"/>
<line x1="808.9" y1="333.2" x2="808.9" y2="384.4" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="347.6" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="812.9" y1="315.0" x2="812.9" y2="350.3" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="324.5" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="816.8" y1="317.0" x2="816.8" y2="353.4" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="325.4" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="820.8" y1="302.5" x2="820.8" y2="330.2" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="312.8" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="824.7" y1="286.3" x2="824.7" y2="327.1" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="290.0" width="2.45" height="23.9" fill="var(--down)"/>
<line x1="828.7" y1="313.1" x2="828.7" y2="353.4" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="314.5" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="832.7" y1="338.5" x2="832.7" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="345.5" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="836.6" y1="341.4" x2="836.6" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="342.7" width="2.45" height="23.9" fill="var(--down)"/>
<line x1="840.6" y1="393.4" x2="840.6" y2="436.6" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="403.0" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="844.5" y1="412.7" x2="844.5" y2="444.5" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="418.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="848.5" y1="418.6" x2="848.5" y2="449.4" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="428.0" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="852.4" y1="398.2" x2="852.4" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="398.2" width="2.45" height="43.4" fill="var(--up)"/>
<line x1="856.4" y1="401.6" x2="856.4" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="410.6" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="860.3" y1="407.2" x2="860.3" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="407.2" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="864.3" y1="381.3" x2="864.3" y2="468.3" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="409.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="868.2" y1="404.3" x2="868.2" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="418.4" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="872.2" y1="372.5" x2="872.2" y2="447.3" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="374.0" width="2.45" height="69.9" fill="var(--up)"/>
<line x1="876.1" y1="349.6" x2="876.1" y2="384.9" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="362.7" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="880.1" y1="346.9" x2="880.1" y2="380.9" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="350.3" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="884.0" y1="340.9" x2="884.0" y2="373.6" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="360.0" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="888.0" y1="307.3" x2="888.0" y2="364.2" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="322.0" width="2.45" height="37.6" fill="var(--up)"/>
<line x1="891.9" y1="273.3" x2="891.9" y2="323.8" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="295.9" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="895.9" y1="251.1" x2="895.9" y2="294.2" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="279.0" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="899.8" y1="245.7" x2="899.8" y2="316.2" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="279.7" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="903.8" y1="271.5" x2="903.8" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="280.9" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="907.7" y1="272.7" x2="907.7" y2="322.4" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="294.6" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="911.7" y1="327.9" x2="911.7" y2="372.2" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="341.0" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="915.6" y1="345.3" x2="915.6" y2="413.8" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="357.5" width="2.45" height="50.1" fill="var(--down)"/>
<line x1="919.6" y1="372.3" x2="919.6" y2="404.6" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="374.1" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="923.6" y1="372.0" x2="923.6" y2="395.8" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="380.4" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="927.5" y1="354.0" x2="927.5" y2="422.4" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="380.0" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="931.5" y1="353.5" x2="931.5" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="360.3" width="2.45" height="32.9" fill="var(--up)"/>
<line x1="935.4" y1="370.0" x2="935.4" y2="435.8" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="377.1" width="2.45" height="50.1" fill="var(--down)"/>
<line x1="939.4" y1="422.0" x2="939.4" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="439.4" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="943.3" y1="407.7" x2="943.3" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="421.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="947.3" y1="411.2" x2="947.3" y2="438.8" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="422.7" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="951.2" y1="436.7" x2="951.2" y2="489.5" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="441.6" width="2.45" height="41.0" fill="var(--down)"/>
<line x1="955.2" y1="447.9" x2="955.2" y2="474.3" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="455.1" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="959.1" y1="443.5" x2="959.1" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="455.0" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="963.1" y1="489.8" x2="963.1" y2="525.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="498.9" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="967.0" y1="496.7" x2="967.0" y2="541.3" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="519.6" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="971.0" y1="496.7" x2="971.0" y2="530.3" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="507.5" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="974.9" y1="502.1" x2="974.9" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="507.7" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="978.9" y1="470.2" x2="978.9" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="494.8" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="982.8" y1="461.8" x2="982.8" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="485.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="986.8" y1="475.2" x2="986.8" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="483.1" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="990.7" y1="455.4" x2="990.7" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="474.2" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="994.7" y1="502.6" x2="994.7" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="502.6" width="2.45" height="26.3" fill="var(--down)"/>
<line x1="998.6" y1="539.3" x2="998.6" y2="606.8" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="539.3" width="2.45" height="65.4" fill="var(--down)"/>
<line x1="1002.6" y1="549.1" x2="1002.6" y2="590.3" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="554.2" width="2.45" height="26.1" fill="var(--up)"/>
<line x1="1006.5" y1="524.0" x2="1006.5" y2="559.6" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="534.9" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="1010.5" y1="496.9" x2="1010.5" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="503.4" width="2.45" height="38.0" fill="var(--up)"/>
<line x1="1014.5" y1="474.2" x2="1014.5" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="505.2" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="1018.4" y1="505.6" x2="1018.4" y2="537.8" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="514.5" width="2.45" height="23.0" fill="var(--down)"/>
<line x1="1022.4" y1="511.1" x2="1022.4" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="539.3" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="1026.3" y1="518.6" x2="1026.3" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="527.5" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="1030.3" y1="514.5" x2="1030.3" y2="534.2" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="520.9" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="1034.2" y1="507.5" x2="1034.2" y2="533.6" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="522.1" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="1038.2" y1="499.1" x2="1038.2" y2="537.0" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="505.2" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="1042.1" y1="503.9" x2="1042.1" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="511.6" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="1046.1" y1="505.2" x2="1046.1" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="506.9" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="1050.0" y1="498.4" x2="1050.0" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="509.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="60" y1="457.2" x2="1052" y2="457.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="460.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$181 R1</text>
<text x="1058" y="472.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="226.0" x2="1052" y2="226.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="229.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$219 R2</text>
<text x="1058" y="241.5" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="552.9" x2="1052" y2="552.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="546.9" font-size="11.5" fill="var(--support)" font-weight="600">$166 S1</text>
<text x="1058" y="558.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="605.8" x2="1052" y2="605.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="599.8" font-size="11.5" fill="var(--support)" font-weight="600">$157 S2</text>
<text x="1058" y="611.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="509.0" r="3" fill="var(--ink)"/>
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

## 2. 지지선 / 저항선 요약

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $219 | 7 | 2026년 상반기 랠리~조정 국면에서 반복적으로 형성된 저항대. 52주 최고($241.82)보다는 낮은 구간 |
| R1 | $181 | 4 | 현재가에 가장 가까운 저항대. 최근 수개월간 반등이 여러 차례 막힌 레벨 |
| **현재가** | **$172.89** (2026-08-17 종가) | — | R1과 S1 사이 |
| S1 | $166 | 4 | 현재가에 가장 근접한 지지. 최근 조정 국면에서 여러 차례 방어된 레벨 |
| S2 | $157 | 2 | 52주 최저($157.10)와 거의 일치하는 구간 |
| 참고선 | $242 | — | 52주 최고(정확히는 $241.82) — 이후 밸류에이션 부담·모멘텀 둔화로 조정에 들어가 현재는 이 레벨과 단절된 국면(3. 관측된 특이 구간 — 2026년 상반기 고점 이후 조정·투자 판단 3. 리스크 (약점 / Bear Case) 리스크1 참고), 근시일 저항으로 보지 않음 |

> 레벨 개수는 스크립트 기본값(위/아래 각 3개)보다 적게 나왔다(R 2개·S 2개) — 유효 클러스터(터치 2회 이상)가 그만큼만 존재했기 때문이며 억지로 채우지 않았다.

---

## 3. 관측된 특이 구간 — 2026년 상반기 고점 이후 조정

- 2026년 상반기 중 52주 최고 $241.82를 기록한 뒤, 밸류에이션 부담과 단기 모멘텀 둔화로 최근 90일 기준 약 −27%의 조정을 거쳐 현재 $172.89 수준까지 되돌렸다(관련 코멘터리는 [최근 뉴스 / 이슈](./08_news.md) 2026-08-03 Q2 실적·가이던스 상향 항목 참고 — 실적·가이던스 자체는 견조했음에도 밸류에이션 재평가가 함께 진행된 것으로 보인다).
- 이 조정은 특정 하루의 갭이 아니라 여러 주에 걸친 점진적 되돌림이라, 단일 이벤트(실적 발표 갭 등)로 특정하기 어렵다 — 그래서 위 표는 52주 최고를 "참고선"으로만 표시했고, 전일 대비 급락 폭·거래량 급증 같은 단일 갭 이벤트 지표는 이 구간에 해당하지 않는다.
- 이 되돌림 이후 거래 레짐은 R2($219)~S1($166) 박스권에 가깝게 재형성된 것으로 보이며, 52주 최고 부근 레벨은 현재로선 근시일 저항으로 작동하지 않는 것으로 판단해 2. 지지선 / 저항선 요약에서 참고선으로 분리했다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-18~2026-08-17. 수집 시점: 2026-08-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py BWXT --name "BWX Technologies" --ref-line 241.82:"52주 최고" --close-on 2026-08-17`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 3. 관측된 특이 구간 — 2026년 상반기 고점 이후 조정에서 다룬 조정 구간은 점진적 되돌림이라 이 모델(스윙 고점/저점 빈도)이 포착하는 정보에 한계가 있다 — 왜 조정이 일어났는지(밸류에이션 재평가 등)는 이 기술적 모델로는 설명되지 않는다.
    - 최근 1년(2025-08~2026-08) 안에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다(원주가 그대로 사용, 소급조정 불필요).

---

*작성일: 2026-08-18 (최종 수정일: 2026-08-23)*
