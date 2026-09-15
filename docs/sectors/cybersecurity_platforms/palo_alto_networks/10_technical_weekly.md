# 기술적 분석 (주봉 캔들차트 · 5년)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 단기 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-15 종가 $375.09는 [핵심 지표 A.2 밸류에이션 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.** [핵심 지표](./04_metrics.md) A.2의 FY2024·FY2025 회계연도 말 주가($152.80·$172.88)도 이 주봉 시계열에서 가져온 값이다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-15)

<div class="panw-chart">
<style>
.panw-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .panw-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .panw-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.panw-chart svg { width:100%; height:auto; display:block; }
.panw-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.panw-chart .title { fill: var(--ink); font-weight:600; }
.panw-chart .grid { stroke: var(--grid); stroke-width:1; }
.panw-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="팔로알토 네트웍스(PANW) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">팔로알토 네트웍스 (PANW) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-15 · 마지막 종가 $375.09 (2026-09-15) · 단위 USD</text>
<line x1="60" y1="553.7" x2="1052" y2="553.7" class="grid"/>
<text x="52" y="557.7" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="473.5" x2="1052" y2="473.5" class="grid"/>
<text x="52" y="477.5" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="393.2" x2="1052" y2="393.2" class="grid"/>
<text x="52" y="397.2" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="312.9" x2="1052" y2="312.9" class="grid"/>
<text x="52" y="316.9" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="232.6" x2="1052" y2="232.6" class="grid"/>
<text x="52" y="236.6" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="152.3" x2="1052" y2="152.3" class="grid"/>
<text x="52" y="156.3" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="72.1" x2="1052" y2="72.1" class="grid"/>
<text x="52" y="76.1" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="61.9" y1="584.3" x2="61.9" y2="587.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="584.6" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="65.7" y1="582.9" x2="65.7" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="583.1" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="69.4" y1="583.6" x2="69.4" y2="588.9" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="584.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="73.2" y1="579.9" x2="73.2" y2="590.4" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="582.4" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="77.0" y1="576.7" x2="77.0" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="578.4" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="80.7" y1="575.3" x2="80.7" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="577.8" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="84.5" y1="577.2" x2="84.5" y2="586.1" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="578.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="88.3" y1="577.0" x2="88.3" y2="584.5" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="577.7" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="92.1" y1="574.2" x2="92.1" y2="582.6" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="576.4" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="95.8" y1="568.2" x2="95.8" y2="579.6" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="572.4" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="99.6" y1="564.6" x2="99.6" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="571.6" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="103.4" y1="565.0" x2="103.4" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="569.8" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="107.1" y1="570.0" x2="107.1" y2="581.0" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="572.0" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="110.9" y1="569.0" x2="110.9" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="569.8" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="114.7" y1="562.6" x2="114.7" y2="575.8" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="564.0" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="118.5" y1="561.1" x2="118.5" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="563.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="122.2" y1="564.3" x2="122.2" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="564.9" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="126.0" y1="570.4" x2="126.0" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="576.8" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="129.8" y1="570.6" x2="129.8" y2="585.2" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="583.3" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="133.6" y1="578.0" x2="133.6" y2="592.3" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="581.5" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="137.3" y1="575.2" x2="137.3" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="576.4" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="141.1" y1="570.4" x2="141.1" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="577.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="144.9" y1="571.0" x2="144.9" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="578.9" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="148.6" y1="561.5" x2="148.6" y2="589.5" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="561.8" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="152.4" y1="554.0" x2="152.4" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="559.9" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="156.2" y1="563.6" x2="156.2" y2="574.6" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="564.6" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="160.0" y1="559.8" x2="160.0" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="559.9" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="163.7" y1="547.2" x2="163.7" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="547.8" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="167.5" y1="544.1" x2="167.5" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="549.1" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="171.3" y1="545.4" x2="171.3" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="549.4" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="175.0" y1="544.2" x2="175.0" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="546.6" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="178.8" y1="542.8" x2="178.8" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="548.1" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="182.6" y1="553.5" x2="182.6" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="561.1" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="186.4" y1="561.0" x2="186.4" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="564.9" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="190.1" y1="580.6" x2="190.1" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="582.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="193.9" y1="579.3" x2="193.9" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="582.7" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="197.7" y1="576.0" x2="197.7" y2="588.5" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="578.7" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="201.4" y1="574.4" x2="201.4" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="577.1" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="205.2" y1="571.2" x2="205.2" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="576.1" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="209.0" y1="581.6" x2="209.0" y2="591.3" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="587.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="212.8" y1="576.6" x2="212.8" y2="585.3" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="577.6" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="216.5" y1="576.6" x2="216.5" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="576.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="220.3" y1="573.6" x2="220.3" y2="580.4" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="574.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="224.1" y1="573.4" x2="224.1" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="575.5" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="227.8" y1="574.1" x2="227.8" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="576.3" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="231.6" y1="576.8" x2="231.6" y2="590.4" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="577.3" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="235.4" y1="572.4" x2="235.4" y2="584.8" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="580.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="239.2" y1="570.6" x2="239.2" y2="582.6" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="573.3" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="242.9" y1="572.7" x2="242.9" y2="578.7" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="575.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="246.7" y1="559.4" x2="246.7" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="564.3" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="250.5" y1="561.0" x2="250.5" y2="571.3" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="565.8" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="254.3" y1="562.2" x2="254.3" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="563.2" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="258.0" y1="561.8" x2="258.0" y2="576.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="562.8" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="261.8" y1="571.9" x2="261.8" y2="585.4" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="576.9" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="265.6" y1="579.5" x2="265.6" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="582.8" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="269.3" y1="570.6" x2="269.3" y2="581.4" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="577.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="273.1" y1="577.4" x2="273.1" y2="595.5" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="578.2" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="276.9" y1="580.4" x2="276.9" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="584.2" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="280.7" y1="576.6" x2="280.7" y2="587.9" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="577.0" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="284.4" y1="572.9" x2="284.4" y2="601.9" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="577.6" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="288.2" y1="579.3" x2="288.2" y2="601.5" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="581.6" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="292.0" y1="575.4" x2="292.0" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="579.9" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="295.7" y1="573.3" x2="295.7" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="575.6" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="299.5" y1="570.6" x2="299.5" y2="582.8" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="575.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="303.3" y1="575.2" x2="303.3" y2="586.9" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="576.0" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="307.1" y1="578.6" x2="307.1" y2="593.6" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="586.4" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="310.8" y1="592.2" x2="310.8" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="592.4" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="314.6" y1="600.6" x2="314.6" y2="604.5" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="601.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="318.4" y1="599.1" x2="318.4" y2="607.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="600.9" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="322.1" y1="602.2" x2="322.1" y2="608.2" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="602.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="325.9" y1="596.7" x2="325.9" y2="604.2" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="597.0" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="329.7" y1="584.9" x2="329.7" y2="597.0" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="586.0" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="333.5" y1="581.3" x2="333.5" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="586.1" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="337.2" y1="578.6" x2="337.2" y2="590.6" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="581.6" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="341.0" y1="571.7" x2="341.0" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="578.4" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="344.8" y1="562.6" x2="344.8" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="564.5" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="348.5" y1="559.5" x2="348.5" y2="565.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="560.5" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="352.3" y1="561.5" x2="352.3" y2="567.8" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="563.6" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="356.1" y1="560.6" x2="356.1" y2="568.5" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="562.5" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="359.9" y1="556.9" x2="359.9" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="560.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="363.6" y1="553.5" x2="363.6" y2="561.9" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="554.0" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="367.4" y1="554.6" x2="367.4" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="555.3" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="371.2" y1="553.9" x2="371.2" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="554.2" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="375.0" y1="551.0" x2="375.0" y2="560.8" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="553.8" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="378.7" y1="558.0" x2="378.7" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="559.3" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="382.5" y1="565.6" x2="382.5" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="566.6" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="386.3" y1="552.5" x2="386.3" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="554.3" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="390.0" y1="554.9" x2="390.0" y2="564.4" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="555.1" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="393.8" y1="540.1" x2="393.8" y2="563.1" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="544.4" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="397.6" y1="537.7" x2="397.6" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="539.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="401.4" y1="529.5" x2="401.4" y2="540.8" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="532.5" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="405.1" y1="515.5" x2="405.1" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="516.4" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="408.9" y1="514.2" x2="408.9" y2="523.9" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="518.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="412.7" y1="508.1" x2="412.7" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="509.2" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="416.4" y1="506.5" x2="416.4" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="509.5" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="420.2" y1="512.1" x2="420.2" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="514.4" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="424.0" y1="513.0" x2="424.0" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="518.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="427.8" y1="513.7" x2="427.8" y2="522.5" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="514.9" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="431.5" y1="510.4" x2="431.5" y2="543.0" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="513.6" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="435.3" y1="537.3" x2="435.3" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="538.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="439.1" y1="536.3" x2="439.1" y2="552.8" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="538.9" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="442.8" y1="516.6" x2="442.8" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="524.4" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="446.6" y1="517.8" x2="446.6" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="519.5" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="450.4" y1="513.7" x2="450.4" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="514.6" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="454.2" y1="510.2" x2="454.2" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="513.7" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="457.9" y1="519.0" x2="457.9" y2="532.4" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="521.4" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="461.7" y1="523.0" x2="461.7" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="526.1" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="465.5" y1="513.7" x2="465.5" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="516.3" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="469.2" y1="500.8" x2="469.2" y2="517.0" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="506.1" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="473.0" y1="500.9" x2="473.0" y2="521.4" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="505.8" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="476.8" y1="510.1" x2="476.8" y2="524.8" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="520.7" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="480.6" y1="511.9" x2="480.6" y2="523.5" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="518.8" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="484.3" y1="510.4" x2="484.3" y2="526.6" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="510.8" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="488.1" y1="501.8" x2="488.1" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="510.1" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="491.9" y1="499.1" x2="491.9" y2="514.0" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="500.7" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="495.7" y1="476.0" x2="495.7" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="476.5" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="499.4" y1="474.3" x2="499.4" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="474.7" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="503.2" y1="459.0" x2="503.2" y2="477.2" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="467.6" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="507.0" y1="464.7" x2="507.0" y2="476.7" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="470.1" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="510.7" y1="471.9" x2="510.7" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="474.4" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="514.5" y1="479.8" x2="514.5" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="479.9" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="518.3" y1="449.1" x2="518.3" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="453.2" width="2.34" height="33.5" fill="var(--up)"/>
<line x1="522.1" y1="441.0" x2="522.1" y2="455.3" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="443.2" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="525.8" y1="432.8" x2="525.8" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="436.3" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="529.6" y1="435.2" x2="529.6" y2="447.2" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="437.3" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="533.4" y1="408.6" x2="533.4" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="411.7" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="537.1" y1="412.2" x2="537.1" y2="430.3" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="412.9" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="540.9" y1="417.8" x2="540.9" y2="505.5" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="423.0" width="2.34" height="64.8" fill="var(--down)"/>
<line x1="544.7" y1="451.3" x2="544.7" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="471.5" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="548.5" y1="471.6" x2="548.5" y2="492.1" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="471.9" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="552.2" y1="479.3" x2="552.2" y2="491.4" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="487.8" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="556.0" y1="480.8" x2="556.0" y2="492.3" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="484.1" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="559.8" y1="480.8" x2="559.8" y2="489.5" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="485.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="563.5" y1="485.0" x2="563.5" y2="501.6" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="485.5" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="567.3" y1="485.1" x2="567.3" y2="501.0" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="490.3" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="571.1" y1="485.6" x2="571.1" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="490.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="574.9" y1="477.5" x2="574.9" y2="493.4" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="480.4" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="578.6" y1="470.3" x2="578.6" y2="486.3" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="475.1" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="582.4" y1="466.5" x2="582.4" y2="477.4" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="474.3" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="586.2" y1="458.2" x2="586.2" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="459.1" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="589.9" y1="453.7" x2="589.9" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="456.1" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="593.7" y1="455.9" x2="593.7" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="457.3" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="597.5" y1="471.1" x2="597.5" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="471.9" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="601.3" y1="453.8" x2="601.3" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="459.6" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="605.0" y1="456.3" x2="605.0" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="457.1" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="608.8" y1="436.6" x2="608.8" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="442.1" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="612.6" y1="436.9" x2="612.6" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="439.7" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="616.3" y1="439.8" x2="616.3" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="441.2" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="620.1" y1="438.4" x2="620.1" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="447.1" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="623.9" y1="440.6" x2="623.9" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="445.8" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="627.7" y1="450.4" x2="627.7" y2="473.8" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="451.4" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="631.4" y1="446.9" x2="631.4" y2="486.3" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="448.2" width="2.34" height="35.5" fill="var(--up)"/>
<line x1="635.2" y1="436.7" x2="635.2" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="446.1" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="639.0" y1="413.0" x2="639.0" y2="445.3" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="432.7" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="642.8" y1="420.4" x2="642.8" y2="438.7" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="423.1" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="646.5" y1="420.9" x2="646.5" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="425.7" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="650.3" y1="431.2" x2="650.3" y2="447.2" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="435.8" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="654.1" y1="433.9" x2="654.1" y2="450.4" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="436.1" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="657.8" y1="436.6" x2="657.8" y2="445.8" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="441.6" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="661.6" y1="438.6" x2="661.6" y2="450.8" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="439.5" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="665.4" y1="410.6" x2="665.4" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="414.7" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="669.2" y1="409.5" x2="669.2" y2="419.3" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="411.7" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="672.9" y1="406.0" x2="672.9" y2="427.2" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="413.3" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="676.7" y1="417.8" x2="676.7" y2="427.6" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="418.9" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="680.5" y1="398.6" x2="680.5" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="400.1" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="684.2" y1="386.3" x2="684.2" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="396.7" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="688.0" y1="390.0" x2="688.0" y2="413.1" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="398.8" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="691.8" y1="395.4" x2="691.8" y2="407.0" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="402.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="695.6" y1="385.8" x2="695.6" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="388.4" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="699.3" y1="385.0" x2="699.3" y2="403.0" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="387.6" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="703.1" y1="381.6" x2="703.1" y2="417.3" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="396.2" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="706.9" y1="410.0" x2="706.9" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="413.6" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="710.6" y1="416.0" x2="710.6" y2="427.2" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="419.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="714.4" y1="420.8" x2="714.4" y2="445.8" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="421.5" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="718.2" y1="423.1" x2="718.2" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="429.9" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="722.0" y1="407.7" x2="722.0" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="412.9" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="725.7" y1="396.8" x2="725.7" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="417.1" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="729.5" y1="396.9" x2="729.5" y2="425.1" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="402.9" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="733.3" y1="389.3" x2="733.3" y2="411.2" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="393.1" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="737.0" y1="379.7" x2="737.0" y2="408.8" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="396.9" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="740.8" y1="403.8" x2="740.8" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="406.6" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="744.6" y1="403.4" x2="744.6" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="406.8" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="748.4" y1="418.6" x2="748.4" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="421.5" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="752.1" y1="409.8" x2="752.1" y2="425.7" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="419.7" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="755.9" y1="407.6" x2="755.9" y2="440.1" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="415.7" width="2.34" height="21.3" fill="var(--down)"/>
<line x1="759.7" y1="433.7" x2="759.7" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="442.0" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="763.5" y1="434.8" x2="763.5" y2="482.9" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="444.0" width="2.34" height="33.3" fill="var(--up)"/>
<line x1="767.2" y1="433.4" x2="767.2" y2="446.0" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="438.7" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="771.0" y1="426.1" x2="771.0" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="426.9" width="2.34" height="22.3" fill="var(--up)"/>
<line x1="774.8" y1="406.5" x2="774.8" y2="428.4" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="412.9" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="778.5" y1="407.7" x2="778.5" y2="418.3" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="414.2" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="782.3" y1="400.5" x2="782.3" y2="410.2" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="404.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="786.1" y1="401.3" x2="786.1" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="408.5" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="789.9" y1="404.9" x2="789.9" y2="420.7" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="405.4" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="793.6" y1="391.8" x2="793.6" y2="406.9" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="393.8" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="797.4" y1="393.3" x2="797.4" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="394.7" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="801.2" y1="388.5" x2="801.2" y2="398.2" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="394.4" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="804.9" y1="382.4" x2="804.9" y2="399.6" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="392.3" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="808.7" y1="385.3" x2="808.7" y2="401.4" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="390.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="812.5" y1="383.3" x2="812.5" y2="414.5" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="391.8" width="2.34" height="21.7" fill="var(--down)"/>
<line x1="816.3" y1="397.0" x2="816.3" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="400.0" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="820.0" y1="384.7" x2="820.0" y2="401.9" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="387.9" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="823.8" y1="376.5" x2="823.8" y2="444.0" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="387.1" width="2.34" height="49.6" fill="var(--down)"/>
<line x1="827.6" y1="434.2" x2="827.6" y2="449.0" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="434.2" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="831.3" y1="424.7" x2="831.3" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="430.0" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="835.1" y1="410.8" x2="835.1" y2="433.8" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="415.9" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="838.9" y1="404.8" x2="838.9" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="408.4" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="842.7" y1="399.1" x2="842.7" y2="415.1" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="402.1" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="846.4" y1="388.8" x2="846.4" y2="401.5" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="399.1" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="850.2" y1="378.7" x2="850.2" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="380.0" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="854.0" y1="377.9" x2="854.0" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="382.1" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="857.7" y1="373.8" x2="857.7" y2="391.8" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="381.6" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="861.5" y1="364.4" x2="861.5" y2="379.8" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="378.1" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="865.3" y1="369.5" x2="865.3" y2="387.8" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="371.6" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="869.1" y1="363.9" x2="869.1" y2="377.9" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="365.7" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="872.8" y1="355.3" x2="872.8" y2="367.5" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="360.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="876.6" y1="360.3" x2="876.6" y2="381.4" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="361.1" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="880.4" y1="361.0" x2="880.4" y2="395.8" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="370.4" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="884.2" y1="381.6" x2="884.2" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="385.2" width="2.34" height="35.5" fill="var(--down)"/>
<line x1="887.9" y1="407.8" x2="887.9" y2="423.4" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="409.0" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="891.7" y1="393.6" x2="891.7" y2="416.3" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="395.0" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="895.5" y1="393.3" x2="895.5" y2="411.6" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="394.2" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="899.2" y1="407.1" x2="899.2" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="407.1" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="903.0" y1="408.4" x2="903.0" y2="417.6" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="411.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="906.8" y1="410.8" x2="906.8" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="412.2" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="910.6" y1="399.3" x2="910.6" y2="423.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="410.8" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="914.3" y1="402.7" x2="914.3" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="411.9" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="918.1" y1="411.6" x2="918.1" y2="427.3" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="418.5" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="921.9" y1="410.2" x2="921.9" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="423.1" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="925.6" y1="428.9" x2="925.6" y2="470.7" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="429.4" width="2.34" height="29.1" fill="var(--down)"/>
<line x1="929.4" y1="440.6" x2="929.4" y2="463.2" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="446.2" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="933.2" y1="447.8" x2="933.2" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="448.3" width="2.34" height="27.3" fill="var(--down)"/>
<line x1="937.0" y1="471.4" x2="937.0" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="475.2" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="940.7" y1="448.8" x2="940.7" y2="479.9" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="449.3" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="944.5" y1="439.5" x2="944.5" y2="456.1" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="446.1" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="948.3" y1="438.1" x2="948.3" y2="454.4" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="445.0" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="952.0" y1="447.2" x2="952.0" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="450.3" width="2.34" height="28.0" fill="var(--down)"/>
<line x1="955.8" y1="452.1" x2="955.8" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="452.3" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="959.6" y1="426.5" x2="959.6" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="452.0" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="963.4" y1="440.4" x2="963.4" y2="465.7" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="444.8" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="967.1" y1="422.9" x2="967.1" y2="449.1" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="427.6" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="970.9" y1="415.7" x2="970.9" y2="436.4" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="423.6" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="974.7" y1="380.2" x2="974.7" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="380.5" width="2.34" height="42.1" fill="var(--up)"/>
<line x1="978.4" y1="319.6" x2="978.4" y2="384.1" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="324.4" width="2.34" height="56.3" fill="var(--up)"/>
<line x1="982.2" y1="294.6" x2="982.2" y2="336.6" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="295.9" width="2.34" height="34.8" fill="var(--up)"/>
<line x1="986.0" y1="258.8" x2="986.0" y2="324.1" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="262.0" width="2.34" height="37.8" fill="var(--up)"/>
<line x1="989.8" y1="227.9" x2="989.8" y2="282.4" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="256.0" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="993.5" y1="261.6" x2="993.5" y2="311.1" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="265.3" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="997.3" y1="250.5" x2="997.3" y2="273.8" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="252.2" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="1001.1" y1="222.6" x2="1001.1" y2="260.7" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="225.9" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="1004.9" y1="139.3" x2="1004.9" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="155.5" width="2.34" height="61.4" fill="var(--up)"/>
<line x1="1008.6" y1="123.2" x2="1008.6" y2="208.6" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="170.1" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="1012.4" y1="122.2" x2="1012.4" y2="206.5" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="138.4" width="2.34" height="53.9" fill="var(--up)"/>
<line x1="1016.2" y1="126.2" x2="1016.2" y2="197.8" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="144.8" width="2.34" height="49.7" fill="var(--down)"/>
<line x1="1019.9" y1="178.1" x2="1019.9" y2="218.9" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="181.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1023.7" y1="109.0" x2="1023.7" y2="184.5" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="130.1" width="2.34" height="43.9" fill="var(--up)"/>
<line x1="1027.5" y1="73.9" x2="1027.5" y2="131.5" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="97.3" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="1031.3" y1="94.5" x2="1031.3" y2="163.6" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="99.0" width="2.34" height="40.8" fill="var(--down)"/>
<line x1="1035.0" y1="92.4" x2="1035.0" y2="187.7" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="117.7" width="2.34" height="24.9" fill="var(--up)"/>
<line x1="1038.8" y1="98.2" x2="1038.8" y2="198.3" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="120.2" width="2.34" height="59.0" fill="var(--down)"/>
<line x1="1042.6" y1="160.7" x2="1042.6" y2="192.0" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="183.4" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="1046.3" y1="106.4" x2="1046.3" y2="168.0" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="113.9" width="2.34" height="44.1" fill="var(--up)"/>
<line x1="1050.1" y1="103.5" x2="1050.1" y2="125.4" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="112.1" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="60" y1="449.1" x2="1052" y2="449.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="443.1" font-size="11.5" fill="var(--support)" font-weight="600">$165 S1</text>
<text x="1058" y="455.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="486.5" x2="1052" y2="486.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="480.5" font-size="11.5" fill="var(--support)" font-weight="600">$142 S2</text>
<text x="1058" y="492.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="503.5" x2="1052" y2="503.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="497.5" font-size="11.5" fill="var(--support)" font-weight="600">$131 S3</text>
<text x="1058" y="509.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="112.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="104.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $375 (2026-09-15)</text>
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
| **현재가** | **$375.09** (2026-09-15 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $165 | 3 | 2024-09-30·2025-01-13·2025-08-04 — 2024년 하반기~2025년 여름에 걸쳐 세 차례 확인된 가격대. FY2025 회계연도 말 주가($172.88)가 이 부근이다 |
| S2 | $142 | 3 | 2024-08-05·2025-04-07·2026-02-23 — 2년 반에 걸쳐 세 차례. 마지막 터치가 CyberArk 인수 종결 직후라 가장 최근의 의미 있는 저점대다 |
| S3 | $131 | 2 | 2024-02-19·2024-04-01 — 2024년 2월 플랫폼화 전략 발표 직후의 급락 구간 |

**5년 전체를 봐도 저항선이 없다** — 현재가가 5년 구간의 최고가(398.88) 부근이기 때문이다. 세 지지선은 모두 $131~$165 구간에 몰려 있는데, 이는 **현재가의 35~44% 수준**이다. 즉 **최근 5년간 형성된 어떤 가격 기억도 현재가 근처에는 없다.**

이 종목의 5년 최저는 $66.11(분할 소급 조정 후)이었다 — 5년 만에 **5.7배**가 된 셈이고, 그중 상당 부분이 최근 1년에 집중돼 있다([기술적 분석 — 일봉·1년](./09_technical_daily.md) 참고).

---

## 3. 관측된 특이 구간 — 2026년 상반기 재평가

- **2026-02-16 주간: -10.9%** (전주 종가 $166.95 → $148.70). CyberArk 인수가 종결된 주(2026-02-11)에 주가가 밀리며 S2($142) 클러스터 부근까지 내려왔다.
- 그 뒤 약 7개월 만에 $375.09까지 **152% 상승**했다. 같은 기간 Non-GAAP EPS 기대치는 FY2026 $3.84에서 FY2027 가이던스 $4.18로 8.9% 오르는 데 그쳤으므로, **이 상승은 이익이 아니라 배수 확장**이다([밸류에이션 / 적정주가 2. 최근 3개년 — 적정주가 vs 실제주가](./06_valuation.md)).
- 이 구간 이후 가격대가 구조적으로 재설정됐다 — **$180 아래의 스윙 레벨들(S1~S3)은 인수 전 자본구조·사업 규모 기준이므로**, 인수 후의 회사에 대한 지지선으로 기계적으로 적용하기 어렵다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-15. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PANW --name "팔로알토 네트웍스" --interval 1wk --close-on 2026-09-15 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 재설정 구간 때문에 세 지지선의 실효성이 낮다.** 전부 CyberArk 인수 이전에 형성된 레벨이며, 현재가 대비 35~44% 수준이라 근시일 참고치로 쓰기 어렵다.
    - **주식분할**: 이 5년 구간에는 **2022-09-14 3:1**, **2024-12-16 2:1** 두 차례의 분할이 있다. 차트의 가격은 Yahoo Finance가 **두 분할을 모두 소급 반영한 값**이므로 시계열이 연속적이며, [핵심 지표](./04_metrics.md)의 주당 수치와 같은 기준이다. 발표 당시의 실제 거래가격(예: 2022년의 $500대)과는 다르다.

---

*작성일: 2026-09-16*
