# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉으로 여러 사이클에 걸친 구조적 지지/저항을 본다. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-15 종가 $108.09**는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)와 일치한다(2026-09-15는 주 중간이라 주봉 데이터로는 직접 대조되지 않아 일봉으로 확인했다).
- ⚠️ **모든 가격은 2024-02-26 3:1 분할 소급 조정 후 기준이다** — 2024년 2월 이전 캔들은 실제 당시 호가의 3분의 1로 표시된다(§4 참고).
- ⚠️ **마지막 주봉은 미완성이다.** 생성 시점(2026-09-16 미 동부 10:01)이 해당 주의 거래 중이라 마지막 캔들은 아직 마감되지 않았다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-16)

<div class="wmt-chart">
<style>
.wmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.wmt-chart svg { width:100%; height:auto; display:block; }
.wmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.wmt-chart .title { fill: var(--ink); font-weight:600; }
.wmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.wmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="월마트(WMT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">월마트 (WMT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-16 · 마지막 종가 $107.74 (2026-09-16) · 단위 USD</text>
<line x1="60" y1="604.1" x2="1052" y2="604.1" class="grid"/>
<text x="52" y="608.1" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="494.5" x2="1052" y2="494.5" class="grid"/>
<text x="52" y="498.5" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="384.8" x2="1052" y2="384.8" class="grid"/>
<text x="52" y="388.8" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="275.2" x2="1052" y2="275.2" class="grid"/>
<text x="52" y="279.2" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="165.6" x2="1052" y2="165.6" class="grid"/>
<text x="52" y="169.6" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
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
<line x1="61.9" y1="556.3" x2="61.9" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="558.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="558.1" x2="65.7" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="561.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="69.4" y1="561.1" x2="69.4" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="562.3" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="73.2" y1="566.3" x2="73.2" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="568.2" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="77.0" y1="565.5" x2="77.0" y2="571.0" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="566.5" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="80.7" y1="549.8" x2="80.7" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="552.3" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="84.5" y1="548.3" x2="84.5" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="550.3" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="88.3" y1="545.6" x2="88.3" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="548.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="92.1" y1="548.3" x2="92.1" y2="553.8" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="548.9" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="95.8" y1="552.1" x2="95.8" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="552.6" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="99.6" y1="553.1" x2="99.6" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="558.6" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="103.4" y1="557.9" x2="103.4" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="558.4" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="107.1" y1="565.2" x2="107.1" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="565.7" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="110.9" y1="555.6" x2="110.9" y2="570.5" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="567.1" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="114.7" y1="567.2" x2="114.7" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="568.5" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="118.5" y1="558.3" x2="118.5" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="559.0" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="122.2" y1="556.7" x2="122.2" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="558.6" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="126.0" y1="555.4" x2="126.0" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="557.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="129.8" y1="558.4" x2="129.8" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="559.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="133.6" y1="566.6" x2="133.6" y2="578.6" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="569.2" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="137.3" y1="563.9" x2="137.3" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="568.8" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="141.1" y1="567.4" x2="141.1" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="567.4" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="144.9" y1="568.3" x2="144.9" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="571.2" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="148.6" y1="570.8" x2="148.6" y2="582.1" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="571.6" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="152.4" y1="562.2" x2="152.4" y2="578.9" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="562.4" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="156.2" y1="560.1" x2="156.2" y2="570.9" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="563.8" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="160.0" y1="554.9" x2="160.0" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="557.6" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="163.7" y1="554.2" x2="163.7" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="557.6" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="167.5" y1="546.9" x2="167.5" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="547.4" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="171.3" y1="533.9" x2="171.3" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="535.7" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="175.0" y1="534.1" x2="175.0" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="536.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="178.8" y1="529.6" x2="178.8" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="536.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="182.6" y1="534.4" x2="182.6" y2="544.3" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="537.6" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="186.4" y1="540.2" x2="186.4" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="540.2" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="190.1" y1="543.6" x2="190.1" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="552.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="193.9" y1="549.8" x2="193.9" y2="609.1" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="550.4" width="2.34" height="55.1" fill="var(--down)"/>
<line x1="197.7" y1="588.3" x2="197.7" y2="604.3" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="588.6" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="201.4" y1="586.0" x2="201.4" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="590.4" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="205.2" y1="592.6" x2="205.2" y2="605.3" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="593.4" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="209.0" y1="600.9" x2="209.0" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="604.6" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="212.8" y1="594.4" x2="212.8" y2="607.3" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="597.3" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="216.5" y1="593.9" x2="216.5" y2="604.3" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="597.2" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="220.3" y1="592.0" x2="220.3" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="594.2" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="224.1" y1="585.3" x2="224.1" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="587.5" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="227.8" y1="579.6" x2="227.8" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="581.8" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="231.6" y1="580.9" x2="231.6" y2="604.0" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="581.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="235.4" y1="578.1" x2="235.4" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="583.9" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="239.2" y1="580.6" x2="239.2" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="581.8" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="242.9" y1="562.6" x2="242.9" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="573.0" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="246.7" y1="573.3" x2="246.7" y2="583.0" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="574.5" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="250.5" y1="575.4" x2="250.5" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="580.3" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="254.3" y1="572.1" x2="254.3" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="573.3" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="258.0" y1="570.7" x2="258.0" y2="583.5" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="572.9" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="261.8" y1="572.2" x2="261.8" y2="588.1" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="580.7" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="265.6" y1="578.3" x2="265.6" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="586.4" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="269.3" y1="576.3" x2="269.3" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="585.4" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="273.1" y1="577.1" x2="273.1" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="585.0" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="276.9" y1="572.3" x2="276.9" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="573.4" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="280.7" y1="562.2" x2="280.7" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="563.0" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="284.4" y1="561.0" x2="284.4" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="563.3" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="288.2" y1="560.1" x2="288.2" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="562.8" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="292.0" y1="548.8" x2="292.0" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="548.8" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="295.7" y1="543.1" x2="295.7" y2="548.9" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="543.7" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="299.5" y1="540.8" x2="299.5" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="543.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="303.3" y1="543.8" x2="303.3" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="544.2" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="307.1" y1="548.9" x2="307.1" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="556.8" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="310.8" y1="556.7" x2="310.8" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="560.7" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="314.6" y1="559.4" x2="314.6" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="560.2" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="318.4" y1="553.7" x2="318.4" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="555.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="322.1" y1="553.2" x2="322.1" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="556.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="325.9" y1="557.1" x2="325.9" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="557.9" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="329.7" y1="555.6" x2="329.7" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="561.5" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="333.5" y1="557.3" x2="333.5" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="563.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="337.2" y1="560.3" x2="337.2" y2="569.9" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="560.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="341.0" y1="554.5" x2="341.0" y2="559.9" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="555.8" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="344.8" y1="552.3" x2="344.8" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="562.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="348.5" y1="561.9" x2="348.5" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="562.6" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="352.3" y1="564.5" x2="352.3" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="566.6" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="356.1" y1="567.9" x2="356.1" y2="573.8" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="568.6" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="359.9" y1="563.0" x2="359.9" y2="568.5" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="564.3" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="363.6" y1="552.1" x2="363.6" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="553.9" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="367.4" y1="547.4" x2="367.4" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="547.8" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="371.2" y1="547.2" x2="371.2" y2="552.6" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="548.6" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="375.0" y1="545.1" x2="375.0" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="546.1" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="378.7" y1="542.4" x2="378.7" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="546.1" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="382.5" y1="544.6" x2="382.5" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="546.0" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="386.3" y1="541.3" x2="386.3" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="543.7" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="390.0" y1="541.4" x2="390.0" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="542.9" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="393.8" y1="549.1" x2="393.8" y2="558.2" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="549.8" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="397.6" y1="551.1" x2="397.6" y2="558.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="551.4" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="401.4" y1="542.5" x2="401.4" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="543.6" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="405.1" y1="534.2" x2="405.1" y2="543.5" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="539.2" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="408.9" y1="537.8" x2="408.9" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="539.3" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="412.7" y1="535.5" x2="412.7" y2="543.5" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="536.2" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="416.4" y1="532.6" x2="416.4" y2="543.0" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="536.8" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="420.2" y1="538.5" x2="420.2" y2="542.7" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="540.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="424.0" y1="533.2" x2="424.0" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="534.0" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="427.8" y1="529.3" x2="427.8" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="531.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="431.5" y1="529.8" x2="431.5" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="531.1" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="435.3" y1="527.2" x2="435.3" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="528.8" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="439.1" y1="525.9" x2="439.1" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="527.3" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="442.8" y1="532.4" x2="442.8" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="535.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="446.6" y1="525.5" x2="446.6" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="528.1" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="450.4" y1="523.9" x2="450.4" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="524.1" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="454.2" y1="520.3" x2="454.2" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="522.5" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="457.9" y1="521.5" x2="457.9" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="522.4" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="461.7" y1="524.5" x2="461.7" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="526.7" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="465.5" y1="529.1" x2="465.5" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="531.9" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="469.2" y1="530.2" x2="469.2" y2="543.3" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="531.3" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="473.0" y1="526.7" x2="473.0" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="530.0" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="476.8" y1="523.1" x2="476.8" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="528.9" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="480.6" y1="519.5" x2="480.6" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="522.5" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="484.3" y1="518.9" x2="484.3" y2="525.1" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="519.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="488.1" y1="512.8" x2="488.1" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="519.3" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="491.9" y1="536.8" x2="491.9" y2="541.7" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="538.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="495.7" y1="533.0" x2="495.7" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="538.4" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="499.4" y1="538.6" x2="499.4" y2="548.8" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="543.2" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="503.2" y1="541.9" x2="503.2" y2="550.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="544.3" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="507.0" y1="536.2" x2="507.0" y2="543.6" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="537.1" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="510.7" y1="534.1" x2="510.7" y2="538.1" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="535.3" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="514.5" y1="530.5" x2="514.5" y2="539.0" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="536.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="518.3" y1="527.5" x2="518.3" y2="537.1" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="528.6" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="522.1" y1="524.5" x2="522.1" y2="529.8" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="526.7" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="525.8" y1="523.0" x2="525.8" y2="530.4" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="523.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="529.6" y1="511.7" x2="529.6" y2="524.6" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="513.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="533.4" y1="511.5" x2="533.4" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="512.7" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="537.1" y1="509.2" x2="537.1" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="512.1" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="540.9" y1="492.0" x2="540.9" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="497.2" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="544.7" y1="495.3" x2="544.7" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="499.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="548.5" y1="488.6" x2="548.5" y2="503.2" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="493.8" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="552.2" y1="485.9" x2="552.2" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="490.7" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="556.0" y1="485.4" x2="556.0" y2="492.3" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="489.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="559.8" y1="488.7" x2="559.8" y2="493.6" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="489.7" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="563.5" y1="490.3" x2="563.5" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="492.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="567.3" y1="489.6" x2="567.3" y2="498.3" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="493.7" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="571.1" y1="490.6" x2="571.1" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="491.7" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="574.9" y1="491.6" x2="574.9" y2="502.4" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="493.6" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="578.6" y1="492.3" x2="578.6" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="493.5" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="582.4" y1="489.8" x2="582.4" y2="497.8" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="491.8" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="586.2" y1="467.7" x2="586.2" y2="497.5" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="469.0" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="589.9" y1="463.3" x2="589.9" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="465.0" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="593.7" y1="462.1" x2="593.7" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="462.9" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="597.5" y1="453.0" x2="597.5" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="462.2" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="601.3" y1="454.3" x2="601.3" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="455.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="605.0" y1="447.6" x2="605.0" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="451.1" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="608.8" y1="444.9" x2="608.8" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="450.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="612.6" y1="438.8" x2="612.6" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="439.4" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="616.3" y1="437.2" x2="616.3" y2="444.2" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="440.2" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="620.1" y1="432.4" x2="620.1" y2="443.5" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="435.5" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="623.9" y1="432.7" x2="623.9" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="434.9" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="627.7" y1="438.3" x2="627.7" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="440.5" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="631.4" y1="447.2" x2="631.4" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="450.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="635.2" y1="415.3" x2="635.2" y2="455.3" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="420.7" width="2.34" height="28.0" fill="var(--up)"/>
<line x1="639.0" y1="405.6" x2="639.0" y2="421.3" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="408.4" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="642.8" y1="398.7" x2="642.8" y2="409.1" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="400.0" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="646.5" y1="396.8" x2="646.5" y2="405.1" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="399.5" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="650.3" y1="381.1" x2="650.3" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="381.6" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="654.1" y1="379.3" x2="654.1" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="380.2" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="657.8" y1="376.1" x2="657.8" y2="389.9" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="386.1" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="661.6" y1="376.5" x2="661.6" y2="385.7" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="379.7" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="665.4" y1="379.7" x2="665.4" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="381.1" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="669.2" y1="374.9" x2="669.2" y2="386.2" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="377.7" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="672.9" y1="366.5" x2="672.9" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="371.1" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="676.7" y1="368.0" x2="676.7" y2="378.2" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="369.8" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="680.5" y1="354.5" x2="680.5" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="358.4" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="684.2" y1="353.1" x2="684.2" y2="363.3" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="357.7" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="688.0" y1="325.1" x2="688.0" y2="364.8" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="327.6" width="2.34" height="30.8" fill="var(--up)"/>
<line x1="691.8" y1="315.6" x2="691.8" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="316.3" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="695.6" y1="296.2" x2="695.6" y2="319.4" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="298.8" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="699.3" y1="297.5" x2="699.3" y2="313.4" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="299.0" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="703.1" y1="297.7" x2="703.1" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="305.8" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="706.9" y1="314.3" x2="706.9" y2="336.0" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="320.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="710.6" y1="322.9" x2="710.6" y2="332.7" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="325.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="714.4" y1="310.4" x2="714.4" y2="327.6" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="313.6" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="718.2" y1="316.7" x2="718.2" y2="329.4" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="318.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="722.0" y1="302.6" x2="722.0" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="303.9" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="725.7" y1="280.7" x2="725.7" y2="303.6" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="285.3" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="729.5" y1="258.2" x2="729.5" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="268.9" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="733.3" y1="246.2" x2="733.3" y2="268.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="253.1" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="737.0" y1="252.2" x2="737.0" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="254.8" width="2.34" height="49.0" fill="var(--down)"/>
<line x1="740.8" y1="281.5" x2="740.8" y2="318.4" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="282.8" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="744.6" y1="278.0" x2="744.6" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="286.3" width="2.34" height="34.3" fill="var(--down)"/>
<line x1="748.4" y1="328.8" x2="748.4" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="331.4" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="752.1" y1="341.1" x2="752.1" y2="358.6" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="352.1" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="755.9" y1="342.9" x2="755.9" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="349.4" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="759.7" y1="329.2" x2="759.7" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="358.8" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="763.5" y1="311.7" x2="763.5" y2="385.9" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="314.7" width="2.34" height="68.8" fill="var(--up)"/>
<line x1="767.2" y1="297.0" x2="767.2" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="312.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="771.0" y1="293.9" x2="771.0" y2="322.7" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="302.1" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="774.8" y1="279.5" x2="774.8" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="282.1" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="778.5" y1="276.7" x2="778.5" y2="295.6" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="281.0" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="782.3" y1="279.7" x2="782.3" y2="319.7" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="284.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="786.1" y1="281.7" x2="786.1" y2="302.6" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="293.6" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="789.9" y1="281.1" x2="789.9" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="282.2" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="793.6" y1="270.4" x2="793.6" y2="291.8" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="281.6" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="797.4" y1="285.7" x2="797.4" y2="311.2" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="289.5" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="801.2" y1="295.5" x2="801.2" y2="310.2" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="296.5" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="804.9" y1="280.1" x2="804.9" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="290.2" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="808.7" y1="279.7" x2="808.7" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="284.2" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="812.5" y1="278.8" x2="812.5" y2="306.9" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="284.9" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="816.3" y1="298.0" x2="816.3" y2="306.0" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="302.4" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="820.0" y1="288.1" x2="820.0" y2="302.1" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="289.1" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="823.8" y1="281.4" x2="823.8" y2="291.2" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="283.5" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="827.6" y1="249.4" x2="827.6" y2="285.1" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="254.8" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="831.3" y1="251.5" x2="831.3" y2="277.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="253.9" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="835.1" y1="260.7" x2="835.1" y2="293.0" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="275.2" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="838.9" y1="288.5" x2="838.9" y2="300.3" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="291.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="842.7" y1="267.1" x2="842.7" y2="294.4" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="272.4" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="846.4" y1="253.4" x2="846.4" y2="273.7" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="256.1" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="850.2" y1="241.7" x2="850.2" y2="263.8" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="255.2" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="854.0" y1="256.0" x2="854.0" y2="267.9" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="257.9" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="857.7" y1="253.6" x2="857.7" y2="275.9" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="258.5" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="861.5" y1="255.3" x2="861.5" y2="273.2" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="264.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="865.3" y1="222.7" x2="865.3" y2="269.4" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="232.9" width="2.34" height="34.9" fill="var(--up)"/>
<line x1="869.1" y1="230.0" x2="869.1" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="232.2" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="872.8" y1="240.4" x2="872.8" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="240.5" width="2.34" height="28.3" fill="var(--down)"/>
<line x1="876.6" y1="259.0" x2="876.6" y2="275.1" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="261.0" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="880.4" y1="253.7" x2="880.4" y2="281.4" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="261.6" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="884.2" y1="230.6" x2="884.2" y2="277.0" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="246.1" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="887.9" y1="216.6" x2="887.9" y2="254.6" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="217.6" width="2.34" height="28.2" fill="var(--up)"/>
<line x1="891.7" y1="186.1" x2="891.7" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="192.4" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="895.5" y1="182.3" x2="895.5" y2="207.8" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="183.7" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="899.2" y1="179.6" x2="899.2" y2="201.1" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="182.4" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="903.0" y1="196.7" x2="903.0" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="198.4" width="2.34" height="12.4" fill="var(--down)"/>
<line x1="906.8" y1="205.1" x2="906.8" y2="214.3" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="205.3" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="910.6" y1="190.5" x2="910.6" y2="221.5" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="195.6" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="914.3" y1="158.8" x2="914.3" y2="185.3" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="167.3" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="918.1" y1="156.7" x2="918.1" y2="181.3" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="160.7" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="921.9" y1="168.8" x2="921.9" y2="190.4" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="170.3" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="925.6" y1="101.5" x2="925.6" y2="170.8" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="104.3" width="2.34" height="64.0" fill="var(--up)"/>
<line x1="929.4" y1="85.3" x2="929.4" y2="130.6" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="89.5" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="933.2" y1="85.1" x2="933.2" y2="159.9" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="93.8" width="2.34" height="55.5" fill="var(--down)"/>
<line x1="937.0" y1="118.5" x2="937.0" y2="149.4" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="122.0" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="940.7" y1="117.7" x2="940.7" y2="156.7" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="124.7" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="944.5" y1="128.9" x2="944.5" y2="153.1" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="129.9" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="948.3" y1="126.2" x2="948.3" y2="176.5" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="128.6" width="2.34" height="42.4" fill="var(--down)"/>
<line x1="952.0" y1="142.2" x2="952.0" y2="170.8" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="149.8" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="955.8" y1="133.3" x2="955.8" y2="150.1" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="133.9" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="959.6" y1="112.5" x2="959.6" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="128.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="963.4" y1="124.1" x2="963.4" y2="151.6" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="124.5" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="967.1" y1="97.3" x2="967.1" y2="125.5" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="111.2" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="970.9" y1="92.3" x2="970.9" y2="133.2" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="102.0" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="974.7" y1="101.2" x2="974.7" y2="118.1" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="108.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="978.4" y1="89.2" x2="978.4" y2="130.6" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="102.9" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="982.2" y1="82.5" x2="982.2" y2="171.6" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="102.5" width="2.34" height="61.7" fill="var(--down)"/>
<line x1="986.0" y1="159.9" x2="986.0" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="161.8" width="2.34" height="27.1" fill="var(--down)"/>
<line x1="989.8" y1="160.7" x2="989.8" y2="205.5" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="171.8" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="993.5" y1="155.4" x2="993.5" y2="179.2" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="159.9" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="997.3" y1="149.5" x2="997.3" y2="183.2" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="167.0" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="1001.1" y1="163.4" x2="1001.1" y2="192.5" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="182.3" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="1004.9" y1="183.2" x2="1004.9" y2="235.5" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="185.0" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="1008.6" y1="197.6" x2="1008.6" y2="223.9" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="199.0" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="1012.4" y1="176.1" x2="1012.4" y2="209.1" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="194.5" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="1016.2" y1="196.3" x2="1016.2" y2="238.0" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="198.7" width="2.34" height="24.6" fill="var(--down)"/>
<line x1="1019.9" y1="187.4" x2="1019.9" y2="221.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="213.8" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="1023.7" y1="195.4" x2="1023.7" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="203.4" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="1027.5" y1="185.1" x2="1027.5" y2="216.3" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="191.5" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="1031.3" y1="182.8" x2="1031.3" y2="263.4" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="196.7" width="2.34" height="58.3" fill="var(--down)"/>
<line x1="1035.0" y1="239.1" x2="1035.0" y2="262.8" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="252.5" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="1038.8" y1="224.0" x2="1038.8" y2="259.7" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="236.1" width="2.34" height="22.3" fill="var(--up)"/>
<line x1="1042.6" y1="235.7" x2="1042.6" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="236.0" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="1046.3" y1="221.8" x2="1046.3" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="230.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1050.1" y1="229.0" x2="1050.1" y2="233.7" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="229.7" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="60" y1="83.8" x2="1052" y2="83.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="87.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$135 R1</text>
<text x="1058" y="99.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="548.2" x2="1052" y2="548.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="542.2" font-size="11.5" fill="var(--support)" font-weight="600">$50 S1</text>
<text x="1058" y="554.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="577.7" x2="1052" y2="577.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="571.7" font-size="11.5" fill="var(--support)" font-weight="600">$45 S2</text>
<text x="1058" y="583.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="232.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="224.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $108 (2026-09-16)</text>
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
| R1 | $135 | 2 | 2026-02-16·2026-05-18 — **5년(그리고 사상) 최고가 $135.16** 부근. 두 번 시도해 모두 실패했다 |
| **현재가** | **$108.09** (2026-09-15 종가) | — | R1과 S1 사이. 5년 최고 대비 **−20.0%** |
| S1 | $50 | 2 | 2023-10-02·2023-12-11 — **2023년 가격대**(분할 조정 기준)로 현재가의 절반 이하다. 구조적 참고선일 뿐 근시일 지지로 보지 않는다 |
| S2 | $45 | 3 | 2021-11-29·2022-02-21·2023-03-06 — 2021~2023년 가격대. S1과 같은 이유로 참고선 성격이다 |

**유효 레벨이 3개뿐이고, 그중 쓸 수 있는 것은 사실상 R1 하나다.** 이것이 이 차트에서 가장 중요한 관찰이다 — **현재가($108.09)와 가장 가까운 지지 클러스터가 $50으로 54% 아래에 있다.** 2024년 초부터 2026년 초까지 주가가 $50에서 $135로 거의 쉬지 않고 오르는 동안 **주봉 스윙 저점이 한 곳에도 쌓이지 않았기 때문**이며, 되돌림이 와도 기댈 구조적 지지가 이 구간에 없다는 뜻이다. 실제 근시일 지지는 주봉이 아니라 [일봉 문서](./09_technical_daily.md)의 $100(터치 5회)에서 찾아야 한다.

**5년 구조는 "2년 횡보 후 2년 급등, 그리고 첫 조정"으로 읽힌다.** 2021~2023년에는 $45~$50 구간에서 머물렀고, 2024년부터 2026년 5월까지 $135.16까지 올랐다가 현재 −20% 조정 중이다. 이 급등 구간이 [밸류에이션](./06_valuation.md) 2절에서 말하는 배수 재평가(Non-GAAP PER 24.8 → 45.1배)와 정확히 겹친다 — **가격 구조와 밸류에이션 구조가 같은 사건을 다른 방식으로 보여준다.**

---


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-16. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py WMT --name "월마트" --interval 1wk --close-on 2026-09-15 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - ⚠️ **주식분할 소급 조정**: 기간 내 **2024-02-26 3:1 분할**이 있었고 차트의 모든 과거 가격은 조정 후 기준이다. 즉 2021~2023년의 $45~$50 레벨은 당시 실제로는 $135~$150에 거래되던 가격이다. 조정하지 않은 과거 자료와 이 차트를 겹쳐 보면 3배 어긋난다.
    - ⚠️ **마지막 주봉은 미완성이다.** 생성 시점이 해당 주의 거래 중(2026-09-16 미 동부 10:01, 정규장)이었으므로 마지막 캔들의 고가·저가·종가는 그 주가 끝나면 달라진다. **기준 종가는 마지막 완료 거래일 2026-09-15의 $108.09**를 쓴다.
    - **현재가와 가장 가까운 지지가 54% 아래에 있다** — 위 §2에서 설명한 대로 급등 구간에 스윙 저점이 쌓이지 않은 결과이며, 이 문서의 지지 레벨을 근시일 판단에 쓰기 어려운 이유다.
    - 원주가 기준이라 **배당은 반영되지 않았다**(기간 내 배당 20회). 5년처럼 긴 구간에서는 이 누락이 작지 않다.

---

*작성일: 2026-09-16*
