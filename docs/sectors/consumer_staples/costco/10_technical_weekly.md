# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉으로 여러 사이클에 걸친 구조적 지지/저항을 본다. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-15 종가 $901.35**는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)와 일치한다(2026-09-15는 주 중간이라 주봉 데이터로는 직접 대조되지 않아 일봉으로 확인했다).
- ⚠️ **마지막 주봉은 미완성이다.** 생성 시점(2026-09-16 미 동부 10:01)이 해당 주의 거래 중이라 마지막 캔들은 아직 마감되지 않았다(§4 참고).

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-16)

<style>
.cost-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .cost-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cost-chart svg { width:100%; height:auto; display:block; }
.cost-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cost-chart .title { fill: var(--ink); font-weight:600; }
.cost-chart .grid { stroke: var(--grid); stroke-width:1; }
.cost-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="cost-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코스트코(COST) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코스트코 (COST) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-16 · 마지막 종가 $898.49 (2026-09-16) · 단위 USD</text>
<line x1="60" y1="610.6" x2="1052" y2="610.6" class="grid"/>
<text x="52" y="614.6" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="533.6" x2="1052" y2="533.6" class="grid"/>
<text x="52" y="537.6" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="456.5" x2="1052" y2="456.5" class="grid"/>
<text x="52" y="460.5" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="379.5" x2="1052" y2="379.5" class="grid"/>
<text x="52" y="383.5" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="302.5" x2="1052" y2="302.5" class="grid"/>
<text x="52" y="306.5" font-size="11" text-anchor="end" fill="var(--muted)">800</text>
<line x1="60" y1="225.5" x2="1052" y2="225.5" class="grid"/>
<text x="52" y="229.5" font-size="11" text-anchor="end" fill="var(--muted)">900</text>
<line x1="60" y1="148.4" x2="1052" y2="148.4" class="grid"/>
<text x="52" y="152.4" font-size="11" text-anchor="end" fill="var(--muted)">1,000</text>
<line x1="60" y1="71.4" x2="1052" y2="71.4" class="grid"/>
<text x="52" y="75.4" font-size="11" text-anchor="end" fill="var(--muted)">1,100</text>
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
<line x1="61.9" y1="561.5" x2="61.9" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="563.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="65.7" y1="557.7" x2="65.7" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="558.4" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="69.4" y1="556.3" x2="69.4" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="560.1" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="73.2" y1="564.7" x2="73.2" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="570.7" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="77.0" y1="569.0" x2="77.0" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="570.2" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="80.7" y1="545.1" x2="80.7" y2="573.2" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="547.4" width="2.34" height="24.9" fill="var(--up)"/>
<line x1="84.5" y1="538.1" x2="84.5" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="540.1" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="88.3" y1="518.0" x2="88.3" y2="543.4" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="523.5" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="92.1" y1="518.4" x2="92.1" y2="533.4" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="520.3" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="95.8" y1="506.4" x2="95.8" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="507.5" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="99.6" y1="491.5" x2="99.6" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="498.0" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="103.4" y1="486.8" x2="103.4" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="498.0" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="107.1" y1="486.4" x2="107.1" y2="515.2" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="488.3" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="110.9" y1="482.3" x2="110.9" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="494.7" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="114.7" y1="493.0" x2="114.7" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="494.8" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="118.5" y1="478.5" x2="118.5" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="481.4" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="122.2" y1="480.6" x2="122.2" y2="507.2" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="483.5" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="126.0" y1="510.1" x2="126.0" y2="532.1" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="511.0" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="129.8" y1="533.7" x2="129.8" y2="548.0" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="537.8" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="133.6" y1="536.8" x2="133.6" y2="557.4" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="539.4" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="137.3" y1="513.2" x2="137.3" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="518.3" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="141.1" y1="507.2" x2="141.1" y2="527.9" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="517.2" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="144.9" y1="519.5" x2="144.9" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="523.8" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="148.6" y1="519.5" x2="148.6" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="520.1" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="152.4" y1="503.6" x2="152.4" y2="524.9" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="513.9" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="156.2" y1="498.7" x2="156.2" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="512.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="160.0" y1="485.4" x2="160.0" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="486.3" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="163.7" y1="482.2" x2="163.7" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="487.2" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="167.5" y1="467.1" x2="167.5" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="475.4" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="171.3" y1="447.1" x2="171.3" y2="479.4" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="456.5" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="175.0" y1="455.8" x2="175.0" y2="472.9" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="457.5" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="178.8" y1="449.5" x2="178.8" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="467.8" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="182.6" y1="479.4" x2="182.6" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="479.4" width="2.34" height="29.7" fill="var(--down)"/>
<line x1="186.4" y1="498.0" x2="186.4" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="508.7" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="190.1" y1="525.4" x2="190.1" y2="549.2" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="535.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="193.9" y1="535.4" x2="193.9" y2="605.6" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="536.5" width="2.34" height="61.4" fill="var(--down)"/>
<line x1="197.7" y1="552.9" x2="197.7" y2="597.8" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="556.1" width="2.34" height="39.1" fill="var(--up)"/>
<line x1="201.4" y1="540.4" x2="201.4" y2="566.9" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="551.9" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="205.2" y1="545.7" x2="205.2" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="548.6" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="209.0" y1="561.0" x2="209.0" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="572.1" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="212.8" y1="545.3" x2="212.8" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="545.6" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="216.5" y1="540.3" x2="216.5" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="544.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="220.3" y1="529.3" x2="220.3" y2="550.2" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="532.4" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="224.1" y1="514.5" x2="224.1" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="515.9" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="227.8" y1="505.0" x2="227.8" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="510.7" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="231.6" y1="501.1" x2="231.6" y2="526.8" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="501.8" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="235.4" y1="493.0" x2="235.4" y2="507.9" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="501.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="239.2" y1="495.1" x2="239.2" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="499.8" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="242.9" y1="483.7" x2="242.9" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="491.6" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="246.7" y1="492.7" x2="246.7" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="492.7" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="250.5" y1="505.8" x2="250.5" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="512.7" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="254.3" y1="504.3" x2="254.3" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="505.4" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="258.0" y1="500.8" x2="258.0" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="504.5" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="261.8" y1="528.4" x2="261.8" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="531.9" width="2.34" height="27.5" fill="var(--down)"/>
<line x1="265.6" y1="540.1" x2="265.6" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="554.9" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="269.3" y1="538.3" x2="269.3" y2="559.7" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="553.2" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="273.1" y1="549.2" x2="273.1" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="556.9" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="276.9" y1="549.3" x2="276.9" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="550.4" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="280.7" y1="523.7" x2="280.7" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="525.2" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="284.4" y1="526.1" x2="284.4" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="526.1" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="288.2" y1="520.6" x2="288.2" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="521.7" width="2.34" height="29.6" fill="var(--up)"/>
<line x1="292.0" y1="510.6" x2="292.0" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="515.3" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="295.7" y1="505.2" x2="295.7" y2="516.6" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="507.6" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="299.5" y1="500.8" x2="299.5" y2="539.6" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="509.8" width="2.34" height="28.0" fill="var(--down)"/>
<line x1="303.3" y1="539.2" x2="303.3" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="539.3" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="307.1" y1="535.1" x2="307.1" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="546.9" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="310.8" y1="561.5" x2="310.8" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="562.3" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="314.6" y1="560.8" x2="314.6" y2="571.5" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="561.0" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="318.4" y1="545.6" x2="318.4" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="546.8" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="322.1" y1="543.7" x2="322.1" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="544.9" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="325.9" y1="540.9" x2="325.9" y2="558.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="545.0" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="329.7" y1="526.6" x2="329.7" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="531.0" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="333.5" y1="510.4" x2="333.5" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="522.2" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="337.2" y1="519.7" x2="337.2" y2="537.1" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="522.4" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="341.0" y1="524.8" x2="341.0" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="527.8" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="344.8" y1="529.4" x2="344.8" y2="545.4" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="532.9" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="348.5" y1="539.0" x2="348.5" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="539.3" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="352.3" y1="537.3" x2="352.3" y2="557.9" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="551.7" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="356.1" y1="541.3" x2="356.1" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="543.5" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="359.9" y1="536.2" x2="359.9" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="537.2" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="363.6" y1="533.7" x2="363.6" y2="544.8" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="535.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="367.4" y1="530.4" x2="367.4" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="536.3" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="371.2" y1="533.3" x2="371.2" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="540.3" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="375.0" y1="525.4" x2="375.0" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="528.7" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="378.7" y1="523.5" x2="378.7" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="528.9" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="382.5" y1="533.5" x2="382.5" y2="544.4" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="534.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="386.3" y1="528.9" x2="386.3" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="530.4" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="390.0" y1="529.7" x2="390.0" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="530.5" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="393.8" y1="525.3" x2="393.8" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="528.0" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="397.6" y1="519.3" x2="397.6" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="523.9" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="401.4" y1="516.6" x2="401.4" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="520.3" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="405.1" y1="509.5" x2="405.1" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="515.4" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="408.9" y1="514.0" x2="408.9" y2="520.8" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="514.7" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="412.7" y1="503.1" x2="412.7" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="504.0" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="416.4" y1="498.1" x2="416.4" y2="514.6" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="504.9" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="420.2" y1="497.5" x2="420.2" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="497.6" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="424.0" y1="485.8" x2="424.0" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="489.0" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="427.8" y1="478.8" x2="427.8" y2="490.5" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="484.8" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="431.5" y1="484.0" x2="431.5" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="485.0" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="435.3" y1="480.3" x2="435.3" y2="493.6" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="485.1" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="439.1" y1="481.4" x2="439.1" y2="500.4" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="483.7" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="442.8" y1="498.8" x2="442.8" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="499.8" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="446.6" y1="492.4" x2="446.6" y2="508.1" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="499.5" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="450.4" y1="493.2" x2="450.4" y2="502.6" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="494.1" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="454.2" y1="482.2" x2="454.2" y2="493.6" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="490.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="457.9" y1="480.2" x2="457.9" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="488.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="461.7" y1="478.0" x2="461.7" y2="499.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="483.5" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="465.5" y1="474.9" x2="465.5" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="481.3" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="469.2" y1="480.3" x2="469.2" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="482.1" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="473.0" y1="474.0" x2="473.0" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="479.9" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="476.8" y1="489.7" x2="476.8" y2="502.6" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="491.9" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="480.6" y1="485.0" x2="480.6" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="486.7" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="484.3" y1="473.6" x2="484.3" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="474.2" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="488.1" y1="456.6" x2="488.1" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="474.1" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="491.9" y1="461.0" x2="491.9" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="463.2" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="495.7" y1="456.6" x2="495.7" y2="469.8" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="459.4" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="499.4" y1="446.1" x2="499.4" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="448.2" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="503.2" y1="408.9" x2="503.2" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="411.2" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="507.0" y1="393.4" x2="507.0" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="401.4" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="510.7" y1="398.1" x2="510.7" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="400.3" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="514.5" y1="410.6" x2="514.5" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="413.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="518.3" y1="392.1" x2="518.3" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="392.4" width="2.34" height="21.1" fill="var(--up)"/>
<line x1="522.1" y1="382.5" x2="522.1" y2="396.3" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="383.4" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="525.8" y1="380.5" x2="525.8" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="383.0" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="529.6" y1="368.5" x2="529.6" y2="390.1" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="372.2" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="533.4" y1="357.8" x2="533.4" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="361.5" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="537.1" y1="357.1" x2="537.1" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="361.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="540.9" y1="346.8" x2="540.9" y2="363.9" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="350.3" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="544.7" y1="339.0" x2="544.7" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="341.4" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="548.5" y1="312.4" x2="548.5" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="337.1" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="552.2" y1="348.2" x2="552.2" y2="371.0" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="359.8" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="556.0" y1="339.2" x2="556.0" y2="359.5" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="352.7" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="559.8" y1="351.9" x2="559.8" y2="358.9" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="354.4" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="563.5" y1="353.9" x2="563.5" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="355.0" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="567.3" y1="353.5" x2="567.3" y2="374.1" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="355.4" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="571.1" y1="347.9" x2="571.1" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="352.2" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="574.9" y1="355.7" x2="574.9" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="357.0" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="578.6" y1="342.9" x2="578.6" y2="367.7" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="345.7" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="582.4" y1="312.2" x2="582.4" y2="343.7" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="312.4" width="2.34" height="29.0" fill="var(--up)"/>
<line x1="586.2" y1="299.0" x2="586.2" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="305.7" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="589.9" y1="289.5" x2="589.9" y2="308.6" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="295.0" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="593.7" y1="287.5" x2="593.7" y2="311.6" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="294.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="597.5" y1="263.7" x2="597.5" y2="297.0" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="267.4" width="2.34" height="26.6" fill="var(--up)"/>
<line x1="601.3" y1="259.2" x2="601.3" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="259.6" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="605.0" y1="245.5" x2="605.0" y2="265.8" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="260.5" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="608.8" y1="256.5" x2="608.8" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="264.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="612.6" y1="235.5" x2="612.6" y2="271.3" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="236.5" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="616.3" y1="228.0" x2="616.3" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="235.6" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="620.1" y1="257.9" x2="620.1" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="266.4" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="623.9" y1="260.4" x2="623.9" y2="295.5" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="267.2" width="2.34" height="21.7" fill="var(--down)"/>
<line x1="627.7" y1="279.2" x2="627.7" y2="300.0" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="285.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="631.4" y1="258.0" x2="631.4" y2="307.9" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="260.2" width="2.34" height="43.9" fill="var(--up)"/>
<line x1="635.2" y1="240.6" x2="635.2" y2="262.1" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="248.1" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="639.0" y1="232.3" x2="639.0" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="241.5" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="642.8" y1="210.9" x2="642.8" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="231.3" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="646.5" y1="227.9" x2="646.5" y2="249.6" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="228.0" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="650.3" y1="207.1" x2="650.3" y2="242.5" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="213.1" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="654.1" y1="208.0" x2="654.1" y2="232.4" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="208.5" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="657.8" y1="210.4" x2="657.8" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="220.1" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="661.6" y1="217.8" x2="661.6" y2="250.8" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="232.1" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="665.4" y1="217.8" x2="665.4" y2="246.8" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="233.9" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="669.2" y1="225.0" x2="669.2" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="231.3" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="672.9" y1="221.1" x2="672.9" y2="238.0" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="232.2" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="676.7" y1="228.5" x2="676.7" y2="250.6" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="228.5" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="680.5" y1="177.7" x2="680.5" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="191.7" width="2.34" height="48.1" fill="var(--up)"/>
<line x1="684.2" y1="186.0" x2="684.2" y2="221.2" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="191.7" width="2.34" height="28.3" fill="var(--down)"/>
<line x1="688.0" y1="166.7" x2="688.0" y2="220.0" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="176.2" width="2.34" height="41.1" fill="var(--up)"/>
<line x1="691.8" y1="167.7" x2="691.8" y2="187.2" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="167.7" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="695.6" y1="150.2" x2="695.6" y2="175.6" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="154.1" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="699.3" y1="142.4" x2="699.3" y2="174.8" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="150.7" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="703.1" y1="142.1" x2="703.1" y2="192.3" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="156.9" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="706.9" y1="179.7" x2="706.9" y2="200.8" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="184.0" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="710.6" y1="199.1" x2="710.6" y2="223.9" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="201.6" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="714.4" y1="191.4" x2="714.4" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="197.0" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="718.2" y1="191.7" x2="718.2" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="192.2" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="722.0" y1="181.9" x2="722.0" y2="199.6" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="190.6" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="725.7" y1="155.4" x2="725.7" y2="204.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="163.9" width="2.34" height="38.4" fill="var(--up)"/>
<line x1="729.5" y1="99.9" x2="729.5" y2="172.4" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="114.7" width="2.34" height="55.0" fill="var(--up)"/>
<line x1="733.3" y1="88.2" x2="733.3" y2="113.0" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="93.1" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="737.0" y1="93.7" x2="737.0" y2="129.4" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="95.1" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="740.8" y1="103.1" x2="740.8" y2="133.9" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="111.0" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="744.6" y1="97.6" x2="744.6" y2="192.5" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="108.6" width="2.34" height="67.3" fill="var(--down)"/>
<line x1="748.4" y1="179.5" x2="748.4" y2="239.7" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="182.7" width="2.34" height="39.7" fill="var(--down)"/>
<line x1="752.1" y1="207.4" x2="752.1" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="218.3" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="755.9" y1="192.4" x2="755.9" y2="210.1" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="202.6" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="759.7" y1="152.3" x2="759.7" y2="214.6" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="208.2" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="763.5" y1="153.5" x2="763.5" y2="247.3" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="176.6" width="2.34" height="58.3" fill="var(--up)"/>
<line x1="767.2" y1="148.5" x2="767.2" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="152.7" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="771.0" y1="150.8" x2="771.0" y2="192.4" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="153.8" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="774.8" y1="134.6" x2="774.8" y2="172.5" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="142.0" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="778.5" y1="134.7" x2="778.5" y2="155.1" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="142.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="782.3" y1="126.7" x2="782.3" y2="161.5" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="128.5" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="786.1" y1="118.0" x2="786.1" y2="143.0" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="134.1" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="789.9" y1="108.0" x2="789.9" y2="146.9" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="117.5" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="793.6" y1="96.8" x2="793.6" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="122.0" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="797.4" y1="138.1" x2="797.4" y2="157.2" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="138.9" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="801.2" y1="147.0" x2="801.2" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="154.3" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="804.9" y1="143.9" x2="804.9" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="159.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="808.7" y1="150.9" x2="808.7" y2="168.1" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="158.4" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="812.5" y1="151.6" x2="812.5" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="160.0" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="816.3" y1="162.7" x2="816.3" y2="188.9" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="170.7" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="820.0" y1="181.0" x2="820.0" y2="199.7" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="185.8" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="823.8" y1="181.8" x2="823.8" y2="206.2" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="185.0" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="827.6" y1="157.5" x2="827.6" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="163.1" width="2.34" height="21.9" fill="var(--up)"/>
<line x1="831.3" y1="154.8" x2="831.3" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="161.4" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="835.1" y1="149.0" x2="835.1" y2="184.6" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="169.0" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="838.9" y1="180.6" x2="838.9" y2="199.8" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="183.1" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="842.7" y1="171.9" x2="842.7" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="176.6" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="846.4" y1="163.1" x2="846.4" y2="183.9" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="173.2" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="850.2" y1="171.7" x2="850.2" y2="191.7" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="173.2" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="854.0" y1="184.1" x2="854.0" y2="221.6" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="189.0" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="857.7" y1="202.0" x2="857.7" y2="222.9" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="212.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="861.5" y1="190.5" x2="861.5" y2="222.5" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="202.3" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="865.3" y1="176.2" x2="865.3" y2="209.2" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="197.5" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="869.1" y1="184.6" x2="869.1" y2="202.2" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="197.6" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="872.8" y1="199.9" x2="872.8" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="202.2" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="876.6" y1="190.6" x2="876.6" y2="219.1" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="207.9" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="880.4" y1="203.2" x2="880.4" y2="218.5" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="207.8" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="884.2" y1="206.3" x2="884.2" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="208.5" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="887.9" y1="214.5" x2="887.9" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="215.0" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="891.7" y1="205.2" x2="891.7" y2="234.6" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="215.3" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="895.5" y1="230.1" x2="895.5" y2="250.8" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="230.5" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="899.2" y1="235.1" x2="899.2" y2="268.5" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="239.2" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="903.0" y1="242.7" x2="903.0" y2="266.4" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="246.0" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="906.8" y1="245.1" x2="906.8" y2="262.0" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="246.0" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="910.6" y1="201.1" x2="910.6" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="206.3" width="2.34" height="46.9" fill="var(--up)"/>
<line x1="914.3" y1="175.4" x2="914.3" y2="212.4" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="176.5" width="2.34" height="33.3" fill="var(--up)"/>
<line x1="918.1" y1="156.4" x2="918.1" y2="183.8" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="161.3" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="921.9" y1="153.8" x2="921.9" y2="202.1" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="158.9" width="2.34" height="35.6" fill="var(--down)"/>
<line x1="925.6" y1="147.4" x2="925.6" y2="201.4" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="147.5" width="2.34" height="43.9" fill="var(--up)"/>
<line x1="929.4" y1="130.8" x2="929.4" y2="173.8" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="134.2" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="933.2" y1="126.5" x2="933.2" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="131.2" width="2.34" height="28.6" fill="var(--down)"/>
<line x1="937.0" y1="137.5" x2="937.0" y2="165.3" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="140.1" width="2.34" height="22.3" fill="var(--up)"/>
<line x1="940.7" y1="132.4" x2="940.7" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="140.0" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="944.5" y1="138.5" x2="944.5" y2="160.8" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="141.9" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="948.3" y1="138.7" x2="948.3" y2="171.2" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="140.3" width="2.34" height="29.4" fill="var(--down)"/>
<line x1="952.0" y1="158.3" x2="952.0" y2="178.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="159.5" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="955.8" y1="136.1" x2="955.8" y2="160.0" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="136.9" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="959.6" y1="120.8" x2="959.6" y2="151.9" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="136.9" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="963.4" y1="147.9" x2="963.4" y2="174.6" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="148.5" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="967.1" y1="135.6" x2="967.1" y2="158.7" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="139.8" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="970.9" y1="124.3" x2="970.9" y2="159.9" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="139.4" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="974.7" y1="129.4" x2="974.7" y2="155.6" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="141.7" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="978.4" y1="104.1" x2="978.4" y2="159.9" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="110.7" width="2.34" height="33.2" fill="var(--up)"/>
<line x1="982.2" y1="74.1" x2="982.2" y2="129.0" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="109.9" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="986.0" y1="127.2" x2="986.0" y2="190.5" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="128.3" width="2.34" height="53.8" fill="var(--down)"/>
<line x1="989.8" y1="150.4" x2="989.8" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="170.1" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="993.5" y1="156.8" x2="993.5" y2="178.5" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="162.0" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="997.3" y1="152.0" x2="997.3" y2="188.2" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="168.3" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="1001.1" y1="173.1" x2="1001.1" y2="195.7" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="185.0" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="1004.9" y1="171.6" x2="1004.9" y2="209.6" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="180.4" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="1008.6" y1="172.3" x2="1008.6" y2="219.9" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="187.6" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="1012.4" y1="175.9" x2="1012.4" y2="217.4" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="194.0" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="1016.2" y1="189.3" x2="1016.2" y2="212.5" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="195.6" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="1019.9" y1="158.0" x2="1019.9" y2="197.2" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="185.5" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="1023.7" y1="173.1" x2="1023.7" y2="198.3" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="175.3" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="1027.5" y1="175.1" x2="1027.5" y2="198.5" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="178.4" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="1031.3" y1="164.8" x2="1031.3" y2="205.6" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="183.2" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="1035.0" y1="168.1" x2="1035.0" y2="199.8" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="184.6" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="1038.8" y1="185.3" x2="1038.8" y2="214.3" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="190.7" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="1042.6" y1="213.8" x2="1042.6" y2="226.7" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="215.9" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="1046.3" y1="208.5" x2="1046.3" y2="225.3" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="214.9" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="1050.1" y1="223.9" x2="1050.1" y2="226.9" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="224.7" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="60" y1="149.7" x2="1052" y2="149.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="153.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$998 R1</text>
<text x="1058" y="165.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="123.7" x2="1052" y2="123.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="127.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,032 R2</text>
<text x="1058" y="139.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="86.3" x2="1052" y2="86.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="89.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,081 R3</text>
<text x="1058" y="101.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="249.0" x2="1052" y2="249.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="243.0" font-size="11.5" fill="var(--support)" font-weight="600">$869 S1</text>
<text x="1058" y="255.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="506.3" x2="1052" y2="506.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="500.3" font-size="11.5" fill="var(--support)" font-weight="600">$535 S2</text>
<text x="1058" y="512.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="556.4" x2="1052" y2="556.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="550.4" font-size="11.5" fill="var(--support)" font-weight="600">$470 S3</text>
<text x="1058" y="562.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="226.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="218.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $898 (2026-09-16)</text>
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
| R3 | $1,081 | 3 | 2025-02-10·2025-06-02·2026-05-18 — **5년 최고가($1,096.50) 바로 아래 고점대**. 세 번 모두 돌파에 실패했다 |
| R2 | $1,032 | 2 | 2026-02-16·2026-04-06 — 2026년 상반기 고점대 |
| R1 | $998 | 3 | 2024-12-16·2025-08-18·2026-07-27 — **$1,000 선**이 2년에 걸쳐 세 번 저항으로 작동했다 |
| **현재가** | **$901.35** (2026-09-15 종가) | — | R1 바로 아래. 5년 최고 대비 −17.8% |
| S1 | $869 | 2 | 2024-09-30·2025-04-07 — 현재가에 가장 근접한 지지이며, 일봉의 S1($848)과 함께 $848~$869 구간을 이룬다 |
| S2 | $535 | 2 | 2023-08-21·2023-10-23 — **2023년 가격대**로 현재가보다 41% 아래다. 구조적 참고선일 뿐 근시일 지지로 보지 않는다 |
| S3 | $470 | 3 | 2022-01-24·2023-02-27·2023-05-22 — 2022~2023년 가격대. S2와 같은 이유로 참고선 성격이다 |

**이 표에서 실질적으로 유효한 것은 R1·S1 두 개다.** S2($535)·S3($470)는 5년 창의 앞쪽 절반, 즉 **PER이 30배대이던 시절의 가격대**라 지금의 밸류에이션 구조와 연결되지 않는다 — 주가가 그 수준으로 돌아가려면 배수가 절반이 되어야 하며, 그것은 기술적 지지의 문제가 아니라 [밸류에이션](./06_valuation.md)의 문제다.

**5년 구조는 "계단식 상승 후 첫 횡보"로 읽힌다.** $470(2022) → $535(2023) → $869(2024~25) → $998~$1,081(2025~26)로 지지대가 차례로 올라섰고, 2025년 이후로는 $998(R1)을 세 번 뚫지 못한 채 $869~$1,081 구간에 머물러 있다. 현재가 $901.35는 그 구간의 하단부다.

---


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-16. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py COST --name "코스트코" --interval 1wk --close-on 2026-09-15 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - ⚠️ **마지막 주봉은 미완성이다.** 이 스크립트는 시계열 종료일을 고정하는 인자가 없어 항상 가장 최근 봉까지 그린다. 생성 시점이 해당 주의 거래 중(2026-09-16 미 동부 10:01, 정규장)이었으므로 마지막 캔들의 고가·저가·종가는 그 주가 끝나면 달라진다. **기준 종가는 마지막 완료 거래일 2026-09-15의 $901.35**를 쓴다.
    - 원주가 기준이라 **배당은 반영되지 않았다**(기간 내 배당 21회). 5년처럼 긴 구간에서는 이 누락이 작지 않아, 총수익률 기준 성과는 이 차트보다 눈에 띄게 높다.
    - S2·S3는 현재가 대비 41~48% 아래로 **밸류에이션 구조가 달랐던 시기의 가격대**다 — 위 §2 서술 참고.
    - 코스트코는 2000-01 이후 주식분할이 없어 가격 연속성을 깨는 이벤트가 없다.

---

*작성일: 2026-09-16*
