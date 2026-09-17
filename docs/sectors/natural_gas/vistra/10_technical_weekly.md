# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL)와는 계보가 다르다.
- **대조 결과**: **2026-09-04 종가 $149.30은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[기술적 분석 (일봉)](./09_technical_daily.md)와 모두 일치한다.**

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-06 ~ 2026-09-04)

<style>
.vst-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .vst-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.vst-chart svg { width:100%; height:auto; display:block; }
.vst-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.vst-chart .title { fill: var(--ink); font-weight:600; }
.vst-chart .grid { stroke: var(--grid); stroke-width:1; }
.vst-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="vst-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vistra(VST) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Vistra (VST) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-04 · 마지막 종가 $149.30 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="522.4" x2="1052" y2="522.4" class="grid"/>
<text x="52" y="526.4" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="392.8" x2="1052" y2="392.8" class="grid"/>
<text x="52" y="396.8" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="263.3" x2="1052" y2="263.3" class="grid"/>
<text x="52" y="267.3" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="133.7" x2="1052" y2="133.7" class="grid"/>
<text x="52" y="137.7" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
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
<line x1="61.9" y1="601.9" x2="61.9" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="602.7" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="65.7" y1="603.4" x2="65.7" y2="605.9" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="603.8" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="69.5" y1="605.7" x2="69.5" y2="608.1" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="606.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="73.3" y1="606.2" x2="73.3" y2="609.1" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="606.4" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="77.0" y1="604.4" x2="77.0" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="605.5" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="80.8" y1="599.8" x2="80.8" y2="606.7" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="600.9" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="84.6" y1="601.0" x2="84.6" y2="602.7" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="601.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="88.4" y1="600.4" x2="88.4" y2="602.5" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="601.2" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="92.2" y1="598.0" x2="92.2" y2="602.9" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="598.8" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="96.0" y1="598.5" x2="96.0" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="598.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="99.8" y1="598.6" x2="99.8" y2="601.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="600.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="103.5" y1="597.6" x2="103.5" y2="600.3" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="599.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="107.3" y1="596.8" x2="107.3" y2="601.0" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="598.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="111.1" y1="596.7" x2="111.1" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="597.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="114.9" y1="596.6" x2="114.9" y2="599.0" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="596.9" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="118.7" y1="593.7" x2="118.7" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="594.8" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="122.5" y1="592.7" x2="122.5" y2="595.4" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="592.9" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="126.3" y1="592.4" x2="126.3" y2="595.0" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="592.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="130.0" y1="592.3" x2="130.0" y2="594.1" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="593.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="133.8" y1="592.8" x2="133.8" y2="596.4" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="593.5" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="137.6" y1="594.3" x2="137.6" y2="597.2" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="595.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="141.4" y1="594.2" x2="141.4" y2="596.8" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="595.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="145.2" y1="593.1" x2="145.2" y2="596.0" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="595.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="149.0" y1="595.0" x2="149.0" y2="596.9" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="595.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="152.8" y1="593.8" x2="152.8" y2="599.4" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="595.2" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="156.5" y1="592.6" x2="156.5" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="593.6" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="160.3" y1="591.1" x2="160.3" y2="594.2" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="593.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="164.1" y1="593.0" x2="164.1" y2="595.1" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="593.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="167.9" y1="592.8" x2="167.9" y2="595.5" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="593.0" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="171.7" y1="590.8" x2="171.7" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="591.2" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="175.5" y1="588.2" x2="175.5" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="588.4" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="179.3" y1="588.0" x2="179.3" y2="590.6" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="588.4" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="183.1" y1="582.9" x2="183.1" y2="589.9" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="586.2" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="186.8" y1="585.9" x2="186.8" y2="588.2" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="586.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="190.6" y1="581.7" x2="190.6" y2="589.3" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="582.9" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="194.4" y1="583.4" x2="194.4" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="583.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="198.2" y1="583.4" x2="198.2" y2="588.7" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="586.5" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="202.0" y1="583.4" x2="202.0" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="583.7" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="205.8" y1="582.8" x2="205.8" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="583.2" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="209.6" y1="580.9" x2="209.6" y2="586.0" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="584.6" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="213.3" y1="587.0" x2="213.3" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="587.1" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="217.1" y1="590.8" x2="217.1" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="591.3" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="220.9" y1="589.6" x2="220.9" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="591.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="224.7" y1="592.0" x2="224.7" y2="597.5" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="592.4" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="228.5" y1="592.1" x2="228.5" y2="595.5" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="593.4" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="232.3" y1="590.4" x2="232.3" y2="593.2" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="592.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="236.1" y1="584.9" x2="236.1" y2="592.9" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="584.9" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="239.8" y1="584.8" x2="239.8" y2="588.9" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="585.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="243.6" y1="584.8" x2="243.6" y2="588.9" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="584.9" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="247.4" y1="584.2" x2="247.4" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="585.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="251.2" y1="584.6" x2="251.2" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="587.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="255.0" y1="585.8" x2="255.0" y2="589.7" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="587.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="258.8" y1="586.0" x2="258.8" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="586.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="262.6" y1="584.9" x2="262.6" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="586.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="266.4" y1="585.0" x2="266.4" y2="592.1" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="587.0" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="270.1" y1="591.4" x2="270.1" y2="597.7" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="592.0" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="273.9" y1="592.0" x2="273.9" y2="597.4" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="595.0" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="277.7" y1="593.9" x2="277.7" y2="598.1" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="594.9" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="281.5" y1="593.3" x2="281.5" y2="597.2" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="595.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="285.3" y1="592.3" x2="285.3" y2="596.3" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="592.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="289.1" y1="590.1" x2="289.1" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="592.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="292.9" y1="587.2" x2="292.9" y2="593.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="589.5" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="296.6" y1="589.5" x2="296.6" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="590.0" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="300.4" y1="588.7" x2="300.4" y2="593.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="589.5" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="304.2" y1="587.6" x2="304.2" y2="590.9" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="589.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="308.0" y1="589.6" x2="308.0" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="590.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="311.8" y1="587.1" x2="311.8" y2="590.6" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="589.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="315.6" y1="589.0" x2="315.6" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="589.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="319.4" y1="589.3" x2="319.4" y2="592.7" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="590.2" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="323.1" y1="591.4" x2="323.1" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="591.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="326.9" y1="592.1" x2="326.9" y2="594.6" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="593.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="330.7" y1="592.9" x2="330.7" y2="596.9" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="593.8" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="334.5" y1="592.6" x2="334.5" y2="595.5" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="593.2" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="338.3" y1="590.1" x2="338.3" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="592.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="342.1" y1="591.5" x2="342.1" y2="593.3" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="592.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="345.9" y1="591.0" x2="345.9" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="592.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="349.6" y1="592.5" x2="349.6" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="592.9" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="353.4" y1="592.8" x2="353.4" y2="597.0" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="593.4" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="357.2" y1="581.2" x2="357.2" y2="594.8" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="588.4" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="361.0" y1="585.3" x2="361.0" y2="590.0" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="587.6" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="364.8" y1="585.4" x2="364.8" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="586.9" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="368.6" y1="589.7" x2="368.6" y2="592.1" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="589.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="372.4" y1="589.0" x2="372.4" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="589.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="376.2" y1="586.8" x2="376.2" y2="590.2" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="588.5" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="379.9" y1="588.4" x2="379.9" y2="591.1" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="588.4" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="383.7" y1="589.8" x2="383.7" y2="592.4" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="590.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="387.5" y1="589.4" x2="387.5" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="590.1" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="391.3" y1="585.3" x2="391.3" y2="591.7" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="588.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="395.1" y1="587.3" x2="395.1" y2="589.7" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="588.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="587.2" x2="398.9" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="588.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="402.7" y1="587.1" x2="402.7" y2="590.9" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="587.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="406.4" y1="586.5" x2="406.4" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="587.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="410.2" y1="585.9" x2="410.2" y2="588.2" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="587.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="414.0" y1="585.8" x2="414.0" y2="587.9" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="586.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="583.5" x2="417.8" y2="586.0" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="583.9" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="421.6" y1="581.8" x2="421.6" y2="584.9" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="582.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="425.4" y1="582.1" x2="425.4" y2="583.9" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="582.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="429.2" y1="578.0" x2="429.2" y2="584.4" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="578.4" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="432.9" y1="578.0" x2="432.9" y2="580.5" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="578.4" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="436.7" y1="577.2" x2="436.7" y2="580.6" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="578.0" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="440.5" y1="571.6" x2="440.5" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="573.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="444.3" y1="573.0" x2="444.3" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="574.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="448.1" y1="573.0" x2="448.1" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="573.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="451.9" y1="569.0" x2="451.9" y2="574.6" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="569.5" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="455.7" y1="563.4" x2="455.7" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="563.7" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="459.5" y1="563.1" x2="459.5" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="563.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="463.2" y1="564.4" x2="463.2" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="565.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="467.0" y1="564.0" x2="467.0" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="565.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="470.8" y1="564.5" x2="470.8" y2="571.2" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="565.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="474.6" y1="566.4" x2="474.6" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="569.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="478.4" y1="566.8" x2="478.4" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="569.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="482.2" y1="565.3" x2="482.2" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="568.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="486.0" y1="560.4" x2="486.0" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="561.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="489.7" y1="557.3" x2="489.7" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="560.8" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="493.5" y1="560.4" x2="493.5" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="561.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="497.3" y1="561.0" x2="497.3" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="561.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="501.1" y1="557.9" x2="501.1" y2="562.0" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="557.9" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="504.9" y1="554.2" x2="504.9" y2="558.7" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="556.1" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="508.7" y1="552.6" x2="508.7" y2="557.4" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="554.3" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="512.5" y1="553.0" x2="512.5" y2="555.1" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="553.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="516.2" y1="551.1" x2="516.2" y2="553.8" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="552.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="520.0" y1="550.8" x2="520.0" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="551.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="548.9" x2="523.8" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="550.3" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="527.6" y1="547.8" x2="527.6" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="547.8" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="531.4" y1="546.0" x2="531.4" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="546.3" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="535.2" y1="535.4" x2="535.2" y2="546.9" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="536.5" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="539.0" y1="537.5" x2="539.0" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="537.8" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="542.7" y1="531.9" x2="542.7" y2="542.5" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="533.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="546.5" y1="525.6" x2="546.5" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="525.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="550.3" y1="506.9" x2="550.3" y2="527.0" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="510.7" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="554.1" y1="491.0" x2="554.1" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="495.2" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="557.9" y1="488.1" x2="557.9" y2="502.9" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="492.4" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="561.7" y1="472.4" x2="561.7" y2="494.2" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="472.9" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="565.5" y1="462.6" x2="565.5" y2="477.2" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="471.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="569.3" y1="455.3" x2="569.3" y2="472.6" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="456.7" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="573.0" y1="456.0" x2="573.0" y2="476.8" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="457.7" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="576.8" y1="464.1" x2="576.8" y2="485.4" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="468.4" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="580.6" y1="461.3" x2="580.6" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="463.6" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="584.4" y1="436.8" x2="584.4" y2="462.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="440.8" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="588.2" y1="403.0" x2="588.2" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="409.9" width="2.35" height="28.8" fill="var(--up)"/>
<line x1="592.0" y1="398.3" x2="592.0" y2="424.1" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="407.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="595.8" y1="382.1" x2="595.8" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="387.4" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="599.5" y1="374.1" x2="599.5" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="379.2" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="603.3" y1="393.2" x2="603.3" y2="436.8" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="393.2" width="2.35" height="38.3" fill="var(--down)"/>
<line x1="607.1" y1="407.1" x2="607.1" y2="432.9" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="425.0" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="610.9" y1="418.9" x2="610.9" y2="438.6" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="425.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="614.7" y1="415.2" x2="614.7" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="428.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="618.5" y1="409.7" x2="618.5" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="420.4" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="622.3" y1="403.2" x2="622.3" y2="427.0" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="415.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="626.0" y1="417.5" x2="626.0" y2="460.8" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="417.8" width="2.35" height="36.0" fill="var(--down)"/>
<line x1="629.8" y1="441.3" x2="629.8" y2="473.1" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="451.7" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="633.6" y1="437.2" x2="633.6" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="464.2" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="637.4" y1="443.4" x2="637.4" y2="479.6" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="448.2" width="2.35" height="30.6" fill="var(--up)"/>
<line x1="641.2" y1="439.6" x2="641.2" y2="457.4" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="446.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="645.0" y1="428.6" x2="645.0" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="429.7" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="648.8" y1="424.2" x2="648.8" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="428.3" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="652.5" y1="431.6" x2="652.5" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="431.7" width="2.35" height="29.3" fill="var(--down)"/>
<line x1="656.3" y1="429.2" x2="656.3" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="430.3" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="660.1" y1="371.4" x2="660.1" y2="431.9" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="372.4" width="2.35" height="59.3" fill="var(--up)"/>
<line x1="663.9" y1="335.8" x2="663.9" y2="374.6" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="346.9" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="667.7" y1="290.8" x2="667.7" y2="354.4" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="293.3" width="2.35" height="53.2" fill="var(--up)"/>
<line x1="671.5" y1="279.2" x2="671.5" y2="355.2" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="289.5" width="2.35" height="37.7" fill="var(--down)"/>
<line x1="675.3" y1="290.5" x2="675.3" y2="327.1" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="312.1" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="679.1" y1="306.2" x2="679.1" y2="333.0" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="311.0" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="682.8" y1="318.7" x2="682.8" y2="343.4" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="327.5" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="686.6" y1="276.8" x2="686.6" y2="363.0" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="284.3" width="2.35" height="62.7" fill="var(--up)"/>
<line x1="690.4" y1="263.8" x2="690.4" y2="296.9" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="272.9" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="694.2" y1="214.9" x2="694.2" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="232.4" width="2.35" height="49.7" fill="var(--up)"/>
<line x1="698.0" y1="220.8" x2="698.0" y2="256.2" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="221.8" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="701.8" y1="224.8" x2="701.8" y2="254.1" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="233.2" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="705.6" y1="235.5" x2="705.6" y2="291.0" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="236.9" width="2.35" height="39.6" fill="var(--down)"/>
<line x1="709.3" y1="270.5" x2="709.3" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="277.0" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="713.1" y1="276.5" x2="713.1" y2="300.5" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="289.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="716.9" y1="230.5" x2="716.9" y2="302.5" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="231.2" width="2.35" height="68.2" fill="var(--up)"/>
<line x1="720.7" y1="213.6" x2="720.7" y2="256.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="219.9" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="724.5" y1="189.7" x2="724.5" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="209.2" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="728.3" y1="134.1" x2="728.3" y2="198.9" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="156.8" width="2.35" height="30.6" fill="var(--up)"/>
<line x1="732.1" y1="194.6" x2="732.1" y2="308.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="216.6" width="2.35" height="36.1" fill="var(--up)"/>
<line x1="735.8" y1="195.0" x2="735.8" y2="247.0" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="219.5" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="739.6" y1="204.5" x2="739.6" y2="234.6" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="214.0" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="743.4" y1="202.9" x2="743.4" y2="269.0" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="214.4" width="2.35" height="47.8" fill="var(--down)"/>
<line x1="747.2" y1="255.7" x2="747.2" y2="330.5" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="260.2" width="2.35" height="45.4" fill="var(--down)"/>
<line x1="751.0" y1="304.0" x2="751.0" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="305.6" width="2.35" height="50.1" fill="var(--down)"/>
<line x1="754.8" y1="320.7" x2="754.8" y2="381.6" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="329.4" width="2.35" height="37.5" fill="var(--up)"/>
<line x1="758.6" y1="306.7" x2="758.6" y2="335.1" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="313.6" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="762.4" y1="292.4" x2="762.4" y2="347.6" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="302.2" width="2.35" height="41.3" fill="var(--down)"/>
<line x1="766.1" y1="321.3" x2="766.1" y2="413.2" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="356.8" width="2.35" height="41.0" fill="var(--down)"/>
<line x1="769.9" y1="338.5" x2="769.9" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="362.5" width="2.35" height="49.4" fill="var(--up)"/>
<line x1="773.7" y1="340.5" x2="773.7" y2="365.6" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="348.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="777.5" y1="319.7" x2="777.5" y2="384.2" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="323.8" width="2.35" height="36.6" fill="var(--up)"/>
<line x1="781.3" y1="286.3" x2="781.3" y2="335.0" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="291.0" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="785.1" y1="271.4" x2="785.1" y2="305.4" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="298.0" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="788.9" y1="243.9" x2="788.9" y2="281.4" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="246.1" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="792.6" y1="238.8" x2="792.6" y2="264.3" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="242.1" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="796.4" y1="221.8" x2="796.4" y2="245.0" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="235.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="800.2" y1="189.8" x2="800.2" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="202.1" width="2.35" height="33.7" fill="var(--up)"/>
<line x1="804.0" y1="196.0" x2="804.0" y2="236.9" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="201.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="807.8" y1="171.3" x2="807.8" y2="197.9" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="172.3" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="811.6" y1="138.4" x2="811.6" y2="185.7" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="146.6" width="2.35" height="28.0" fill="var(--up)"/>
<line x1="815.4" y1="140.2" x2="815.4" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="140.2" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="819.1" y1="133.1" x2="819.1" y2="173.1" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="142.6" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="822.9" y1="139.8" x2="822.9" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="142.7" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="826.7" y1="115.3" x2="826.7" y2="181.1" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="150.2" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="830.5" y1="99.9" x2="830.5" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="112.9" width="2.35" height="38.7" fill="var(--up)"/>
<line x1="834.3" y1="90.1" x2="834.3" y2="159.6" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="106.4" width="2.35" height="21.8" fill="var(--down)"/>
<line x1="838.1" y1="99.6" x2="838.1" y2="147.2" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="124.4" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="841.9" y1="135.3" x2="841.9" y2="175.6" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="141.5" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="845.6" y1="130.2" x2="845.6" y2="168.2" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="155.6" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="849.4" y1="154.2" x2="849.4" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="164.8" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="853.2" y1="100.4" x2="853.2" y2="173.6" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="108.6" width="2.35" height="52.1" fill="var(--up)"/>
<line x1="857.0" y1="87.4" x2="857.0" y2="121.6" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="104.5" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="860.8" y1="82.4" x2="860.8" y2="144.1" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="105.2" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="864.6" y1="107.3" x2="864.6" y2="157.8" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="128.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="868.4" y1="101.7" x2="868.4" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="117.8" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="872.2" y1="89.4" x2="872.2" y2="133.6" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="130.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="875.9" y1="119.5" x2="875.9" y2="186.5" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="123.0" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="879.7" y1="124.2" x2="879.7" y2="176.4" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="124.2" width="2.35" height="39.8" fill="var(--down)"/>
<line x1="883.5" y1="146.2" x2="883.5" y2="194.4" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="157.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="887.3" y1="142.0" x2="887.3" y2="222.9" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="147.2" width="2.35" height="52.1" fill="var(--down)"/>
<line x1="891.1" y1="161.5" x2="891.1" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="197.4" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="894.9" y1="183.6" x2="894.9" y2="222.1" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="188.5" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="898.7" y1="190.6" x2="898.7" y2="220.6" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="195.9" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="902.4" y1="185.5" x2="902.4" y2="240.9" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="211.2" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="906.2" y1="198.1" x2="906.2" y2="240.7" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="203.8" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="910.0" y1="226.2" x2="910.0" y2="238.0" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="227.0" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="913.8" y1="213.3" x2="913.8" y2="237.6" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="223.8" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="917.6" y1="199.2" x2="917.6" y2="265.4" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="213.1" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="921.4" y1="178.9" x2="921.4" y2="229.6" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="220.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="925.2" y1="221.8" x2="925.2" y2="253.5" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="234.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="928.9" y1="216.9" x2="928.9" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="235.8" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="932.7" y1="237.4" x2="932.7" y2="293.0" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="243.5" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="936.5" y1="207.2" x2="936.5" y2="269.0" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="207.6" width="2.35" height="55.7" fill="var(--up)"/>
<line x1="940.3" y1="194.2" x2="940.3" y2="216.0" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="207.8" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="944.1" y1="189.9" x2="944.1" y2="229.9" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="201.4" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="947.9" y1="194.6" x2="947.9" y2="255.6" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="210.9" width="2.35" height="29.9" fill="var(--down)"/>
<line x1="951.7" y1="214.6" x2="951.7" y2="250.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="240.1" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="955.5" y1="203.7" x2="955.5" y2="276.7" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="234.8" width="2.35" height="38.8" fill="var(--down)"/>
<line x1="959.2" y1="236.8" x2="959.2" y2="272.4" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="249.1" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="963.0" y1="240.1" x2="963.0" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="244.9" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="966.8" y1="230.8" x2="966.8" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="251.0" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="970.6" y1="215.4" x2="970.6" y2="256.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="228.4" width="2.35" height="28.0" fill="var(--up)"/>
<line x1="974.4" y1="223.2" x2="974.4" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="226.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="978.2" y1="215.5" x2="978.2" y2="255.3" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="224.4" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="982.0" y1="215.6" x2="982.0" y2="271.1" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="243.3" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="985.7" y1="256.1" x2="985.7" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="268.5" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="989.5" y1="243.7" x2="989.5" y2="308.2" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="247.0" width="2.35" height="44.7" fill="var(--up)"/>
<line x1="993.3" y1="218.2" x2="993.3" y2="245.4" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="236.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="997.1" y1="235.3" x2="997.1" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="245.1" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="1000.9" y1="262.0" x2="1000.9" y2="294.6" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="267.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1004.7" y1="210.6" x2="1004.7" y2="262.6" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="227.6" width="2.35" height="28.3" fill="var(--up)"/>
<line x1="1008.5" y1="208.0" x2="1008.5" y2="239.6" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="228.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1012.2" y1="222.9" x2="1012.2" y2="267.2" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="227.8" width="2.35" height="32.8" fill="var(--down)"/>
<line x1="1016.0" y1="234.3" x2="1016.0" y2="259.9" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="240.3" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="1019.8" y1="216.1" x2="1019.8" y2="268.1" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="243.5" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="1023.6" y1="212.1" x2="1023.6" y2="248.8" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="228.6" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="1027.4" y1="221.4" x2="1027.4" y2="283.6" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="223.1" width="2.35" height="44.8" fill="var(--down)"/>
<line x1="1031.2" y1="245.2" x2="1031.2" y2="302.8" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="266.5" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="1035.0" y1="262.8" x2="1035.0" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="268.1" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="1038.7" y1="263.6" x2="1038.7" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="264.9" width="2.35" height="34.1" fill="var(--down)"/>
<line x1="1042.5" y1="278.7" x2="1042.5" y2="303.4" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="296.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="1046.3" y1="264.7" x2="1046.3" y2="302.4" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="265.1" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="1050.1" y1="264.7" x2="1050.1" y2="281.0" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="265.1" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="60" y1="211.4" x2="1052" y2="211.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="214.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$170 R1</text>
<text x="1058" y="226.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="184.4" x2="1052" y2="184.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="187.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$180 R2</text>
<text x="1058" y="199.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="86.2" x2="1052" y2="86.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="89.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$218 R3</text>
<text x="1058" y="101.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="309.5" x2="1052" y2="309.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="303.5" font-size="11.5" fill="var(--support)" font-weight="600">$132 S1</text>
<text x="1058" y="315.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="592.9" x2="1052" y2="592.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="586.9" font-size="11.5" fill="var(--support)" font-weight="600">$23 S2</text>
<text x="1058" y="598.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="597.8" x2="1052" y2="597.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="591.8" font-size="11.5" fill="var(--support)" font-weight="600">$21 S3</text>
<text x="1058" y="603.8" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="265.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="257.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $149 (2026-09-04)</text>
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
| R3 | $218 | 2 | 2025-08-04·2025-09-22 — **5년 최고($219.82) 구간**. 일봉 차트의 R3와 같은 자리다 |
| R2 | $180 | 2 | 2026-01-12·2026-02-23 |
| R1 | $170 | 2 | 2024-11-18·2026-06-22 — **2024년 11월에 처음 닿은 자리를 2026년 6월에 다시 만났다.** 1년 반 사이 위로 갔다가 되돌아온 셈 |
| **현재가** | **$149.30** (2026-09-04 종가) | — | R1과 S1 사이 |
| S1 | $132 | 2 | 2024-12-16·2026-05-18 — **5년 창에서 현재가 아래에 있는 유일한 실질 지지대**이며, 일봉 차트의 52주 최저($132.66)와 같은 자리다 |
| S2 | $23 | 2 | 2022-05-09·2023-05-01 — **현재가의 6분의 1 수준**. 아래 3절 참고 |
| S3 | $21 | 5 | 2022-02-21·2022-07-04·2022-10-10·2023-01-16·2023-02-27 — 터치 5회로 5년 창에서 가장 두꺼운 클러스터이지만, **현재가의 7분의 1이라 지지선으로서의 의미가 없다** |
| 참고선 | $16.51 | — | **5년 최저**(2021년 하반기). 지금과 완전히 다른 회사·시장 국면의 가격이다 |

---

## 3. 관측된 특이 구간 — 2023~2024년의 재평가로 가격대가 통째로 이동했다

**이 차트에서 S2($23)·S3($21)를 지지선으로 읽으면 안 된다.** 5년 창의 앞쪽 2년(2021~2023)과 뒤쪽 2년(2024~2026)은 **가격대가 한 자리 수 배수로 다르다.**

- 2021년 9월~2023년 상반기 이 종목은 **$16~$25 구간**에서 움직였다. 당시 시장이 이 회사를 매긴 값은 [밸류에이션 / 적정주가](./06_valuation.md) 2절이 정리한 그대로다 — FY2023 말 EV/Adjusted EBITDA **6.73배**로 3개년 최저였고, 같은 문서 기준 적정주가 대비 **−55.0%** 저평가였다. **"석탄을 태우는 사양산업"으로 값이 매겨지던 국면**이다.
- 2024년부터 두 가지가 겹치며 가격대가 재설정됐다 — ① **2024년 3월 Energy Harbor 인수**로 원전 4,048 MW를 확보했고([역사 / 주요 이벤트](./02_history.md)), ② AI 데이터센터 전력 수요가 산업 서사로 자리 잡았다. 주가는 2023년 말 $38.52 → 2024년 말 $137.87로 **1년 만에 3.6배**가 됐다.
- 그 결과 **2024년 이후의 클러스터(R1 $170 · S1 $132)만 현재 가격 구조와 연속성을 갖는다.** S2·S3는 다른 회사에 매겨진 가격이라고 보는 편이 정확하며, 표에는 스크립트 산출물 그대로 남겨두되 해석에서 제외한다.
- **주봉 구조가 말하는 현재 위치**: 현재가 $149.30은 R1($170)과 S1($132) 사이 중간쯤이다. 이 두 선의 폭이 약 29%로 넓고 그 안에 클러스터가 없어, **5년 구조만으로는 방향을 읽을 수 없는 구간**이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-06~2026-09-04. 수집 시점: 2026-09-07. **원주가(과거 분할은 소급 반영, 배당은 미반영)**
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py VST --name "Vistra" --interval 1wk --close-on 2026-09-04 --emit all` (재현용, 옵션 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 가격대 재설정이 이 표의 절반을 무력화한다.** S2($23)·S3($21)는 알고리즘상 유효한 클러스터이지만 현재가의 6~7분의 1이라 지지선으로 쓸 수 없다 — **±2.5% 상대 허용오차를 쓰는 클러스터링은 가격대가 10배 바뀐 구간을 자동으로 걸러내지 못한다.**
    - **기간 내 배당이 20회 있었으나 원주가라 반영되지 않았다.**
    - 해당 기간에 주식분할·대규모 유상증자는 없었다. 다만 같은 기간 **자사주매입으로 발행주식수가 약 30% 줄었다** — 주당 가격은 그만큼 시가총액 변화보다 크게 오른 것이며, 이 차트는 주당 가격만 보여준다.

---

*작성일: 2026-09-11*
