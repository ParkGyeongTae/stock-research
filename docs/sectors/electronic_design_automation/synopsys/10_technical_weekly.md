# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL·10-Q)와는 계보가 다르다.
- **대조 결과**: **2026-09-04 종가 $393.84는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)·[일봉 문서](./09_technical_daily.md)에 인용된 값과 모두 일치**한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-06 ~ 2026-09-04)

<style>
.snps-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.snps-chart svg { width:100%; height:auto; display:block; }
.snps-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.snps-chart .title { fill: var(--ink); font-weight:600; }
.snps-chart .grid { stroke: var(--grid); stroke-width:1; }
.snps-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="snps-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synopsys(SNPS) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Synopsys (SNPS) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-04 · 마지막 종가 $393.84 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="545.5" x2="1052" y2="545.5" class="grid"/>
<text x="52" y="549.5" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="411.4" x2="1052" y2="411.4" class="grid"/>
<text x="52" y="415.4" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="277.3" x2="1052" y2="277.3" class="grid"/>
<text x="52" y="281.3" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="143.2" x2="1052" y2="143.2" class="grid"/>
<text x="52" y="147.2" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
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
<line x1="61.9" y1="493.7" x2="61.9" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="496.6" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="65.7" y1="496.1" x2="65.7" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="499.3" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="69.5" y1="512.3" x2="69.5" y2="526.7" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="516.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="73.3" y1="520.1" x2="73.3" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="521.3" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="77.0" y1="542.7" x2="77.0" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="546.3" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="80.8" y1="536.6" x2="80.8" y2="560.9" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="537.1" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="84.6" y1="509.4" x2="84.6" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="517.2" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="88.4" y1="500.4" x2="88.4" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="501.0" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="92.2" y1="485.0" x2="92.2" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="490.9" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="96.0" y1="480.0" x2="96.0" y2="495.9" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="482.5" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="99.8" y1="465.5" x2="99.8" y2="487.4" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="467.8" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="103.5" y1="463.4" x2="103.5" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="465.1" width="2.35" height="23.9" fill="var(--down)"/>
<line x1="107.3" y1="457.8" x2="107.3" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="478.8" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="111.1" y1="458.1" x2="111.1" y2="499.8" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="461.9" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="114.9" y1="457.2" x2="114.9" y2="489.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="461.6" width="2.35" height="19.5" fill="var(--down)"/>
<line x1="118.7" y1="453.1" x2="118.7" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="456.8" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="122.5" y1="441.5" x2="122.5" y2="455.6" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="453.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="126.3" y1="449.3" x2="126.3" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="455.5" width="2.35" height="49.3" fill="var(--down)"/>
<line x1="130.0" y1="482.8" x2="130.0" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="510.4" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="133.8" y1="515.1" x2="133.8" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="521.1" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="137.6" y1="533.8" x2="137.6" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="545.6" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="141.4" y1="523.6" x2="141.4" y2="550.9" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="533.6" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="145.2" y1="512.6" x2="145.2" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="532.8" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="149.0" y1="519.2" x2="149.0" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="554.0" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="152.8" y1="529.2" x2="152.8" y2="579.1" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="530.6" width="2.35" height="32.2" fill="var(--up)"/>
<line x1="156.5" y1="520.6" x2="156.5" y2="541.7" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="533.4" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="160.3" y1="530.7" x2="160.3" y2="559.8" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="532.5" width="2.35" height="21.5" fill="var(--down)"/>
<line x1="164.1" y1="517.9" x2="164.1" y2="576.2" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="521.1" width="2.35" height="35.1" fill="var(--up)"/>
<line x1="167.9" y1="510.7" x2="167.9" y2="535.9" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="520.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="171.7" y1="488.4" x2="171.7" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="498.6" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="175.5" y1="490.3" x2="175.5" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="495.9" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="179.3" y1="515.9" x2="179.3" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="524.0" width="2.35" height="28.5" fill="var(--down)"/>
<line x1="183.1" y1="528.7" x2="183.1" y2="566.3" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="554.8" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="186.8" y1="538.7" x2="186.8" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="563.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="190.6" y1="545.6" x2="190.6" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="563.6" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="194.4" y1="575.6" x2="194.4" y2="605.9" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="577.7" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="198.2" y1="534.7" x2="198.2" y2="585.8" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="536.5" width="2.35" height="44.7" fill="var(--up)"/>
<line x1="202.0" y1="514.0" x2="202.0" y2="555.6" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="514.7" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="205.8" y1="503.7" x2="205.8" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="508.4" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="209.6" y1="498.2" x2="209.6" y2="540.3" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="502.4" width="2.35" height="35.9" fill="var(--down)"/>
<line x1="213.3" y1="533.3" x2="213.3" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="550.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="217.1" y1="520.6" x2="217.1" y2="549.3" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="522.1" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="220.9" y1="522.4" x2="220.9" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="527.0" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="224.7" y1="517.6" x2="224.7" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="522.0" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="228.5" y1="519.2" x2="228.5" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="525.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="232.3" y1="487.6" x2="232.3" y2="533.6" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="494.5" width="2.35" height="29.0" fill="var(--up)"/>
<line x1="236.1" y1="452.7" x2="236.1" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="455.0" width="2.35" height="41.0" fill="var(--up)"/>
<line x1="239.8" y1="444.0" x2="239.8" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="445.9" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="243.6" y1="430.2" x2="243.6" y2="453.0" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="430.9" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="247.4" y1="423.3" x2="247.4" y2="463.5" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="431.4" width="2.35" height="29.6" fill="var(--down)"/>
<line x1="251.2" y1="460.3" x2="251.2" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="467.3" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="255.0" y1="472.4" x2="255.0" y2="512.5" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="477.7" width="2.35" height="26.8" fill="var(--down)"/>
<line x1="258.8" y1="488.8" x2="258.8" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="491.6" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="262.6" y1="488.6" x2="262.6" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="489.3" width="2.35" height="37.2" fill="var(--down)"/>
<line x1="266.4" y1="511.3" x2="266.4" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="531.3" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="270.1" y1="525.6" x2="270.1" y2="544.0" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="538.1" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="273.9" y1="510.5" x2="273.9" y2="538.5" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="533.7" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="277.7" y1="534.6" x2="277.7" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="536.0" width="2.35" height="39.5" fill="var(--down)"/>
<line x1="281.5" y1="545.1" x2="281.5" y2="565.4" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="550.2" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="285.3" y1="539.1" x2="285.3" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="547.7" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="289.1" y1="547.7" x2="289.1" y2="585.9" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="554.5" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="292.9" y1="503.3" x2="292.9" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="503.4" width="2.35" height="70.4" fill="var(--up)"/>
<line x1="296.6" y1="491.1" x2="296.6" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="505.3" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="300.4" y1="496.8" x2="300.4" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="501.8" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="304.2" y1="459.7" x2="304.2" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="480.9" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="308.0" y1="484.7" x2="308.0" y2="517.0" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="484.7" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="311.8" y1="477.9" x2="311.8" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="506.5" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="315.6" y1="503.1" x2="315.6" y2="524.6" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="505.7" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="319.4" y1="512.3" x2="319.4" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="517.6" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="323.1" y1="510.2" x2="323.1" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="514.7" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="326.9" y1="496.6" x2="326.9" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="501.3" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="330.7" y1="483.7" x2="330.7" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="488.6" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="334.5" y1="465.2" x2="334.5" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="468.7" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="338.3" y1="445.4" x2="338.3" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="463.1" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="342.1" y1="449.8" x2="342.1" y2="470.7" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="466.3" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="345.9" y1="438.6" x2="345.9" y2="478.5" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="463.4" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="349.6" y1="454.9" x2="349.6" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="462.0" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="353.4" y1="453.8" x2="353.4" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="455.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="357.2" y1="445.9" x2="357.2" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="455.1" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="361.0" y1="440.5" x2="361.0" y2="477.7" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="448.3" width="2.35" height="28.5" fill="var(--up)"/>
<line x1="364.8" y1="435.7" x2="364.8" y2="452.3" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="442.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="368.6" y1="429.2" x2="368.6" y2="457.0" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="429.9" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="372.4" y1="421.1" x2="372.4" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="431.3" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="376.2" y1="433.7" x2="376.2" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="436.0" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="379.9" y1="432.5" x2="379.9" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="435.6" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="383.7" y1="437.1" x2="383.7" y2="464.6" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="444.0" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="387.5" y1="445.2" x2="387.5" y2="456.9" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="449.6" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="391.3" y1="447.1" x2="391.3" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="449.8" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="395.1" y1="386.7" x2="395.1" y2="457.5" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="400.0" width="2.35" height="54.2" fill="var(--up)"/>
<line x1="398.9" y1="344.4" x2="398.9" y2="424.6" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="351.4" width="2.35" height="52.3" fill="var(--up)"/>
<line x1="402.7" y1="320.2" x2="402.7" y2="349.9" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="338.8" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="406.4" y1="338.9" x2="406.4" y2="366.8" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="346.7" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="410.2" y1="341.7" x2="410.2" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="356.2" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="414.0" y1="356.0" x2="414.0" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="361.3" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="417.8" y1="360.0" x2="417.8" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="363.9" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="421.6" y1="361.0" x2="421.6" y2="377.3" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="369.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="425.4" y1="334.7" x2="425.4" y2="368.5" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="338.8" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="429.2" y1="323.3" x2="429.2" y2="343.4" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="338.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="432.9" y1="330.6" x2="432.9" y2="350.5" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="339.0" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="436.7" y1="338.2" x2="436.7" y2="362.2" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="343.0" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="440.5" y1="345.7" x2="440.5" y2="377.3" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="350.6" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="444.3" y1="341.7" x2="444.3" y2="386.6" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="376.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="448.1" y1="335.2" x2="448.1" y2="374.4" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="354.8" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="451.9" y1="325.6" x2="451.9" y2="356.8" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="330.3" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="455.7" y1="316.0" x2="455.7" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="330.3" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="459.5" y1="317.9" x2="459.5" y2="347.1" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="331.2" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="463.2" y1="326.2" x2="463.2" y2="352.4" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="344.1" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="467.0" y1="314.9" x2="467.0" y2="356.9" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="332.3" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="470.8" y1="308.2" x2="470.8" y2="346.7" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="313.2" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="474.6" y1="273.7" x2="474.6" y2="325.1" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="291.1" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="478.4" y1="283.5" x2="478.4" y2="322.4" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="290.0" width="2.35" height="30.7" fill="var(--down)"/>
<line x1="482.2" y1="311.6" x2="482.2" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="322.9" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="486.0" y1="287.7" x2="486.0" y2="337.6" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="293.5" width="2.35" height="37.1" fill="var(--up)"/>
<line x1="489.7" y1="249.8" x2="489.7" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="252.0" width="2.35" height="41.4" fill="var(--up)"/>
<line x1="493.5" y1="221.2" x2="493.5" y2="257.9" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="230.6" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="497.3" y1="211.6" x2="497.3" y2="230.0" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="220.0" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="501.1" y1="190.4" x2="501.1" y2="236.4" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="215.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="504.9" y1="220.4" x2="504.9" y2="246.6" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="223.4" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="508.7" y1="178.4" x2="508.7" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="201.8" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="512.5" y1="189.3" x2="512.5" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="200.2" width="2.35" height="44.3" fill="var(--down)"/>
<line x1="516.2" y1="230.9" x2="516.2" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="237.1" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="520.0" y1="264.6" x2="520.0" y2="307.3" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="266.6" width="2.35" height="31.0" fill="var(--down)"/>
<line x1="523.8" y1="264.2" x2="523.8" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="284.8" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="527.6" y1="253.6" x2="527.6" y2="288.6" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="254.1" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="531.4" y1="204.1" x2="531.4" y2="246.4" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="239.6" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="535.2" y1="207.0" x2="535.2" y2="238.5" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="207.5" width="2.35" height="30.4" fill="var(--up)"/>
<line x1="539.0" y1="166.2" x2="539.0" y2="231.4" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="176.3" width="2.35" height="27.2" fill="var(--up)"/>
<line x1="542.7" y1="172.7" x2="542.7" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="175.4" width="2.35" height="31.0" fill="var(--down)"/>
<line x1="546.5" y1="103.8" x2="546.5" y2="241.0" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="175.8" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="550.3" y1="152.7" x2="550.3" y2="188.5" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="154.8" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="554.1" y1="137.3" x2="554.1" y2="196.2" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="146.2" width="2.35" height="35.5" fill="var(--down)"/>
<line x1="557.9" y1="173.8" x2="557.9" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="192.8" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="561.7" y1="121.0" x2="561.7" y2="203.4" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="151.0" width="2.35" height="47.8" fill="var(--up)"/>
<line x1="565.5" y1="154.9" x2="565.5" y2="183.4" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="160.7" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="569.3" y1="153.0" x2="569.3" y2="192.0" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="172.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="573.0" y1="165.7" x2="573.0" y2="210.0" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="176.2" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="576.8" y1="186.2" x2="576.8" y2="266.3" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="186.2" width="2.35" height="76.7" fill="var(--down)"/>
<line x1="580.6" y1="211.9" x2="580.6" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="218.7" width="2.35" height="41.0" fill="var(--up)"/>
<line x1="584.4" y1="211.8" x2="584.4" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="216.7" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="588.2" y1="192.9" x2="588.2" y2="227.6" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="201.2" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="592.0" y1="166.0" x2="592.0" y2="206.5" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="187.8" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="595.8" y1="135.9" x2="595.8" y2="189.9" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="160.1" width="2.35" height="27.7" fill="var(--up)"/>
<line x1="599.5" y1="153.4" x2="599.5" y2="216.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="168.1" width="2.35" height="27.6" fill="var(--down)"/>
<line x1="603.3" y1="152.8" x2="603.3" y2="210.3" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="181.5" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="607.1" y1="147.2" x2="607.1" y2="188.5" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="156.3" width="2.35" height="31.2" fill="var(--up)"/>
<line x1="610.9" y1="112.3" x2="610.9" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="135.8" width="2.35" height="19.5" fill="var(--up)"/>
<line x1="614.7" y1="132.2" x2="614.7" y2="151.7" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="144.2" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="618.5" y1="112.6" x2="618.5" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="114.6" width="2.35" height="35.6" fill="var(--up)"/>
<line x1="622.3" y1="109.9" x2="622.3" y2="139.0" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="114.1" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="626.0" y1="114.7" x2="626.0" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="126.3" width="2.35" height="66.3" fill="var(--down)"/>
<line x1="629.8" y1="151.3" x2="629.8" y2="227.5" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="179.4" width="2.35" height="35.7" fill="var(--down)"/>
<line x1="633.6" y1="184.8" x2="633.6" y2="299.2" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="209.9" width="2.35" height="59.6" fill="var(--down)"/>
<line x1="637.4" y1="242.0" x2="637.4" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="244.1" width="2.35" height="66.7" fill="var(--up)"/>
<line x1="641.2" y1="204.8" x2="641.2" y2="253.2" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="211.6" width="2.35" height="34.8" fill="var(--up)"/>
<line x1="645.0" y1="162.4" x2="645.0" y2="226.2" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="211.6" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="648.8" y1="227.2" x2="648.8" y2="268.8" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="232.3" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="652.5" y1="258.0" x2="652.5" y2="327.7" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="258.3" width="2.35" height="67.3" fill="var(--down)"/>
<line x1="656.3" y1="284.3" x2="656.3" y2="334.3" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="290.6" width="2.35" height="31.6" fill="var(--up)"/>
<line x1="660.1" y1="248.6" x2="660.1" y2="289.2" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="268.4" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="663.9" y1="243.1" x2="663.9" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="259.4" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="667.7" y1="261.9" x2="667.7" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="261.9" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="671.5" y1="222.0" x2="671.5" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="223.8" width="2.35" height="62.9" fill="var(--up)"/>
<line x1="675.3" y1="209.4" x2="675.3" y2="283.3" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="217.9" width="2.35" height="50.0" fill="var(--down)"/>
<line x1="679.1" y1="266.1" x2="679.1" y2="291.0" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="274.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="682.8" y1="227.8" x2="682.8" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="252.6" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="686.6" y1="177.2" x2="686.6" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="194.7" width="2.35" height="53.6" fill="var(--up)"/>
<line x1="690.4" y1="187.4" x2="690.4" y2="250.9" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="197.5" width="2.35" height="52.0" fill="var(--down)"/>
<line x1="694.2" y1="185.5" x2="694.2" y2="257.2" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="190.0" width="2.35" height="55.5" fill="var(--up)"/>
<line x1="698.0" y1="183.0" x2="698.0" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="184.2" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="701.8" y1="152.6" x2="701.8" y2="259.7" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="202.3" width="2.35" height="51.8" fill="var(--down)"/>
<line x1="705.6" y1="253.5" x2="705.6" y2="283.5" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="256.8" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="709.3" y1="243.3" x2="709.3" y2="299.4" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="267.4" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="713.1" y1="266.6" x2="713.1" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="285.4" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="716.9" y1="284.2" x2="716.9" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="285.7" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="720.7" y1="265.1" x2="720.7" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="277.8" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="724.5" y1="237.1" x2="724.5" y2="297.9" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="241.5" width="2.35" height="50.5" fill="var(--up)"/>
<line x1="728.3" y1="201.8" x2="728.3" y2="241.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="215.3" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="732.1" y1="231.7" x2="732.1" y2="274.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="243.1" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="735.8" y1="216.1" x2="735.8" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="242.7" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="739.6" y1="228.7" x2="739.6" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="239.9" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="743.4" y1="239.7" x2="743.4" y2="313.9" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="239.8" width="2.35" height="71.2" fill="var(--down)"/>
<line x1="747.2" y1="293.4" x2="747.2" y2="346.9" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="305.1" width="2.35" height="29.5" fill="var(--down)"/>
<line x1="751.0" y1="320.6" x2="751.0" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="326.2" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="754.8" y1="344.7" x2="754.8" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="349.4" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="758.6" y1="329.9" x2="758.6" y2="360.3" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="346.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="762.4" y1="325.3" x2="762.4" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="335.2" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="766.1" y1="352.9" x2="766.1" y2="428.3" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="372.5" width="2.35" height="54.8" fill="var(--down)"/>
<line x1="769.9" y1="367.8" x2="769.9" y2="457.4" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="383.0" width="2.35" height="60.7" fill="var(--up)"/>
<line x1="773.7" y1="370.4" x2="773.7" y2="399.9" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="372.7" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="777.5" y1="348.0" x2="777.5" y2="416.7" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="348.9" width="2.35" height="54.1" fill="var(--up)"/>
<line x1="781.3" y1="308.9" x2="781.3" y2="361.9" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="314.5" width="2.35" height="37.4" fill="var(--up)"/>
<line x1="785.1" y1="288.9" x2="785.1" y2="323.4" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="300.2" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="788.9" y1="249.0" x2="788.9" y2="281.3" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="257.9" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="792.6" y1="252.5" x2="792.6" y2="285.7" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="267.2" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="796.4" y1="257.1" x2="796.4" y2="360.9" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="267.7" width="2.35" height="57.9" fill="var(--down)"/>
<line x1="800.2" y1="289.7" x2="800.2" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="296.1" width="2.35" height="35.0" fill="var(--up)"/>
<line x1="804.0" y1="261.2" x2="804.0" y2="307.4" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="272.1" width="2.35" height="33.6" fill="var(--down)"/>
<line x1="807.8" y1="298.0" x2="807.8" y2="319.5" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="303.4" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="811.6" y1="248.2" x2="811.6" y2="329.7" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="273.8" width="2.35" height="45.3" fill="var(--up)"/>
<line x1="815.4" y1="203.5" x2="815.4" y2="272.0" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="211.9" width="2.35" height="57.5" fill="var(--up)"/>
<line x1="819.1" y1="179.5" x2="819.1" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="197.8" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="822.9" y1="142.0" x2="822.9" y2="220.3" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="163.6" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="826.7" y1="118.4" x2="826.7" y2="171.5" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="141.1" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="830.5" y1="73.8" x2="830.5" y2="158.8" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="118.2" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="834.3" y1="94.1" x2="834.3" y2="132.2" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="113.1" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="838.1" y1="104.4" x2="838.1" y2="134.7" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="115.8" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="841.9" y1="108.0" x2="841.9" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="119.2" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="845.6" y1="123.6" x2="845.6" y2="152.6" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="136.5" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="849.4" y1="122.1" x2="849.4" y2="164.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="145.7" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="853.2" y1="122.0" x2="853.2" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="141.9" width="2.35" height="235.3" fill="var(--down)"/>
<line x1="857.0" y1="279.9" x2="857.0" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="283.3" width="2.35" height="85.8" fill="var(--up)"/>
<line x1="860.8" y1="256.3" x2="860.8" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="290.7" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="864.6" y1="283.0" x2="864.6" y2="322.1" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="293.4" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="868.4" y1="287.5" x2="868.4" y2="361.4" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="314.9" width="2.35" height="44.4" fill="var(--down)"/>
<line x1="872.2" y1="335.2" x2="872.2" y2="368.5" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="345.1" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="875.9" y1="312.8" x2="875.9" y2="351.9" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="325.3" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="879.7" y1="310.3" x2="879.7" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="315.8" width="2.35" height="23.4" fill="var(--down)"/>
<line x1="883.5" y1="341.0" x2="883.5" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="341.9" width="2.35" height="78.3" fill="var(--down)"/>
<line x1="887.3" y1="406.4" x2="887.3" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="412.9" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="891.1" y1="404.0" x2="891.1" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="425.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="894.9" y1="386.1" x2="894.9" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="387.3" width="2.35" height="30.9" fill="var(--up)"/>
<line x1="898.7" y1="316.0" x2="898.7" y2="372.2" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="321.9" width="2.35" height="27.8" fill="var(--up)"/>
<line x1="902.4" y1="301.1" x2="902.4" y2="341.0" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="320.5" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="906.2" y1="316.6" x2="906.2" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="325.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="910.0" y1="298.9" x2="910.0" y2="320.5" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="308.0" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="913.8" y1="296.2" x2="913.8" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="303.6" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="917.6" y1="238.5" x2="917.6" y2="305.5" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="243.5" width="2.35" height="53.8" fill="var(--up)"/>
<line x1="921.4" y1="230.1" x2="921.4" y2="279.2" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="244.8" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="925.2" y1="243.1" x2="925.2" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="275.4" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="928.9" y1="256.1" x2="928.9" y2="326.6" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="277.4" width="2.35" height="46.7" fill="var(--down)"/>
<line x1="932.7" y1="315.9" x2="932.7" y2="403.8" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="330.0" width="2.35" height="45.3" fill="var(--down)"/>
<line x1="936.5" y1="341.7" x2="936.5" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="361.7" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="940.3" y1="343.8" x2="940.3" y2="394.9" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="357.8" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="944.1" y1="338.8" x2="944.1" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="372.0" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="947.9" y1="347.4" x2="947.9" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="361.2" width="2.35" height="32.2" fill="var(--up)"/>
<line x1="951.7" y1="356.5" x2="951.7" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="367.7" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="955.5" y1="363.5" x2="955.5" y2="387.8" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="384.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="959.2" y1="355.4" x2="959.2" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="370.9" width="2.35" height="66.7" fill="var(--down)"/>
<line x1="963.0" y1="406.8" x2="963.0" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="416.8" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="966.8" y1="391.1" x2="966.8" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="416.7" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="970.6" y1="332.3" x2="970.6" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="344.9" width="2.35" height="76.6" fill="var(--up)"/>
<line x1="974.4" y1="274.2" x2="974.4" y2="347.8" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="276.2" width="2.35" height="70.7" fill="var(--up)"/>
<line x1="978.2" y1="276.0" x2="978.2" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="281.4" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="982.0" y1="251.7" x2="982.0" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="255.2" width="2.35" height="30.4" fill="var(--up)"/>
<line x1="985.7" y1="250.9" x2="985.7" y2="289.3" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="258.7" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="989.5" y1="231.5" x2="989.5" y2="312.5" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="244.1" width="2.35" height="34.3" fill="var(--up)"/>
<line x1="993.3" y1="224.3" x2="993.3" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="237.1" width="2.35" height="72.9" fill="var(--down)"/>
<line x1="997.1" y1="265.6" x2="997.1" y2="332.9" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="298.7" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="1000.9" y1="294.0" x2="1000.9" y2="351.1" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="321.2" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="1004.7" y1="306.1" x2="1004.7" y2="351.3" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="327.9" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="1008.5" y1="304.4" x2="1008.5" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="336.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="1012.2" y1="325.0" x2="1012.2" y2="365.5" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="333.7" width="2.35" height="27.9" fill="var(--down)"/>
<line x1="1016.0" y1="342.2" x2="1016.0" y2="376.8" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="350.4" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="1019.8" y1="339.1" x2="1019.8" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="345.9" width="2.35" height="86.6" fill="var(--down)"/>
<line x1="1023.6" y1="423.4" x2="1023.6" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="435.6" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="1027.4" y1="408.4" x2="1027.4" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="426.5" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="1031.2" y1="389.4" x2="1031.2" y2="430.2" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="390.0" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="1035.0" y1="379.3" x2="1035.0" y2="408.5" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="382.6" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="1038.7" y1="376.8" x2="1038.7" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="387.8" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="1042.5" y1="324.3" x2="1042.5" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="354.3" width="2.35" height="63.6" fill="var(--up)"/>
<line x1="1046.3" y1="349.9" x2="1046.3" y2="437.8" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="360.5" width="2.35" height="59.2" fill="var(--down)"/>
<line x1="1050.1" y1="387.1" x2="1050.1" y2="437.8" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="387.1" width="2.35" height="32.6" fill="var(--down)"/>
<line x1="60" y1="321.8" x2="1052" y2="321.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="325.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$467 R1</text>
<text x="1058" y="337.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="227.2" x2="1052" y2="227.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="230.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$537 R2</text>
<text x="1058" y="242.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="106.8" x2="1052" y2="106.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="110.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$627 R3</text>
<text x="1058" y="122.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="439.8" x2="1052" y2="439.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="433.8" font-size="11.5" fill="var(--support)" font-weight="600">$379 S1</text>
<text x="1058" y="445.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="459.6" x2="1052" y2="459.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="453.6" font-size="11.5" fill="var(--support)" font-weight="600">$364 S2</text>
<text x="1058" y="465.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="419.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="411.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $394 (2026-09-04)</text>
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
| R3 | $627 | 2 | 2024-02-19·2024-07-08 주간 고점대 — Ansys 인수 발표 전후의 고점 구간이라 현재 자본구조와 단절돼 있다 |
| R2 | $537 | 2 | 2026-01-12·2026-05-25 주간 고점대 |
| R1 | $467 | 2 | 2023-05-29·2023-07-17 주간 고점대 — 3년 전 가격대이지만 2026년 하반기 조정으로 다시 유효 범위에 들어왔다 |
| **현재가** | **$393.84** (2026-09-04 종가) | — | R1과 S1 사이 |
| S1 | $379 | 3 | 2025-09-08·2025-11-17·2026-03-23 주간 저점대 — 현재가 바로 아래, 터치 3회로 이 차트에서 가장 두꺼운 지지 |
| S2 | $364 | 3 | 2023-04-24·2025-04-07·2026-07-13 주간 저점대 — 52주 최저($366.00)를 포함하는 구간 |

> 저항 3개는 모두 터치 2회에 그치는 반면 **지지 두 개(S1·S2)는 각각 3회씩 터치됐다.** 5년 창에서 이 종목의 상단은 계속 밀려 올라갔다가 되돌려진 반면, 하단은 반복해서 확인된 형태다 — 다만 S2($364)의 터치 중 하나는 2023년 것이라 **현재 자본구조와 계보가 다르다**(아래 한계 참고).

---

## 3. 관측된 특이 구간 — 2025~2026년의 두 번의 레짐 전환

- 주봉으로 보면 최근 2년은 **두 번의 단절**을 지난다. **① 2025-07-17 Ansys 인수 완료** — 자기자본이 3배, 이자부 차입금이 20배 늘며 재무 계보가 끊겼다([핵심 지표](./04_metrics.md) 상단 경고). **② 2025-09-08 사상 최고 $615.79 이후의 장기 하락** — 2026-07-17 저점 $366.00까지 −40.6%.
- 현재가 $393.84는 **S1($379)과 R1($467) 사이**로, 5년 창에서 보면 2023년 중반 수준으로 되돌아온 자리다. 그 사이 매출은 $5,318M(FY2023) → $9,715M(FY2026 E)으로 1.83배가 됐으므로, **같은 가격이지만 매출 대비로는 훨씬 싸졌다**(EV/매출 13.53 → 8.54).
- 반대로 **R3($627)·R2($537)는 Ansys 인수 전후의 고점**이라 현재 재무구조와 계보가 다르다. 회복 목표로 삼기 전에 그때와 지금의 이자비용·주식수 차이를 함께 볼 것.

---

## 4. 방법론 · 한계

@@FACTS@@
- **생성**: `scripts/gen_technical_chart.py SNPS --name Synopsys --interval 1wk --close-on 2026-09-04 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **5년 창 안에서 회사가 두 번 바뀌었다.** 2024-09-30 Software Integrity 매각으로 **과거 재무가 소급 재작성**됐고, 2025-07-17 Ansys 인수로 **자본구조가 단절**됐다. 2023~2024년에 형성된 레벨(R1 $467, R3 $627, S2의 2023년 터치)은 **지금과 다른 회사의 가격**이므로 현재 판단에 그대로 쓰지 말 것.
    - 이 기간에 주식분할·병합은 없었다(확인 완료). 발행주식수 증가(154.1 → 191.6백만 주)는 Ansys 인수 대가 신주 발행 때문이며 주가 소급조정 대상이 아니다.

---

*작성일: 2026-09-11*
