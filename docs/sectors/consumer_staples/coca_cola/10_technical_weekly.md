# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-10 종가 **$87.83**은 [핵심 지표 A.2](./04_metrics.md)·[밸류에이션 / 적정주가 5. 결론 — 목표주가와 판단](./06_valuation.md)에 인용된 값과 **일치**한다.

:::

---

## 1. 차트 — 최근 5년 주봉 (2021-09-06 ~ 2026-09-10)

<style>
.ko-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .ko-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ko-chart svg { width:100%; height:auto; display:block; }
.ko-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ko-chart .title { fill: var(--ink); font-weight:600; }
.ko-chart .grid { stroke: var(--grid); stroke-width:1; }
.ko-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="ko-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코카콜라(KO) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코카콜라 (KO) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-10 · 마지막 종가 $87.83 (2026-09-10) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="496.5" x2="1052" y2="496.5" class="grid"/>
<text x="52" y="500.5" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="366.9" x2="1052" y2="366.9" class="grid"/>
<text x="52" y="370.9" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="237.4" x2="1052" y2="237.4" class="grid"/>
<text x="52" y="241.4" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="107.8" x2="1052" y2="107.8" class="grid"/>
<text x="52" y="111.8" font-size="11" text-anchor="end" fill="var(--muted)">90</text>
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
<line x1="61.9" y1="546.6" x2="61.9" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="548.1" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="65.7" y1="543.1" x2="65.7" y2="569.4" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="551.6" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="69.4" y1="563.6" x2="69.4" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="572.8" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="73.2" y1="570.9" x2="73.2" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="576.1" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="77.0" y1="569.1" x2="77.0" y2="594.9" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="572.6" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="80.7" y1="562.8" x2="80.7" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="568.0" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="84.5" y1="564.3" x2="84.5" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="568.4" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="88.3" y1="542.2" x2="88.3" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="543.5" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="92.1" y1="533.2" x2="92.1" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="537.4" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="95.8" y1="535.4" x2="95.8" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="538.6" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="99.6" y1="536.1" x2="99.6" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="541.4" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="103.4" y1="546.8" x2="103.4" y2="579.6" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="559.9" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="107.1" y1="564.7" x2="107.1" y2="596.5" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="573.5" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="110.9" y1="544.1" x2="110.9" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="544.6" width="2.34" height="25.5" fill="var(--up)"/>
<line x1="114.7" y1="510.4" x2="114.7" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="525.9" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="118.5" y1="514.5" x2="118.5" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="519.5" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="122.2" y1="504.9" x2="122.2" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="506.7" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="126.0" y1="480.9" x2="126.0" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="492.2" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="129.8" y1="477.7" x2="129.8" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="478.4" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="133.6" y1="477.8" x2="133.6" y2="491.3" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="482.7" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="137.3" y1="484.4" x2="137.3" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="485.6" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="141.1" y1="473.4" x2="141.1" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="484.0" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="144.9" y1="466.3" x2="144.9" y2="494.5" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="478.6" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="148.6" y1="459.9" x2="148.6" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="463.5" width="2.34" height="30.8" fill="var(--up)"/>
<line x1="152.4" y1="458.9" x2="152.4" y2="506.6" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="459.5" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="156.2" y1="457.3" x2="156.2" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="463.2" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="160.0" y1="469.6" x2="160.0" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="470.4" width="2.34" height="53.0" fill="var(--down)"/>
<line x1="163.7" y1="492.6" x2="163.7" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="495.2" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="167.5" y1="475.6" x2="167.5" y2="496.5" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="476.6" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="171.3" y1="458.2" x2="171.3" y2="480.8" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="459.3" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="175.0" y1="444.1" x2="175.0" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="446.8" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="178.8" y1="424.3" x2="178.8" y2="449.3" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="431.4" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="182.6" y1="405.8" x2="182.6" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="428.4" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="186.4" y1="403.2" x2="186.4" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="405.8" width="2.34" height="31.0" fill="var(--down)"/>
<line x1="190.1" y1="427.7" x2="190.1" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="428.1" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="193.9" y1="421.3" x2="193.9" y2="454.9" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="422.4" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="197.7" y1="413.8" x2="197.7" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="426.0" width="2.34" height="57.8" fill="var(--down)"/>
<line x1="201.4" y1="430.4" x2="201.4" y2="475.9" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="435.8" width="2.34" height="39.3" fill="var(--up)"/>
<line x1="205.2" y1="440.5" x2="205.2" y2="469.1" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="443.6" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="209.0" y1="447.6" x2="209.0" y2="490.5" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="453.3" width="2.34" height="24.9" fill="var(--down)"/>
<line x1="212.8" y1="466.8" x2="212.8" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="486.7" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="216.5" y1="456.8" x2="216.5" y2="509.3" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="457.1" width="2.34" height="46.0" fill="var(--up)"/>
<line x1="220.3" y1="438.8" x2="220.3" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="439.7" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="224.1" y1="442.3" x2="224.1" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="442.3" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="227.8" y1="451.6" x2="227.8" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="457.7" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="231.6" y1="462.1" x2="231.6" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="463.8" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="235.4" y1="440.9" x2="235.4" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="442.4" width="2.34" height="33.9" fill="var(--up)"/>
<line x1="239.2" y1="431.2" x2="239.2" y2="461.9" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="443.5" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="242.9" y1="444.8" x2="242.9" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="448.5" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="246.7" y1="425.6" x2="246.7" y2="450.2" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="429.5" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="250.5" y1="432.7" x2="250.5" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="433.8" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="254.3" y1="457.2" x2="254.3" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="461.6" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="258.0" y1="459.1" x2="258.0" y2="483.6" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="466.4" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="261.8" y1="460.1" x2="261.8" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="465.0" width="2.34" height="37.4" fill="var(--down)"/>
<line x1="265.6" y1="487.4" x2="265.6" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="504.4" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="269.3" y1="515.0" x2="269.3" y2="549.4" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="516.0" width="2.34" height="32.0" fill="var(--down)"/>
<line x1="273.1" y1="524.8" x2="273.1" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="543.6" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="276.9" y1="542.2" x2="276.9" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="561.5" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="280.7" y1="538.2" x2="280.7" y2="561.7" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="548.8" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="284.4" y1="484.7" x2="284.4" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="486.6" width="2.34" height="53.4" fill="var(--up)"/>
<line x1="288.2" y1="489.1" x2="288.2" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="489.8" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="292.0" y1="477.7" x2="292.0" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="479.4" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="295.7" y1="474.2" x2="295.7" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="479.4" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="299.5" y1="460.1" x2="299.5" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="461.6" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="303.3" y1="437.9" x2="303.3" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="440.1" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="307.1" y1="446.2" x2="307.1" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="452.3" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="310.8" y1="435.6" x2="310.8" y2="466.3" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="453.7" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="314.6" y1="444.0" x2="314.6" y2="464.5" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="447.0" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="318.4" y1="436.2" x2="318.4" y2="455.4" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="445.5" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="322.1" y1="448.9" x2="322.1" y2="469.5" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="450.3" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="325.9" y1="448.3" x2="325.9" y2="488.8" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="453.7" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="329.7" y1="465.6" x2="329.7" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="474.0" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="333.5" y1="472.5" x2="333.5" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="490.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="337.2" y1="476.0" x2="337.2" y2="506.4" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="489.5" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="341.0" y1="492.0" x2="341.0" y2="511.0" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="499.2" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="344.8" y1="484.8" x2="344.8" y2="510.1" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="494.9" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="348.5" y1="491.0" x2="348.5" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="496.6" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="352.3" y1="492.6" x2="352.3" y2="517.6" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="494.1" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="356.1" y1="489.1" x2="356.1" y2="509.5" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="506.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="359.9" y1="485.2" x2="359.9" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="496.2" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="363.6" y1="483.2" x2="363.6" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="484.8" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="367.4" y1="467.3" x2="367.4" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="470.2" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="371.2" y1="457.1" x2="371.2" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="459.7" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="375.0" y1="455.5" x2="375.0" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="456.9" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="378.7" y1="441.1" x2="378.7" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="444.0" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="382.5" y1="431.8" x2="382.5" y2="456.2" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="434.9" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="386.3" y1="435.7" x2="386.3" y2="454.1" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="442.7" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="390.0" y1="442.2" x2="390.0" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="443.2" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="393.8" y1="441.4" x2="393.8" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="441.8" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="397.6" y1="459.3" x2="397.6" y2="495.0" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="460.3" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="401.4" y1="479.4" x2="401.4" y2="504.6" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="481.4" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="405.1" y1="477.8" x2="405.1" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="483.5" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="408.9" y1="468.3" x2="408.9" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="474.8" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="412.7" y1="469.3" x2="412.7" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="475.9" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="416.4" y1="478.8" x2="416.4" y2="499.4" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="480.8" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="420.2" y1="482.2" x2="420.2" y2="500.0" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="493.9" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="424.0" y1="483.0" x2="424.0" y2="511.5" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="484.8" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="427.8" y1="461.7" x2="427.8" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="464.8" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="431.5" y1="454.1" x2="431.5" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="464.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="435.3" y1="462.9" x2="435.3" y2="488.4" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="464.7" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="439.1" y1="474.0" x2="439.1" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="481.3" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="442.8" y1="477.3" x2="442.8" y2="491.7" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="479.4" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="446.6" y1="484.4" x2="446.6" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="485.3" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="450.4" y1="486.9" x2="450.4" y2="507.9" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="489.3" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="454.2" y1="505.3" x2="454.2" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="506.2" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="457.9" y1="509.4" x2="457.9" y2="525.6" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="517.2" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="461.7" y1="511.6" x2="461.7" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="522.6" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="465.5" y1="529.0" x2="465.5" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="530.1" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="469.2" y1="548.1" x2="469.2" y2="605.9" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="549.4" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="473.0" y1="569.9" x2="473.0" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="587.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="476.8" y1="561.0" x2="476.8" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="566.8" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="480.6" y1="540.1" x2="480.6" y2="573.5" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="558.1" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="484.3" y1="527.7" x2="484.3" y2="555.8" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="538.7" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="488.1" y1="529.2" x2="488.1" y2="547.5" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="538.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="491.9" y1="528.5" x2="491.9" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="532.0" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="495.7" y1="512.6" x2="495.7" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="515.0" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="499.4" y1="511.6" x2="499.4" y2="527.5" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="514.1" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="503.2" y1="509.9" x2="503.2" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="514.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="507.0" y1="495.9" x2="507.0" y2="525.0" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="511.6" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="510.7" y1="503.1" x2="510.7" y2="529.2" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="512.0" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="514.5" y1="509.7" x2="514.5" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="510.3" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="518.3" y1="493.1" x2="518.3" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="500.7" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="522.1" y1="490.5" x2="522.1" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="491.4" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="525.8" y1="490.9" x2="525.8" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="491.4" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="529.6" y1="495.5" x2="529.6" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="499.6" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="533.4" y1="483.4" x2="533.4" y2="507.2" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="489.5" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="537.1" y1="491.5" x2="537.1" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="491.5" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="540.9" y1="487.9" x2="540.9" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="500.9" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="544.7" y1="475.5" x2="544.7" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="480.9" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="548.5" y1="480.0" x2="548.5" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="480.4" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="552.2" y1="495.0" x2="552.2" y2="509.8" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="502.7" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="556.0" y1="480.8" x2="556.0" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="498.0" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="559.8" y1="483.6" x2="559.8" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="490.1" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="563.5" y1="477.9" x2="563.5" y2="494.9" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="481.2" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="567.3" y1="479.6" x2="567.3" y2="510.6" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="481.2" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="571.1" y1="499.8" x2="571.1" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="504.2" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="574.9" y1="491.8" x2="574.9" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="494.3" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="578.6" y1="462.9" x2="578.6" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="473.9" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="582.4" y1="459.8" x2="582.4" y2="480.8" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="468.3" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="586.2" y1="452.9" x2="586.2" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="454.2" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="589.9" y1="447.7" x2="589.9" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="454.5" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="593.7" y1="457.3" x2="593.7" y2="470.9" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="458.5" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="597.5" y1="457.2" x2="597.5" y2="482.6" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="458.5" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="601.3" y1="440.0" x2="601.3" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="445.8" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="605.0" y1="444.8" x2="605.0" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="445.4" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="608.8" y1="456.3" x2="608.8" y2="471.2" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="460.6" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="612.6" y1="441.1" x2="612.6" y2="458.8" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="449.2" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="616.3" y1="440.7" x2="616.3" y2="459.4" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="444.2" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="620.1" y1="443.2" x2="620.1" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="448.5" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="623.9" y1="421.2" x2="623.9" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="427.9" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="627.7" y1="404.3" x2="627.7" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="405.1" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="631.4" y1="371.2" x2="631.4" y2="414.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="375.6" width="2.34" height="31.7" fill="var(--up)"/>
<line x1="635.2" y1="372.7" x2="635.2" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="380.0" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="639.0" y1="376.0" x2="639.0" y2="395.0" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="377.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="642.8" y1="365.2" x2="642.8" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="369.6" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="646.5" y1="333.6" x2="646.5" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="334.9" width="2.34" height="34.2" fill="var(--up)"/>
<line x1="650.3" y1="321.2" x2="650.3" y2="355.4" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="335.3" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="654.1" y1="335.6" x2="654.1" y2="360.7" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="348.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="657.8" y1="336.1" x2="657.8" y2="362.0" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="344.0" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="661.6" y1="338.4" x2="661.6" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="343.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="665.4" y1="331.3" x2="665.4" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="341.0" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="669.2" y1="365.6" x2="669.2" y2="381.7" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="366.3" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="672.9" y1="351.2" x2="672.9" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="361.2" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="676.7" y1="362.6" x2="676.7" y2="411.2" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="366.9" width="2.34" height="39.9" fill="var(--down)"/>
<line x1="680.5" y1="400.6" x2="680.5" y2="433.1" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="406.3" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="684.2" y1="425.6" x2="684.2" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="430.6" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="688.0" y1="443.1" x2="688.0" y2="478.4" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="444.8" width="2.34" height="29.1" fill="var(--down)"/>
<line x1="691.8" y1="438.4" x2="691.8" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="445.7" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="695.6" y1="430.4" x2="695.6" y2="447.6" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="440.5" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="699.3" y1="442.2" x2="699.3" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="444.0" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="703.1" y1="445.7" x2="703.1" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="456.0" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="706.9" y1="446.4" x2="706.9" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="454.6" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="710.6" y1="458.2" x2="710.6" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="464.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="714.4" y1="460.8" x2="714.4" y2="475.5" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="466.1" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="718.2" y1="473.5" x2="718.2" y2="488.4" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="477.0" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="722.0" y1="460.6" x2="722.0" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="461.3" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="725.7" y1="454.6" x2="725.7" y2="478.7" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="458.9" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="729.5" y1="440.9" x2="729.5" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="451.4" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="733.3" y1="445.7" x2="733.3" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="446.7" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="737.0" y1="366.5" x2="737.0" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="381.5" width="2.34" height="61.8" fill="var(--up)"/>
<line x1="740.8" y1="346.2" x2="740.8" y2="387.4" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="349.4" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="744.6" y1="344.0" x2="744.6" y2="362.6" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="351.2" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="748.4" y1="332.6" x2="748.4" y2="374.0" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="348.4" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="752.1" y1="325.2" x2="752.1" y2="387.9" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="341.5" width="2.34" height="36.3" fill="var(--down)"/>
<line x1="755.9" y1="364.4" x2="755.9" y2="390.5" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="376.8" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="759.7" y1="349.8" x2="759.7" y2="388.5" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="362.1" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="763.5" y1="315.7" x2="763.5" y2="369.6" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="357.5" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="767.2" y1="342.9" x2="767.2" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="348.4" width="2.34" height="67.4" fill="var(--up)"/>
<line x1="771.0" y1="322.5" x2="771.0" y2="354.9" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="328.0" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="774.8" y1="310.2" x2="774.8" y2="352.3" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="323.1" width="2.34" height="19.0" fill="var(--down)"/>
<line x1="778.5" y1="321.8" x2="778.5" y2="363.3" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="340.0" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="782.3" y1="332.1" x2="782.3" y2="361.0" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="345.3" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="786.1" y1="337.6" x2="786.1" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="341.0" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="789.9" y1="338.8" x2="789.9" y2="358.0" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="340.6" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="793.6" y1="334.9" x2="793.6" y2="361.0" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="339.7" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="797.4" y1="340.5" x2="797.4" y2="360.8" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="340.6" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="801.2" y1="332.1" x2="801.2" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="349.4" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="804.9" y1="345.9" x2="804.9" y2="382.7" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="351.4" width="2.34" height="30.6" fill="var(--down)"/>
<line x1="808.7" y1="359.7" x2="808.7" y2="380.3" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="362.6" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="812.5" y1="335.2" x2="812.5" y2="365.7" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="349.4" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="816.3" y1="349.2" x2="816.3" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="349.2" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="820.0" y1="357.8" x2="820.0" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="368.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="823.8" y1="358.9" x2="823.8" y2="385.0" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="364.4" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="827.6" y1="374.4" x2="827.6" y2="396.2" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="381.7" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="831.3" y1="355.6" x2="831.3" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="362.5" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="835.1" y1="353.2" x2="835.1" y2="374.8" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="363.0" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="838.9" y1="344.8" x2="838.9" y2="379.2" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="365.2" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="842.7" y1="363.9" x2="842.7" y2="389.2" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="365.5" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="846.4" y1="373.9" x2="846.4" y2="401.0" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="380.4" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="850.2" y1="390.6" x2="850.2" y2="406.5" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="394.6" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="854.0" y1="404.1" x2="854.0" y2="418.1" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="409.9" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="857.7" y1="406.8" x2="857.7" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="416.7" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="861.5" y1="405.9" x2="861.5" y2="427.1" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="410.3" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="865.3" y1="400.6" x2="865.3" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="405.3" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="869.1" y1="386.3" x2="869.1" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="387.1" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="872.8" y1="345.9" x2="872.8" y2="393.9" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="370.7" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="876.6" y1="355.2" x2="876.6" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="369.8" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="880.4" y1="355.6" x2="880.4" y2="397.2" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="359.8" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="884.2" y1="342.4" x2="884.2" y2="374.2" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="351.9" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="887.9" y1="325.6" x2="887.9" y2="359.5" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="328.7" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="891.7" y1="325.1" x2="891.7" y2="346.6" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="326.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="895.5" y1="329.2" x2="895.5" y2="368.6" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="333.2" width="2.34" height="33.7" fill="var(--down)"/>
<line x1="899.2" y1="358.0" x2="899.2" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="360.2" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="903.0" y1="349.8" x2="903.0" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="361.3" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="906.8" y1="363.5" x2="906.8" y2="371.3" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="367.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="910.6" y1="361.5" x2="910.6" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="366.9" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="914.3" y1="358.4" x2="914.3" y2="402.3" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="360.3" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="918.1" y1="344.8" x2="918.1" y2="366.4" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="355.2" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="921.9" y1="327.3" x2="921.9" y2="369.6" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="329.6" width="2.34" height="37.3" fill="var(--up)"/>
<line x1="925.6" y1="303.4" x2="925.6" y2="337.5" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="304.6" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="929.4" y1="247.7" x2="929.4" y2="309.9" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="249.9" width="2.34" height="52.1" fill="var(--up)"/>
<line x1="933.2" y1="232.1" x2="933.2" y2="289.1" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="254.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="937.0" y1="239.4" x2="937.0" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="239.4" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="940.7" y1="211.5" x2="940.7" y2="243.8" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="217.2" width="2.34" height="26.4" fill="var(--up)"/>
<line x1="944.5" y1="219.2" x2="944.5" y2="284.6" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="221.2" width="2.34" height="54.5" fill="var(--down)"/>
<line x1="948.3" y1="258.0" x2="948.3" y2="282.3" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="271.8" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="952.0" y1="257.7" x2="952.0" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="263.3" width="2.34" height="42.1" fill="var(--down)"/>
<line x1="955.8" y1="288.5" x2="955.8" y2="314.2" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="292.9" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="959.6" y1="276.0" x2="959.6" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="279.9" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="963.4" y1="259.5" x2="963.4" y2="298.0" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="270.1" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="967.1" y1="270.4" x2="967.1" y2="305.8" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="272.1" width="2.34" height="20.5" fill="var(--down)"/>
<line x1="970.9" y1="276.1" x2="970.9" y2="308.0" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="281.0" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="974.7" y1="233.2" x2="974.7" y2="297.0" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="255.8" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="978.4" y1="246.0" x2="978.4" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="257.8" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="982.2" y1="219.7" x2="982.2" y2="265.3" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="226.7" width="2.34" height="34.5" fill="var(--up)"/>
<line x1="986.0" y1="202.9" x2="986.0" y2="232.3" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="218.2" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="989.8" y1="204.8" x2="989.8" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="226.5" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="993.5" y1="227.8" x2="993.5" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="244.1" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="997.3" y1="185.0" x2="997.3" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="203.4" width="2.34" height="42.9" fill="var(--up)"/>
<line x1="1001.1" y1="219.4" x2="1001.1" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="223.4" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="1004.9" y1="201.0" x2="1004.9" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="203.3" width="2.34" height="43.8" fill="var(--up)"/>
<line x1="1008.6" y1="183.7" x2="1008.6" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="183.7" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="1012.4" y1="163.8" x2="1012.4" y2="215.2" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="184.3" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="1016.2" y1="165.3" x2="1016.2" y2="226.6" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="186.8" width="2.34" height="30.3" fill="var(--down)"/>
<line x1="1019.9" y1="199.5" x2="1019.9" y2="226.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="208.2" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="1023.7" y1="95.9" x2="1023.7" y2="205.0" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="139.0" width="2.34" height="58.4" fill="var(--up)"/>
<line x1="1027.5" y1="127.5" x2="1027.5" y2="170.5" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="127.5" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="1031.3" y1="134.1" x2="1031.3" y2="164.0" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="137.5" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="1035.0" y1="83.6" x2="1035.0" y2="148.6" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="93.6" width="2.34" height="49.2" fill="var(--up)"/>
<line x1="1038.8" y1="75.6" x2="1038.8" y2="121.3" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="80.4" width="2.34" height="31.9" fill="var(--down)"/>
<line x1="1042.6" y1="110.7" x2="1042.6" y2="137.2" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="114.2" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="1046.3" y1="121.3" x2="1046.3" y2="141.4" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="135.9" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="1050.1" y1="121.3" x2="1050.1" y2="136.4" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="126.2" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="60" y1="384.0" x2="1052" y2="384.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="378.0" font-size="11.5" fill="var(--support)" font-weight="600">$69 S1</text>
<text x="1058" y="390.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="410.9" x2="1052" y2="410.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="404.9" font-size="11.5" fill="var(--support)" font-weight="600">$67 S2</text>
<text x="1058" y="416.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="483.2" x2="1052" y2="483.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.2" font-size="11.5" fill="var(--support)" font-weight="600">$61 S3</text>
<text x="1058" y="489.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="135.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="127.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $88 (2026-09-10)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **기술적 분석 — 일봉·1년의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$87.83** (2026-09-10 종가) | — | **기간 내 상단 저항 없음(신고가 구간)** — 가장 가까운 지지는 S1 |
| S1 | $69 | 2 | 2025-05-12·2025-06-16 — 2025년 상반기 고점대였던 자리가 이제 지지 후보다 |
| S2 | $67 | 4 | 2025-04-07·2025-07-28·2025-09-29·2026-01-05 — 5년 구간에서 **가장 많이 닿은 레벨**(터치 4회) |
| S3 | $61 | 3 | 2024-05-27·2024-11-11·2025-01-06 — 2024~2025년 박스권 하단 |
| 참고선 | $92.49 | — | 2026-08-24 사상 최고가. 스윙 클러스터가 아니라 단일 고점이라 **저항 레벨로 처리하지 않았다** |

> **현재가 위에 저항이 없다는 것은 강세 신호가 아니라 "참고할 과거 데이터가 없다"는 뜻이다.** 5년 내내 $50~70에서 움직이던 주가가 2026년에 처음 $87대로 올라왔으므로, 위쪽에는 비교할 거래 이력 자체가 없다. 반대로 아래쪽 지지($69·$67)는 현재가에서 **21~24% 떨어진 곳**이라 근시일 완충 역할을 하지 못한다.

---

## 3. 관측된 특이 구간 — 2026년 상반기 배수 재평가 구간

- 일봉 문서가 다루는 2026-07-28 갭업은 이 구간의 마지막 계기일 뿐이고, 주봉에서 보면 **2026년 1월($67대)부터 8월($92)까지 이어진 37% 상승이 하나의 레짐 전환**이다.
- 2021~2025년 5년간 이 주식은 $50~70의 박스권에 있었고, S2($67)에 네 번, S3($61)에 세 번 닿았다. 그 박스의 상단을 2026년 상반기에 돌파한 뒤 되돌아오지 않았다.
- **이 재평가는 이익이 아니라 배수에서 왔다** — 같은 기간 비교 EPS는 가이던스 기준 +9.5% 늘 뿐인데 주가는 37% 올랐다([밸류에이션 / 적정주가 2. 최근 3개년](./06_valuation.md)). 따라서 박스권 상단이던 $69~70이 앞으로 지지로 작동할지는 **배수가 유지되는지에 달려 있고**, 기술적 레벨만으로는 답이 나오지 않는다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-06~2026-09-10. 수집 시점: 2026-09-11. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py KO --name "코카콜라" --interval 1wk --close-on 2026-09-10 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **5년 구간 안에 사업 구조가 크게 바뀌지는 않았다** — 재프랜차이즈(해외 병입 매각)가 이어졌지만 매출의 10% 안팎이라 과거 레벨이 현재 펀더멘털과 단절되지는 않았다. 다만 2026년 중 종결 예정인 CCBA 매각은 FY2026 보고 매출에 2~3%p 역풍을 주므로, 그 이후의 주가는 매출 계보가 한 단계 끊긴 상태에서 형성된다.
    - 기간 내 **주식분할은 없었다**(마지막 2:1 분할은 2012-08). 이 차트는 **원주가**라 5년간의 배당(누적 약 $9.6)이 반영돼 있지 않다.

---

*작성일: 2026-09-11*
