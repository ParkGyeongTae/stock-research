# 기술적 분석 (주봉 캔들차트 · 5년)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 단기 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트의 가격은 전부 분할 후 기준
2026-07-02 **4:1 분할**이 이 차트 기간 안에 있다. Yahoo Finance가 분할 전 구간을 소급 조정했으므로 시계열은 연속적이지만, **당시 실제 거래가격은 표시된 값의 4배**였다 — 예컨대 5년 최저 $23.06은 당시 $92.24였다. 4. 방법론 · 한계 참고.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-15 종가 $242.49는 [핵심 지표 A.2 밸류에이션 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.** [핵심 지표](./04_metrics.md) A.2의 회계연도 말 주가($75.89·$99.52·$110.35)도 이 주봉 시계열에서 가져온 값이다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-15)

<div class="crwd-chart">
<style>
.crwd-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .crwd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .crwd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.crwd-chart svg { width:100%; height:auto; display:block; }
.crwd-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.crwd-chart .title { fill: var(--ink); font-weight:600; }
.crwd-chart .grid { stroke: var(--grid); stroke-width:1; }
.crwd-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="크라우드스트라이크(CRWD) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">크라우드스트라이크 (CRWD) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-15 · 마지막 종가 $242.49 (2026-09-15) · 단위 USD</text>
<line x1="60" y1="542.9" x2="1052" y2="542.9" class="grid"/>
<text x="52" y="546.9" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="424.1" x2="1052" y2="424.1" class="grid"/>
<text x="52" y="428.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="305.4" x2="1052" y2="305.4" class="grid"/>
<text x="52" y="309.4" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="186.6" x2="1052" y2="186.6" class="grid"/>
<text x="52" y="190.6" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="67.9" x2="1052" y2="67.9" class="grid"/>
<text x="52" y="71.9" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
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
<line x1="61.9" y1="503.3" x2="61.9" y2="510.6" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="505.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="65.7" y1="504.7" x2="65.7" y2="512.9" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="506.2" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="69.4" y1="506.7" x2="69.4" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="507.7" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="73.2" y1="510.9" x2="73.2" y2="521.7" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="515.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="77.0" y1="497.2" x2="77.0" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="499.5" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="80.7" y1="489.0" x2="80.7" y2="501.3" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="493.4" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="84.5" y1="485.0" x2="84.5" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="493.0" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="88.3" y1="493.2" x2="88.3" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="498.0" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="92.1" y1="484.4" x2="92.1" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="492.8" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="95.8" y1="498.4" x2="95.8" y2="514.5" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="500.8" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="99.6" y1="511.2" x2="99.6" y2="529.4" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="511.6" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="103.4" y1="521.7" x2="103.4" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="522.1" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="107.1" y1="534.9" x2="107.1" y2="551.4" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="543.7" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="110.9" y1="535.6" x2="110.9" y2="547.6" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="539.8" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="114.7" y1="535.2" x2="114.7" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="536.0" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="118.5" y1="532.7" x2="118.5" y2="542.1" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="536.1" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="122.2" y1="539.6" x2="122.2" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="539.9" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="126.0" y1="542.5" x2="126.0" y2="559.4" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="553.2" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="129.8" y1="552.4" x2="129.8" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="559.1" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="133.6" y1="560.0" x2="133.6" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="561.3" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="137.3" y1="551.8" x2="137.3" y2="561.3" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="556.4" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="141.1" y1="546.7" x2="141.1" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="553.6" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="144.9" y1="549.1" x2="144.9" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="554.7" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="148.6" y1="552.2" x2="148.6" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="553.7" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="152.4" y1="539.5" x2="152.4" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="550.4" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="156.2" y1="543.7" x2="156.2" y2="569.4" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="548.5" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="160.0" y1="537.1" x2="160.0" y2="555.9" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="538.1" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="163.7" y1="527.6" x2="163.7" y2="545.5" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="529.8" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="167.5" y1="523.4" x2="167.5" y2="534.8" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="526.3" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="171.3" y1="524.8" x2="171.3" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="526.2" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="175.0" y1="517.9" x2="175.0" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="522.0" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="178.8" y1="522.4" x2="178.8" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="522.7" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="182.6" y1="533.1" x2="182.6" y2="544.2" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="541.2" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="186.4" y1="538.2" x2="186.4" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="543.8" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="190.1" y1="566.3" x2="190.1" y2="584.4" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="567.2" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="193.9" y1="568.0" x2="193.9" y2="580.7" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="570.2" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="197.7" y1="562.3" x2="197.7" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="562.6" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="201.4" y1="556.8" x2="201.4" y2="567.8" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="562.1" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="205.2" y1="553.6" x2="205.2" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="561.1" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="209.0" y1="562.2" x2="209.0" y2="572.2" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="564.3" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="212.8" y1="549.6" x2="212.8" y2="565.5" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="551.8" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="216.5" y1="551.4" x2="216.5" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="551.8" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="220.3" y1="545.9" x2="220.3" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="548.6" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="224.1" y1="548.7" x2="224.1" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="550.0" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="227.8" y1="546.5" x2="227.8" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="552.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="231.6" y1="552.3" x2="231.6" y2="561.8" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="552.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="235.4" y1="544.6" x2="235.4" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="548.1" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="239.2" y1="539.5" x2="239.2" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="542.4" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="242.9" y1="541.2" x2="242.9" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="543.3" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="246.7" y1="540.7" x2="246.7" y2="552.4" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="546.1" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="250.5" y1="544.0" x2="250.5" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="548.2" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="254.3" y1="547.9" x2="254.3" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="548.3" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="258.0" y1="545.7" x2="258.0" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="548.1" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="261.8" y1="556.6" x2="261.8" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="560.6" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="265.6" y1="559.7" x2="265.6" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="563.8" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="269.3" y1="553.7" x2="269.3" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="559.6" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="273.1" y1="559.2" x2="273.1" y2="577.1" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="559.7" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="276.9" y1="565.7" x2="276.9" y2="573.8" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="568.8" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="280.7" y1="561.8" x2="280.7" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="564.5" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="284.4" y1="561.6" x2="284.4" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="565.7" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="288.2" y1="575.6" x2="288.2" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="576.6" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="292.0" y1="571.7" x2="292.0" y2="580.2" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="577.6" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="295.7" y1="577.5" x2="295.7" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="578.5" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="299.5" y1="577.9" x2="299.5" y2="597.0" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="578.7" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="303.3" y1="587.8" x2="303.3" y2="596.1" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="588.9" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="307.1" y1="587.1" x2="307.1" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="593.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="310.8" y1="595.5" x2="310.8" y2="601.7" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="595.8" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="314.6" y1="598.6" x2="314.6" y2="603.0" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="599.1" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="318.4" y1="597.2" x2="318.4" y2="606.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="597.8" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="322.1" y1="602.3" x2="322.1" y2="606.9" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="602.5" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="325.9" y1="597.9" x2="325.9" y2="603.4" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="600.2" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="329.7" y1="596.9" x2="329.7" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="599.7" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="333.5" y1="591.8" x2="333.5" y2="601.8" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="594.2" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="337.2" y1="590.9" x2="337.2" y2="597.7" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="595.5" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="341.0" y1="590.0" x2="341.0" y2="597.1" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="593.8" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="344.8" y1="590.0" x2="344.8" y2="595.4" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="592.0" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="348.5" y1="586.1" x2="348.5" y2="591.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="586.8" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="352.3" y1="581.5" x2="352.3" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="584.4" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="356.1" y1="580.6" x2="356.1" y2="591.4" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="582.6" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="359.9" y1="579.5" x2="359.9" y2="584.3" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="583.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="363.6" y1="579.5" x2="363.6" y2="585.9" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="580.1" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="367.4" y1="579.3" x2="367.4" y2="588.2" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="581.2" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="371.2" y1="578.4" x2="371.2" y2="587.7" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="581.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="375.0" y1="578.6" x2="375.0" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="580.5" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="378.7" y1="582.2" x2="378.7" y2="590.7" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="583.0" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="382.5" y1="588.5" x2="382.5" y2="592.9" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="588.9" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="386.3" y1="580.9" x2="386.3" y2="587.2" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="584.3" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="390.0" y1="573.5" x2="390.0" y2="584.2" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="575.7" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="393.8" y1="567.7" x2="393.8" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="570.1" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="397.6" y1="565.6" x2="397.6" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="566.9" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="401.4" y1="569.1" x2="401.4" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="571.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="405.1" y1="565.3" x2="405.1" y2="573.2" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="569.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="408.9" y1="569.2" x2="408.9" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="571.0" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="412.7" y1="573.0" x2="412.7" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="574.4" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="416.4" y1="574.0" x2="416.4" y2="578.9" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="574.2" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="420.2" y1="570.2" x2="420.2" y2="576.4" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="572.9" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="424.0" y1="565.7" x2="424.0" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="572.0" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="427.8" y1="567.8" x2="427.8" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="569.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="431.5" y1="562.5" x2="431.5" y2="573.4" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="567.9" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="435.3" y1="571.3" x2="435.3" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="571.8" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="439.1" y1="571.0" x2="439.1" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="574.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="442.8" y1="569.3" x2="442.8" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="572.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="446.6" y1="562.9" x2="446.6" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="565.9" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="450.4" y1="561.1" x2="450.4" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="561.8" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="454.2" y1="559.1" x2="454.2" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="561.0" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="457.9" y1="560.1" x2="457.9" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="563.7" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="461.7" y1="561.0" x2="461.7" y2="568.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="562.2" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="465.5" y1="556.6" x2="465.5" y2="566.1" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="556.7" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="469.2" y1="548.6" x2="469.2" y2="557.1" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="551.4" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="473.0" y1="547.6" x2="473.0" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="551.5" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="476.8" y1="552.3" x2="476.8" y2="560.6" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="557.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="480.6" y1="549.6" x2="480.6" y2="559.7" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="549.9" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="484.3" y1="544.7" x2="484.3" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="545.1" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="488.1" y1="536.9" x2="488.1" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="538.7" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="491.9" y1="535.2" x2="491.9" y2="539.4" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="536.5" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="495.7" y1="520.0" x2="495.7" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="522.1" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="499.4" y1="516.4" x2="499.4" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="517.6" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="503.2" y1="506.8" x2="503.2" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="507.2" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="507.0" y1="506.2" x2="507.0" y2="512.8" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="507.1" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="510.7" y1="507.5" x2="510.7" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="510.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="514.5" y1="511.8" x2="514.5" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="512.3" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="518.3" y1="489.2" x2="518.3" y2="512.3" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="493.4" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="522.1" y1="488.9" x2="522.1" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="489.1" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="525.8" y1="479.0" x2="525.8" y2="491.4" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="483.2" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="529.6" y1="480.4" x2="529.6" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="481.4" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="533.4" y1="461.5" x2="533.4" y2="486.3" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="466.1" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="537.1" y1="460.7" x2="537.1" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="465.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="540.9" y1="467.5" x2="540.9" y2="499.4" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="467.5" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="544.7" y1="466.2" x2="544.7" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="474.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="548.5" y1="444.9" x2="548.5" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="469.9" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="552.2" y1="461.1" x2="552.2" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="472.1" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="556.0" y1="463.8" x2="556.0" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="467.1" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="559.8" y1="463.4" x2="559.8" y2="473.1" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="468.1" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="563.5" y1="468.1" x2="563.5" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="471.0" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="567.3" y1="472.9" x2="567.3" y2="480.3" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="473.9" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="571.1" y1="476.4" x2="571.1" y2="494.9" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="477.5" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="574.9" y1="480.1" x2="574.9" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="481.1" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="578.6" y1="475.3" x2="578.6" y2="490.3" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="476.0" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="582.4" y1="467.2" x2="582.4" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="471.2" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="586.2" y1="456.0" x2="586.2" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="456.2" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="589.9" y1="450.4" x2="589.9" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="452.9" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="593.7" y1="448.6" x2="593.7" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="448.7" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="597.5" y1="453.9" x2="597.5" y2="481.4" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="454.3" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="601.3" y1="429.6" x2="601.3" y2="443.7" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="432.8" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="605.0" y1="427.3" x2="605.0" y2="441.5" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="434.4" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="608.8" y1="428.1" x2="608.8" y2="439.6" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="434.1" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="612.6" y1="428.4" x2="612.6" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="430.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="616.3" y1="425.1" x2="616.3" y2="444.6" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="429.8" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="620.1" y1="433.9" x2="620.1" y2="489.4" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="440.9" width="2.34" height="39.6" fill="var(--down)"/>
<line x1="623.9" y1="492.4" x2="623.9" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="492.4" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="627.7" y1="504.0" x2="627.7" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="507.5" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="631.4" y1="515.6" x2="631.4" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="518.6" width="2.34" height="23.4" fill="var(--up)"/>
<line x1="635.2" y1="505.1" x2="635.2" y2="521.7" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="505.7" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="639.0" y1="496.3" x2="639.0" y2="505.7" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="500.4" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="642.8" y1="492.0" x2="642.8" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="497.0" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="646.5" y1="496.9" x2="646.5" y2="516.5" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="497.9" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="650.3" y1="506.3" x2="650.3" y2="517.8" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="507.8" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="654.1" y1="483.2" x2="654.1" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="483.6" width="2.34" height="23.2" fill="var(--up)"/>
<line x1="657.8" y1="482.2" x2="657.8" y2="496.6" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="484.8" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="661.6" y1="487.9" x2="661.6" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="488.1" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="665.4" y1="470.1" x2="665.4" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="471.5" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="669.2" y1="469.3" x2="669.2" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="470.7" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="672.9" y1="473.4" x2="672.9" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="477.8" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="676.7" y1="474.3" x2="676.7" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="481.6" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="680.5" y1="463.8" x2="680.5" y2="486.4" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="465.7" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="684.2" y1="448.2" x2="684.2" y2="464.6" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="461.7" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="688.0" y1="440.4" x2="688.0" y2="461.7" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="440.6" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="691.8" y1="437.5" x2="691.8" y2="459.4" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="439.0" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="695.6" y1="441.2" x2="695.6" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="444.5" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="699.3" y1="441.8" x2="699.3" y2="457.0" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="443.1" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="703.1" y1="430.7" x2="703.1" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="442.7" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="706.9" y1="443.9" x2="706.9" y2="453.9" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="448.8" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="710.6" y1="448.1" x2="710.6" y2="459.9" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="448.5" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="714.4" y1="441.7" x2="714.4" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="446.4" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="718.2" y1="441.4" x2="718.2" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="449.7" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="722.0" y1="433.4" x2="722.0" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="439.0" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="725.7" y1="417.4" x2="725.7" y2="448.1" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="425.3" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="729.5" y1="405.5" x2="729.5" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="411.3" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="733.3" y1="392.0" x2="733.3" y2="409.8" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="393.4" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="737.0" y1="391.1" x2="737.0" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="393.4" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="740.8" y1="420.2" x2="740.8" y2="442.3" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="420.9" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="744.6" y1="421.4" x2="744.6" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="424.7" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="748.4" y1="451.1" x2="748.4" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="451.6" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="752.1" y1="435.3" x2="752.1" y2="452.3" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="446.5" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="755.9" y1="428.5" x2="755.9" y2="451.7" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="441.9" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="759.7" y1="438.2" x2="759.7" y2="477.4" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="456.3" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="763.5" y1="434.4" x2="763.5" y2="484.7" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="437.2" width="2.34" height="46.2" fill="var(--up)"/>
<line x1="767.2" y1="424.1" x2="767.2" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="431.9" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="771.0" y1="408.8" x2="771.0" y2="450.5" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="409.4" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="774.8" y1="398.2" x2="774.8" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="400.0" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="778.5" y1="393.8" x2="778.5" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="402.8" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="782.3" y1="395.6" x2="782.3" y2="415.2" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="400.8" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="786.1" y1="388.5" x2="786.1" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="391.1" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="789.9" y1="380.1" x2="789.9" y2="392.4" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="381.7" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="793.6" y1="370.0" x2="793.6" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="382.0" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="797.4" y1="371.4" x2="797.4" y2="390.1" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="376.3" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="801.2" y1="368.8" x2="801.2" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="375.5" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="804.9" y1="361.0" x2="804.9" y2="387.6" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="365.1" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="808.7" y1="354.1" x2="808.7" y2="375.7" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="356.4" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="812.5" y1="356.1" x2="812.5" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="360.2" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="816.3" y1="376.2" x2="816.3" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="379.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="820.0" y1="370.7" x2="820.0" y2="392.0" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="377.4" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="823.8" y1="376.2" x2="823.8" y2="401.5" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="382.0" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="827.6" y1="389.8" x2="827.6" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="392.7" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="831.3" y1="398.9" x2="831.3" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="407.6" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="835.1" y1="402.8" x2="835.1" y2="418.6" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="408.7" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="838.9" y1="395.6" x2="838.9" y2="418.6" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="410.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="842.7" y1="413.4" x2="842.7" y2="422.5" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="413.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="846.4" y1="398.6" x2="846.4" y2="414.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="402.7" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="850.2" y1="360.5" x2="850.2" y2="403.7" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="363.2" width="2.34" height="36.2" fill="var(--up)"/>
<line x1="854.0" y1="364.6" x2="854.0" y2="383.2" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="367.1" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="857.7" y1="363.4" x2="857.7" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="370.8" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="861.5" y1="354.4" x2="861.5" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="367.4" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="865.3" y1="358.1" x2="865.3" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="364.1" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="869.1" y1="343.7" x2="869.1" y2="372.8" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="348.5" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="872.8" y1="332.9" x2="872.8" y2="349.8" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="339.2" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="876.6" y1="331.6" x2="876.6" y2="354.6" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="335.5" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="880.4" y1="325.0" x2="880.4" y2="359.4" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="336.4" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="884.2" y1="340.6" x2="884.2" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="342.8" width="2.34" height="27.5" fill="var(--down)"/>
<line x1="887.9" y1="355.8" x2="887.9" y2="368.9" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="359.3" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="891.7" y1="348.8" x2="891.7" y2="372.9" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="357.6" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="895.5" y1="347.0" x2="895.5" y2="365.5" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="357.0" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="899.2" y1="359.4" x2="899.2" y2="382.7" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="359.4" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="903.0" y1="373.1" x2="903.0" y2="382.2" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="375.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="906.8" y1="374.7" x2="906.8" y2="394.8" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="377.6" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="910.6" y1="372.7" x2="910.6" y2="393.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="382.2" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="914.3" y1="378.4" x2="914.3" y2="398.2" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="388.4" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="918.1" y1="389.2" x2="918.1" y2="400.9" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="393.0" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="921.9" y1="372.3" x2="921.9" y2="405.5" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="392.1" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="925.6" y1="396.1" x2="925.6" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="400.4" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="929.4" y1="404.6" x2="929.4" y2="432.3" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="406.5" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="933.2" y1="405.2" x2="933.2" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="410.1" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="937.0" y1="433.0" x2="937.0" y2="458.1" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="433.1" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="940.7" y1="404.1" x2="940.7" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="406.9" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="944.5" y1="393.2" x2="944.5" y2="409.0" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="399.3" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="948.3" y1="398.3" x2="948.3" y2="422.0" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="398.6" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="952.0" y1="413.8" x2="952.0" y2="446.8" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="417.6" width="2.34" height="24.6" fill="var(--down)"/>
<line x1="955.8" y1="423.7" x2="955.8" y2="438.1" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="424.6" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="959.6" y1="394.5" x2="959.6" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="421.2" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="963.4" y1="405.2" x2="963.4" y2="437.0" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="409.9" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="967.1" y1="383.8" x2="967.1" y2="414.0" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="395.5" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="970.9" y1="386.3" x2="970.9" y2="404.8" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="391.1" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="974.7" y1="347.6" x2="974.7" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="348.3" width="2.34" height="42.1" fill="var(--up)"/>
<line x1="978.4" y1="306.4" x2="978.4" y2="351.7" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="308.9" width="2.34" height="41.7" fill="var(--up)"/>
<line x1="982.2" y1="260.9" x2="982.2" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="267.7" width="2.34" height="43.9" fill="var(--up)"/>
<line x1="986.0" y1="227.3" x2="986.0" y2="285.7" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="227.6" width="2.34" height="39.2" fill="var(--up)"/>
<line x1="989.8" y1="195.1" x2="989.8" y2="263.8" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="224.7" width="2.34" height="38.5" fill="var(--down)"/>
<line x1="993.5" y1="244.7" x2="993.5" y2="294.8" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="256.2" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="997.3" y1="245.5" x2="997.3" y2="269.2" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="250.4" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="1001.1" y1="238.8" x2="1001.1" y2="268.6" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="245.4" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="1004.9" y1="187.7" x2="1004.9" y2="243.6" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="200.9" width="2.34" height="39.4" fill="var(--up)"/>
<line x1="1008.6" y1="164.1" x2="1008.6" y2="221.5" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="211.5" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="1012.4" y1="145.1" x2="1012.4" y2="231.8" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="179.3" width="2.34" height="38.5" fill="var(--up)"/>
<line x1="1016.2" y1="167.0" x2="1016.2" y2="229.9" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="179.3" width="2.34" height="47.0" fill="var(--down)"/>
<line x1="1019.9" y1="206.5" x2="1019.9" y2="248.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="208.3" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="1023.7" y1="140.7" x2="1023.7" y2="204.2" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="152.4" width="2.34" height="48.4" fill="var(--up)"/>
<line x1="1027.5" y1="121.3" x2="1027.5" y2="152.1" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="146.4" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="1031.3" y1="141.1" x2="1031.3" y2="217.5" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="147.4" width="2.34" height="58.4" fill="var(--down)"/>
<line x1="1035.0" y1="117.6" x2="1035.0" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="142.9" width="2.34" height="68.6" fill="var(--up)"/>
<line x1="1038.8" y1="106.2" x2="1038.8" y2="185.2" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="134.8" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="1042.6" y1="151.8" x2="1042.6" y2="176.5" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="163.2" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="1046.3" y1="93.1" x2="1046.3" y2="148.5" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="102.6" width="2.34" height="38.9" fill="var(--up)"/>
<line x1="1050.1" y1="82.2" x2="1050.1" y2="110.4" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="85.7" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="60" y1="460.3" x2="1052" y2="460.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="454.3" font-size="11.5" fill="var(--support)" font-weight="600">$85 S1</text>
<text x="1058" y="466.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="483.1" x2="1052" y2="483.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.1" font-size="11.5" fill="var(--support)" font-weight="600">$75 S2</text>
<text x="1058" y="489.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="578.5" x2="1052" y2="578.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="572.5" font-size="11.5" fill="var(--support)" font-weight="600">$35 S3</text>
<text x="1058" y="584.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="85.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="77.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $242 (2026-09-15)</text>
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
| **현재가** | **$242.49** (2026-09-15 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $85 | 2 | 2025-01-13·2026-02-23 — 2024년 장애에서 회복한 뒤의 고점권 눌림목 두 차례 |
| S2 | $75 | 2 | 2024-06-03·2025-04-07 — 2024-07-19 장애 **직전**의 고점권과, 그로부터 약 9개월 뒤 되돌아온 자리 |
| S3 | $35 | 2 | 2023-07-03·2023-08-14 — 2023년 여름 구간. 현재가 대비 86% 아래라 사실상 역사적 참고치 |

**5년 전체에서도 저항선이 없다** — 현재가가 5년 최고($243.98) 부근이기 때문이다. 세 지지선은 $35~$85 구간에 있어 **현재가의 14~35% 수준**이며, 근시일 참고치로는 의미가 없다.

터치 횟수가 전부 2회에 그치는 것도 이 표의 한계다. 5년간 거의 일방향으로 오른 종목이라(최저 $23.06 → 현재 $242.49, **10.5배**) 같은 가격대를 여러 번 되밟은 구간 자체가 드물다.

---

## 3. 관측된 특이 구간 — 2024-07 글로벌 장애

- 2024-07-19 Falcon 센서 콘텐츠 업데이트 결함으로 전 세계 약 850만 대의 Windows 기기가 중단됐다([역사 / 주요 이벤트](./02_history.md) 참고).
- 사고가 발생한 주(2024-07-22 주간) 종가는 **$64.04**로 전주 $76.24 대비 **-16.0%**였고, 3주 뒤 $60.22까지 밀려 고점 대비 약 **-21%**를 기록했다.
- **이 구간이 S2($75) 클러스터의 성격을 설명한다** — 2024-06-03(사고 직전 고점권)과 2025-04-07(약 9개월 뒤 되돌아온 자리)이 같은 가격대에 묶여 있다. 즉 **주가가 사고 이전 수준을 회복하는 데 9개월가량 걸렸고**, 그 가격대가 이후 지지로 작동했다.
- 사고 이후 2년여 만에 현재가는 사고 직전 수준의 **약 3.2배**($76.24 → $242.49)가 됐다. **가격만 보면 이 사건은 완전히 소화됐다** — 다만 같은 아키텍처가 그대로 남아 있다는 점은 [투자 판단 3. 리스크 (약점 / Bear Case)](./07_investment.md)에서 별도로 다룬다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-15. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py CRWD --name "크라우드스트라이크" --interval 1wk --close-on 2026-09-15 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **세 지지선 모두 터치 2회에 그쳐 강도가 약하다.** 5년간 10.5배 오르는 동안 같은 가격대를 되밟은 구간이 드물었던 결과이며, 현재가 대비 65~86% 아래라 근시일 참고치로 쓸 수 없다.
    - **주식분할**: 이 5년 구간에는 **2026-07-02 4:1 분할**이 있다. 차트 가격은 Yahoo Finance가 분할 전 구간을 **소급 조정한 값**이며, [핵심 지표](./04_metrics.md)의 주당 수치와 같은 기준이다. 3절에 인용한 2024년 장애 당시 가격($76.24 → $64.04)도 분할 후 환산값이며, 당시 실제 거래가격은 각각 $304.96·$256.16이었다.

---

*작성일: 2026-09-16*
