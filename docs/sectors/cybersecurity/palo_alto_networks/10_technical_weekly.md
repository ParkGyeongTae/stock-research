# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API에서 직접 수집한 것이다(5년 주봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 대신 **두 문서에서 겹치는 시점의 종가를 반드시 대조하고 그 결과를 여기 적을 것** — `2026-08-14` 종가 `$384.27`은 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 stockanalysis.com 값과 일치 확인함.

> ⚠️ 상장 후 거래 기간이 2년 미만이거나 유동성이 극히 얕은 종목은 스윙 클러스터가 표본 부족으로 무의미해진다 — 그럴 땐 이 문서를 만들지 말거나, 기간을 실제 거래 구간으로 줄이고 4. 방법론 · 한계에 그 사실을 남길 것. 기술적 분석 — 일봉·1년(일봉·1년)만으로 충분한 경우 이 문서 자체를 생략해도 된다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="panw-chart">
<style>
.panw-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .panw-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .panw-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.panw-chart svg { width:100%; height:auto; display:block; }
.panw-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.panw-chart .title { fill: var(--ink); font-weight:600; }
.panw-chart .grid { stroke: var(--grid); stroke-width:1; }
.panw-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Palo Alto Networks(PANW) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Palo Alto Networks (PANW) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $384.27 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="618.2" x2="1052" y2="618.2" class="grid"/>
<text x="52" y="622.2" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="540.1" x2="1052" y2="540.1" class="grid"/>
<text x="52" y="544.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="462.0" x2="1052" y2="462.0" class="grid"/>
<text x="52" y="466.0" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="383.9" x2="1052" y2="383.9" class="grid"/>
<text x="52" y="387.9" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="305.9" x2="1052" y2="305.9" class="grid"/>
<text x="52" y="309.9" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="227.8" x2="1052" y2="227.8" class="grid"/>
<text x="52" y="231.8" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="149.7" x2="1052" y2="149.7" class="grid"/>
<text x="52" y="153.7" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="71.6" x2="1052" y2="71.6" class="grid"/>
<text x="52" y="75.6" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.6" y1="626.0" x2="137.6" y2="631.0" class="axis"/>
<text x="137.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="334.5" y1="626.0" x2="334.5" y2="631.0" class="axis"/>
<text x="334.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="531.4" y1="626.0" x2="531.4" y2="631.0" class="axis"/>
<text x="531.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="732.1" y1="626.0" x2="732.1" y2="631.0" class="axis"/>
<text x="732.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.9" y1="626.0" x2="928.9" y2="631.0" class="axis"/>
<text x="928.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="720.7" y1="56.0" x2="720.7" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="726.7" y="68.0" font-size="10.5" fill="var(--down)">2024-12-16 2:1 주식분할</text>
<line x1="61.9" y1="598.3" x2="61.9" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="599.3" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="65.7" y1="575.7" x2="65.7" y2="600.7" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="576.2" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="69.5" y1="574.4" x2="69.5" y2="577.9" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="574.4" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="73.3" y1="571.6" x2="73.3" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="573.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="77.0" y1="567.2" x2="77.0" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="572.3" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="80.8" y1="568.5" x2="80.8" y2="574.4" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="568.6" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="84.6" y1="569.1" x2="84.6" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="569.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="88.4" y1="565.6" x2="88.4" y2="575.7" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="568.0" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="92.2" y1="562.5" x2="92.2" y2="569.2" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="564.1" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="96.0" y1="561.1" x2="96.0" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="563.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="99.8" y1="562.9" x2="99.8" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="563.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="103.5" y1="562.7" x2="103.5" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="563.4" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="107.3" y1="560.0" x2="107.3" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="562.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="111.1" y1="554.2" x2="111.1" y2="565.2" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="558.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="114.9" y1="550.6" x2="114.9" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="557.5" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="118.7" y1="551.0" x2="118.7" y2="561.3" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="555.7" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="122.5" y1="555.9" x2="122.5" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="557.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="126.3" y1="555.0" x2="126.3" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="555.7" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="130.0" y1="548.7" x2="130.0" y2="561.6" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="550.1" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="133.8" y1="547.2" x2="133.8" y2="552.2" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="549.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="137.6" y1="550.4" x2="137.6" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="550.9" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="141.4" y1="556.3" x2="141.4" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="562.5" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="145.2" y1="556.5" x2="145.2" y2="570.7" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="568.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="149.0" y1="563.7" x2="149.0" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="567.1" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="152.8" y1="560.9" x2="152.8" y2="569.3" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="562.1" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="156.5" y1="556.3" x2="156.5" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="562.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="160.3" y1="556.9" x2="160.3" y2="571.0" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="564.6" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="164.1" y1="547.7" x2="164.1" y2="574.9" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="548.0" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="167.9" y1="540.4" x2="167.9" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="546.1" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="171.7" y1="549.7" x2="171.7" y2="560.4" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="550.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="175.5" y1="546.0" x2="175.5" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="546.1" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="179.3" y1="533.7" x2="179.3" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="534.3" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="183.1" y1="530.8" x2="183.1" y2="541.0" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="535.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="186.8" y1="532.0" x2="186.8" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="535.9" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="190.6" y1="530.8" x2="190.6" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="533.1" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="194.4" y1="529.5" x2="194.4" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="534.6" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="198.2" y1="539.9" x2="198.2" y2="551.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="547.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="202.0" y1="547.2" x2="202.0" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="551.0" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="205.8" y1="566.2" x2="205.8" y2="579.1" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="568.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="209.6" y1="565.0" x2="209.6" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="568.3" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="213.3" y1="561.7" x2="213.3" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="564.4" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="217.1" y1="560.2" x2="217.1" y2="567.3" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="562.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="220.9" y1="557.1" x2="220.9" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="561.9" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="224.7" y1="567.2" x2="224.7" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="572.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="228.5" y1="562.3" x2="228.5" y2="570.8" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="563.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="232.3" y1="562.3" x2="232.3" y2="570.8" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="562.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="236.1" y1="559.5" x2="236.1" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="559.8" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="239.8" y1="559.2" x2="239.8" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="561.3" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="243.6" y1="559.9" x2="243.6" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="562.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="247.4" y1="562.5" x2="247.4" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="563.0" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="251.2" y1="558.2" x2="251.2" y2="570.3" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="565.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="255.0" y1="556.5" x2="255.0" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="559.1" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="258.8" y1="558.5" x2="258.8" y2="564.4" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="560.8" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="262.6" y1="545.6" x2="262.6" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="550.3" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="266.4" y1="547.1" x2="266.4" y2="557.2" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="551.8" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="270.1" y1="548.4" x2="270.1" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="549.3" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="273.9" y1="547.9" x2="273.9" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="548.9" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="277.7" y1="557.7" x2="277.7" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="562.6" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="281.5" y1="565.2" x2="281.5" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="568.4" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="285.3" y1="556.5" x2="285.3" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="563.6" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="289.1" y1="563.2" x2="289.1" y2="580.7" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="563.9" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="292.9" y1="566.0" x2="292.9" y2="574.2" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="569.8" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="296.6" y1="562.4" x2="296.6" y2="573.4" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="562.7" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="300.4" y1="558.8" x2="300.4" y2="586.9" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="563.3" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="304.2" y1="565.0" x2="304.2" y2="586.6" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="567.2" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="308.0" y1="561.2" x2="308.0" y2="578.0" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="565.5" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="311.8" y1="559.1" x2="311.8" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="561.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="315.6" y1="556.5" x2="315.6" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="561.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="319.4" y1="561.0" x2="319.4" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="561.7" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="323.1" y1="564.3" x2="323.1" y2="578.9" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="571.8" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="326.9" y1="577.5" x2="326.9" y2="586.5" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="577.7" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="330.7" y1="585.7" x2="330.7" y2="589.5" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="586.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="334.5" y1="584.3" x2="334.5" y2="592.7" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="585.9" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="338.3" y1="587.2" x2="338.3" y2="593.0" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="587.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="342.1" y1="581.9" x2="342.1" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="582.2" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="345.9" y1="570.4" x2="345.9" y2="582.2" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="571.5" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="349.6" y1="566.9" x2="349.6" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="571.6" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="353.4" y1="564.3" x2="353.4" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="567.2" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="357.2" y1="557.6" x2="357.2" y2="567.9" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="564.1" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="361.0" y1="548.7" x2="361.0" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="550.5" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="364.8" y1="545.7" x2="364.8" y2="551.4" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="546.7" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="368.6" y1="547.6" x2="368.6" y2="553.8" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="549.7" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="372.4" y1="546.8" x2="372.4" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="548.6" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="376.2" y1="543.1" x2="376.2" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="546.7" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="379.9" y1="539.9" x2="379.9" y2="548.0" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="540.3" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="383.7" y1="541.0" x2="383.7" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="541.7" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="387.5" y1="540.2" x2="387.5" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="540.5" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="391.3" y1="537.4" x2="391.3" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="540.1" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="395.1" y1="544.2" x2="395.1" y2="554.9" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="545.5" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="398.9" y1="551.6" x2="398.9" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="552.7" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="402.7" y1="538.9" x2="402.7" y2="549.5" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="540.7" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="406.4" y1="541.2" x2="406.4" y2="550.5" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="541.4" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="410.2" y1="526.8" x2="410.2" y2="549.2" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="531.0" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="414.0" y1="524.5" x2="414.0" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="526.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="516.5" x2="417.8" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="519.4" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="421.6" y1="502.9" x2="421.6" y2="524.1" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="503.8" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="425.4" y1="501.6" x2="425.4" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="505.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="429.2" y1="495.7" x2="429.2" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="496.8" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="432.9" y1="494.1" x2="432.9" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="497.1" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="436.7" y1="499.6" x2="436.7" y2="515.3" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="501.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="440.5" y1="500.5" x2="440.5" y2="508.1" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="505.9" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="444.3" y1="501.2" x2="444.3" y2="509.8" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="502.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="448.1" y1="497.9" x2="448.1" y2="529.7" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="501.1" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="451.9" y1="524.1" x2="451.9" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="525.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="455.7" y1="523.1" x2="455.7" y2="539.2" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="525.7" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="459.5" y1="504.0" x2="459.5" y2="519.6" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="511.6" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="463.2" y1="505.2" x2="463.2" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="506.8" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="467.0" y1="501.2" x2="467.0" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="502.1" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="470.8" y1="497.8" x2="470.8" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="501.1" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="474.6" y1="506.3" x2="474.6" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="508.6" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="478.4" y1="510.2" x2="478.4" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="513.2" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="482.2" y1="501.1" x2="482.2" y2="516.6" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="503.7" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="486.0" y1="488.7" x2="486.0" y2="504.3" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="493.7" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="489.7" y1="488.7" x2="489.7" y2="508.7" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="493.5" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="493.5" y1="497.7" x2="493.5" y2="512.0" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="507.9" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="497.3" y1="499.4" x2="497.3" y2="510.7" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="506.1" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="501.1" y1="498.0" x2="501.1" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="498.3" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="504.9" y1="489.6" x2="504.9" y2="513.4" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="497.7" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="508.7" y1="486.9" x2="508.7" y2="501.4" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="488.5" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="512.5" y1="464.5" x2="512.5" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="465.0" width="2.35" height="23.5" fill="var(--up)"/>
<line x1="516.2" y1="462.9" x2="516.2" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="463.3" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="520.0" y1="448.0" x2="520.0" y2="465.7" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="456.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="523.8" y1="453.5" x2="523.8" y2="465.2" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="458.7" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="527.6" y1="460.5" x2="527.6" y2="468.3" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="462.9" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="531.4" y1="468.2" x2="531.4" y2="476.2" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="468.3" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="535.2" y1="438.3" x2="535.2" y2="474.9" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="442.3" width="2.35" height="32.6" fill="var(--up)"/>
<line x1="539.0" y1="430.5" x2="539.0" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="432.6" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="542.7" y1="422.5" x2="542.7" y2="433.5" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="425.9" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="546.5" y1="424.8" x2="546.5" y2="436.5" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="426.8" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="550.3" y1="398.9" x2="550.3" y2="433.9" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="402.0" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="554.1" y1="402.5" x2="554.1" y2="420.0" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="403.1" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="557.9" y1="407.9" x2="557.9" y2="493.2" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="413.0" width="2.35" height="63.1" fill="var(--down)"/>
<line x1="561.7" y1="440.5" x2="561.7" y2="472.3" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="460.2" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="565.5" y1="460.2" x2="565.5" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="460.5" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="569.3" y1="467.7" x2="569.3" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="476.0" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="573.0" y1="469.1" x2="573.0" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="472.3" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="576.8" y1="469.1" x2="576.8" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="473.3" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="580.6" y1="473.2" x2="580.6" y2="489.4" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="473.7" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="584.4" y1="473.4" x2="584.4" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="478.4" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="588.2" y1="473.8" x2="588.2" y2="485.2" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="478.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="592.0" y1="465.9" x2="592.0" y2="481.4" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="468.7" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="595.8" y1="459.0" x2="595.8" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="463.6" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="599.5" y1="455.3" x2="599.5" y2="465.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="462.8" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="603.3" y1="447.2" x2="603.3" y2="463.2" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="448.1" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="607.1" y1="442.8" x2="607.1" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="445.2" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="610.9" y1="445.0" x2="610.9" y2="472.5" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="446.3" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="614.7" y1="459.7" x2="614.7" y2="470.7" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="460.5" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="618.5" y1="442.9" x2="618.5" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="448.5" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="622.3" y1="445.3" x2="622.3" y2="454.8" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="446.2" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="626.0" y1="426.2" x2="626.0" y2="449.7" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="431.6" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="629.8" y1="426.5" x2="629.8" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="429.2" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="633.6" y1="429.3" x2="633.6" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="430.7" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="637.4" y1="427.9" x2="637.4" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="436.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="641.2" y1="430.1" x2="641.2" y2="447.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="435.1" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="645.0" y1="439.6" x2="645.0" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="440.6" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="648.8" y1="436.2" x2="648.8" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="437.4" width="2.35" height="34.6" fill="var(--up)"/>
<line x1="652.5" y1="426.3" x2="652.5" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="435.4" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="656.3" y1="403.2" x2="656.3" y2="434.6" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="422.4" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="660.1" y1="410.5" x2="660.1" y2="428.2" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="413.1" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="663.9" y1="410.9" x2="663.9" y2="435.6" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="415.5" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="667.7" y1="421.0" x2="667.7" y2="436.5" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="425.4" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="671.5" y1="423.6" x2="671.5" y2="439.6" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="425.7" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="675.3" y1="426.2" x2="675.3" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="431.1" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="679.1" y1="428.1" x2="679.1" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="429.0" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="682.8" y1="400.9" x2="682.8" y2="433.3" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="404.9" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="686.6" y1="399.8" x2="686.6" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="401.9" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="690.4" y1="396.4" x2="690.4" y2="417.1" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="403.5" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="694.2" y1="407.9" x2="694.2" y2="417.4" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="408.9" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="698.0" y1="389.2" x2="698.0" y2="418.3" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="390.7" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="701.8" y1="377.3" x2="701.8" y2="395.2" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="387.3" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="705.6" y1="380.8" x2="705.6" y2="403.3" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="389.4" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="709.3" y1="386.1" x2="709.3" y2="397.4" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="393.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="713.1" y1="376.8" x2="713.1" y2="394.5" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="379.3" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="716.9" y1="376.0" x2="716.9" y2="393.5" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="378.5" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="720.7" y1="372.6" x2="720.7" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="386.8" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="724.5" y1="400.3" x2="724.5" y2="410.2" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="403.8" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="728.3" y1="406.1" x2="728.3" y2="417.0" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="409.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="732.1" y1="410.8" x2="732.1" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="411.5" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="735.8" y1="413.1" x2="735.8" y2="436.7" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="419.7" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="739.6" y1="398.1" x2="739.6" y2="414.4" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="403.2" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="743.4" y1="387.5" x2="743.4" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="407.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="747.2" y1="387.6" x2="747.2" y2="415.0" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="393.4" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="751.0" y1="380.2" x2="751.0" y2="401.5" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="383.9" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="754.8" y1="370.8" x2="754.8" y2="399.2" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="387.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="758.6" y1="394.3" x2="758.6" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="397.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="762.4" y1="393.8" x2="762.4" y2="424.7" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="397.2" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="766.1" y1="408.7" x2="766.1" y2="426.7" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="411.5" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="769.9" y1="400.1" x2="769.9" y2="415.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="409.7" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="773.7" y1="398.0" x2="773.7" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="405.8" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="777.5" y1="423.4" x2="777.5" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="431.5" width="2.35" height="25.0" fill="var(--down)"/>
<line x1="781.3" y1="424.4" x2="781.3" y2="471.2" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="433.4" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="785.1" y1="423.1" x2="785.1" y2="435.3" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="428.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="788.9" y1="416.0" x2="788.9" y2="450.2" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="416.8" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="792.6" y1="396.9" x2="792.6" y2="418.2" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="403.2" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="796.4" y1="398.0" x2="796.4" y2="408.4" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="404.4" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="800.2" y1="391.1" x2="800.2" y2="400.5" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="394.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="804.0" y1="391.9" x2="804.0" y2="417.3" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="398.8" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="807.8" y1="395.3" x2="807.8" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="395.8" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="811.6" y1="382.6" x2="811.6" y2="397.3" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="384.6" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="815.4" y1="384.0" x2="815.4" y2="393.9" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="385.4" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="819.1" y1="379.4" x2="819.1" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="385.1" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="822.9" y1="373.4" x2="822.9" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="383.1" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="826.7" y1="376.3" x2="826.7" y2="391.9" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="381.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="830.5" y1="374.3" x2="830.5" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="382.6" width="2.35" height="21.1" fill="var(--down)"/>
<line x1="834.3" y1="387.7" x2="834.3" y2="405.8" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="390.5" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="838.1" y1="375.7" x2="838.1" y2="392.4" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="378.8" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="841.9" y1="367.7" x2="841.9" y2="433.4" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="378.1" width="2.35" height="48.2" fill="var(--down)"/>
<line x1="845.6" y1="423.8" x2="845.6" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="423.8" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="849.4" y1="414.6" x2="849.4" y2="436.7" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="419.7" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="853.2" y1="401.1" x2="853.2" y2="423.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="406.0" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="857.0" y1="395.2" x2="857.0" y2="412.2" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="398.7" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="860.8" y1="389.7" x2="860.8" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="392.6" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="864.6" y1="379.7" x2="864.6" y2="392.1" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="389.7" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="868.4" y1="369.9" x2="868.4" y2="388.1" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="371.2" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="872.2" y1="369.1" x2="872.2" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="373.2" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="875.9" y1="365.0" x2="875.9" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="372.7" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="879.7" y1="355.9" x2="879.7" y2="371.0" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="369.3" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="883.5" y1="361.0" x2="883.5" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="363.0" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="887.3" y1="355.5" x2="887.3" y2="369.1" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="357.2" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="891.1" y1="347.1" x2="891.1" y2="359.0" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="352.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="894.9" y1="352.0" x2="894.9" y2="372.5" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="352.8" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="898.7" y1="352.7" x2="898.7" y2="386.4" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="361.7" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="902.4" y1="372.7" x2="902.4" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="376.1" width="2.35" height="34.5" fill="var(--down)"/>
<line x1="906.2" y1="398.1" x2="906.2" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="399.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="910.0" y1="384.4" x2="910.0" y2="406.4" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="385.8" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="913.8" y1="384.1" x2="913.8" y2="401.9" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="384.9" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="917.6" y1="397.5" x2="917.6" y2="410.2" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="397.5" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="921.4" y1="398.7" x2="921.4" y2="407.7" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="401.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="925.2" y1="401.1" x2="925.2" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="402.5" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="928.9" y1="389.9" x2="928.9" y2="413.6" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="401.1" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="932.7" y1="393.2" x2="932.7" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="402.2" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="936.5" y1="401.9" x2="936.5" y2="417.1" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="408.6" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="940.3" y1="400.5" x2="940.3" y2="428.8" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="413.0" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="944.1" y1="418.7" x2="944.1" y2="459.4" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="419.2" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="947.9" y1="430.0" x2="947.9" y2="452.1" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="435.6" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="951.7" y1="437.0" x2="951.7" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="437.5" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="955.5" y1="460.0" x2="955.5" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="463.7" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="959.2" y1="438.0" x2="959.2" y2="468.3" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="438.5" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="963.0" y1="429.0" x2="963.0" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="435.4" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="966.8" y1="427.6" x2="966.8" y2="443.5" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="434.3" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="970.6" y1="436.5" x2="970.6" y2="472.2" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="439.5" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="974.4" y1="441.2" x2="974.4" y2="459.7" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="441.4" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="978.2" y1="416.3" x2="978.2" y2="460.0" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="441.1" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="982.0" y1="429.8" x2="982.0" y2="454.5" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="434.2" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="985.7" y1="412.8" x2="985.7" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="417.5" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="989.5" y1="405.8" x2="989.5" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="413.5" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="993.3" y1="371.3" x2="993.3" y2="416.4" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="371.6" width="2.35" height="41.0" fill="var(--up)"/>
<line x1="997.1" y1="312.4" x2="997.1" y2="375.1" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="317.1" width="2.35" height="54.7" fill="var(--up)"/>
<line x1="1000.9" y1="288.0" x2="1000.9" y2="328.9" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="289.3" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="1004.7" y1="253.2" x2="1004.7" y2="316.7" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="256.4" width="2.35" height="36.7" fill="var(--up)"/>
<line x1="1008.5" y1="223.2" x2="1008.5" y2="276.2" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="250.5" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="1012.2" y1="255.9" x2="1012.2" y2="304.1" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="259.6" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="1016.0" y1="245.1" x2="1016.0" y2="267.9" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="246.9" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="1019.8" y1="218.0" x2="1019.8" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="221.2" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="1023.6" y1="137.0" x2="1023.6" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="152.7" width="2.35" height="59.7" fill="var(--up)"/>
<line x1="1027.4" y1="121.3" x2="1027.4" y2="204.4" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="166.9" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="1031.2" y1="120.3" x2="1031.2" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="136.1" width="2.35" height="52.4" fill="var(--up)"/>
<line x1="1035.0" y1="124.2" x2="1035.0" y2="193.9" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="142.3" width="2.35" height="48.3" fill="var(--down)"/>
<line x1="1038.7" y1="174.7" x2="1038.7" y2="214.4" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="178.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1042.5" y1="107.6" x2="1042.5" y2="180.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="128.1" width="2.35" height="42.7" fill="var(--up)"/>
<line x1="1046.3" y1="73.4" x2="1046.3" y2="129.5" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="96.2" width="2.35" height="29.5" fill="var(--up)"/>
<line x1="1050.1" y1="75.8" x2="1050.1" y2="101.5" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="76.4" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="60" y1="438.3" x2="1052" y2="438.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="432.3" font-size="11.5" fill="var(--support)" font-weight="600">$165 S1</text>
<text x="1058" y="444.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="474.7" x2="1052" y2="474.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="468.7" font-size="11.5" fill="var(--support)" font-weight="600">$142 S2</text>
<text x="1058" y="480.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="491.3" x2="1052" y2="491.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="485.3" font-size="11.5" fill="var(--support)" font-weight="600">$131 S3</text>
<text x="1058" y="497.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="96.2" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다 — 둘을 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$384.27** (2026-08-14 종가) | — | 5년 구간 내 상단 저항 없음(역대 신고가 부근) — 가장 가까운 지지는 S1 |
| S1 | $165 | 3 | 2024년 중반(FY2024 회계연도 말 $162.37 부근)~2025년 초 사이 반복 형성된 스윙 저점대 |
| S2 | $142 | 3 | 2024년 초~2025년 상반기(2025-04 관세발 조정 저점 $152 부근 포함) 사이 여러 차례 저점을 형성한 구간 |
| S3 | $131 | 2 | 2023년 하반기(2023-11 종가 $122 부근) 저점대 |
| 참고선 | $59.73 | — | 5년 내 최저가(2022년 금리인상기 성장주 전반 조정 국면) — 현재가와 6배 이상 괴리돼 근시일 지지로서 의미 없음, 장기 사이클 참고용 |

---

## 3. 관측된 특이 구간 — 2024-12~2026-08 CyberArk 인수 발표~종결 및 이후 재평가 국면

- 2025-07-30 CyberArk 인수 계약 발표([최근 뉴스 / 이슈](./08_news.md))부터 2026-02-11 종결까지 약 7개월간 주가는 $165~$207 박스권(2. 지지선 / 저항선 요약 S1·S2)에서 정체됐다 — 대형 M&A 발표 이후 통합 성과 확인 전까지 시장이 관망세를 취한 전형적인 패턴으로 해석할 수 있다.
- 2026-02-11 인수 종결 직후~2026-04까지 오히려 주가는 박스권 하단($164 부근, 52주 최저 $139.57 근접)까지 밀렸다가, 2026-06-02 Q3 FY2026 실적발표(CyberArk 편입 첫 분기, NGS ARR +60%·RPO +36%)를 기점으로 급격히 재평가돼 2026-08 현재 역대 신고가($398.88) 부근까지 상승했다(일봉 기준 상세는 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3. 관측된 특이 구간 — 2026-06-02 Q3 FY2026 실적발표 이후 급등).
- 이 급등 이후 거래 레짐이 5년 구간 전체를 통틀어 완전히 달라졌다 — 2021~2026년 초까지 형성된 모든 스윙 레벨(S1~S3, 5년 최저 $59.73 포함)이 현재가와 크게 괴리돼 있어, 위 2. 지지선 / 저항선 요약에서 5년 최저가는 참고선으로만 처리했다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py PANW --name "Palo Alto Networks" --interval 1wk --event 2024-12-16:"2:1 주식분할" --close-on 2026-08-14`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 스크립트 기본값(회사 간 비교용 고정 파라미터)이며, PANW에 최적화된 값이 아니다.
    - 5년 구간 안에 CyberArk 인수(2026-02)라는 대형 M&A로 사업 구조 자체가 바뀌었다 — 과거 레벨(특히 5년 최저가 $59.73)이 현재 펀더멘털과 무관해졌을 가능성이 커, 2. 지지선 / 저항선 요약에서 참고선으로만 처리했다(3. 관측된 특이 구간 — 2024-12~2026-08 CyberArk 인수 발표~종결 및 이후 재평가 국면 참고).
    - 표본 기간(5년) 안에 두 차례 주식분할(2022-09 3:1, 2024-12 2:1)이 있었다 — Yahoo Finance 데이터가 두 분할을 모두 소급 반영해 제공하므로 이 문서 내 가격은 전 구간 일관된 기준이다. 2026-02-11 CyberArk 인수 종결 이벤트는 정확히 일치하는 주봉 거래일이 없어 차트에는 2024-12-16 분할 이벤트만 표시했다(3. 관측된 특이 구간 — 2024-12~2026-08 CyberArk 인수 발표~종결 및 이후 재평가 국면 서술로 대신 설명).

---

*작성일: 2026-08-23*
