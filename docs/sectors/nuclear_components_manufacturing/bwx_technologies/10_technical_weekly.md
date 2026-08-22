# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 주봉 API에서 직접 수집한 것이다(5년 주봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점 종가 대조**: 2026-08-17 종가는 이 문서(주봉 마감 기준) $172.97, [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉) $172.89, 핵심 지표·밸류에이션 / 적정주가(stockanalysis.com) $172.86로 세 출처 모두 $0.11(약 0.06%) 이내 — 데이터 제공처·집계 시점 차이로 판단되며 실질적 불일치는 아니다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-17)

<div class="bwxt-chart">
<style>
.bwxt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .bwxt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .bwxt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.bwxt-chart svg { width:100%; height:auto; display:block; }
.bwxt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.bwxt-chart .title { fill: var(--ink); font-weight:600; }
.bwxt-chart .grid { stroke: var(--grid); stroke-width:1; }
.bwxt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="BWX Technologies(BWXT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">BWX Technologies (BWXT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-17 · 마지막 종가 $172.97 (2026-08-17) · 단위 USD</text>
<line x1="60" y1="586.2" x2="1052" y2="586.2" class="grid"/>
<text x="52" y="590.2" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="453.7" x2="1052" y2="453.7" class="grid"/>
<text x="52" y="457.7" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="321.1" x2="1052" y2="321.1" class="grid"/>
<text x="52" y="325.1" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="188.6" x2="1052" y2="188.6" class="grid"/>
<text x="52" y="192.6" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
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
<line x1="60" y1="77.7" x2="1052" y2="77.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="80.7" font-size="10.5" fill="var(--muted)">$242 5년 최고</text>
<line x1="61.9" y1="570.1" x2="61.9" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="570.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="65.7" y1="563.8" x2="65.7" y2="571.3" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="566.4" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="69.5" y1="565.0" x2="69.5" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="566.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="73.3" y1="565.6" x2="73.3" y2="570.5" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="567.1" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="77.0" y1="567.2" x2="77.0" y2="574.5" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="567.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="80.8" y1="570.5" x2="80.8" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="572.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="84.6" y1="569.9" x2="84.6" y2="577.2" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="571.5" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="88.4" y1="563.7" x2="88.4" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="565.8" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="92.2" y1="562.1" x2="92.2" y2="570.3" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="565.7" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="96.0" y1="563.7" x2="96.0" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="564.7" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="99.8" y1="553.0" x2="99.8" y2="570.6" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="564.4" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="103.5" y1="565.0" x2="103.5" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="567.3" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="107.3" y1="572.2" x2="107.3" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="572.9" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="111.1" y1="575.6" x2="111.1" y2="585.4" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="576.2" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="114.9" y1="580.5" x2="114.9" y2="589.1" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="582.5" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="118.7" y1="586.9" x2="118.7" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="586.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="122.5" y1="587.5" x2="122.5" y2="593.4" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="591.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="126.3" y1="589.6" x2="126.3" y2="594.4" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="592.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="130.0" y1="591.1" x2="130.0" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="591.9" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="133.8" y1="589.6" x2="133.8" y2="592.9" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="591.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="137.6" y1="588.0" x2="137.6" y2="593.5" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="588.8" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="141.4" y1="588.1" x2="141.4" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="588.2" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="145.2" y1="586.5" x2="145.2" y2="592.9" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="590.4" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="149.0" y1="590.7" x2="149.0" y2="605.9" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="592.5" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="152.8" y1="599.7" x2="152.8" y2="605.5" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="603.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="156.5" y1="598.0" x2="156.5" y2="604.7" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="601.7" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="160.3" y1="598.8" x2="160.3" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="602.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="164.1" y1="586.4" x2="164.1" y2="605.4" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="587.3" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="167.9" y1="574.8" x2="167.9" y2="587.2" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="577.5" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="171.7" y1="567.4" x2="171.7" y2="580.1" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="576.7" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="175.5" y1="575.5" x2="175.5" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="575.6" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="179.3" y1="571.5" x2="179.3" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="572.0" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="183.1" y1="572.4" x2="183.1" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="572.7" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="186.8" y1="570.3" x2="186.8" y2="578.0" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="573.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="190.6" y1="570.0" x2="190.6" y2="574.4" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="570.8" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="194.4" y1="567.6" x2="194.4" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="571.0" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="198.2" y1="573.9" x2="198.2" y2="581.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="573.9" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="202.0" y1="579.1" x2="202.0" y2="587.0" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="582.3" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="205.8" y1="586.5" x2="205.8" y2="597.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="586.5" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="209.6" y1="584.0" x2="209.6" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="588.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="213.3" y1="581.5" x2="213.3" y2="588.4" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="581.6" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="217.1" y1="581.0" x2="217.1" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="581.8" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="220.9" y1="574.1" x2="220.9" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="578.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="224.7" y1="577.7" x2="224.7" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="580.1" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="228.5" y1="577.8" x2="228.5" y2="587.5" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="577.8" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="232.3" y1="568.6" x2="232.3" y2="578.9" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="569.2" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="236.1" y1="567.5" x2="236.1" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="569.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="239.8" y1="567.7" x2="239.8" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="569.1" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="243.6" y1="570.9" x2="243.6" y2="578.3" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="573.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="247.4" y1="567.7" x2="247.4" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="568.5" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="251.2" y1="566.8" x2="251.2" y2="572.3" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="568.4" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="255.0" y1="566.3" x2="255.0" y2="576.4" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="569.5" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="258.8" y1="571.7" x2="258.8" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="574.0" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="262.6" y1="574.2" x2="262.6" y2="578.7" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="577.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="266.4" y1="576.7" x2="266.4" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="579.3" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="270.1" y1="574.0" x2="270.1" y2="583.1" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="574.5" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="273.9" y1="573.1" x2="273.9" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="574.2" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="277.7" y1="576.5" x2="277.7" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="580.3" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="281.5" y1="581.3" x2="281.5" y2="587.1" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="585.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="285.3" y1="576.7" x2="285.3" y2="584.2" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="580.5" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="289.1" y1="576.6" x2="289.1" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="580.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="292.9" y1="571.7" x2="292.9" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="571.8" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="296.6" y1="565.6" x2="296.6" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="566.5" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="300.4" y1="563.9" x2="300.4" y2="571.5" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="567.5" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="304.2" y1="552.2" x2="304.2" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="558.7" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="308.0" y1="558.3" x2="308.0" y2="564.4" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="558.4" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="311.8" y1="556.0" x2="311.8" y2="563.0" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="557.2" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="315.6" y1="553.6" x2="315.6" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="553.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="319.4" y1="554.7" x2="319.4" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="555.4" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="323.1" y1="555.7" x2="323.1" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="560.1" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="326.9" y1="561.3" x2="326.9" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="562.4" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="330.7" y1="562.9" x2="330.7" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="563.6" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="334.5" y1="563.9" x2="334.5" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="564.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="338.3" y1="561.6" x2="338.3" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="564.6" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="342.1" y1="564.8" x2="342.1" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="566.4" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="345.9" y1="555.9" x2="345.9" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="556.6" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="349.6" y1="556.0" x2="349.6" y2="561.6" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="556.3" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="353.4" y1="557.8" x2="353.4" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="559.2" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="357.2" y1="556.6" x2="357.2" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="558.3" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="361.0" y1="555.6" x2="361.0" y2="562.2" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="557.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="364.8" y1="551.1" x2="364.8" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="551.4" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="368.6" y1="547.5" x2="368.6" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="551.5" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="372.4" y1="551.3" x2="372.4" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="557.0" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="376.2" y1="552.0" x2="376.2" y2="558.7" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="556.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="379.9" y1="550.4" x2="379.9" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="551.7" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="383.7" y1="549.6" x2="383.7" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="551.4" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="387.5" y1="546.8" x2="387.5" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="549.0" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="391.3" y1="546.6" x2="391.3" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="548.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="395.1" y1="546.7" x2="395.1" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="547.6" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="398.9" y1="544.6" x2="398.9" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="545.9" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="402.7" y1="539.8" x2="402.7" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="542.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="406.4" y1="539.9" x2="406.4" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="541.9" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="410.2" y1="541.8" x2="410.2" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="543.4" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="414.0" y1="551.3" x2="414.0" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="551.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="417.8" y1="544.3" x2="417.8" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="546.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="421.6" y1="533.8" x2="421.6" y2="547.1" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="533.9" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="425.4" y1="533.4" x2="425.4" y2="540.4" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="535.1" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="429.2" y1="528.1" x2="429.2" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="529.0" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="432.9" y1="528.6" x2="432.9" y2="532.8" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="529.5" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="436.7" y1="528.8" x2="436.7" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="530.8" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="440.5" y1="530.3" x2="440.5" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="531.9" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="444.3" y1="531.3" x2="444.3" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="532.2" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="448.1" y1="517.2" x2="448.1" y2="538.1" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="523.0" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="451.9" y1="516.6" x2="451.9" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="522.6" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="455.7" y1="521.7" x2="455.7" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="523.7" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="459.5" y1="523.7" x2="459.5" y2="530.0" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="526.2" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="463.2" y1="521.5" x2="463.2" y2="526.2" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="522.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="467.0" y1="523.1" x2="467.0" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="523.4" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="470.8" y1="520.3" x2="470.8" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="520.4" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="474.6" y1="514.8" x2="474.6" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="519.7" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="478.4" y1="518.4" x2="478.4" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="520.0" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="482.2" y1="519.4" x2="482.2" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="520.2" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="486.0" y1="512.1" x2="486.0" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="513.7" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="489.7" y1="508.2" x2="489.7" y2="516.1" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="513.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="493.5" y1="515.5" x2="493.5" y2="524.3" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="516.0" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="497.3" y1="513.0" x2="497.3" y2="525.5" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="517.0" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="501.1" y1="514.8" x2="501.1" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="515.7" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="504.9" y1="510.1" x2="504.9" y2="517.3" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="513.7" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="508.7" y1="508.7" x2="508.7" y2="515.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="509.8" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="512.5" y1="508.9" x2="512.5" y2="515.8" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="509.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="516.2" y1="502.3" x2="516.2" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="508.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="520.0" y1="504.6" x2="520.0" y2="516.5" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="509.1" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="523.8" y1="512.4" x2="523.8" y2="516.9" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="514.5" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="527.6" y1="513.4" x2="527.6" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="514.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="531.4" y1="514.3" x2="531.4" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="515.8" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="535.2" y1="506.4" x2="535.2" y2="520.8" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="506.8" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="539.0" y1="506.4" x2="539.0" y2="510.8" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="507.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="542.7" y1="500.5" x2="542.7" y2="507.7" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="501.6" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="546.5" y1="497.2" x2="546.5" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="498.2" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="550.3" y1="492.2" x2="550.3" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="492.9" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="554.1" y1="485.1" x2="554.1" y2="496.9" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="486.3" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="557.9" y1="479.2" x2="557.9" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="480.6" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="561.7" y1="446.0" x2="561.7" y2="483.7" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="447.4" width="2.35" height="32.6" fill="var(--up)"/>
<line x1="565.5" y1="434.6" x2="565.5" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="445.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="569.3" y1="445.1" x2="569.3" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="445.5" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="573.0" y1="445.9" x2="573.0" y2="456.3" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="446.9" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="576.8" y1="444.4" x2="576.8" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="446.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="580.6" y1="446.1" x2="580.6" y2="452.7" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="446.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="584.4" y1="450.7" x2="584.4" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="452.1" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="588.2" y1="464.4" x2="588.2" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="464.9" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="592.0" y1="463.2" x2="592.0" y2="475.8" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="464.3" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="595.8" y1="459.9" x2="595.8" y2="467.6" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="460.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="599.5" y1="456.6" x2="599.5" y2="488.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="459.0" width="2.35" height="21.5" fill="var(--down)"/>
<line x1="603.3" y1="477.7" x2="603.3" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="480.2" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="607.1" y1="481.0" x2="607.1" y2="486.8" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="482.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="610.9" y1="473.4" x2="610.9" y2="486.5" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="474.5" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="614.7" y1="473.2" x2="614.7" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="475.8" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="618.5" y1="480.6" x2="618.5" y2="486.4" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="481.7" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="622.3" y1="471.0" x2="622.3" y2="483.0" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="472.2" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="626.0" y1="463.0" x2="626.0" y2="472.5" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="466.9" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="629.8" y1="464.6" x2="629.8" y2="471.6" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="465.5" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="633.6" y1="455.2" x2="633.6" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="457.8" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="637.4" y1="441.5" x2="637.4" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="448.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="641.2" y1="436.7" x2="641.2" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="445.8" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="645.0" y1="451.5" x2="645.0" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="454.4" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="648.8" y1="457.8" x2="648.8" y2="480.6" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="459.4" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="652.5" y1="455.6" x2="652.5" y2="463.3" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="458.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="656.3" y1="447.6" x2="656.3" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="448.2" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="660.1" y1="442.2" x2="660.1" y2="452.1" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="445.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="663.9" y1="445.2" x2="663.9" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="447.0" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="667.7" y1="455.9" x2="667.7" y2="469.4" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="457.9" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="671.5" y1="445.7" x2="671.5" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="446.1" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="675.3" y1="430.2" x2="675.3" y2="447.3" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="430.9" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="679.1" y1="405.7" x2="679.1" y2="432.9" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="406.7" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="682.8" y1="403.2" x2="682.8" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="407.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="686.6" y1="381.8" x2="686.6" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="384.2" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="690.4" y1="379.4" x2="690.4" y2="398.1" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="381.8" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="694.2" y1="384.1" x2="694.2" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="391.6" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="698.0" y1="387.4" x2="698.0" y2="416.4" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="388.5" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="701.8" y1="357.4" x2="701.8" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="384.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="705.6" y1="359.7" x2="705.6" y2="386.3" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="366.5" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="709.3" y1="363.1" x2="709.3" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="364.9" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="713.1" y1="370.0" x2="713.1" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="370.0" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="716.9" y1="384.7" x2="716.9" y2="399.6" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="384.7" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="720.7" y1="393.0" x2="720.7" y2="423.9" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="398.7" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="724.5" y1="417.2" x2="724.5" y2="425.4" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="419.1" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="728.3" y1="416.7" x2="728.3" y2="425.6" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="417.9" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="732.1" y1="400.5" x2="732.1" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="414.7" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="735.8" y1="390.4" x2="735.8" y2="424.1" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="394.2" width="2.35" height="24.8" fill="var(--up)"/>
<line x1="739.6" y1="375.4" x2="739.6" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="380.4" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="743.4" y1="390.6" x2="743.4" y2="425.4" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="391.1" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="747.2" y1="414.4" x2="747.2" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="415.4" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="751.0" y1="412.2" x2="751.0" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="413.9" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="754.8" y1="427.7" x2="754.8" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="435.1" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="758.6" y1="431.3" x2="758.6" y2="454.3" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="443.1" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="762.4" y1="440.7" x2="762.4" y2="464.0" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="442.9" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="766.1" y1="455.6" x2="766.1" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="458.3" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="769.9" y1="445.7" x2="769.9" y2="461.6" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="455.3" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="773.7" y1="440.4" x2="773.7" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="450.1" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="777.5" y1="447.6" x2="777.5" y2="488.9" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="459.1" width="2.35" height="23.1" fill="var(--down)"/>
<line x1="781.3" y1="441.8" x2="781.3" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="445.1" width="2.35" height="43.1" fill="var(--up)"/>
<line x1="785.1" y1="439.3" x2="785.1" y2="447.5" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="440.4" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="788.9" y1="428.9" x2="788.9" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="429.9" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="792.6" y1="415.5" x2="792.6" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="420.2" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="796.4" y1="418.9" x2="796.4" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="423.2" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="800.2" y1="421.8" x2="800.2" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="421.8" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="804.0" y1="400.8" x2="804.0" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="402.0" width="2.35" height="28.9" fill="var(--up)"/>
<line x1="807.8" y1="380.4" x2="807.8" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="385.8" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="811.6" y1="373.0" x2="811.6" y2="389.3" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="374.9" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="815.4" y1="348.8" x2="815.4" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="352.7" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="819.1" y1="333.5" x2="819.1" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="341.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="822.9" y1="335.6" x2="822.9" y2="351.3" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="339.2" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="826.7" y1="335.0" x2="826.7" y2="353.1" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="335.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="830.5" y1="335.5" x2="830.5" y2="364.0" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="339.6" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="834.3" y1="336.7" x2="834.3" y2="357.5" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="339.8" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="838.1" y1="324.4" x2="838.1" y2="357.8" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="326.5" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="841.9" y1="311.8" x2="841.9" y2="339.5" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="322.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="845.6" y1="217.1" x2="845.6" y2="322.3" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="243.7" width="2.35" height="74.0" fill="var(--up)"/>
<line x1="849.4" y1="228.4" x2="849.4" y2="266.2" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="246.8" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="853.2" y1="256.0" x2="853.2" y2="290.2" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="258.7" width="2.35" height="27.8" fill="var(--down)"/>
<line x1="857.0" y1="274.5" x2="857.0" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="284.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="860.8" y1="276.7" x2="860.8" y2="301.4" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="285.0" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="864.6" y1="263.2" x2="864.6" y2="294.9" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="272.5" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="868.4" y1="244.0" x2="868.4" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="256.2" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="872.2" y1="236.3" x2="872.2" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="239.9" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="875.9" y1="215.0" x2="875.9" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="224.0" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="879.7" y1="189.3" x2="879.7" y2="220.4" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="214.9" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="883.5" y1="149.5" x2="883.5" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="180.3" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="887.3" y1="165.3" x2="887.3" y2="213.7" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="172.7" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="891.1" y1="139.5" x2="891.1" y2="182.3" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="152.5" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="894.9" y1="143.7" x2="894.9" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="151.4" width="2.35" height="54.3" fill="var(--down)"/>
<line x1="898.7" y1="188.6" x2="898.7" y2="261.7" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="195.2" width="2.35" height="50.9" fill="var(--down)"/>
<line x1="902.4" y1="222.9" x2="902.4" y2="284.0" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="243.1" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="906.2" y1="241.6" x2="906.2" y2="268.6" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="244.6" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="910.0" y1="235.0" x2="910.0" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="247.2" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="913.8" y1="231.1" x2="913.8" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="244.3" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="917.6" y1="249.8" x2="917.6" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="250.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="921.4" y1="238.9" x2="921.4" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="242.0" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="925.2" y1="236.2" x2="925.2" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="236.7" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="928.9" y1="180.6" x2="928.9" y2="225.7" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="184.7" width="2.35" height="41.0" fill="var(--up)"/>
<line x1="932.7" y1="134.0" x2="932.7" y2="187.7" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="141.1" width="2.35" height="43.5" fill="var(--up)"/>
<line x1="936.5" y1="146.1" x2="936.5" y2="181.9" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="156.5" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="940.3" y1="135.9" x2="940.3" y2="181.7" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="170.7" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="944.1" y1="154.1" x2="944.1" y2="232.3" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="180.8" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="947.9" y1="171.4" x2="947.9" y2="206.4" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="187.5" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="951.7" y1="154.9" x2="951.7" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="171.5" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="955.5" y1="146.6" x2="955.5" y2="194.9" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="172.7" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="959.2" y1="139.1" x2="959.2" y2="216.8" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="176.0" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="963.0" y1="182.1" x2="963.0" y2="218.1" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="204.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="966.8" y1="154.4" x2="966.8" y2="195.9" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="189.2" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="970.6" y1="129.5" x2="970.6" y2="189.0" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="181.7" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="974.4" y1="138.6" x2="974.4" y2="217.7" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="148.8" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="978.2" y1="88.1" x2="978.2" y2="157.5" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="110.2" width="2.35" height="33.0" fill="var(--up)"/>
<line x1="982.0" y1="77.7" x2="982.0" y2="114.3" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="93.7" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="985.7" y1="92.1" x2="985.7" y2="154.5" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="95.8" width="2.35" height="31.4" fill="var(--down)"/>
<line x1="989.5" y1="124.9" x2="989.5" y2="173.6" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="127.5" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="993.3" y1="116.7" x2="993.3" y2="180.5" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="142.8" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="997.1" y1="156.5" x2="997.1" y2="190.6" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="176.0" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="1000.9" y1="172.1" x2="1000.9" y2="207.1" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="172.3" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="1004.7" y1="165.1" x2="1004.7" y2="205.3" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="166.7" width="2.35" height="32.7" fill="var(--down)"/>
<line x1="1008.5" y1="211.0" x2="1008.5" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="215.1" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="1012.2" y1="192.2" x2="1012.2" y2="243.0" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="205.9" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="1016.0" y1="159.6" x2="1016.0" y2="205.6" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="174.2" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="1019.8" y1="147.8" x2="1019.8" y2="201.9" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="166.7" width="2.35" height="27.4" fill="var(--down)"/>
<line x1="1023.6" y1="190.4" x2="1023.6" y2="223.4" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="195.6" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="1027.4" y1="193.9" x2="1027.4" y2="240.3" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="210.9" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="1031.2" y1="229.5" x2="1031.2" y2="274.3" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="231.6" width="2.35" height="33.4" fill="var(--down)"/>
<line x1="1035.0" y1="240.3" x2="1035.0" y2="272.5" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="256.1" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="1038.7" y1="237.5" x2="1038.7" y2="302.3" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="245.6" width="2.35" height="26.0" fill="var(--down)"/>
<line x1="1042.5" y1="245.6" x2="1042.5" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="268.4" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="1046.3" y1="256.2" x2="1046.3" y2="275.4" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="259.6" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="1050.1" y1="255.9" x2="1050.1" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="260.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="60" y1="140.4" x2="1052" y2="140.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="143.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$218 R1</text>
<text x="1058" y="155.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="597.8" x2="1052" y2="597.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="591.8" font-size="11.5" fill="var(--support)" font-weight="600">$46 S1</text>
<text x="1058" y="603.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="260.2" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $218 | 3 | 2026년 상반기 랠리 국면에서 형성된 5년 관점의 상단 저항대 |
| **현재가** | **$172.97** (2026-08-17 종가) | — | R1과 S1 사이 |
| S1 | $46 | 2 | 2022년 무렵의 저점대 — 현재가($172.97)와는 3.8배 가까이 차이 나는 5년 전 구조적 저점으로, 근시일 지지로서의 의미는 사실상 없다(아래 4. 방법론 · 한계 참고) |
| 참고선 | $242 | — | 5년 최고(정확히는 $241.82, 2026년 상반기 기록) — 기술적 분석 — 일봉·1년와 동일한 레벨로, 이후 조정을 거쳐 현재는 단절된 국면 |

> 5년 관점에서는 유효 클러스터(터치 2회 이상)가 R 1개·S 1개뿐이라 스크립트 기본값(위/아래 각 3개)보다 훨씬 적게 나왔다 — BWXT 주가가 2021~2025년 사이 완만한 상승 후 2025~2026년에 가파르게 재평가되면서, 중간 구간의 스윙 포인트들이 ±2.5% 클러스터링 기준으로 서로 잘 묶이지 않았기 때문으로 보인다.

---

## 3. 관측된 특이 구간 — 2025년 이후 밸류에이션 재평가 국면

- 5년 구간(2021-08~2026-08) 중 2023년 말~2025년 초까지는 완만한 상승(FY2023 말 종가 $75.23 → FY2024 말 $110.23, 핵심 지표 A.2)이었으나, 2025년 5월 Kinectrics 인수 이후 상업 원전·AI 데이터센터발 원자력 재조명 테마가 겹치며 2026년 상반기 $241.82까지 급등했다가 현재 $172.97 수준으로 조정된 국면이다. 일봉 기준 최근 조정 서술은 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3. 관측된 특이 구간 — 2026년 상반기 고점 이후 조정, Kinectrics 인수 자체는 [역사 / 주요 이벤트](./02_history.md) 참고.
- 5년 구간 안에 사업 구조 자체가 바뀐 사건(2025-05 Kinectrics 인수로 총자산·이자부 차입금이 단절적으로 확대, 핵심 지표 A.3 각주)이 있어, S1($46) 같은 2022년 무렵의 저점 레벨은 현재의 확장된 자본구조·사업 포트폴리오와는 무관한 "다른 회사 시절"의 가격대에 가깝다 — 근시일 지지로 해석하지 않고 참고 수준으로만 남긴다.
- 이후 거래 레짐은 5년 최고($241.82)와 확연히 단절된 채 R1($218)~현재가 사이 박스권으로 재형성되는 중으로 보인다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-17. 수집 시점: 2026-08-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py BWXT --name "BWX Technologies" --interval 1wk --ref-line 241.82:"5년 최고" --close-on 2026-08-17`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 5년 구간 안에 사업 구조 자체가 바뀐 사건(2025-05 Kinectrics 인수)이 있어, 인수 이전 스윙 레벨(특히 S1)이 현재 펀더멘털과 무관해졌을 가능성이 크다 — 3. 관측된 특이 구간 — 2025년 이후 밸류에이션 재평가 국면에서 참고선으로만 처리한 이유.
    - 최근 5년 안에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다(원주가 그대로 사용, 소급조정 불필요) — 다만 위 M&A로 인한 펀더멘털 단절은 가격 연속성 자체는 깨지 않았으므로 소급조정 대상은 아니다.

---

## 관련 문서

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 일봉·1년](./09_technical_daily.md)
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — BWXT 주봉 시세](https://finance.yahoo.com/quote/BWXT/history/)
- [stockanalysis.com — BWXT 현재가·통계](https://stockanalysis.com/stocks/bwxt/) (핵심 지표·밸류에이션 대조용)

---

*작성일: 2026-08-18*
