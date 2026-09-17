# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 2026-09-11 종가 **$175.26**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-11)

<style>
.coin-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .coin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.coin-chart svg { width:100%; height:auto; display:block; }
.coin-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.coin-chart .title { fill: var(--ink); font-weight:600; }
.coin-chart .grid { stroke: var(--grid); stroke-width:1; }
.coin-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="coin-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Coinbase(COIN) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Coinbase (COIN) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $175.26 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="517.1" x2="1052" y2="517.1" class="grid"/>
<text x="52" y="521.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="389.0" x2="1052" y2="389.0" class="grid"/>
<text x="52" y="393.0" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="260.9" x2="1052" y2="260.9" class="grid"/>
<text x="52" y="264.9" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="132.9" x2="1052" y2="132.9" class="grid"/>
<text x="52" y="136.9" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.5" y1="56.0" x2="122.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.5" y1="626.0" x2="122.5" y2="631.0" class="axis"/>
<text x="122.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="319.4" y1="56.0" x2="319.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="319.4" y1="626.0" x2="319.4" y2="631.0" class="axis"/>
<text x="319.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="516.2" y1="56.0" x2="516.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="516.2" y1="626.0" x2="516.2" y2="631.0" class="axis"/>
<text x="516.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.9" y1="56.0" x2="716.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.9" y1="626.0" x2="716.9" y2="631.0" class="axis"/>
<text x="716.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.8" y1="56.0" x2="913.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.8" y1="626.0" x2="913.8" y2="631.0" class="axis"/>
<text x="913.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="75.7" x2="1052" y2="75.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="78.7" font-size="10.5" fill="var(--muted)">$445 역대 최고(2021-11)</text>
<line x1="61.9" y1="322.6" x2="61.9" y2="339.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="329.5" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="65.7" y1="330.4" x2="65.7" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="344.9" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="69.5" y1="343.2" x2="69.5" y2="357.0" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="348.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="73.3" y1="317.1" x2="73.3" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="327.4" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="77.0" y1="284.4" x2="77.0" y2="332.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="285.8" width="2.35" height="39.8" fill="var(--up)"/>
<line x1="80.8" y1="238.7" x2="80.8" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="259.9" width="2.35" height="32.2" fill="var(--up)"/>
<line x1="84.6" y1="224.5" x2="84.6" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="236.1" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="88.4" y1="202.2" x2="88.4" y2="230.3" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="213.5" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="92.2" y1="172.7" x2="92.2" y2="235.3" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="197.5" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="96.0" y1="190.2" x2="96.0" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="203.2" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="99.8" y1="215.0" x2="99.8" y2="262.0" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="218.3" width="2.35" height="38.6" fill="var(--down)"/>
<line x1="103.5" y1="220.3" x2="103.5" y2="314.5" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="245.3" width="2.35" height="59.7" fill="var(--down)"/>
<line x1="107.3" y1="273.5" x2="107.3" y2="332.1" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="317.6" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="111.1" y1="301.6" x2="111.1" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="322.2" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="114.9" y1="300.3" x2="114.9" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="301.7" width="2.35" height="40.5" fill="var(--up)"/>
<line x1="118.7" y1="284.0" x2="118.7" y2="323.2" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="299.0" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="122.5" y1="310.1" x2="122.5" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="317.0" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="126.3" y1="329.8" x2="126.3" y2="370.3" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="350.6" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="130.0" y1="348.0" x2="130.0" y2="405.9" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="354.7" width="2.35" height="44.6" fill="var(--down)"/>
<line x1="133.8" y1="391.5" x2="133.8" y2="437.5" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="417.8" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="137.6" y1="387.2" x2="137.6" y2="421.0" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="396.2" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="141.4" y1="366.6" x2="141.4" y2="400.5" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="390.7" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="145.2" y1="371.1" x2="145.2" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="397.4" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="149.0" y1="407.3" x2="149.0" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="413.5" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="152.8" y1="381.5" x2="152.8" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="424.3" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="156.5" y1="412.8" x2="156.5" y2="444.7" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="429.7" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="160.3" y1="406.1" x2="160.3" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="407.0" width="2.35" height="33.2" fill="var(--up)"/>
<line x1="164.1" y1="394.5" x2="164.1" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="406.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="167.9" y1="380.3" x2="167.9" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="397.6" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="171.7" y1="397.9" x2="171.7" y2="440.1" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="405.2" width="2.35" height="33.8" fill="var(--down)"/>
<line x1="175.5" y1="437.1" x2="175.5" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="444.7" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="179.3" y1="446.7" x2="179.3" y2="477.1" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="458.9" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="183.1" y1="469.3" x2="183.1" y2="501.6" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="478.7" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="186.8" y1="475.1" x2="186.8" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="500.4" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="190.6" y1="521.7" x2="190.6" y2="592.9" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="522.2" width="2.35" height="36.0" fill="var(--down)"/>
<line x1="194.4" y1="553.2" x2="194.4" y2="567.7" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="558.0" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="198.2" y1="546.4" x2="198.2" y2="569.5" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="548.7" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="202.0" y1="538.5" x2="202.0" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="542.7" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="205.8" y1="550.3" x2="205.8" y2="571.2" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="554.6" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="209.6" y1="572.6" x2="209.6" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="579.6" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="213.3" y1="563.1" x2="213.3" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="564.9" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="217.1" y1="567.8" x2="217.1" y2="588.7" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="568.9" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="220.9" y1="563.6" x2="220.9" y2="586.4" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="568.0" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="224.7" y1="570.4" x2="224.7" y2="580.7" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="571.5" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="228.5" y1="544.0" x2="228.5" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="554.5" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="232.3" y1="555.6" x2="232.3" y2="577.8" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="556.9" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="236.1" y1="496.2" x2="236.1" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="526.0" width="2.35" height="40.8" fill="var(--up)"/>
<line x1="239.8" y1="512.6" x2="239.8" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="519.9" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="243.6" y1="522.9" x2="243.6" y2="550.4" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="531.1" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="247.4" y1="547.3" x2="247.4" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="554.4" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="251.2" y1="555.1" x2="251.2" y2="565.9" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="561.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="255.0" y1="541.4" x2="255.0" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="541.6" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="258.8" y1="536.9" x2="258.8" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="539.4" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="262.6" y1="552.3" x2="262.6" y2="569.1" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="553.1" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="266.4" y1="558.4" x2="266.4" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="562.6" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="270.1" y1="547.5" x2="270.1" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="559.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="273.9" y1="550.7" x2="273.9" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="558.7" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="277.7" y1="550.6" x2="277.7" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="560.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="281.5" y1="544.9" x2="281.5" y2="563.6" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="552.9" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="285.3" y1="549.6" x2="285.3" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="552.5" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="289.1" y1="567.1" x2="289.1" y2="588.1" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="568.4" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="292.9" y1="570.9" x2="292.9" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="573.9" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="296.6" y1="586.1" x2="296.6" y2="593.2" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="588.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="300.4" y1="584.1" x2="300.4" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="584.2" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="304.2" y1="581.4" x2="304.2" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="583.8" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="308.0" y1="585.9" x2="308.0" y2="600.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="594.0" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="311.8" y1="598.0" x2="311.8" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="599.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="315.6" y1="599.3" x2="315.6" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="599.9" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="319.4" y1="595.9" x2="319.4" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="598.5" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="323.1" y1="580.4" x2="323.1" y2="600.7" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="581.2" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="326.9" y1="571.8" x2="326.9" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="574.6" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="330.7" y1="565.4" x2="330.7" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="566.6" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="334.5" y1="533.0" x2="334.5" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="549.6" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="338.3" y1="547.9" x2="338.3" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="551.5" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="342.1" y1="551.3" x2="342.1" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="561.7" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="345.9" y1="558.8" x2="345.9" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="564.1" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="349.6" y1="558.8" x2="349.6" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="562.6" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="353.4" y1="555.8" x2="353.4" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="562.5" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="357.2" y1="546.8" x2="357.2" y2="580.2" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="549.2" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="361.0" y1="535.9" x2="361.0" y2="566.4" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="546.9" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="364.8" y1="557.3" x2="364.8" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="558.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="557.7" x2="368.6" y2="570.7" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="560.7" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="372.4" y1="552.2" x2="372.4" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="555.7" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="376.2" y1="553.3" x2="376.2" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="559.2" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="379.9" y1="569.0" x2="379.9" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="569.7" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="383.7" y1="570.2" x2="383.7" y2="584.2" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="570.6" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="387.5" y1="563.6" x2="387.5" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="571.8" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="391.3" y1="566.2" x2="391.3" y2="572.7" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="570.4" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="395.1" y1="564.2" x2="395.1" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="572.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="560.2" x2="398.9" y2="569.4" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="562.5" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="402.7" y1="562.7" x2="402.7" y2="585.7" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="564.0" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="406.4" y1="573.1" x2="406.4" y2="581.0" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="574.0" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="410.2" y1="565.9" x2="410.2" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="566.5" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="414.0" y1="549.2" x2="414.0" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="553.6" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="417.8" y1="541.2" x2="417.8" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="544.4" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="421.6" y1="498.6" x2="421.6" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="510.3" width="2.35" height="33.6" fill="var(--up)"/>
<line x1="425.4" y1="501.9" x2="425.4" y2="518.8" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="511.3" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="429.2" y1="513.6" x2="429.2" y2="527.6" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="518.1" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="432.9" y1="516.9" x2="432.9" y2="534.2" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="523.8" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="436.7" y1="531.2" x2="436.7" y2="542.1" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="533.5" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="440.5" y1="538.8" x2="440.5" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="542.7" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="444.3" y1="545.1" x2="444.3" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="550.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="448.1" y1="534.4" x2="448.1" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="545.3" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="451.9" y1="539.3" x2="451.9" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="540.1" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="455.7" y1="534.6" x2="455.7" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="540.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="459.5" y1="537.2" x2="459.5" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="537.9" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="463.2" y1="545.9" x2="463.2" y2="556.0" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="549.0" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="467.0" y1="542.8" x2="467.0" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="544.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="470.8" y1="540.1" x2="470.8" y2="552.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="547.2" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="474.6" y1="543.6" x2="474.6" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="545.8" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="478.4" y1="530.7" x2="478.4" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="548.5" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="482.2" y1="532.1" x2="482.2" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="535.3" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="486.0" y1="517.4" x2="486.0" y2="537.5" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="526.2" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="489.7" y1="516.9" x2="489.7" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="518.3" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="493.5" y1="495.4" x2="493.5" y2="517.1" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="497.2" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="497.3" y1="473.2" x2="497.3" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="473.9" width="2.35" height="27.1" fill="var(--up)"/>
<line x1="501.1" y1="455.8" x2="501.1" y2="478.5" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="457.4" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="504.9" y1="447.0" x2="504.9" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="455.8" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="508.7" y1="416.3" x2="508.7" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="420.4" width="2.35" height="39.3" fill="var(--up)"/>
<line x1="512.5" y1="405.2" x2="512.5" y2="428.7" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="421.3" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="516.2" y1="420.3" x2="516.2" y2="460.6" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="423.6" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="520.0" y1="438.5" x2="520.0" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="443.1" width="2.35" height="34.6" fill="var(--down)"/>
<line x1="523.8" y1="469.3" x2="523.8" y2="494.0" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="479.4" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="527.6" y1="476.4" x2="527.6" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="484.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="531.4" y1="469.9" x2="531.4" y2="486.1" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="479.7" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="535.2" y1="460.1" x2="535.2" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="463.3" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="539.0" y1="397.2" x2="539.0" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="414.3" width="2.35" height="50.2" fill="var(--up)"/>
<line x1="542.7" y1="413.0" x2="542.7" y2="439.4" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="414.8" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="546.5" y1="373.4" x2="546.5" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="381.6" width="2.35" height="47.5" fill="var(--up)"/>
<line x1="550.3" y1="298.7" x2="550.3" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="316.5" width="2.35" height="50.2" fill="var(--up)"/>
<line x1="554.1" y1="297.3" x2="554.1" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="299.3" width="2.35" height="35.5" fill="var(--down)"/>
<line x1="557.9" y1="291.2" x2="557.9" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="317.9" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="561.7" y1="282.1" x2="561.7" y2="319.9" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="305.6" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="565.5" y1="300.9" x2="565.5" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="309.8" width="2.35" height="26.9" fill="var(--down)"/>
<line x1="569.3" y1="306.7" x2="569.3" y2="345.3" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="321.3" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="573.0" y1="325.3" x2="573.0" y2="381.8" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="327.6" width="2.35" height="47.3" fill="var(--down)"/>
<line x1="576.8" y1="339.1" x2="576.8" y2="371.6" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="342.5" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="580.6" y1="347.1" x2="580.6" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="350.7" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="584.4" y1="343.2" x2="584.4" y2="388.4" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="355.9" width="2.35" height="31.9" fill="var(--down)"/>
<line x1="588.2" y1="361.6" x2="588.2" y2="395.5" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="379.3" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="592.0" y1="339.4" x2="592.0" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="340.8" width="2.35" height="38.0" fill="var(--up)"/>
<line x1="595.8" y1="326.4" x2="595.8" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="343.6" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="599.5" y1="307.3" x2="599.5" y2="357.4" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="332.5" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="603.3" y1="308.0" x2="603.3" y2="345.4" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="332.0" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="607.1" y1="326.7" x2="607.1" y2="362.5" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="338.0" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="610.9" y1="356.0" x2="610.9" y2="379.2" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="360.6" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="614.7" y1="342.9" x2="614.7" y2="376.9" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="355.7" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="618.5" y1="354.3" x2="618.5" y2="371.7" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="355.1" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="622.3" y1="312.4" x2="622.3" y2="353.2" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="315.0" width="2.35" height="36.4" fill="var(--up)"/>
<line x1="626.0" y1="296.1" x2="626.0" y2="355.3" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="311.6" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="629.8" y1="318.0" x2="629.8" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="323.0" width="2.35" height="60.3" fill="var(--down)"/>
<line x1="633.6" y1="389.1" x2="633.6" y2="438.8" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="393.8" width="2.35" height="43.9" fill="var(--up)"/>
<line x1="637.4" y1="381.4" x2="637.4" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="382.2" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="641.2" y1="373.8" x2="641.2" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="374.4" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="645.0" y1="375.1" x2="645.0" y2="414.6" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="377.1" width="2.35" height="33.2" fill="var(--down)"/>
<line x1="648.8" y1="411.2" x2="648.8" y2="458.0" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="412.1" width="2.35" height="44.4" fill="var(--down)"/>
<line x1="652.5" y1="428.8" x2="652.5" y2="453.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="436.4" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="656.3" y1="420.6" x2="656.3" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="427.3" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="660.1" y1="398.7" x2="660.1" y2="435.4" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="400.3" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="663.9" y1="407.7" x2="663.9" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="409.3" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="667.7" y1="415.7" x2="667.7" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="419.3" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="671.5" y1="363.1" x2="671.5" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="363.1" width="2.35" height="50.0" fill="var(--up)"/>
<line x1="675.3" y1="367.4" x2="675.3" y2="396.0" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="369.3" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="679.1" y1="358.4" x2="679.1" y2="416.2" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="371.9" width="2.35" height="39.0" fill="var(--down)"/>
<line x1="682.8" y1="294.9" x2="682.8" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="298.4" width="2.35" height="116.1" fill="var(--up)"/>
<line x1="686.6" y1="216.3" x2="686.6" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="253.5" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="690.4" y1="207.5" x2="690.4" y2="275.7" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="255.0" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="694.2" y1="238.6" x2="694.2" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="249.4" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="698.0" y1="197.2" x2="698.0" y2="265.2" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="205.1" width="2.35" height="53.3" fill="var(--up)"/>
<line x1="701.8" y1="209.5" x2="701.8" y2="262.8" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="209.8" width="2.35" height="37.6" fill="var(--down)"/>
<line x1="705.6" y1="227.3" x2="705.6" y2="309.8" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="239.3" width="2.35" height="48.9" fill="var(--down)"/>
<line x1="709.3" y1="281.4" x2="709.3" y2="308.2" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="293.6" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="713.1" y1="297.3" x2="713.1" y2="329.6" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="298.5" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="716.9" y1="269.1" x2="716.9" y2="327.5" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="287.8" width="2.35" height="26.0" fill="var(--down)"/>
<line x1="720.7" y1="260.5" x2="720.7" y2="336.8" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="266.7" width="2.35" height="62.1" fill="var(--up)"/>
<line x1="724.5" y1="247.4" x2="724.5" y2="294.7" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="262.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="728.3" y1="253.3" x2="728.3" y2="305.5" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="272.0" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="732.1" y1="274.5" x2="732.1" y2="300.7" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="293.6" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="735.8" y1="257.9" x2="735.8" y2="307.7" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="286.0" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="739.6" y1="287.6" x2="739.6" y2="344.5" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="288.1" width="2.35" height="55.6" fill="var(--down)"/>
<line x1="743.4" y1="337.5" x2="743.4" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="338.9" width="2.35" height="30.1" fill="var(--down)"/>
<line x1="747.2" y1="346.3" x2="747.2" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="347.8" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="751.0" y1="380.3" x2="751.0" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="382.5" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="754.8" y1="396.8" x2="754.8" y2="416.2" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="402.0" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="758.6" y1="380.2" x2="758.6" y2="423.6" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="392.2" width="2.35" height="30.2" fill="var(--down)"/>
<line x1="762.4" y1="409.4" x2="762.4" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="428.3" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="766.1" y1="409.7" x2="766.1" y2="462.6" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="420.4" width="2.35" height="37.7" fill="var(--up)"/>
<line x1="769.9" y1="411.6" x2="769.9" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="414.0" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="773.7" y1="374.1" x2="773.7" y2="425.7" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="376.7" width="2.35" height="44.2" fill="var(--up)"/>
<line x1="777.5" y1="377.5" x2="777.5" y2="394.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="378.5" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="781.3" y1="370.9" x2="781.3" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="386.8" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="785.1" y1="298.8" x2="785.1" y2="381.8" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="303.9" width="2.35" height="73.7" fill="var(--up)"/>
<line x1="788.9" y1="290.4" x2="788.9" y2="315.7" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="308.1" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="792.6" y1="299.2" x2="792.6" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="300.6" width="2.35" height="28.7" fill="var(--down)"/>
<line x1="796.4" y1="304.9" x2="796.4" y2="337.7" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="323.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="800.2" y1="309.1" x2="800.2" y2="343.8" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="317.7" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="804.0" y1="247.2" x2="804.0" y2="331.0" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="250.2" width="2.35" height="77.6" fill="var(--up)"/>
<line x1="807.8" y1="155.9" x2="807.8" y2="267.9" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="192.5" width="2.35" height="65.8" fill="var(--up)"/>
<line x1="811.6" y1="183.5" x2="811.6" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="185.1" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="815.4" y1="138.6" x2="815.4" y2="199.5" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="149.4" width="2.35" height="42.1" fill="var(--up)"/>
<line x1="819.1" y1="75.7" x2="819.1" y2="167.4" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="107.5" width="2.35" height="34.9" fill="var(--up)"/>
<line x1="822.9" y1="86.3" x2="822.9" y2="150.3" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="100.1" width="2.35" height="43.4" fill="var(--down)"/>
<line x1="826.7" y1="138.8" x2="826.7" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="139.7" width="2.35" height="102.4" fill="var(--down)"/>
<line x1="830.5" y1="230.2" x2="830.5" y2="269.5" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="235.9" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="834.3" y1="202.8" x2="834.3" y2="242.8" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="232.6" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="838.1" y1="229.8" x2="838.1" y2="271.9" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="235.5" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="841.9" y1="240.5" x2="841.9" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="245.3" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="845.6" y1="240.8" x2="845.6" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="261.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="849.4" y1="223.2" x2="849.4" y2="264.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="231.4" width="2.35" height="27.1" fill="var(--up)"/>
<line x1="853.2" y1="194.5" x2="853.2" y2="246.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="206.6" width="2.35" height="25.1" fill="var(--up)"/>
<line x1="857.0" y1="214.6" x2="857.0" y2="256.6" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="218.1" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="860.8" y1="154.0" x2="860.8" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="158.4" width="2.35" height="79.4" fill="var(--up)"/>
<line x1="864.6" y1="130.1" x2="864.6" y2="194.8" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="145.2" width="2.35" height="42.7" fill="var(--down)"/>
<line x1="868.4" y1="177.8" x2="868.4" y2="238.2" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="180.0" width="2.35" height="34.8" fill="var(--down)"/>
<line x1="872.2" y1="188.1" x2="872.2" y2="247.5" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="191.2" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="875.9" y1="167.1" x2="875.9" y2="224.8" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="180.5" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="879.7" y1="206.1" x2="879.7" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="208.6" width="2.35" height="40.6" fill="var(--down)"/>
<line x1="883.5" y1="229.2" x2="883.5" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="231.5" width="2.35" height="50.0" fill="var(--down)"/>
<line x1="887.3" y1="289.3" x2="887.3" y2="349.1" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="293.1" width="2.35" height="44.2" fill="var(--down)"/>
<line x1="891.1" y1="286.7" x2="891.1" y2="336.8" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="295.8" width="2.35" height="36.0" fill="var(--up)"/>
<line x1="894.9" y1="281.1" x2="894.9" y2="322.2" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="299.7" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="898.7" y1="280.5" x2="898.7" y2="313.8" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="295.8" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="902.4" y1="301.2" x2="902.4" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="301.9" width="2.35" height="29.3" fill="var(--down)"/>
<line x1="906.2" y1="318.8" x2="906.2" y2="347.0" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="322.8" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="910.0" y1="337.9" x2="910.0" y2="356.4" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="342.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="913.8" y1="313.6" x2="913.8" y2="341.4" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="328.7" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="917.6" y1="308.2" x2="917.6" y2="342.7" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="336.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="921.4" y1="344.3" x2="921.4" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="347.2" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="925.2" y1="369.0" x2="925.2" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="373.4" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="928.9" y1="400.6" x2="928.9" y2="459.3" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="402.1" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="932.7" y1="430.1" x2="932.7" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="434.7" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="936.5" y1="420.4" x2="936.5" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="425.7" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="940.3" y1="406.5" x2="940.3" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="420.0" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="944.1" y1="371.7" x2="944.1" y2="424.8" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="392.6" width="2.35" height="31.7" fill="var(--up)"/>
<line x1="947.9" y1="379.9" x2="947.9" y2="398.7" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="391.6" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="951.7" y1="371.8" x2="951.7" y2="399.4" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="386.7" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="955.5" y1="384.0" x2="955.5" y2="440.5" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="390.8" width="2.35" height="48.0" fill="var(--down)"/>
<line x1="959.2" y1="415.5" x2="959.2" y2="442.2" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="425.6" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="963.0" y1="402.4" x2="963.0" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="420.9" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="966.8" y1="368.5" x2="966.8" y2="434.7" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="380.9" width="2.35" height="53.2" fill="var(--up)"/>
<line x1="970.6" y1="373.3" x2="970.6" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="387.7" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="974.4" y1="383.3" x2="974.4" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="390.2" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="978.2" y1="377.7" x2="978.2" y2="411.1" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="387.5" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="982.0" y1="360.4" x2="982.0" y2="398.9" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="388.5" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="985.7" y1="393.4" x2="985.7" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="401.5" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="989.5" y1="399.5" x2="989.5" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="403.1" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="993.3" y1="406.2" x2="993.3" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="415.7" width="2.35" height="34.3" fill="var(--down)"/>
<line x1="997.1" y1="433.2" x2="997.1" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="440.6" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="1000.9" y1="421.8" x2="1000.9" y2="439.6" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="427.5" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="1004.7" y1="419.2" x2="1004.7" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="433.9" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="1008.5" y1="423.5" x2="1008.5" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="433.3" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="1012.2" y1="425.3" x2="1012.2" y2="447.0" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="438.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="1016.0" y1="429.4" x2="1016.0" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="444.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="1019.8" y1="412.7" x2="1019.8" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="442.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1023.6" y1="427.9" x2="1023.6" y2="467.0" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="436.0" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="1027.4" y1="446.2" x2="1027.4" y2="464.6" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="448.5" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="1031.2" y1="447.4" x2="1031.2" y2="457.8" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="448.8" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="1035.0" y1="400.1" x2="1035.0" y2="458.2" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="406.3" width="2.35" height="48.8" fill="var(--up)"/>
<line x1="1038.7" y1="397.0" x2="1038.7" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="403.4" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="1042.5" y1="394.3" x2="1042.5" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="408.7" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="1046.3" y1="408.3" x2="1046.3" y2="427.0" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="413.8" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="1050.1" y1="412.0" x2="1050.1" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="420.7" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="60" y1="465.8" x2="1052" y2="465.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="459.8" font-size="11.5" fill="var(--support)" font-weight="600">$140 S1</text>
<text x="1058" y="471.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="420.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="412.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $175 (2026-09-11)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **[기술적 분석 — 일봉·1년](./09_technical_daily.md)의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$175.26** (2026-09-11 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $140 | 4 | 2025-04-07·2026-02-09·2026-06-22·2026-07-27 주 — 2021~2022년 약세장 바닥권에서 형성돼 다섯 해에 걸쳐 네 번 재확인된 구조적 레벨 |
| 참고선 | $445 | — | 역대 최고(2021-11) — 직상장 직후 크립토 강세장 정점의 가격이고, 이후 사업·자본 구조가 크게 달라져 현재 펀더멘털과 연결되지 않는다 |

**표의 "기간 내 상단 저항 없음(신고가 구간)"이라는 비고는 문자 그대로 읽으면 안 된다** — 스크립트가 현재가 위에 터치 2회 이상 클러스터를 찾지 못했을 때 자동으로 붙이는 문구일 뿐이고, 실제 현재가는 역대 최고($444.65, 2021-11) 대비 61% 아래다. 상단에 클러스터가 없는 이유는 신고가여서가 아니라 **2021년 이후 고점들이 서로 너무 멀리 떨어져 있어 ±2.5% 안에 두 개가 모이지 않았기 때문**이다(4. 방법론 · 한계 참고).

반면 **S1($140)은 4회 터치로 이 저장소의 주봉 문서 중에서도 강한 편**이며, 2021년 약세장 저점부터 2026년까지 다섯 해에 걸쳐 반복 확인된 구조적 레벨이다.

---

## 3. 관측된 특이 구간 — 2021~2022 크립토 겨울과 그 이후의 레짐

- 2021-04 나스닥 직상장 직후 형성된 역대 최고 $444.65(2021-11)에서 2022년 말까지 이어진 하락으로 주가가 90% 이상 빠졌다. 2022.06 인력 18% 감원, 2023.01 추가 950명 감원이 이 구간의 대응이다([역사 / 주요 이벤트](./02_history.md) 참고).
- 그 바닥권에서 형성된 가격대가 위 표의 **S1($140)**이며, 이후 2026-02·2026-06·2026-07에 반복해서 다시 확인됐다 — **다섯 해에 걸쳐 네 번 작동한 레벨**이라는 점이 이 문서에서 가장 의미 있는 관측이다.
- 다만 그 사이 회사는 크게 달라졌다. 2025년 SEC 소송 취하·S&P500 편입·Deribit 인수를 거치며 사업 구조와 자본 구조가 모두 바뀌었고, 자기자본은 FY2023 $6,282M에서 FY2025 $14,793M으로 2.4배가 됐다 — **2021~2022년에 만들어진 가격대를 현재 펀더멘털의 지지선으로 곧바로 등치하면 안 되는 이유**다. 역대 최고 $444.65는 같은 이유로 참고선으로만 처리했다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-13. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py COIN --name Coinbase --interval 1wk --ref-line 444.65:"역대 최고(2021-11)" --close-on 2026-09-11 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨이 1개만 나온 것은 이 종목의 변동성 때문이다.** 5년 주가 범위가 $31.55~$444.65로 14배에 달해, 고정 비율(±2.5%) 클러스터링에서는 고가 구간의 스윙들이 같은 클러스터로 묶이기 어렵다. **"저항이 없다"가 아니라 "이 방법론으로는 저항이 잡히지 않는다"로 읽어야 한다.**
    - **5년 구간 안에서 사업 구조가 크게 바뀌었다** — 2025년 Deribit 인수(약 $2.9B)로 파생 사업이 더해졌고 SEC 소송 취하·S&P500 편입으로 규제·수급 환경이 달라졌다. 3. 관측된 특이 구간에 적은 대로 2021~2022년 레벨은 현재 펀더멘털과 직접 연결되지 않는다.
    - 표본 기간에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다(2019.05 6:1 분할은 비상장 시절이라 이 구간 밖이다).

---

*작성일: 2026-09-13*
