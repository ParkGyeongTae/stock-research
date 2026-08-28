# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-08-27 종가 $464.89로 [기술적 분석 — 일봉·1년](./09_technical_daily.md)·[핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)와 일치**한다. 마지막 주(2026-08-24 시작)는 아직 진행 중이라 그 주 종가 = 2026-08-27 종가다.
    - 이 5년 안에 주식분할·병합은 없었고 두 시계열 모두 원주가(배당 미반영)라 값이 어긋나지 않는다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-27)

<div class="snps-chart">
<style>
.snps-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.snps-chart svg { width:100%; height:auto; display:block; }
.snps-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.snps-chart .title { fill: var(--ink); font-weight:600; }
.snps-chart .grid { stroke: var(--grid); stroke-width:1; }
.snps-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synopsys(SNPS) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Synopsys (SNPS) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-27 · 마지막 종가 $464.89 (2026-08-27) · 단위 USD</text>
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
<line x1="60" y1="605.9" x2="1052" y2="605.9" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="608.9" font-size="10.5" fill="var(--muted)">$255 5년 최저</text>
<line x1="60" y1="73.8" x2="1052" y2="73.8" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="76.8" font-size="10.5" fill="var(--muted)">$652 5년 최고</text>
<line x1="827.6" y1="56.0" x2="827.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="833.6" y="68.0" font-size="10.5" fill="var(--down)">2025-07-14 Ansys 인수 완료</text>
<line x1="857.7" y1="56.0" x2="857.7" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="863.7" y="68.0" font-size="10.5" fill="var(--down)">2025-09-08 FY2025 Q3 실적 갭다운</text>
<line x1="61.9" y1="500.7" x2="61.9" y2="509.3" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="502.9" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="65.7" y1="491.0" x2="65.7" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="496.4" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="69.4" y1="493.7" x2="69.4" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="496.6" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="73.2" y1="496.1" x2="73.2" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="499.3" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="77.0" y1="512.3" x2="77.0" y2="526.7" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="516.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="80.7" y1="520.1" x2="80.7" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="521.3" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="84.5" y1="542.7" x2="84.5" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="546.3" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="88.3" y1="536.6" x2="88.3" y2="560.9" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="537.1" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="92.1" y1="509.4" x2="92.1" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="517.2" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="95.8" y1="500.4" x2="95.8" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="501.0" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="99.6" y1="485.0" x2="99.6" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="490.9" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="103.4" y1="480.0" x2="103.4" y2="495.9" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="482.5" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="107.1" y1="465.5" x2="107.1" y2="487.4" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="467.8" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="110.9" y1="463.4" x2="110.9" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="465.1" width="2.34" height="23.9" fill="var(--down)"/>
<line x1="114.7" y1="457.8" x2="114.7" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="478.8" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="118.5" y1="458.1" x2="118.5" y2="499.8" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="461.9" width="2.34" height="24.9" fill="var(--up)"/>
<line x1="122.2" y1="457.2" x2="122.2" y2="489.3" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="461.6" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="126.0" y1="453.1" x2="126.0" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="456.8" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="129.8" y1="441.5" x2="129.8" y2="455.6" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="453.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="133.6" y1="449.3" x2="133.6" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="455.5" width="2.34" height="49.3" fill="var(--down)"/>
<line x1="137.3" y1="482.8" x2="137.3" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="510.4" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="141.1" y1="515.1" x2="141.1" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="521.1" width="2.34" height="20.0" fill="var(--down)"/>
<line x1="144.9" y1="533.8" x2="144.9" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="545.6" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="148.6" y1="523.6" x2="148.6" y2="550.9" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="533.6" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="152.4" y1="512.6" x2="152.4" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="532.8" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="156.2" y1="519.2" x2="156.2" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="554.0" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="160.0" y1="529.2" x2="160.0" y2="579.1" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="530.6" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="163.7" y1="520.6" x2="163.7" y2="541.7" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="533.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="167.5" y1="530.7" x2="167.5" y2="559.8" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="532.5" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="171.3" y1="517.9" x2="171.3" y2="576.2" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="521.1" width="2.34" height="35.1" fill="var(--up)"/>
<line x1="175.0" y1="510.7" x2="175.0" y2="535.9" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="520.2" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="178.8" y1="488.4" x2="178.8" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="498.6" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="182.6" y1="490.3" x2="182.6" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="495.9" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="186.4" y1="515.9" x2="186.4" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="524.0" width="2.34" height="28.5" fill="var(--down)"/>
<line x1="190.1" y1="528.7" x2="190.1" y2="566.3" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="554.8" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="193.9" y1="538.7" x2="193.9" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="563.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="197.7" y1="545.6" x2="197.7" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="563.6" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="201.4" y1="575.6" x2="201.4" y2="605.9" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="577.7" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="205.2" y1="534.7" x2="205.2" y2="585.8" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="536.5" width="2.34" height="44.7" fill="var(--up)"/>
<line x1="209.0" y1="514.0" x2="209.0" y2="555.6" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="514.7" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="212.8" y1="503.7" x2="212.8" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="508.4" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="216.5" y1="498.2" x2="216.5" y2="540.3" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="502.4" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="220.3" y1="533.3" x2="220.3" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="550.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="224.1" y1="520.6" x2="224.1" y2="549.3" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="522.1" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="227.8" y1="522.4" x2="227.8" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="527.0" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="231.6" y1="517.6" x2="231.6" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="522.0" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="235.4" y1="519.2" x2="235.4" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="525.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="239.2" y1="487.6" x2="239.2" y2="533.6" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="494.5" width="2.34" height="29.0" fill="var(--up)"/>
<line x1="242.9" y1="452.7" x2="242.9" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="455.0" width="2.34" height="41.0" fill="var(--up)"/>
<line x1="246.7" y1="444.0" x2="246.7" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="445.9" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="250.5" y1="430.2" x2="250.5" y2="453.0" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="430.9" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="254.3" y1="423.3" x2="254.3" y2="463.5" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="431.4" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="258.0" y1="460.3" x2="258.0" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="467.3" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="261.8" y1="472.4" x2="261.8" y2="512.5" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="477.7" width="2.34" height="26.8" fill="var(--down)"/>
<line x1="265.6" y1="488.8" x2="265.6" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="491.6" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="269.3" y1="488.6" x2="269.3" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="489.3" width="2.34" height="37.2" fill="var(--down)"/>
<line x1="273.1" y1="511.3" x2="273.1" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="531.3" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="276.9" y1="525.6" x2="276.9" y2="544.0" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="538.1" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="280.7" y1="510.5" x2="280.7" y2="538.5" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="533.7" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="284.4" y1="534.6" x2="284.4" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="536.0" width="2.34" height="39.5" fill="var(--down)"/>
<line x1="288.2" y1="545.1" x2="288.2" y2="565.4" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="550.2" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="292.0" y1="539.1" x2="292.0" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="547.7" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="295.7" y1="547.7" x2="295.7" y2="585.9" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="554.5" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="299.5" y1="503.3" x2="299.5" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="503.4" width="2.34" height="70.4" fill="var(--up)"/>
<line x1="303.3" y1="491.1" x2="303.3" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="505.3" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="307.1" y1="496.8" x2="307.1" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="501.8" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="310.8" y1="459.7" x2="310.8" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="480.9" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="314.6" y1="484.7" x2="314.6" y2="517.0" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="484.7" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="318.4" y1="477.9" x2="318.4" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="506.5" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="322.1" y1="503.1" x2="322.1" y2="524.6" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="505.7" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="325.9" y1="512.3" x2="325.9" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="517.6" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="329.7" y1="510.2" x2="329.7" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="514.7" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="333.5" y1="496.6" x2="333.5" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="501.3" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="337.2" y1="483.7" x2="337.2" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="488.6" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="341.0" y1="465.2" x2="341.0" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="468.7" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="344.8" y1="445.4" x2="344.8" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="463.1" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="348.5" y1="449.8" x2="348.5" y2="470.7" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="466.3" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="352.3" y1="438.6" x2="352.3" y2="478.5" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="463.4" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="356.1" y1="454.9" x2="356.1" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="462.0" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="359.9" y1="453.8" x2="359.9" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="455.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="363.6" y1="445.9" x2="363.6" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="455.1" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="367.4" y1="440.5" x2="367.4" y2="477.7" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="448.3" width="2.34" height="28.5" fill="var(--up)"/>
<line x1="371.2" y1="435.7" x2="371.2" y2="452.3" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="442.8" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="375.0" y1="429.2" x2="375.0" y2="457.0" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="429.9" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="378.7" y1="421.1" x2="378.7" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="431.3" width="2.34" height="12.4" fill="var(--down)"/>
<line x1="382.5" y1="433.7" x2="382.5" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="436.0" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="386.3" y1="432.5" x2="386.3" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="435.6" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="390.0" y1="437.1" x2="390.0" y2="464.6" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="444.0" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="393.8" y1="445.2" x2="393.8" y2="456.9" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="449.6" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="397.6" y1="447.1" x2="397.6" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="449.8" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="401.4" y1="386.7" x2="401.4" y2="457.5" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="400.0" width="2.34" height="54.2" fill="var(--up)"/>
<line x1="405.1" y1="344.4" x2="405.1" y2="424.6" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="351.4" width="2.34" height="52.3" fill="var(--up)"/>
<line x1="408.9" y1="320.2" x2="408.9" y2="349.9" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="338.8" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="412.7" y1="338.9" x2="412.7" y2="366.8" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="346.7" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="416.4" y1="341.7" x2="416.4" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="356.2" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="420.2" y1="356.0" x2="420.2" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="361.3" width="2.34" height="23.8" fill="var(--down)"/>
<line x1="424.0" y1="360.0" x2="424.0" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="363.9" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="427.8" y1="361.0" x2="427.8" y2="377.3" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="369.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="431.5" y1="334.7" x2="431.5" y2="368.5" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="338.8" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="435.3" y1="323.3" x2="435.3" y2="343.4" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="338.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="439.1" y1="330.6" x2="439.1" y2="350.5" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="339.0" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="442.8" y1="338.2" x2="442.8" y2="362.2" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="343.0" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="446.6" y1="345.7" x2="446.6" y2="377.3" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="350.6" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="450.4" y1="341.7" x2="450.4" y2="386.6" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="376.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="454.2" y1="335.2" x2="454.2" y2="374.4" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="354.8" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="457.9" y1="325.6" x2="457.9" y2="356.8" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="330.3" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="461.7" y1="316.0" x2="461.7" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="330.3" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="465.5" y1="317.9" x2="465.5" y2="347.1" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="331.2" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="469.2" y1="326.2" x2="469.2" y2="352.4" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="344.1" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="473.0" y1="314.9" x2="473.0" y2="356.9" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="332.3" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="476.8" y1="308.2" x2="476.8" y2="346.7" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="313.2" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="480.6" y1="273.7" x2="480.6" y2="325.1" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="291.1" width="2.34" height="29.1" fill="var(--up)"/>
<line x1="484.3" y1="283.5" x2="484.3" y2="322.4" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="290.0" width="2.34" height="30.7" fill="var(--down)"/>
<line x1="488.1" y1="311.6" x2="488.1" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="322.9" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="491.9" y1="287.7" x2="491.9" y2="337.6" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="293.5" width="2.34" height="37.1" fill="var(--up)"/>
<line x1="495.7" y1="249.8" x2="495.7" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="252.0" width="2.34" height="41.4" fill="var(--up)"/>
<line x1="499.4" y1="221.2" x2="499.4" y2="257.9" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="230.6" width="2.34" height="24.9" fill="var(--up)"/>
<line x1="503.2" y1="211.6" x2="503.2" y2="230.0" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="220.0" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="507.0" y1="190.4" x2="507.0" y2="236.4" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="215.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="220.4" x2="510.7" y2="246.6" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="223.4" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="514.5" y1="178.4" x2="514.5" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="201.8" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="518.3" y1="189.3" x2="518.3" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="200.2" width="2.34" height="44.3" fill="var(--down)"/>
<line x1="522.1" y1="230.9" x2="522.1" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="237.1" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="525.8" y1="264.6" x2="525.8" y2="307.3" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="266.6" width="2.34" height="31.0" fill="var(--down)"/>
<line x1="529.6" y1="264.2" x2="529.6" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="284.8" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="533.4" y1="253.6" x2="533.4" y2="288.6" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="254.1" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="537.1" y1="204.1" x2="537.1" y2="246.4" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="239.6" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="540.9" y1="207.0" x2="540.9" y2="238.5" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="207.5" width="2.34" height="30.4" fill="var(--up)"/>
<line x1="544.7" y1="166.2" x2="544.7" y2="231.4" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="176.3" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="548.5" y1="172.7" x2="548.5" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="175.4" width="2.34" height="31.0" fill="var(--down)"/>
<line x1="552.2" y1="103.8" x2="552.2" y2="241.0" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="175.8" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="556.0" y1="152.7" x2="556.0" y2="188.5" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="154.8" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="559.8" y1="137.3" x2="559.8" y2="196.2" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="146.2" width="2.34" height="35.5" fill="var(--down)"/>
<line x1="563.5" y1="173.8" x2="563.5" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="192.8" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="567.3" y1="121.0" x2="567.3" y2="203.4" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="151.0" width="2.34" height="47.8" fill="var(--up)"/>
<line x1="571.1" y1="154.9" x2="571.1" y2="183.4" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="160.7" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="574.9" y1="153.0" x2="574.9" y2="192.0" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="172.6" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="578.6" y1="165.7" x2="578.6" y2="210.0" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="176.2" width="2.34" height="24.5" fill="var(--down)"/>
<line x1="582.4" y1="186.2" x2="582.4" y2="266.3" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="186.2" width="2.34" height="76.7" fill="var(--down)"/>
<line x1="586.2" y1="211.9" x2="586.2" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="218.7" width="2.34" height="41.0" fill="var(--up)"/>
<line x1="589.9" y1="211.8" x2="589.9" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="216.7" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="593.7" y1="192.9" x2="593.7" y2="227.6" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="201.2" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="597.5" y1="166.0" x2="597.5" y2="206.5" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="187.8" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="601.3" y1="135.9" x2="601.3" y2="189.9" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="160.1" width="2.34" height="27.7" fill="var(--up)"/>
<line x1="605.0" y1="153.4" x2="605.0" y2="216.9" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="168.1" width="2.34" height="27.6" fill="var(--down)"/>
<line x1="608.8" y1="152.8" x2="608.8" y2="210.3" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="181.5" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="612.6" y1="147.2" x2="612.6" y2="188.5" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="156.3" width="2.34" height="31.2" fill="var(--up)"/>
<line x1="616.3" y1="112.3" x2="616.3" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="135.8" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="620.1" y1="132.2" x2="620.1" y2="151.7" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="144.2" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="623.9" y1="112.6" x2="623.9" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="114.6" width="2.34" height="35.6" fill="var(--up)"/>
<line x1="627.7" y1="109.9" x2="627.7" y2="139.0" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="114.1" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="631.4" y1="114.7" x2="631.4" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="126.3" width="2.34" height="66.3" fill="var(--down)"/>
<line x1="635.2" y1="151.3" x2="635.2" y2="227.5" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="179.4" width="2.34" height="35.7" fill="var(--down)"/>
<line x1="639.0" y1="184.8" x2="639.0" y2="299.2" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="209.9" width="2.34" height="59.6" fill="var(--down)"/>
<line x1="642.8" y1="242.0" x2="642.8" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="244.1" width="2.34" height="66.7" fill="var(--up)"/>
<line x1="646.5" y1="204.8" x2="646.5" y2="253.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="211.6" width="2.34" height="34.8" fill="var(--up)"/>
<line x1="650.3" y1="162.4" x2="650.3" y2="226.2" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="211.6" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="654.1" y1="227.2" x2="654.1" y2="268.8" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="232.3" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="657.8" y1="258.0" x2="657.8" y2="327.7" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="258.3" width="2.34" height="67.3" fill="var(--down)"/>
<line x1="661.6" y1="284.3" x2="661.6" y2="334.3" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="290.6" width="2.34" height="31.6" fill="var(--up)"/>
<line x1="665.4" y1="248.6" x2="665.4" y2="289.2" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="268.4" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="669.2" y1="243.1" x2="669.2" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="259.4" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="672.9" y1="261.9" x2="672.9" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="261.9" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="676.7" y1="222.0" x2="676.7" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="223.8" width="2.34" height="62.9" fill="var(--up)"/>
<line x1="680.5" y1="209.4" x2="680.5" y2="283.3" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="217.9" width="2.34" height="50.0" fill="var(--down)"/>
<line x1="684.2" y1="266.1" x2="684.2" y2="291.0" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="274.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="688.0" y1="227.8" x2="688.0" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="252.6" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="691.8" y1="177.2" x2="691.8" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="194.7" width="2.34" height="53.6" fill="var(--up)"/>
<line x1="695.6" y1="187.4" x2="695.6" y2="250.9" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="197.5" width="2.34" height="52.0" fill="var(--down)"/>
<line x1="699.3" y1="185.5" x2="699.3" y2="257.2" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="190.0" width="2.34" height="55.5" fill="var(--up)"/>
<line x1="703.1" y1="183.0" x2="703.1" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="184.2" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="706.9" y1="152.6" x2="706.9" y2="259.7" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="202.3" width="2.34" height="51.8" fill="var(--down)"/>
<line x1="710.6" y1="253.5" x2="710.6" y2="283.5" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="256.8" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="714.4" y1="243.3" x2="714.4" y2="299.4" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="267.4" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="718.2" y1="266.6" x2="718.2" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="285.4" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="722.0" y1="284.2" x2="722.0" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="285.7" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="725.7" y1="265.1" x2="725.7" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="277.8" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="729.5" y1="237.1" x2="729.5" y2="297.9" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="241.5" width="2.34" height="50.5" fill="var(--up)"/>
<line x1="733.3" y1="201.8" x2="733.3" y2="241.0" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="215.3" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="737.0" y1="231.7" x2="737.0" y2="274.4" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="243.1" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="740.8" y1="216.1" x2="740.8" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="242.7" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="744.6" y1="228.7" x2="744.6" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="239.9" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="748.4" y1="239.7" x2="748.4" y2="313.9" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="239.8" width="2.34" height="71.2" fill="var(--down)"/>
<line x1="752.1" y1="293.4" x2="752.1" y2="346.9" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="305.1" width="2.34" height="29.5" fill="var(--down)"/>
<line x1="755.9" y1="320.6" x2="755.9" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="326.2" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="759.7" y1="344.7" x2="759.7" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="349.4" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="763.5" y1="329.9" x2="763.5" y2="360.3" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="346.2" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="767.2" y1="325.3" x2="767.2" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="335.2" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="771.0" y1="352.9" x2="771.0" y2="428.3" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="372.5" width="2.34" height="54.8" fill="var(--down)"/>
<line x1="774.8" y1="367.8" x2="774.8" y2="457.4" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="383.0" width="2.34" height="60.7" fill="var(--up)"/>
<line x1="778.5" y1="370.4" x2="778.5" y2="399.9" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="372.7" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="782.3" y1="348.0" x2="782.3" y2="416.7" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="348.9" width="2.34" height="54.1" fill="var(--up)"/>
<line x1="786.1" y1="308.9" x2="786.1" y2="361.9" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="314.5" width="2.34" height="37.4" fill="var(--up)"/>
<line x1="789.9" y1="288.9" x2="789.9" y2="323.4" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="300.2" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="793.6" y1="249.0" x2="793.6" y2="281.3" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="257.9" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="797.4" y1="252.5" x2="797.4" y2="285.7" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="267.2" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="801.2" y1="257.1" x2="801.2" y2="360.9" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="267.7" width="2.34" height="57.9" fill="var(--down)"/>
<line x1="804.9" y1="289.7" x2="804.9" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="296.1" width="2.34" height="35.0" fill="var(--up)"/>
<line x1="808.7" y1="261.2" x2="808.7" y2="307.4" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="272.1" width="2.34" height="33.6" fill="var(--down)"/>
<line x1="812.5" y1="298.0" x2="812.5" y2="319.5" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="303.4" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="816.3" y1="248.2" x2="816.3" y2="329.7" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="273.8" width="2.34" height="45.3" fill="var(--up)"/>
<line x1="820.0" y1="203.5" x2="820.0" y2="272.0" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="211.9" width="2.34" height="57.5" fill="var(--up)"/>
<line x1="823.8" y1="179.5" x2="823.8" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="197.8" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="827.6" y1="142.0" x2="827.6" y2="220.3" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="163.6" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="831.3" y1="118.4" x2="831.3" y2="171.5" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="141.1" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="835.1" y1="73.8" x2="835.1" y2="158.8" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="118.2" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="838.9" y1="94.1" x2="838.9" y2="132.2" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="113.1" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="842.7" y1="104.4" x2="842.7" y2="134.7" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="115.8" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="846.4" y1="108.0" x2="846.4" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="119.2" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="850.2" y1="123.6" x2="850.2" y2="152.6" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="136.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="854.0" y1="122.1" x2="854.0" y2="164.6" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="145.7" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="857.7" y1="122.0" x2="857.7" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="141.9" width="2.34" height="235.3" fill="var(--down)"/>
<line x1="861.5" y1="279.9" x2="861.5" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="283.3" width="2.34" height="85.8" fill="var(--up)"/>
<line x1="865.3" y1="256.3" x2="865.3" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="290.7" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="869.1" y1="283.0" x2="869.1" y2="322.1" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="293.4" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="872.8" y1="287.5" x2="872.8" y2="361.4" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="314.9" width="2.34" height="44.4" fill="var(--down)"/>
<line x1="876.6" y1="335.2" x2="876.6" y2="368.5" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="345.1" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="880.4" y1="312.8" x2="880.4" y2="351.9" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="325.3" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="884.2" y1="310.3" x2="884.2" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="315.8" width="2.34" height="23.4" fill="var(--down)"/>
<line x1="887.9" y1="341.0" x2="887.9" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="341.9" width="2.34" height="78.3" fill="var(--down)"/>
<line x1="891.7" y1="406.4" x2="891.7" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="412.9" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="895.5" y1="404.0" x2="895.5" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="425.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="899.2" y1="386.1" x2="899.2" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="387.3" width="2.34" height="30.9" fill="var(--up)"/>
<line x1="903.0" y1="316.0" x2="903.0" y2="372.2" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="321.9" width="2.34" height="27.8" fill="var(--up)"/>
<line x1="906.8" y1="301.1" x2="906.8" y2="341.0" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="320.5" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="910.6" y1="316.6" x2="910.6" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="325.9" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="914.3" y1="298.9" x2="914.3" y2="320.5" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="308.0" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="918.1" y1="296.2" x2="918.1" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="303.6" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="921.9" y1="238.5" x2="921.9" y2="305.5" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="243.5" width="2.34" height="53.8" fill="var(--up)"/>
<line x1="925.6" y1="230.1" x2="925.6" y2="279.2" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="244.8" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="929.4" y1="243.1" x2="929.4" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="275.4" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="933.2" y1="256.1" x2="933.2" y2="326.6" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="277.4" width="2.34" height="46.7" fill="var(--down)"/>
<line x1="937.0" y1="315.9" x2="937.0" y2="403.8" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="330.0" width="2.34" height="45.3" fill="var(--down)"/>
<line x1="940.7" y1="341.7" x2="940.7" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="361.7" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="944.5" y1="343.8" x2="944.5" y2="394.9" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="357.8" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="948.3" y1="338.8" x2="948.3" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="372.0" width="2.34" height="20.6" fill="var(--down)"/>
<line x1="952.0" y1="347.4" x2="952.0" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="361.2" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="955.8" y1="356.5" x2="955.8" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="367.7" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="959.6" y1="363.5" x2="959.6" y2="387.8" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="384.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="963.4" y1="355.4" x2="963.4" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="370.9" width="2.34" height="66.7" fill="var(--down)"/>
<line x1="967.1" y1="406.8" x2="967.1" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="416.8" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="970.9" y1="391.1" x2="970.9" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="416.7" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="974.7" y1="332.3" x2="974.7" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="344.9" width="2.34" height="76.6" fill="var(--up)"/>
<line x1="978.4" y1="274.2" x2="978.4" y2="347.8" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="276.2" width="2.34" height="70.7" fill="var(--up)"/>
<line x1="982.2" y1="276.0" x2="982.2" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="281.4" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="986.0" y1="251.7" x2="986.0" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="255.2" width="2.34" height="30.4" fill="var(--up)"/>
<line x1="989.8" y1="250.9" x2="989.8" y2="289.3" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="258.7" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="993.5" y1="231.5" x2="993.5" y2="312.5" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="244.1" width="2.34" height="34.3" fill="var(--up)"/>
<line x1="997.3" y1="224.3" x2="997.3" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="237.1" width="2.34" height="72.9" fill="var(--down)"/>
<line x1="1001.1" y1="265.6" x2="1001.1" y2="332.9" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="298.7" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="1004.9" y1="294.0" x2="1004.9" y2="351.1" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="321.2" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="1008.6" y1="306.1" x2="1008.6" y2="351.3" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="327.9" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="1012.4" y1="304.4" x2="1012.4" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="336.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="1016.2" y1="325.0" x2="1016.2" y2="365.5" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="333.7" width="2.34" height="27.9" fill="var(--down)"/>
<line x1="1019.9" y1="342.2" x2="1019.9" y2="376.8" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="350.4" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="1023.7" y1="339.1" x2="1023.7" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="345.9" width="2.34" height="86.6" fill="var(--down)"/>
<line x1="1027.5" y1="423.4" x2="1027.5" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="435.6" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="1031.3" y1="408.4" x2="1031.3" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="426.5" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="1035.0" y1="389.4" x2="1035.0" y2="430.2" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="390.0" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="1038.8" y1="379.3" x2="1038.8" y2="408.5" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="382.6" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="1042.6" y1="376.8" x2="1042.6" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="387.8" width="2.34" height="26.5" fill="var(--down)"/>
<line x1="1046.3" y1="324.3" x2="1046.3" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="324.4" width="2.34" height="93.5" fill="var(--up)"/>
<line x1="1050.1" y1="324.3" x2="1050.1" y2="390.9" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="324.4" width="2.34" height="61.7" fill="var(--up)"/>
<line x1="60" y1="321.8" x2="1052" y2="321.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="325.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$467 R1</text>
<text x="1058" y="337.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="227.2" x2="1052" y2="227.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="230.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$537 R2</text>
<text x="1058" y="242.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="106.8" x2="1052" y2="106.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="110.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$627 R3</text>
<text x="1058" y="122.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="387.7" x2="1052" y2="387.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="381.7" font-size="11.5" fill="var(--support)" font-weight="600">$418 S1</text>
<text x="1058" y="393.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="439.8" x2="1052" y2="439.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="433.8" font-size="11.5" fill="var(--support)" font-weight="600">$379 S2</text>
<text x="1058" y="445.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="459.6" x2="1052" y2="459.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="453.6" font-size="11.5" fill="var(--support)" font-weight="600">$364 S3</text>
<text x="1058" y="465.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="324.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="316.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $465 (2026-08-27)</text>
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
| R3 | $627 | 2 | 2024-02-19 · 2024-07-08 주. **2024년 상반기 고점대**로, Ansys 인수 발표(2024-01) 이후 기대가 가장 컸던 구간이다. 현재가 대비 +34.9%로 근시일 저항이라기보다 이전 레짐의 천장에 가깝다 |
| R2 | $537 | 2 | 2026-01-12 · 2026-05-25 주. **2025-09 갭다운 이후 두 차례 반등이 모두 멈춘 자리** — 갭다운 후 형성된 밴드의 실질 상단이다 |
| R1 | $467 | 2 | 2023-05-29 · 2023-07-17 주. 2023년 상승 국면의 중간 밴드였던 자리가 **현재가($464.89)와 사실상 겹친다**(+0.5%) |
| **현재가** | **$464.89** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $418 | 2 | 2023-06-26 · 2023-08-14 주. R1과 같은 2023년 여름 박스의 하단 |
| S2 | $379 | 3 | 2025-09-08 · 2025-11-17 · 2026-03-23 주. **갭다운 주의 저가가 만든 대역**이며 이후 두 번 재확인됐다 |
| S3 | $364 | 3 | 2023-04-24 · 2025-04-07 · 2026-07-13 주. **3년에 걸쳐 세 번, 서로 다른 계기로 닿은 자리**(2023년 상승 초입 · 2025년 4월 관세 조정 · 2026-07-17 52주 최저)라 이 표에서 가장 오래 유지된 구조적 하단이다 |
| 참고선 | $652 | — | 5년 최고(2025년). **저항선으로 취급하지 않는다** — 2025-09-08 주 −28.9% 이후 이 대역과 현재 밴드 사이($540~$650)에 스윙 포인트가 거의 없어 연속적인 가격 기억이 없다 |
| 참고선 | $255 | — | 5년 최저(2022년 금리 인상기 조정). **지지선으로 취급하지 않는다** — 매출이 $5,000M 미만이던 시기의 가격으로, FY2026 가이던스 $9,715M인 현재 회사와 펀더멘털 기반이 다르다 |

---

## 3. 관측된 특이 구간

주봉 5년 구간에서 **가격 밴드 자체가 재설정된** 국면은 둘이다. 일봉 기준 단발 이벤트는 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3절에 있으므로 여기서는 다루지 않는다.

### 3-1. 2022~2023 — 저금리 조정 이후의 재평가

- 2022년 금리 인상 국면에서 $255.02(5년 최저)까지 밀렸다가, 2023년 들어 AI 반도체 설계 수요 기대가 반영되며 2023년 한 해에만 종가 기준 $319.29 → $514.91(+61.3%)로 올랐다.
- 이 상승으로 만들어진 2023년 여름 밴드($418~$467, 위 표 S1·R1)가 **3년이 지난 지금 현재가가 놓인 구간과 그대로 겹친다.** 즉 주가만 놓고 보면 2023년 중반 수준으로 되돌아온 상태다 — 같은 기간 매출은 FY2023 $5,318M → FY2026(E) $9,715M으로 늘었고, 그 괴리가 [밸류에이션 / 적정주가](./06_valuation.md)에서 배수 축소로 나타난다.

### 3-2. 2025-07 Ansys 인수 완료 → 2025-09 갭다운 — 레짐 전환

- 2025-07-17 Ansys 인수 완료(약 349억 달러)로 회사의 매출 규모·자본구조가 단절적으로 바뀌었고([역사 / 주요 이벤트](./02_history.md)), 두 달 뒤인 2025-09-08 주에 FY2025 Q3 실적 갭다운이 겹쳤다.
- 그 주 종가는 전주 대비 **−28.87%**($598.14 → $425.45). 이후 1년간 주봉 종가는 $364~$539 안에서만 움직였고, 갭다운 전 밴드($540~$650)로 복귀한 주는 한 번도 없다.
- **그래서 위 표의 R2($537)·S2($379)는 전적으로 갭다운 이후에 형성된 레벨이고, R3($627)·참고선($652)은 그 이전 레짐의 잔재다.** 5년 창 안에서 사업 구조 자체가 바뀐 사례이므로(사업부 매각 + 대형 인수) 2024년 이전 레벨을 현재 펀더멘털과 직접 연결하지 말 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-23~2026-08-27. 수집 시점: 2026-08-28. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py --interval 1wk` (`SNPS --name Synopsys --interval 1wk --event 2025-07-14:"Ansys 인수 완료" --event 2025-09-08:"FY2025 Q3 실적 갭다운" --ref-line 255.02:"5년 최저" --ref-line 651.73:"5년 최고" --close-on 2026-08-27 --emit all`)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨 개수·강제 포함은 없다** — 자동 기준(터치 2회 이상)으로 R3~S3 6개가 그대로 나왔다. 이벤트선의 날짜는 주봉이라 각 주의 시작일(월요일)로 지정했다(2025-07-14 = Ansys 인수 완료 2025-07-17이 속한 주, 2025-09-08 = 갭다운 2025-09-10이 속한 주).
    - **5년 창 안에서 회사가 두 번 바뀌었다.** Software Integrity 매각(2024-09)과 Ansys 인수(2025-07)로 매출 기반과 자본구조가 달라졌고, 회계상으로도 FY2024 이전 수치가 소급 재작성됐다([핵심 지표](./04_metrics.md) 상단 경고). **2024년 이전 가격 레벨은 지금과 다른 회사의 가격**이므로 R3·참고선 두 개는 표에서 참고 용도로만 처리했다.
    - 이 5년 안에 주식분할·병합은 없었다. 발행주식수는 Ansys 인수 신주 발행으로 FY2024 154.1백만 주 → FY2026 Q3 191.6백만 주로 늘었으나 **주가 시계열의 소급 조정 사유는 아니다.**

---

*작성일: 2026-08-28*
