# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API(Yahoo Finance)에서 직접 수집했다(5년 주봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 겹치는 시점의 종가를 대조한 결과: `2026-08-14` 종가 $192.81은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)에 인용된 같은 날짜 종가와 **일치**한다(개요·밸류에이션 / 적정주가의 기준일은 하루 앞선 2026-08-13, $189.43 — 기술적 분석 — 일봉·1년 상단 각주에서 이미 대조).

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="avav-chart">
<style>
.avav-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .avav-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .avav-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.avav-chart svg { width:100%; height:auto; display:block; }
.avav-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.avav-chart .title { fill: var(--ink); font-weight:600; }
.avav-chart .grid { stroke: var(--grid); stroke-width:1; }
.avav-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AeroVironment(AVAV) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">AeroVironment (AVAV) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $192.81 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="611.4" x2="1052" y2="611.4" class="grid"/>
<text x="52" y="615.4" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="538.3" x2="1052" y2="538.3" class="grid"/>
<text x="52" y="542.3" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="465.2" x2="1052" y2="465.2" class="grid"/>
<text x="52" y="469.2" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="392.2" x2="1052" y2="392.2" class="grid"/>
<text x="52" y="396.2" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="319.1" x2="1052" y2="319.1" class="grid"/>
<text x="52" y="323.1" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="246.0" x2="1052" y2="246.0" class="grid"/>
<text x="52" y="250.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="172.9" x2="1052" y2="172.9" class="grid"/>
<text x="52" y="176.9" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="99.8" x2="1052" y2="99.8" class="grid"/>
<text x="52" y="103.8" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="149.0" y1="56.0" x2="149.0" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="155.0" y="68.0" font-size="10.5" fill="var(--down)">2022-01-24 금리 인상기 약세장 저점(5년 최저 $52.03)</text>
<line x1="792.6" y1="56.0" x2="792.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="798.6" y="68.0" font-size="10.5" fill="var(--down)">2025-04-28 BlueHalo 인수 완료(자본구조 단절)</text>
<line x1="61.9" y1="535.9" x2="61.9" y2="544.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="538.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="65.7" y1="532.2" x2="65.7" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="533.3" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="69.5" y1="530.2" x2="69.5" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="531.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="73.3" y1="529.1" x2="73.3" y2="552.9" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="533.1" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="77.0" y1="546.7" x2="77.0" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="547.0" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="80.8" y1="557.7" x2="80.8" y2="562.7" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="560.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="84.6" y1="556.3" x2="84.6" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="557.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="88.4" y1="555.8" x2="88.4" y2="561.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="557.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="92.2" y1="550.4" x2="92.2" y2="556.9" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="552.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="96.0" y1="547.2" x2="96.0" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="551.6" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="99.8" y1="549.1" x2="99.8" y2="556.0" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="552.0" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="103.5" y1="544.0" x2="103.5" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="545.4" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="107.3" y1="544.4" x2="107.3" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="545.0" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="111.1" y1="548.9" x2="111.1" y2="555.8" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="550.4" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="114.9" y1="552.7" x2="114.9" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="555.0" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="118.7" y1="560.7" x2="118.7" y2="573.2" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="561.4" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="122.5" y1="565.9" x2="122.5" y2="606.3" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="569.6" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="126.3" y1="590.1" x2="126.3" y2="597.9" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="590.7" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="130.0" y1="590.3" x2="130.0" y2="593.9" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="591.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="133.8" y1="591.1" x2="133.8" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="591.4" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="137.6" y1="590.6" x2="137.6" y2="593.7" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="593.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="141.4" y1="592.8" x2="141.4" y2="597.4" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="593.5" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="145.2" y1="595.6" x2="145.2" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="595.8" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="149.0" y1="598.9" x2="149.0" y2="608.4" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="602.1" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="152.8" y1="599.8" x2="152.8" y2="605.8" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="601.6" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="156.5" y1="593.2" x2="156.5" y2="601.9" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="595.6" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="160.3" y1="594.3" x2="160.3" y2="598.5" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="595.6" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="164.1" y1="591.2" x2="164.1" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="593.5" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="167.9" y1="573.4" x2="167.9" y2="590.9" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="576.0" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="171.7" y1="565.1" x2="171.7" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="573.8" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="175.5" y1="539.1" x2="175.5" y2="578.9" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="548.3" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="179.3" y1="536.2" x2="179.3" y2="548.4" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="539.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="183.1" y1="538.3" x2="183.1" y2="552.0" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="539.3" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="186.8" y1="528.1" x2="186.8" y2="546.3" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="533.8" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="190.6" y1="517.7" x2="190.6" y2="535.7" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="524.9" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="194.4" y1="524.0" x2="194.4" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="525.0" width="2.35" height="32.7" fill="var(--down)"/>
<line x1="198.2" y1="556.4" x2="198.2" y2="568.8" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="558.7" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="202.0" y1="550.9" x2="202.0" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="565.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="205.8" y1="565.7" x2="205.8" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="567.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="209.6" y1="552.9" x2="209.6" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="560.9" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="213.3" y1="543.7" x2="213.3" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="544.2" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="217.1" y1="540.9" x2="217.1" y2="553.7" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="543.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="220.9" y1="542.6" x2="220.9" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="542.6" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="224.7" y1="555.3" x2="224.7" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="557.6" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="228.5" y1="560.3" x2="228.5" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="561.7" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="232.3" y1="558.8" x2="232.3" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="558.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="236.1" y1="558.6" x2="236.1" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="560.7" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="239.8" y1="563.7" x2="239.8" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="563.7" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="243.6" y1="561.6" x2="243.6" y2="571.5" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="565.8" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="247.4" y1="556.7" x2="247.4" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="557.8" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="251.2" y1="549.0" x2="251.2" y2="559.7" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="552.7" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="255.0" y1="541.1" x2="255.0" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="541.3" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="258.8" y1="528.7" x2="258.8" y2="543.8" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="534.5" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="262.6" y1="534.7" x2="262.6" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="536.8" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="266.4" y1="544.5" x2="266.4" y2="565.3" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="544.8" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="270.1" y1="530.5" x2="270.1" y2="563.7" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="538.2" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="273.9" y1="536.6" x2="273.9" y2="550.4" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="538.4" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="277.7" y1="543.6" x2="277.7" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="551.5" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="281.5" y1="552.4" x2="281.5" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="556.1" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="285.3" y1="555.3" x2="285.3" y2="573.2" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="561.6" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="289.1" y1="566.9" x2="289.1" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="572.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="292.9" y1="565.6" x2="292.9" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="567.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="296.6" y1="552.2" x2="296.6" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="552.7" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="300.4" y1="547.4" x2="300.4" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="552.5" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="304.2" y1="547.0" x2="304.2" y2="565.4" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="548.6" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="308.0" y1="546.6" x2="308.0" y2="555.6" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="548.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="311.8" y1="546.6" x2="311.8" y2="555.6" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="548.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="315.6" y1="547.3" x2="315.6" y2="556.3" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="549.0" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="319.4" y1="550.3" x2="319.4" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="550.3" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="323.1" y1="550.7" x2="323.1" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="562.9" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="326.9" y1="559.2" x2="326.9" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="560.6" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="330.7" y1="558.6" x2="330.7" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="559.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="334.5" y1="557.9" x2="334.5" y2="565.9" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="557.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="338.3" y1="550.8" x2="338.3" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="553.6" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="342.1" y1="553.8" x2="342.1" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="555.7" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="345.9" y1="552.5" x2="345.9" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="555.0" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="349.6" y1="544.9" x2="349.6" y2="556.9" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="550.1" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="353.4" y1="548.2" x2="353.4" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="550.6" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="357.2" y1="549.6" x2="357.2" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="554.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="361.0" y1="556.8" x2="361.0" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="557.2" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="364.8" y1="552.7" x2="364.8" y2="561.9" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="554.0" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="368.6" y1="544.1" x2="368.6" y2="557.8" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="552.1" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="372.4" y1="548.9" x2="372.4" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="552.4" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="376.2" y1="548.1" x2="376.2" y2="555.4" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="551.7" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="379.9" y1="549.4" x2="379.9" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="550.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="383.7" y1="528.2" x2="383.7" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="532.8" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="387.5" y1="524.8" x2="387.5" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="529.1" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="391.3" y1="525.5" x2="391.3" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="529.8" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="395.1" y1="534.3" x2="395.1" y2="540.4" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="534.7" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="398.9" y1="532.3" x2="398.9" y2="538.9" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="534.2" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="402.7" y1="527.1" x2="402.7" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="528.6" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="406.4" y1="523.7" x2="406.4" y2="534.5" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="528.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="410.2" y1="520.2" x2="410.2" y2="555.5" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="528.3" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="414.0" y1="537.6" x2="414.0" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="540.0" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="417.8" y1="538.3" x2="417.8" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="540.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="421.6" y1="540.2" x2="421.6" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="542.2" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="425.4" y1="540.9" x2="425.4" y2="551.8" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="547.9" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="429.2" y1="533.5" x2="429.2" y2="554.2" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="535.0" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="432.9" y1="534.7" x2="432.9" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="535.3" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="436.7" y1="537.1" x2="436.7" y2="544.5" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="543.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="440.5" y1="541.8" x2="440.5" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="543.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="444.3" y1="541.2" x2="444.3" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="543.5" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="448.1" y1="539.3" x2="448.1" y2="546.6" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="543.2" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="451.9" y1="540.9" x2="451.9" y2="545.3" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="543.2" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="455.7" y1="543.1" x2="455.7" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="545.6" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="459.5" y1="539.0" x2="459.5" y2="548.3" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="546.5" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="463.2" y1="539.0" x2="463.2" y2="547.1" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="541.2" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="467.0" y1="502.7" x2="467.0" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="518.6" width="2.35" height="23.2" fill="var(--up)"/>
<line x1="470.8" y1="517.2" x2="470.8" y2="524.2" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="519.0" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="474.6" y1="518.1" x2="474.6" y2="523.6" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="520.3" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="478.4" y1="519.3" x2="478.4" y2="525.1" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="521.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="482.2" y1="519.5" x2="482.2" y2="531.5" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="521.6" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="486.0" y1="515.9" x2="486.0" y2="531.3" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="521.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="489.7" y1="508.4" x2="489.7" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="513.7" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="493.5" y1="504.2" x2="493.5" y2="519.9" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="514.0" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="497.3" y1="505.8" x2="497.3" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="509.3" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="501.1" y1="497.4" x2="501.1" y2="512.2" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="506.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="504.9" y1="494.6" x2="504.9" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="501.7" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="508.7" y1="488.1" x2="508.7" y2="501.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="489.5" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="512.5" y1="480.0" x2="512.5" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="480.3" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="516.2" y1="474.0" x2="516.2" y2="505.8" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="478.2" width="2.35" height="23.9" fill="var(--down)"/>
<line x1="520.0" y1="493.2" x2="520.0" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="500.0" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="523.8" y1="493.6" x2="523.8" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="498.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="527.6" y1="494.8" x2="527.6" y2="501.0" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="496.4" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="531.4" y1="499.7" x2="531.4" y2="512.4" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="501.5" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="535.2" y1="498.4" x2="535.2" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="499.1" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="539.0" y1="498.8" x2="539.0" y2="508.4" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="498.8" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="542.7" y1="498.8" x2="542.7" y2="508.9" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="503.7" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="546.5" y1="503.4" x2="546.5" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="505.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="550.3" y1="499.3" x2="550.3" y2="509.7" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="501.5" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="554.1" y1="498.5" x2="554.1" y2="506.9" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="501.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="557.9" y1="499.1" x2="557.9" y2="507.1" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="503.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="561.7" y1="493.0" x2="561.7" y2="506.5" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="496.3" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="565.5" y1="414.6" x2="565.5" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="441.5" width="2.35" height="45.6" fill="var(--up)"/>
<line x1="569.3" y1="442.3" x2="569.3" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="442.6" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="573.0" y1="463.2" x2="573.0" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="466.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="576.8" y1="458.4" x2="576.8" y2="468.8" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="460.4" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="580.6" y1="457.3" x2="580.6" y2="473.4" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="457.8" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="584.4" y1="460.9" x2="584.4" y2="472.5" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="465.6" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="588.2" y1="461.5" x2="588.2" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="465.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="592.0" y1="446.5" x2="592.0" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="453.4" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="595.8" y1="437.8" x2="595.8" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="437.8" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="599.5" y1="406.6" x2="599.5" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="411.9" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="603.3" y1="395.7" x2="603.3" y2="411.5" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="401.2" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="607.1" y1="392.0" x2="607.1" y2="402.3" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="392.5" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="610.9" y1="384.4" x2="610.9" y2="398.6" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="389.0" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="614.7" y1="382.2" x2="614.7" y2="390.8" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="386.3" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="618.5" y1="362.6" x2="618.5" y2="395.0" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="369.9" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="622.3" y1="357.1" x2="622.3" y2="413.3" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="375.5" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="626.0" y1="389.3" x2="626.0" y2="447.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="407.8" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="629.8" y1="414.5" x2="629.8" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="415.9" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="633.6" y1="423.7" x2="633.6" y2="439.8" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="431.2" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="637.4" y1="424.2" x2="637.4" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="428.7" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="641.2" y1="429.2" x2="641.2" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="430.4" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="645.0" y1="420.4" x2="645.0" y2="444.6" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="429.8" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="648.8" y1="423.6" x2="648.8" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="427.2" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="652.5" y1="404.2" x2="652.5" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="406.1" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="656.3" y1="404.3" x2="656.3" y2="416.9" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="406.1" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="660.1" y1="375.4" x2="660.1" y2="429.1" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="386.7" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="663.9" y1="380.6" x2="663.9" y2="427.4" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="386.4" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="667.7" y1="403.3" x2="667.7" y2="427.3" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="403.7" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="671.5" y1="409.4" x2="671.5" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="410.9" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="675.3" y1="384.4" x2="675.3" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="393.3" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="679.1" y1="364.0" x2="679.1" y2="397.1" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="380.5" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="682.8" y1="366.6" x2="682.8" y2="387.0" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="369.7" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="686.6" y1="360.7" x2="686.6" y2="378.2" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="365.8" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="690.4" y1="352.4" x2="690.4" y2="374.4" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="361.6" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="694.2" y1="359.2" x2="694.2" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="359.9" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="698.0" y1="345.4" x2="698.0" y2="387.5" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="351.4" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="701.8" y1="338.7" x2="701.8" y2="395.6" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="345.4" width="2.35" height="46.7" fill="var(--down)"/>
<line x1="705.6" y1="384.8" x2="705.6" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="392.9" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="709.3" y1="386.8" x2="709.3" y2="406.0" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="393.4" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="713.1" y1="386.9" x2="713.1" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="396.5" width="2.35" height="49.2" fill="var(--down)"/>
<line x1="716.9" y1="443.5" x2="716.9" y2="464.5" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="445.3" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="720.7" y1="433.0" x2="720.7" y2="457.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="444.7" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="724.5" y1="443.6" x2="724.5" y2="458.5" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="443.9" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="728.3" y1="448.1" x2="728.3" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="449.1" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="732.1" y1="438.9" x2="732.1" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="443.3" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="735.8" y1="434.5" x2="735.8" y2="454.6" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="437.8" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="739.6" y1="417.5" x2="739.6" y2="434.5" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="420.9" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="743.4" y1="417.6" x2="743.4" y2="437.5" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="421.2" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="747.2" y1="408.5" x2="747.2" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="425.9" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="751.0" y1="417.5" x2="751.0" y2="455.9" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="425.1" width="2.35" height="29.9" fill="var(--down)"/>
<line x1="754.8" y1="448.3" x2="754.8" y2="460.6" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="453.2" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="758.6" y1="453.8" x2="758.6" y2="471.1" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="458.2" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="762.4" y1="464.0" x2="762.4" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="465.4" width="2.35" height="25.6" fill="var(--down)"/>
<line x1="766.1" y1="493.7" x2="766.1" y2="508.4" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="494.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="769.9" y1="495.7" x2="769.9" y2="507.4" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="496.4" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="773.7" y1="491.5" x2="773.7" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="498.7" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="777.5" y1="497.3" x2="777.5" y2="523.5" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="511.4" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="781.3" y1="468.1" x2="781.3" y2="535.0" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="470.6" width="2.35" height="58.8" fill="var(--up)"/>
<line x1="785.1" y1="465.6" x2="785.1" y2="482.8" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="465.8" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="788.9" y1="455.9" x2="788.9" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="465.8" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="792.6" y1="450.6" x2="792.6" y2="469.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="452.4" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="796.4" y1="437.5" x2="796.4" y2="458.8" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="442.6" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="800.2" y1="433.9" x2="800.2" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="434.4" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="804.0" y1="436.6" x2="804.0" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="437.4" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="807.8" y1="420.3" x2="807.8" y2="435.6" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="424.3" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="811.6" y1="389.7" x2="811.6" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="405.5" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="815.4" y1="388.1" x2="815.4" y2="416.3" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="397.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="819.1" y1="395.5" x2="819.1" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="396.0" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="822.9" y1="266.5" x2="822.9" y2="409.9" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="278.1" width="2.35" height="127.3" fill="var(--up)"/>
<line x1="826.7" y1="252.0" x2="826.7" y2="327.2" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="269.8" width="2.35" height="54.7" fill="var(--down)"/>
<line x1="830.5" y1="297.4" x2="830.5" y2="349.9" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="298.9" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="834.3" y1="269.1" x2="834.3" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="284.0" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="838.1" y1="274.6" x2="838.1" y2="309.6" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="279.6" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="841.9" y1="271.4" x2="841.9" y2="317.1" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="278.6" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="845.6" y1="280.3" x2="845.6" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="296.1" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="849.4" y1="308.8" x2="849.4" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="317.4" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="853.2" y1="313.2" x2="853.2" y2="351.9" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="324.0" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="857.0" y1="313.7" x2="857.0" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="331.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="860.8" y1="326.3" x2="860.8" y2="361.6" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="334.4" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="864.6" y1="308.7" x2="864.6" y2="354.5" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="329.3" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="868.4" y1="261.5" x2="868.4" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="277.4" width="2.35" height="48.6" fill="var(--up)"/>
<line x1="872.2" y1="235.6" x2="872.2" y2="281.9" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="244.2" width="2.35" height="33.5" fill="var(--up)"/>
<line x1="875.9" y1="123.5" x2="875.9" y2="240.6" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="136.9" width="2.35" height="93.9" fill="var(--up)"/>
<line x1="879.7" y1="73.7" x2="879.7" y2="139.3" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="111.1" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="883.5" y1="83.5" x2="883.5" y2="174.3" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="111.1" width="2.35" height="60.9" fill="var(--down)"/>
<line x1="887.3" y1="128.8" x2="887.3" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="131.2" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="891.1" y1="108.5" x2="891.1" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="116.3" width="2.35" height="27.5" fill="var(--down)"/>
<line x1="894.9" y1="129.1" x2="894.9" y2="235.3" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="135.7" width="2.35" height="67.0" fill="var(--down)"/>
<line x1="898.7" y1="185.8" x2="898.7" y2="275.2" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="189.9" width="2.35" height="68.9" fill="var(--down)"/>
<line x1="902.4" y1="252.4" x2="902.4" y2="304.1" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="259.1" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="906.2" y1="269.4" x2="906.2" y2="290.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="276.0" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="910.0" y1="256.6" x2="910.0" y2="308.4" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="277.6" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="913.8" y1="258.4" x2="913.8" y2="340.8" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="273.5" width="2.35" height="61.6" fill="var(--down)"/>
<line x1="917.6" y1="326.2" x2="917.6" y2="352.0" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="329.3" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="921.4" y1="299.6" x2="921.4" y2="322.6" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="311.8" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="925.2" y1="307.5" x2="925.2" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="310.0" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="928.9" y1="141.6" x2="928.9" y2="292.8" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="151.0" width="2.35" height="140.9" fill="var(--up)"/>
<line x1="932.7" y1="87.8" x2="932.7" y2="178.1" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="110.3" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="936.5" y1="114.4" x2="936.5" y2="246.0" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="143.7" width="2.35" height="91.0" fill="var(--down)"/>
<line x1="940.3" y1="215.2" x2="940.3" y2="280.0" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="235.7" width="2.35" height="41.9" fill="var(--down)"/>
<line x1="944.1" y1="264.3" x2="944.1" y2="342.5" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="287.0" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="947.9" y1="278.3" x2="947.9" y2="342.8" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="309.4" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="951.7" y1="266.8" x2="951.7" y2="315.7" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="297.7" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="955.5" y1="293.5" x2="955.5" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="309.4" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="959.2" y1="241.6" x2="959.2" y2="397.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="269.0" width="2.35" height="79.6" fill="var(--down)"/>
<line x1="963.0" y1="349.0" x2="963.0" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="349.0" width="2.35" height="32.8" fill="var(--down)"/>
<line x1="966.8" y1="359.0" x2="966.8" y2="401.6" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="373.9" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="970.6" y1="375.3" x2="970.6" y2="415.8" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="391.2" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="974.4" y1="404.1" x2="974.4" y2="428.1" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="412.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="978.2" y1="396.5" x2="978.2" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="414.1" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="982.0" y1="379.5" x2="982.0" y2="425.8" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="404.7" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="985.7" y1="359.4" x2="985.7" y2="407.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="397.6" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="989.5" y1="390.9" x2="989.5" y2="418.9" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="398.7" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="993.3" y1="413.0" x2="993.3" y2="443.9" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="413.0" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="997.1" y1="430.9" x2="997.1" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="443.7" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="1000.9" y1="429.4" x2="1000.9" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="429.8" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="1004.7" y1="366.2" x2="1004.7" y2="428.0" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="381.6" width="2.35" height="35.7" fill="var(--up)"/>
<line x1="1008.5" y1="379.1" x2="1008.5" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="388.2" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="1012.2" y1="406.4" x2="1012.2" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="411.1" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="1016.0" y1="427.2" x2="1016.0" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="429.6" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="1019.8" y1="445.0" x2="1019.8" y2="486.9" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="449.5" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="1023.6" y1="391.6" x2="1023.6" y2="481.3" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="405.5" width="2.35" height="69.1" fill="var(--up)"/>
<line x1="1027.4" y1="403.8" x2="1027.4" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="406.5" width="2.35" height="66.7" fill="var(--down)"/>
<line x1="1031.2" y1="462.5" x2="1031.2" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="473.9" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="1035.0" y1="447.3" x2="1035.0" y2="479.8" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="465.9" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="1038.7" y1="455.7" x2="1038.7" y2="479.2" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="465.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1042.5" y1="410.4" x2="1042.5" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="411.5" width="2.35" height="51.9" fill="var(--up)"/>
<line x1="1046.3" y1="380.7" x2="1046.3" y2="420.7" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="402.7" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="1050.1" y1="380.7" x2="1050.1" y2="409.5" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="389.2" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="60" y1="360.9" x2="1052" y2="360.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="364.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$221 R1</text>
<text x="1058" y="376.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="246.8" x2="1052" y2="246.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="250.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$299 R2</text>
<text x="1058" y="262.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="80.8" x2="1052" y2="80.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="84.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$413 R3</text>
<text x="1058" y="96.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="462.8" x2="1052" y2="462.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="456.8" font-size="11.5" fill="var(--support)" font-weight="600">$152 S1</text>
<text x="1058" y="468.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="554.8" x2="1052" y2="554.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="548.8" font-size="11.5" fill="var(--support)" font-weight="600">$89 S2</text>
<text x="1058" y="560.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="402.7" r="3" fill="var(--ink)"/>
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
| R3 | $413 | 2 | 2025년 10월(10/6, 5년 최고 $417.86)·2026년 1월(1/12) 스윙 고점 |
| R2 | $299 | 2 | 2025년 6월(6/30)·2026년 3월(3/2) 스윙 고점 |
| R1 | $221 | 3 | 2024년 6월(6/17)·2026년 4월(4/20)·5월(5/25) 스윙 고점 — 서로 다른 시기지만 가격대(±2.5%)가 겹쳐 하나의 클러스터로 묶임 |
| **현재가** | **$192.81** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $152 | 2 | 2024년 8월(8/5)·12월(12/9) 스윙 저점 |
| S2 | $89 | 2 | 2023년 5월(5/22)·6월(6/26) 스윙 저점 |

> 현재가 위쪽 R1($221)은 2024년 중반과 2026년 봄이라는 서로 다른 시기의 스윙 고점이 가격대만으로 겹쳐 하나의 클러스터로 묶인 경우다 — 방법론이 "가격 근접성"만 보고 시간 흐름은 고려하지 않기 때문에 나타나는 현상이며, 실제로는 2년 가까이 떨어진 별개의 저항 시도로 봐야 한다. 5년 최저가($52.03, 2022-01-24)와 그 주변 저점들(3-A. 2021년 하반기~2022년 초 — 금리 인상기 약세장(거시 국면 전환) 참고)은 현재가 대비 너무 멀고 터치 횟수도 표본 기간 초반에 몰려 있어 참고선으로도 포함하지 않았다.

---

## 3. 관측된 특이 구간

### 3-A. 2021년 하반기~2022년 초 — 금리 인상기 약세장(거시 국면 전환)

- 2021-08-16(차트 시작일) 주간 종가 $99.51에서 시작해, 연준 긴축 전환에 따른 성장주 전반의 밸류에이션 조정 국면에서 2022-01-24 주간 저점 **$52.03**(주간 종가 $53.78)까지 약 5개월간 **−47%** 하락했다. 이 주의 거래량은 129만 주로 5년 평균 주간 거래량(약 277만 주)보다는 낮아, 패닉성 급락이라기보다 완만한 다주(多週)간 조정에 가깝다.
- 이 시기는 AeroVironment 고유의 악재라기보다 2022년 전반의 금리 인상기 성장주 전반의 약세장과 궤를 같이한다 — 개별 이벤트가 아니라 거시 국면 전환으로 분류하는 이유다.
- 이후 주가는 2022~2023년에 걸쳐 완만히 회복해 S2($89) 구간을 거쳐 2024년 R1($221) 구간까지 올라섰다 — 저점 이후 약 2년간 4배 가까이 상승한 장기 회복 국면이었다.

### 3-B. 2025-04-28(주간) — BlueHalo 인수 완료(자본구조 단절)

- 2025-05-01 BlueHalo 인수가 완료되며 보통주 약 1,740만 주가 신규 발행됐다(비현금, 인수대가) — 발행주식수가 이후 몇 달 사이 28백만 주대에서 50백만 주대로 79% 급증했다([역사 / 주요 이벤트](./02_history.md), [핵심 지표](./04_metrics.md) 상단 각주 참고).
- 가격 반응 자체는 크지 않았다 — 인수 완료 주간(2025-04-28 주간, 시가 $150.25 → 종가 $158.79) 대비 전주(종가 $149.59) 대비 **+6.2%**로, 이미 2024년부터 예고된 거래였던 만큼 가격에 상당 부분 선반영돼 있었다.
- 다만 이 사건은 **가격보다 주당 지표(BPS·EPS·발행주식수)의 연속성을 깨는 자본구조적 이벤트**라는 점에서 별도로 기록한다 — [핵심 지표](./04_metrics.md) 상단 각주가 지적하듯 FY2025→FY2026 BPS·PBR 비교는 이 단절을 감안해서 읽어야 한다. 이 문서의 가격 패턴(지지·저항 레벨)에는 큰 영향을 남기지 않았지만, 펀더멘털 지표를 이 시점 전후로 비교할 때는 3-A. 2021년 하반기~2022년 초 — 금리 인상기 약세장(거시 국면 전환)와 달리 "가격 차트로는 안 보이는 단절"이라는 점을 유의할 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영 — 조사 기간 내 분할 없음, 배당은 미반영이나 AeroVironment는 배당을 지급한 적이 없어 배당락 영향 자체가 없음)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py AVAV --name AeroVironment --interval 1wk --event 2022-01-24:"금리 인상기 약세장 저점(5년 최저 $52.03)" --event 2025-04-28:"BlueHalo 인수 완료(자본구조 단절)" --close-on 2026-08-14 --emit all` (파라미터는 스크립트 기본값 그대로 사용 — 강제 레벨·기본값 변경 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 2. 지지선 / 저항선 요약에서 확인했듯 R1 클러스터는 2년 가까이 떨어진 두 시기의 스윙이 가격대만으로 묶인 것이다 — 클러스터링이 "가격 근접성"만 보고 시간 간격을 고려하지 않는 방법론적 한계를 그대로 보여주는 사례다.
    - 2025년 5월 BlueHalo 인수(3-B. 2025-04-28(주간) — BlueHalo 인수 완료(자본구조 단절))로 사업 구조·자본구조 자체가 바뀌었다 — 인수 이전(순수 UAS 기업) 스윙 레벨과 이후(우주·사이버·지향성 에너지 포함) 레벨을 같은 펀더멘털 기준으로 비교하면 안 된다는 점을 2. 지지선 / 저항선 요약·3-B. 2025-04-28(주간) — BlueHalo 인수 완료(자본구조 단절)에서 이미 밝혔다.
    - 조사 기간(2021-08~2026-08) 내 주식분할·병합은 없었다 — 소급조정 이슈 없음.

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-23)*
