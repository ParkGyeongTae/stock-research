# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 마지막 캔들의 종가 **$64.39(2026-08-28)**는 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 기준일로 쓰는 값과 **일치한다.** 다만 그 마지막 캔들은 한 주가 아니라 **1거래일짜리 부분 봉**이다(4. 방법론 · 한계 참고) — 같은 원자료에서 2026-08-24 주(월~목)의 종가는 $67.53이다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

<div class="rklb-chart">
<style>
.rklb-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .rklb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .rklb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.rklb-chart svg { width:100%; height:auto; display:block; }
.rklb-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.rklb-chart .title { fill: var(--ink); font-weight:600; }
.rklb-chart .grid { stroke: var(--grid); stroke-width:1; }
.rklb-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Rocket Lab(RKLB) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Rocket Lab (RKLB) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $64.39 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="617.1" x2="1052" y2="617.1" class="grid"/>
<text x="52" y="621.1" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="545.8" x2="1052" y2="545.8" class="grid"/>
<text x="52" y="549.8" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="474.6" x2="1052" y2="474.6" class="grid"/>
<text x="52" y="478.6" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="403.3" x2="1052" y2="403.3" class="grid"/>
<text x="52" y="407.3" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="332.1" x2="1052" y2="332.1" class="grid"/>
<text x="52" y="336.1" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="260.8" x2="1052" y2="260.8" class="grid"/>
<text x="52" y="264.8" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="189.6" x2="1052" y2="189.6" class="grid"/>
<text x="52" y="193.6" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="118.3" x2="1052" y2="118.3" class="grid"/>
<text x="52" y="122.3" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.0" y1="56.0" x2="130.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.0" y1="626.0" x2="130.0" y2="631.0" class="axis"/>
<text x="130.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="326.9" y1="56.0" x2="326.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="326.9" y1="626.0" x2="326.9" y2="631.0" class="axis"/>
<text x="326.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="523.8" y1="56.0" x2="523.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="523.8" y1="626.0" x2="523.8" y2="631.0" class="axis"/>
<text x="523.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="724.5" y1="56.0" x2="724.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="724.5" y1="626.0" x2="724.5" y2="631.0" class="axis"/>
<text x="724.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.4" y1="56.0" x2="921.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.4" y1="626.0" x2="921.4" y2="631.0" class="axis"/>
<text x="921.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="81.9" x2="1052" y2="81.9" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="84.9" font-size="10.5" fill="var(--muted)">$150 5년 최고 종가 (2026-05)</text>
<line x1="61.9" y1="566.0" x2="61.9" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="568.9" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="65.7" y1="541.1" x2="65.7" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="550.5" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="69.5" y1="551.5" x2="69.5" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="551.6" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="73.3" y1="562.2" x2="73.3" y2="569.1" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="564.4" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="77.0" y1="558.6" x2="77.0" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="560.2" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="80.8" y1="559.7" x2="80.8" y2="567.9" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="560.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="84.6" y1="564.8" x2="84.6" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="564.9" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="88.4" y1="570.3" x2="88.4" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="570.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="92.2" y1="566.7" x2="92.2" y2="572.0" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="567.0" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="96.0" y1="559.2" x2="96.0" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="561.8" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="99.8" y1="560.7" x2="99.8" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="560.8" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="103.5" y1="557.4" x2="103.5" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="561.9" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="107.3" y1="558.8" x2="107.3" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="561.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="111.1" y1="556.6" x2="111.1" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="561.8" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="114.9" y1="570.0" x2="114.9" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="570.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="118.7" y1="570.3" x2="118.7" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="571.8" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="122.5" y1="572.9" x2="122.5" y2="575.7" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="574.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="126.3" y1="572.7" x2="126.3" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="573.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="130.0" y1="573.2" x2="130.0" y2="581.1" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="573.3" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="133.8" y1="575.3" x2="133.8" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="578.7" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="137.6" y1="579.4" x2="137.6" y2="585.2" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="580.5" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="141.4" y1="584.8" x2="141.4" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="586.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="145.2" y1="582.6" x2="145.2" y2="587.3" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="583.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="149.0" y1="577.5" x2="149.0" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="582.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="152.8" y1="580.6" x2="152.8" y2="586.0" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="582.9" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="156.5" y1="581.7" x2="156.5" y2="587.9" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="583.4" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="160.3" y1="582.3" x2="160.3" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="583.1" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="164.1" y1="584.9" x2="164.1" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="586.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="167.9" y1="583.3" x2="167.9" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="584.8" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="171.7" y1="583.6" x2="171.7" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="585.0" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="175.5" y1="586.9" x2="175.5" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="588.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="179.3" y1="587.2" x2="179.3" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="588.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="183.1" y1="586.9" x2="183.1" y2="589.8" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="587.1" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="186.8" y1="586.0" x2="186.8" y2="590.1" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="587.2" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="190.6" y1="589.0" x2="190.6" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="589.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="194.4" y1="590.0" x2="194.4" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="590.8" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="198.2" y1="594.3" x2="198.2" y2="599.5" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="594.8" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="202.0" y1="596.1" x2="202.0" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="596.4" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="205.8" y1="598.7" x2="205.8" y2="601.9" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="599.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="209.6" y1="598.7" x2="209.6" y2="600.7" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="599.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="213.3" y1="598.8" x2="213.3" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="598.9" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="217.1" y1="601.5" x2="217.1" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="602.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="220.9" y1="601.3" x2="220.9" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="601.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="224.7" y1="601.7" x2="224.7" y2="604.5" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="602.2" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="228.5" y1="601.8" x2="228.5" y2="604.3" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="602.0" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="232.3" y1="602.0" x2="232.3" y2="603.7" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="602.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="236.1" y1="601.0" x2="236.1" y2="603.0" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="602.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="239.8" y1="600.4" x2="239.8" y2="603.0" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="600.5" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="243.6" y1="597.2" x2="243.6" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="598.1" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="247.4" y1="591.6" x2="247.4" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="591.8" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="251.2" y1="591.1" x2="251.2" y2="597.2" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="591.5" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="255.0" y1="596.8" x2="255.0" y2="598.8" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="597.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="258.8" y1="596.0" x2="258.8" y2="599.5" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="598.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="262.6" y1="596.5" x2="262.6" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="597.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="266.4" y1="596.0" x2="266.4" y2="599.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="597.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="270.1" y1="598.6" x2="270.1" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="599.4" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="273.9" y1="601.3" x2="273.9" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="602.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="277.7" y1="600.1" x2="277.7" y2="602.8" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="601.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="281.5" y1="601.4" x2="281.5" y2="603.7" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="601.6" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="285.3" y1="601.1" x2="285.3" y2="602.8" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="602.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="289.1" y1="598.5" x2="289.1" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="598.8" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="292.9" y1="598.0" x2="292.9" y2="600.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="598.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="296.6" y1="596.6" x2="296.6" y2="600.2" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="597.0" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="300.4" y1="597.2" x2="300.4" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="597.3" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="304.2" y1="600.5" x2="304.2" y2="602.3" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="600.7" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="308.0" y1="601.8" x2="308.0" y2="603.3" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="602.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="311.8" y1="601.6" x2="311.8" y2="603.3" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="601.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="315.6" y1="601.1" x2="315.6" y2="603.0" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="602.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="319.4" y1="602.6" x2="319.4" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="602.6" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="323.1" y1="603.5" x2="323.1" y2="604.7" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="603.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="326.9" y1="601.9" x2="326.9" y2="603.6" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="602.0" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="330.7" y1="598.9" x2="330.7" y2="602.5" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="599.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="334.5" y1="596.9" x2="334.5" y2="600.4" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="599.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="338.3" y1="599.1" x2="338.3" y2="600.7" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="599.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="342.1" y1="597.6" x2="342.1" y2="600.1" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="598.2" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="345.9" y1="598.3" x2="345.9" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="598.5" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="349.6" y1="598.5" x2="349.6" y2="600.7" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="599.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="353.4" y1="599.7" x2="353.4" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="599.9" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="357.2" y1="600.5" x2="357.2" y2="602.2" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="600.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="361.0" y1="600.7" x2="361.0" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="600.8" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="364.8" y1="602.6" x2="364.8" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="603.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="602.9" x2="368.6" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="603.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="372.4" y1="602.3" x2="372.4" y2="603.4" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="602.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="376.2" y1="602.5" x2="376.2" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="602.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="379.9" y1="602.3" x2="379.9" y2="603.8" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="602.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="383.7" y1="602.1" x2="383.7" y2="603.3" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="602.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="387.5" y1="602.6" x2="387.5" y2="603.8" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="602.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="391.3" y1="602.8" x2="391.3" y2="603.7" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="603.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="395.1" y1="601.5" x2="395.1" y2="603.7" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="602.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="600.4" x2="398.9" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="600.5" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="402.7" y1="599.2" x2="402.7" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="600.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="406.4" y1="599.5" x2="406.4" y2="601.2" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="599.6" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="410.2" y1="597.8" x2="410.2" y2="600.0" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="598.5" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="414.0" y1="595.4" x2="414.0" y2="598.9" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="597.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="417.8" y1="595.9" x2="417.8" y2="597.4" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="597.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="421.6" y1="595.2" x2="421.6" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="595.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="425.4" y1="595.5" x2="425.4" y2="597.4" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="595.6" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="429.2" y1="592.7" x2="429.2" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="594.6" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="432.9" y1="588.4" x2="432.9" y2="595.0" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="590.4" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="436.7" y1="589.3" x2="436.7" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="590.5" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="440.5" y1="590.7" x2="440.5" y2="592.9" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="591.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="444.3" y1="590.4" x2="444.3" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="592.6" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="448.1" y1="594.4" x2="448.1" y2="598.0" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="594.9" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="451.9" y1="595.4" x2="451.9" y2="597.1" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="595.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="455.7" y1="594.0" x2="455.7" y2="596.3" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="594.5" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="459.5" y1="593.6" x2="459.5" y2="595.5" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="594.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="463.2" y1="594.5" x2="463.2" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="594.8" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="467.0" y1="598.5" x2="467.0" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="598.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="470.8" y1="600.8" x2="470.8" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="601.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="474.6" y1="601.0" x2="474.6" y2="602.4" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="601.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="478.4" y1="599.0" x2="478.4" y2="602.0" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="601.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="482.2" y1="601.0" x2="482.2" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="601.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="486.0" y1="601.5" x2="486.0" y2="602.8" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="602.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="489.7" y1="600.0" x2="489.7" y2="602.5" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="600.7" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="493.5" y1="600.5" x2="493.5" y2="602.1" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="600.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="497.3" y1="600.5" x2="497.3" y2="602.3" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="601.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="501.1" y1="601.4" x2="501.1" y2="602.2" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="601.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="504.9" y1="600.6" x2="504.9" y2="602.3" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="601.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="508.7" y1="599.5" x2="508.7" y2="601.3" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="600.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="512.5" y1="597.6" x2="512.5" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="600.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="516.2" y1="596.6" x2="516.2" y2="601.6" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="597.7" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="520.0" y1="595.2" x2="520.0" y2="597.9" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="597.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="523.8" y1="597.1" x2="523.8" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="597.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="527.6" y1="596.9" x2="527.6" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="597.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="531.4" y1="598.7" x2="531.4" y2="600.4" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="598.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="535.2" y1="598.4" x2="535.2" y2="599.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="599.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="539.0" y1="598.7" x2="539.0" y2="603.2" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="599.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="542.7" y1="601.2" x2="542.7" y2="603.0" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="601.6" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="546.5" y1="599.0" x2="546.5" y2="601.5" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="599.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="550.3" y1="598.9" x2="550.3" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="599.6" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="554.1" y1="600.0" x2="554.1" y2="602.5" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="600.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="557.9" y1="600.4" x2="557.9" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="600.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="561.7" y1="600.3" x2="561.7" y2="602.5" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="601.3" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="565.5" y1="601.8" x2="565.5" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="602.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="569.3" y1="602.0" x2="569.3" y2="602.7" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="602.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="573.0" y1="602.3" x2="573.0" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="602.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="576.8" y1="603.0" x2="576.8" y2="604.1" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="603.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="580.6" y1="603.6" x2="580.6" y2="604.7" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="603.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="584.4" y1="603.6" x2="584.4" y2="604.7" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="603.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="588.2" y1="602.6" x2="588.2" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="602.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="592.0" y1="601.8" x2="592.0" y2="604.1" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="602.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="595.8" y1="600.6" x2="595.8" y2="602.3" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="602.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="599.5" y1="601.0" x2="599.5" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="601.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="603.3" y1="601.2" x2="603.3" y2="602.3" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="601.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="607.1" y1="601.2" x2="607.1" y2="602.0" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="601.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="610.9" y1="599.5" x2="610.9" y2="601.7" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="601.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="614.7" y1="598.9" x2="614.7" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="599.2" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="618.5" y1="598.7" x2="618.5" y2="600.5" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="599.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="622.3" y1="599.7" x2="622.3" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="599.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="626.0" y1="596.9" x2="626.0" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="597.0" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="629.8" y1="596.3" x2="629.8" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="597.2" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="633.6" y1="597.4" x2="633.6" y2="599.0" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="597.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="637.4" y1="597.5" x2="637.4" y2="600.5" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="597.8" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="641.2" y1="597.2" x2="641.2" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="598.0" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="645.0" y1="591.8" x2="645.0" y2="599.2" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="593.7" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="648.8" y1="590.9" x2="648.8" y2="594.9" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="592.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="652.5" y1="592.3" x2="652.5" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="592.3" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="656.3" y1="594.0" x2="656.3" y2="596.6" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="595.0" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="660.1" y1="590.5" x2="660.1" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="590.5" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="663.9" y1="589.6" x2="663.9" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="590.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="667.7" y1="580.4" x2="667.7" y2="591.2" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="582.3" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="671.5" y1="580.9" x2="671.5" y2="585.7" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="581.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="675.3" y1="581.0" x2="675.3" y2="585.1" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="581.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="679.1" y1="577.2" x2="679.1" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="578.6" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="682.8" y1="574.0" x2="682.8" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="577.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="686.6" y1="575.7" x2="686.6" y2="580.4" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="576.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="690.4" y1="567.6" x2="690.4" y2="578.0" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="569.0" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="694.2" y1="536.8" x2="694.2" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="549.4" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="698.0" y1="532.3" x2="698.0" y2="551.3" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="534.2" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="701.8" y1="517.2" x2="701.8" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="519.9" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="705.6" y1="517.0" x2="705.6" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="517.4" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="709.3" y1="527.7" x2="709.3" y2="539.2" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="528.2" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="713.1" y1="521.7" x2="713.1" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="528.5" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="716.9" y1="514.5" x2="716.9" y2="530.4" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="520.1" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="720.7" y1="514.6" x2="720.7" y2="532.7" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="514.7" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="724.5" y1="509.3" x2="724.5" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="513.8" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="728.3" y1="522.7" x2="728.3" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="526.1" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="732.1" y1="498.3" x2="732.1" y2="526.2" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="508.9" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="735.8" y1="507.3" x2="735.8" y2="518.2" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="513.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="739.6" y1="509.6" x2="739.6" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="519.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="743.4" y1="506.4" x2="743.4" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="517.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="747.2" y1="511.0" x2="747.2" y2="533.9" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="516.4" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="751.0" y1="532.0" x2="751.0" y2="559.5" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="532.5" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="754.8" y1="540.7" x2="754.8" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="541.4" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="758.6" y1="548.1" x2="758.6" y2="559.9" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="550.1" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="762.4" y1="546.0" x2="762.4" y2="553.8" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="549.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="766.1" y1="544.2" x2="766.1" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="547.8" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="769.9" y1="546.7" x2="769.9" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="553.4" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="773.7" y1="540.9" x2="773.7" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="547.2" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="777.5" y1="538.4" x2="777.5" y2="550.6" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="544.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="781.3" y1="536.7" x2="781.3" y2="552.2" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="537.4" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="785.1" y1="532.4" x2="785.1" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="534.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="788.9" y1="534.4" x2="788.9" y2="545.0" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="536.7" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="792.6" y1="525.4" x2="792.6" y2="542.7" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="526.0" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="796.4" y1="522.1" x2="796.4" y2="531.9" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="526.5" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="800.2" y1="507.4" x2="800.2" y2="524.4" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="521.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="804.0" y1="513.5" x2="804.0" y2="526.2" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="514.1" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="807.8" y1="500.6" x2="807.8" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="510.2" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="811.6" y1="509.8" x2="811.6" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="510.1" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="815.4" y1="482.9" x2="815.4" y2="515.8" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="491.1" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="819.1" y1="480.8" x2="819.1" y2="496.9" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="486.9" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="822.9" y1="473.5" x2="822.9" y2="491.4" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="478.0" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="826.7" y1="426.7" x2="826.7" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="434.0" width="2.35" height="43.1" fill="var(--up)"/>
<line x1="830.5" y1="433.3" x2="830.5" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="438.8" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="834.3" y1="445.5" x2="834.3" y2="466.3" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="446.3" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="838.1" y1="439.3" x2="838.1" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="456.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="841.9" y1="448.7" x2="841.9" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="458.0" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="845.6" y1="449.4" x2="845.6" y2="480.8" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="459.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="849.4" y1="435.7" x2="849.4" y2="460.2" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="444.0" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="853.2" y1="435.8" x2="853.2" y2="466.1" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="450.5" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="857.0" y1="424.6" x2="857.0" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="427.1" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="860.8" y1="420.6" x2="860.8" y2="451.6" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="426.2" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="864.6" y1="424.2" x2="864.6" y2="456.0" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="449.2" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="868.4" y1="414.2" x2="868.4" y2="451.9" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="417.0" width="2.35" height="31.2" fill="var(--up)"/>
<line x1="872.2" y1="355.2" x2="872.2" y2="418.3" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="388.2" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="875.9" y1="353.6" x2="875.9" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="375.3" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="879.7" y1="360.0" x2="879.7" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="370.8" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="883.5" y1="377.0" x2="883.5" y2="401.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="381.3" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="887.3" y1="392.3" x2="887.3" y2="452.1" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="392.5" width="2.35" height="40.6" fill="var(--down)"/>
<line x1="891.1" y1="414.2" x2="891.1" y2="462.8" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="425.6" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="894.9" y1="452.3" x2="894.9" y2="483.3" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="456.2" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="898.7" y1="461.8" x2="898.7" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="467.0" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="902.4" y1="440.0" x2="902.4" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="442.3" width="2.35" height="28.2" fill="var(--up)"/>
<line x1="906.2" y1="384.9" x2="906.2" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="398.0" width="2.35" height="40.6" fill="var(--up)"/>
<line x1="910.0" y1="365.7" x2="910.0" y2="429.4" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="365.9" width="2.35" height="26.6" fill="var(--up)"/>
<line x1="913.8" y1="332.7" x2="913.8" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="357.2" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="917.6" y1="345.5" x2="917.6" y2="378.9" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="346.4" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="921.4" y1="296.9" x2="921.4" y2="363.1" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="314.8" width="2.35" height="36.4" fill="var(--up)"/>
<line x1="925.2" y1="262.3" x2="925.2" y2="319.9" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="274.0" width="2.35" height="40.3" fill="var(--up)"/>
<line x1="928.9" y1="267.0" x2="928.9" y2="327.3" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="283.3" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="932.7" y1="297.2" x2="932.7" y2="339.1" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="308.1" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="936.5" y1="327.3" x2="936.5" y2="384.8" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="335.1" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="940.3" y1="343.5" x2="940.3" y2="389.6" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="360.5" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="944.1" y1="338.5" x2="944.1" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="364.7" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="947.9" y1="358.0" x2="947.9" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="370.9" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="951.7" y1="349.5" x2="951.7" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="367.3" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="955.5" y1="356.0" x2="955.5" y2="376.8" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="369.9" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="959.2" y1="336.8" x2="959.2" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="370.1" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="963.0" y1="349.7" x2="963.0" y2="402.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="374.5" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="966.8" y1="369.9" x2="966.8" y2="417.1" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="375.8" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="970.6" y1="354.7" x2="970.6" y2="389.2" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="374.7" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="974.4" y1="307.2" x2="974.4" y2="379.9" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="315.0" width="2.35" height="63.2" fill="var(--up)"/>
<line x1="978.2" y1="285.4" x2="978.2" y2="335.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="314.8" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="982.0" y1="318.6" x2="982.0" y2="353.5" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="333.2" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="985.7" y1="240.8" x2="985.7" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="241.4" width="2.35" height="96.6" fill="var(--up)"/>
<line x1="989.5" y1="142.6" x2="989.5" y2="246.6" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="172.6" width="2.35" height="69.5" fill="var(--up)"/>
<line x1="993.3" y1="119.2" x2="993.3" y2="206.6" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="133.4" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="997.1" y1="79.2" x2="997.1" y2="139.5" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="105.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="1000.9" y1="133.9" x2="1000.9" y2="236.9" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="145.5" width="2.35" height="79.4" fill="var(--down)"/>
<line x1="1004.7" y1="190.3" x2="1004.7" y2="262.2" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="208.6" width="2.35" height="43.7" fill="var(--down)"/>
<line x1="1008.5" y1="220.4" x2="1008.5" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="232.5" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="1012.2" y1="234.5" x2="1012.2" y2="332.1" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="235.9" width="2.35" height="80.0" fill="var(--down)"/>
<line x1="1016.0" y1="233.8" x2="1016.0" y2="297.0" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="259.2" width="2.35" height="32.7" fill="var(--up)"/>
<line x1="1019.8" y1="253.4" x2="1019.8" y2="335.4" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="259.3" width="2.35" height="69.1" fill="var(--down)"/>
<line x1="1023.6" y1="323.0" x2="1023.6" y2="387.3" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="332.5" width="2.35" height="43.7" fill="var(--down)"/>
<line x1="1027.4" y1="357.2" x2="1027.4" y2="392.7" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="373.5" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="1031.2" y1="373.6" x2="1031.2" y2="409.8" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="385.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1035.0" y1="320.5" x2="1035.0" y2="395.6" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="322.0" width="2.35" height="69.4" fill="var(--up)"/>
<line x1="1038.7" y1="307.8" x2="1038.7" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="317.6" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="1042.5" y1="312.3" x2="1042.5" y2="362.6" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="328.5" width="2.35" height="30.1" fill="var(--down)"/>
<line x1="1046.3" y1="363.4" x2="1046.3" y2="384.0" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="363.4" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="1050.1" y1="379.3" x2="1050.1" y2="390.9" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="379.5" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="60" y1="482.0" x2="1052" y2="482.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="476.0" font-size="11.5" fill="var(--support)" font-weight="600">$38 S1</text>
<text x="1058" y="488.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="604.6" x2="1052" y2="604.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="598.6" font-size="11.5" fill="var(--support)" font-weight="600">$3.49 S2</text>
<text x="1058" y="610.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="387.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="379.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $64 (2026-08-28)</text>
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
| **현재가** | **$64.39** (2026-08-28 종가) | — | **위쪽에 유효한 저항 클러스터가 없다 — 다만 신고가 구간이어서가 아니다** (아래 설명) |
| S1 | $38 | 2 | 2025-08-18·2025-11-17 — 5년 창에서 현재가에 가장 근접한 지지대이고, 현재가보다 -41% 아래다 |
| S2 | $3.49 | 3 | 2022-06-27·2022-12-26·2024-04-15 — 상장 후 장기 침체기의 바닥대. 현재 주가의 5% 수준이라 **실질적으로 지지 기능을 하지 않는다**(아래 4절) |
| 참고선 | $150 | — | 5년(=상장 이후) 최고 **종가** $150.23(2026-05-27 · 주봉으로는 2026-05-25 주, 장중 최고 $151.00). 단발 고점이라 클러스터가 되지 않았다 |

**"상단 저항 없음"을 신고가로 읽으면 안 된다.** 현재가 위쪽으로 2회 이상 시험된 가격대가 없는 것은 맞지만, 주가는 사상 최고 $150.23에서 **-57%** 내려온 상태다. 2026년 5~8월의 $80~$150 구간은 **오르내림이 빨라 같은 가격대를 두 번 밟지 않은 채 지나간 구간**이라 클러스터가 만들어지지 않았을 뿐이다. 즉 위쪽이 비어 있다는 것은 저항이 없다는 뜻이 아니라 **참조할 만한 거래 흔적이 얇다**는 뜻이다.

**아래쪽도 사실상 비어 있다.** S1 $38과 현재가 사이(약 $38~$64)에는 유효 클러스터가 하나도 없다. 이 구간은 2025년 말~2026년 초에 **한 방향으로 빠르게 통과한 구간**이라 그렇다.

---

## 3. 관측된 특이 구간 — 2024년 중반 이후의 구조적 재평가

- **계기는 단일 사건이 아니라 사업 구조의 이동이다.** 2021.08 SPAC 상장 이후 2년 반 동안 주가는 $3~$5대에 눌려 있었고(S2 클러스터), 2024-04-15 주에 5년 최저 $3.47을 찍었다. 그 뒤 연쇄 인수로 Space Systems 매출 비중이 3분의 2를 넘고(FY2025 66.9%) 미 정부·프라임 매출 비중이 FY2023 31% → FY2025 47%로 오르면서 가격대가 단계적으로 재설정됐다 → [역사 / 주요 이벤트](./02_history.md) · [개요](./01_overview.md)
- 주봉 기준으로 보면 재설정은 **두 계단**이다. 2024년 하반기에 $3~$5대에서 벗어나 2025년에 $38~$47 대역(현재의 S1)을 만들었고, 2026년에 다시 그 위로 올라섰다. **저점이 두 자릿수 배율로 이동했기 때문에 그 이전 레벨(S2 $3.49)은 현재 펀더멘털과 무관하다.**
- **이 5년 구간 안에서 회사의 사업 구조 자체가 바뀌었다.** 상장 시점의 Rocket Lab은 소형 발사 단일 사업이었고, 지금은 매출의 80%가 위성 시스템에서 나오며 EV 약 80억 달러의 Iridium 인수를 진행 중이다. 위 표에서 5년 창의 옛 레벨을 지지선으로 그대로 읽지 않는 근거가 이것이다.
- **단기 이벤트(2026-05-08 갭업, 2026-06-29 Iridium 공시)는 여기서 다루지 않는다** — [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3절에 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 일봉(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py RKLB --name "Rocket Lab" --interval 1wk --ref-line 150.23:"5년 최고 종가 (2026-05)" --close-on 2026-08-27 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **마지막 캔들은 1거래일짜리 부분 봉이다.** 수집 시점 원자료에서 마지막 주가 2026-08-24(월~목, 종가 $67.53)와 2026-08-28(금 하루, 종가 $64.39)로 쪼개져 들어왔다. 표의 "현재가" $64.39는 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)의 기준일 종가와 일치하지만, 차트 오른쪽 끝 캔들의 폭은 한 주가 아니다. **레벨 산출에는 영향이 없다**(마지막 봉은 전후 4주 창을 채우지 못해 스윙 포인트가 되지 않는다). `--close-on 2026-08-27`을 걸었으나 그 날짜가 주봉의 봉 시작일이 아니어서 적용되지 않았다.
    - **레벨 개수를 3개로 채우지 않았다.** 저항 0개·지지 2개만 유효했고 사유는 2절에 적었다. `--force-level`은 쓰지 않았다.
    - **이 5년 구간에 주식분할은 없다.** 대신 **지속적인 희석**이 있었다 — 발행주식수가 FY2023 488.9백만 주에서 현재 639.3백만 주로 늘었고, 여기에는 2021년 SPAC 상장, 전환사채의 주식 전환, ATM 유상증자, 인수 대가 주식이 섞여 있다([핵심 지표](./04_metrics.md) A.2·A.4). 주당 가격 차트는 이 변화를 보여주지 않는다.

---

*작성일: 2026-08-30*
