# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트를 볼 때 특히 주의할 점
**이 5년 구간에는 2022년의 −64% 하락이 들어 있다.** 5년 최저 $88.09(2022년)와 5년 최고 $796.25(2025년)가 9배 차이라 y축 하단부가 압축돼 보이고, 그 시기의 스윙대(S3 $311)는 현재가와 −52% 떨어져 있다. **분할·병합은 없다** — Meta는 2012년 상장 이후 주식분할을 한 적이 없어 전 구간이 같은 기준의 원주가다.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 2026-09-11 종가 **$648.03**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치한다**. [기술적 분석 — 일봉·1년](./09_technical_daily.md)의 종가와도 같다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-11)

<div class="meta-chart">
<style>
.meta-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .meta-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .meta-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.meta-chart svg { width:100%; height:auto; display:block; }
.meta-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.meta-chart .title { fill: var(--ink); font-weight:600; }
.meta-chart .grid { stroke: var(--grid); stroke-width:1; }
.meta-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Meta Platforms(META) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Meta Platforms (META) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $648.03 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="596.0" x2="1052" y2="596.0" class="grid"/>
<text x="52" y="600.0" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="521.0" x2="1052" y2="521.0" class="grid"/>
<text x="52" y="525.0" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="446.0" x2="1052" y2="446.0" class="grid"/>
<text x="52" y="450.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="371.0" x2="1052" y2="371.0" class="grid"/>
<text x="52" y="375.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="296.0" x2="1052" y2="296.0" class="grid"/>
<text x="52" y="300.0" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="221.0" x2="1052" y2="221.0" class="grid"/>
<text x="52" y="225.0" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="146.0" x2="1052" y2="146.0" class="grid"/>
<text x="52" y="150.0" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="71.0" x2="1052" y2="71.0" class="grid"/>
<text x="52" y="75.0" font-size="11" text-anchor="end" fill="var(--muted)">800</text>
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
<line x1="61.9" y1="384.7" x2="61.9" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="384.7" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="65.7" y1="400.2" x2="65.7" y2="415.5" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="401.5" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="69.5" y1="404.6" x2="69.5" y2="417.4" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="408.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="73.3" y1="416.9" x2="73.3" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="419.4" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="77.0" y1="423.1" x2="77.0" y2="433.0" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="425.3" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="80.8" y1="413.0" x2="80.8" y2="430.2" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="424.3" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="84.6" y1="423.3" x2="84.6" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="428.3" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="88.4" y1="410.9" x2="88.4" y2="428.6" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="415.2" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="92.2" y1="412.4" x2="92.2" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="412.7" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="96.0" y1="405.8" x2="96.0" y2="419.5" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="412.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="99.8" y1="405.6" x2="99.8" y2="422.1" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="409.2" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="103.5" y1="415.5" x2="103.5" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="418.3" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="107.3" y1="418.9" x2="107.3" y2="441.2" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="423.7" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="111.1" y1="412.7" x2="111.1" y2="428.0" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="420.7" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="114.9" y1="418.5" x2="114.9" y2="429.1" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="419.6" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="118.7" y1="406.5" x2="118.7" y2="418.8" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="416.9" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="122.5" y1="413.7" x2="122.5" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="417.3" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="126.3" y1="418.7" x2="126.3" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="422.1" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="130.0" y1="425.1" x2="130.0" y2="443.7" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="428.5" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="133.8" y1="438.9" x2="133.8" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="444.7" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="137.6" y1="425.0" x2="137.6" y2="498.4" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="445.5" width="2.35" height="47.7" fill="var(--down)"/>
<line x1="141.4" y1="492.3" x2="141.4" y2="508.9" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="492.7" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="145.2" y1="505.1" x2="145.2" y2="517.1" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="506.5" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="149.0" y1="512.5" x2="149.0" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="513.1" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="152.8" y1="511.1" x2="152.8" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="515.2" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="156.5" y1="520.3" x2="156.5" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="520.4" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="160.3" y1="508.4" x2="160.3" y2="531.6" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="508.6" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="164.1" y1="501.9" x2="164.1" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="504.6" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="167.9" y1="497.6" x2="167.9" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="502.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="171.7" y1="493.4" x2="171.7" y2="507.1" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="501.5" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="175.5" y1="504.5" x2="175.5" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="507.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="179.3" y1="507.2" x2="179.3" y2="533.5" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="513.5" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="183.1" y1="511.6" x2="183.1" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="520.6" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="186.8" y1="502.8" x2="186.8" y2="520.3" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="518.2" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="190.6" y1="518.8" x2="190.6" y2="532.4" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="521.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="194.4" y1="516.9" x2="194.4" y2="530.1" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="523.2" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="198.2" y1="523.3" x2="198.2" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="524.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="202.0" y1="520.3" x2="202.0" y2="532.2" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="524.8" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="205.8" y1="519.5" x2="205.8" y2="539.7" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="525.5" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="209.6" y1="541.6" x2="209.6" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="543.1" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="213.3" y1="543.3" x2="213.3" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="543.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="217.1" y1="542.2" x2="217.1" y2="554.8" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="542.5" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="220.9" y1="541.5" x2="220.9" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="542.8" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="224.7" y1="545.4" x2="224.7" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="545.7" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="228.5" y1="533.1" x2="228.5" y2="546.8" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="544.0" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="232.3" y1="542.8" x2="232.3" y2="554.9" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="544.2" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="236.1" y1="541.9" x2="236.1" y2="554.6" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="545.7" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="239.8" y1="533.7" x2="239.8" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="535.6" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="243.6" y1="534.9" x2="243.6" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="536.8" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="247.4" y1="542.8" x2="247.4" y2="551.2" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="546.9" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="251.2" y1="545.1" x2="251.2" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="550.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="255.0" y1="543.8" x2="255.0" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="544.1" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="258.8" y1="542.5" x2="258.8" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="545.5" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="262.6" y1="558.8" x2="262.6" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="562.1" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="266.4" y1="564.3" x2="266.4" y2="570.4" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="565.9" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="270.1" y1="564.2" x2="270.1" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="568.1" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="273.9" y1="568.9" x2="273.9" y2="579.1" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="570.8" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="277.7" y1="567.6" x2="277.7" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="573.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="281.5" y1="567.2" x2="281.5" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="575.6" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="285.3" y1="596.5" x2="285.3" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="597.3" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="289.1" y1="584.8" x2="289.1" y2="601.2" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="586.2" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="292.9" y1="581.9" x2="292.9" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="587.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="296.6" y1="586.5" x2="296.6" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="587.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="300.4" y1="578.0" x2="300.4" y2="589.7" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="578.4" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="304.2" y1="577.5" x2="304.2" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="579.7" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="308.0" y1="577.9" x2="308.0" y2="586.1" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="581.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="311.8" y1="580.7" x2="311.8" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="582.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="315.6" y1="580.2" x2="315.6" y2="584.4" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="580.7" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="319.4" y1="573.3" x2="319.4" y2="579.3" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="573.5" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="323.1" y1="567.7" x2="323.1" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="568.3" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="326.9" y1="566.0" x2="326.9" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="566.5" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="330.7" y1="556.1" x2="330.7" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="557.2" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="334.5" y1="523.1" x2="334.5" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="531.1" width="2.35" height="27.8" fill="var(--up)"/>
<line x1="338.3" y1="525.7" x2="338.3" y2="541.0" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="531.1" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="342.1" y1="534.9" x2="342.1" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="537.3" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="345.9" y1="537.4" x2="345.9" y2="545.3" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="540.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="349.6" y1="531.0" x2="349.6" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="532.1" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="353.4" y1="528.2" x2="353.4" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="530.0" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="357.2" y1="516.7" x2="357.2" y2="539.9" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="524.3" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="361.0" y1="515.1" x2="361.0" y2="525.8" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="516.5" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="364.8" y1="511.9" x2="364.8" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="512.0" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="368.6" y1="508.3" x2="368.6" y2="514.9" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="508.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="372.4" y1="504.4" x2="372.4" y2="513.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="504.9" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="376.2" y1="505.3" x2="376.2" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="506.2" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="379.9" y1="489.7" x2="379.9" y2="515.7" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="490.8" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="383.7" y1="487.3" x2="383.7" y2="498.6" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="492.0" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="387.5" y1="492.3" x2="387.5" y2="498.3" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="495.6" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="391.3" y1="484.5" x2="391.3" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="486.8" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="395.1" y1="474.3" x2="395.1" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="474.5" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="398.9" y1="464.5" x2="398.9" y2="477.2" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="466.5" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="402.7" y1="463.6" x2="402.7" y2="476.8" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="468.3" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="406.4" y1="455.1" x2="406.4" y2="472.0" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="460.2" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="410.2" y1="453.7" x2="410.2" y2="463.8" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="454.5" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="414.0" y1="453.7" x2="414.0" y2="462.8" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="454.5" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="417.8" y1="447.4" x2="417.8" y2="457.4" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="453.1" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="421.6" y1="433.8" x2="421.6" y2="455.7" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="439.3" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="425.4" y1="432.0" x2="425.4" y2="452.6" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="440.3" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="429.2" y1="426.3" x2="429.2" y2="454.8" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="426.9" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="432.9" y1="426.8" x2="432.9" y2="438.6" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="428.2" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="436.7" y1="432.6" x2="436.7" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="436.1" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="440.5" y1="440.6" x2="440.5" y2="465.2" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="445.3" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="444.3" y1="446.4" x2="444.3" y2="464.0" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="456.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="448.1" y1="444.7" x2="448.1" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="448.7" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="451.9" y1="440.7" x2="451.9" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="447.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="455.7" y1="436.3" x2="455.7" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="444.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="459.5" y1="440.0" x2="459.5" y2="451.0" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="446.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="463.2" y1="438.0" x2="463.2" y2="455.9" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="445.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="467.0" y1="433.8" x2="467.0" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="434.4" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="470.8" y1="423.1" x2="470.8" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="435.0" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="474.6" y1="426.5" x2="474.6" y2="441.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="432.0" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="478.4" y1="432.2" x2="478.4" y2="461.5" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="438.9" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="482.2" y1="431.9" x2="482.2" y2="448.4" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="435.0" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="486.0" y1="424.2" x2="486.0" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="424.4" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="489.7" y1="417.2" x2="489.7" y2="426.7" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="419.7" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="493.5" y1="413.8" x2="493.5" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="417.3" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="497.3" y1="416.1" x2="497.3" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="418.9" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="501.1" y1="421.1" x2="501.1" y2="435.8" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="421.4" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="504.9" y1="417.0" x2="504.9" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="419.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="508.7" y1="403.1" x2="508.7" y2="418.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="406.0" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="512.5" y1="399.6" x2="512.5" y2="407.1" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="404.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="516.2" y1="405.9" x2="516.2" y2="416.0" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="407.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="520.0" y1="388.2" x2="520.0" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="390.1" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="523.8" y1="382.7" x2="523.8" y2="402.0" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="383.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="527.6" y1="373.4" x2="527.6" y2="385.1" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="375.4" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="531.4" y1="306.5" x2="531.4" y2="380.7" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="314.8" width="2.35" height="60.0" fill="var(--up)"/>
<line x1="535.2" y1="315.8" x2="535.2" y2="331.2" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="318.6" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="539.0" y1="304.5" x2="539.0" y2="329.7" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="316.0" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="542.7" y1="300.2" x2="542.7" y2="324.7" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="308.0" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="546.5" y1="292.8" x2="546.5" y2="311.1" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="294.3" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="550.3" y1="278.3" x2="550.3" y2="305.1" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="291.5" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="554.1" y1="294.3" x2="554.1" y2="314.0" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="298.2" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="557.9" y1="284.7" x2="557.9" y2="310.0" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="288.8" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="561.7" y1="288.5" x2="561.7" y2="307.1" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="291.7" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="565.5" y1="273.0" x2="565.5" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="275.5" width="2.35" height="30.1" fill="var(--up)"/>
<line x1="569.3" y1="272.4" x2="569.3" y2="291.7" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="274.0" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="573.0" y1="282.1" x2="573.0" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="283.5" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="576.8" y1="288.5" x2="576.8" y2="360.1" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="303.7" width="2.35" height="34.8" fill="var(--down)"/>
<line x1="580.6" y1="330.4" x2="580.6" y2="350.7" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="332.0" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="584.4" y1="312.9" x2="584.4" y2="331.0" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="313.8" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="588.2" y1="309.1" x2="588.2" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="316.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="592.0" y1="311.1" x2="592.0" y2="324.8" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="312.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="595.8" y1="310.4" x2="595.8" y2="330.2" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="313.6" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="599.5" y1="293.9" x2="599.5" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="301.3" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="603.3" y1="285.5" x2="603.3" y2="300.9" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="292.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="607.1" y1="287.9" x2="607.1" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="294.7" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="610.9" y1="278.8" x2="610.9" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="292.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="614.7" y1="265.3" x2="614.7" y2="301.1" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="266.1" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="618.5" y1="263.9" x2="618.5" y2="300.3" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="264.2" width="2.35" height="32.6" fill="var(--down)"/>
<line x1="622.3" y1="291.0" x2="622.3" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="297.0" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="626.0" y1="299.6" x2="626.0" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="306.1" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="629.8" y1="275.6" x2="629.8" y2="328.5" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="304.9" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="633.6" y1="282.2" x2="633.6" y2="332.9" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="282.7" width="2.35" height="49.8" fill="var(--up)"/>
<line x1="637.4" y1="266.2" x2="637.4" y2="289.2" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="275.4" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="641.2" y1="262.8" x2="641.2" y2="278.9" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="275.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="645.0" y1="275.0" x2="645.0" y2="286.7" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="275.3" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="648.8" y1="276.9" x2="648.8" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="281.3" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="652.5" y1="275.3" x2="652.5" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="277.5" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="656.3" y1="247.6" x2="656.3" y2="282.9" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="250.0" width="2.35" height="27.6" fill="var(--up)"/>
<line x1="660.1" y1="237.9" x2="660.1" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="243.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="663.9" y1="223.4" x2="663.9" y2="247.4" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="224.0" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="667.7" y1="218.8" x2="667.7" y2="234.8" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="222.3" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="671.5" y1="220.9" x2="671.5" y2="240.5" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="225.3" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="675.3" y1="232.2" x2="675.3" y2="249.9" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="239.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="679.1" y1="220.1" x2="679.1" y2="249.1" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="234.5" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="682.8" y1="224.9" x2="682.8" y2="254.6" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="229.0" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="686.6" y1="221.3" x2="686.6" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="231.2" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="690.4" y1="243.5" x2="690.4" y2="259.2" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="251.6" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="694.2" y1="237.2" x2="694.2" y2="253.7" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="240.3" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="698.0" y1="198.7" x2="698.0" y2="239.3" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="203.2" width="2.35" height="34.7" fill="var(--up)"/>
<line x1="701.8" y1="192.2" x2="701.8" y2="216.4" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="203.1" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="705.6" y1="196.7" x2="705.6" y2="236.0" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="198.5" width="2.35" height="33.5" fill="var(--down)"/>
<line x1="709.3" y1="215.0" x2="709.3" y2="231.3" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="221.1" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="713.1" y1="213.9" x2="713.1" y2="233.1" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="217.5" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="716.9" y1="196.9" x2="716.9" y2="223.0" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="209.1" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="720.7" y1="202.3" x2="720.7" y2="229.6" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="211.4" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="724.5" y1="182.0" x2="724.5" y2="214.2" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="185.4" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="728.3" y1="137.9" x2="728.3" y2="202.2" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="154.1" width="2.35" height="46.9" fill="var(--up)"/>
<line x1="732.1" y1="127.2" x2="732.1" y2="164.6" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="135.1" width="2.35" height="29.0" fill="var(--up)"/>
<line x1="735.8" y1="115.3" x2="735.8" y2="138.5" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="118.5" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="739.6" y1="118.2" x2="739.6" y2="159.2" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="119.0" width="2.35" height="39.3" fill="var(--down)"/>
<line x1="743.4" y1="154.5" x2="743.4" y2="189.6" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="156.3" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="747.2" y1="160.1" x2="747.2" y2="220.5" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="165.7" width="2.35" height="36.0" fill="var(--down)"/>
<line x1="751.0" y1="196.0" x2="751.0" y2="231.1" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="214.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="754.8" y1="211.2" x2="754.8" y2="240.0" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="215.4" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="758.6" y1="195.6" x2="758.6" y2="240.6" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="209.8" width="2.35" height="28.7" fill="var(--down)"/>
<line x1="762.4" y1="226.5" x2="762.4" y2="300.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="248.4" width="2.35" height="44.1" fill="var(--down)"/>
<line x1="766.1" y1="230.1" x2="766.1" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="263.3" width="2.35" height="43.9" fill="var(--up)"/>
<line x1="769.9" y1="252.7" x2="769.9" y2="299.3" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="253.9" width="2.35" height="41.0" fill="var(--down)"/>
<line x1="773.7" y1="258.6" x2="773.7" y2="311.2" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="260.5" width="2.35" height="42.0" fill="var(--up)"/>
<line x1="777.5" y1="217.7" x2="777.5" y2="273.9" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="223.2" width="2.35" height="31.0" fill="var(--up)"/>
<line x1="781.3" y1="212.5" x2="781.3" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="226.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="785.1" y1="174.0" x2="785.1" y2="205.2" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="190.7" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="788.9" y1="186.0" x2="788.9" y2="204.0" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="199.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="792.6" y1="181.0" x2="792.6" y2="196.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="185.4" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="796.4" y1="143.9" x2="796.4" y2="187.8" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="147.7" width="2.35" height="40.0" fill="var(--up)"/>
<line x1="800.2" y1="139.3" x2="800.2" y2="160.2" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="147.2" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="804.0" y1="140.6" x2="804.0" y2="162.0" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="146.5" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="807.8" y1="119.4" x2="807.8" y2="161.9" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="120.8" width="2.35" height="37.5" fill="var(--up)"/>
<line x1="811.6" y1="110.1" x2="811.6" y2="136.4" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="112.6" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="815.4" y1="117.9" x2="815.4" y2="138.7" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="132.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="819.1" y1="125.0" x2="819.1" y2="152.3" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="132.8" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="822.9" y1="128.3" x2="822.9" y2="144.9" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="136.5" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="826.7" y1="82.4" x2="826.7" y2="152.6" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="108.5" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="830.5" y1="83.7" x2="830.5" y2="102.2" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="94.0" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="834.3" y1="73.8" x2="834.3" y2="97.5" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="82.1" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="838.1" y1="89.1" x2="838.1" y2="122.8" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="89.7" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="841.9" y1="101.8" x2="841.9" y2="119.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="104.9" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="845.6" y1="100.1" x2="845.6" y2="129.7" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="106.7" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="849.4" y1="96.1" x2="849.4" y2="113.2" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="104.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="853.2" y1="77.9" x2="853.2" y2="107.0" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="87.2" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="857.0" y1="81.7" x2="857.0" y2="118.0" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="84.6" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="860.8" y1="107.9" x2="860.8" y2="138.4" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="109.5" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="864.6" y1="119.5" x2="864.6" y2="153.1" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="142.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="868.4" y1="126.9" x2="868.4" y2="146.5" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="133.3" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="872.2" y1="114.2" x2="872.2" y2="130.9" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="117.2" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="875.9" y1="101.6" x2="875.9" y2="186.8" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="108.7" width="2.35" height="76.0" fill="var(--down)"/>
<line x1="879.7" y1="176.5" x2="879.7" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="179.0" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="883.5" y1="194.8" x2="883.5" y2="224.6" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="197.7" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="887.3" y1="212.2" x2="887.3" y2="235.1" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="214.2" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="891.1" y1="185.0" x2="891.1" y2="222.8" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="185.0" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="894.9" y1="163.9" x2="894.9" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="165.9" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="898.7" y1="137.8" x2="898.7" y2="192.0" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="169.0" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="902.4" y1="167.8" x2="902.4" y2="192.0" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="176.9" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="906.2" y1="165.8" x2="906.2" y2="178.5" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="173.5" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="910.0" y1="166.8" x2="910.0" y2="188.4" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="177.5" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="913.8" y1="171.9" x2="913.8" y2="194.2" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="181.2" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="917.6" y1="180.5" x2="917.6" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="181.6" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="921.4" y1="171.1" x2="921.4" y2="221.0" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="176.9" width="2.35" height="38.2" fill="var(--up)"/>
<line x1="925.2" y1="113.0" x2="925.2" y2="175.0" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="133.6" width="2.35" height="38.5" fill="var(--up)"/>
<line x1="928.9" y1="130.0" x2="928.9" y2="186.1" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="135.1" width="2.35" height="39.9" fill="var(--down)"/>
<line x1="932.7" y1="158.5" x2="932.7" y2="195.1" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="173.6" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="936.5" y1="173.5" x2="936.5" y2="199.9" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="179.3" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="940.3" y1="175.2" x2="940.3" y2="199.3" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="181.6" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="944.1" y1="166.4" x2="944.1" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="187.4" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="947.9" y1="175.8" x2="947.9" y2="213.8" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="194.9" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="951.7" y1="193.6" x2="951.7" y2="230.6" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="197.0" width="2.35" height="28.8" fill="var(--down)"/>
<line x1="955.5" y1="214.5" x2="955.5" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="216.7" width="2.35" height="60.1" fill="var(--down)"/>
<line x1="959.2" y1="226.6" x2="959.2" y2="274.6" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="240.2" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="963.0" y1="192.1" x2="963.0" y2="247.4" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="198.6" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="966.8" y1="152.4" x2="966.8" y2="202.7" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="154.6" width="2.35" height="44.3" fill="var(--up)"/>
<line x1="970.6" y1="158.5" x2="970.6" y2="181.2" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="160.0" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="974.4" y1="159.1" x2="974.4" y2="221.0" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="167.8" width="2.35" height="46.7" fill="var(--down)"/>
<line x1="978.2" y1="202.3" x2="978.2" y2="222.4" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="213.8" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="982.0" y1="203.2" x2="982.0" y2="226.6" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="210.3" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="985.7" y1="209.3" x2="985.7" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="213.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="989.5" y1="188.8" x2="989.5" y2="217.0" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="196.6" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="993.3" y1="189.2" x2="993.3" y2="233.8" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="198.2" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="997.1" y1="222.8" x2="997.1" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="227.0" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="1000.9" y1="216.6" x2="1000.9" y2="248.7" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="236.1" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="1004.7" y1="239.1" x2="1004.7" y2="265.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="242.0" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="1008.5" y1="199.8" x2="1008.5" y2="257.4" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="233.8" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="1012.2" y1="162.6" x2="1012.2" y2="238.2" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="169.1" width="2.35" height="55.8" fill="var(--up)"/>
<line x1="1016.0" y1="156.4" x2="1016.0" y2="201.5" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="175.0" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="1019.8" y1="179.1" x2="1019.8" y2="225.2" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="186.0" width="2.35" height="38.6" fill="var(--down)"/>
<line x1="1023.6" y1="212.6" x2="1023.6" y2="277.6" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="215.6" width="2.35" height="37.9" fill="var(--down)"/>
<line x1="1027.4" y1="220.2" x2="1027.4" y2="251.5" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="226.9" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="1031.2" y1="211.7" x2="1031.2" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="221.7" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="1035.0" y1="228.3" x2="1035.0" y2="268.0" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="228.7" width="2.35" height="29.9" fill="var(--down)"/>
<line x1="1038.7" y1="226.0" x2="1038.7" y2="261.3" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="237.5" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="1042.5" y1="206.4" x2="1042.5" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="208.4" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="1046.3" y1="172.8" x2="1046.3" y2="213.7" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="185.0" width="2.35" height="23.9" fill="var(--up)"/>
<line x1="1050.1" y1="172.8" x2="1050.1" y2="186.3" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="181.2" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="60" y1="154.4" x2="1052" y2="154.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="157.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$689 R1</text>
<text x="1058" y="169.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="110.0" x2="1052" y2="110.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="113.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$748 R2</text>
<text x="1058" y="125.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="75.9" x2="1052" y2="75.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="79.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$794 R3</text>
<text x="1058" y="91.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="262.5" x2="1052" y2="262.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="256.5" font-size="11.5" fill="var(--support)" font-weight="600">$545 S1</text>
<text x="1058" y="268.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="279.2" x2="1052" y2="279.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="273.2" font-size="11.5" fill="var(--support)" font-weight="600">$522 S2</text>
<text x="1058" y="285.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="437.8" x2="1052" y2="437.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="431.8" font-size="11.5" fill="var(--support)" font-weight="600">$311 S3</text>
<text x="1058" y="443.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="185.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="177.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $648 (2026-09-11)</text>
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
| R3 | $794 | 2 | 2025-08-11·2025-09-15 — 5년 최고가($796.25)와 겹치는 최상단 고점대 |
| R2 | $748 | 3 | 2025-02-10·2025-10-27·2026-01-26 — 1년 이상에 걸쳐 세 번 막힌 자리 |
| R1 | $689 | 2 | 2026-04-13·2026-07-13 — **2026년에 형성된 가장 가까운 저항.** 마지막 터치가 2분기 실적 발표(07-29) 직전이다 |
| **현재가** | **$648.03** (2026-09-11 종가) | — | R1과 S1 사이. R1까지 +6.3%, S1까지 −15.9% |
| S1 | $545 | 2 | 2024-11-18·2026-06-22 — 1년 7개월 간격으로 두 번 확인된 지지 |
| S2 | $522 | 2 | 2026-03-23·2026-07-27 — 최근 1년 최저가($520.26)와 겹친다 |
| S3 | $311 | 2 | 2021-10-25·2023-12-04 — 2022년 하락 전후 구간. 현재가와 −52%로 근시일 참고 대상이 아니다 |

> **동종사 [Alphabet](../alphabet/10_technical_weekly.md)의 같은 표와 구조가 정반대다.** Alphabet은 5년 기간 내 상단 저항이 0개(신고가 구간)인데 Meta는 현재가 위에 R1·R2·R3 세 개가 있다 — Meta 주가가 5년 최고($796.25)보다 19% 아래에 있기 때문이다. 즉 **Alphabet은 위쪽이 비어 있고 Meta는 위쪽이 막혀 있다.**
>
> 현재가와 S1 사이 15.9% 구간이 비어 있어, 근시일 지지는 이 문서가 아니라 [기술적 분석 — 일봉·1년](./09_technical_daily.md)의 S1($633)·S2($589)를 봐야 한다.

---

## 3. 관측된 특이 구간 — 2022년 하락과 2025~2026년 고점 형성

- **2022년 −64% 하락**: 5년 최저 $88.09까지 밀렸다. Apple ATT 도입으로 광고 타게팅이 제한돼 매출이 상장 후 첫 감소를 기록하고, 메타버스 전환에 시장이 거부 반응을 보인 국면이다([역사 / 주요 이벤트](./02_history.md) 2021~2023 항목). 위 S3($311)의 두 터치는 이 하락의 시작(2021-10)과 회복 국면(2023-12)에 걸쳐 있어, **같은 클러스터지만 성격이 다른 두 시점**이다.
- **2025년 고점권 형성**: R3($794)·R2($748)가 2025년에 집중돼 있다. 2025년 회계연도 말 종가는 $660.09였다.
- **2026년 상단 하락과 박스 형성**: R1($689)이 2026-04·07에 두 번 막혔고, 그 사이 S2($522)가 2026-03·07에 두 번 확인됐다. 즉 2026년 주가는 $522~689 박스 안에 있었고, **현재가 $648.03은 그 박스 상단부**다. 2026-07-29 실적 발표(영업이익 −8% YoY, 총비용 가이던스 상향)와 2026-08-26 아동 안전 합의가 이 박스 후반부의 사건이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py META --name "Meta Platforms" --interval 1wk --close-on 2026-09-11 --emit all` (기본 옵션, `--force-level`·`--event` 미사용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **6개 레벨 중 5개가 터치 2회**로 표본이 얕다. R2(3회)만 상대적으로 두껍다.
    - **S3($311)은 레짐이 다른 구간의 레벨이다** — 3. 관측된 특이 구간에서 설명한 대로 2022년 하락 전후에 형성됐고 현재가와 −52% 떨어져 있다. 근시일 지지로 해석하면 안 된다.
    - 기간 내 주식분할·병합·유상증자가 없어 가격 연속성이 유지된다. 다만 기간 내 배당이 10회 있었고 원주가를 썼으므로 배당 재투자 수익은 반영되지 않았다.

---

*작성일: 2026-09-12*
