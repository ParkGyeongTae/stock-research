# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉으로 여러 사이클에 걸친 구조적 지지/저항을 본다. 최근 1년 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)을 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트의 가격은 전 구간이 20:1 분할 후 기준이다
2022년 7월 **20:1 주식분할**이 이 5년 구간 안에 있다. Yahoo Finance 원자료가 과거 분할을 소급 반영하므로 아래 차트와 표의 2021~2022년 가격($84·$103 등)은 **당시 실제 호가가 아니라 분할 후로 환산된 값**이다. 당시 실제 주가는 이 값의 20배였다.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 2026-09-22 종가 **$351.16**은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 기준 종가와 **일치한다.**

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-20 ~ 2026-09-22)


<style>
.googl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .googl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.googl-chart svg { width:100%; height:auto; display:block; }
.googl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.googl-chart .title { fill: var(--ink); font-weight:600; }
.googl-chart .grid { stroke: var(--grid); stroke-width:1; }
.googl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="googl-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Alphabet(GOOGL) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Alphabet (GOOGL) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-20 ~ 2026-09-22 · 마지막 종가 $351.16 (2026-09-22) · 단위 USD</text>
<line x1="60" y1="577.1" x2="1052" y2="577.1" class="grid"/>
<text x="52" y="581.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="495.7" x2="1052" y2="495.7" class="grid"/>
<text x="52" y="499.7" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="414.3" x2="1052" y2="414.3" class="grid"/>
<text x="52" y="418.3" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="332.9" x2="1052" y2="332.9" class="grid"/>
<text x="52" y="336.9" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="251.4" x2="1052" y2="251.4" class="grid"/>
<text x="52" y="255.4" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="170.0" x2="1052" y2="170.0" class="grid"/>
<text x="52" y="174.0" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="88.6" x2="1052" y2="88.6" class="grid"/>
<text x="52" y="92.6" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="118.5" y1="56.0" x2="118.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="118.5" y1="626.0" x2="118.5" y2="631.0" class="axis"/>
<text x="118.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="314.6" y1="56.0" x2="314.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="314.6" y1="626.0" x2="314.6" y2="631.0" class="axis"/>
<text x="314.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="510.7" y1="56.0" x2="510.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="510.7" y1="626.0" x2="510.7" y2="631.0" class="axis"/>
<text x="510.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="710.6" y1="56.0" x2="710.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="710.6" y1="626.0" x2="710.6" y2="631.0" class="axis"/>
<text x="710.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="906.8" y1="56.0" x2="906.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="906.8" y1="626.0" x2="906.8" y2="631.0" class="axis"/>
<text x="906.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="508.2" x2="61.9" y2="514.4" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="508.4" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="65.7" y1="508.8" x2="65.7" y2="522.5" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="510.7" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="69.4" y1="511.5" x2="69.4" y2="526.6" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="512.3" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="73.2" y1="509.2" x2="73.2" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="509.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="77.0" y1="506.0" x2="77.0" y2="518.4" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="510.2" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="80.7" y1="497.9" x2="80.7" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="498.9" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="84.5" y1="495.2" x2="84.5" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="497.6" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="88.3" y1="494.7" x2="88.3" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="496.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="92.1" y1="494.1" x2="92.1" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="497.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="95.8" y1="496.0" x2="95.8" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="496.8" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="99.6" y1="501.7" x2="99.6" y2="511.7" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="505.5" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="103.4" y1="497.2" x2="103.4" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="499.0" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="107.1" y1="499.0" x2="107.1" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="499.3" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="110.9" y1="498.6" x2="110.9" y2="513.1" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="500.7" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="114.7" y1="498.4" x2="114.7" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="500.2" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="118.5" y1="501.4" x2="118.5" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="503.8" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="122.2" y1="507.4" x2="122.2" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="512.8" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="126.0" y1="515.3" x2="126.0" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="518.2" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="129.8" y1="522.8" x2="129.8" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="522.8" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="133.6" y1="493.2" x2="133.6" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="506.6" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="137.3" y1="505.1" x2="137.3" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="505.1" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="141.1" y1="515.1" x2="141.1" y2="528.0" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="523.0" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="144.9" y1="519.7" x2="144.9" y2="536.5" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="521.0" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="148.6" y1="517.8" x2="148.6" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="523.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="152.4" y1="522.1" x2="152.4" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="525.9" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="156.2" y1="518.1" x2="156.2" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="518.3" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="160.0" y1="508.7" x2="160.0" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="509.3" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="163.7" y1="505.8" x2="163.7" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="510.5" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="167.5" y1="506.0" x2="167.5" y2="523.5" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="511.4" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="171.3" y1="524.9" x2="171.3" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="525.3" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="175.0" y1="526.0" x2="175.0" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="533.2" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="178.8" y1="539.2" x2="178.8" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="546.0" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="182.6" y1="539.9" x2="182.6" y2="556.6" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="551.5" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="186.4" y1="548.0" x2="186.4" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="551.0" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="190.1" y1="549.6" x2="190.1" y2="567.7" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="552.8" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="193.9" y1="557.1" x2="193.9" y2="574.1" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="557.1" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="197.7" y1="548.0" x2="197.7" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="553.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="201.4" y1="545.6" x2="201.4" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="549.9" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="205.2" y1="558.5" x2="205.2" y2="568.9" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="565.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="209.0" y1="547.7" x2="209.0" y2="563.1" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="547.9" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="212.8" y1="546.9" x2="212.8" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="547.4" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="216.5" y1="545.1" x2="216.5" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="545.6" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="220.3" y1="547.8" x2="220.3" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="547.8" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="224.1" y1="552.1" x2="224.1" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="556.6" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="227.8" y1="549.9" x2="227.8" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="550.6" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="231.6" y1="546.6" x2="231.6" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="548.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="235.4" y1="541.8" x2="235.4" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="541.8" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="239.2" y1="540.6" x2="239.2" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="542.7" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="242.9" y1="549.9" x2="242.9" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="552.4" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="246.7" y1="559.3" x2="246.7" y2="565.3" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="560.9" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="250.5" y1="559.2" x2="250.5" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="559.8" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="254.3" y1="558.2" x2="254.3" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="559.2" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="258.0" y1="571.7" x2="258.0" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="574.3" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="261.8" y1="576.0" x2="261.8" y2="584.4" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="580.2" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="265.6" y1="572.4" x2="265.6" y2="582.8" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="579.3" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="269.3" y1="576.0" x2="269.3" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="578.8" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="273.1" y1="571.5" x2="273.1" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="575.3" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="276.9" y1="569.3" x2="276.9" y2="590.5" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="574.2" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="280.7" y1="583.6" x2="280.7" y2="604.3" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="584.6" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="284.4" y1="582.1" x2="284.4" y2="598.6" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="583.0" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="288.2" y1="576.9" x2="288.2" y2="586.1" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="581.3" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="292.0" y1="579.2" x2="292.0" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="581.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="295.7" y1="573.5" x2="295.7" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="576.4" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="299.5" y1="574.9" x2="299.5" y2="589.0" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="578.1" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="303.3" y1="577.9" x2="303.3" y2="594.2" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="589.0" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="307.1" y1="592.5" x2="307.1" y2="599.4" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="593.0" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="310.8" y1="595.2" x2="310.8" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="595.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="314.6" y1="591.7" x2="314.6" y2="601.8" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="594.1" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="318.4" y1="589.9" x2="318.4" y2="600.2" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="590.0" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="322.1" y1="579.9" x2="322.1" y2="593.3" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="580.4" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="325.9" y1="576.6" x2="325.9" y2="587.3" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="578.2" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="329.7" y1="564.4" x2="329.7" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="569.4" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="333.5" y1="563.8" x2="333.5" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="573.2" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="337.2" y1="580.9" x2="337.2" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="585.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="341.0" y1="588.4" x2="341.0" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="588.5" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="344.8" y1="587.4" x2="344.8" y2="594.5" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="587.5" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="348.5" y1="583.7" x2="348.5" y2="592.8" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="586.9" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="352.3" y1="572.5" x2="352.3" y2="594.4" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="574.5" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="356.1" y1="566.4" x2="356.1" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="568.3" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="359.9" y1="569.4" x2="359.9" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="569.6" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="363.6" y1="562.2" x2="363.6" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="563.4" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="367.4" y1="562.6" x2="367.4" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="562.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="371.2" y1="566.5" x2="371.2" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="568.3" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="375.0" y1="563.5" x2="375.0" y2="572.9" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="565.2" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="378.7" y1="564.1" x2="378.7" y2="571.1" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="566.0" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="382.5" y1="547.8" x2="382.5" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="548.6" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="386.3" y1="534.8" x2="386.3" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="540.1" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="390.0" y1="534.1" x2="390.0" y2="544.8" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="537.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="393.8" y1="534.6" x2="393.8" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="535.4" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="397.6" y1="529.8" x2="397.6" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="538.0" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="401.4" y1="534.6" x2="401.4" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="538.8" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="405.1" y1="537.1" x2="405.1" y2="546.5" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="539.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="408.9" y1="541.3" x2="408.9" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="543.3" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="412.7" y1="540.3" x2="412.7" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="545.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="416.4" y1="533.5" x2="416.4" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="535.7" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="420.2" y1="533.0" x2="420.2" y2="547.5" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="534.9" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="424.0" y1="522.2" x2="424.0" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="524.1" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="427.8" y1="522.5" x2="427.8" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="523.8" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="431.5" y1="524.9" x2="431.5" y2="531.3" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="529.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="435.3" y1="525.0" x2="435.3" y2="534.2" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="529.3" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="439.1" y1="521.4" x2="439.1" y2="533.9" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="528.5" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="442.8" y1="515.3" x2="442.8" y2="528.1" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="519.1" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="446.6" y1="517.4" x2="446.6" y2="523.5" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="517.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="450.4" y1="514.1" x2="450.4" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="516.2" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="454.2" y1="513.4" x2="454.2" y2="528.9" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="517.5" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="457.9" y1="521.7" x2="457.9" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="526.9" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="461.7" y1="515.0" x2="461.7" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="515.9" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="465.5" y1="510.0" x2="465.5" y2="519.1" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="516.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="469.2" y1="510.8" x2="469.2" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="515.0" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="473.0" y1="513.0" x2="473.0" y2="544.2" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="520.1" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="476.8" y1="529.1" x2="476.8" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="529.8" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="480.6" y1="523.7" x2="480.6" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="524.1" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="484.3" y1="516.5" x2="484.3" y2="526.2" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="519.6" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="488.1" y1="512.9" x2="488.1" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="517.4" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="491.9" y1="514.6" x2="491.9" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="518.5" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="495.7" y1="514.3" x2="495.7" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="520.2" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="499.4" y1="522.2" x2="499.4" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="524.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="503.2" y1="508.8" x2="503.2" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="509.6" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="507.0" y1="507.6" x2="507.0" y2="514.0" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="509.4" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="510.7" y1="512.6" x2="510.7" y2="519.9" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="514.4" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="514.5" y1="503.5" x2="514.5" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="507.7" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="518.3" y1="501.5" x2="518.3" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="501.6" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="522.1" y1="490.7" x2="522.1" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="492.1" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="525.8" y1="489.6" x2="525.8" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="492.4" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="529.6" y1="496.6" x2="529.6" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="497.3" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="533.4" y1="496.8" x2="533.4" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="498.3" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="537.1" y1="503.9" x2="537.1" y2="512.8" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="505.6" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="540.9" y1="508.0" x2="540.9" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="508.5" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="544.7" y1="515.1" x2="544.7" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="519.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="548.5" y1="506.2" x2="548.5" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="510.1" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="552.2" y1="492.2" x2="552.2" y2="502.1" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="494.5" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="556.0" y1="492.0" x2="556.0" y2="499.3" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="494.2" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="559.8" y1="486.4" x2="559.8" y2="496.4" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="491.6" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="563.5" y1="479.1" x2="563.5" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="483.1" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="567.3" y1="480.7" x2="567.3" y2="492.0" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="481.3" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="571.1" y1="455.5" x2="571.1" y2="494.3" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="460.0" width="2.34" height="28.7" fill="var(--up)"/>
<line x1="574.9" y1="463.9" x2="574.9" y2="475.2" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="464.7" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="578.6" y1="460.3" x2="578.6" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="465.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="582.4" y1="452.9" x2="582.4" y2="472.9" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="453.3" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="586.2" y1="448.9" x2="586.2" y2="458.3" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="453.1" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="589.9" y1="451.3" x2="589.9" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="455.9" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="593.7" y1="450.3" x2="593.7" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="455.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="597.5" y1="446.2" x2="597.5" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="452.1" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="601.3" y1="445.5" x2="601.3" y2="456.5" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="447.5" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="605.0" y1="437.0" x2="605.0" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="443.4" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="608.8" y1="429.2" x2="608.8" y2="444.7" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="429.6" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="612.6" y1="427.7" x2="612.6" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="430.7" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="616.3" y1="432.7" x2="616.3" y2="452.6" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="438.8" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="620.1" y1="441.0" x2="620.1" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="445.9" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="623.9" y1="456.2" x2="623.9" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="465.0" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="627.7" y1="472.2" x2="627.7" y2="487.7" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="473.5" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="631.4" y1="471.2" x2="631.4" y2="483.2" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="472.3" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="635.2" y1="465.4" x2="635.2" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="470.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="639.0" y1="467.1" x2="639.0" y2="479.0" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="469.0" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="642.8" y1="476.4" x2="642.8" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="476.6" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="646.5" y1="482.1" x2="646.5" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="483.6" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="650.3" y1="473.3" x2="650.3" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="473.6" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="654.1" y1="470.1" x2="654.1" y2="478.3" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="472.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="657.8" y1="464.5" x2="657.8" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="467.9" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="661.6" y1="465.6" x2="661.6" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="466.9" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="665.4" y1="466.9" x2="665.4" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="473.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="669.2" y1="470.0" x2="669.2" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="470.8" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="672.9" y1="443.6" x2="672.9" y2="473.0" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="461.0" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="676.7" y1="445.1" x2="676.7" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="449.5" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="680.5" y1="442.8" x2="680.5" y2="461.2" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="449.2" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="684.2" y1="448.7" x2="684.2" y2="473.4" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="457.6" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="688.0" y1="463.4" x2="688.0" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="464.9" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="691.8" y1="453.3" x2="691.8" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="455.5" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="695.6" y1="421.4" x2="695.6" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="430.9" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="699.3" y1="412.0" x2="699.3" y2="438.4" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="425.9" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="703.1" y1="419.6" x2="703.1" y2="430.3" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="426.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="706.9" y1="425.3" x2="706.9" y2="434.6" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="427.7" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="710.6" y1="412.7" x2="710.6" y2="430.1" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="424.1" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="714.4" y1="418.8" x2="714.4" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="420.8" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="718.2" y1="410.6" x2="718.2" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="413.9" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="722.0" y1="405.4" x2="722.0" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="407.7" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="725.7" y1="402.8" x2="725.7" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="413.2" width="2.34" height="25.0" fill="var(--down)"/>
<line x1="729.5" y1="433.5" x2="729.5" y2="443.9" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="434.9" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="733.3" y1="437.2" x2="733.3" y2="448.4" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="437.7" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="737.0" y1="441.8" x2="737.0" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="443.6" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="740.8" y1="455.0" x2="740.8" y2="470.0" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="456.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="744.6" y1="465.7" x2="744.6" y2="477.2" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="466.0" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="748.4" y1="469.2" x2="748.4" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="471.2" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="752.1" y1="462.1" x2="752.1" y2="489.8" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="467.9" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="755.9" y1="482.0" x2="755.9" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="490.6" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="759.7" y1="480.2" x2="759.7" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="484.1" width="2.34" height="25.4" fill="var(--up)"/>
<line x1="763.5" y1="476.6" x2="763.5" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="479.4" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="767.2" y1="469.5" x2="767.2" y2="502.1" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="476.2" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="771.0" y1="471.3" x2="771.0" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="472.9" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="774.8" y1="470.7" x2="774.8" y2="499.2" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="474.5" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="778.5" y1="464.2" x2="778.5" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="469.3" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="782.3" y1="452.1" x2="782.3" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="465.6" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="786.1" y1="454.6" x2="786.1" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="460.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="789.9" y1="455.8" x2="789.9" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="457.1" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="793.6" y1="445.0" x2="793.6" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="455.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="797.4" y1="451.2" x2="797.4" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="455.4" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="801.2" y1="449.0" x2="801.2" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="449.3" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="804.9" y1="444.9" x2="804.9" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="445.6" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="808.7" y1="444.5" x2="808.7" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="446.5" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="812.5" y1="436.4" x2="812.5" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="438.6" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="816.3" y1="417.6" x2="816.3" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="425.4" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="820.0" y1="418.2" x2="820.0" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="424.6" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="823.8" y1="410.0" x2="823.8" y2="430.4" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="412.0" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="827.6" y1="403.8" x2="827.6" y2="418.3" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="407.9" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="831.3" y1="400.4" x2="831.3" y2="419.8" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="404.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="835.1" y1="390.4" x2="835.1" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="393.3" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="838.9" y1="356.0" x2="838.9" y2="404.2" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="357.3" width="2.34" height="43.3" fill="var(--up)"/>
<line x1="842.7" y1="345.5" x2="842.7" y2="360.2" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="347.8" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="846.4" y1="323.1" x2="846.4" y2="341.6" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="325.2" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="850.2" y1="323.4" x2="850.2" y2="347.9" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="325.6" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="854.0" y1="331.0" x2="854.0" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="336.4" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="857.7" y1="330.7" x2="857.7" y2="355.9" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="341.4" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="861.5" y1="321.5" x2="861.5" y2="349.6" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="327.5" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="865.3" y1="313.8" x2="865.3" y2="342.4" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="316.7" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="869.1" y1="265.1" x2="869.1" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="282.1" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="872.8" y1="270.4" x2="872.8" y2="291.8" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="280.4" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="876.6" y1="264.4" x2="876.6" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="276.8" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="880.4" y1="241.0" x2="880.4" y2="286.9" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="252.0" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="884.2" y1="204.5" x2="884.2" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="218.6" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="887.9" y1="213.7" x2="887.9" y2="228.8" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="216.8" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="891.7" y1="216.7" x2="891.7" y2="242.4" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="218.8" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="895.5" y1="232.8" x2="895.5" y2="257.7" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="233.0" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="899.2" y1="226.9" x2="899.2" y2="242.8" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="229.4" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="903.0" y1="214.8" x2="903.0" y2="234.6" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="226.8" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="906.8" y1="201.2" x2="906.8" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="204.9" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="910.6" y1="185.5" x2="910.6" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="202.6" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="914.3" y1="194.2" x2="914.3" y2="219.9" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="205.9" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="918.1" y1="182.6" x2="918.1" y2="208.2" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="189.5" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="921.9" y1="171.6" x2="921.9" y2="240.9" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="192.4" width="2.34" height="21.8" fill="var(--down)"/>
<line x1="925.6" y1="206.3" x2="925.6" y2="245.4" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="217.3" width="2.34" height="24.8" fill="var(--down)"/>
<line x1="929.4" y1="224.6" x2="929.4" y2="257.5" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="227.0" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="933.2" y1="219.6" x2="933.2" y2="247.6" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="220.4" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="937.0" y1="237.6" x2="937.0" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="246.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="940.7" y1="232.8" x2="940.7" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="247.7" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="944.5" y1="231.1" x2="944.5" y2="254.2" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="244.3" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="948.3" y1="241.7" x2="948.3" y2="293.9" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="248.0" width="2.34" height="45.2" fill="var(--down)"/>
<line x1="952.0" y1="250.6" x2="952.0" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="258.3" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="955.8" y1="215.5" x2="955.8" y2="259.3" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="223.4" width="2.34" height="34.8" fill="var(--up)"/>
<line x1="959.6" y1="182.5" x2="959.6" y2="226.2" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="183.5" width="2.34" height="40.0" fill="var(--up)"/>
<line x1="963.4" y1="177.7" x2="963.4" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="179.1" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="967.1" y1="110.1" x2="967.1" y2="181.8" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="111.9" width="2.34" height="64.7" fill="var(--up)"/>
<line x1="970.9" y1="85.3" x2="970.9" y2="121.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="87.3" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="974.7" y1="82.5" x2="974.7" y2="116.6" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="93.8" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="978.4" y1="74.5" x2="978.4" y2="118.3" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="95.6" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="982.2" y1="98.5" x2="982.2" y2="123.7" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="113.8" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="986.0" y1="123.5" x2="986.0" y2="156.8" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="126.8" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="989.8" y1="134.0" x2="989.8" y2="175.9" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="145.3" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="993.5" y1="127.7" x2="993.5" y2="155.9" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="140.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="997.3" y1="155.5" x2="997.3" y2="202.2" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="157.1" width="2.34" height="33.5" fill="var(--down)"/>
<line x1="1001.1" y1="146.9" x2="1001.1" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="153.9" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="1004.9" y1="132.3" x2="1004.9" y2="168.2" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="151.2" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="1008.6" y1="128.8" x2="1008.6" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="159.9" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="1012.4" y1="154.2" x2="1012.4" y2="227.2" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="168.6" width="2.34" height="50.7" fill="var(--down)"/>
<line x1="1016.2" y1="156.0" x2="1016.2" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="160.0" width="2.34" height="50.6" fill="var(--up)"/>
<line x1="1019.9" y1="113.8" x2="1019.9" y2="163.8" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="144.8" width="2.34" height="18.2" fill="var(--down)"/>
<line x1="1023.7" y1="157.6" x2="1023.7" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="161.6" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="1027.5" y1="174.5" x2="1027.5" y2="188.6" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="176.1" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="1031.3" y1="167.4" x2="1031.3" y2="188.7" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="175.6" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="1035.0" y1="178.7" x2="1035.0" y2="198.0" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="180.0" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="1038.8" y1="181.4" x2="1038.8" y2="206.3" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="188.7" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="1042.6" y1="154.6" x2="1042.6" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="170.7" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="1046.3" y1="157.6" x2="1046.3" y2="171.5" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="161.9" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="1050.1" y1="146.9" x2="1050.1" y2="169.6" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="157.1" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="60" y1="529.5" x2="1052" y2="529.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="523.5" font-size="11.5" fill="var(--support)" font-weight="600">$129 S1</text>
<text x="1058" y="535.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="572.3" x2="1052" y2="572.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="566.3" font-size="11.5" fill="var(--support)" font-weight="600">$103 S2</text>
<text x="1058" y="578.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="603.0" x2="1052" y2="603.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="597.0" font-size="11.5" fill="var(--support)" font-weight="600">$84 S3</text>
<text x="1058" y="609.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="168.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="160.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $351 (2026-09-22)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 일봉(09)과 탐지 창만 다르고 나머지 파라미터는 같다. 터치 횟수는 강도 근사치이며 미래 지지/저항을 보장하지 않는다.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$351.16** (2026-09-22 종가) | — | 위쪽에 검출된 저항 레벨 없음 — 스윙 포인트는 있으나 터치 2회 이상으로 묶인 클러스터가 없다(가장 먼 쪽 $409, 현재가 대비 16%). §4에 표본 한계를 남길 것. 가장 가까운 지지는 S1 |
| S1 | $129 | 2 | 2023-12-04·2024-03-04 — 2023년 말~2024년 초 상승 구간의 눌림목. 현재가 대비 −63%로 실질적 의미는 없다 |
| S2 | $103 | 2 | 2022-05-23·2022-07-25 — ATT·광고 불황기의 저점대(분할 후 환산 기준) |
| S3 | $84 | 2 | 2022-10-31·2023-01-02 — 5년 최저 구간($83.34). 분할 후 환산 기준 |

---

## 3. 관측된 특이 구간 — 위쪽에 검출된 저항이 없다

- 스크립트가 **저항 레벨을 하나도 만들지 못했다.** 현재가 위쪽에 스윙 고점 자체는 있으나(가장 먼 쪽 $409, 현재가 대비 +16%) 터치 2회 이상으로 묶이는 클러스터가 없다. 즉 **지금 가격대는 "신고가 부근"이며, 위쪽에 여러 번 확인된 매물대가 없다.**
- 반대로 아래쪽 지지 3개는 전부 **현재가 대비 −63% 이상 떨어져 있어** 실질적인 지지선 역할을 하지 못한다. 5년 차트에서 이 종목의 상승폭(최저 $83.34 → 최고 $408.61, 4.9배)이 워낙 커서 중간 가격대에 스윙이 충분히 쌓이지 않았기 때문이다.
- **따라서 이 문서의 주봉 레벨은 "현재 구간의 지지/저항"으로 쓸 수 없다.** 근시일 참고는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)의 레벨을 본다.


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-20~2026-09-22. 수집 시점: 2026-09-23. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py` (`GOOGL --name Alphabet --interval 1wk --close-on 2026-09-22 --emit all`)

**한계**
- **표본 한계가 이 문서의 핵심이다.** 위 3절대로 저항 클러스터가 0개이고 지지 3개가 모두 −63% 이하에 있어, **이 표는 현재 가격대에 대해 아무 정보도 주지 않는다.** 5년 동안 가격이 한 방향으로 4.9배 오른 종목에서 구조적으로 발생하는 현상이며, 파라미터를 조정해 억지로 레벨을 만들지 않았다.
- **원주가라 배당이 반영돼 있지 않다.** 기간 내 배당 10회. 분할(2022-07, 20:1)은 소급 반영돼 있다 — 위 경고 블록 참고.
- 레벨 개수를 3개로 고정하지 않았다. 저항은 유효 클러스터가 없어 0개, 지지는 3개다.

---

*작성일: 2026-09-23*
