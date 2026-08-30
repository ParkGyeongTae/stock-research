# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉으로 본 다년 가격 구조. 최근 1년의 세부 레벨은 [기술적 분석 — 일봉](./09_technical_daily.md)을 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 마지막 종가 **$103.09 (2026-08-28)**는 [밸류에이션 / 적정주가](./06_valuation.md)와 [핵심 지표](./04_metrics.md)가 쓰는 기준 종가와 **일치**한다. [일봉 차트](./09_technical_daily.md)는 시계열이 하루 짧아 $102.63(2026-08-27)에서 끝난다.
    - **분할 소급 조정**: 기간 내 **2024-02-26 3:1 분할**이 있었고, 차트의 과거 가격은 모두 분할 후 기준으로 소급 조정돼 있다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

<div class="wmt-chart">
<style>
.wmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.wmt-chart svg { width:100%; height:auto; display:block; }
.wmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.wmt-chart .title { fill: var(--ink); font-weight:600; }
.wmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.wmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Walmart(WMT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Walmart (WMT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $103.09 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="604.1" x2="1052" y2="604.1" class="grid"/>
<text x="52" y="608.1" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="494.5" x2="1052" y2="494.5" class="grid"/>
<text x="52" y="498.5" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="384.8" x2="1052" y2="384.8" class="grid"/>
<text x="52" y="388.8" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="275.2" x2="1052" y2="275.2" class="grid"/>
<text x="52" y="279.2" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="165.6" x2="1052" y2="165.6" class="grid"/>
<text x="52" y="169.6" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
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
<line x1="61.9" y1="549.9" x2="61.9" y2="556.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="550.6" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="65.7" y1="550.8" x2="65.7" y2="557.6" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="551.2" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="69.5" y1="554.5" x2="69.5" y2="560.8" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="555.6" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="73.3" y1="558.1" x2="73.3" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="561.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="77.0" y1="561.1" x2="77.0" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="562.3" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="80.8" y1="566.3" x2="80.8" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="568.2" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="84.6" y1="565.5" x2="84.6" y2="571.0" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="566.5" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="88.4" y1="549.8" x2="88.4" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="552.3" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="92.2" y1="548.3" x2="92.2" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="550.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="96.0" y1="545.6" x2="96.0" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="548.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="99.8" y1="548.3" x2="99.8" y2="553.8" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="548.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="103.5" y1="552.1" x2="103.5" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="552.6" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="107.3" y1="553.1" x2="107.3" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="558.6" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="111.1" y1="557.9" x2="111.1" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="558.4" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="114.9" y1="565.2" x2="114.9" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="565.7" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="118.7" y1="555.6" x2="118.7" y2="570.5" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="567.1" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="122.5" y1="567.2" x2="122.5" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="568.5" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="126.3" y1="558.3" x2="126.3" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="559.0" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="130.0" y1="556.7" x2="130.0" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="558.6" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="133.8" y1="555.4" x2="133.8" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="557.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="137.6" y1="558.4" x2="137.6" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="559.5" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="141.4" y1="566.6" x2="141.4" y2="578.6" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="569.2" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="145.2" y1="563.9" x2="145.2" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="568.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="149.0" y1="567.4" x2="149.0" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="567.4" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="152.8" y1="568.3" x2="152.8" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="571.2" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="156.5" y1="570.8" x2="156.5" y2="582.1" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="571.6" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="160.3" y1="562.2" x2="160.3" y2="578.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="562.4" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="164.1" y1="560.1" x2="164.1" y2="570.9" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="563.8" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="167.9" y1="554.9" x2="167.9" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="557.6" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="171.7" y1="554.2" x2="171.7" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="557.6" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="175.5" y1="546.9" x2="175.5" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="547.4" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="179.3" y1="533.9" x2="179.3" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="535.7" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="183.1" y1="534.1" x2="183.1" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="536.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="186.8" y1="529.6" x2="186.8" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="536.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="190.6" y1="534.4" x2="190.6" y2="544.3" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="537.6" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="194.4" y1="540.2" x2="194.4" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="540.2" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="198.2" y1="543.6" x2="198.2" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="552.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="202.0" y1="549.8" x2="202.0" y2="609.1" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="550.4" width="2.35" height="55.1" fill="var(--down)"/>
<line x1="205.8" y1="588.3" x2="205.8" y2="604.3" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="588.6" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="209.6" y1="586.0" x2="209.6" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="590.4" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="213.3" y1="592.6" x2="213.3" y2="605.3" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="593.4" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="217.1" y1="600.9" x2="217.1" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="604.6" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="220.9" y1="594.4" x2="220.9" y2="607.3" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="597.3" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="224.7" y1="593.9" x2="224.7" y2="604.3" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="597.2" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="228.5" y1="592.0" x2="228.5" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="594.2" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="232.3" y1="585.3" x2="232.3" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="587.5" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="236.1" y1="579.6" x2="236.1" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="581.8" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="239.8" y1="580.9" x2="239.8" y2="604.0" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="581.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="243.6" y1="578.1" x2="243.6" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="583.9" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="247.4" y1="580.6" x2="247.4" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="581.8" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="251.2" y1="562.6" x2="251.2" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="573.0" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="255.0" y1="573.3" x2="255.0" y2="583.0" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="574.5" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="258.8" y1="575.4" x2="258.8" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="580.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="262.6" y1="572.1" x2="262.6" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="573.3" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="266.4" y1="570.7" x2="266.4" y2="583.5" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="572.9" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="270.1" y1="572.2" x2="270.1" y2="588.1" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="580.7" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="273.9" y1="578.3" x2="273.9" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="586.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="277.7" y1="576.3" x2="277.7" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="585.4" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="281.5" y1="577.1" x2="281.5" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="585.0" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="285.3" y1="572.3" x2="285.3" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="573.4" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="289.1" y1="562.2" x2="289.1" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="563.0" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="292.9" y1="561.0" x2="292.9" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="563.3" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="296.6" y1="560.1" x2="296.6" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="562.8" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="300.4" y1="548.8" x2="300.4" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="548.8" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="304.2" y1="543.1" x2="304.2" y2="548.9" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="543.7" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="308.0" y1="540.8" x2="308.0" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="543.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="311.8" y1="543.8" x2="311.8" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="544.2" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="315.6" y1="548.9" x2="315.6" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="556.8" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="319.4" y1="556.7" x2="319.4" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="560.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="323.1" y1="559.4" x2="323.1" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="560.2" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="326.9" y1="553.7" x2="326.9" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="555.2" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="330.7" y1="553.2" x2="330.7" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="556.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="334.5" y1="557.1" x2="334.5" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="557.9" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="338.3" y1="555.6" x2="338.3" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="561.5" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="342.1" y1="557.3" x2="342.1" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="563.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="345.9" y1="560.3" x2="345.9" y2="569.9" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="560.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="349.6" y1="554.5" x2="349.6" y2="559.9" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="555.8" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="353.4" y1="552.3" x2="353.4" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="562.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="561.9" x2="357.2" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="562.6" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="361.0" y1="564.5" x2="361.0" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="566.6" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="364.8" y1="567.9" x2="364.8" y2="573.8" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="568.6" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="368.6" y1="563.0" x2="368.6" y2="568.5" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="564.3" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="372.4" y1="552.1" x2="372.4" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="553.9" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="376.2" y1="547.4" x2="376.2" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="547.8" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="379.9" y1="547.2" x2="379.9" y2="552.6" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="548.6" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="383.7" y1="545.1" x2="383.7" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="546.1" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="387.5" y1="542.4" x2="387.5" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="546.1" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="391.3" y1="544.6" x2="391.3" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="546.0" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="395.1" y1="541.3" x2="395.1" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="543.7" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="398.9" y1="541.4" x2="398.9" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="542.9" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="402.7" y1="549.1" x2="402.7" y2="558.2" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="549.8" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="406.4" y1="551.1" x2="406.4" y2="558.4" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="551.4" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="410.2" y1="542.5" x2="410.2" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="543.6" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="414.0" y1="534.2" x2="414.0" y2="543.5" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="539.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="417.8" y1="537.8" x2="417.8" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="539.3" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="421.6" y1="535.5" x2="421.6" y2="543.5" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="536.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="425.4" y1="532.6" x2="425.4" y2="543.0" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="536.8" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="429.2" y1="538.5" x2="429.2" y2="542.7" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="540.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="432.9" y1="533.2" x2="432.9" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="534.0" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="436.7" y1="529.3" x2="436.7" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="531.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="440.5" y1="529.8" x2="440.5" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="531.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="444.3" y1="527.2" x2="444.3" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="528.8" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="448.1" y1="525.9" x2="448.1" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="527.3" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="451.9" y1="532.4" x2="451.9" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="535.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="455.7" y1="525.5" x2="455.7" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="528.1" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="459.5" y1="523.9" x2="459.5" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="524.1" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="463.2" y1="520.3" x2="463.2" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="522.5" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="467.0" y1="521.5" x2="467.0" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="522.4" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="470.8" y1="524.5" x2="470.8" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="526.7" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="474.6" y1="529.1" x2="474.6" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="531.9" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="478.4" y1="530.2" x2="478.4" y2="543.3" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="531.3" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="482.2" y1="526.7" x2="482.2" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="530.0" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="486.0" y1="523.1" x2="486.0" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="528.9" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="489.7" y1="519.5" x2="489.7" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="522.5" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="493.5" y1="518.9" x2="493.5" y2="525.1" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="519.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="497.3" y1="512.8" x2="497.3" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="519.3" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="501.1" y1="536.8" x2="501.1" y2="541.7" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="538.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="504.9" y1="533.0" x2="504.9" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="538.4" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="508.7" y1="538.6" x2="508.7" y2="548.8" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="543.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="512.5" y1="541.9" x2="512.5" y2="550.1" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="544.3" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="516.2" y1="536.2" x2="516.2" y2="543.6" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="537.1" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="520.0" y1="534.1" x2="520.0" y2="538.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="535.3" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="523.8" y1="530.5" x2="523.8" y2="539.0" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="536.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="527.6" y1="527.5" x2="527.6" y2="537.1" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="528.6" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="531.4" y1="524.5" x2="531.4" y2="529.8" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="526.7" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="535.2" y1="523.0" x2="535.2" y2="530.4" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="523.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="539.0" y1="511.7" x2="539.0" y2="524.6" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="513.5" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="542.7" y1="511.5" x2="542.7" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="512.7" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="546.5" y1="509.2" x2="546.5" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="512.1" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="550.3" y1="492.0" x2="550.3" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="497.2" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="554.1" y1="495.3" x2="554.1" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="499.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="557.9" y1="488.6" x2="557.9" y2="503.2" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="493.8" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="561.7" y1="485.9" x2="561.7" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="490.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="565.5" y1="485.4" x2="565.5" y2="492.3" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="489.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="569.3" y1="488.7" x2="569.3" y2="493.6" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="489.7" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="573.0" y1="490.3" x2="573.0" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="492.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="576.8" y1="489.6" x2="576.8" y2="498.3" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="493.7" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="580.6" y1="490.6" x2="580.6" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="491.7" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="584.4" y1="491.6" x2="584.4" y2="502.4" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="493.6" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="588.2" y1="492.3" x2="588.2" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="493.5" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="592.0" y1="489.8" x2="592.0" y2="497.8" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="491.8" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="595.8" y1="467.7" x2="595.8" y2="497.5" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="469.0" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="599.5" y1="463.3" x2="599.5" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="465.0" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="603.3" y1="462.1" x2="603.3" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="462.9" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="607.1" y1="453.0" x2="607.1" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="462.2" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="610.9" y1="454.3" x2="610.9" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="455.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="614.7" y1="447.6" x2="614.7" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="451.1" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="618.5" y1="444.9" x2="618.5" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="450.3" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="622.3" y1="438.8" x2="622.3" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="439.4" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="626.0" y1="437.2" x2="626.0" y2="444.2" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="440.2" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="629.8" y1="432.4" x2="629.8" y2="443.5" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="435.5" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="633.6" y1="432.7" x2="633.6" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="434.9" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="637.4" y1="438.3" x2="637.4" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="440.5" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="641.2" y1="447.2" x2="641.2" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="450.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="645.0" y1="415.3" x2="645.0" y2="455.3" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="420.7" width="2.35" height="28.0" fill="var(--up)"/>
<line x1="648.8" y1="405.6" x2="648.8" y2="421.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="408.4" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="652.5" y1="398.7" x2="652.5" y2="409.1" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="400.0" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="656.3" y1="396.8" x2="656.3" y2="405.1" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="399.5" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="660.1" y1="381.1" x2="660.1" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="381.6" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="663.9" y1="379.3" x2="663.9" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="380.2" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="667.7" y1="376.1" x2="667.7" y2="389.9" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="386.1" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="671.5" y1="376.5" x2="671.5" y2="385.7" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="379.7" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="675.3" y1="379.7" x2="675.3" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="381.1" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="679.1" y1="374.9" x2="679.1" y2="386.2" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="377.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="682.8" y1="366.5" x2="682.8" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="371.1" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="686.6" y1="368.0" x2="686.6" y2="378.2" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="369.8" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="690.4" y1="354.5" x2="690.4" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="358.4" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="694.2" y1="353.1" x2="694.2" y2="363.3" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="357.7" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="698.0" y1="325.1" x2="698.0" y2="364.8" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="327.6" width="2.35" height="30.8" fill="var(--up)"/>
<line x1="701.8" y1="315.6" x2="701.8" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="316.3" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="705.6" y1="296.2" x2="705.6" y2="319.4" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="298.8" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="709.3" y1="297.5" x2="709.3" y2="313.4" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="299.0" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="713.1" y1="297.7" x2="713.1" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="305.8" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="716.9" y1="314.3" x2="716.9" y2="336.0" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="320.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="720.7" y1="322.9" x2="720.7" y2="332.7" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="325.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="724.5" y1="310.4" x2="724.5" y2="327.6" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="313.6" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="728.3" y1="316.7" x2="728.3" y2="329.4" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="318.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="732.1" y1="302.6" x2="732.1" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="303.9" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="735.8" y1="280.7" x2="735.8" y2="303.6" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="285.3" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="739.6" y1="258.2" x2="739.6" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="268.9" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="743.4" y1="246.2" x2="743.4" y2="268.4" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="253.1" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="747.2" y1="252.2" x2="747.2" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="254.8" width="2.35" height="49.0" fill="var(--down)"/>
<line x1="751.0" y1="281.5" x2="751.0" y2="318.4" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="282.8" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="754.8" y1="278.0" x2="754.8" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="286.3" width="2.35" height="34.3" fill="var(--down)"/>
<line x1="758.6" y1="328.8" x2="758.6" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="331.4" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="762.4" y1="341.1" x2="762.4" y2="358.6" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="352.1" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="766.1" y1="342.9" x2="766.1" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="349.4" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="769.9" y1="329.2" x2="769.9" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="358.8" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="773.7" y1="311.7" x2="773.7" y2="385.9" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="314.7" width="2.35" height="68.8" fill="var(--up)"/>
<line x1="777.5" y1="297.0" x2="777.5" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="312.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="781.3" y1="293.9" x2="781.3" y2="322.7" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="302.1" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="785.1" y1="279.5" x2="785.1" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="282.1" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="788.9" y1="276.7" x2="788.9" y2="295.6" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="281.0" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="792.6" y1="279.7" x2="792.6" y2="319.7" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="284.9" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="796.4" y1="281.7" x2="796.4" y2="302.6" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="293.6" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="800.2" y1="281.1" x2="800.2" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="282.2" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="804.0" y1="270.4" x2="804.0" y2="291.8" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="281.6" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="807.8" y1="285.7" x2="807.8" y2="311.2" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="289.5" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="811.6" y1="295.5" x2="811.6" y2="310.2" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="296.5" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="815.4" y1="280.1" x2="815.4" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="290.2" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="819.1" y1="279.7" x2="819.1" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="284.2" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="822.9" y1="278.8" x2="822.9" y2="306.9" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="284.9" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="826.7" y1="298.0" x2="826.7" y2="306.0" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="302.4" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="830.5" y1="288.1" x2="830.5" y2="302.1" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="289.1" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="834.3" y1="281.4" x2="834.3" y2="291.2" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="283.5" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="838.1" y1="249.4" x2="838.1" y2="285.1" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="254.8" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="841.9" y1="251.5" x2="841.9" y2="277.8" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="253.9" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="845.6" y1="260.7" x2="845.6" y2="293.0" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="275.2" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="849.4" y1="288.5" x2="849.4" y2="300.3" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="291.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="853.2" y1="267.1" x2="853.2" y2="294.4" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="272.4" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="857.0" y1="253.4" x2="857.0" y2="273.7" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="256.1" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="860.8" y1="241.7" x2="860.8" y2="263.8" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="255.2" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="864.6" y1="256.0" x2="864.6" y2="267.9" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="257.9" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="868.4" y1="253.6" x2="868.4" y2="275.9" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="258.5" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="872.2" y1="255.3" x2="872.2" y2="273.2" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="264.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="875.9" y1="222.7" x2="875.9" y2="269.4" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="232.9" width="2.35" height="34.9" fill="var(--up)"/>
<line x1="879.7" y1="230.0" x2="879.7" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="232.2" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="883.5" y1="240.4" x2="883.5" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="240.5" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="887.3" y1="259.0" x2="887.3" y2="275.1" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="261.0" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="891.1" y1="253.7" x2="891.1" y2="281.4" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="261.6" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="894.9" y1="230.6" x2="894.9" y2="277.0" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="246.1" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="898.7" y1="216.6" x2="898.7" y2="254.6" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="217.6" width="2.35" height="28.2" fill="var(--up)"/>
<line x1="902.4" y1="186.1" x2="902.4" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="192.4" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="906.2" y1="182.3" x2="906.2" y2="207.8" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="183.7" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="910.0" y1="179.6" x2="910.0" y2="201.1" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="182.4" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="913.8" y1="196.7" x2="913.8" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="198.4" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="917.6" y1="205.1" x2="917.6" y2="214.3" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="205.3" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="921.4" y1="190.5" x2="921.4" y2="221.5" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="195.6" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="925.2" y1="158.8" x2="925.2" y2="185.3" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="167.3" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="928.9" y1="156.7" x2="928.9" y2="181.3" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="160.7" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="932.7" y1="168.8" x2="932.7" y2="190.4" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="170.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="936.5" y1="101.5" x2="936.5" y2="170.8" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="104.3" width="2.35" height="64.0" fill="var(--up)"/>
<line x1="940.3" y1="85.3" x2="940.3" y2="130.6" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="89.5" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="944.1" y1="85.1" x2="944.1" y2="159.9" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="93.8" width="2.35" height="55.5" fill="var(--down)"/>
<line x1="947.9" y1="118.5" x2="947.9" y2="149.4" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="122.0" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="951.7" y1="117.7" x2="951.7" y2="156.7" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="124.7" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="955.5" y1="128.9" x2="955.5" y2="153.1" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="129.9" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="959.2" y1="126.2" x2="959.2" y2="176.5" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="128.6" width="2.35" height="42.4" fill="var(--down)"/>
<line x1="963.0" y1="142.2" x2="963.0" y2="170.8" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="149.8" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="966.8" y1="133.3" x2="966.8" y2="150.1" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="133.9" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="970.6" y1="112.5" x2="970.6" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="128.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="974.4" y1="124.1" x2="974.4" y2="151.6" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="124.5" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="978.2" y1="97.3" x2="978.2" y2="125.5" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="111.2" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="982.0" y1="92.3" x2="982.0" y2="133.2" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="102.0" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="985.7" y1="101.2" x2="985.7" y2="118.1" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="108.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="989.5" y1="89.2" x2="989.5" y2="130.6" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="102.9" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="993.3" y1="82.5" x2="993.3" y2="171.6" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="102.5" width="2.35" height="61.7" fill="var(--down)"/>
<line x1="997.1" y1="159.9" x2="997.1" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="161.8" width="2.35" height="27.1" fill="var(--down)"/>
<line x1="1000.9" y1="160.7" x2="1000.9" y2="205.5" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="171.8" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="1004.7" y1="155.4" x2="1004.7" y2="179.2" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="159.9" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="1008.5" y1="149.5" x2="1008.5" y2="183.2" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="167.0" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="1012.2" y1="163.4" x2="1012.2" y2="192.5" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="182.3" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="1016.0" y1="183.2" x2="1016.0" y2="235.5" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="185.0" width="2.35" height="25.4" fill="var(--down)"/>
<line x1="1019.8" y1="197.6" x2="1019.8" y2="223.9" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="199.0" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="1023.6" y1="176.1" x2="1023.6" y2="209.1" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="194.5" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="1027.4" y1="196.3" x2="1027.4" y2="238.0" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="198.7" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="1031.2" y1="187.4" x2="1031.2" y2="221.0" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="213.8" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="1035.0" y1="195.4" x2="1035.0" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="203.4" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="1038.7" y1="185.1" x2="1038.7" y2="216.3" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="191.5" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="1042.5" y1="182.8" x2="1042.5" y2="263.4" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="196.7" width="2.35" height="58.3" fill="var(--down)"/>
<line x1="1046.3" y1="239.1" x2="1046.3" y2="262.8" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="252.5" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="1050.1" y1="256.6" x2="1050.1" y2="261.5" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="258.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="60" y1="247.8" x2="1052" y2="247.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="251.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$105 R1</text>
<text x="1058" y="263.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="83.8" x2="1052" y2="83.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="87.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$135 R2</text>
<text x="1058" y="99.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="548.2" x2="1052" y2="548.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="542.2" font-size="11.5" fill="var(--support)" font-weight="600">$50 S1</text>
<text x="1058" y="554.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="577.6" x2="1052" y2="577.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="571.6" font-size="11.5" fill="var(--support)" font-weight="600">$45 S2</text>
<text x="1058" y="583.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="258.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="250.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $103 (2026-08-28)</text>
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
| R2 | $135 | 2 | 2026-02-16·2026-05-18 — 사상 최고가대($135.16). FY2026 실적 발표 직후와 Q1 FY2027 기대 국면에서 두 번 닿고 두 번 다 되밀렸다 |
| R1 | $105 | 2 | 2025-02-10·2025-08-04 — 재평가가 진행되던 구간의 중간 고점대. **8월 급락으로 현재가가 이 레벨 아래로 내려왔다** |
| **현재가** | **$103.09** (2026-08-28 종가) | — | R1 바로 아래. 아래쪽 클러스터(S1 $50)와는 51% 떨어져 있다 |
| S1 | $50 | 2 | 2023-10-02·2023-12-11 — **재평가 이전 가격대**. 현재가 대비 −51%로 근시일 지지로 볼 수 없다 |
| S2 | $45 | 4 | 2021-10-04·2021-11-29·2022-02-21·2023-03-06 — 5년 중 가장 두꺼운 클러스터지만 2021~2023년 구간이다. 현재가 대비 −56% |
| 참고선 | $39.09 | — | 최근 5년 최저(2022년) |

**이 표에서 읽을 것은 지지선이 아니라 "지지선이 없다"는 사실이다.** 5년 스윙 저점 클러스터는 전부 $45~$50, 즉 **2023년 이전 재평가 이전 가격대**에 몰려 있다. 2024년 이후 주가가 $55 → $135로 오르는 동안 의미 있는 조정이 없었기 때문에 그 구간에는 스윙 저점 자체가 만들어지지 않았다. 현재가 아래 51% 구간이 가격 기억의 공백이며, 근시일 지지는 이 문서가 아니라 [일봉 문서](./09_technical_daily.md)의 S1($100)에서 봐야 한다.

---

## 3. 관측된 특이 구간 — 2024년 이후의 단절적 재평가

- 2021-08~2024-01의 약 2년 반 동안 주가는 $45~$55 박스에 머물렀고, 그 구간에 5년 스윙 저점 6개 중 6개가 모두 들어 있다.
- 2024년부터 2026년 5월까지 주가는 $55 → $135.16으로 **2.5배** 올랐다. 같은 기간 Non-GAAP PER은 24.8배 → 45.1배로 확대됐고, 조정 EPS는 $2.22 → $2.64(+19%)에 그쳤다 — 상승의 대부분이 이익이 아니라 배수였다([밸류에이션 / 적정주가 2. 최근 3개년](./06_valuation.md) 참고).
- 이 구간에는 조정다운 조정이 없었다. 그 결과 **$55~$135 사이 80달러 구간 전체에 스윙 저점 클러스터가 하나도 없다.** 차트에서 이 구간은 지지가 촘촘한 것이 아니라 검증된 적이 없는 것이다.
- 2024-02-26에 3:1 주식분할이 있었고, 위 가격은 모두 소급 조정 후 기준이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, **배당은 미반영** — 기간 내 배당 20회 지급)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py WMT --name Walmart --interval 1wk --close-on 2026-08-28 --emit all` (기본 파라미터, `--force-level`·`--ref-line` 미사용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨이 4개(R2·R1·S1·S2)로 나왔고 그중 지지 2개가 현재가 대비 −51~−56%에 있다.** 3절에서 설명한 대로 2024~2026년 상승 구간에 조정이 없어 스윙 저점이 만들어지지 않았기 때문이며, 이 문서의 지지선은 근시일 매매 준거로 쓸 수 없다.
    - **기간 내 2024-02-26 3:1 주식분할**이 있었고 과거 가격은 소급 조정됐다. 분할 자체는 가격 연속성을 깨지 않는다.
    - 배당이 미반영된 원주가이므로, 5년 총수익률은 이 차트의 가격 변화율보다 높다.

---

*작성일: 2026-08-30*
