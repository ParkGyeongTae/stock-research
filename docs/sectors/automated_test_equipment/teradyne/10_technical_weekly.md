# Teradyne, Inc. (테라다인) — 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [`09_technical_daily.md`](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API(Yahoo Finance)에서 직접 수집했다(5년 주봉은 `04_metrics.md`가 다루는 범위 밖이라 단일 출처 규칙의 예외). 겹치는 시점의 종가를 대조한 결과: `2026-08-14` 종가 $418.79는 [`09_technical_daily.md`](./09_technical_daily.md)·[`01_overview.md`](./01_overview.md)·[`06_valuation.md`](./06_valuation.md)에 인용된 현재주가와 **일치**한다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="ter-chart">
<style>
.ter-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $418.79 (2026-08-14) · 단위 USD</text>
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
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.6" y1="626.0" x2="137.6" y2="631.0" class="axis"/>
<text x="137.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="334.5" y1="626.0" x2="334.5" y2="631.0" class="axis"/>
<text x="334.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="531.4" y1="626.0" x2="531.4" y2="631.0" class="axis"/>
<text x="531.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="732.1" y1="626.0" x2="732.1" y2="631.0" class="axis"/>
<text x="732.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.9" y1="626.0" x2="928.9" y2="631.0" class="axis"/>
<text x="928.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="77.4" x2="1052" y2="77.4" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="80.4" font-size="10.5" fill="var(--muted)">$488 5년 최고가(2026-06-29)</text>
<line x1="781.3" y1="56.0" x2="781.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="787.3" y="68.0" font-size="10.5" fill="var(--down)">2025-04-07 관세 충격(Liberation Day) 저점</text>
<line x1="61.9" y1="538.8" x2="61.9" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="540.4" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="65.7" y1="534.8" x2="65.7" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="535.1" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="69.5" y1="533.2" x2="69.5" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="534.0" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="73.3" y1="533.1" x2="73.3" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="535.6" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="77.0" y1="533.5" x2="77.0" y2="539.0" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="535.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="80.8" y1="537.2" x2="80.8" y2="545.0" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="539.1" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="84.6" y1="539.4" x2="84.6" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="540.4" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="88.4" y1="547.0" x2="88.4" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="551.4" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="92.2" y1="544.8" x2="92.2" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="545.9" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="96.0" y1="537.3" x2="96.0" y2="547.6" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="543.2" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="99.8" y1="514.8" x2="99.8" y2="544.4" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="515.5" width="2.35" height="27.7" fill="var(--up)"/>
<line x1="103.5" y1="504.8" x2="103.5" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="508.0" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="107.3" y1="505.3" x2="107.3" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="505.5" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="111.1" y1="496.1" x2="111.1" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="499.1" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="114.9" y1="495.1" x2="114.9" y2="506.5" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="498.1" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="118.7" y1="490.4" x2="118.7" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="500.0" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="122.5" y1="486.3" x2="122.5" y2="507.1" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="488.5" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="126.3" y1="484.4" x2="126.3" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="487.5" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="130.0" y1="483.0" x2="130.0" y2="494.6" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="484.8" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="133.8" y1="477.0" x2="133.8" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="483.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="137.6" y1="479.1" x2="137.6" y2="492.1" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="482.1" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="141.4" y1="478.6" x2="141.4" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="482.5" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="145.2" y1="486.2" x2="145.2" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="487.0" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="149.0" y1="503.3" x2="149.0" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="514.8" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="152.8" y1="537.6" x2="152.8" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="545.8" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="156.5" y1="535.6" x2="156.5" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="545.6" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="160.3" y1="538.3" x2="160.3" y2="549.5" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="544.8" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="164.1" y1="538.1" x2="164.1" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="538.3" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="167.9" y1="538.9" x2="167.9" y2="550.8" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="539.0" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="171.7" y1="546.0" x2="171.7" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="547.3" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="175.5" y1="533.5" x2="175.5" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="534.6" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="179.3" y1="533.1" x2="179.3" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="533.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="183.1" y1="529.2" x2="183.1" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="537.1" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="186.8" y1="538.1" x2="186.8" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="542.2" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="190.6" y1="549.2" x2="190.6" y2="555.8" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="554.2" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="194.4" y1="541.5" x2="194.4" y2="556.6" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="551.8" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="198.2" y1="544.0" x2="198.2" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="552.6" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="202.0" y1="545.6" x2="202.0" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="555.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="205.8" y1="552.8" x2="205.8" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="554.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="209.6" y1="552.3" x2="209.6" y2="566.3" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="555.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="213.3" y1="551.5" x2="213.3" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="551.6" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="217.1" y1="550.1" x2="217.1" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="552.1" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="220.9" y1="551.2" x2="220.9" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="552.0" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="224.7" y1="570.1" x2="224.7" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="571.4" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="228.5" y1="566.8" x2="228.5" y2="576.8" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="567.0" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="232.3" y1="564.3" x2="232.3" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="565.7" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="236.1" y1="572.8" x2="236.1" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="573.3" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="239.8" y1="571.2" x2="239.8" y2="579.1" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="571.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="243.6" y1="559.8" x2="243.6" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="562.8" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="247.4" y1="561.9" x2="247.4" y2="576.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="562.2" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="251.2" y1="560.0" x2="251.2" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="562.4" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="255.0" y1="556.8" x2="255.0" y2="574.5" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="557.9" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="258.8" y1="557.6" x2="258.8" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="558.4" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="262.6" y1="567.8" x2="262.6" y2="576.0" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="570.1" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="266.4" y1="575.1" x2="266.4" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="576.6" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="270.1" y1="575.9" x2="270.1" y2="586.1" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="577.3" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="273.9" y1="577.3" x2="273.9" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="577.3" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="277.7" y1="582.7" x2="277.7" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="586.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="281.5" y1="587.9" x2="281.5" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="589.4" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="285.3" y1="584.4" x2="285.3" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="591.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="289.1" y1="591.4" x2="289.1" y2="603.7" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="591.4" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="292.9" y1="591.6" x2="292.9" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="591.8" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="296.6" y1="581.9" x2="296.6" y2="592.6" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="584.2" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="300.4" y1="582.4" x2="300.4" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="582.5" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="304.2" y1="567.3" x2="304.2" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="568.0" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="308.0" y1="566.2" x2="308.0" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="569.8" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="311.8" y1="568.9" x2="311.8" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="572.6" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="315.6" y1="570.1" x2="315.6" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="572.5" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="319.4" y1="569.5" x2="319.4" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="572.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="323.1" y1="564.4" x2="323.1" y2="579.4" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="573.5" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="326.9" y1="575.9" x2="326.9" y2="583.7" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="576.6" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="330.7" y1="578.2" x2="330.7" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="579.2" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="334.5" y1="573.6" x2="334.5" y2="581.5" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="574.3" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="338.3" y1="565.6" x2="338.3" y2="572.9" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="566.6" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="342.1" y1="565.3" x2="342.1" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="566.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="345.9" y1="557.1" x2="345.9" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="559.1" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="349.6" y1="548.3" x2="349.6" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="553.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="353.4" y1="549.7" x2="353.4" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="554.1" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="357.2" y1="552.7" x2="357.2" y2="558.8" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="556.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="361.0" y1="557.9" x2="361.0" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="559.1" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="364.8" y1="559.1" x2="364.8" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="559.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="557.4" x2="368.6" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="558.9" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="372.4" y1="554.8" x2="372.4" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="557.0" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="376.2" y1="552.2" x2="376.2" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="555.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="379.9" y1="552.3" x2="379.9" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="554.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="383.7" y1="554.2" x2="383.7" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="555.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="387.5" y1="558.7" x2="387.5" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="562.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="391.3" y1="562.5" x2="391.3" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="565.9" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="395.1" y1="565.0" x2="395.1" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="565.9" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="398.9" y1="571.1" x2="398.9" y2="576.2" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="572.6" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="402.7" y1="572.2" x2="402.7" y2="577.2" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="572.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="406.4" y1="564.2" x2="406.4" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="567.0" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="410.2" y1="557.6" x2="410.2" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="558.7" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="414.0" y1="555.5" x2="414.0" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="555.5" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="417.8" y1="555.2" x2="417.8" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="557.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="421.6" y1="548.1" x2="421.6" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="549.5" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="425.4" y1="548.3" x2="425.4" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="549.5" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="429.2" y1="547.6" x2="429.2" y2="556.7" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="549.2" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="432.9" y1="548.2" x2="432.9" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="548.6" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="436.7" y1="544.6" x2="436.7" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="547.0" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="440.5" y1="541.3" x2="440.5" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="544.5" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="444.3" y1="539.3" x2="444.3" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="544.2" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="448.1" y1="546.3" x2="448.1" y2="556.0" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="548.0" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="451.9" y1="552.0" x2="451.9" y2="561.6" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="552.2" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="455.7" y1="557.4" x2="455.7" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="561.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="459.5" y1="555.1" x2="459.5" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="558.6" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="463.2" y1="551.9" x2="463.2" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="552.8" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="467.0" y1="553.4" x2="467.0" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="553.5" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="470.8" y1="562.1" x2="470.8" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="562.1" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="474.6" y1="564.7" x2="474.6" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="569.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="478.4" y1="561.4" x2="478.4" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="562.8" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="482.2" y1="561.3" x2="482.2" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="562.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="486.0" y1="561.5" x2="486.0" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="564.1" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="489.7" y1="566.6" x2="489.7" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="568.8" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="493.5" y1="572.4" x2="493.5" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="574.6" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="497.3" y1="578.0" x2="497.3" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="578.8" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="501.1" y1="577.8" x2="501.1" y2="582.6" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="578.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="504.9" y1="572.8" x2="504.9" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="573.3" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="508.7" y1="571.0" x2="508.7" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="572.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="512.5" y1="570.7" x2="512.5" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="571.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="516.2" y1="571.4" x2="516.2" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="572.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="520.0" y1="555.5" x2="520.0" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="556.9" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="523.8" y1="553.6" x2="523.8" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="553.8" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="527.6" y1="549.3" x2="527.6" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="552.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="531.4" y1="554.6" x2="531.4" y2="563.4" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="554.6" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="535.2" y1="555.7" x2="535.2" y2="559.7" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="557.3" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="539.0" y1="552.0" x2="539.0" y2="562.4" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="552.4" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="542.7" y1="546.3" x2="542.7" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="550.8" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="546.5" y1="555.3" x2="546.5" y2="573.0" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="558.1" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="550.3" y1="560.3" x2="550.3" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="560.5" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="554.1" y1="557.4" x2="554.1" y2="566.5" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="560.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="557.9" y1="559.2" x2="557.9" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="562.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="561.7" y1="554.9" x2="561.7" y2="564.9" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="556.0" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="565.5" y1="549.7" x2="565.5" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="555.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="569.3" y1="552.8" x2="569.3" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="556.1" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="573.0" y1="547.1" x2="573.0" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="549.9" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="576.8" y1="546.7" x2="576.8" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="547.3" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="580.6" y1="544.8" x2="580.6" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="547.3" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="584.4" y1="549.3" x2="584.4" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="553.4" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="588.2" y1="553.4" x2="588.2" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="554.0" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="592.0" y1="545.0" x2="592.0" y2="568.1" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="545.7" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="595.8" y1="536.0" x2="595.8" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="537.8" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="599.5" y1="533.2" x2="599.5" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="534.6" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="603.3" y1="521.4" x2="603.3" y2="534.7" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="523.4" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="607.1" y1="506.2" x2="607.1" y2="519.9" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="508.2" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="610.9" y1="505.1" x2="610.9" y2="518.3" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="508.0" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="614.7" y1="506.2" x2="614.7" y2="515.0" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="508.4" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="618.5" y1="497.9" x2="618.5" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="506.9" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="622.3" y1="498.3" x2="622.3" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="502.7" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="626.0" y1="498.8" x2="626.0" y2="507.9" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="502.9" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="629.8" y1="497.4" x2="629.8" y2="506.5" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="499.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="633.6" y1="486.7" x2="633.6" y2="498.4" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="492.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="637.4" y1="484.2" x2="637.4" y2="505.7" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="491.7" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="641.2" y1="494.2" x2="641.2" y2="537.9" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="499.5" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="645.0" y1="523.8" x2="645.0" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="527.8" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="648.8" y1="534.2" x2="648.8" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="536.2" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="652.5" y1="521.4" x2="652.5" y2="537.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="521.9" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="656.3" y1="516.4" x2="656.3" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="518.3" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="660.1" y1="515.6" x2="660.1" y2="525.0" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="517.3" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="663.9" y1="520.4" x2="663.9" y2="538.5" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="521.4" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="667.7" y1="523.0" x2="667.7" y2="535.9" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="524.2" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="671.5" y1="518.3" x2="671.5" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="527.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="675.3" y1="515.2" x2="675.3" y2="527.1" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="520.0" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="679.1" y1="520.4" x2="679.1" y2="528.5" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="522.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="682.8" y1="523.0" x2="682.8" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="523.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="686.6" y1="519.1" x2="686.6" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="523.7" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="690.4" y1="530.1" x2="690.4" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="531.2" width="2.35" height="17.5" fill="var(--down)"/>
<line x1="694.2" y1="546.1" x2="694.2" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="548.5" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="698.0" y1="547.8" x2="698.0" y2="558.7" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="549.7" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="701.8" y1="550.0" x2="701.8" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="550.2" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="705.6" y1="553.0" x2="705.6" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="553.1" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="709.3" y1="547.9" x2="709.3" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="549.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="713.1" y1="538.6" x2="713.1" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="540.2" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="716.9" y1="532.8" x2="716.9" y2="543.2" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="534.3" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="720.7" y1="521.6" x2="720.7" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="528.4" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="724.5" y1="523.4" x2="724.5" y2="531.1" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="527.6" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="728.3" y1="524.0" x2="728.3" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="525.0" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="732.1" y1="508.0" x2="732.1" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="518.8" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="735.8" y1="513.3" x2="735.8" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="515.3" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="739.6" y1="518.0" x2="739.6" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="519.5" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="743.4" y1="531.6" x2="743.4" y2="562.4" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="532.6" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="747.2" y1="545.1" x2="747.2" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="546.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="751.0" y1="544.5" x2="751.0" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="544.8" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="754.8" y1="537.5" x2="754.8" y2="546.4" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="543.4" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="758.6" y1="542.4" x2="758.6" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="543.2" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="762.4" y1="548.7" x2="762.4" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="549.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="766.1" y1="555.8" x2="766.1" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="555.9" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="769.9" y1="574.8" x2="769.9" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="579.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="773.7" y1="574.3" x2="773.7" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="576.2" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="777.5" y1="582.3" x2="777.5" y2="604.6" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="586.7" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="781.3" y1="587.9" x2="781.3" y2="606.2" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="596.4" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="785.1" y1="593.4" x2="785.1" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="594.0" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="788.9" y1="591.3" x2="788.9" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="592.0" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="792.6" y1="590.1" x2="792.6" y2="599.4" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="592.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="796.4" y1="590.5" x2="796.4" y2="597.0" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="591.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="800.2" y1="581.1" x2="800.2" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="584.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="804.0" y1="585.9" x2="804.0" y2="593.4" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="587.7" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="807.8" y1="585.3" x2="807.8" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="589.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="811.6" y1="581.2" x2="811.6" y2="591.2" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="581.9" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="815.4" y1="576.4" x2="815.4" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="580.8" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="819.1" y1="577.7" x2="819.1" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="580.5" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="822.9" y1="573.7" x2="822.9" y2="581.4" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="575.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="826.7" y1="569.4" x2="826.7" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="572.1" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="830.5" y1="564.3" x2="830.5" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="567.1" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="834.3" y1="565.7" x2="834.3" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="567.1" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="838.1" y1="566.8" x2="838.1" y2="576.3" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="568.6" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="841.9" y1="546.5" x2="841.9" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="558.2" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="845.6" y1="552.9" x2="845.6" y2="559.6" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="554.0" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="849.4" y1="545.4" x2="849.4" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="551.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="853.2" y1="541.9" x2="853.2" y2="555.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="544.2" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="857.0" y1="538.1" x2="857.0" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="540.5" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="860.8" y1="534.0" x2="860.8" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="538.1" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="864.6" y1="536.7" x2="864.6" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="538.0" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="868.4" y1="537.6" x2="868.4" y2="549.7" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="538.5" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="872.2" y1="515.5" x2="872.2" y2="530.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="519.1" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="875.9" y1="501.4" x2="875.9" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="506.2" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="879.7" y1="499.8" x2="879.7" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="503.4" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="883.5" y1="509.4" x2="883.5" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="514.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="887.3" y1="502.0" x2="887.3" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="507.9" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="891.1" y1="455.7" x2="891.1" y2="508.1" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="460.9" width="2.35" height="42.2" fill="var(--up)"/>
<line x1="894.9" y1="448.7" x2="894.9" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="459.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="898.7" y1="452.2" x2="898.7" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="452.6" width="2.35" height="23.1" fill="var(--down)"/>
<line x1="902.4" y1="470.9" x2="902.4" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="477.6" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="906.2" y1="460.4" x2="906.2" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="460.8" width="2.35" height="27.4" fill="var(--up)"/>
<line x1="910.0" y1="434.2" x2="910.0" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="437.1" width="2.35" height="27.1" fill="var(--up)"/>
<line x1="913.8" y1="431.8" x2="913.8" y2="448.3" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="434.3" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="917.6" y1="437.5" x2="917.6" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="438.2" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="921.4" y1="435.6" x2="921.4" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="436.8" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="925.2" y1="427.1" x2="925.2" y2="446.4" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="428.6" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="928.9" y1="400.9" x2="928.9" y2="423.3" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="416.5" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="932.7" y1="389.3" x2="932.7" y2="417.3" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="402.8" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="936.5" y1="390.5" x2="936.5" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="401.5" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="940.3" y1="368.9" x2="940.3" y2="404.2" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="386.7" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="944.1" y1="311.1" x2="944.1" y2="387.1" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="312.7" width="2.35" height="74.0" fill="var(--up)"/>
<line x1="947.9" y1="277.7" x2="947.9" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="294.4" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="951.7" y1="279.0" x2="951.7" y2="312.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="281.7" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="955.5" y1="256.5" x2="955.5" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="287.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="959.2" y1="280.3" x2="959.2" y2="351.5" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="299.7" width="2.35" height="46.9" fill="var(--down)"/>
<line x1="963.0" y1="297.0" x2="963.0" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="329.8" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="966.8" y1="303.0" x2="966.8" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="317.9" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="970.6" y1="278.5" x2="970.6" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="311.5" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="974.4" y1="291.8" x2="974.4" y2="346.5" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="300.8" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="978.2" y1="221.4" x2="978.2" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="227.6" width="2.35" height="70.0" fill="var(--up)"/>
<line x1="982.0" y1="210.8" x2="982.0" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="212.1" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="985.7" y1="159.8" x2="985.7" y2="221.4" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="164.9" width="2.35" height="44.3" fill="var(--up)"/>
<line x1="989.5" y1="160.7" x2="989.5" y2="310.5" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="160.7" width="2.35" height="95.2" fill="var(--down)"/>
<line x1="993.3" y1="208.8" x2="993.3" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="237.9" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="997.1" y1="228.3" x2="997.1" y2="268.6" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="243.1" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="1000.9" y1="237.2" x2="1000.9" y2="301.0" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="239.6" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="1004.7" y1="179.2" x2="1004.7" y2="231.6" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="219.7" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1008.5" y1="161.7" x2="1008.5" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="229.5" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="1012.2" y1="177.5" x2="1012.2" y2="262.3" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="183.5" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="1016.0" y1="136.5" x2="1016.0" y2="177.2" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="140.0" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="1019.8" y1="96.9" x2="1019.8" y2="176.6" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="117.2" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="1023.6" y1="77.4" x2="1023.6" y2="235.1" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="136.7" width="2.35" height="89.6" fill="var(--down)"/>
<line x1="1027.4" y1="187.8" x2="1027.4" y2="277.4" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="204.4" width="2.35" height="33.8" fill="var(--down)"/>
<line x1="1031.2" y1="231.4" x2="1031.2" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="256.4" width="2.35" height="28.4" fill="var(--down)"/>
<line x1="1035.0" y1="213.6" x2="1035.0" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="250.3" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="1038.7" y1="197.6" x2="1038.7" y2="311.6" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="228.0" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="1042.5" y1="175.4" x2="1042.5" y2="251.0" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="213.5" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="1046.3" y1="159.6" x2="1046.3" y2="232.3" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="164.0" width="2.35" height="40.3" fill="var(--up)"/>
<line x1="1050.1" y1="163.7" x2="1050.1" y2="189.5" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="164.0" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="60" y1="560.4" x2="1052" y2="560.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="554.4" font-size="11.5" fill="var(--support)" font-weight="600">$102 S1</text>
<text x="1058" y="566.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="569.2" x2="1052" y2="569.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="563.2" font-size="11.5" fill="var(--support)" font-weight="600">$95 S2</text>
<text x="1058" y="575.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="585.3" x2="1052" y2="585.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="579.3" font-size="11.5" fill="var(--support)" font-weight="600">$82 S3</text>
<text x="1058" y="591.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="164.0" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고). `09_technical_daily.md`의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$418.79** (2026-08-14 종가) | — | 기간 내 2회 이상 터치된 상단 저항 없음(신고가 근접 구간) |
| S1 | $102 | 4 | 2022년 1월(1/24)·3월(3/14)·2024년 11월(11/18)·2025년 1월(1/27) 스윙 저점 — 3년에 걸쳐 반복 형성된 가장 강한 장기 지지대 |
| S2 | $95 | 2 | 2023년 9월(9/11)·2024년 4월(4/15) 스윙 저점 |
| S3 | $82 | 3 | 2022년 7월(7/4)·12월(12/26)·2023년 10월(10/30) 스윙 저점 — 2022년 금리 인상기 약세장의 저점대 |
| 참고선 | $488 | — | 5년 최고가(2026-06-29) — 터치 1회뿐이라 정식 저항 레벨로 포함하지 않고 참고선으로만 표시 |

> 현재가($418.79) 위쪽에는 2회 이상 터치된 유효 클러스터가 없다 — 2026년 상반기 AI 사이클 랠리로 주가가 단기간에 사상 최고가 부근까지 급등해 그 위로 반복 터치된 스윙 고점이 아직 쌓이지 않았기 때문이다. 억지로 저항 레벨을 만들지 않고 5년 최고가($487.91)만 참고선으로 남겼다. 아래쪽 S1($102)은 2022~2025년 세 차례 하락 국면(2022년 금리 인상기, 2024년 조정, 2025년 관세 충격)에 걸쳐 반복적으로 방어된, 이 종목에서 가장 오래되고 강한 지지대다 — 다만 현재가 대비 −76% 떨어진 가격이라 근시일 관점에서는 의미가 제한적이다.

---

## 3. 관측된 특이 구간 — 2025-04-07(주간) 관세 충격("Liberation Day") 저점

- 2025년 4월 초 미국의 신규 관세("Liberation Day") 발표로 촉발된 글로벌 증시 급락 국면에서, Teradyne 주가는 2025-03-31 주간 종가 $68.72에서 이어진 급락으로 **2025-04-07 주간 중 장중 $65.77(5년 최저가)**까지 밀렸다 — 검색 결과 기준 이 관세 충격 기간 동안 주가는 고점 대비 약 -41.4% 하락한 것으로 보도됐다.
- 다만 그 주(2025-04-07 주간, 시가 $67.46 → 종가 $73.65) 자체는 전주 종가 대비 **+7.2%**로 마감했다 — 주 초반 급락 후 주 후반 반등한 전형적인 패닉·리바운드 패턴이다. 거래량은 3,143만 주로 5년 평균 주간 거래량(약 1,145만 주) 대비 약 2.7배.
- 이 저점은 Teradyne 고유의 악재가 아니라 관세发 거시 충격이라는 시장 전체의 사건과 궤를 같이한다. 이후 주가는 2025년 하반기~2026년 상반기에 걸쳐 AI 반도체 사이클 기대와 함께 가파르게 반등해, 저점($65.77) 대비 현재가($418.79)까지 약 5.4배 상승했다 — [`09_technical_daily.md`](./09_technical_daily.md)에서 다루는 최근 1년의 극심한 변동성(§3-A·3-B)은 이 장기 반등 랠리 안에서 발생한 사건들이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영 — 조사 기간 내 분할 없음, 배당은 미반영이나 배당수익률이 낮아(현재 0.12%) 배당락 영향은 무시할 만한 수준)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. `09_technical_daily.md`(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py TER --name Teradyne --interval 1wk --event 2025-04-07:"관세 충격(Liberation Day) 저점" --ref-line 487.91:"5년 최고가(2026-06-29)" --close-on 2026-08-14 --emit all` (파라미터는 스크립트 기본값 그대로 사용 — 강제 레벨 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - S1($102) 클러스터는 2022~2025년 서로 다른 3개 하락 국면의 스윙이 가격대만으로 묶인 것이다 — 클러스터링이 "가격 근접성"만 보고 시간 간격을 고려하지 않는 방법론적 한계를 보여주는 사례로, 실제로는 성격이 다른 세 번의 하락(금리 인상기·개별 조정·관세 충격)이 우연히 비슷한 가격대에서 멈춘 것이다.
    - 5년 구간 안에 이 회사의 펀더멘털 자체가 크게 바뀌었다(FY2023 반도체 다운사이클 저점 → FY2026 AI 슈퍼사이클) — 2022~2023년의 스윙 레벨(S2·S3)은 지금과는 완전히 다른 이익 수준·성장 전망 하에서 형성된 것이라 참고선 이상의 의미를 두기 어렵다.
    - 조사 기간(2021-08~2026-08) 내 주식분할·병합은 없었다 — 소급조정 이슈 없음.

---

## 관련 문서

같은 폴더 내 다른 문서로 이동:

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 일봉·1년](./09_technical_daily.md)

---

## 참고 자료

- [Yahoo Finance — Teradyne, Inc. (TER) 주봉 시세](https://finance.yahoo.com/quote/TER/history/) (수집 2026-08-16)
- [stockanalysis.com — Teradyne 주가 이력 API 교차 확인](https://stockanalysis.com/stocks/TER/history/)

---

*작성일: 2026-08-16*
