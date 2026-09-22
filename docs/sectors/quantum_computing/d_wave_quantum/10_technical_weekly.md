# 기술적 분석 (주봉 캔들차트 · 5년)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: **2026-09-21 종가 $17.70은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[일봉 차트](./09_technical_daily.md)와 모두 일치한다.** 데이터 시작이 2021-09-20으로 NYSE 상장일(2022-08)보다 앞서는 것은 **SPAC(DPCM Capital) 시절의 주가가 같은 계보로 이어지기 때문**이며, 아래 S2($0.57)가 그 구간의 흔적이다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-20 ~ 2026-09-21)

<style>
.qbts-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .qbts-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.qbts-chart svg { width:100%; height:auto; display:block; }
.qbts-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.qbts-chart .title { fill: var(--ink); font-weight:600; }
.qbts-chart .grid { stroke: var(--grid); stroke-width:1; }
.qbts-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="qbts-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="D-Wave Quantum(QBTS) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">D-Wave Quantum (QBTS) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-20 ~ 2026-09-21 · 마지막 종가 $17.70 (2026-09-21) · 단위 USD</text>
<line x1="60" y1="614.5" x2="1052" y2="614.5" class="grid"/>
<text x="52" y="618.5" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="499.3" x2="1052" y2="499.3" class="grid"/>
<text x="52" y="503.3" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="384.2" x2="1052" y2="384.2" class="grid"/>
<text x="52" y="388.2" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="269.0" x2="1052" y2="269.0" class="grid"/>
<text x="52" y="273.0" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="153.9" x2="1052" y2="153.9" class="grid"/>
<text x="52" y="157.9" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
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
<line x1="61.9" y1="501.8" x2="61.9" y2="502.6" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="501.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="501.6" x2="65.7" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="501.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="69.5" y1="501.5" x2="69.5" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="501.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="73.3" y1="501.4" x2="73.3" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="501.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="77.0" y1="501.4" x2="77.0" y2="502.0" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="501.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="80.8" y1="501.4" x2="80.8" y2="501.8" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="501.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="84.6" y1="501.3" x2="84.6" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="501.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="88.4" y1="501.1" x2="88.4" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="501.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="92.2" y1="500.8" x2="92.2" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="501.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="96.0" y1="500.6" x2="96.0" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="500.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="99.8" y1="500.7" x2="99.8" y2="501.5" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="501.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="103.5" y1="501.1" x2="103.5" y2="501.5" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="501.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="107.3" y1="500.6" x2="107.3" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="501.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="111.1" y1="501.4" x2="111.1" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="501.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="114.9" y1="501.3" x2="114.9" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="501.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="118.7" y1="501.1" x2="118.7" y2="501.6" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="501.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="122.5" y1="501.3" x2="122.5" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="501.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="126.3" y1="501.1" x2="126.3" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="501.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="130.0" y1="501.5" x2="130.0" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="501.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="133.8" y1="501.4" x2="133.8" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="501.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="137.6" y1="495.5" x2="137.6" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="500.3" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="141.4" y1="499.8" x2="141.4" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="499.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="145.2" y1="500.1" x2="145.2" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="500.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="149.0" y1="500.4" x2="149.0" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="500.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="152.8" y1="500.5" x2="152.8" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="500.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="156.5" y1="500.7" x2="156.5" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="500.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="160.3" y1="500.4" x2="160.3" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="500.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="164.1" y1="500.5" x2="164.1" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="500.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="167.9" y1="500.5" x2="167.9" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="500.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="171.7" y1="500.5" x2="171.7" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="500.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="175.5" y1="500.5" x2="175.5" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="500.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="179.3" y1="500.5" x2="179.3" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="500.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="183.1" y1="500.4" x2="183.1" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="500.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="186.8" y1="500.6" x2="186.8" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="500.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="190.6" y1="500.6" x2="190.6" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="500.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="194.4" y1="500.6" x2="194.4" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="500.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="198.2" y1="500.5" x2="198.2" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="500.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="202.0" y1="500.4" x2="202.0" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="500.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="205.8" y1="500.4" x2="205.8" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="500.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="209.6" y1="500.3" x2="209.6" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="500.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="213.3" y1="500.1" x2="213.3" y2="500.5" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="500.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="217.1" y1="500.1" x2="217.1" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="500.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="220.9" y1="499.4" x2="220.9" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="499.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="224.7" y1="499.3" x2="224.7" y2="499.8" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="499.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="228.5" y1="499.3" x2="228.5" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="499.6" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="232.3" y1="507.3" x2="232.3" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="514.8" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="236.1" y1="462.1" x2="236.1" y2="528.1" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="489.4" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="239.8" y1="482.1" x2="239.8" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="487.8" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="243.6" y1="505.1" x2="243.6" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="509.9" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="247.4" y1="509.1" x2="247.4" y2="545.6" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="509.6" width="2.35" height="34.7" fill="var(--down)"/>
<line x1="251.2" y1="531.5" x2="251.2" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="536.4" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="255.0" y1="516.6" x2="255.0" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="530.4" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="258.8" y1="524.1" x2="258.8" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="531.6" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="262.6" y1="518.9" x2="262.6" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="523.9" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="266.4" y1="519.0" x2="266.4" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="520.3" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="270.1" y1="520.6" x2="270.1" y2="539.5" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="522.0" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="273.9" y1="529.3" x2="273.9" y2="560.6" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="536.2" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="277.7" y1="555.9" x2="277.7" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="556.9" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="281.5" y1="568.9" x2="281.5" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="570.4" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="285.3" y1="582.3" x2="285.3" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="582.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="289.1" y1="582.2" x2="289.1" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="583.0" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="292.9" y1="583.6" x2="292.9" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="585.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="296.6" y1="583.4" x2="296.6" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="585.0" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="300.4" y1="584.8" x2="300.4" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="587.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="304.2" y1="585.2" x2="304.2" y2="593.1" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="586.4" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="308.0" y1="589.3" x2="308.0" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="589.5" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="311.8" y1="593.6" x2="311.8" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="595.0" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="315.6" y1="596.9" x2="315.6" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="597.2" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="319.4" y1="591.5" x2="319.4" y2="602.7" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="595.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="323.1" y1="595.2" x2="323.1" y2="600.6" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="595.3" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="326.9" y1="599.2" x2="326.9" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="599.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="330.7" y1="596.1" x2="330.7" y2="601.6" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="596.3" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="334.5" y1="593.2" x2="334.5" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="593.8" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="338.3" y1="601.2" x2="338.3" y2="604.5" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="601.2" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="342.1" y1="603.5" x2="342.1" y2="606.0" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="603.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="345.9" y1="605.3" x2="345.9" y2="606.8" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="605.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="349.6" y1="604.9" x2="349.6" y2="607.3" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="604.9" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="353.4" y1="607.1" x2="353.4" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="607.4" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="357.2" y1="607.8" x2="357.2" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="608.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="361.0" y1="606.7" x2="361.0" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="606.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="364.8" y1="605.0" x2="364.8" y2="606.7" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="605.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="604.5" x2="368.6" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="605.2" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="372.4" y1="606.8" x2="372.4" y2="608.6" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="608.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="376.2" y1="607.5" x2="376.2" y2="609.0" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="607.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="379.9" y1="608.7" x2="379.9" y2="609.7" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="608.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="383.7" y1="609.1" x2="383.7" y2="609.9" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="609.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="387.5" y1="607.2" x2="387.5" y2="609.7" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="608.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="391.3" y1="595.3" x2="391.3" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="595.3" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="395.1" y1="594.7" x2="395.1" y2="601.2" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="595.0" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="398.9" y1="583.6" x2="398.9" y2="598.1" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="588.5" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="402.7" y1="587.9" x2="402.7" y2="593.6" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="588.1" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="406.4" y1="591.6" x2="406.4" y2="597.6" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="592.5" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="410.2" y1="587.2" x2="410.2" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="590.4" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="414.0" y1="586.8" x2="414.0" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="589.4" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="417.8" y1="582.2" x2="417.8" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="589.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="421.6" y1="577.6" x2="421.6" y2="589.4" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="586.7" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="425.4" y1="584.9" x2="425.4" y2="593.1" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="585.9" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="429.2" y1="583.2" x2="429.2" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="590.4" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="432.9" y1="592.0" x2="432.9" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="592.3" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="436.7" y1="595.4" x2="436.7" y2="600.3" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="597.1" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="440.5" y1="597.8" x2="440.5" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="598.7" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="444.3" y1="599.9" x2="444.3" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="601.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="448.1" y1="600.6" x2="448.1" y2="604.6" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="601.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="451.9" y1="601.5" x2="451.9" y2="604.0" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="602.5" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="455.7" y1="602.4" x2="455.7" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="602.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="459.5" y1="602.5" x2="459.5" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="603.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="463.2" y1="603.1" x2="463.2" y2="604.8" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="603.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="467.0" y1="601.1" x2="467.0" y2="603.7" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="603.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="470.8" y1="602.7" x2="470.8" y2="605.7" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="603.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="474.6" y1="605.0" x2="474.6" y2="607.6" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="605.7" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="478.4" y1="603.2" x2="478.4" y2="607.9" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="604.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="482.2" y1="603.8" x2="482.2" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="604.1" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="486.0" y1="603.7" x2="486.0" y2="606.5" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="604.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="489.7" y1="603.5" x2="489.7" y2="605.5" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="604.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="493.5" y1="603.5" x2="493.5" y2="605.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="603.6" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="497.3" y1="601.9" x2="497.3" y2="604.3" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="602.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="501.1" y1="602.2" x2="501.1" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="602.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="504.9" y1="602.5" x2="504.9" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="603.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="508.7" y1="603.2" x2="508.7" y2="604.7" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="603.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="512.5" y1="604.3" x2="512.5" y2="605.5" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="604.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="516.2" y1="604.4" x2="516.2" y2="606.0" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="604.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="520.0" y1="605.6" x2="520.0" y2="606.6" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="605.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="523.8" y1="604.5" x2="523.8" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="605.0" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="527.6" y1="603.3" x2="527.6" y2="605.5" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="603.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="531.4" y1="601.9" x2="531.4" y2="604.5" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="601.9" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="535.2" y1="590.5" x2="535.2" y2="600.8" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="594.4" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="539.0" y1="589.5" x2="539.0" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="589.7" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="542.7" y1="590.2" x2="542.7" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="593.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="546.5" y1="591.2" x2="546.5" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="593.0" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="550.3" y1="586.4" x2="550.3" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="590.5" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="554.1" y1="586.6" x2="554.1" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="589.8" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="557.9" y1="589.6" x2="557.9" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="591.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="561.7" y1="589.2" x2="561.7" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="591.1" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="565.5" y1="591.7" x2="565.5" y2="596.3" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="591.9" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="569.3" y1="593.7" x2="569.3" y2="597.0" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="595.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="573.0" y1="595.1" x2="573.0" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="596.3" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="576.8" y1="597.0" x2="576.8" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="597.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="580.6" y1="596.9" x2="580.6" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="597.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="584.4" y1="597.2" x2="584.4" y2="600.3" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="599.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="588.2" y1="599.4" x2="588.2" y2="601.2" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="599.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="592.0" y1="595.3" x2="592.0" y2="600.1" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="598.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="595.8" y1="598.2" x2="595.8" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="598.7" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="599.5" y1="600.4" x2="599.5" y2="601.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="600.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="603.3" y1="600.2" x2="603.3" y2="601.7" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="600.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="607.1" y1="600.4" x2="607.1" y2="602.5" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="600.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="610.9" y1="601.1" x2="610.9" y2="602.4" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="601.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="614.7" y1="599.1" x2="614.7" y2="601.8" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="600.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="618.5" y1="598.4" x2="618.5" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="600.3" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="622.3" y1="601.5" x2="622.3" y2="603.5" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="602.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="626.0" y1="602.3" x2="626.0" y2="604.7" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="602.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="629.8" y1="604.0" x2="629.8" y2="605.8" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="604.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="633.6" y1="603.0" x2="633.6" y2="604.8" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="603.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="637.4" y1="601.7" x2="637.4" y2="604.2" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="602.2" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="641.2" y1="602.2" x2="641.2" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="602.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="645.0" y1="602.9" x2="645.0" y2="604.6" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="602.9" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="648.8" y1="602.6" x2="648.8" y2="605.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="602.9" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="652.5" y1="602.7" x2="652.5" y2="603.8" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="603.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="656.3" y1="602.2" x2="656.3" y2="604.1" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="602.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="660.1" y1="602.6" x2="660.1" y2="604.1" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="602.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="663.9" y1="603.0" x2="663.9" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="603.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="667.7" y1="600.6" x2="667.7" y2="603.2" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="601.0" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="671.5" y1="598.5" x2="671.5" y2="602.5" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="600.6" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="675.3" y1="600.1" x2="675.3" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="602.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="679.1" y1="596.1" x2="679.1" y2="603.3" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="596.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="682.8" y1="589.7" x2="682.8" y2="597.6" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="594.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="686.6" y1="579.9" x2="686.6" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="580.7" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="690.4" y1="571.1" x2="690.4" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="575.1" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="694.2" y1="554.4" x2="694.2" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="556.2" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="698.0" y1="552.5" x2="698.0" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="553.9" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="701.8" y1="493.6" x2="701.8" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="540.3" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="705.6" y1="483.1" x2="705.6" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="500.4" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="709.3" y1="497.6" x2="709.3" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="508.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="713.1" y1="492.7" x2="713.1" y2="560.9" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="508.9" width="2.35" height="39.2" fill="var(--down)"/>
<line x1="716.9" y1="540.3" x2="716.9" y2="571.4" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="553.8" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="720.7" y1="532.6" x2="720.7" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="544.4" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="724.5" y1="540.9" x2="724.5" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="546.1" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="728.3" y1="537.8" x2="728.3" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="547.6" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="732.1" y1="536.2" x2="732.1" y2="553.3" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="541.1" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="735.8" y1="519.9" x2="735.8" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="531.0" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="739.6" y1="530.8" x2="739.6" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="530.8" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="743.4" y1="548.0" x2="743.4" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="550.2" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="747.2" y1="497.0" x2="747.2" y2="562.8" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="497.6" width="2.35" height="59.2" fill="var(--up)"/>
<line x1="751.0" y1="476.9" x2="751.0" y2="520.5" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="488.9" width="2.35" height="29.4" fill="var(--down)"/>
<line x1="754.8" y1="506.8" x2="754.8" y2="531.0" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="512.0" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="758.6" y1="521.3" x2="758.6" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="531.5" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="762.4" y1="527.0" x2="762.4" y2="548.0" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="531.0" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="766.1" y1="525.0" x2="766.1" y2="542.3" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="527.3" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="769.9" y1="526.2" x2="769.9" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="527.8" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="773.7" y1="520.8" x2="773.7" y2="539.4" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="523.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="777.5" y1="479.9" x2="777.5" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="486.8" width="2.35" height="38.9" fill="var(--up)"/>
<line x1="781.3" y1="468.7" x2="781.3" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="473.4" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="785.1" y1="386.9" x2="785.1" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="398.0" width="2.35" height="72.3" fill="var(--up)"/>
<line x1="788.9" y1="390.7" x2="788.9" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="392.5" width="2.35" height="34.0" fill="var(--down)"/>
<line x1="792.6" y1="398.1" x2="792.6" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="400.1" width="2.35" height="27.5" fill="var(--up)"/>
<line x1="796.4" y1="396.3" x2="796.4" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="397.1" width="2.35" height="42.7" fill="var(--down)"/>
<line x1="800.2" y1="421.1" x2="800.2" y2="441.5" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="434.3" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="804.0" y1="436.7" x2="804.0" y2="458.2" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="441.5" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="807.8" y1="420.7" x2="807.8" y2="455.2" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="421.1" width="2.35" height="30.7" fill="var(--up)"/>
<line x1="811.6" y1="412.5" x2="811.6" y2="444.5" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="422.1" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="815.4" y1="389.6" x2="815.4" y2="443.0" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="397.0" width="2.35" height="43.9" fill="var(--up)"/>
<line x1="819.1" y1="377.7" x2="819.1" y2="421.3" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="390.5" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="822.9" y1="390.6" x2="822.9" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="392.2" width="2.35" height="33.6" fill="var(--down)"/>
<line x1="826.7" y1="393.7" x2="826.7" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="419.9" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="830.5" y1="394.7" x2="830.5" y2="424.3" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="418.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="834.3" y1="417.9" x2="834.3" y2="451.0" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="418.8" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="838.1" y1="426.9" x2="838.1" y2="444.5" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="434.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="841.9" y1="428.9" x2="841.9" y2="444.3" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="437.5" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="845.6" y1="407.4" x2="845.6" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="410.0" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="849.4" y1="299.8" x2="849.4" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="305.0" width="2.35" height="105.7" fill="var(--up)"/>
<line x1="853.2" y1="278.5" x2="853.2" y2="351.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="306.3" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="857.0" y1="231.3" x2="857.0" y2="341.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="237.9" width="2.35" height="65.4" fill="var(--up)"/>
<line x1="860.8" y1="159.1" x2="860.8" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="234.3" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="864.6" y1="76.2" x2="864.6" y2="238.9" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="173.1" width="2.35" height="46.6" fill="var(--up)"/>
<line x1="868.4" y1="157.6" x2="868.4" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="159.4" width="2.35" height="79.1" fill="var(--down)"/>
<line x1="872.2" y1="183.4" x2="872.2" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="187.7" width="2.35" height="35.4" fill="var(--up)"/>
<line x1="875.9" y1="181.3" x2="875.9" y2="310.3" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="183.6" width="2.35" height="91.2" fill="var(--down)"/>
<line x1="879.7" y1="250.6" x2="879.7" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="267.8" width="2.35" height="74.8" fill="var(--down)"/>
<line x1="883.5" y1="330.2" x2="883.5" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="347.0" width="2.35" height="32.5" fill="var(--down)"/>
<line x1="887.3" y1="345.7" x2="887.3" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="353.4" width="2.35" height="24.8" fill="var(--up)"/>
<line x1="891.1" y1="281.7" x2="891.1" y2="369.0" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="303.6" width="2.35" height="57.5" fill="var(--up)"/>
<line x1="894.9" y1="278.8" x2="894.9" y2="324.1" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="293.0" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="898.7" y1="300.2" x2="898.7" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="305.6" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="902.4" y1="241.5" x2="902.4" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="296.0" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="906.2" y1="288.0" x2="906.2" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="290.6" width="2.35" height="32.1" fill="var(--up)"/>
<line x1="910.0" y1="244.2" x2="910.0" y2="295.3" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="284.5" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="913.8" y1="253.4" x2="913.8" y2="297.7" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="282.5" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="917.6" y1="286.5" x2="917.6" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="297.0" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="921.4" y1="314.8" x2="921.4" y2="376.1" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="319.7" width="2.35" height="50.4" fill="var(--down)"/>
<line x1="925.2" y1="366.1" x2="925.2" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="366.7" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="928.9" y1="366.7" x2="928.9" y2="402.0" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="379.3" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="932.7" y1="388.6" x2="932.7" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="394.5" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="936.5" y1="364.6" x2="936.5" y2="414.0" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="398.2" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="940.3" y1="388.7" x2="940.3" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="400.4" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="944.1" y1="389.7" x2="944.1" y2="413.8" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="405.7" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="947.9" y1="402.4" x2="947.9" y2="439.2" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="407.4" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="951.7" y1="421.9" x2="951.7" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="433.6" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="955.5" y1="441.9" x2="955.5" y2="467.7" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="449.6" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="959.2" y1="437.7" x2="959.2" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="450.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="963.0" y1="355.5" x2="963.0" y2="455.5" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="364.7" width="2.35" height="87.6" fill="var(--up)"/>
<line x1="966.8" y1="362.0" x2="966.8" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="372.4" width="2.35" height="29.2" fill="var(--down)"/>
<line x1="970.6" y1="376.5" x2="970.6" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="378.5" width="2.35" height="27.1" fill="var(--up)"/>
<line x1="974.4" y1="337.7" x2="974.4" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="354.6" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="978.2" y1="329.1" x2="978.2" y2="381.9" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="358.8" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="982.0" y1="251.2" x2="982.0" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="275.9" width="2.35" height="107.0" fill="var(--up)"/>
<line x1="985.7" y1="266.5" x2="985.7" y2="318.6" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="267.4" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="989.5" y1="254.1" x2="989.5" y2="346.4" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="281.1" width="2.35" height="58.7" fill="var(--down)"/>
<line x1="993.3" y1="306.7" x2="993.3" y2="357.1" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="330.1" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="997.1" y1="301.8" x2="997.1" y2="354.9" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="327.6" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="1000.9" y1="306.9" x2="1000.9" y2="373.5" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="333.6" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="1004.7" y1="329.7" x2="1004.7" y2="357.7" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="347.7" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="1008.5" y1="342.4" x2="1008.5" y2="384.8" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="356.1" width="2.35" height="27.1" fill="var(--down)"/>
<line x1="1012.2" y1="387.8" x2="1012.2" y2="430.0" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="387.8" width="2.35" height="34.1" fill="var(--down)"/>
<line x1="1016.0" y1="407.0" x2="1016.0" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="418.7" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="1019.8" y1="389.5" x2="1019.8" y2="429.4" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="406.3" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="1023.6" y1="361.2" x2="1023.6" y2="407.2" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="375.4" width="2.35" height="30.7" fill="var(--up)"/>
<line x1="1027.4" y1="364.0" x2="1027.4" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="370.7" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="1031.2" y1="368.6" x2="1031.2" y2="402.1" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="375.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="1035.0" y1="384.8" x2="1035.0" y2="422.5" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="387.1" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="1038.7" y1="414.7" x2="1038.7" y2="428.1" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="422.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="1042.5" y1="401.7" x2="1042.5" y2="424.1" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="410.7" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="1046.3" y1="406.1" x2="1046.3" y2="432.4" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="417.5" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="1050.1" y1="408.1" x2="1050.1" y2="414.3" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="410.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="60" y1="501.2" x2="1052" y2="501.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="495.2" font-size="11.5" fill="var(--support)" font-weight="600">$9.84 S1</text>
<text x="1058" y="507.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="607.9" x2="1052" y2="607.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="601.9" font-size="11.5" fill="var(--support)" font-weight="600">$0.57 S2</text>
<text x="1058" y="613.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="410.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="402.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $17.70 (2026-09-21)</text>
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
| **현재가** | **$17.70** (2026-09-21 종가) | — | **위쪽에 검출된 저항 레벨이 없다** — 스윙 고점은 있으나 터치 2회 이상으로 묶인 클러스터가 만들어지지 않았다(가장 먼 스윙 고점은 $47, 현재가 대비 +164%). 표본 한계이며 4절에 사유를 남겼다 |
| S1 | $9.84 | 5 | 2022-01-24·2022-03-14·2022-05-09·2022-05-16·2022-05-23 스윙 저점대. **전부 2022년 상반기(SPAC 합병 전후)**에 몰려 있다. 현재가 대비 -44.4% |
| S2 | $0.57 | 2 | 2023-10-30·2023-11-06 스윙 저점대. **자기자본이 마이너스(-$24M)였던 FY2023의 바닥권**이다([핵심 지표](./04_metrics.md) A.3). 현재가 대비 -96.8% |
| 참고선 | $46.75 | — | 최근 5년 최고가(최근 1년 최고와 동일). 현재가 대비 +164.1% |
| 참고선 | $0.40 | — | 최근 5년 최저가. S2($0.57)보다 아래이며 단일 저점이라 클러스터를 이루지 않았다 |

> **이 표는 근시일 판단에 거의 쓸 수 없다.** 두 지지선이 모두 2022~2023년 가격대(현재가 대비 -44%·-97%)이고 저항은 아예 검출되지 않았다. 주봉·5년 스케일에서 이 종목에 대해 말할 수 있는 것은 레벨이 아니라 **레짐이 통째로 바뀌었다**는 사실뿐이며, 그 내용은 3절에 적었다. 근시일 레벨은 [일봉 문서](./09_technical_daily.md)를 볼 것.

---

## 3. 관측된 특이 구간 — 2024년 하반기 이후의 레짐 이동

- 2022-08 상장 이후 2024년 중반까지 주가는 대체로 $1 미만~$10 구간에 머물렀다. 5년 최저가는 $0.57(클러스터 기준, 단일 저점으로는 $0.40)이고, S1($9.84) 터치 5회가 전부 2022년 상반기에 몰려 있다.
- 2024년 하반기부터 가격대가 통째로 올라 2025~2026년에는 $12~$47 구간에서 움직였다. **이 이동으로 상장 초기 스윙 레벨은 현재 가격대와 완전히 단절됐다.**
- 이 기간은 [역사 / 주요 이벤트](./02_history.md)에서 회사가 **대규모 자본조달로 순현금을 확보하고(FY2025말 $884.5M) Quantum Circuits 인수로 게이트 모델 축을 더한 시기**와 겹친다. 다만 같은 기간 **발행주식수도 FY2024 +68.2%·FY2025 +30.2%·2026년 +8.3%로 계속 늘었다** — 기말 발행주식수가 FY2023 약 1.60억 주에서 현재 3.80억 주로 2.4배가 됐으므로, **주가 배수와 시가총액 배수는 전혀 다른 값이다.**
- 매출은 이 레짐 이동에 거의 참여하지 않았다. FY2023 $8.8M → TTM $12.43M으로, 주가가 20배 넘게 오르는 동안 매출은 1.4배 늘었다([핵심 지표](./04_metrics.md) A.1).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-20~2026-09-21. 수집 시점: 2026-09-22. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py QBTS --name "D-Wave Quantum" --interval 1wk --close-on 2026-09-21 --emit all` (재현용 — 옵션 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **저항 레벨이 하나도 검출되지 않은 것은 표본 한계이지 "위가 비어 있다"는 뜻이 아니다.** 2024년 하반기 이후 주가가 $12~$47을 빠르게 오간 탓에 스윙 고점들이 넓게 흩어져 ±2.5% 안에 2회 이상 겹치는 클러스터가 만들어지지 않았다. 레벨 수를 억지로 채우지 않고 비워 뒀으며(`--force-level` 미사용), **근시일 저항은 일봉 문서의 R1($22)·R2($32)를 볼 것.**
    - 검출된 두 지지선이 모두 2022~2023년 가격대라 **현재 가격대와 단절**돼 있다(3절 레짐 이동). 같은 표에 있다고 해서 현재 유효한 레벨로 읽으면 안 된다.
    - 해당 기간에 주식분할·병합은 없었다(2022-08 상장 이후 이력 없음). 다만 증자·M&A 주식대가·정부 지분 발행으로 **발행주식수가 3년간 2.4배가 됐으므로**, 주가의 시계열 연속성과 주주가치의 연속성은 다르다([핵심 지표](./04_metrics.md) A.4 주식수 증감률).

---

*작성일: 2026-09-22*
