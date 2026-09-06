# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL)와는 계보가 다르다.
    - **대조 결과**: **2026-09-04 종가 $119.02는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[기술적 분석 (일봉)](./09_technical_daily.md)와 모두 일치한다.**

---

## 1. 차트 — 최근 5년 주봉 (2021-09-06 ~ 2026-09-04)

<div class="nrg-chart">
<style>
.nrg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .nrg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .nrg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.nrg-chart svg { width:100%; height:auto; display:block; }
.nrg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.nrg-chart .title { fill: var(--ink); font-weight:600; }
.nrg-chart .grid { stroke: var(--grid); stroke-width:1; }
.nrg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NRG Energy(NRG) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">NRG Energy (NRG) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-04 · 마지막 종가 $119.02 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">25</text>
<line x1="60" y1="542.2" x2="1052" y2="542.2" class="grid"/>
<text x="52" y="546.2" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="458.4" x2="1052" y2="458.4" class="grid"/>
<text x="52" y="462.4" font-size="11" text-anchor="end" fill="var(--muted)">75</text>
<line x1="60" y1="374.5" x2="1052" y2="374.5" class="grid"/>
<text x="52" y="378.5" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="290.7" x2="1052" y2="290.7" class="grid"/>
<text x="52" y="294.7" font-size="11" text-anchor="end" fill="var(--muted)">125</text>
<line x1="60" y1="206.9" x2="1052" y2="206.9" class="grid"/>
<text x="52" y="210.9" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="123.1" x2="1052" y2="123.1" class="grid"/>
<text x="52" y="127.1" font-size="11" text-anchor="end" fill="var(--muted)">175</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="126.3" y1="56.0" x2="126.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="126.3" y1="626.0" x2="126.3" y2="631.0" class="axis"/>
<text x="126.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="323.1" y1="56.0" x2="323.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="323.1" y1="626.0" x2="323.1" y2="631.0" class="axis"/>
<text x="323.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="520.0" y1="56.0" x2="520.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="520.0" y1="626.0" x2="520.0" y2="631.0" class="axis"/>
<text x="520.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="720.7" y1="56.0" x2="720.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="720.7" y1="626.0" x2="720.7" y2="631.0" class="axis"/>
<text x="720.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="917.6" y1="56.0" x2="917.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="917.6" y1="626.0" x2="917.6" y2="631.0" class="axis"/>
<text x="917.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="557.1" x2="61.9" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="557.9" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="65.7" y1="560.5" x2="65.7" y2="569.4" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="562.7" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="69.5" y1="564.8" x2="69.5" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="565.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="73.3" y1="563.6" x2="73.3" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="565.7" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="77.0" y1="569.0" x2="77.0" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="571.0" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="80.8" y1="567.7" x2="80.8" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="571.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="84.6" y1="569.6" x2="84.6" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="571.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="88.4" y1="569.1" x2="88.4" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="570.6" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="92.2" y1="572.7" x2="92.2" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="576.0" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="96.0" y1="588.2" x2="96.0" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="588.3" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="99.8" y1="585.9" x2="99.8" y2="591.5" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="588.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="103.5" y1="583.7" x2="103.5" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="588.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="107.3" y1="585.6" x2="107.3" y2="590.5" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="586.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="111.1" y1="577.3" x2="111.1" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="579.5" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="114.9" y1="573.2" x2="114.9" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="574.1" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="118.7" y1="565.9" x2="118.7" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="568.3" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="122.5" y1="564.6" x2="122.5" y2="569.5" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="565.4" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="126.3" y1="564.4" x2="126.3" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="564.9" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="130.0" y1="570.0" x2="130.0" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="572.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="133.8" y1="573.2" x2="133.8" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="573.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="137.6" y1="574.4" x2="137.6" y2="581.1" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="576.0" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="141.4" y1="575.3" x2="141.4" y2="583.9" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="577.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="145.2" y1="571.7" x2="145.2" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="576.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="149.0" y1="575.8" x2="149.0" y2="582.0" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="576.0" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="152.8" y1="579.7" x2="152.8" y2="586.9" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="582.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="156.5" y1="581.5" x2="156.5" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="583.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="160.3" y1="579.6" x2="160.3" y2="586.4" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="580.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="164.1" y1="576.5" x2="164.1" y2="582.8" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="578.8" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="167.9" y1="582.1" x2="167.9" y2="588.6" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="583.8" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="171.7" y1="579.2" x2="171.7" y2="585.5" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="581.1" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="175.5" y1="576.8" x2="175.5" y2="585.3" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="577.2" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="179.3" y1="576.5" x2="179.3" y2="581.6" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="577.1" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="183.1" y1="570.6" x2="183.1" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="578.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="186.8" y1="582.4" x2="186.8" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="583.1" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="190.6" y1="570.8" x2="190.6" y2="589.4" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="571.0" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="194.4" y1="566.7" x2="194.4" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="568.0" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="198.2" y1="552.7" x2="198.2" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="556.5" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="202.0" y1="549.5" x2="202.0" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="554.1" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="205.8" y1="552.9" x2="205.8" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="554.1" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="209.6" y1="553.6" x2="209.6" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="556.7" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="213.3" y1="564.5" x2="213.3" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="564.5" width="2.35" height="23.5" fill="var(--down)"/>
<line x1="217.1" y1="581.1" x2="217.1" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="581.3" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="220.9" y1="578.4" x2="220.9" y2="585.6" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="579.6" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="224.7" y1="580.7" x2="224.7" y2="587.3" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="581.1" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="228.5" y1="581.5" x2="228.5" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="583.5" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="232.3" y1="586.6" x2="232.3" y2="592.8" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="589.1" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="236.1" y1="582.4" x2="236.1" y2="590.4" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="583.2" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="239.8" y1="576.9" x2="239.8" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="580.9" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="243.6" y1="570.0" x2="243.6" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="570.1" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="247.4" y1="562.6" x2="247.4" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="565.8" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="251.2" y1="565.9" x2="251.2" y2="570.8" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="567.5" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="255.0" y1="567.5" x2="255.0" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="570.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="258.8" y1="564.1" x2="258.8" y2="573.4" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="564.7" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="262.6" y1="559.2" x2="262.6" y2="564.9" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="562.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="266.4" y1="561.8" x2="266.4" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="563.9" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="270.1" y1="572.8" x2="270.1" y2="581.8" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="574.0" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="273.9" y1="569.7" x2="273.9" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="572.0" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="277.7" y1="569.1" x2="277.7" y2="578.9" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="571.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="281.5" y1="565.1" x2="281.5" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="567.8" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="285.3" y1="559.8" x2="285.3" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="560.0" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="289.1" y1="559.6" x2="289.1" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="561.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="292.9" y1="556.6" x2="292.9" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="557.6" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="296.6" y1="556.3" x2="296.6" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="558.2" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="300.4" y1="567.0" x2="300.4" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="568.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="304.2" y1="564.9" x2="304.2" y2="573.0" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="569.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="308.0" y1="572.1" x2="308.0" y2="605.2" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="573.0" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="311.8" y1="597.0" x2="311.8" y2="607.1" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="601.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="315.6" y1="600.5" x2="315.6" y2="604.9" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="602.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="319.4" y1="600.6" x2="319.4" y2="603.9" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="602.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="323.1" y1="600.9" x2="323.1" y2="604.5" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="601.9" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="326.9" y1="599.1" x2="326.9" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="601.3" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="330.7" y1="601.0" x2="330.7" y2="607.0" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="601.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="334.5" y1="596.5" x2="334.5" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="596.7" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="338.3" y1="590.9" x2="338.3" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="594.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="342.1" y1="591.9" x2="342.1" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="592.9" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="345.9" y1="589.6" x2="345.9" y2="597.2" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="593.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="349.6" y1="593.5" x2="349.6" y2="599.2" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="595.8" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="353.4" y1="595.4" x2="353.4" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="596.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="592.9" x2="357.2" y2="604.0" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="596.3" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="361.0" y1="601.9" x2="361.0" y2="608.4" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="604.3" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="364.8" y1="595.8" x2="364.8" y2="607.6" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="600.6" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="368.6" y1="594.7" x2="368.6" y2="604.0" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="594.9" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="372.4" y1="592.8" x2="372.4" y2="599.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="593.1" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="376.2" y1="588.0" x2="376.2" y2="594.0" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="591.8" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="379.9" y1="590.8" x2="379.9" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="590.8" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="383.7" y1="592.4" x2="383.7" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="594.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="387.5" y1="594.3" x2="387.5" y2="607.5" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="595.6" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="391.3" y1="599.0" x2="391.3" y2="607.2" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="599.9" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="395.1" y1="591.9" x2="395.1" y2="600.4" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="592.1" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="398.9" y1="595.1" x2="398.9" y2="599.4" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="596.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="402.7" y1="594.4" x2="402.7" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="595.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="406.4" y1="595.1" x2="406.4" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="595.6" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="410.2" y1="593.3" x2="410.2" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="595.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="414.0" y1="589.4" x2="414.0" y2="599.4" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="593.5" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="417.8" y1="584.0" x2="417.8" y2="592.8" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="584.5" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="421.6" y1="580.4" x2="421.6" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="582.0" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="425.4" y1="580.8" x2="425.4" y2="588.2" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="582.1" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="429.2" y1="579.2" x2="429.2" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="581.7" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="432.9" y1="579.2" x2="432.9" y2="584.9" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="581.7" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="436.7" y1="581.3" x2="436.7" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="584.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="440.5" y1="581.8" x2="440.5" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="583.0" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="444.3" y1="583.5" x2="444.3" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="587.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="583.3" x2="448.1" y2="588.1" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="585.2" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="451.9" y1="580.8" x2="451.9" y2="586.2" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="580.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="455.7" y1="577.1" x2="455.7" y2="584.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="577.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="459.5" y1="577.3" x2="459.5" y2="580.8" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="577.3" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="463.2" y1="575.3" x2="463.2" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="578.6" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="467.0" y1="578.4" x2="467.0" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="580.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="470.8" y1="578.0" x2="470.8" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="579.2" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="474.6" y1="570.1" x2="474.6" y2="579.1" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="572.3" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="478.4" y1="568.9" x2="478.4" y2="574.5" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="571.6" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="482.2" y1="566.9" x2="482.2" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="570.1" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="486.0" y1="554.7" x2="486.0" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="558.9" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="489.7" y1="552.8" x2="489.7" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="556.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="493.5" y1="546.9" x2="493.5" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="548.6" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="497.3" y1="548.8" x2="497.3" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="549.4" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="501.1" y1="547.6" x2="501.1" y2="557.4" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="547.6" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="504.9" y1="546.4" x2="504.9" y2="551.5" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="549.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="508.7" y1="545.0" x2="508.7" y2="550.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="546.3" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="512.5" y1="541.0" x2="512.5" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="542.2" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="516.2" y1="534.9" x2="516.2" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="536.5" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="520.0" y1="535.1" x2="520.0" y2="539.0" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="536.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="534.1" x2="523.8" y2="541.4" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="535.8" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="527.6" y1="533.7" x2="527.6" y2="541.4" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="533.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="531.4" y1="527.9" x2="531.4" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="527.9" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="535.2" y1="524.2" x2="535.2" y2="533.4" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="526.3" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="539.0" y1="527.2" x2="539.0" y2="535.7" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="527.8" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="542.7" y1="533.1" x2="542.7" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="534.1" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="546.5" y1="534.4" x2="546.5" y2="537.4" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="537.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="550.3" y1="519.5" x2="550.3" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="519.7" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="554.1" y1="502.3" x2="554.1" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="506.2" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="557.9" y1="492.5" x2="557.9" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="495.5" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="561.7" y1="482.0" x2="561.7" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="484.6" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="565.5" y1="479.9" x2="565.5" y2="489.0" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="482.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="569.3" y1="464.6" x2="569.3" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="465.8" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="573.0" y1="454.6" x2="573.0" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="461.9" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="576.8" y1="453.2" x2="576.8" y2="478.1" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="459.7" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="580.6" y1="463.8" x2="580.6" y2="474.9" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="465.7" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="584.4" y1="449.4" x2="584.4" y2="470.1" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="452.8" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="588.2" y1="426.6" x2="588.2" y2="465.1" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="429.3" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="592.0" y1="421.5" x2="592.0" y2="436.8" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="427.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="595.8" y1="419.9" x2="595.8" y2="443.5" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="421.5" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="599.5" y1="416.2" x2="599.5" y2="449.4" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="419.9" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="603.3" y1="432.7" x2="603.3" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="439.5" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="607.1" y1="433.5" x2="607.1" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="446.1" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="610.9" y1="435.9" x2="610.9" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="441.5" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="614.7" y1="429.0" x2="614.7" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="442.4" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="618.5" y1="441.6" x2="618.5" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="445.5" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="622.3" y1="438.6" x2="622.3" y2="451.0" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="441.8" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="626.0" y1="442.8" x2="626.0" y2="469.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="442.8" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="629.8" y1="450.1" x2="629.8" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="457.1" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="633.6" y1="446.7" x2="633.6" y2="477.9" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="460.6" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="637.4" y1="440.0" x2="637.4" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="440.6" width="2.35" height="46.4" fill="var(--up)"/>
<line x1="641.2" y1="428.7" x2="641.2" y2="448.4" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="432.3" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="645.0" y1="429.3" x2="645.0" y2="439.4" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="429.9" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="648.8" y1="423.5" x2="648.8" y2="441.8" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="424.8" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="652.5" y1="425.5" x2="652.5" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="425.5" width="2.35" height="27.8" fill="var(--down)"/>
<line x1="656.3" y1="436.9" x2="656.3" y2="454.6" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="438.1" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="660.1" y1="417.6" x2="660.1" y2="440.7" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="417.8" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="663.9" y1="397.4" x2="663.9" y2="419.7" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="404.0" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="667.7" y1="387.3" x2="667.7" y2="409.5" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="390.1" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="671.5" y1="386.6" x2="671.5" y2="422.7" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="389.3" width="2.35" height="19.5" fill="var(--down)"/>
<line x1="675.3" y1="398.6" x2="675.3" y2="423.1" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="407.2" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="679.1" y1="407.6" x2="679.1" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="416.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="682.8" y1="404.7" x2="682.8" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="414.4" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="686.6" y1="365.0" x2="686.6" y2="424.0" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="387.5" width="2.35" height="35.0" fill="var(--up)"/>
<line x1="690.4" y1="376.7" x2="690.4" y2="406.8" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="379.4" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="694.2" y1="382.0" x2="694.2" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="389.7" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="698.0" y1="364.0" x2="698.0" y2="403.0" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="369.1" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="701.8" y1="364.8" x2="701.8" y2="379.0" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="368.2" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="705.6" y1="376.7" x2="705.6" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="377.1" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="709.3" y1="384.9" x2="709.3" y2="415.7" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="390.9" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="713.1" y1="395.6" x2="713.1" y2="411.6" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="401.5" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="716.9" y1="372.3" x2="716.9" y2="409.1" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="379.6" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="720.7" y1="372.8" x2="720.7" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="376.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="724.5" y1="352.2" x2="724.5" y2="390.3" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="359.4" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="728.3" y1="323.0" x2="728.3" y2="350.6" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="333.1" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="732.1" y1="354.3" x2="732.1" y2="391.9" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="357.5" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="735.8" y1="355.2" x2="735.8" y2="377.9" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="364.4" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="739.6" y1="345.1" x2="739.6" y2="370.0" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="349.0" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="743.4" y1="331.9" x2="743.4" y2="356.5" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="344.9" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="747.2" y1="316.7" x2="747.2" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="352.6" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="751.0" y1="351.1" x2="751.0" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="352.4" width="2.35" height="62.1" fill="var(--down)"/>
<line x1="754.8" y1="389.2" x2="754.8" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="390.0" width="2.35" height="34.5" fill="var(--up)"/>
<line x1="758.6" y1="372.0" x2="758.6" y2="397.3" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="372.3" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="762.4" y1="360.4" x2="762.4" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="366.9" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="766.1" y1="362.8" x2="766.1" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="397.3" width="2.35" height="32.2" fill="var(--down)"/>
<line x1="769.9" y1="379.2" x2="769.9" y2="443.0" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="393.1" width="2.35" height="47.1" fill="var(--up)"/>
<line x1="773.7" y1="372.3" x2="773.7" y2="391.3" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="381.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="777.5" y1="343.7" x2="777.5" y2="405.2" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="346.6" width="2.35" height="41.0" fill="var(--up)"/>
<line x1="781.3" y1="314.5" x2="781.3" y2="356.8" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="318.7" width="2.35" height="28.5" fill="var(--up)"/>
<line x1="785.1" y1="304.4" x2="785.1" y2="327.6" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="309.7" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="788.9" y1="175.9" x2="788.9" y2="250.6" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="176.0" width="2.35" height="74.4" fill="var(--up)"/>
<line x1="792.6" y1="167.4" x2="792.6" y2="198.9" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="180.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="796.4" y1="174.1" x2="796.4" y2="196.5" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="175.8" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="800.2" y1="165.5" x2="800.2" y2="192.6" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="185.0" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="804.0" y1="176.4" x2="804.0" y2="214.6" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="184.4" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="807.8" y1="187.2" x2="807.8" y2="206.4" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="195.2" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="811.6" y1="144.6" x2="811.6" y2="207.2" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="164.4" width="2.35" height="35.8" fill="var(--up)"/>
<line x1="815.4" y1="157.6" x2="815.4" y2="194.5" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="160.5" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="819.1" y1="171.2" x2="819.1" y2="209.8" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="178.6" width="2.35" height="26.0" fill="var(--down)"/>
<line x1="822.9" y1="191.7" x2="822.9" y2="229.0" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="201.0" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="826.7" y1="154.3" x2="826.7" y2="215.1" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="184.8" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="830.5" y1="142.4" x2="830.5" y2="183.8" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="147.8" width="2.35" height="32.3" fill="var(--up)"/>
<line x1="834.3" y1="119.8" x2="834.3" y2="223.6" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="141.5" width="2.35" height="56.8" fill="var(--down)"/>
<line x1="838.1" y1="176.8" x2="838.1" y2="212.6" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="200.2" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="841.9" y1="203.9" x2="841.9" y2="228.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="210.6" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="845.6" y1="202.8" x2="845.6" y2="227.6" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="221.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="849.4" y1="206.0" x2="849.4" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="214.7" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="853.2" y1="153.8" x2="853.2" y2="224.4" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="157.1" width="2.35" height="54.0" fill="var(--up)"/>
<line x1="857.0" y1="143.1" x2="857.0" y2="167.1" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="156.2" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="860.8" y1="133.0" x2="860.8" y2="180.4" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="144.6" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="864.6" y1="132.4" x2="864.6" y2="171.4" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="142.1" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="868.4" y1="139.9" x2="868.4" y2="172.1" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="143.3" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="872.2" y1="126.4" x2="872.2" y2="163.0" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="144.0" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="875.9" y1="130.1" x2="875.9" y2="179.0" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="133.8" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="879.7" y1="104.5" x2="879.7" y2="153.8" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="132.2" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="883.5" y1="116.1" x2="883.5" y2="166.6" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="127.8" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="887.3" y1="117.3" x2="887.3" y2="173.2" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="120.9" width="2.35" height="35.1" fill="var(--down)"/>
<line x1="891.1" y1="124.0" x2="891.1" y2="188.8" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="156.0" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="894.9" y1="133.9" x2="894.9" y2="176.9" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="141.5" width="2.35" height="30.7" fill="var(--up)"/>
<line x1="898.7" y1="139.0" x2="898.7" y2="172.6" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="148.0" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="902.4" y1="131.8" x2="902.4" y2="171.4" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="159.3" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="906.2" y1="163.1" x2="906.2" y2="213.7" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="167.0" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="910.0" y1="168.3" x2="910.0" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="170.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="913.8" y1="151.0" x2="913.8" y2="176.1" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="152.7" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="917.6" y1="139.0" x2="917.6" y2="233.8" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="144.9" width="2.35" height="64.4" fill="var(--down)"/>
<line x1="921.4" y1="175.9" x2="921.4" y2="220.3" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="200.0" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="925.2" y1="194.9" x2="925.2" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="209.2" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="928.9" y1="181.7" x2="928.9" y2="210.3" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="198.1" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="932.7" y1="191.6" x2="932.7" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="195.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="936.5" y1="130.8" x2="936.5" y2="197.5" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="131.9" width="2.35" height="61.0" fill="var(--up)"/>
<line x1="940.3" y1="105.9" x2="940.3" y2="141.0" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="109.0" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="944.1" y1="72.9" x2="944.1" y2="160.7" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="109.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="947.9" y1="101.0" x2="947.9" y2="192.7" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="120.7" width="2.35" height="71.7" fill="var(--down)"/>
<line x1="951.7" y1="175.5" x2="951.7" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="197.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="955.5" y1="163.4" x2="955.5" y2="225.0" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="186.8" width="2.35" height="34.2" fill="var(--down)"/>
<line x1="959.2" y1="189.9" x2="959.2" y2="225.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="213.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="963.0" y1="197.5" x2="963.0" y2="240.8" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="197.9" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="966.8" y1="149.7" x2="966.8" y2="209.6" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="159.7" width="2.35" height="39.0" fill="var(--up)"/>
<line x1="970.6" y1="121.3" x2="970.6" y2="170.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="147.4" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="974.4" y1="140.6" x2="974.4" y2="210.9" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="142.7" width="2.35" height="31.3" fill="var(--down)"/>
<line x1="978.2" y1="168.8" x2="978.2" y2="211.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="170.4" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="982.0" y1="175.9" x2="982.0" y2="247.9" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="196.8" width="2.35" height="49.9" fill="var(--down)"/>
<line x1="985.7" y1="243.4" x2="985.7" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="247.0" width="2.35" height="34.3" fill="var(--down)"/>
<line x1="989.5" y1="240.9" x2="989.5" y2="303.4" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="248.3" width="2.35" height="34.5" fill="var(--up)"/>
<line x1="993.3" y1="230.1" x2="993.3" y2="260.8" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="240.4" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="997.1" y1="250.7" x2="997.1" y2="283.6" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="270.3" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="1000.9" y1="269.2" x2="1000.9" y2="307.1" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="276.2" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="1004.7" y1="238.5" x2="1004.7" y2="285.9" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="257.0" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="1008.5" y1="205.1" x2="1008.5" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="209.0" width="2.35" height="47.0" fill="var(--up)"/>
<line x1="1012.2" y1="203.6" x2="1012.2" y2="256.6" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="208.4" width="2.35" height="43.1" fill="var(--down)"/>
<line x1="1016.0" y1="228.8" x2="1016.0" y2="256.4" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="239.0" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="1019.8" y1="224.6" x2="1019.8" y2="278.9" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="243.4" width="2.35" height="33.5" fill="var(--down)"/>
<line x1="1023.6" y1="226.4" x2="1023.6" y2="276.7" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="237.0" width="2.35" height="36.2" fill="var(--up)"/>
<line x1="1027.4" y1="233.6" x2="1027.4" y2="299.3" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="233.7" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="1031.2" y1="238.0" x2="1031.2" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="258.2" width="2.35" height="55.6" fill="var(--down)"/>
<line x1="1035.0" y1="286.4" x2="1035.0" y2="319.0" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="286.5" width="2.35" height="27.2" fill="var(--up)"/>
<line x1="1038.7" y1="282.2" x2="1038.7" y2="330.7" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="282.7" width="2.35" height="47.9" fill="var(--down)"/>
<line x1="1042.5" y1="316.2" x2="1042.5" y2="338.8" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="329.9" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="1046.3" y1="310.0" x2="1046.3" y2="346.6" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="310.8" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="1050.1" y1="310.0" x2="1050.1" y2="336.3" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="310.8" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="60" y1="120.6" x2="1052" y2="120.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="124.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$176 R1</text>
<text x="1058" y="136.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="590.8" x2="1052" y2="590.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="584.8" font-size="11.5" fill="var(--support)" font-weight="600">$36 S1</text>
<text x="1058" y="596.8" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="607.5" x2="1052" y2="607.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="601.5" font-size="11.5" fill="var(--support)" font-weight="600">$31 S2</text>
<text x="1058" y="613.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="310.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="302.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $119 (2026-09-04)</text>
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

!!! warning "유효 클러스터가 3개뿐이고, 그중 둘은 현재가의 4분의 1 수준이다"
    5년 창 안에서 터치 2회 이상 조건을 만족한 클러스터는 R1·S1·S2 셋뿐이다. **레벨을 3개씩 채우려고 `--force-level`로 추가하지 않았다.** 게다가 S1($36)·S2($31)는 2021~2023년의 가격대라 현재가($119.02)와 연속성이 없다 — 아래 3절 참고.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $176 | 2 | 2025-08-04·2026-04-13 — **5년 최고($189.96) 바로 아래 구간.** 8개월 간격으로 두 번 닿았고 뚫지 못했다 |
| **현재가** | **$119.02** (2026-09-04 종가) | — | R1과 S1 사이. 다만 S1은 현재가의 3분의 1이라 실질 지지가 아니다 |
| S1 | $36 | 6 | 2021-11-08·2022-02-28·2022-04-25·2022-06-13·2022-07-18·2023-08-14 — **터치 6회로 5년 창에서 가장 두꺼운 클러스터**이지만 현재가의 30% 수준이다 |
| S2 | $31 | 4 | 2022-12-12·2023-01-16·2023-03-13·2023-05-01 — 위와 같은 이유로 지지선으로 쓸 수 없다 |
| 참고선 | $30.25 | — | **5년 최저**(2023년 상반기). Vivint 인수 발표 직후 주가가 급락했던 국면의 가격이다 |

---

## 3. 관측된 특이 구간 — 2023~2025년의 재평가로 가격대가 통째로 이동했다

**이 차트에서 S1($36)·S2($31)를 지지선으로 읽으면 안 된다.** 5년 창의 앞쪽 2년(2021~2023)과 뒤쪽 2년(2024~2026)은 **가격대가 네 배 이상 다르다.**

- 2021년 9월~2023년 상반기 이 종목은 **$30~$45 구간**에서 움직였다. 2023년 3월 Vivint Smart Home 인수(약 $2.8B)를 발표했을 때 시장은 "에너지 회사가 왜 홈보안을 사느냐"는 반응으로 주가를 눌렀고, 5년 최저 $30.25가 그 국면에서 나왔다([역사 / 주요 이벤트](./02_history.md)).
- 2023년 하반기부터 세 가지가 겹치며 가격대가 재설정됐다 — ① Vivint가 실제로 이익을 내기 시작했고(FY2025 Adjusted EBITDA $1,092M), ② AI 데이터센터 전력 수요가 산업 서사가 됐고, ③ 2025년 5월 LS Power 인수 발표가 나왔다. 주가는 2023년 말 $51.70 → 2025년 말 $159.24로 **2년 만에 3.1배**가 됐다.
- 그 결과 **2024년 이후의 클러스터(R1 $176)만 현재 가격 구조와 연속성을 갖는다.** S1·S2는 다른 사업 구성에 매겨진 가격이라고 보는 편이 정확하며, 표에는 스크립트 산출물 그대로 남겨두되 해석에서 제외한다.
- **주봉 구조가 말하는 현재 위치**: 현재가와 R1($176) 사이가 48% 벌어져 있고 그 사이에 클러스터가 없다. 아래로도 유효한 지지가 없다. **즉 이 종목은 지금 5년 구조상 "빈 구간"에 있으며, 기술적 레벨로 잡을 수 있는 것이 사실상 없다** — 방향은 [투자 판단](./07_investment.md)의 관찰 항목(레버리지 방향·데이터센터 계약 잔고)으로 판단해야 한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-06~2026-09-04. 수집 시점: 2026-09-07. **원주가(과거 분할은 소급 반영, 배당은 미반영)**
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py NRG --name "NRG Energy" --interval 1wk --close-on 2026-09-04 --emit all` (재현용, 옵션 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 가격대 재설정이 이 표의 대부분을 무력화한다.** S1($36)·S2($31)는 알고리즘상 유효한 클러스터이지만 현재가의 4분의 1 수준이라 지지선으로 쓸 수 없다 — **±2.5% 상대 허용오차를 쓰는 클러스터링은 가격대가 네 배 바뀐 구간을 자동으로 걸러내지 못한다.** 결과적으로 이 문서에서 실제로 쓸 수 있는 레벨은 R1($176) 하나뿐이다.
    - **레벨 개수를 3개로 채우지 않았다** — 터치 2회 이상 조건을 만족하는 클러스터가 셋뿐이었고, `--force-level`로 억지로 추가하지 않았다.
    - **기간 내 배당이 20회 있었으나 원주가라 반영되지 않았다.**
    - 해당 기간에 주식분할은 없었다. 다만 **2021~2025년에는 자사주매입으로 주식수가 매년 6~7%씩 줄었고, 2026년에는 LS Power 신주 발행으로 늘었다** — 주당 가격의 궤적에 이 두 방향의 효과가 섞여 있다.

---

*작성일: 2026-09-07*
