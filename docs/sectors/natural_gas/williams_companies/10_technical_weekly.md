# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉으로 다년 가격 구조를 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-17 종가 $71.81은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[일봉 차트](./09_technical_daily.md)와 모두 일치**한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-17)

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
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Williams Companies(WMB) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Williams Companies (WMB) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-17 · 마지막 종가 $71.81 (2026-09-17) · 단위 USD</text>
<line x1="60" y1="550.0" x2="1052" y2="550.0" class="grid"/>
<text x="52" y="554.0" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="455.0" x2="1052" y2="455.0" class="grid"/>
<text x="52" y="459.0" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="360.0" x2="1052" y2="360.0" class="grid"/>
<text x="52" y="364.0" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="265.0" x2="1052" y2="265.0" class="grid"/>
<text x="52" y="269.0" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="170.0" x2="1052" y2="170.0" class="grid"/>
<text x="52" y="174.0" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="75.0" x2="1052" y2="75.0" class="grid"/>
<text x="52" y="79.0" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
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
<line x1="61.9" y1="591.5" x2="61.9" y2="595.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="594.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="65.7" y1="591.7" x2="65.7" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="593.7" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="69.4" y1="582.2" x2="69.4" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="584.2" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="73.2" y1="565.7" x2="73.2" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="566.0" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="77.0" y1="552.4" x2="77.0" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="554.3" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="80.7" y1="551.0" x2="80.7" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="552.5" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="84.5" y1="559.6" x2="84.5" y2="569.6" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="561.5" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="88.3" y1="560.2" x2="88.3" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="563.7" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="92.1" y1="559.5" x2="92.1" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="562.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="95.8" y1="561.2" x2="95.8" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="562.9" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="99.6" y1="563.5" x2="99.6" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="566.7" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="103.4" y1="562.7" x2="103.4" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="563.5" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="107.1" y1="568.7" x2="107.1" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="574.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="110.9" y1="582.5" x2="110.9" y2="594.0" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="583.4" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="114.7" y1="587.8" x2="114.7" y2="598.8" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="589.4" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="118.5" y1="584.2" x2="118.5" y2="591.6" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="587.6" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="122.2" y1="568.4" x2="122.2" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="568.9" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="126.0" y1="555.5" x2="126.0" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="556.7" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="129.8" y1="551.5" x2="129.8" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="555.0" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="133.6" y1="550.8" x2="133.6" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="553.4" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="137.3" y1="541.3" x2="137.3" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="544.5" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="141.1" y1="540.3" x2="141.1" y2="550.0" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="543.3" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="144.9" y1="543.0" x2="144.9" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="543.3" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="148.6" y1="542.9" x2="148.6" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="542.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="152.4" y1="516.5" x2="152.4" y2="546.3" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="517.0" width="2.34" height="28.3" fill="var(--up)"/>
<line x1="156.2" y1="508.3" x2="156.2" y2="533.1" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="514.6" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="160.0" y1="532.2" x2="160.0" y2="546.6" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="535.0" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="163.7" y1="512.9" x2="163.7" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="513.1" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="167.5" y1="511.8" x2="167.5" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="513.6" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="171.3" y1="507.1" x2="171.3" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="508.0" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="175.0" y1="494.9" x2="175.0" y2="513.0" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="497.6" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="178.8" y1="489.5" x2="178.8" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="496.9" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="182.6" y1="501.8" x2="182.6" y2="521.3" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="508.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="186.4" y1="483.0" x2="186.4" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="486.6" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="190.1" y1="491.3" x2="190.1" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="492.8" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="193.9" y1="491.4" x2="193.9" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="498.9" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="197.7" y1="477.8" x2="197.7" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="479.1" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="201.4" y1="474.3" x2="201.4" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="476.8" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="205.2" y1="474.9" x2="205.2" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="477.3" width="2.34" height="26.2" fill="var(--down)"/>
<line x1="209.0" y1="510.7" x2="209.0" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="511.6" width="2.34" height="40.9" fill="var(--down)"/>
<line x1="212.8" y1="539.4" x2="212.8" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="546.9" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="216.5" y1="529.0" x2="216.5" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="537.7" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="220.3" y1="533.8" x2="220.3" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="537.5" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="224.1" y1="532.1" x2="224.1" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="536.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="227.8" y1="522.5" x2="227.8" y2="536.7" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="527.8" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="231.6" y1="508.8" x2="231.6" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="511.1" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="235.4" y1="508.9" x2="235.4" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="514.2" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="239.2" y1="510.1" x2="239.2" y2="528.9" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="510.5" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="242.9" y1="498.9" x2="242.9" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="503.2" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="246.7" y1="495.0" x2="246.7" y2="507.7" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="502.2" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="250.5" y1="496.8" x2="250.5" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="502.5" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="254.3" y1="512.0" x2="254.3" y2="535.0" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="512.7" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="258.0" y1="512.7" x2="258.0" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="520.6" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="261.8" y1="526.6" x2="261.8" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="539.5" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="265.6" y1="554.7" x2="265.6" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="560.0" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="269.3" y1="542.2" x2="269.3" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="552.0" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="273.1" y1="543.5" x2="273.1" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="551.0" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="276.9" y1="533.3" x2="276.9" y2="553.0" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="535.6" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="280.7" y1="522.5" x2="280.7" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="524.6" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="284.4" y1="513.5" x2="284.4" y2="526.7" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="516.4" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="288.2" y1="509.7" x2="288.2" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="511.2" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="292.0" y1="507.0" x2="292.0" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="511.2" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="295.7" y1="509.1" x2="295.7" y2="527.8" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="512.9" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="299.5" y1="498.1" x2="299.5" y2="519.7" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="502.9" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="303.3" y1="500.4" x2="303.3" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="501.0" width="2.34" height="24.4" fill="var(--down)"/>
<line x1="307.1" y1="510.2" x2="307.1" y2="532.8" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="524.2" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="310.8" y1="517.6" x2="310.8" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="518.5" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="314.6" y1="516.4" x2="314.6" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="517.8" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="318.4" y1="522.3" x2="318.4" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="524.3" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="322.1" y1="520.8" x2="322.1" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="522.2" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="325.9" y1="520.7" x2="325.9" y2="537.0" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="521.9" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="329.7" y1="525.8" x2="329.7" y2="545.2" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="534.2" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="333.5" y1="526.8" x2="333.5" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="530.2" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="337.2" y1="528.8" x2="337.2" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="530.8" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="341.0" y1="527.1" x2="341.0" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="534.0" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="344.8" y1="537.6" x2="344.8" y2="545.5" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="538.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="348.5" y1="538.3" x2="348.5" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="540.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="352.3" y1="540.3" x2="352.3" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="542.3" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="356.1" y1="553.0" x2="356.1" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="564.2" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="359.9" y1="556.2" x2="359.9" y2="570.9" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="562.0" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="363.6" y1="551.1" x2="363.6" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="551.3" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="367.4" y1="546.1" x2="367.4" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="547.1" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="371.2" y1="542.6" x2="371.2" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="546.3" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="375.0" y1="544.6" x2="375.0" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="545.2" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="378.7" y1="545.8" x2="378.7" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="547.5" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="382.5" y1="545.2" x2="382.5" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="548.3" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="386.3" y1="545.4" x2="386.3" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="545.8" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="390.0" y1="554.8" x2="390.0" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="556.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="393.8" y1="553.8" x2="393.8" y2="563.0" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="557.7" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="397.6" y1="545.0" x2="397.6" y2="566.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="547.8" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="401.4" y1="533.7" x2="401.4" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="544.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="405.1" y1="540.6" x2="405.1" y2="549.0" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="545.0" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="408.9" y1="540.1" x2="408.9" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="544.4" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="412.7" y1="523.8" x2="412.7" y2="544.4" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="525.0" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="416.4" y1="521.0" x2="416.4" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="524.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="420.2" y1="509.2" x2="420.2" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="517.9" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="424.0" y1="512.3" x2="424.0" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="513.4" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="427.8" y1="508.1" x2="427.8" y2="514.9" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="511.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="431.5" y1="501.8" x2="431.5" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="508.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="435.3" y1="498.1" x2="435.3" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="498.9" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="439.1" y1="498.5" x2="439.1" y2="509.4" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="498.8" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="442.8" y1="501.2" x2="442.8" y2="510.5" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="504.2" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="446.6" y1="501.5" x2="446.6" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="504.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="450.4" y1="503.7" x2="450.4" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="505.3" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="454.2" y1="504.0" x2="454.2" y2="516.3" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="508.8" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="457.9" y1="505.4" x2="457.9" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="507.4" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="461.7" y1="505.7" x2="461.7" y2="516.8" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="514.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="465.5" y1="513.0" x2="465.5" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="515.0" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="469.2" y1="498.7" x2="469.2" y2="511.7" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="500.7" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="473.0" y1="490.9" x2="473.0" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="498.6" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="476.8" y1="502.0" x2="476.8" y2="513.0" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="505.6" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="480.6" y1="491.0" x2="480.6" y2="514.6" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="492.2" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="484.3" y1="490.0" x2="484.3" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="490.5" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="488.1" y1="495.2" x2="488.1" y2="506.0" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="498.4" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="491.9" y1="488.3" x2="491.9" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="490.0" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="495.7" y1="479.2" x2="495.7" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="480.8" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="499.4" y1="480.5" x2="499.4" y2="506.0" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="483.5" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="503.2" y1="498.1" x2="503.2" y2="511.9" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="498.5" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="507.0" y1="498.9" x2="507.0" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="501.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="498.9" x2="510.7" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="500.3" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="514.5" y1="486.4" x2="514.5" y2="503.1" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="497.3" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="518.3" y1="496.1" x2="518.3" y2="508.4" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="500.6" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="522.1" y1="503.1" x2="522.1" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="504.2" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="525.8" y1="503.4" x2="525.8" y2="515.2" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="503.7" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="529.6" y1="498.8" x2="529.6" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="504.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="533.4" y1="505.3" x2="533.4" y2="513.4" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="506.7" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="537.1" y1="505.4" x2="537.1" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="509.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="540.9" y1="499.7" x2="540.9" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="503.1" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="544.7" y1="489.1" x2="544.7" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="489.2" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="548.5" y1="482.5" x2="548.5" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="489.2" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="552.2" y1="480.1" x2="552.2" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="483.5" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="556.0" y1="466.8" x2="556.0" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="471.6" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="559.8" y1="463.6" x2="559.8" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="464.8" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="563.5" y1="457.3" x2="563.5" y2="468.6" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="462.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="567.3" y1="460.5" x2="567.3" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="461.4" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="571.1" y1="468.7" x2="571.1" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="469.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="574.9" y1="459.6" x2="574.9" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="462.0" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="578.6" y1="459.2" x2="578.6" y2="476.9" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="460.6" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="582.4" y1="455.1" x2="582.4" y2="468.0" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="458.4" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="586.2" y1="442.2" x2="586.2" y2="459.1" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="442.9" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="589.9" y1="437.0" x2="589.9" y2="456.1" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="442.6" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="593.7" y1="440.2" x2="593.7" y2="454.4" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="440.7" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="597.5" y1="439.3" x2="597.5" y2="449.4" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="441.1" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="601.3" y1="438.1" x2="601.3" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="443.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="605.0" y1="424.6" x2="605.0" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="435.4" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="608.8" y1="424.4" x2="608.8" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="431.2" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="612.6" y1="426.1" x2="612.6" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="429.4" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="616.3" y1="424.5" x2="616.3" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="426.7" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="620.1" y1="415.3" x2="620.1" y2="433.6" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="417.0" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="623.9" y1="406.6" x2="623.9" y2="438.8" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="416.0" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="627.7" y1="421.8" x2="627.7" y2="439.0" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="429.9" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="631.4" y1="414.2" x2="631.4" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="424.0" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="635.2" y1="414.5" x2="635.2" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="415.8" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="639.0" y1="404.2" x2="639.0" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="404.7" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="642.8" y1="399.8" x2="642.8" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="400.2" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="646.5" y1="400.9" x2="646.5" y2="416.1" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="403.1" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="650.3" y1="403.9" x2="650.3" y2="417.2" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="407.2" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="654.1" y1="399.7" x2="654.1" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="403.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="657.8" y1="393.4" x2="657.8" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="403.3" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="661.6" y1="363.1" x2="661.6" y2="409.6" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="363.5" width="2.34" height="42.6" fill="var(--up)"/>
<line x1="665.4" y1="355.0" x2="665.4" y2="374.2" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="355.4" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="669.2" y1="336.8" x2="669.2" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="337.6" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="672.9" y1="332.9" x2="672.9" y2="343.9" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="336.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="676.7" y1="333.0" x2="676.7" y2="346.1" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="341.0" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="680.5" y1="295.4" x2="680.5" y2="345.9" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="300.1" width="2.34" height="44.5" fill="var(--up)"/>
<line x1="684.2" y1="290.4" x2="684.2" y2="310.6" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="296.4" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="688.0" y1="261.6" x2="688.0" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="268.3" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="691.8" y1="265.9" x2="691.8" y2="294.1" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="266.8" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="695.6" y1="277.4" x2="695.6" y2="307.6" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="278.3" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="699.3" y1="293.5" x2="699.3" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="294.3" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="703.1" y1="318.0" x2="703.1" y2="342.0" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="318.2" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="706.9" y1="315.9" x2="706.9" y2="334.1" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="322.6" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="710.6" y1="294.5" x2="710.6" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="297.3" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="714.4" y1="291.1" x2="714.4" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="293.3" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="718.2" y1="268.8" x2="718.2" y2="307.9" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="273.2" width="2.34" height="33.9" fill="var(--up)"/>
<line x1="722.0" y1="251.1" x2="722.0" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="269.1" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="725.7" y1="285.2" x2="725.7" y2="331.1" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="285.4" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="729.5" y1="289.8" x2="729.5" y2="316.3" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="303.6" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="733.3" y1="284.9" x2="733.3" y2="329.9" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="293.7" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="737.0" y1="273.1" x2="737.0" y2="294.3" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="289.3" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="740.8" y1="278.4" x2="740.8" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="282.3" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="744.6" y1="274.1" x2="744.6" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="279.3" width="2.34" height="39.0" fill="var(--down)"/>
<line x1="748.4" y1="286.3" x2="748.4" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="290.9" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="752.1" y1="266.1" x2="752.1" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="268.8" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="755.9" y1="249.1" x2="755.9" y2="277.6" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="264.4" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="759.7" y1="249.3" x2="759.7" y2="326.3" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="277.3" width="2.34" height="39.2" fill="var(--down)"/>
<line x1="763.5" y1="289.4" x2="763.5" y2="345.0" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="299.3" width="2.34" height="35.6" fill="var(--up)"/>
<line x1="767.2" y1="264.9" x2="767.2" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="278.1" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="771.0" y1="264.0" x2="771.0" y2="307.2" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="274.2" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="774.8" y1="264.1" x2="774.8" y2="287.8" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="265.0" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="778.5" y1="261.1" x2="778.5" y2="294.8" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="269.4" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="782.3" y1="273.1" x2="782.3" y2="299.0" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="276.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="786.1" y1="272.9" x2="786.1" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="274.6" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="789.9" y1="256.7" x2="789.9" y2="269.8" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="260.2" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="793.6" y1="251.2" x2="793.6" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="254.0" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="797.4" y1="258.3" x2="797.4" y2="279.4" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="260.1" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="801.2" y1="258.7" x2="801.2" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="260.3" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="804.9" y1="234.8" x2="804.9" y2="264.9" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="239.6" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="808.7" y1="232.2" x2="808.7" y2="284.9" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="239.6" width="2.34" height="38.3" fill="var(--down)"/>
<line x1="812.5" y1="273.1" x2="812.5" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="277.9" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="816.3" y1="265.3" x2="816.3" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="271.2" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="820.0" y1="271.8" x2="820.0" y2="293.9" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="275.0" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="823.8" y1="258.3" x2="823.8" y2="291.3" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="262.4" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="827.6" y1="254.3" x2="827.6" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="259.4" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="831.3" y1="277.7" x2="831.3" y2="294.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="284.3" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="835.1" y1="283.2" x2="835.1" y2="304.7" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="292.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="838.9" y1="283.1" x2="838.9" y2="298.5" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="285.1" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="842.7" y1="278.4" x2="842.7" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="288.7" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="846.4" y1="271.2" x2="846.4" y2="298.6" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="276.3" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="850.2" y1="252.8" x2="850.2" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="264.0" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="854.0" y1="222.4" x2="854.0" y2="268.4" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="226.9" width="2.34" height="38.3" fill="var(--up)"/>
<line x1="857.7" y1="212.3" x2="857.7" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="222.4" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="861.5" y1="216.0" x2="861.5" y2="240.7" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="219.5" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="865.3" y1="224.2" x2="865.3" y2="248.2" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="239.2" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="869.1" y1="232.3" x2="869.1" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="240.2" width="2.34" height="48.7" fill="var(--down)"/>
<line x1="872.8" y1="281.6" x2="872.8" y2="298.0" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="285.2" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="876.6" y1="267.2" x2="876.6" y2="301.2" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="269.0" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="880.4" y1="252.3" x2="880.4" y2="275.6" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="255.6" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="884.2" y1="255.7" x2="884.2" y2="282.2" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="257.0" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="887.9" y1="254.4" x2="887.9" y2="278.3" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="256.2" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="891.7" y1="228.1" x2="891.7" y2="263.3" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="238.3" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="895.5" y1="240.1" x2="895.5" y2="273.8" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="241.1" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="899.2" y1="265.6" x2="899.2" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="268.3" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="903.0" y1="264.7" x2="903.0" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="269.6" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="906.8" y1="254.0" x2="906.8" y2="269.0" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="256.9" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="910.6" y1="249.2" x2="910.6" y2="279.3" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="251.7" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="914.3" y1="247.2" x2="914.3" y2="273.8" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="250.3" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="918.1" y1="216.1" x2="918.1" y2="251.3" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="217.9" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="921.9" y1="186.4" x2="921.9" y2="228.6" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="196.0" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="925.6" y1="180.0" x2="925.6" y2="212.3" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="199.3" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="929.4" y1="145.0" x2="929.4" y2="199.0" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="148.3" width="2.34" height="48.6" fill="var(--up)"/>
<line x1="933.2" y1="141.1" x2="933.2" y2="156.5" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="141.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="937.0" y1="116.9" x2="937.0" y2="152.5" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="125.2" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="940.7" y1="104.7" x2="940.7" y2="132.6" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="110.6" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="944.5" y1="119.3" x2="944.5" y2="146.2" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="134.9" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="948.3" y1="121.6" x2="948.3" y2="149.2" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="135.3" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="952.0" y1="119.0" x2="952.0" y2="151.0" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="136.0" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="955.8" y1="124.2" x2="955.8" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="130.2" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="959.6" y1="124.9" x2="959.6" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="144.0" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="963.4" y1="141.0" x2="963.4" y2="176.4" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="142.0" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="967.1" y1="148.6" x2="967.1" y2="172.7" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="149.3" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="970.9" y1="108.7" x2="970.9" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="117.4" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="974.7" y1="99.6" x2="974.7" y2="153.0" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="119.3" width="2.34" height="32.1" fill="var(--down)"/>
<line x1="978.4" y1="91.7" x2="978.4" y2="151.5" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="96.7" width="2.34" height="51.6" fill="var(--up)"/>
<line x1="982.2" y1="74.2" x2="982.2" y2="103.4" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="89.5" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="986.0" y1="89.5" x2="986.0" y2="158.5" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="91.6" width="2.34" height="65.2" fill="var(--down)"/>
<line x1="989.8" y1="144.1" x2="989.8" y2="169.9" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="151.4" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="993.5" y1="142.0" x2="993.5" y2="163.6" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="147.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="997.3" y1="138.8" x2="997.3" y2="169.8" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="140.4" width="2.34" height="25.6" fill="var(--up)"/>
<line x1="1001.1" y1="84.5" x2="1001.1" y2="144.7" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="94.8" width="2.34" height="48.1" fill="var(--up)"/>
<line x1="1004.9" y1="89.4" x2="1004.9" y2="150.0" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="97.7" width="2.34" height="42.5" fill="var(--down)"/>
<line x1="1008.6" y1="108.4" x2="1008.6" y2="147.2" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="122.3" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="1012.4" y1="109.8" x2="1012.4" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="118.3" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="1016.2" y1="109.0" x2="1016.2" y2="143.8" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="132.0" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="1019.9" y1="141.3" x2="1019.9" y2="176.9" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="143.2" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="1023.7" y1="139.3" x2="1023.7" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="163.8" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="1027.5" y1="120.2" x2="1027.5" y2="164.4" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="120.6" width="2.34" height="39.9" fill="var(--up)"/>
<line x1="1031.3" y1="114.1" x2="1031.3" y2="170.8" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="120.5" width="2.34" height="44.8" fill="var(--down)"/>
<line x1="1035.0" y1="117.5" x2="1035.0" y2="173.8" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="134.6" width="2.34" height="31.8" fill="var(--up)"/>
<line x1="1038.8" y1="110.0" x2="1038.8" y2="138.0" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="130.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1042.6" y1="104.8" x2="1042.6" y2="147.0" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="125.0" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="1046.3" y1="138.4" x2="1046.3" y2="171.4" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="146.2" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="1050.1" y1="149.1" x2="1050.1" y2="160.4" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="152.8" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="60" y1="79.4" x2="1052" y2="79.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="82.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$80 R1</text>
<text x="1058" y="94.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="176.8" x2="1052" y2="176.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="170.8" font-size="11.5" fill="var(--support)" font-weight="600">$69 S1</text>
<text x="1058" y="182.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="301.4" x2="1052" y2="301.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="295.4" font-size="11.5" fill="var(--support)" font-weight="600">$56 S2</text>
<text x="1058" y="307.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="337.9" x2="1052" y2="337.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="331.9" font-size="11.5" fill="var(--support)" font-weight="600">$52 S3</text>
<text x="1058" y="343.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="152.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="144.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $72 (2026-09-17)</text>
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
| R1 | $80 | 2 | 2026-05-18·06-22 주. 5년 전체의 최고 구간이며 52주 최고 $80.08이 여기 있다. 터치 2회로 표본이 얇다 |
| **현재가** | **$71.81** (2026-09-17 종가) | — | R1과 S1 사이 |
| S1 | $69 | 3 | 2026-04-13·06-01·08-03 주. **2026년에만 생긴 신생 지지대**로, 일봉에서는 같은 레벨이 5회 터치됐다([일봉 차트](./09_technical_daily.md) §2) |
| S2 | $56 | 3 | 2025-07-07·08-18·11-03 주. 2025년 거래 레인지의 하단 |
| S3 | $52 | 4 | 2024-12-16·2025-01-27·03-03·04-07 주. **터치가 가장 많은 지지대**이나 3절의 레벨 이동 이전 가격대라 근시일 지지로 보지 않는다 |

---

## 3. 관측된 특이 구간 — 2024~2026년, 세 단계에 걸친 레벨 상승

- **5년 차트의 특징은 단일 갭이 아니라 계단이 세 번 놓였다는 점이다.** 유효 클러스터의 시기가 뚜렷하게 갈린다 — S3 $52는 **2024-12~2025-04**, S2 $56은 **2025-07~11**, S1 $69는 **2026-04~08**이다. 각 구간 사이에 클러스터가 없다는 것은 가격이 그 구간에 머무르지 않고 통과했다는 뜻이다.
- 계기는 회사 고유 사건 하나가 아니라 **이익이 아닌 배수의 재평가**다. [핵심 지표](./04_metrics.md) A.2에서 보듯 FY2023 → TTM 구간에 Non-GAAP EPS는 $1.91 → $2.27(+19%)인데 주가는 $34.83 → $71.81(+106%)로 올랐고, 그만큼 Non-GAAP PER이 18.2x → 31.6x로 확대됐다. LNG 수출·데이터센터 전력 수요가 미드스트림 전반의 배수를 끌어올린 국면이며, 여기에 Power Innovation이라는 이 회사만의 성장 서사가 더해졌다.
- **지금 유의할 점은 그 재평가가 저금리 구간에서 일어났다는 것이다.** 세 계단이 놓인 2024~2026년 상반기는 [10년물 국채금리](../../../macro/rates/treasury_10y.md)가 지금(5.01%)보다 낮던 시기다. 이 회사는 순부채가 시가총액의 34%이고 부채비율이 343%라 할인율에 특히 민감한데([밸류에이션 / 적정주가](./06_valuation.md) 4-B에서 목표 EV 배수가 FY2023 수준으로 되돌아가면 적정주가가 $37.93까지 내려간다), **차트상 $56(S2)과 $69(S1) 사이의 공백은 그 재평가분이 놓인 구간**이기도 하다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-17. 수집 시점: 2026-09-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py WMB --name "Williams Companies" --interval 1wk --close-on 2026-09-17 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **R1은 터치가 2회뿐이라 강도가 얕다.** 주봉은 창이 9주라 일봉보다 스윙 포인트가 훨씬 적게 잡히므로, 같은 레벨이라도 일봉과 터치 횟수를 직접 비교하면 안 된다 — 일봉에서 9회 터치된 $76 클러스터는 주봉에서는 아예 잡히지 않는다.
    - **5년 원주가 차트에서 배당 미반영의 영향은 누적된다.** 이 기간 연 2.8~5.1%의 배당수익률이 계속 지급됐으므로 실제 총수익률은 차트상 상승률보다 상당히 높다.
    - 기간 내 주식분할·병합은 없었고, 2026-09-03 Momentum 인수의 신주 발행도 가격 연속성을 깨지 않는다(대가 지급용 발행이라 소급 조정 대상이 아니다).
    - `--close-on 2026-09-17`로 종료일을 고정했다 — 고정하지 않으면 진행 중인 주의 미완성 봉이 종가로 들어간다.

---

*작성일: 2026-09-18*
