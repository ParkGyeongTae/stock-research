# 기술적 분석 (주봉 캔들차트 · 5년)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-21 종가 $40.51은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[일봉 차트](./09_technical_daily.md)와 모두 일치한다.** 데이터 시작이 2021-09-20으로 NYSE 상장일(2021-10-01)보다 앞서는 것은 주봉 구간이 상장 주의 월요일부터 잡히기 때문이다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-20 ~ 2026-09-21)

<style>
.ionq-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ionq-chart svg { width:100%; height:auto; display:block; }
.ionq-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ionq-chart .title { fill: var(--ink); font-weight:600; }
.ionq-chart .grid { stroke: var(--grid); stroke-width:1; }
.ionq-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="ionq-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="IonQ(IONQ) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">IonQ (IONQ) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-20 ~ 2026-09-21 · 마지막 종가 $40.51 (2026-09-21) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="496.5" x2="1052" y2="496.5" class="grid"/>
<text x="52" y="500.5" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="366.9" x2="1052" y2="366.9" class="grid"/>
<text x="52" y="370.9" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="237.4" x2="1052" y2="237.4" class="grid"/>
<text x="52" y="241.4" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="107.8" x2="1052" y2="107.8" class="grid"/>
<text x="52" y="111.8" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="118.7" y1="56.0" x2="118.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="118.7" y1="626.0" x2="118.7" y2="631.0" class="axis"/>
<text x="118.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="315.6" y1="56.0" x2="315.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="315.6" y1="626.0" x2="315.6" y2="631.0" class="axis"/>
<text x="315.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="512.5" y1="56.0" x2="512.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="512.5" y1="626.0" x2="512.5" y2="631.0" class="axis"/>
<text x="512.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="713.1" y1="56.0" x2="713.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="713.1" y1="626.0" x2="713.1" y2="631.0" class="axis"/>
<text x="713.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="910.0" y1="56.0" x2="910.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="910.0" y1="626.0" x2="910.0" y2="631.0" class="axis"/>
<text x="910.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="551.7" x2="61.9" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="552.8" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="65.7" y1="542.1" x2="65.7" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="551.8" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="69.5" y1="564.5" x2="69.5" y2="580.2" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="565.1" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="73.3" y1="558.0" x2="73.3" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="560.9" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="77.0" y1="549.1" x2="77.0" y2="565.2" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="560.9" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="80.8" y1="522.2" x2="80.8" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="528.6" width="2.35" height="35.2" fill="var(--up)"/>
<line x1="84.6" y1="500.4" x2="84.6" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="501.2" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="88.4" y1="476.1" x2="88.4" y2="515.8" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="487.1" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="92.2" y1="393.5" x2="92.2" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="444.6" width="2.35" height="47.4" fill="var(--up)"/>
<line x1="96.0" y1="446.1" x2="96.0" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="450.4" width="2.35" height="19.0" fill="var(--down)"/>
<line x1="99.8" y1="458.6" x2="99.8" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="464.1" width="2.35" height="40.3" fill="var(--down)"/>
<line x1="103.5" y1="481.4" x2="103.5" y2="514.6" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="505.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="107.3" y1="501.4" x2="107.3" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="505.7" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="111.1" y1="507.5" x2="111.1" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="510.3" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="114.9" y1="503.9" x2="114.9" y2="521.5" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="506.2" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="118.7" y1="510.3" x2="118.7" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="515.4" width="2.35" height="17.5" fill="var(--down)"/>
<line x1="122.5" y1="528.7" x2="122.5" y2="544.3" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="536.9" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="126.3" y1="543.0" x2="126.3" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="545.5" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="130.0" y1="550.8" x2="130.0" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="559.3" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="133.8" y1="541.8" x2="133.8" y2="561.2" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="542.4" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="137.6" y1="514.4" x2="137.6" y2="544.8" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="517.1" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="141.4" y1="511.6" x2="141.4" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="521.4" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="145.2" y1="524.2" x2="145.2" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="528.2" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="149.0" y1="518.7" x2="149.0" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="527.0" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="152.8" y1="541.8" x2="152.8" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="545.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="156.5" y1="533.0" x2="156.5" y2="553.3" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="533.0" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="160.3" y1="526.0" x2="160.3" y2="542.1" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="532.1" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="164.1" y1="538.1" x2="164.1" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="540.2" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="167.9" y1="536.9" x2="167.9" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="541.8" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="171.7" y1="549.2" x2="171.7" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="549.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="175.5" y1="554.6" x2="175.5" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="555.9" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="179.3" y1="565.4" x2="179.3" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="567.5" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="183.1" y1="573.5" x2="183.1" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="575.0" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="186.8" y1="588.2" x2="186.8" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="588.8" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="190.6" y1="584.9" x2="190.6" y2="594.8" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="589.5" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="194.4" y1="586.4" x2="194.4" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="587.6" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="198.2" y1="586.4" x2="198.2" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="586.9" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="202.0" y1="586.9" x2="202.0" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="588.8" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="205.8" y1="592.8" x2="205.8" y2="597.6" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="593.4" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="209.6" y1="590.6" x2="209.6" y2="594.6" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="592.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="213.3" y1="591.8" x2="213.3" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="592.3" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="217.1" y1="592.8" x2="217.1" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="593.2" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="220.9" y1="593.6" x2="220.9" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="593.9" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="224.7" y1="591.9" x2="224.7" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="594.4" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="228.5" y1="591.0" x2="228.5" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="591.0" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="232.3" y1="584.3" x2="232.3" y2="592.6" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="584.4" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="236.1" y1="582.9" x2="236.1" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="583.8" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="239.8" y1="570.2" x2="239.8" y2="585.9" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="583.1" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="243.6" y1="579.9" x2="243.6" y2="586.2" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="584.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="247.4" y1="584.8" x2="247.4" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="587.1" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="251.2" y1="588.4" x2="251.2" y2="593.0" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="588.5" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="255.0" y1="587.3" x2="255.0" y2="591.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="590.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="258.8" y1="590.2" x2="258.8" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="591.0" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="262.6" y1="590.4" x2="262.6" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="593.2" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="266.4" y1="587.3" x2="266.4" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="591.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="270.1" y1="591.4" x2="270.1" y2="596.7" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="591.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="273.9" y1="591.1" x2="273.9" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="592.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="277.7" y1="588.8" x2="277.7" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="589.1" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="281.5" y1="586.6" x2="281.5" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="589.4" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="285.3" y1="587.6" x2="285.3" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="588.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="289.1" y1="585.4" x2="289.1" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="588.6" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="292.9" y1="593.5" x2="292.9" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="594.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="296.6" y1="591.9" x2="296.6" y2="595.3" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="594.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="300.4" y1="594.3" x2="300.4" y2="598.1" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="594.5" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="304.2" y1="595.2" x2="304.2" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="597.3" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="308.0" y1="600.7" x2="308.0" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="600.9" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="311.8" y1="602.2" x2="311.8" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="603.7" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="315.6" y1="601.5" x2="315.6" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="601.6" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="319.4" y1="597.4" x2="319.4" y2="602.2" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="597.4" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="323.1" y1="596.5" x2="323.1" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="597.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="326.9" y1="595.4" x2="326.9" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="596.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="330.7" y1="589.0" x2="330.7" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="590.4" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="334.5" y1="587.1" x2="334.5" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="588.4" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="338.3" y1="589.4" x2="338.3" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="594.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="342.1" y1="594.1" x2="342.1" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="594.5" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="345.9" y1="593.3" x2="345.9" y2="597.1" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="593.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="349.6" y1="592.3" x2="349.6" y2="596.9" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="593.2" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="353.4" y1="594.1" x2="353.4" y2="597.6" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="595.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="357.2" y1="593.1" x2="357.2" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="594.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="361.0" y1="582.1" x2="361.0" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="586.2" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="364.8" y1="579.3" x2="364.8" y2="587.7" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="581.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="368.6" y1="578.4" x2="368.6" y2="583.8" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="581.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="372.4" y1="581.5" x2="372.4" y2="587.1" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="582.7" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="376.2" y1="584.9" x2="376.2" y2="591.2" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="585.3" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="379.9" y1="587.4" x2="379.9" y2="591.7" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="587.8" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="383.7" y1="579.9" x2="383.7" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="584.9" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="387.5" y1="564.8" x2="387.5" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="568.5" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="391.3" y1="550.5" x2="391.3" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="561.2" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="395.1" y1="552.5" x2="395.1" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="559.9" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="398.9" y1="552.7" x2="398.9" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="557.7" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="402.7" y1="551.1" x2="402.7" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="557.0" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="406.4" y1="556.9" x2="406.4" y2="568.8" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="563.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="410.2" y1="530.1" x2="410.2" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="538.4" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="414.0" y1="528.4" x2="414.0" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="536.7" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="417.8" y1="526.5" x2="417.8" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="538.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="421.6" y1="520.4" x2="421.6" y2="538.8" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="532.6" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="425.4" y1="509.3" x2="425.4" y2="534.3" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="509.9" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="429.2" y1="495.5" x2="429.2" y2="514.9" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="504.1" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="432.9" y1="511.1" x2="432.9" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="513.2" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="436.7" y1="517.3" x2="436.7" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="518.8" width="2.35" height="20.3" fill="var(--down)"/>
<line x1="440.5" y1="519.6" x2="440.5" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="531.0" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="444.3" y1="511.9" x2="444.3" y2="533.2" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="512.6" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="448.1" y1="496.1" x2="448.1" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="500.7" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="451.9" y1="486.1" x2="451.9" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="501.6" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="455.7" y1="511.5" x2="455.7" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="515.7" width="2.35" height="24.3" fill="var(--down)"/>
<line x1="459.5" y1="523.2" x2="459.5" y2="542.1" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="529.6" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="463.2" y1="526.6" x2="463.2" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="527.0" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="467.0" y1="518.5" x2="467.0" y2="534.1" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="531.7" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="470.8" y1="530.4" x2="470.8" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="534.0" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="474.6" y1="542.6" x2="474.6" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="546.1" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="478.4" y1="547.7" x2="478.4" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="551.0" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="482.2" y1="544.5" x2="482.2" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="549.5" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="486.0" y1="538.0" x2="486.0" y2="557.8" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="543.7" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="489.7" y1="539.3" x2="489.7" y2="547.8" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="542.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="493.5" y1="537.5" x2="493.5" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="537.8" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="497.3" y1="534.7" x2="497.3" y2="544.1" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="537.3" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="501.1" y1="525.6" x2="501.1" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="529.3" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="504.9" y1="527.4" x2="504.9" y2="539.7" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="531.4" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="508.7" y1="535.9" x2="508.7" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="537.5" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="512.5" y1="544.3" x2="512.5" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="546.0" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="516.2" y1="543.5" x2="516.2" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="547.5" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="520.0" y1="552.2" x2="520.0" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="553.5" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="523.8" y1="547.5" x2="523.8" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="553.6" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="527.6" y1="553.3" x2="527.6" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="555.5" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="531.4" y1="553.1" x2="531.4" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="553.7" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="535.2" y1="548.1" x2="535.2" y2="558.3" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="553.9" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="539.0" y1="553.7" x2="539.0" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="555.6" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="542.7" y1="550.1" x2="542.7" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="555.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="546.5" y1="546.2" x2="546.5" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="556.0" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="550.3" y1="556.2" x2="550.3" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="556.2" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="554.1" y1="562.6" x2="554.1" y2="567.3" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="565.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="557.9" y1="561.2" x2="557.9" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="561.3" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="561.7" y1="560.6" x2="561.7" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="561.4" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="565.5" y1="565.4" x2="565.5" y2="574.6" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="566.0" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="569.3" y1="574.0" x2="569.3" y2="580.8" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="574.1" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="573.0" y1="567.9" x2="573.0" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="567.9" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="576.8" y1="565.7" x2="576.8" y2="571.3" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="568.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="580.6" y1="564.7" x2="580.6" y2="571.1" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="566.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="584.4" y1="564.1" x2="584.4" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="569.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="588.2" y1="567.7" x2="588.2" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="568.9" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="592.0" y1="570.2" x2="592.0" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="571.5" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="595.8" y1="572.1" x2="595.8" y2="576.3" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="572.3" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="599.5" y1="571.8" x2="599.5" y2="577.1" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="575.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="603.3" y1="576.5" x2="603.3" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="576.7" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="607.1" y1="579.4" x2="607.1" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="580.5" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="610.9" y1="576.7" x2="610.9" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="578.0" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="614.7" y1="569.2" x2="614.7" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="571.3" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="618.5" y1="567.4" x2="618.5" y2="578.3" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="570.7" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="622.3" y1="571.8" x2="622.3" y2="577.5" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="572.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="626.0" y1="571.2" x2="626.0" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="572.0" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="629.8" y1="577.3" x2="629.8" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="579.9" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="633.6" y1="576.4" x2="633.6" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="578.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="637.4" y1="575.5" x2="637.4" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="578.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="641.2" y1="576.4" x2="641.2" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="577.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="645.0" y1="578.3" x2="645.0" y2="582.5" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="578.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="648.8" y1="575.3" x2="648.8" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="575.7" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="652.5" y1="572.4" x2="652.5" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="572.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="656.3" y1="561.2" x2="656.3" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="563.1" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="660.1" y1="560.5" x2="660.1" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="562.8" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="663.9" y1="556.6" x2="663.9" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="557.0" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="667.7" y1="536.6" x2="667.7" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="539.9" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="671.5" y1="515.6" x2="671.5" y2="541.9" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="516.1" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="675.3" y1="508.1" x2="675.3" y2="531.9" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="512.5" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="679.1" y1="459.7" x2="679.1" y2="534.3" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="465.4" width="2.35" height="64.1" fill="var(--up)"/>
<line x1="682.8" y1="435.1" x2="682.8" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="437.3" width="2.35" height="30.8" fill="var(--up)"/>
<line x1="686.6" y1="407.1" x2="686.6" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="420.0" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="690.4" y1="384.5" x2="690.4" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="389.6" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="694.2" y1="377.0" x2="694.2" y2="426.4" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="380.1" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="698.0" y1="378.2" x2="698.0" y2="444.4" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="379.9" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="701.8" y1="318.9" x2="701.8" y2="416.2" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="338.3" width="2.35" height="77.4" fill="var(--up)"/>
<line x1="705.6" y1="311.5" x2="705.6" y2="367.9" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="331.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="709.3" y1="315.7" x2="709.3" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="316.6" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="713.1" y1="271.4" x2="713.1" y2="458.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="313.1" width="2.35" height="103.4" fill="var(--down)"/>
<line x1="716.9" y1="351.7" x2="716.9" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="374.1" width="2.35" height="60.5" fill="var(--up)"/>
<line x1="720.7" y1="330.9" x2="720.7" y2="374.7" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="362.0" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="724.5" y1="347.6" x2="724.5" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="370.2" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="728.3" y1="337.2" x2="728.3" y2="385.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="363.2" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="732.1" y1="348.4" x2="732.1" y2="389.4" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="370.2" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="735.8" y1="390.7" x2="735.8" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="392.8" width="2.35" height="27.6" fill="var(--down)"/>
<line x1="739.6" y1="415.2" x2="739.6" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="424.2" width="2.35" height="42.7" fill="var(--down)"/>
<line x1="743.4" y1="460.3" x2="743.4" y2="497.0" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="462.0" width="2.35" height="30.9" fill="var(--down)"/>
<line x1="747.2" y1="462.5" x2="747.2" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="464.1" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="751.0" y1="460.8" x2="751.0" y2="492.5" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="464.2" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="754.8" y1="445.7" x2="754.8" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="475.5" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="758.6" y1="458.7" x2="758.6" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="485.6" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="762.4" y1="449.5" x2="762.4" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="457.0" width="2.35" height="42.0" fill="var(--up)"/>
<line x1="766.1" y1="443.0" x2="766.1" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="446.6" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="769.9" y1="419.7" x2="769.9" y2="473.9" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="438.8" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="773.7" y1="423.1" x2="773.7" y2="455.5" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="425.7" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="777.5" y1="409.0" x2="777.5" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="423.5" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="781.3" y1="397.4" x2="781.3" y2="419.2" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="399.4" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="785.1" y1="309.1" x2="785.1" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="330.1" width="2.35" height="78.3" fill="var(--up)"/>
<line x1="788.9" y1="309.0" x2="788.9" y2="371.4" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="324.5" width="2.35" height="40.2" fill="var(--down)"/>
<line x1="792.6" y1="351.4" x2="792.6" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="366.8" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="796.4" y1="340.7" x2="796.4" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="350.5" width="2.35" height="30.4" fill="var(--down)"/>
<line x1="800.2" y1="357.6" x2="800.2" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="364.6" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="804.0" y1="348.7" x2="804.0" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="365.3" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="807.8" y1="330.8" x2="807.8" y2="368.7" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="338.5" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="811.6" y1="315.9" x2="811.6" y2="355.4" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="325.6" width="2.35" height="29.6" fill="var(--down)"/>
<line x1="815.4" y1="317.4" x2="815.4" y2="361.5" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="324.7" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="819.1" y1="316.9" x2="819.1" y2="358.6" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="322.8" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="822.9" y1="337.6" x2="822.9" y2="384.7" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="341.5" width="2.35" height="37.6" fill="var(--down)"/>
<line x1="826.7" y1="343.6" x2="826.7" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="354.9" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="830.5" y1="322.7" x2="830.5" y2="371.6" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="354.3" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="834.3" y1="363.7" x2="834.3" y2="400.8" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="366.9" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="838.1" y1="342.7" x2="838.1" y2="376.4" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="349.2" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="841.9" y1="346.1" x2="841.9" y2="365.5" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="355.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="845.6" y1="262.8" x2="845.6" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="265.8" width="2.35" height="87.6" fill="var(--up)"/>
<line x1="849.4" y1="164.2" x2="849.4" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="169.9" width="2.35" height="87.6" fill="var(--up)"/>
<line x1="853.2" y1="132.9" x2="853.2" y2="202.8" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="184.8" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="857.0" y1="148.2" x2="857.0" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="151.3" width="2.35" height="31.7" fill="var(--up)"/>
<line x1="860.8" y1="88.6" x2="860.8" y2="168.4" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="159.6" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="864.6" y1="77.8" x2="864.6" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="146.0" width="2.35" height="72.4" fill="var(--down)"/>
<line x1="868.4" y1="201.7" x2="868.4" y2="287.4" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="203.0" width="2.35" height="32.5" fill="var(--down)"/>
<line x1="872.2" y1="201.7" x2="872.2" y2="256.3" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="217.9" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="875.9" y1="219.9" x2="875.9" y2="295.3" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="222.1" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="879.7" y1="243.7" x2="879.7" y2="348.6" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="247.1" width="2.35" height="73.3" fill="var(--down)"/>
<line x1="883.5" y1="297.7" x2="883.5" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="323.3" width="2.35" height="32.5" fill="var(--down)"/>
<line x1="887.3" y1="303.1" x2="887.3" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="306.7" width="2.35" height="42.4" fill="var(--up)"/>
<line x1="891.1" y1="267.7" x2="891.1" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="284.7" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="894.9" y1="265.5" x2="894.9" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="276.3" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="898.7" y1="288.2" x2="898.7" y2="333.4" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="297.1" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="902.4" y1="265.9" x2="902.4" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="302.9" width="2.35" height="25.1" fill="var(--down)"/>
<line x1="906.2" y1="321.0" x2="906.2" y2="342.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="323.1" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="910.0" y1="285.2" x2="910.0" y2="324.7" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="305.7" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="913.8" y1="289.7" x2="913.8" y2="319.4" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="297.0" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="917.6" y1="274.7" x2="917.6" y2="330.1" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="306.8" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="921.4" y1="298.3" x2="921.4" y2="373.9" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="313.0" width="2.35" height="54.0" fill="var(--down)"/>
<line x1="925.2" y1="362.2" x2="925.2" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="362.8" width="2.35" height="36.5" fill="var(--down)"/>
<line x1="928.9" y1="389.1" x2="928.9" y2="426.2" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="401.4" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="932.7" y1="400.0" x2="932.7" y2="422.7" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="409.1" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="936.5" y1="354.6" x2="936.5" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="377.5" width="2.35" height="47.6" fill="var(--up)"/>
<line x1="940.3" y1="377.0" x2="940.3" y2="403.8" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="390.0" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="944.1" y1="386.9" x2="944.1" y2="413.3" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="400.8" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="947.9" y1="403.1" x2="947.9" y2="428.4" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="408.9" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="951.7" y1="404.6" x2="951.7" y2="448.7" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="421.1" width="2.35" height="26.8" fill="var(--down)"/>
<line x1="955.5" y1="432.3" x2="955.5" y2="458.3" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="436.2" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="959.2" y1="424.6" x2="959.2" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="436.0" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="963.0" y1="323.6" x2="963.0" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="327.5" width="2.35" height="115.5" fill="var(--up)"/>
<line x1="966.8" y1="307.8" x2="966.8" y2="358.7" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="332.3" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="970.6" y1="326.0" x2="970.6" y2="368.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="326.7" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="974.4" y1="279.6" x2="974.4" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="307.1" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="978.2" y1="242.9" x2="978.2" y2="315.8" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="289.5" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="982.0" y1="199.8" x2="982.0" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="213.8" width="2.35" height="76.6" fill="var(--up)"/>
<line x1="985.7" y1="158.5" x2="985.7" y2="239.2" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="159.2" width="2.35" height="50.3" fill="var(--up)"/>
<line x1="989.5" y1="148.9" x2="989.5" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="174.9" width="2.35" height="83.3" fill="var(--down)"/>
<line x1="993.3" y1="205.6" x2="993.3" y2="281.0" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="240.3" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="997.1" y1="214.3" x2="997.1" y2="283.2" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="228.3" width="2.35" height="31.4" fill="var(--down)"/>
<line x1="1000.9" y1="224.5" x2="1000.9" y2="311.9" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="259.5" width="2.35" height="47.1" fill="var(--down)"/>
<line x1="1004.7" y1="270.8" x2="1004.7" y2="313.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="298.1" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="1008.5" y1="293.5" x2="1008.5" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="308.4" width="2.35" height="40.0" fill="var(--down)"/>
<line x1="1012.2" y1="352.8" x2="1012.2" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="353.5" width="2.35" height="47.2" fill="var(--down)"/>
<line x1="1016.0" y1="390.9" x2="1016.0" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="399.0" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="1019.8" y1="382.2" x2="1019.8" y2="420.0" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="390.0" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="1023.6" y1="337.0" x2="1023.6" y2="396.5" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="338.2" width="2.35" height="55.7" fill="var(--up)"/>
<line x1="1027.4" y1="315.4" x2="1027.4" y2="352.8" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="326.4" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="1031.2" y1="320.2" x2="1031.2" y2="364.8" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="328.0" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="1035.0" y1="343.9" x2="1035.0" y2="375.7" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="345.3" width="2.35" height="26.8" fill="var(--down)"/>
<line x1="1038.7" y1="363.3" x2="1038.7" y2="387.7" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="370.0" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="1042.5" y1="338.2" x2="1042.5" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="351.9" width="2.35" height="36.1" fill="var(--down)"/>
<line x1="1046.3" y1="360.8" x2="1046.3" y2="399.3" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="372.5" width="2.35" height="25.7" fill="var(--up)"/>
<line x1="1050.1" y1="360.9" x2="1050.1" y2="368.0" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="363.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="60" y1="313.4" x2="1052" y2="313.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="316.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$48 R1</text>
<text x="1058" y="328.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="458.2" x2="1052" y2="458.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="452.2" font-size="11.5" fill="var(--support)" font-weight="600">$26 S1</text>
<text x="1058" y="464.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="566.4" x2="1052" y2="566.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="560.4" font-size="11.5" fill="var(--support)" font-weight="600">$9.19 S2</text>
<text x="1058" y="572.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="585.4" x2="1052" y2="585.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="579.4" font-size="11.5" fill="var(--support)" font-weight="600">$6.27 S3</text>
<text x="1058" y="591.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="363.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="355.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $41 (2026-09-21)</text>
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
| R1 | $48 | 3 | 2025-05-26·2025-07-07·2026-08-10 스윙 고점대. **3개 터치가 1년 이상에 걸쳐 있어 이 표에서 가장 반복 검증된 레벨**이다 |
| **현재가** | **$40.51** (2026-09-21 종가) | — | R1과 S1 사이. R1까지 +18.5%, S1까지 -35.8% |
| S1 | $26 | 2 | 2025-01-06·2026-03-30 스윙 저점대. 현재가에 가장 근접한 지지 |
| S2 | $9.19 | 2 | 2022-01-24·2023-10-30 스윙 저점대. **상장 초기~2023년의 저가권**이며 현재가 대비 -77.3%다 |
| S3 | $6.27 | 2 | 2024-06-17·2024-08-05 스윙 저점대. 2024년 하반기 급등 직전의 바닥권 |
| 참고선 | $84.64 | — | 최근 5년 최고가(최근 1년 최고와 동일). 현재가 대비 +108.9% |
| 참고선 | $3.04 | — | 최근 5년 최저가. S3($6.27)보다 아래이며 단일 저점이라 클러스터를 이루지 않았다 |

> **S2·S3은 현재가에서 -77% 이상 떨어져 있어 실질적인 근시일 지지로 보기 어렵다.** 2024년 하반기 이후 주가 레짐이 한 자릿수에서 $25~$85 구간으로 통째로 이동했기 때문이며(3절 참고), 이 표에 남긴 것은 "그 이전 레짐이 어디였는지"를 기록하기 위해서다.

---

## 3. 관측된 특이 구간 — 2024년 하반기 가격 레짐 이동

- 2021-10 상장 이후 2024년 중반까지 주가는 대체로 한 자릿수~$10대에 머물렀고(S2 $9.19·S3 $6.27 클러스터가 그 구간이다), 5년 최저가는 $3.04다.
- 2024년 하반기부터 주가대가 통째로 올라서 2025~2026년에는 $25~$85 구간에서 움직였다. **이 이동으로 상장 초기 스윙 레벨(S2·S3)은 현재 가격대와 단절됐다.**
- 이 기간은 [역사 / 주요 이벤트](./02_history.md)에서 회사가 **연쇄 인수와 대규모 워런트 발행으로 규모·자본구조를 바꾼 시기**와 겹친다. 주가 차트만으로는 보이지 않지만 **분모(발행주식수)도 같이 커졌다** — 기말 발행주식수가 FY2023 2.066억 주 → 현재 약 3.973억 주로 +92% 늘었으므로, 주가 배수와 시가총액 배수는 전혀 다른 값이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-20~2026-09-21. 수집 시점: 2026-09-22. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py IONQ --name IonQ --interval 1wk --close-on 2026-09-21 --emit all` (재현용 — 옵션 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 레짐 이동 때문에 이 표의 레벨은 두 세계가 섞여 있다.** S2($9.19)·S3($6.27)은 2022~2024년 가격대이고 R1($48)·S1($26)은 2025년 이후 가격대다. 같은 표에 있다고 해서 같은 강도로 읽으면 안 된다 — **근시일 판단에 쓸 수 있는 것은 R1과 S1뿐**이다.
    - 해당 기간에 주식분할·병합은 없었다(2021-10 상장 이후 이력 없음). 다만 연쇄 M&A의 주식대가 지급과 2025년 사모워런트 발행으로 **발행주식수가 계속 늘어왔으므로**, 주가의 시계열 연속성과 주주가치의 연속성은 다르다([핵심 지표](./04_metrics.md) A.4 희석주식수 증감률).

---

*작성일: 2026-09-22*
