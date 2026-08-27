# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(5년 주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: `2026-08-25` 종가 $366.43은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)·[개요](./01_overview.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 현재주가와 **일치**한다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-25)

<div class="ter-chart">
<style>
.ter-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ter-chart svg { width:100%; height:auto; display:block; }
.ter-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ter-chart .title { fill: var(--ink); font-weight:600; }
.ter-chart .grid { stroke: var(--grid); stroke-width:1; }
.ter-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Teradyne(TER) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Teradyne (TER) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-25 · 마지막 종가 $366.43 (2026-08-25) · 단위 USD</text>
<line x1="60" y1="563.4" x2="1052" y2="563.4" class="grid"/>
<text x="52" y="567.4" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="438.1" x2="1052" y2="438.1" class="grid"/>
<text x="52" y="442.1" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="312.8" x2="1052" y2="312.8" class="grid"/>
<text x="52" y="316.8" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="187.5" x2="1052" y2="187.5" class="grid"/>
<text x="52" y="191.5" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="62.3" x2="1052" y2="62.3" class="grid"/>
<text x="52" y="66.3" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="133.6" y1="56.0" x2="133.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.6" y1="626.0" x2="133.6" y2="631.0" class="axis"/>
<text x="133.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="329.7" y1="56.0" x2="329.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="329.7" y1="626.0" x2="329.7" y2="631.0" class="axis"/>
<text x="329.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="525.8" y1="56.0" x2="525.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="525.8" y1="626.0" x2="525.8" y2="631.0" class="axis"/>
<text x="525.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="725.7" y1="56.0" x2="725.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="725.7" y1="626.0" x2="725.7" y2="631.0" class="axis"/>
<text x="725.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.9" y1="56.0" x2="921.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.9" y1="626.0" x2="921.9" y2="631.0" class="axis"/>
<text x="921.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="534.8" x2="61.9" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="535.1" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="65.7" y1="533.2" x2="65.7" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="534.0" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="69.4" y1="533.1" x2="69.4" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="535.6" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="73.2" y1="533.5" x2="73.2" y2="539.0" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="535.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="77.0" y1="537.2" x2="77.0" y2="545.0" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="539.1" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="80.7" y1="539.4" x2="80.7" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="540.4" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="84.5" y1="547.0" x2="84.5" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="551.4" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="88.3" y1="544.8" x2="88.3" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="545.9" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="92.1" y1="537.3" x2="92.1" y2="547.6" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="543.2" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="95.8" y1="514.8" x2="95.8" y2="544.4" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="515.5" width="2.34" height="27.7" fill="var(--up)"/>
<line x1="99.6" y1="504.8" x2="99.6" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="508.0" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="103.4" y1="505.3" x2="103.4" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="505.5" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="107.1" y1="496.1" x2="107.1" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="499.1" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="110.9" y1="495.1" x2="110.9" y2="506.5" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="498.1" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="114.7" y1="490.4" x2="114.7" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="500.0" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="118.5" y1="486.3" x2="118.5" y2="507.1" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="488.5" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="122.2" y1="484.4" x2="122.2" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="487.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="126.0" y1="483.0" x2="126.0" y2="494.6" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="484.8" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="129.8" y1="477.0" x2="129.8" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="483.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="133.6" y1="479.1" x2="133.6" y2="492.1" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="482.1" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="137.3" y1="478.6" x2="137.3" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="482.5" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="141.1" y1="486.2" x2="141.1" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="487.0" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="144.9" y1="503.3" x2="144.9" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="514.8" width="2.34" height="33.3" fill="var(--down)"/>
<line x1="148.6" y1="537.6" x2="148.6" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="545.8" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="152.4" y1="535.6" x2="152.4" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="545.6" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="156.2" y1="538.3" x2="156.2" y2="549.5" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="544.8" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="160.0" y1="538.1" x2="160.0" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="538.3" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="163.7" y1="538.9" x2="163.7" y2="550.8" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="539.0" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="167.5" y1="546.0" x2="167.5" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="547.3" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="171.3" y1="533.5" x2="171.3" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="534.6" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="175.0" y1="533.1" x2="175.0" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="533.2" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="178.8" y1="529.2" x2="178.8" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="537.1" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="182.6" y1="538.1" x2="182.6" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="542.2" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="186.4" y1="549.2" x2="186.4" y2="555.8" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="554.2" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="190.1" y1="541.5" x2="190.1" y2="556.6" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="551.8" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="193.9" y1="544.0" x2="193.9" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="552.6" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="197.7" y1="545.6" x2="197.7" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="555.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="201.4" y1="552.8" x2="201.4" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="554.2" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="205.2" y1="552.3" x2="205.2" y2="566.3" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="555.9" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="209.0" y1="551.5" x2="209.0" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="551.6" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="212.8" y1="550.1" x2="212.8" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="552.1" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="216.5" y1="551.2" x2="216.5" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="552.0" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="220.3" y1="570.1" x2="220.3" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="571.4" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="224.1" y1="566.8" x2="224.1" y2="576.8" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="567.0" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="227.8" y1="564.3" x2="227.8" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="565.7" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="231.6" y1="572.8" x2="231.6" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="573.3" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="235.4" y1="571.2" x2="235.4" y2="579.1" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="571.2" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="239.2" y1="559.8" x2="239.2" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="562.8" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="242.9" y1="561.9" x2="242.9" y2="576.8" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="562.2" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="246.7" y1="560.0" x2="246.7" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="562.4" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="250.5" y1="556.8" x2="250.5" y2="574.5" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="557.9" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="254.3" y1="557.6" x2="254.3" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="558.4" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="258.0" y1="567.8" x2="258.0" y2="576.0" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="570.1" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="261.8" y1="575.1" x2="261.8" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="576.6" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="265.6" y1="575.9" x2="265.6" y2="586.1" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="577.3" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="269.3" y1="577.3" x2="269.3" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="577.3" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="273.1" y1="582.7" x2="273.1" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="586.9" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="276.9" y1="587.9" x2="276.9" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="589.4" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="280.7" y1="584.4" x2="280.7" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="591.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="284.4" y1="591.4" x2="284.4" y2="603.7" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="591.4" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="288.2" y1="591.6" x2="288.2" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="591.8" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="292.0" y1="581.9" x2="292.0" y2="592.6" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="584.2" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="295.7" y1="582.4" x2="295.7" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="582.5" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="299.5" y1="567.3" x2="299.5" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="568.0" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="303.3" y1="566.2" x2="303.3" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="569.8" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="307.1" y1="568.9" x2="307.1" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="572.6" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="310.8" y1="570.1" x2="310.8" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="572.5" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="314.6" y1="569.5" x2="314.6" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="572.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="318.4" y1="564.4" x2="318.4" y2="579.4" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="573.5" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="322.1" y1="575.9" x2="322.1" y2="583.7" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="576.6" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="325.9" y1="578.2" x2="325.9" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="579.2" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="329.7" y1="573.6" x2="329.7" y2="581.5" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="574.3" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="333.5" y1="565.6" x2="333.5" y2="572.9" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="566.6" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="337.2" y1="565.3" x2="337.2" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="566.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="341.0" y1="557.1" x2="341.0" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="559.1" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="344.8" y1="548.3" x2="344.8" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="553.4" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="348.5" y1="549.7" x2="348.5" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="554.1" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="352.3" y1="552.7" x2="352.3" y2="558.8" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="556.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="557.9" x2="356.1" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="559.1" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="359.9" y1="559.1" x2="359.9" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="559.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="363.6" y1="557.4" x2="363.6" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="558.9" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="367.4" y1="554.8" x2="367.4" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="557.0" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="371.2" y1="552.2" x2="371.2" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="555.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="375.0" y1="552.3" x2="375.0" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="554.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="378.7" y1="554.2" x2="378.7" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="555.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="382.5" y1="558.7" x2="382.5" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="562.4" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="386.3" y1="562.5" x2="386.3" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="565.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="390.0" y1="565.0" x2="390.0" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="565.9" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="393.8" y1="571.1" x2="393.8" y2="576.2" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="572.6" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="397.6" y1="572.2" x2="397.6" y2="577.2" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="572.5" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="401.4" y1="564.2" x2="401.4" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="567.0" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="405.1" y1="557.6" x2="405.1" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="558.7" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="408.9" y1="555.5" x2="408.9" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="555.5" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="412.7" y1="555.2" x2="412.7" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="557.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="416.4" y1="548.1" x2="416.4" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="549.5" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="420.2" y1="548.3" x2="420.2" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="549.5" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="424.0" y1="547.6" x2="424.0" y2="556.7" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="549.2" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="427.8" y1="548.2" x2="427.8" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="548.6" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="431.5" y1="544.6" x2="431.5" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="547.0" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="435.3" y1="541.3" x2="435.3" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="544.5" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="439.1" y1="539.3" x2="439.1" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="544.2" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="442.8" y1="546.3" x2="442.8" y2="556.0" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="548.0" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="446.6" y1="552.0" x2="446.6" y2="561.6" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="552.2" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="450.4" y1="557.4" x2="450.4" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="561.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="454.2" y1="555.1" x2="454.2" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="558.6" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="457.9" y1="551.9" x2="457.9" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="552.8" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="461.7" y1="553.4" x2="461.7" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="553.5" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="465.5" y1="562.1" x2="465.5" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="562.1" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="469.2" y1="564.7" x2="469.2" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="569.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="473.0" y1="561.4" x2="473.0" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="562.8" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="476.8" y1="561.3" x2="476.8" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="562.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="480.6" y1="561.5" x2="480.6" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="564.1" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="484.3" y1="566.6" x2="484.3" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="568.8" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="488.1" y1="572.4" x2="488.1" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="574.6" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="491.9" y1="578.0" x2="491.9" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="578.8" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="495.7" y1="577.8" x2="495.7" y2="582.6" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="578.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="499.4" y1="572.8" x2="499.4" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="573.3" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="503.2" y1="571.0" x2="503.2" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="572.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="507.0" y1="570.7" x2="507.0" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="571.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="510.7" y1="571.4" x2="510.7" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="572.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="514.5" y1="555.5" x2="514.5" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="556.9" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="518.3" y1="553.6" x2="518.3" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="553.8" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="522.1" y1="549.3" x2="522.1" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="552.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="525.8" y1="554.6" x2="525.8" y2="563.4" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="554.6" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="529.6" y1="555.7" x2="529.6" y2="559.7" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="557.3" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="533.4" y1="552.0" x2="533.4" y2="562.4" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="552.4" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="537.1" y1="546.3" x2="537.1" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="550.8" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="540.9" y1="555.3" x2="540.9" y2="573.0" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="558.1" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="544.7" y1="560.3" x2="544.7" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="560.5" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="548.5" y1="557.4" x2="548.5" y2="566.5" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="560.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="552.2" y1="559.2" x2="552.2" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="562.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="556.0" y1="554.9" x2="556.0" y2="564.9" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="556.0" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="559.8" y1="549.7" x2="559.8" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="555.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="563.5" y1="552.8" x2="563.5" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="556.1" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="567.3" y1="547.1" x2="567.3" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="549.9" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="571.1" y1="546.7" x2="571.1" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="547.3" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="574.9" y1="544.8" x2="574.9" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="547.3" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="578.6" y1="549.3" x2="578.6" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="553.4" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="582.4" y1="553.4" x2="582.4" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="554.0" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="586.2" y1="545.0" x2="586.2" y2="568.1" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="545.7" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="589.9" y1="536.0" x2="589.9" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="537.8" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="593.7" y1="533.2" x2="593.7" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="534.6" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="597.5" y1="521.4" x2="597.5" y2="534.7" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="523.4" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="601.3" y1="506.2" x2="601.3" y2="519.9" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="508.2" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="605.0" y1="505.1" x2="605.0" y2="518.3" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="508.0" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="608.8" y1="506.2" x2="608.8" y2="515.0" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="508.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="612.6" y1="497.9" x2="612.6" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="506.9" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="616.3" y1="498.3" x2="616.3" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="502.7" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="620.1" y1="498.8" x2="620.1" y2="507.9" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="502.9" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="623.9" y1="497.4" x2="623.9" y2="506.5" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="499.2" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="627.7" y1="486.7" x2="627.7" y2="498.4" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="492.8" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="631.4" y1="484.2" x2="631.4" y2="505.7" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="491.7" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="635.2" y1="494.2" x2="635.2" y2="537.9" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="499.5" width="2.34" height="30.7" fill="var(--down)"/>
<line x1="639.0" y1="523.8" x2="639.0" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="527.8" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="642.8" y1="534.2" x2="642.8" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="536.2" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="646.5" y1="521.4" x2="646.5" y2="537.7" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="521.9" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="650.3" y1="516.4" x2="650.3" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="518.3" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="654.1" y1="515.6" x2="654.1" y2="525.0" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="517.3" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="657.8" y1="520.4" x2="657.8" y2="538.5" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="521.4" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="661.6" y1="523.0" x2="661.6" y2="535.9" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="524.2" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="665.4" y1="518.3" x2="665.4" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="527.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="669.2" y1="515.2" x2="669.2" y2="527.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="520.0" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="672.9" y1="520.4" x2="672.9" y2="528.5" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="522.1" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="676.7" y1="523.0" x2="676.7" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="523.4" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="680.5" y1="519.1" x2="680.5" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="523.7" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="684.2" y1="530.1" x2="684.2" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="531.2" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="688.0" y1="546.1" x2="688.0" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="548.5" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="691.8" y1="547.8" x2="691.8" y2="558.7" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="549.7" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="695.6" y1="550.0" x2="695.6" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="550.2" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="699.3" y1="553.0" x2="699.3" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="553.1" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="703.1" y1="547.9" x2="703.1" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="549.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="706.9" y1="538.6" x2="706.9" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="540.2" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="710.6" y1="532.8" x2="710.6" y2="543.2" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="534.3" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="714.4" y1="521.6" x2="714.4" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="528.4" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="718.2" y1="523.4" x2="718.2" y2="531.1" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="527.6" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="722.0" y1="524.0" x2="722.0" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="525.0" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="725.7" y1="508.0" x2="725.7" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="518.8" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="729.5" y1="513.3" x2="729.5" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="515.3" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="733.3" y1="518.0" x2="733.3" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="519.5" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="737.0" y1="531.6" x2="737.0" y2="562.4" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="532.6" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="740.8" y1="545.1" x2="740.8" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="546.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="744.6" y1="544.5" x2="744.6" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="544.8" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="748.4" y1="537.5" x2="748.4" y2="546.4" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="543.4" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="752.1" y1="542.4" x2="752.1" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="543.2" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="755.9" y1="548.7" x2="755.9" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="549.6" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="759.7" y1="555.8" x2="759.7" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="555.9" width="2.34" height="24.1" fill="var(--down)"/>
<line x1="763.5" y1="574.8" x2="763.5" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="579.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="767.2" y1="574.3" x2="767.2" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="576.2" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="771.0" y1="582.3" x2="771.0" y2="604.6" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="586.7" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="774.8" y1="587.9" x2="774.8" y2="606.2" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="596.4" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="778.5" y1="593.4" x2="778.5" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="594.0" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="782.3" y1="591.3" x2="782.3" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="592.0" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="786.1" y1="590.1" x2="786.1" y2="599.4" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="592.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="789.9" y1="590.5" x2="789.9" y2="597.0" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="591.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="793.6" y1="581.1" x2="793.6" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="584.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="797.4" y1="585.9" x2="797.4" y2="593.4" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="587.7" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="801.2" y1="585.3" x2="801.2" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="589.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="804.9" y1="581.2" x2="804.9" y2="591.2" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="581.9" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="808.7" y1="576.4" x2="808.7" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="580.8" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="812.5" y1="577.7" x2="812.5" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="580.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="816.3" y1="573.7" x2="816.3" y2="581.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="575.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="820.0" y1="569.4" x2="820.0" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="572.1" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="823.8" y1="564.3" x2="823.8" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="567.1" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="827.6" y1="565.7" x2="827.6" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="567.1" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="831.3" y1="566.8" x2="831.3" y2="576.3" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="568.6" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="835.1" y1="546.5" x2="835.1" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="558.2" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="838.9" y1="552.9" x2="838.9" y2="559.6" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="554.0" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="842.7" y1="545.4" x2="842.7" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="551.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="846.4" y1="541.9" x2="846.4" y2="555.5" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="544.2" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="850.2" y1="538.1" x2="850.2" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="540.5" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="854.0" y1="534.0" x2="854.0" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="538.1" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="857.7" y1="536.7" x2="857.7" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="538.0" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="861.5" y1="537.6" x2="861.5" y2="549.7" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="538.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="865.3" y1="515.5" x2="865.3" y2="530.8" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="519.1" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="869.1" y1="501.4" x2="869.1" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="506.2" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="872.8" y1="499.8" x2="872.8" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="503.4" width="2.34" height="19.8" fill="var(--down)"/>
<line x1="876.6" y1="509.4" x2="876.6" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="514.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="880.4" y1="502.0" x2="880.4" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="507.9" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="884.2" y1="455.7" x2="884.2" y2="508.1" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="460.9" width="2.34" height="42.2" fill="var(--up)"/>
<line x1="887.9" y1="448.7" x2="887.9" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="459.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="891.7" y1="452.2" x2="891.7" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="452.6" width="2.34" height="23.1" fill="var(--down)"/>
<line x1="895.5" y1="470.9" x2="895.5" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="477.6" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="899.2" y1="460.4" x2="899.2" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="460.8" width="2.34" height="27.4" fill="var(--up)"/>
<line x1="903.0" y1="434.2" x2="903.0" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="437.1" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="906.8" y1="431.8" x2="906.8" y2="448.3" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="434.3" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="910.6" y1="437.5" x2="910.6" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="438.2" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="914.3" y1="435.6" x2="914.3" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="436.8" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="918.1" y1="427.1" x2="918.1" y2="446.4" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="428.6" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="921.9" y1="400.9" x2="921.9" y2="423.3" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="416.5" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="925.6" y1="389.3" x2="925.6" y2="417.3" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="402.8" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="929.4" y1="390.5" x2="929.4" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="401.5" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="933.2" y1="368.9" x2="933.2" y2="404.2" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="386.7" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="937.0" y1="311.1" x2="937.0" y2="387.1" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="312.7" width="2.34" height="74.0" fill="var(--up)"/>
<line x1="940.7" y1="277.7" x2="940.7" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="294.4" width="2.34" height="21.1" fill="var(--up)"/>
<line x1="944.5" y1="279.0" x2="944.5" y2="312.3" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="281.7" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="948.3" y1="256.5" x2="948.3" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="287.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="952.0" y1="280.3" x2="952.0" y2="351.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="299.7" width="2.34" height="46.9" fill="var(--down)"/>
<line x1="955.8" y1="297.0" x2="955.8" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="329.8" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="959.6" y1="303.0" x2="959.6" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="317.9" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="963.4" y1="278.5" x2="963.4" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="311.5" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="967.1" y1="291.8" x2="967.1" y2="346.5" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="300.8" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="970.9" y1="221.4" x2="970.9" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="227.6" width="2.34" height="70.0" fill="var(--up)"/>
<line x1="974.7" y1="210.8" x2="974.7" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="212.1" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="978.4" y1="159.8" x2="978.4" y2="221.4" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="164.9" width="2.34" height="44.3" fill="var(--up)"/>
<line x1="982.2" y1="160.7" x2="982.2" y2="310.5" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="160.7" width="2.34" height="95.2" fill="var(--down)"/>
<line x1="986.0" y1="208.8" x2="986.0" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="237.9" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="989.8" y1="228.3" x2="989.8" y2="268.6" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="243.1" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="993.5" y1="237.2" x2="993.5" y2="301.0" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="239.6" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="997.3" y1="179.2" x2="997.3" y2="231.6" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="219.7" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="1001.1" y1="161.7" x2="1001.1" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="229.5" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="1004.9" y1="177.5" x2="1004.9" y2="262.3" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="183.5" width="2.34" height="31.8" fill="var(--up)"/>
<line x1="1008.6" y1="136.5" x2="1008.6" y2="177.2" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="140.0" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="1012.4" y1="96.9" x2="1012.4" y2="176.6" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="117.2" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="1016.2" y1="77.4" x2="1016.2" y2="235.1" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="136.7" width="2.34" height="89.6" fill="var(--down)"/>
<line x1="1019.9" y1="187.8" x2="1019.9" y2="277.4" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="204.4" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="1023.7" y1="231.4" x2="1023.7" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="256.4" width="2.34" height="28.4" fill="var(--down)"/>
<line x1="1027.5" y1="213.6" x2="1027.5" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="250.3" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="1031.3" y1="197.6" x2="1031.3" y2="311.6" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="228.0" width="2.34" height="22.2" fill="var(--up)"/>
<line x1="1035.0" y1="175.4" x2="1035.0" y2="251.0" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="213.5" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="1038.8" y1="159.6" x2="1038.8" y2="232.3" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="164.0" width="2.34" height="40.3" fill="var(--up)"/>
<line x1="1042.6" y1="132.2" x2="1042.6" y2="231.4" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="156.2" width="2.34" height="61.7" fill="var(--down)"/>
<line x1="1046.3" y1="227.9" x2="1046.3" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="231.5" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="1050.1" y1="214.2" x2="1050.1" y2="236.8" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="219.8" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="60" y1="560.4" x2="1052" y2="560.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="554.4" font-size="11.5" fill="var(--support)" font-weight="600">$102 S1</text>
<text x="1058" y="566.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="569.2" x2="1052" y2="569.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="563.2" font-size="11.5" fill="var(--support)" font-weight="600">$95 S2</text>
<text x="1058" y="575.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="585.3" x2="1052" y2="585.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="579.3" font-size="11.5" fill="var(--support)" font-weight="600">$82 S3</text>
<text x="1058" y="591.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="229.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="221.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $366 (2026-08-25)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$366.43** (2026-08-25 종가) | — | 기간 내 2회 이상 터치된 상단 저항 없음(신고가 근접 구간) |
| S1 | $102 | 4 | 2022년 1월(1/24)·3월(3/14)·2024년 11월(11/18)·2025년 1월(1/27) 스윙 저점 — 3년에 걸쳐 반복 형성된 가장 강한 장기 지지대 |
| S2 | $95 | 2 | 2023년 9월(9/11)·2024년 4월(4/15) 스윙 저점 |
| S3 | $82 | 3 | 2022년 7월(7/4)·12월(12/26)·2023년 10월(10/30) 스윙 저점 — 2022년 금리 인상기 약세장의 저점대 |
| 참고선 | $487.91 | — | 5년 최고가(2026-06-29 주간) — 터치 1회뿐이라 정식 저항 레벨로 포함하지 않고 참고선으로만 표시 |

> 현재가($366.43) 위쪽에는 2회 이상 터치된 유효 클러스터가 없다 — 2026년 상반기 AI 사이클 랠리로 주가가 단기간에 사상 최고가 부근까지 급등해 그 위로 반복 터치된 스윙 고점이 아직 쌓이지 않았기 때문이다. 억지로 저항 레벨을 만들지 않고 5년 최고가($487.91)만 참고선으로 남겼다.
>
> **아래쪽 세 지지대는 근시일 관점에서 사실상 의미가 없다.** S1($102)조차 현재가 대비 −72%이고, S3($82)는 −78%다. 이 레벨들은 "여기까지 빠질 수 있다"는 뜻이 아니라, **이 종목이 5년 사이 얼마나 다른 회사가 됐는지를 보여주는 눈금**으로 읽어야 한다 — 그 가격대가 형성되던 2022~2025년의 Teradyne은 매출 $2.7~3.2B에 다운사이클을 겪던 회사였고, 지금은 TTM 매출 $4.5B에 분기 영업이익률 30%대인 회사다([핵심 지표](./04_metrics.md) A.1·B). 근시일 지지/저항 판단은 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 쪽 레벨을 보는 것이 맞다.

---

## 3. 관측된 특이 구간 — 2025-04-07(주간) 관세 충격("Liberation Day") 저점

- 2025년 4월 초 미국의 신규 관세("Liberation Day") 발표로 촉발된 글로벌 증시 급락 국면에서, Teradyne 주가는 2025-03-31 주간 종가 $68.72에서 이어진 급락으로 **2025-04-07 주간 중 장중 $65.77(5년 최저가)**까지 밀렸다 — 보도 기준 이 관세 충격 기간 동안 주가는 고점 대비 약 −41.4% 하락한 것으로 전해졌다.
- 다만 그 주(2025-04-07 주간, 시가 $67.46 → 종가 $73.65) 자체는 전주 종가 대비 **+7.2%**로 마감했다 — 주 초반 급락 후 주 후반 반등한 전형적인 패닉·리바운드 패턴이다. 거래량은 3,143만 주로 5년 평균 주간 거래량(약 1,144만 주) 대비 약 2.7배.
- 이 저점은 Teradyne 고유의 악재가 아니라 관세발 거시 충격이라는 시장 전체의 사건과 궤를 같이한다. 이후 주가는 2025년 하반기~2026년 상반기에 걸쳐 AI 반도체 사이클 기대와 함께 가파르게 반등해, 저점($65.77) 대비 현재가($366.43)까지 **약 5.6배(+457%)** 상승했다 — [기술적 분석 — 일봉·1년](./09_technical_daily.md)에서 다루는 최근 1년의 극심한 변동성은 이 장기 반등 랠리 안에서 발생한 사건들이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-23~2026-08-25. 수집 시점: 2026-08-26. 원주가(과거 분할은 소급 반영 — 조사 기간 내 분할 없음, 배당은 미반영이나 배당수익률이 낮아(현재 0.14%) 배당락 영향은 무시할 만한 수준)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py TER --name Teradyne --interval 1wk --close-on 2026-08-25 --emit all` (파라미터는 스크립트 기본값 그대로 사용 — 강제 레벨 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 263개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - S1($102) 클러스터는 2022~2025년 서로 다른 3개 하락 국면의 스윙이 가격대만으로 묶인 것이다 — 클러스터링이 "가격 근접성"만 보고 시간 간격을 고려하지 않는 방법론적 한계를 보여주는 사례로, 실제로는 성격이 다른 세 번의 하락(금리 인상기·개별 조정·관세 충격)이 우연히 비슷한 가격대에서 멈춘 것이다.
    - **5년 구간 안에 이 회사의 펀더멘털 자체가 크게 바뀌었다**(FY2023 반도체 다운사이클 저점 → FY2026 AI 슈퍼사이클) — 2022~2023년의 스윙 레벨(S1·S2·S3)은 지금과는 완전히 다른 이익 수준·성장 전망 하에서 형성된 것이라 참고선 이상의 의미를 두기 어렵다. 이 문서의 지지 레벨 전부가 현재가 대비 −70% 아래에 있다는 사실 자체가 그 단절을 보여준다.
    - 기간 내 배당이 20회 있었으나 원주가 기준이라 반영하지 않았다.
    - 조사 기간(2021-08~2026-08) 내 주식분할·병합은 없었다 — 소급조정 이슈 없음.

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-26)*
