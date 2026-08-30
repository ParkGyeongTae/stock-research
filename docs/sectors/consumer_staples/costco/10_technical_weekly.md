# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 최근 1년의 세부 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: 야후 파이낸스 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 마지막 봉의 종가 **$945.47(2026-08-28)**은 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준 주가와 **일치**한다. 일봉 문서만 야후 데이터 누락으로 2026-08-27($934.66)에서 끝난다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

<div class="cost-chart">
<style>
.cost-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .cost-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .cost-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cost-chart svg { width:100%; height:auto; display:block; }
.cost-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cost-chart .title { fill: var(--ink); font-weight:600; }
.cost-chart .grid { stroke: var(--grid); stroke-width:1; }
.cost-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Costco(COST) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Costco (COST) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $945.47 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="610.6" x2="1052" y2="610.6" class="grid"/>
<text x="52" y="614.6" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="533.6" x2="1052" y2="533.6" class="grid"/>
<text x="52" y="537.6" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="456.5" x2="1052" y2="456.5" class="grid"/>
<text x="52" y="460.5" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="379.5" x2="1052" y2="379.5" class="grid"/>
<text x="52" y="383.5" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="302.5" x2="1052" y2="302.5" class="grid"/>
<text x="52" y="306.5" font-size="11" text-anchor="end" fill="var(--muted)">800</text>
<line x1="60" y1="225.5" x2="1052" y2="225.5" class="grid"/>
<text x="52" y="229.5" font-size="11" text-anchor="end" fill="var(--muted)">900</text>
<line x1="60" y1="148.4" x2="1052" y2="148.4" class="grid"/>
<text x="52" y="152.4" font-size="11" text-anchor="end" fill="var(--muted)">1,000</text>
<line x1="60" y1="71.4" x2="1052" y2="71.4" class="grid"/>
<text x="52" y="75.4" font-size="11" text-anchor="end" fill="var(--muted)">1,100</text>
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
<line x1="61.9" y1="561.6" x2="61.9" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="562.4" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="65.7" y1="556.9" x2="65.7" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="560.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="69.5" y1="558.0" x2="69.5" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="558.9" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="73.3" y1="557.7" x2="73.3" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="558.4" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="77.0" y1="556.3" x2="77.0" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="560.1" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="80.8" y1="564.7" x2="80.8" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="570.7" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="84.6" y1="569.0" x2="84.6" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="570.2" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="88.4" y1="545.1" x2="88.4" y2="573.2" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="547.4" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="92.2" y1="538.1" x2="92.2" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="540.1" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="96.0" y1="518.0" x2="96.0" y2="543.4" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="523.5" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="99.8" y1="518.4" x2="99.8" y2="533.4" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="520.3" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="103.5" y1="506.4" x2="103.5" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="507.5" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="107.3" y1="491.5" x2="107.3" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="498.0" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="111.1" y1="486.8" x2="111.1" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="498.0" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="114.9" y1="486.4" x2="114.9" y2="515.2" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="488.3" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="118.7" y1="482.3" x2="118.7" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="494.7" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="122.5" y1="493.0" x2="122.5" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="494.8" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="126.3" y1="478.5" x2="126.3" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="481.4" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="130.0" y1="480.6" x2="130.0" y2="507.2" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="483.5" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="133.8" y1="510.1" x2="133.8" y2="532.1" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="511.0" width="2.35" height="20.3" fill="var(--down)"/>
<line x1="137.6" y1="533.7" x2="137.6" y2="548.0" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="537.8" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="141.4" y1="536.8" x2="141.4" y2="557.4" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="539.4" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="145.2" y1="513.2" x2="145.2" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="518.3" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="149.0" y1="507.2" x2="149.0" y2="527.9" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="517.2" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="152.8" y1="519.5" x2="152.8" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="523.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="156.5" y1="519.5" x2="156.5" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="520.1" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="160.3" y1="503.6" x2="160.3" y2="524.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="513.9" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="164.1" y1="498.7" x2="164.1" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="512.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="167.9" y1="485.4" x2="167.9" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="486.3" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="171.7" y1="482.2" x2="171.7" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="487.2" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="175.5" y1="467.1" x2="175.5" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="475.4" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="179.3" y1="447.1" x2="179.3" y2="479.4" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="456.5" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="183.1" y1="455.8" x2="183.1" y2="472.9" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="457.5" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="186.8" y1="449.5" x2="186.8" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="467.8" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="190.6" y1="479.4" x2="190.6" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="479.4" width="2.35" height="29.7" fill="var(--down)"/>
<line x1="194.4" y1="498.0" x2="194.4" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="508.7" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="198.2" y1="525.4" x2="198.2" y2="549.2" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="535.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="202.0" y1="535.4" x2="202.0" y2="605.6" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="536.5" width="2.35" height="61.4" fill="var(--down)"/>
<line x1="205.8" y1="552.9" x2="205.8" y2="597.8" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="556.1" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="209.6" y1="540.4" x2="209.6" y2="566.9" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="551.9" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="213.3" y1="545.7" x2="213.3" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="548.6" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="217.1" y1="561.0" x2="217.1" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="572.1" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="220.9" y1="545.3" x2="220.9" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="545.6" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="224.7" y1="540.3" x2="224.7" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="544.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="228.5" y1="529.3" x2="228.5" y2="550.2" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="532.4" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="232.3" y1="514.5" x2="232.3" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="515.9" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="236.1" y1="505.0" x2="236.1" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="510.7" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="239.8" y1="501.1" x2="239.8" y2="526.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="501.8" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="243.6" y1="493.0" x2="243.6" y2="507.9" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="501.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="247.4" y1="495.1" x2="247.4" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="499.8" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="251.2" y1="483.7" x2="251.2" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="491.6" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="255.0" y1="492.7" x2="255.0" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="492.7" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="258.8" y1="505.8" x2="258.8" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="512.7" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="262.6" y1="504.3" x2="262.6" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="505.4" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="266.4" y1="500.8" x2="266.4" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="504.5" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="270.1" y1="528.4" x2="270.1" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="531.9" width="2.35" height="27.5" fill="var(--down)"/>
<line x1="273.9" y1="540.1" x2="273.9" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="554.9" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="277.7" y1="538.3" x2="277.7" y2="559.7" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="553.2" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="281.5" y1="549.2" x2="281.5" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="556.9" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="285.3" y1="549.3" x2="285.3" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="550.4" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="289.1" y1="523.7" x2="289.1" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="525.2" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="292.9" y1="526.1" x2="292.9" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="526.1" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="296.6" y1="520.6" x2="296.6" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="521.7" width="2.35" height="29.6" fill="var(--up)"/>
<line x1="300.4" y1="510.6" x2="300.4" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="515.3" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="304.2" y1="505.2" x2="304.2" y2="516.6" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="507.6" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="308.0" y1="500.8" x2="308.0" y2="539.6" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="509.8" width="2.35" height="28.0" fill="var(--down)"/>
<line x1="311.8" y1="539.2" x2="311.8" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="539.3" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="315.6" y1="535.1" x2="315.6" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="546.9" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="319.4" y1="561.5" x2="319.4" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="562.3" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="323.1" y1="560.8" x2="323.1" y2="571.5" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="561.0" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="326.9" y1="545.6" x2="326.9" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="546.8" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="330.7" y1="543.7" x2="330.7" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="544.9" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="334.5" y1="540.9" x2="334.5" y2="558.2" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="545.0" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="338.3" y1="526.6" x2="338.3" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="531.0" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="342.1" y1="510.4" x2="342.1" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="522.2" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="345.9" y1="519.7" x2="345.9" y2="537.1" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="522.4" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="349.6" y1="524.8" x2="349.6" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="527.8" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="353.4" y1="529.4" x2="353.4" y2="545.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="532.9" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="357.2" y1="539.0" x2="357.2" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="539.3" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="361.0" y1="537.3" x2="361.0" y2="557.9" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="551.7" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="364.8" y1="541.3" x2="364.8" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="543.5" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="368.6" y1="536.2" x2="368.6" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="537.2" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="372.4" y1="533.7" x2="372.4" y2="544.8" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="535.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="376.2" y1="530.4" x2="376.2" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="536.3" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="379.9" y1="533.3" x2="379.9" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="540.3" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="383.7" y1="525.4" x2="383.7" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="528.7" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="387.5" y1="523.5" x2="387.5" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="528.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="391.3" y1="533.5" x2="391.3" y2="544.4" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="534.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="395.1" y1="528.9" x2="395.1" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="530.4" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="398.9" y1="529.7" x2="398.9" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="530.5" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="402.7" y1="525.3" x2="402.7" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="528.0" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="406.4" y1="519.3" x2="406.4" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="523.9" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="410.2" y1="516.6" x2="410.2" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="520.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="414.0" y1="509.5" x2="414.0" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="515.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="417.8" y1="514.0" x2="417.8" y2="520.8" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="514.7" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="421.6" y1="503.1" x2="421.6" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="504.0" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="425.4" y1="498.1" x2="425.4" y2="514.6" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="504.9" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="429.2" y1="497.5" x2="429.2" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="497.6" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="432.9" y1="485.8" x2="432.9" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="489.0" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="436.7" y1="478.8" x2="436.7" y2="490.5" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="484.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="440.5" y1="484.0" x2="440.5" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="485.0" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="444.3" y1="480.3" x2="444.3" y2="493.6" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="485.1" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="448.1" y1="481.4" x2="448.1" y2="500.4" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="483.7" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="451.9" y1="498.8" x2="451.9" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="499.8" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="455.7" y1="492.4" x2="455.7" y2="508.1" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="499.5" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="459.5" y1="493.2" x2="459.5" y2="502.6" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="494.1" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="463.2" y1="482.2" x2="463.2" y2="493.6" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="490.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="467.0" y1="480.2" x2="467.0" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="488.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="470.8" y1="478.0" x2="470.8" y2="499.1" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="483.5" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="474.6" y1="474.9" x2="474.6" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="481.3" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="478.4" y1="480.3" x2="478.4" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="482.1" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="482.2" y1="474.0" x2="482.2" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="479.9" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="486.0" y1="489.7" x2="486.0" y2="502.6" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="491.9" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="489.7" y1="485.0" x2="489.7" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="486.7" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="493.5" y1="473.6" x2="493.5" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="474.2" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="497.3" y1="456.6" x2="497.3" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="474.1" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="501.1" y1="461.0" x2="501.1" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="463.2" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="504.9" y1="456.6" x2="504.9" y2="469.8" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="459.4" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="508.7" y1="446.1" x2="508.7" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="448.2" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="512.5" y1="408.9" x2="512.5" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="411.2" width="2.35" height="28.4" fill="var(--up)"/>
<line x1="516.2" y1="393.4" x2="516.2" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="401.4" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="520.0" y1="398.1" x2="520.0" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="400.3" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="523.8" y1="410.6" x2="523.8" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="413.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="527.6" y1="392.1" x2="527.6" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="392.4" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="531.4" y1="382.5" x2="531.4" y2="396.3" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="383.4" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="535.2" y1="380.5" x2="535.2" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="383.0" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="539.0" y1="368.5" x2="539.0" y2="390.1" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="372.2" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="542.7" y1="357.8" x2="542.7" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="361.5" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="546.5" y1="357.1" x2="546.5" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="361.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="550.3" y1="346.8" x2="550.3" y2="363.9" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="350.3" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="554.1" y1="339.0" x2="554.1" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="341.4" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="557.9" y1="312.4" x2="557.9" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="337.1" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="561.7" y1="348.2" x2="561.7" y2="371.0" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="359.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="565.5" y1="339.2" x2="565.5" y2="359.5" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="352.7" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="569.3" y1="351.9" x2="569.3" y2="358.9" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="354.4" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="573.0" y1="353.9" x2="573.0" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="355.0" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="576.8" y1="353.5" x2="576.8" y2="374.1" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="355.4" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="580.6" y1="347.9" x2="580.6" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="352.2" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="584.4" y1="355.7" x2="584.4" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="357.0" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="588.2" y1="342.9" x2="588.2" y2="367.7" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="345.7" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="592.0" y1="312.2" x2="592.0" y2="343.7" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="312.4" width="2.35" height="29.0" fill="var(--up)"/>
<line x1="595.8" y1="299.0" x2="595.8" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="305.7" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="599.5" y1="289.5" x2="599.5" y2="308.6" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="295.0" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="603.3" y1="287.5" x2="603.3" y2="311.6" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="294.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="607.1" y1="263.7" x2="607.1" y2="297.0" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="267.4" width="2.35" height="26.6" fill="var(--up)"/>
<line x1="610.9" y1="259.2" x2="610.9" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="259.6" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="614.7" y1="245.5" x2="614.7" y2="265.8" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="260.5" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="618.5" y1="256.5" x2="618.5" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="264.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="622.3" y1="235.5" x2="622.3" y2="271.3" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="236.5" width="2.35" height="24.8" fill="var(--up)"/>
<line x1="626.0" y1="228.0" x2="626.0" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="235.6" width="2.35" height="33.8" fill="var(--down)"/>
<line x1="629.8" y1="257.9" x2="629.8" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="266.4" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="633.6" y1="260.4" x2="633.6" y2="295.5" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="267.2" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="637.4" y1="279.2" x2="637.4" y2="300.0" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="285.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="641.2" y1="258.0" x2="641.2" y2="307.9" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="260.2" width="2.35" height="43.9" fill="var(--up)"/>
<line x1="645.0" y1="240.6" x2="645.0" y2="262.1" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="248.1" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="648.8" y1="232.3" x2="648.8" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="241.5" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="652.5" y1="210.9" x2="652.5" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="231.3" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="656.3" y1="227.9" x2="656.3" y2="249.6" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="228.0" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="660.1" y1="207.1" x2="660.1" y2="242.5" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="213.1" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="663.9" y1="208.0" x2="663.9" y2="232.4" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="208.5" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="667.7" y1="210.4" x2="667.7" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="220.1" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="671.5" y1="217.8" x2="671.5" y2="250.8" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="232.1" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="675.3" y1="217.8" x2="675.3" y2="246.8" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="233.9" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="679.1" y1="225.0" x2="679.1" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="231.3" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="682.8" y1="221.1" x2="682.8" y2="238.0" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="232.2" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="686.6" y1="228.5" x2="686.6" y2="250.6" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="228.5" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="690.4" y1="177.7" x2="690.4" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="191.7" width="2.35" height="48.1" fill="var(--up)"/>
<line x1="694.2" y1="186.0" x2="694.2" y2="221.2" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="191.7" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="698.0" y1="166.7" x2="698.0" y2="220.0" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="176.2" width="2.35" height="41.1" fill="var(--up)"/>
<line x1="701.8" y1="167.7" x2="701.8" y2="187.2" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="167.7" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="705.6" y1="150.2" x2="705.6" y2="175.6" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="154.1" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="709.3" y1="142.4" x2="709.3" y2="174.8" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="150.7" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="713.1" y1="142.1" x2="713.1" y2="192.3" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="156.9" width="2.35" height="26.9" fill="var(--down)"/>
<line x1="716.9" y1="179.7" x2="716.9" y2="200.8" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="184.0" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="720.7" y1="199.1" x2="720.7" y2="223.9" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="201.6" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="724.5" y1="191.4" x2="724.5" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="197.0" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="728.3" y1="191.7" x2="728.3" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="192.2" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="732.1" y1="181.9" x2="732.1" y2="199.6" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="190.6" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="735.8" y1="155.4" x2="735.8" y2="204.5" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="163.9" width="2.35" height="38.4" fill="var(--up)"/>
<line x1="739.6" y1="99.9" x2="739.6" y2="172.4" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="114.7" width="2.35" height="55.0" fill="var(--up)"/>
<line x1="743.4" y1="88.2" x2="743.4" y2="113.0" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="93.1" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="747.2" y1="93.7" x2="747.2" y2="129.4" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="95.1" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="751.0" y1="103.1" x2="751.0" y2="133.9" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="111.0" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="754.8" y1="97.6" x2="754.8" y2="192.5" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="108.6" width="2.35" height="67.3" fill="var(--down)"/>
<line x1="758.6" y1="179.5" x2="758.6" y2="239.7" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="182.7" width="2.35" height="39.7" fill="var(--down)"/>
<line x1="762.4" y1="207.4" x2="762.4" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="218.3" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="766.1" y1="192.4" x2="766.1" y2="210.1" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="202.6" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="769.9" y1="152.3" x2="769.9" y2="214.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="208.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="773.7" y1="153.5" x2="773.7" y2="247.3" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="176.6" width="2.35" height="58.3" fill="var(--up)"/>
<line x1="777.5" y1="148.5" x2="777.5" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="152.7" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="781.3" y1="150.8" x2="781.3" y2="192.4" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="153.8" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="785.1" y1="134.6" x2="785.1" y2="172.5" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="142.0" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="788.9" y1="134.7" x2="788.9" y2="155.1" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="142.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="792.6" y1="126.7" x2="792.6" y2="161.5" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="128.5" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="796.4" y1="118.0" x2="796.4" y2="143.0" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="134.1" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="800.2" y1="108.0" x2="800.2" y2="146.9" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="117.5" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="804.0" y1="96.8" x2="804.0" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="122.0" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="807.8" y1="138.1" x2="807.8" y2="157.2" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="138.9" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="811.6" y1="147.0" x2="811.6" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="154.3" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="815.4" y1="143.9" x2="815.4" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="159.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="819.1" y1="150.9" x2="819.1" y2="168.1" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="158.4" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="822.9" y1="151.6" x2="822.9" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="160.0" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="826.7" y1="162.7" x2="826.7" y2="188.9" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="170.7" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="830.5" y1="181.0" x2="830.5" y2="199.7" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="185.8" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="834.3" y1="181.8" x2="834.3" y2="206.2" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="185.0" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="838.1" y1="157.5" x2="838.1" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="163.1" width="2.35" height="21.9" fill="var(--up)"/>
<line x1="841.9" y1="154.8" x2="841.9" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="161.4" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="845.6" y1="149.0" x2="845.6" y2="184.6" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="169.0" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="849.4" y1="180.6" x2="849.4" y2="199.8" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="183.1" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="853.2" y1="171.9" x2="853.2" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="176.6" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="857.0" y1="163.1" x2="857.0" y2="183.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="173.2" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="860.8" y1="171.7" x2="860.8" y2="191.7" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="173.2" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="864.6" y1="184.1" x2="864.6" y2="221.6" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="189.0" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="868.4" y1="202.0" x2="868.4" y2="222.9" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="212.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="872.2" y1="190.5" x2="872.2" y2="222.5" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="202.3" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="875.9" y1="176.2" x2="875.9" y2="209.2" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="197.5" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="879.7" y1="184.6" x2="879.7" y2="202.2" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="197.6" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="883.5" y1="199.9" x2="883.5" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="202.2" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="887.3" y1="190.6" x2="887.3" y2="219.1" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="207.9" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="891.1" y1="203.2" x2="891.1" y2="218.5" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="207.8" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="894.9" y1="206.3" x2="894.9" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="208.5" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="898.7" y1="214.5" x2="898.7" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="215.0" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="902.4" y1="205.2" x2="902.4" y2="234.6" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="215.3" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="906.2" y1="230.1" x2="906.2" y2="250.8" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="230.5" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="910.0" y1="235.1" x2="910.0" y2="268.5" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="239.2" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="913.8" y1="242.7" x2="913.8" y2="266.4" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="246.0" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="917.6" y1="245.1" x2="917.6" y2="262.0" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="246.0" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="921.4" y1="201.1" x2="921.4" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="206.3" width="2.35" height="46.9" fill="var(--up)"/>
<line x1="925.2" y1="175.4" x2="925.2" y2="212.4" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="176.5" width="2.35" height="33.3" fill="var(--up)"/>
<line x1="928.9" y1="156.4" x2="928.9" y2="183.8" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="161.3" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="932.7" y1="153.8" x2="932.7" y2="202.1" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="158.9" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="936.5" y1="147.4" x2="936.5" y2="201.4" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="147.5" width="2.35" height="43.9" fill="var(--up)"/>
<line x1="940.3" y1="130.8" x2="940.3" y2="173.8" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="134.2" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="944.1" y1="126.5" x2="944.1" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="131.2" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="947.9" y1="137.5" x2="947.9" y2="165.3" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="140.1" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="951.7" y1="132.4" x2="951.7" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="140.0" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="955.5" y1="138.5" x2="955.5" y2="160.8" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="141.9" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="959.2" y1="138.7" x2="959.2" y2="171.2" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="140.3" width="2.35" height="29.4" fill="var(--down)"/>
<line x1="963.0" y1="158.3" x2="963.0" y2="178.5" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="159.5" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="966.8" y1="136.1" x2="966.8" y2="160.0" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="136.9" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="970.6" y1="120.8" x2="970.6" y2="151.9" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="136.9" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="974.4" y1="147.9" x2="974.4" y2="174.6" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="148.5" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="978.2" y1="135.6" x2="978.2" y2="158.7" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="139.8" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="982.0" y1="124.3" x2="982.0" y2="159.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="139.4" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="985.7" y1="129.4" x2="985.7" y2="155.6" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="141.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="989.5" y1="104.1" x2="989.5" y2="159.9" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="110.7" width="2.35" height="33.2" fill="var(--up)"/>
<line x1="993.3" y1="74.1" x2="993.3" y2="129.0" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="109.9" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="997.1" y1="127.2" x2="997.1" y2="190.5" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="128.3" width="2.35" height="53.8" fill="var(--down)"/>
<line x1="1000.9" y1="150.4" x2="1000.9" y2="197.3" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="170.1" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="1004.7" y1="156.8" x2="1004.7" y2="178.5" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="162.0" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="1008.5" y1="152.0" x2="1008.5" y2="188.2" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="168.3" width="2.35" height="17.5" fill="var(--down)"/>
<line x1="1012.2" y1="173.1" x2="1012.2" y2="195.7" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="185.0" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="1016.0" y1="171.6" x2="1016.0" y2="209.6" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="180.4" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="1019.8" y1="172.3" x2="1019.8" y2="219.9" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="187.6" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="1023.6" y1="175.9" x2="1023.6" y2="217.4" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="194.0" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="1027.4" y1="189.3" x2="1027.4" y2="212.5" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="195.6" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="1031.2" y1="158.0" x2="1031.2" y2="197.2" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="185.5" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="1035.0" y1="173.1" x2="1035.0" y2="198.3" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="175.3" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="1038.7" y1="175.1" x2="1038.7" y2="198.5" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="178.4" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="1042.5" y1="164.8" x2="1042.5" y2="205.6" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="183.2" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="1046.3" y1="168.1" x2="1046.3" y2="199.8" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="184.6" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="1050.1" y1="184.1" x2="1050.1" y2="196.9" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="190.4" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="60" y1="149.7" x2="1052" y2="149.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="153.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$998 R1</text>
<text x="1058" y="165.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="123.7" x2="1052" y2="123.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="127.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,032 R2</text>
<text x="1058" y="139.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="86.3" x2="1052" y2="86.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="89.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,081 R3</text>
<text x="1058" y="101.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="218.2" x2="1052" y2="218.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="212.2" font-size="11.5" fill="var(--support)" font-weight="600">$909 S1</text>
<text x="1058" y="224.2" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="249.0" x2="1052" y2="249.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="243.0" font-size="11.5" fill="var(--support)" font-weight="600">$869 S2</text>
<text x="1058" y="255.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="506.3" x2="1052" y2="506.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="500.3" font-size="11.5" fill="var(--support)" font-weight="600">$535 S3</text>
<text x="1058" y="512.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="190.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="182.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $945 (2026-08-28)</text>
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
| R3 | $1,081 | 3 | 2025-02·2025-06·2026-05 고점대 — 5년 내 최고 구간(사상 최고 $1,096.50 포함) |
| R2 | $1,032 | 2 | 2026-02~04 고점대(2026-02-16·04-06) |
| R1 | $998 | 3 | 2024-12·2025-08·2026-07 고점대(2024-12-16·2025-08-18·2026-07-27). 현재가 바로 위 5.6%p |
| **현재가** | **$945.47** (2026-08-28 종가) | — | R1과 S1 사이 |
| S1 | $909 | 4 | 2024-12~2026-07에 걸친 최다 터치 지지대(2024-12-30·2025-07-28·2025-09-29·2026-07-06) |
| S2 | $869 | 2 | 2024-09·2025-04 저점대(2024-09-30·2025-04-07) |
| S3 | $535 | 2 | 2023-08·2023-10 저점대(2023-08-21·2023-10-23). **아래 3절의 재평가 이전 가격대**로 근시일 지지로 보지 않는다 |
| 참고선 | $406.51 | — | 최근 5년 최저가(2022-05). 아래 3절의 재평가 이전 가격대라 근시일 지지로 보지 않는다 |

**현재가 $945.47은 S1($909)과 R1($998) 사이에 있고, 5년 구조상 상단부에 위치한다.** 5년 최저 $406.51 대비 2.3배, 5년 최고 $1,096.50 대비 −13.8% 지점이다. 아래쪽 레벨 중 S1($909)·S2($869)는 2024년 이후 형성된 것이지만 **S3($535)는 2023년 하반기 가격대로, 지금과는 다른 밸류에이션 레짐에 속한다**(아래 3절).

---

## 3. 관측된 특이 구간 — 2023-10 ~ 2024-12 배수 재평가

- 단일 이벤트로 인한 갭이 아니라 **약 14개월에 걸친 밸류에이션 재평가 구간**이다. 주가는 2023-10 저점대 $535 부근에서 2024-12 고점대 $998 부근까지 약 **+87%** 올랐다.
- 같은 기간 이익 성장은 그 절반에도 못 미쳤다. [핵심 지표](./04_metrics.md) A.2에 따르면 GAAP PER은 FY2023 말 **38.4배**에서 FY2024 말 **53.9배**로 뛰었고 EPS는 $14.16 → $16.56(+16.9%)에 그쳤다 — **상승의 대부분이 이익이 아니라 배수에서 나왔다.**
- 그래서 S3($535)와 5년 최저 $406.51은 **지지선으로 읽지 않는다.** 이 가격대는 시장이 코스트코에 지금과 다른 배수를 매기던 시기의 흔적이며, 여기까지 되돌아가려면 배수가 FY2023 이전 수준으로 회귀해야 한다. 반대로 이 재평가가 유지된다는 가정이 [밸류에이션 / 적정주가](./06_valuation.md)의 목표 PER 48배에 그대로 들어가 있고, 그 신뢰도를 Low로 둔 이유이기도 하다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py COST --name "Costco" --interval 1wk --close-on 2026-08-27 --emit all` (재현용. 주봉은 주 단위 집계라 마지막 봉이 2026-08-28로 마감된다)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 재평가 구간이 레벨 해석을 갈라놓는다.** S1·S2는 재평가 이후(2024~2026) 형성된 레벨이라 현재 레짐 안의 지지로 읽을 수 있지만, S3와 5년 최저는 재평가 이전 가격대라 같은 의미를 갖지 않는다.
    - 코스트코는 2000-01 이후 주식분할이 없어 소급조정 이슈가 없다. 다만 위 데이터는 **원주가(배당 미반영)**이므로, 이 기간 21회 지급된 배당(정규 분기배당 + 2024-01 특별배당 $15.00)만큼 총수익률과는 차이가 난다 — **특히 특별배당은 배당락일에 주가를 그만큼 떨어뜨리므로, 2024-01 부근의 하락 폭 일부는 가격 하락이 아니라 배당락이다.**

---

*작성일: 2026-08-30*
