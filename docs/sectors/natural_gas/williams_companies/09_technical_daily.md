# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-17 종가 $71.81은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치**한다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-18 ~ 2026-09-17)

<style>
.wmb-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .wmb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.wmb-chart svg { width:100%; height:auto; display:block; }
.wmb-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.wmb-chart .title { fill: var(--ink); font-weight:600; }
.wmb-chart .grid { stroke: var(--grid); stroke-width:1; }
.wmb-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="wmb-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Williams Companies(WMB) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Williams Companies (WMB) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-18 ~ 2026-09-17 · 마지막 종가 $71.81 (2026-09-17) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">55</text>
<line x1="60" y1="516.4" x2="1052" y2="516.4" class="grid"/>
<text x="52" y="520.4" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="406.8" x2="1052" y2="406.8" class="grid"/>
<text x="52" y="410.8" font-size="11" text-anchor="end" fill="var(--muted)">65</text>
<line x1="60" y1="297.2" x2="1052" y2="297.2" class="grid"/>
<text x="52" y="301.2" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="187.5" x2="1052" y2="187.5" class="grid"/>
<text x="52" y="191.5" font-size="11" text-anchor="end" fill="var(--muted)">75</text>
<line x1="60" y1="77.9" x2="1052" y2="77.9" class="grid"/>
<text x="52" y="81.9" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="97.5" y1="626.0" x2="97.5" y2="631.0" class="axis"/>
<text x="97.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="188.4" y1="626.0" x2="188.4" y2="631.0" class="axis"/>
<text x="188.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="263.5" y1="626.0" x2="263.5" y2="631.0" class="axis"/>
<text x="263.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="350.5" y1="626.0" x2="350.5" y2="631.0" class="axis"/>
<text x="350.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="429.5" y1="626.0" x2="429.5" y2="631.0" class="axis"/>
<text x="429.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="504.6" y1="626.0" x2="504.6" y2="631.0" class="axis"/>
<text x="504.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="591.6" y1="626.0" x2="591.6" y2="631.0" class="axis"/>
<text x="591.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="674.6" y1="626.0" x2="674.6" y2="631.0" class="axis"/>
<text x="674.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="753.6" y1="626.0" x2="753.6" y2="631.0" class="axis"/>
<text x="753.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="836.6" y1="626.0" x2="836.6" y2="631.0" class="axis"/>
<text x="836.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="923.6" y1="626.0" x2="923.6" y2="631.0" class="axis"/>
<text x="923.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1006.5" y1="626.0" x2="1006.5" y2="631.0" class="axis"/>
<text x="1006.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="498.6" x2="62.0" y2="534.4" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="508.1" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="65.9" y1="488.3" x2="65.9" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="491.4" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="69.9" y1="501.7" x2="69.9" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="512.9" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="73.8" y1="475.4" x2="73.8" y2="512.7" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="485.9" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="77.8" y1="441.4" x2="77.8" y2="475.8" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="453.7" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="81.7" y1="441.2" x2="81.7" y2="468.6" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="443.8" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="85.7" y1="418.2" x2="85.7" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="428.5" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="89.6" y1="427.6" x2="89.6" y2="449.5" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="429.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="93.6" y1="429.6" x2="93.6" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="441.4" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="97.5" y1="431.3" x2="97.5" y2="456.3" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="435.5" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="101.5" y1="394.7" x2="101.5" y2="444.7" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="423.0" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="105.5" y1="406.8" x2="105.5" y2="434.0" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="418.2" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="109.4" y1="403.3" x2="109.4" y2="438.1" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="411.4" width="2.45" height="26.5" fill="var(--down)"/>
<line x1="113.4" y1="429.3" x2="113.4" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="429.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="117.3" y1="428.0" x2="117.3" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="431.1" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="121.3" y1="414.4" x2="121.3" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="425.2" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="125.2" y1="416.4" x2="125.2" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="448.0" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="129.2" y1="444.3" x2="129.2" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="456.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="133.1" y1="455.2" x2="133.1" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="464.6" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="137.1" y1="422.3" x2="137.1" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="433.5" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="141.0" y1="426.3" x2="141.0" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="431.3" width="2.45" height="29.6" fill="var(--down)"/>
<line x1="145.0" y1="458.5" x2="145.0" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="462.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="148.9" y1="441.0" x2="148.9" y2="462.7" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="449.3" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="152.9" y1="443.8" x2="152.9" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="446.2" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="156.8" y1="457.0" x2="156.8" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="458.3" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="160.8" y1="476.0" x2="160.8" y2="542.3" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="479.8" width="2.45" height="60.1" fill="var(--down)"/>
<line x1="164.7" y1="527.6" x2="164.7" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="530.6" width="2.45" height="41.0" fill="var(--down)"/>
<line x1="168.7" y1="554.8" x2="168.7" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="567.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="172.6" y1="562.4" x2="172.6" y2="583.2" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="569.2" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="176.6" y1="559.4" x2="176.6" y2="584.6" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="569.0" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="180.5" y1="555.2" x2="180.5" y2="592.5" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="568.6" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="184.5" y1="557.8" x2="184.5" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="563.1" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="188.4" y1="534.4" x2="188.4" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="537.7" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="192.4" y1="543.1" x2="192.4" y2="599.9" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="582.2" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="196.4" y1="551.7" x2="196.4" y2="598.4" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="570.3" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="200.3" y1="551.7" x2="200.3" y2="571.2" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="561.5" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="204.3" y1="521.4" x2="204.3" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="525.6" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="208.2" y1="500.6" x2="208.2" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="503.2" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="212.2" y1="491.2" x2="212.2" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="503.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="216.1" y1="487.0" x2="216.1" y2="514.6" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="504.8" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="220.1" y1="494.0" x2="220.1" y2="535.9" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="501.7" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="224.0" y1="492.5" x2="224.0" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="494.7" width="2.45" height="40.6" fill="var(--up)"/>
<line x1="228.0" y1="494.9" x2="228.0" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="498.0" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="231.9" y1="509.4" x2="231.9" y2="535.5" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="520.1" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="235.9" y1="539.2" x2="235.9" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="540.7" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="239.8" y1="501.0" x2="239.8" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="530.9" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="243.8" y1="518.8" x2="243.8" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="524.9" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="247.7" y1="518.1" x2="247.7" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="524.5" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="251.7" y1="527.3" x2="251.7" y2="547.1" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="530.2" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="255.6" y1="501.7" x2="255.6" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="511.6" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="259.6" y1="491.8" x2="259.6" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="496.0" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="263.5" y1="482.8" x2="263.5" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="484.8" width="2.45" height="16.0" fill="var(--up)"/>
<line x1="267.5" y1="480.9" x2="267.5" y2="512.4" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="482.2" width="2.45" height="29.6" fill="var(--down)"/>
<line x1="271.4" y1="468.4" x2="271.4" y2="508.3" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="482.4" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="275.4" y1="432.0" x2="275.4" y2="490.5" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="436.1" width="2.45" height="46.3" fill="var(--up)"/>
<line x1="279.3" y1="431.3" x2="279.3" y2="455.4" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="436.1" width="2.45" height="18.6" fill="var(--down)"/>
<line x1="283.3" y1="458.9" x2="283.3" y2="481.7" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="461.1" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="287.3" y1="461.6" x2="287.3" y2="485.9" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="471.4" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="291.2" y1="477.6" x2="291.2" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="480.9" width="2.45" height="24.6" fill="var(--down)"/>
<line x1="295.2" y1="490.7" x2="295.2" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="496.2" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="299.1" y1="498.4" x2="299.1" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="505.4" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="303.1" y1="523.2" x2="303.1" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="524.1" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="307.0" y1="530.4" x2="307.0" y2="554.3" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="534.4" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="311.0" y1="535.5" x2="311.0" y2="558.3" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="541.8" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="314.9" y1="517.7" x2="314.9" y2="546.9" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="536.1" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="318.9" y1="536.6" x2="318.9" y2="555.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="545.8" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="322.8" y1="537.2" x2="322.8" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="540.1" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="326.8" y1="521.0" x2="326.8" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="521.9" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="330.7" y1="515.7" x2="330.7" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="522.3" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="334.7" y1="521.0" x2="334.7" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="525.4" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="338.6" y1="516.6" x2="338.6" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="520.8" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="342.6" y1="508.3" x2="342.6" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="512.9" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="346.5" y1="511.8" x2="346.5" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="511.8" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="350.5" y1="491.0" x2="350.5" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="497.8" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="354.4" y1="483.5" x2="354.4" y2="537.7" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="485.7" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="358.4" y1="498.4" x2="358.4" y2="549.5" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="504.8" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="362.3" y1="498.6" x2="362.3" y2="524.9" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="507.8" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="366.3" y1="483.3" x2="366.3" y2="510.9" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="491.2" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="370.2" y1="480.0" x2="370.2" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="490.3" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="374.2" y1="505.6" x2="374.2" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="512.0" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="378.2" y1="499.5" x2="378.2" y2="523.8" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="505.6" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="382.1" y1="486.4" x2="382.1" y2="510.7" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="500.8" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="386.1" y1="490.5" x2="386.1" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="503.9" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="390.0" y1="475.4" x2="390.0" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="482.4" width="2.45" height="25.9" fill="var(--up)"/>
<line x1="394.0" y1="460.5" x2="394.0" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="469.5" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="397.9" y1="446.7" x2="397.9" y2="468.6" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="446.7" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="401.9" y1="421.2" x2="401.9" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="434.8" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="405.8" y1="403.5" x2="405.8" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="407.6" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="409.8" y1="389.0" x2="409.8" y2="432.4" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="397.3" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="413.7" y1="391.2" x2="413.7" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="396.2" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="417.7" y1="362.7" x2="417.7" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="364.7" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="421.6" y1="335.1" x2="421.6" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="342.5" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="425.6" y1="352.8" x2="425.6" y2="391.6" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="357.2" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="429.5" y1="365.1" x2="429.5" y2="388.6" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="376.3" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="433.5" y1="325.7" x2="433.5" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="330.0" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="437.4" y1="320.2" x2="437.4" y2="394.7" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="321.5" width="2.45" height="53.3" fill="var(--down)"/>
<line x1="441.4" y1="347.6" x2="441.4" y2="394.1" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="353.7" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="445.3" y1="321.9" x2="445.3" y2="385.9" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="349.3" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="449.3" y1="331.1" x2="449.3" y2="364.0" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="344.3" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="453.2" y1="262.5" x2="453.2" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="297.2" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="457.2" y1="262.3" x2="457.2" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="272.6" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="461.1" y1="247.2" x2="461.1" y2="273.0" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="258.4" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="465.1" y1="239.5" x2="465.1" y2="276.8" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="247.2" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="469.1" y1="230.5" x2="469.1" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="232.9" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="473.0" y1="232.0" x2="473.0" y2="257.3" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="238.6" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="477.0" y1="232.0" x2="477.0" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="235.8" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="480.9" y1="231.8" x2="480.9" y2="253.3" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="231.8" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="484.9" y1="212.3" x2="484.9" y2="239.5" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="229.2" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="488.8" y1="217.8" x2="488.8" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="220.4" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="492.8" y1="207.5" x2="492.8" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="210.1" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="496.7" y1="176.8" x2="496.7" y2="216.0" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="192.6" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="500.7" y1="174.6" x2="500.7" y2="202.0" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="184.7" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="504.6" y1="146.5" x2="504.6" y2="193.0" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="159.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="508.6" y1="156.0" x2="508.6" y2="186.4" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="162.5" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="512.5" y1="167.4" x2="512.5" y2="194.1" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="170.7" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="516.5" y1="172.6" x2="516.5" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="187.8" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="520.4" y1="184.5" x2="520.4" y2="210.8" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="185.1" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="524.4" y1="206.4" x2="524.4" y2="238.0" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="216.0" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="528.3" y1="198.9" x2="528.3" y2="242.1" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="213.0" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="532.3" y1="199.2" x2="532.3" y2="225.2" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="200.7" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="536.2" y1="180.1" x2="536.2" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="198.5" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="540.2" y1="212.8" x2="540.2" y2="237.1" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="221.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="544.1" y1="210.6" x2="544.1" y2="234.9" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="211.9" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="548.1" y1="185.3" x2="548.1" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="194.6" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="552.0" y1="212.8" x2="552.0" y2="246.3" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="220.0" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="556.0" y1="185.6" x2="556.0" y2="234.5" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="208.1" width="2.45" height="26.3" fill="var(--up)"/>
<line x1="560.0" y1="195.2" x2="560.0" y2="249.1" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="208.8" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="563.9" y1="207.5" x2="563.9" y2="253.3" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="218.2" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="567.9" y1="186.9" x2="567.9" y2="223.1" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="199.4" width="2.45" height="20.8" fill="var(--up)"/>
<line x1="571.8" y1="193.5" x2="571.8" y2="216.0" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="196.7" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="575.8" y1="197.8" x2="575.8" y2="227.2" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="204.0" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="579.7" y1="179.4" x2="579.7" y2="220.2" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="218.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="583.7" y1="191.5" x2="583.7" y2="245.2" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="205.3" width="2.45" height="37.7" fill="var(--down)"/>
<line x1="587.6" y1="223.3" x2="587.6" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="231.4" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="591.6" y1="239.5" x2="591.6" y2="273.5" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="257.0" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="595.5" y1="229.9" x2="595.5" y2="258.6" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="246.1" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="599.5" y1="231.4" x2="599.5" y2="259.2" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="240.4" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="603.4" y1="197.6" x2="603.4" y2="242.1" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="208.6" width="2.45" height="30.9" fill="var(--up)"/>
<line x1="607.4" y1="225.0" x2="607.4" y2="274.6" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="231.2" width="2.45" height="26.3" fill="var(--up)"/>
<line x1="611.3" y1="193.0" x2="611.3" y2="254.4" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="234.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="615.3" y1="230.9" x2="615.3" y2="260.8" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="237.1" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="619.2" y1="230.3" x2="619.2" y2="274.6" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="232.5" width="2.45" height="30.9" fill="var(--down)"/>
<line x1="623.2" y1="259.4" x2="623.2" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="265.6" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="627.1" y1="264.7" x2="627.1" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="272.2" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="631.1" y1="260.8" x2="631.1" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="278.3" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="635.0" y1="263.4" x2="635.0" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="271.9" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="639.0" y1="250.0" x2="639.0" y2="280.3" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="266.5" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="642.9" y1="258.6" x2="642.9" y2="303.3" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="268.7" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="646.9" y1="266.2" x2="646.9" y2="282.2" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="273.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="650.9" y1="252.7" x2="650.9" y2="270.0" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="261.0" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="654.8" y1="247.8" x2="654.8" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="249.4" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="658.8" y1="235.1" x2="658.8" y2="270.2" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="249.4" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="662.7" y1="220.4" x2="662.7" y2="251.8" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="230.5" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="666.7" y1="218.2" x2="666.7" y2="236.9" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="224.4" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="670.6" y1="155.8" x2="670.6" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="158.8" width="2.45" height="69.3" fill="var(--up)"/>
<line x1="674.6" y1="156.2" x2="674.6" y2="189.7" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="157.9" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="678.5" y1="167.4" x2="678.5" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="178.5" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="682.5" y1="134.7" x2="682.5" y2="183.2" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="163.0" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="686.4" y1="172.9" x2="686.4" y2="218.7" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="196.3" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="690.4" y1="229.0" x2="690.4" y2="256.6" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="232.5" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="694.3" y1="219.5" x2="694.3" y2="257.9" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="229.2" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="698.3" y1="204.0" x2="698.3" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="205.5" width="2.45" height="41.4" fill="var(--up)"/>
<line x1="702.2" y1="184.2" x2="702.2" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="193.5" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="706.2" y1="163.9" x2="706.2" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="172.0" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="710.1" y1="126.4" x2="710.1" y2="172.0" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="128.6" width="2.45" height="43.4" fill="var(--up)"/>
<line x1="714.1" y1="116.5" x2="714.1" y2="141.7" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="126.2" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="718.0" y1="115.0" x2="718.0" y2="143.5" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="122.4" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="722.0" y1="86.9" x2="722.0" y2="141.5" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="91.1" width="2.45" height="34.4" fill="var(--up)"/>
<line x1="725.9" y1="76.2" x2="725.9" y2="131.4" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="88.0" width="2.45" height="36.4" fill="var(--down)"/>
<line x1="729.9" y1="115.4" x2="729.9" y2="138.6" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="117.6" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="733.8" y1="108.2" x2="733.8" y2="133.4" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="111.5" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="737.8" y1="111.5" x2="737.8" y2="159.0" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="116.3" width="2.45" height="41.9" fill="var(--down)"/>
<line x1="741.8" y1="168.0" x2="741.8" y2="205.1" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="177.0" width="2.45" height="24.3" fill="var(--down)"/>
<line x1="745.7" y1="188.9" x2="745.7" y2="229.9" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="189.5" width="2.45" height="39.0" fill="var(--down)"/>
<line x1="749.7" y1="231.8" x2="749.7" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="231.8" width="2.45" height="34.9" fill="var(--down)"/>
<line x1="753.6" y1="260.8" x2="753.6" y2="296.3" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="268.7" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="757.6" y1="263.8" x2="757.6" y2="296.9" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="268.4" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="761.5" y1="237.5" x2="761.5" y2="272.4" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="260.8" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="765.5" y1="243.7" x2="765.5" y2="266.0" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="243.9" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="769.4" y1="237.3" x2="769.4" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="246.9" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="773.4" y1="240.8" x2="773.4" y2="270.4" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="245.9" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="777.3" y1="245.6" x2="777.3" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="262.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="781.3" y1="232.5" x2="781.3" y2="260.5" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="247.6" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="785.2" y1="235.6" x2="785.2" y2="263.0" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="241.0" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="789.2" y1="233.1" x2="789.2" y2="282.0" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="251.6" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="793.1" y1="249.4" x2="793.1" y2="296.7" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="264.5" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="797.1" y1="259.7" x2="797.1" y2="280.3" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="264.7" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="801.0" y1="259.2" x2="801.0" y2="279.8" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="269.8" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="805.0" y1="225.2" x2="805.0" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="228.8" width="2.45" height="29.4" fill="var(--up)"/>
<line x1="808.9" y1="170.2" x2="808.9" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="188.6" width="2.45" height="45.8" fill="var(--up)"/>
<line x1="812.9" y1="168.2" x2="812.9" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="170.2" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="816.8" y1="161.9" x2="816.8" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="168.5" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="820.8" y1="127.2" x2="820.8" y2="172.9" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="132.1" width="2.45" height="35.3" fill="var(--up)"/>
<line x1="824.7" y1="99.8" x2="824.7" y2="133.2" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="123.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="828.7" y1="111.2" x2="828.7" y2="214.9" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="130.3" width="2.45" height="55.9" fill="var(--down)"/>
<line x1="832.7" y1="173.7" x2="832.7" y2="204.0" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="188.9" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="836.6" y1="197.8" x2="836.6" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="206.0" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="840.6" y1="210.3" x2="840.6" y2="250.9" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="219.1" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="844.5" y1="211.9" x2="844.5" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="229.9" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="848.5" y1="178.3" x2="848.5" y2="223.5" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="185.8" width="2.45" height="37.7" fill="var(--up)"/>
<line x1="852.4" y1="173.7" x2="852.4" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="179.0" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="856.4" y1="155.1" x2="856.4" y2="182.1" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="174.6" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="860.3" y1="169.8" x2="860.3" y2="207.0" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="178.3" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="864.3" y1="175.0" x2="864.3" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="177.9" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="868.2" y1="159.3" x2="868.2" y2="188.6" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="166.1" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="872.2" y1="158.2" x2="872.2" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="165.6" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="876.1" y1="182.9" x2="876.1" y2="209.5" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="193.5" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="880.1" y1="171.8" x2="880.1" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="172.9" width="2.45" height="50.2" fill="var(--down)"/>
<line x1="884.0" y1="178.1" x2="884.0" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="206.0" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="888.0" y1="193.2" x2="888.0" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="196.3" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="891.9" y1="186.4" x2="891.9" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="198.7" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="895.9" y1="169.1" x2="895.9" y2="198.7" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="179.4" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="899.8" y1="156.4" x2="899.8" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="178.8" width="2.45" height="30.7" fill="var(--down)"/>
<line x1="903.8" y1="230.9" x2="903.8" y2="284.7" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="235.3" width="2.45" height="44.5" fill="var(--down)"/>
<line x1="907.7" y1="268.0" x2="907.7" y2="313.2" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="280.1" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="911.7" y1="268.2" x2="911.7" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="271.1" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="915.6" y1="270.4" x2="915.6" y2="300.9" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="277.2" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="919.6" y1="255.7" x2="919.6" y2="284.9" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="263.4" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="923.6" y1="270.4" x2="923.6" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="282.9" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="927.5" y1="241.7" x2="927.5" y2="329.6" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="264.0" width="2.45" height="42.5" fill="var(--up)"/>
<line x1="931.5" y1="250.2" x2="931.5" y2="276.1" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="257.5" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="935.4" y1="226.3" x2="935.4" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="231.4" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="939.4" y1="249.4" x2="939.4" y2="291.9" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="265.6" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="943.3" y1="256.4" x2="943.3" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="256.6" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="947.3" y1="236.0" x2="947.3" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="246.5" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="951.2" y1="212.1" x2="951.2" y2="248.9" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="216.0" width="2.45" height="30.3" fill="var(--up)"/>
<line x1="955.2" y1="208.8" x2="955.2" y2="230.5" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="220.4" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="959.1" y1="182.3" x2="959.1" y2="226.8" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="183.2" width="2.45" height="38.8" fill="var(--up)"/>
<line x1="963.1" y1="179.6" x2="963.1" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="182.9" width="2.45" height="38.6" fill="var(--down)"/>
<line x1="967.0" y1="169.1" x2="967.0" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="184.7" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="971.0" y1="168.2" x2="971.0" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="169.8" width="2.45" height="56.3" fill="var(--down)"/>
<line x1="974.9" y1="210.1" x2="974.9" y2="272.6" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="222.0" width="2.45" height="38.4" fill="var(--down)"/>
<line x1="978.9" y1="224.4" x2="978.9" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="249.6" width="2.45" height="36.8" fill="var(--down)"/>
<line x1="982.8" y1="264.5" x2="982.8" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="275.9" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="986.8" y1="252.7" x2="986.8" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="273.5" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="990.7" y1="175.9" x2="990.7" y2="272.8" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="200.5" width="2.45" height="71.2" fill="var(--up)"/>
<line x1="994.7" y1="192.8" x2="994.7" y2="237.5" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="201.8" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="998.6" y1="191.7" x2="998.6" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="199.2" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="1002.6" y1="176.6" x2="1002.6" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="186.4" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="1006.5" y1="158.6" x2="1006.5" y2="201.8" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="175.3" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="1010.5" y1="181.0" x2="1010.5" y2="217.6" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="184.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1014.5" y1="176.1" x2="1014.5" y2="209.5" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="182.5" width="2.45" height="25.9" fill="var(--down)"/>
<line x1="1018.4" y1="200.0" x2="1018.4" y2="223.3" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="206.2" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="1022.4" y1="166.3" x2="1022.4" y2="228.8" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="169.3" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="1026.3" y1="146.8" x2="1026.3" y2="199.6" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="153.6" width="2.45" height="30.7" fill="var(--down)"/>
<line x1="1030.3" y1="181.6" x2="1030.3" y2="240.8" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="189.1" width="2.45" height="46.3" fill="var(--down)"/>
<line x1="1034.2" y1="216.9" x2="1034.2" y2="244.1" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="234.7" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="1038.2" y1="224.1" x2="1038.2" y2="277.6" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="242.1" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="1042.1" y1="239.5" x2="1042.1" y2="273.3" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="244.8" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="1046.1" y1="253.7" x2="1046.1" y2="300.4" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="261.2" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="1050.0" y1="248.9" x2="1050.0" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="257.5" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="60" y1="168.1" x2="1052" y2="168.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="171.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$76 R1</text>
<text x="1058" y="183.6" font-size="9.5" fill="var(--muted)">터치 9회</text>
<line x1="60" y1="88.0" x2="1052" y2="88.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="91.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$80 R2</text>
<text x="1058" y="103.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="308.2" x2="1052" y2="308.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="302.2" font-size="11.5" fill="var(--support)" font-weight="600">$69 S1</text>
<text x="1058" y="314.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="554.6" x2="1052" y2="554.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="548.6" font-size="11.5" fill="var(--support)" font-weight="600">$58 S2</text>
<text x="1058" y="560.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="257.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="249.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $72 (2026-09-17)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $80 | 2 | 2026-05-20·06-26의 스윙 고점대. 52주 최고 $80.08이 여기에 있고, 터치가 2회뿐이라 검증된 저항으로 보기엔 표본이 얇다 |
| R1 | $76 | 9 | 2026-03-02·03-27·04-09·05-05·06-10·07-09·07-24·08-19·09-09. **1년 차트에서 가장 두꺼운 레벨**이며 6개월 넘게 반복적으로 되밀린 구간이다 |
| **현재가** | **$71.81** (2026-09-17 종가) | — | R1과 S1 사이 |
| S1 | $69 | 5 | 2026-04-17·06-02·06-15·08-04·08-24. 현재가에 가장 근접한 지지로, 2026년 4월 이후에만 나타난다 |
| S2 | $58 | 3 | 2025-11-19·12-17·2026-01-06. 2026년 1분기 이전의 거래 레인지 하단 |

---

## 3. 관측된 특이 구간 — 2026년 1~4월, 지지대의 계단식 상승과 $76의 벽

- **구조적으로 두 가지가 관찰된다.** 첫째, S2 $58의 터치는 **전부 2025-11~2026-01**에, S1 $69의 터치는 **전부 2026-04 이후**에 몰려 있다 — 그 사이 3개월 동안 거래 레인지가 $58대에서 $69대로 이동한 뒤 되돌아오지 않았다. 둘째, 그 위의 R1 $76은 **2026-03부터 09까지 9회 되밀린** 1년 차트 최다 터치 레벨이다.
- 즉 이 종목은 2026년의 대부분을 **$69~$76이라는 좁은 박스 안에서** 보냈고, 위로는 아홉 번 막히고 아래로는 다섯 번 받쳐졌다. R1 마지막 터치가 2026-09-09이므로 **박스 상단은 최근까지 유효하다.**
- 현재가 $71.81은 그 박스의 중간보다 약간 아래다. 직전 판의 기준 종가 $74.15(2026-09-04)에서 −3.2% 내렸는데, 그중 $0.525는 **2026-09-11 배당락분**이다([최근 뉴스](./08_news.md)) — 배당을 감안한 실질 하락은 −2.4%다. 같은 구간에 2026-09-03 Momentum 인수 완료와 2026-09-16 연준 금리 인상이 있었으나, **어느 쪽도 박스를 깨지 못했다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-18~2026-09-17. 수집 시점: 2026-09-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py WMB --name "Williams Companies" --close-on 2026-09-17 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **원주가 기준이라 배당이 반영되지 않았다.** 이 기간에 배당락이 4회 있었고(분기당 $0.50~$0.525) 합계 약 $2.1는 차트상 하락으로 나타나지만 주주 수익률에서는 차감되지 않는다. **가장 최근 배당락이 2026-09-11로 기준 종가 직전이라**, 이 차트의 마지막 구간을 해석할 때 특히 주의할 것.
    - **2026-09-03 Momentum 인수로 신주 약 $2B어치가 발행됐지만 주가 자체에는 소급 조정이 필요 없다** — 주식분할·병합이 아니라 대가 지급용 신주 발행이므로 가격 연속성은 유지된다. 다만 시가총액·주당 지표는 이 차트와 별개로 봐야 한다([핵심 지표](./04_metrics.md) A.2).
    - `--close-on 2026-09-17`로 종료일을 고정했다. 이 문서 작성일(2026-09-18)의 미국 장이 열리기 전이라, 고정하지 않으면 미완성 봉이 종가로 들어간다.

---

*작성일: 2026-09-18*
