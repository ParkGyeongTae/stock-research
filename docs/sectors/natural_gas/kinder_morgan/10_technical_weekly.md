# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉으로 다년 가격 구조를 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-17 종가 $31.31은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[일봉 차트](./09_technical_daily.md)와 모두 일치**한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-17)

<style>
.kmi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.kmi-chart svg { width:100%; height:auto; display:block; }
.kmi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.kmi-chart .title { fill: var(--ink); font-weight:600; }
.kmi-chart .grid { stroke: var(--grid); stroke-width:1; }
.kmi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="kmi-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kinder Morgan(KMI) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Kinder Morgan (KMI) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-17 · 마지막 종가 $31.31 (2026-09-17) · 단위 USD</text>
<line x1="60" y1="599.5" x2="1052" y2="599.5" class="grid"/>
<text x="52" y="603.5" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="466.9" x2="1052" y2="466.9" class="grid"/>
<text x="52" y="470.9" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="334.4" x2="1052" y2="334.4" class="grid"/>
<text x="52" y="338.4" font-size="11" text-anchor="end" fill="var(--muted)">25</text>
<line x1="60" y1="201.8" x2="1052" y2="201.8" class="grid"/>
<text x="52" y="205.8" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="69.3" x2="1052" y2="69.3" class="grid"/>
<text x="52" y="73.3" font-size="11" text-anchor="end" fill="var(--muted)">35</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.2" y1="56.0" x2="122.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.2" y1="626.0" x2="122.2" y2="631.0" class="axis"/>
<text x="122.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="318.4" y1="56.0" x2="318.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="318.4" y1="626.0" x2="318.4" y2="631.0" class="axis"/>
<text x="318.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="514.5" y1="56.0" x2="514.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="514.5" y1="626.0" x2="514.5" y2="631.0" class="axis"/>
<text x="514.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="714.4" y1="56.0" x2="714.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="714.4" y1="626.0" x2="714.4" y2="631.0" class="axis"/>
<text x="714.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="910.6" y1="56.0" x2="910.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="910.6" y1="626.0" x2="910.6" y2="631.0" class="axis"/>
<text x="910.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="564.8" x2="61.9" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="569.5" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="65.7" y1="556.0" x2="65.7" y2="587.0" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="558.9" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="69.4" y1="540.9" x2="69.4" y2="554.9" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="548.9" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="73.2" y1="532.4" x2="73.2" y2="559.2" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="534.0" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="77.0" y1="503.8" x2="77.0" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="507.8" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="80.7" y1="499.8" x2="80.7" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="505.1" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="84.5" y1="520.5" x2="84.5" y2="553.6" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="525.0" width="2.34" height="28.1" fill="var(--down)"/>
<line x1="88.3" y1="543.8" x2="88.3" y2="558.1" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="547.8" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="92.1" y1="544.6" x2="92.1" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="545.1" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="95.8" y1="546.5" x2="95.8" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="553.6" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="99.6" y1="557.3" x2="99.6" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="566.1" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="103.4" y1="560.5" x2="103.4" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="561.8" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="107.1" y1="562.6" x2="107.1" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="568.7" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="110.9" y1="567.7" x2="110.9" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="569.3" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="114.7" y1="578.5" x2="114.7" y2="599.2" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="582.5" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="118.5" y1="573.5" x2="118.5" y2="586.5" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="576.7" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="122.2" y1="538.0" x2="122.2" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="539.3" width="2.34" height="35.0" fill="var(--up)"/>
<line x1="126.0" y1="522.6" x2="126.0" y2="544.1" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="522.9" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="129.8" y1="520.5" x2="129.8" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="523.7" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="133.6" y1="514.7" x2="133.6" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="541.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="137.3" y1="532.1" x2="137.3" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="537.2" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="141.1" y1="529.8" x2="141.1" y2="543.5" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="532.1" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="144.9" y1="532.1" x2="144.9" y2="560.8" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="532.9" width="2.34" height="24.1" fill="var(--down)"/>
<line x1="148.6" y1="542.5" x2="148.6" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="544.6" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="152.4" y1="496.9" x2="152.4" y2="549.9" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="497.7" width="2.34" height="50.9" fill="var(--up)"/>
<line x1="156.2" y1="489.5" x2="156.2" y2="517.3" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="496.1" width="2.34" height="21.2" fill="var(--down)"/>
<line x1="160.0" y1="520.2" x2="160.0" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="522.6" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="163.7" y1="491.6" x2="163.7" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="491.6" width="2.34" height="38.4" fill="var(--up)"/>
<line x1="167.5" y1="486.5" x2="167.5" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="487.6" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="171.3" y1="477.8" x2="171.3" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="480.7" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="175.0" y1="479.7" x2="175.0" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="483.6" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="178.8" y1="461.9" x2="178.8" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="481.8" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="182.6" y1="495.8" x2="182.6" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="497.9" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="186.4" y1="484.2" x2="186.4" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="485.5" width="2.34" height="31.8" fill="var(--up)"/>
<line x1="190.1" y1="491.1" x2="190.1" y2="515.7" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="493.4" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="193.9" y1="469.8" x2="193.9" y2="502.2" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="492.6" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="197.7" y1="466.4" x2="197.7" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="468.5" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="201.4" y1="462.7" x2="201.4" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="467.2" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="205.2" y1="461.6" x2="205.2" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="465.9" width="2.34" height="26.8" fill="var(--down)"/>
<line x1="209.0" y1="502.7" x2="209.0" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="504.3" width="2.34" height="67.3" fill="var(--down)"/>
<line x1="212.8" y1="552.0" x2="212.8" y2="573.5" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="560.3" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="216.5" y1="533.5" x2="216.5" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="547.0" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="220.3" y1="543.8" x2="220.3" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="547.3" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="224.1" y1="547.5" x2="224.1" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="551.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="227.8" y1="523.7" x2="227.8" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="529.2" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="231.6" y1="513.9" x2="231.6" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="520.2" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="235.4" y1="518.6" x2="235.4" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="526.6" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="239.2" y1="500.1" x2="239.2" y2="533.7" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="501.7" width="2.34" height="32.1" fill="var(--up)"/>
<line x1="242.9" y1="494.8" x2="242.9" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="500.9" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="246.7" y1="484.7" x2="246.7" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="493.7" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="250.5" y1="489.7" x2="250.5" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="494.8" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="254.3" y1="507.0" x2="254.3" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="508.8" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="258.0" y1="499.5" x2="258.0" y2="527.9" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="506.7" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="261.8" y1="515.2" x2="261.8" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="533.2" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="265.6" y1="547.8" x2="265.6" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="556.0" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="269.3" y1="525.3" x2="269.3" y2="547.5" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="540.1" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="273.1" y1="526.6" x2="273.1" y2="550.7" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="538.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="276.9" y1="517.6" x2="276.9" y2="547.5" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="532.7" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="280.7" y1="515.7" x2="280.7" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="526.1" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="284.4" y1="507.2" x2="284.4" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="515.4" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="288.2" y1="499.0" x2="288.2" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="501.7" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="292.0" y1="494.5" x2="292.0" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="502.5" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="295.7" y1="496.9" x2="295.7" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="503.3" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="299.5" y1="483.9" x2="299.5" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="493.4" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="303.3" y1="490.0" x2="303.3" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="490.5" width="2.34" height="44.0" fill="var(--down)"/>
<line x1="307.1" y1="510.7" x2="307.1" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="528.2" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="310.8" y1="516.2" x2="310.8" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="516.2" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="314.6" y1="510.9" x2="314.6" y2="523.7" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="514.4" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="318.4" y1="501.7" x2="318.4" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="504.6" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="322.1" y1="491.9" x2="322.1" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="497.4" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="325.9" y1="490.8" x2="325.9" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="495.3" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="329.7" y1="496.1" x2="329.7" y2="511.5" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="500.3" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="333.5" y1="503.0" x2="333.5" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="512.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="337.2" y1="509.1" x2="337.2" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="510.4" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="341.0" y1="506.4" x2="341.0" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="511.7" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="344.8" y1="527.9" x2="344.8" y2="539.6" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="529.8" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="348.5" y1="527.9" x2="348.5" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="529.2" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="352.3" y1="526.3" x2="352.3" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="530.0" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="356.1" y1="538.5" x2="356.1" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="559.7" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="359.9" y1="545.9" x2="359.9" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="552.0" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="363.6" y1="532.1" x2="363.6" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="532.9" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="367.4" y1="524.2" x2="367.4" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="526.1" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="371.2" y1="520.5" x2="371.2" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="525.0" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="375.0" y1="523.7" x2="375.0" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="525.0" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="378.7" y1="528.4" x2="378.7" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="536.9" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="382.5" y1="540.4" x2="382.5" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="545.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="386.3" y1="541.7" x2="386.3" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="543.5" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="390.0" y1="549.1" x2="390.0" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="549.9" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="393.8" y1="554.9" x2="393.8" y2="570.1" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="560.3" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="397.6" y1="551.2" x2="397.6" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="553.1" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="401.4" y1="536.7" x2="401.4" y2="556.0" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="545.7" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="405.1" y1="539.6" x2="405.1" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="545.4" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="408.9" y1="545.9" x2="408.9" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="546.2" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="412.7" y1="537.5" x2="412.7" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="540.6" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="416.4" y1="536.1" x2="416.4" y2="552.8" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="540.6" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="420.2" y1="529.0" x2="420.2" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="540.9" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="424.0" y1="522.3" x2="424.0" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="525.3" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="427.8" y1="512.0" x2="427.8" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="523.7" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="431.5" y1="525.8" x2="431.5" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="529.8" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="435.3" y1="522.3" x2="435.3" y2="543.8" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="525.8" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="439.1" y1="523.7" x2="439.1" y2="541.4" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="525.0" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="442.8" y1="533.5" x2="442.8" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="533.5" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="446.6" y1="532.7" x2="446.6" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="535.6" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="450.4" y1="540.6" x2="450.4" y2="557.9" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="543.3" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="454.2" y1="535.9" x2="454.2" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="544.6" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="457.9" y1="542.8" x2="457.9" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="544.3" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="461.7" y1="551.5" x2="461.7" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="557.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="465.5" y1="556.5" x2="465.5" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="557.1" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="469.2" y1="541.7" x2="469.2" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="543.5" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="473.0" y1="534.8" x2="473.0" y2="550.7" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="541.2" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="476.8" y1="544.6" x2="476.8" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="549.4" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="480.6" y1="546.5" x2="480.6" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="549.9" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="484.3" y1="548.1" x2="484.3" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="548.1" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="488.1" y1="544.6" x2="488.1" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="547.5" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="491.9" y1="534.3" x2="491.9" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="537.2" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="495.7" y1="525.3" x2="495.7" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="526.6" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="499.4" y1="522.6" x2="499.4" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="527.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="503.2" y1="523.1" x2="503.2" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="528.7" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="507.0" y1="524.2" x2="507.0" y2="546.5" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="526.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="510.7" y1="522.9" x2="510.7" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="525.3" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="514.5" y1="513.6" x2="514.5" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="519.4" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="518.3" y1="516.0" x2="518.3" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="520.7" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="522.1" y1="520.5" x2="522.1" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="522.1" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="525.8" y1="534.0" x2="525.8" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="534.8" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="529.6" y1="533.5" x2="529.6" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="534.8" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="533.4" y1="550.4" x2="533.4" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="550.4" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="537.1" y1="541.7" x2="537.1" y2="560.5" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="543.5" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="540.9" y1="534.8" x2="540.9" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="539.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="544.7" y1="533.2" x2="544.7" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="534.3" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="548.5" y1="521.3" x2="548.5" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="524.5" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="552.2" y1="517.0" x2="552.2" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="524.5" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="556.0" y1="511.7" x2="556.0" y2="532.7" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="518.4" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="559.8" y1="508.6" x2="559.8" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="510.9" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="563.5" y1="500.9" x2="563.5" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="507.8" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="567.3" y1="503.5" x2="567.3" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="507.2" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="571.1" y1="496.1" x2="571.1" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="497.7" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="574.9" y1="495.6" x2="574.9" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="499.0" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="578.6" y1="503.8" x2="578.6" y2="516.5" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="504.8" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="582.4" y1="488.7" x2="582.4" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="491.3" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="586.2" y1="472.5" x2="586.2" y2="492.1" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="474.9" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="589.9" y1="468.8" x2="589.9" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="474.6" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="593.7" y1="479.9" x2="593.7" y2="497.9" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="480.5" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="597.5" y1="471.2" x2="597.5" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="477.0" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="601.3" y1="465.1" x2="601.3" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="476.5" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="605.0" y1="468.5" x2="605.0" y2="478.6" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="474.6" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="608.8" y1="461.9" x2="608.8" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="470.4" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="612.6" y1="464.8" x2="612.6" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="467.5" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="616.3" y1="458.4" x2="616.3" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="461.9" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="620.1" y1="419.5" x2="620.1" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="427.4" width="2.34" height="32.1" fill="var(--up)"/>
<line x1="623.9" y1="417.6" x2="623.9" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="426.4" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="627.7" y1="419.2" x2="627.7" y2="453.4" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="429.5" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="631.4" y1="432.7" x2="631.4" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="439.9" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="635.2" y1="435.1" x2="635.2" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="438.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="639.0" y1="429.8" x2="639.0" y2="444.7" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="433.0" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="642.8" y1="424.8" x2="642.8" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="425.3" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="646.5" y1="423.2" x2="646.5" y2="439.4" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="428.5" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="650.3" y1="432.7" x2="650.3" y2="452.1" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="435.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="654.1" y1="417.1" x2="654.1" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="419.5" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="657.8" y1="404.9" x2="657.8" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="418.1" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="661.6" y1="370.2" x2="661.6" y2="423.2" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="371.0" width="2.34" height="47.7" fill="var(--up)"/>
<line x1="665.4" y1="342.3" x2="665.4" y2="385.8" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="342.3" width="2.34" height="28.1" fill="var(--up)"/>
<line x1="669.2" y1="323.0" x2="669.2" y2="347.6" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="335.7" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="672.9" y1="329.1" x2="672.9" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="334.4" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="676.7" y1="331.7" x2="676.7" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="342.6" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="680.5" y1="281.3" x2="680.5" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="284.5" width="2.34" height="69.2" fill="var(--up)"/>
<line x1="684.2" y1="265.7" x2="684.2" y2="290.9" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="274.2" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="688.0" y1="233.4" x2="688.0" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="241.8" width="2.34" height="30.2" fill="var(--up)"/>
<line x1="691.8" y1="235.7" x2="691.8" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="239.2" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="695.6" y1="247.7" x2="695.6" y2="278.2" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="249.0" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="699.3" y1="258.0" x2="699.3" y2="289.3" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="258.8" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="703.1" y1="281.6" x2="703.1" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="285.3" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="706.9" y1="271.0" x2="706.9" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="276.6" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="710.6" y1="240.8" x2="710.6" y2="283.2" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="247.7" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="714.4" y1="233.1" x2="714.4" y2="263.3" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="246.9" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="718.2" y1="188.3" x2="718.2" y2="250.1" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="193.6" width="2.34" height="54.6" fill="var(--up)"/>
<line x1="722.0" y1="162.6" x2="722.0" y2="199.4" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="186.4" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="725.7" y1="222.8" x2="725.7" y2="282.7" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="227.3" width="2.34" height="41.4" fill="var(--down)"/>
<line x1="729.5" y1="258.0" x2="729.5" y2="293.5" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="280.3" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="733.3" y1="273.7" x2="733.3" y2="304.4" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="276.0" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="737.0" y1="276.0" x2="737.0" y2="302.8" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="292.0" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="740.8" y1="278.2" x2="740.8" y2="323.0" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="278.7" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="744.6" y1="257.8" x2="744.6" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="268.1" width="2.34" height="36.1" fill="var(--down)"/>
<line x1="748.4" y1="276.0" x2="748.4" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="278.7" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="752.1" y1="250.3" x2="752.1" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="256.7" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="755.9" y1="224.9" x2="755.9" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="245.0" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="759.7" y1="229.9" x2="759.7" y2="331.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="251.9" width="2.34" height="74.8" fill="var(--down)"/>
<line x1="763.5" y1="290.9" x2="763.5" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="295.4" width="2.34" height="55.4" fill="var(--up)"/>
<line x1="767.2" y1="263.3" x2="767.2" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="278.7" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="771.0" y1="277.9" x2="771.0" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="285.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="774.8" y1="272.6" x2="774.8" y2="309.2" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="285.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="778.5" y1="258.3" x2="778.5" y2="300.7" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="273.1" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="782.3" y1="248.7" x2="782.3" y2="284.0" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="252.5" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="786.1" y1="250.1" x2="786.1" y2="279.5" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="258.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="789.9" y1="245.6" x2="789.9" y2="264.9" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="252.7" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="793.6" y1="236.3" x2="793.6" y2="259.6" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="248.2" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="797.4" y1="251.4" x2="797.4" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="252.2" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="801.2" y1="250.6" x2="801.2" y2="273.9" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="254.6" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="804.9" y1="224.1" x2="804.9" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="228.9" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="808.7" y1="212.9" x2="808.7" y2="258.0" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="226.2" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="812.5" y1="240.5" x2="812.5" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="244.2" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="816.3" y1="245.3" x2="816.3" y2="284.3" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="258.0" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="820.0" y1="259.6" x2="820.0" y2="295.1" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="261.2" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="823.8" y1="248.7" x2="823.8" y2="277.9" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="252.2" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="827.6" y1="242.6" x2="827.6" y2="290.1" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="251.9" width="2.34" height="32.3" fill="var(--down)"/>
<line x1="831.3" y1="278.7" x2="831.3" y2="300.7" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="284.0" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="835.1" y1="281.6" x2="835.1" y2="307.3" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="289.3" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="838.9" y1="279.0" x2="838.9" y2="304.1" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="281.9" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="842.7" y1="277.4" x2="842.7" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="288.5" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="846.4" y1="259.9" x2="846.4" y2="300.2" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="266.0" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="850.2" y1="258.0" x2="850.2" y2="279.5" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="263.6" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="854.0" y1="241.3" x2="854.0" y2="277.6" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="249.3" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="857.7" y1="230.7" x2="857.7" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="242.6" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="861.5" y1="238.4" x2="861.5" y2="279.0" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="239.2" width="2.34" height="39.5" fill="var(--down)"/>
<line x1="865.3" y1="259.3" x2="865.3" y2="281.3" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="271.3" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="869.1" y1="251.4" x2="869.1" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="264.1" width="2.34" height="47.5" fill="var(--down)"/>
<line x1="872.8" y1="297.3" x2="872.8" y2="315.0" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="302.8" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="876.6" y1="291.7" x2="876.6" y2="318.5" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="293.3" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="880.4" y1="268.4" x2="880.4" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="270.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="884.2" y1="266.8" x2="884.2" y2="298.6" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="269.9" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="887.9" y1="271.8" x2="887.9" y2="299.4" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="272.9" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="891.7" y1="254.8" x2="891.7" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="260.9" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="895.5" y1="259.6" x2="895.5" y2="295.9" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="262.3" width="2.34" height="26.2" fill="var(--down)"/>
<line x1="899.2" y1="285.1" x2="899.2" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="287.4" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="903.0" y1="271.8" x2="903.0" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="276.3" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="906.8" y1="257.5" x2="906.8" y2="276.3" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="262.5" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="910.6" y1="254.8" x2="910.6" y2="292.2" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="255.9" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="914.3" y1="255.4" x2="914.3" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="255.9" width="2.34" height="21.7" fill="var(--up)"/>
<line x1="918.1" y1="197.0" x2="918.1" y2="261.7" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="213.2" width="2.34" height="37.9" fill="var(--up)"/>
<line x1="921.9" y1="186.7" x2="921.9" y2="228.6" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="188.8" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="925.6" y1="186.2" x2="925.6" y2="216.4" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="188.6" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="929.4" y1="139.8" x2="929.4" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="140.3" width="2.34" height="48.8" fill="var(--up)"/>
<line x1="933.2" y1="128.4" x2="933.2" y2="153.8" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="129.4" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="937.0" y1="113.0" x2="937.0" y2="145.1" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="115.1" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="940.7" y1="89.4" x2="940.7" y2="120.4" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="102.4" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="944.5" y1="98.2" x2="944.5" y2="131.0" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="104.8" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="948.3" y1="98.9" x2="948.3" y2="135.5" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="111.7" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="952.0" y1="76.4" x2="952.0" y2="137.1" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="95.0" width="2.34" height="32.3" fill="var(--up)"/>
<line x1="955.8" y1="86.2" x2="955.8" y2="135.0" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="88.3" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="959.6" y1="101.1" x2="959.6" y2="148.0" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="125.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="963.4" y1="126.3" x2="963.4" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="127.8" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="967.1" y1="137.7" x2="967.1" y2="173.4" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="155.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="970.9" y1="124.4" x2="970.9" y2="182.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="134.7" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="974.7" y1="133.7" x2="974.7" y2="178.5" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="139.2" width="2.34" height="25.2" fill="var(--down)"/>
<line x1="978.4" y1="100.5" x2="978.4" y2="161.8" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="105.6" width="2.34" height="52.2" fill="var(--up)"/>
<line x1="982.2" y1="74.3" x2="982.2" y2="113.3" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="101.3" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="986.0" y1="104.0" x2="986.0" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="105.6" width="2.34" height="67.6" fill="var(--down)"/>
<line x1="989.8" y1="150.6" x2="989.8" y2="180.1" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="157.3" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="993.5" y1="142.4" x2="993.5" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="150.4" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="997.3" y1="156.2" x2="997.3" y2="178.2" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="159.7" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="1001.1" y1="113.3" x2="1001.1" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="117.2" width="2.34" height="42.7" fill="var(--up)"/>
<line x1="1004.9" y1="114.3" x2="1004.9" y2="161.8" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="118.8" width="2.34" height="28.4" fill="var(--down)"/>
<line x1="1008.6" y1="127.8" x2="1008.6" y2="158.1" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="145.6" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="1012.4" y1="123.1" x2="1012.4" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="135.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="1016.2" y1="115.4" x2="1016.2" y2="148.3" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="126.0" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="1019.9" y1="139.0" x2="1019.9" y2="168.7" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="141.6" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="1023.7" y1="155.9" x2="1023.7" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="158.3" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="1027.5" y1="126.5" x2="1027.5" y2="176.9" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="127.1" width="2.34" height="46.1" fill="var(--up)"/>
<line x1="1031.3" y1="120.7" x2="1031.3" y2="179.5" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="126.8" width="2.34" height="49.0" fill="var(--down)"/>
<line x1="1035.0" y1="141.9" x2="1035.0" y2="188.3" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="160.5" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="1038.8" y1="130.2" x2="1038.8" y2="173.4" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="154.1" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="1042.6" y1="140.0" x2="1042.6" y2="182.7" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="163.6" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="1046.3" y1="163.9" x2="1046.3" y2="190.9" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="167.1" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="1050.1" y1="163.9" x2="1050.1" y2="184.1" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="167.1" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="60" y1="75.4" x2="1052" y2="75.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="78.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$35 R1</text>
<text x="1058" y="90.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="181.3" x2="1052" y2="181.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="175.3" font-size="11.5" fill="var(--support)" font-weight="600">$31 S1</text>
<text x="1058" y="187.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="312.8" x2="1052" y2="312.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.8" font-size="11.5" fill="var(--support)" font-weight="600">$26 S2</text>
<text x="1058" y="318.8" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="536.1" x2="1052" y2="536.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="530.1" font-size="11.5" fill="var(--support)" font-weight="600">$17.39 S3</text>
<text x="1058" y="542.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="167.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="159.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $31 (2026-09-17)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $35 | 2 | 2026-03-23·05-18 주의 스윙 고점대. 5년 전체의 최고 구간이며, 터치가 2회뿐이라 검증된 저항으로 보기엔 표본이 얇다 |
| **현재가** | **$31.31** (2026-09-17 종가) | — | R1과 S1 사이 |
| S1 | $31 | 2 | 2026-04-27·06-01 주. **2026년에 처음 생긴 신생 지지대**이고 주봉 기준 터치가 2회뿐이다 — 일봉에서는 같은 레벨이 8회 터치됐다([일봉 차트](./09_technical_daily.md) §2) |
| S2 | $26 | 5 | 2024-12-16·2025-02-24·08-18·11-03·12-15 주. **5년 차트에서 가장 두꺼운 지지대**이며 2024~2025년 거래 레인지의 하단이다 |
| S3 | $17.39 | 2 | 2022-12-12·12-19 주. 3절의 레벨 이동 **이전** 가격대라 근시일 지지로 보지 않는다 — 참고선 성격이다 |

---

## 3. 관측된 특이 구간 — 2024년, 가격대 전체의 한 단 이동

- 이 5년 차트의 특징은 개별 갭이 아니라 **거래 레인지 자체가 2024년에 통째로 올라앉았고 되돌아오지 않았다**는 점이다. S3 $17.39의 터치는 2022년 12월에 몰려 있고, S2 $26의 터치는 2024-12 이후에만 나타난다 — 그 사이 구간에 유효한 클러스터가 없다는 것은 가격이 그 구간을 **머무르지 않고 통과**했다는 뜻이다.
- 계기는 회사 고유 사건이 아니라 **섹터 재평가**로 보는 편이 자연스럽다. [핵심 지표](./04_metrics.md) A.2에서 보듯 같은 기간 Adjusted EPS는 $1.07 → $1.30(+21%)인데 주가는 $17.64 → $27.49(+56%)로, 상승의 대부분이 배수 확대(PBR 1.29x → 1.96x)에서 나왔다. 데이터센터·LNG 수출 수요가 미드스트림 전반의 배수를 끌어올린 국면이다.
- **지금 유의할 점은 그 재평가가 저금리 구간에서 일어났다는 것이다.** 2024~2025년의 배수 확대는 [10년물 국채금리](../../../macro/rates/treasury_10y.md)가 지금(5.01%)보다 낮던 시기의 산물이고, [밸류에이션 / 적정주가](./06_valuation.md) 4-A가 보여주듯 할인율 1%p는 DCF 값을 약 15% 움직인다. 차트상 $26(S2)과 $31(S1) 사이의 공백은 그 재평가분이 놓인 구간이기도 하다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-17. 수집 시점: 2026-09-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py KMI --name "Kinder Morgan" --interval 1wk --close-on 2026-09-17 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **R1과 S1은 터치가 각각 2회뿐이라 강도가 얕다.** 주봉은 창이 9주라 일봉보다 스윙 포인트가 훨씬 적게 잡히므로, 같은 레벨이라도 일봉(각 3회·8회)과 터치 횟수를 직접 비교하면 안 된다.
    - **5년 원주가 차트에서 배당 미반영의 영향은 누적된다.** 이 기간 연 3~6%의 배당수익률이 계속 지급됐으므로 실제 총수익률은 차트상 상승률보다 상당히 높다.
    - 기간 내 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다.
    - `--close-on 2026-09-17`로 종료일을 고정했다 — 고정하지 않으면 진행 중인 주의 미완성 봉이 종가로 들어간다.

---

*작성일: 2026-09-18*
