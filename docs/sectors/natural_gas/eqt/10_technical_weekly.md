# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉으로 다년 가격 구조를 본다. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)에 있다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 마지막 종가 **$55.17(2026-09-04)**는 [일봉 문서](./09_technical_daily.md)·[핵심 지표](./04_metrics.md) A.2가 쓰는 **$55.61(2026-09-03)와 1거래일 차이**다. 수집 시점(2026-09-05)에 주봉 시리즈만 하루 더 반영돼 있었기 때문이며, 두 값의 차이는 0.8%다. **밸류에이션·핵심 지표가 쓰는 기준 종가는 일봉 기준 $55.61로 통일했고, 이 문서의 레벨 표만 주봉 원값을 그대로 둔다.**
    - **주봉 구간에는 2024.07 Equitrans Midstream 재인수(발행주식수 +42%)가 들어 있다.** 분할이 아니므로 과거 주가는 소급 조정되지 않으며, 그 이전과 이후의 주가를 "같은 회사의 같은 지분"으로 비교하면 안 된다([핵심 지표](./04_metrics.md) 상단 주의사항).

---

## 1. 차트 — 최근 5년 주봉 (2021-09-06 ~ 2026-09-04)

<div class="eqt-chart">
<style>
.eqt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eqt-chart svg { width:100%; height:auto; display:block; }
.eqt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eqt-chart .title { fill: var(--ink); font-weight:600; }
.eqt-chart .grid { stroke: var(--grid); stroke-width:1; }
.eqt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="EQT Corporation(EQT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">EQT Corporation (EQT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-04 · 마지막 종가 $55.17 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="583.8" x2="1052" y2="583.8" class="grid"/>
<text x="52" y="587.8" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="478.2" x2="1052" y2="478.2" class="grid"/>
<text x="52" y="482.2" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="372.7" x2="1052" y2="372.7" class="grid"/>
<text x="52" y="376.7" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="267.1" x2="1052" y2="267.1" class="grid"/>
<text x="52" y="271.1" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="161.6" x2="1052" y2="161.6" class="grid"/>
<text x="52" y="165.6" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
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
<line x1="61.9" y1="570.0" x2="61.9" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="577.2" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="65.7" y1="574.9" x2="65.7" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="585.4" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="69.5" y1="579.2" x2="69.5" y2="604.6" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="583.9" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="73.3" y1="553.2" x2="73.3" y2="581.6" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="574.8" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="77.0" y1="558.1" x2="77.0" y2="579.7" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="574.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="80.8" y1="570.5" x2="80.8" y2="590.5" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="571.9" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="84.6" y1="568.4" x2="84.6" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="569.0" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="88.4" y1="553.3" x2="88.4" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="563.8" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="92.2" y1="571.7" x2="92.2" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="577.7" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="96.0" y1="565.8" x2="96.0" y2="592.5" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="569.4" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="99.8" y1="559.3" x2="99.8" y2="579.7" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="567.6" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="103.5" y1="566.1" x2="103.5" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="573.3" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="107.3" y1="570.7" x2="107.3" y2="605.4" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="573.4" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="111.1" y1="571.2" x2="111.1" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="574.7" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="114.9" y1="560.8" x2="114.9" y2="584.0" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="570.5" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="118.7" y1="557.8" x2="118.7" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="561.3" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="122.5" y1="548.2" x2="122.5" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="557.1" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="126.3" y1="548.9" x2="126.3" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="554.1" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="130.0" y1="532.7" x2="130.0" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="543.8" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="133.8" y1="542.4" x2="133.8" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="542.6" width="2.35" height="35.3" fill="var(--down)"/>
<line x1="137.6" y1="568.5" x2="137.6" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="571.7" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="141.4" y1="558.7" x2="141.4" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="567.3" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="145.2" y1="551.9" x2="145.2" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="552.8" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="149.0" y1="541.4" x2="149.0" y2="560.0" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="551.9" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="152.8" y1="552.1" x2="152.8" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="553.2" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="156.5" y1="511.1" x2="156.5" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="516.6" width="2.35" height="41.7" fill="var(--up)"/>
<line x1="160.3" y1="504.0" x2="160.3" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="509.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="164.1" y1="507.4" x2="164.1" y2="538.4" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="508.6" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="167.9" y1="431.0" x2="167.9" y2="503.9" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="432.5" width="2.35" height="71.4" fill="var(--up)"/>
<line x1="171.7" y1="414.0" x2="171.7" y2="451.3" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="414.6" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="175.5" y1="386.1" x2="175.5" y2="420.7" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="390.5" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="179.3" y1="345.4" x2="179.3" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="347.8" width="2.35" height="43.5" fill="var(--up)"/>
<line x1="183.1" y1="314.6" x2="183.1" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="336.1" width="2.35" height="39.3" fill="var(--down)"/>
<line x1="186.8" y1="352.7" x2="186.8" y2="395.9" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="375.3" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="190.6" y1="337.2" x2="190.6" y2="391.7" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="361.6" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="194.4" y1="372.8" x2="194.4" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="373.2" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="198.2" y1="338.4" x2="198.2" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="363.7" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="202.0" y1="276.0" x2="202.0" y2="362.1" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="283.7" width="2.35" height="76.2" fill="var(--up)"/>
<line x1="205.8" y1="262.8" x2="205.8" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="275.5" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="209.6" y1="263.9" x2="209.6" y2="300.9" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="277.4" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="213.3" y1="301.5" x2="213.3" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="304.2" width="2.35" height="111.4" fill="var(--down)"/>
<line x1="217.1" y1="400.8" x2="217.1" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="407.7" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="220.9" y1="380.8" x2="220.9" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="418.9" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="224.7" y1="424.8" x2="224.7" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="433.9" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="228.5" y1="397.7" x2="228.5" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="408.3" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="232.3" y1="331.1" x2="232.3" y2="401.2" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="349.1" width="2.35" height="52.0" fill="var(--up)"/>
<line x1="236.1" y1="301.8" x2="236.1" y2="350.9" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="330.1" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="239.8" y1="337.0" x2="239.8" y2="370.7" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="340.6" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="243.6" y1="306.2" x2="243.6" y2="359.2" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="307.3" width="2.35" height="45.5" fill="var(--up)"/>
<line x1="247.4" y1="277.1" x2="247.4" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="291.4" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="251.2" y1="248.9" x2="251.2" y2="297.3" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="270.6" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="255.0" y1="252.3" x2="255.0" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="278.2" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="258.8" y1="277.1" x2="258.8" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="284.5" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="262.6" y1="246.3" x2="262.6" y2="323.7" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="280.7" width="2.35" height="28.0" fill="var(--down)"/>
<line x1="266.4" y1="287.5" x2="266.4" y2="375.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="320.2" width="2.35" height="39.2" fill="var(--down)"/>
<line x1="270.1" y1="358.1" x2="270.1" y2="392.2" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="364.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="273.9" y1="310.3" x2="273.9" y2="364.8" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="339.2" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="277.7" y1="321.6" x2="277.7" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="332.0" width="2.35" height="28.7" fill="var(--down)"/>
<line x1="281.5" y1="333.3" x2="281.5" y2="399.3" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="361.2" width="2.35" height="33.9" fill="var(--down)"/>
<line x1="285.3" y1="361.1" x2="285.3" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="386.6" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="289.1" y1="346.1" x2="289.1" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="361.3" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="292.9" y1="322.5" x2="292.9" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="345.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="296.6" y1="324.9" x2="296.6" y2="373.9" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="336.7" width="2.35" height="25.1" fill="var(--down)"/>
<line x1="300.4" y1="320.1" x2="300.4" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="340.7" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="304.2" y1="336.9" x2="304.2" y2="377.7" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="357.4" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="308.0" y1="374.5" x2="308.0" y2="421.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="378.8" width="2.35" height="39.6" fill="var(--down)"/>
<line x1="311.8" y1="381.4" x2="311.8" y2="411.9" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="401.8" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="315.6" y1="403.2" x2="315.6" y2="431.2" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="408.8" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="319.4" y1="404.1" x2="319.4" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="409.6" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="323.1" y1="435.4" x2="323.1" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="443.0" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="326.9" y1="422.0" x2="326.9" y2="445.2" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="427.4" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="330.7" y1="415.1" x2="330.7" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="421.6" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="334.5" y1="420.7" x2="334.5" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="430.9" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="338.3" y1="448.1" x2="338.3" y2="468.9" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="455.0" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="342.1" y1="459.6" x2="342.1" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="460.6" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="345.9" y1="444.8" x2="345.9" y2="478.6" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="464.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="349.6" y1="427.9" x2="349.6" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="428.3" width="2.35" height="36.3" fill="var(--up)"/>
<line x1="353.4" y1="427.6" x2="353.4" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="428.1" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="357.2" y1="441.0" x2="357.2" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="444.2" width="2.35" height="29.7" fill="var(--down)"/>
<line x1="361.0" y1="463.6" x2="361.0" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="481.2" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="364.8" y1="465.9" x2="364.8" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="472.3" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="368.6" y1="452.6" x2="368.6" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="458.1" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="372.4" y1="447.6" x2="372.4" y2="464.4" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="448.2" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="376.2" y1="437.2" x2="376.2" y2="454.4" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="445.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="379.9" y1="433.7" x2="379.9" y2="455.4" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="437.2" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="383.7" y1="423.3" x2="383.7" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="427.1" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="387.5" y1="426.9" x2="387.5" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="431.8" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="391.3" y1="440.3" x2="391.3" y2="461.5" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="441.8" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="395.1" y1="399.1" x2="395.1" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="412.5" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="398.9" y1="406.5" x2="398.9" y2="421.5" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="413.9" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="402.7" y1="404.9" x2="402.7" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="409.1" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="406.4" y1="381.0" x2="406.4" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="388.0" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="410.2" y1="371.5" x2="410.2" y2="396.1" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="376.5" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="414.0" y1="372.7" x2="414.0" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="375.8" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="417.8" y1="357.8" x2="417.8" y2="379.6" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="360.7" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="421.6" y1="358.6" x2="421.6" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="363.2" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="425.4" y1="362.1" x2="425.4" y2="392.7" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="377.6" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="429.2" y1="360.9" x2="429.2" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="373.7" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="432.9" y1="344.7" x2="432.9" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="348.6" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="436.7" y1="345.5" x2="436.7" y2="373.4" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="353.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="440.5" y1="326.6" x2="440.5" y2="362.1" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="340.5" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="444.3" y1="334.8" x2="444.3" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="336.0" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="448.1" y1="321.2" x2="448.1" y2="358.1" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="330.4" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="451.9" y1="327.9" x2="451.9" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="328.1" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="455.7" y1="330.3" x2="455.7" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="331.1" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="459.5" y1="330.5" x2="459.5" y2="358.3" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="343.9" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="463.2" y1="352.6" x2="463.2" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="357.5" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="467.0" y1="364.6" x2="467.0" y2="392.0" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="366.5" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="470.8" y1="339.1" x2="470.8" y2="386.9" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="343.2" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="474.6" y1="324.6" x2="474.6" y2="344.9" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="337.1" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="478.4" y1="323.5" x2="478.4" y2="353.6" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="335.7" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="482.2" y1="338.8" x2="482.2" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="352.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="486.0" y1="317.5" x2="486.0" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="322.8" width="2.35" height="34.2" fill="var(--up)"/>
<line x1="489.7" y1="325.5" x2="489.7" y2="387.2" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="328.4" width="2.35" height="53.4" fill="var(--down)"/>
<line x1="493.5" y1="354.5" x2="493.5" y2="381.0" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="368.8" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="497.3" y1="361.1" x2="497.3" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="363.7" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="501.1" y1="364.3" x2="501.1" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="367.3" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="504.9" y1="373.6" x2="504.9" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="376.4" width="2.35" height="26.6" fill="var(--down)"/>
<line x1="508.7" y1="384.7" x2="508.7" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="389.1" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="512.5" y1="377.3" x2="512.5" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="380.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="516.2" y1="373.9" x2="516.2" y2="386.8" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="383.2" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="520.0" y1="379.0" x2="520.0" y2="398.5" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="382.1" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="523.8" y1="387.5" x2="523.8" y2="404.1" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="393.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="527.6" y1="400.4" x2="527.6" y2="429.2" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="405.3" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="531.4" y1="412.4" x2="531.4" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="416.2" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="535.2" y1="409.6" x2="535.2" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="417.3" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="539.0" y1="426.7" x2="539.0" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="427.8" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="542.7" y1="421.6" x2="542.7" y2="456.4" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="428.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="546.5" y1="391.2" x2="546.5" y2="440.8" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="404.2" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="550.3" y1="396.9" x2="550.3" y2="410.8" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="399.8" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="554.1" y1="390.5" x2="554.1" y2="403.3" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="395.4" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="557.9" y1="420.5" x2="557.9" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="426.5" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="561.7" y1="431.7" x2="561.7" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="432.2" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="565.5" y1="400.1" x2="565.5" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="403.6" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="569.3" y1="395.5" x2="569.3" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="400.8" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="573.0" y1="389.5" x2="573.0" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="401.7" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="576.8" y1="397.6" x2="576.8" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="401.2" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="580.6" y1="361.7" x2="580.6" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="366.2" width="2.35" height="43.5" fill="var(--up)"/>
<line x1="584.4" y1="357.1" x2="584.4" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="367.2" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="588.2" y1="357.1" x2="588.2" y2="386.0" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="363.9" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="592.0" y1="350.2" x2="592.0" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="360.3" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="595.8" y1="346.8" x2="595.8" y2="375.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="357.6" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="599.5" y1="354.7" x2="599.5" y2="369.1" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="361.2" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="603.3" y1="350.7" x2="603.3" y2="372.2" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="352.6" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="607.1" y1="353.9" x2="607.1" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="363.8" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="610.9" y1="378.2" x2="610.9" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="381.6" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="614.7" y1="386.7" x2="614.7" y2="406.4" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="401.7" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="618.5" y1="397.6" x2="618.5" y2="414.6" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="405.4" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="622.3" y1="398.3" x2="622.3" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="402.1" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="626.0" y1="400.2" x2="626.0" y2="426.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="401.7" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="629.8" y1="407.8" x2="629.8" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="411.8" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="633.6" y1="421.8" x2="633.6" y2="463.3" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="430.8" width="2.35" height="30.8" fill="var(--down)"/>
<line x1="637.4" y1="460.6" x2="637.4" y2="478.0" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="466.6" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="641.2" y1="453.1" x2="641.2" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="455.5" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="645.0" y1="437.1" x2="645.0" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="439.8" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="648.8" y1="434.4" x2="648.8" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="437.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="652.5" y1="438.6" x2="652.5" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="446.1" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="656.3" y1="437.1" x2="656.3" y2="462.8" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="444.6" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="660.1" y1="423.9" x2="660.1" y2="447.7" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="427.2" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="663.9" y1="403.2" x2="663.9" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="409.3" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="667.7" y1="392.1" x2="667.7" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="405.0" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="671.5" y1="398.4" x2="671.5" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="400.0" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="675.3" y1="402.2" x2="675.3" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="403.0" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="679.1" y1="396.2" x2="679.1" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="399.3" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="682.8" y1="385.0" x2="682.8" y2="420.7" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="405.4" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="686.6" y1="356.0" x2="686.6" y2="419.1" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="359.8" width="2.35" height="58.3" fill="var(--up)"/>
<line x1="690.4" y1="327.5" x2="690.4" y2="352.3" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="344.1" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="694.2" y1="288.0" x2="694.2" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="310.2" width="2.35" height="30.9" fill="var(--up)"/>
<line x1="698.0" y1="289.1" x2="698.0" y2="322.0" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="292.7" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="701.8" y1="314.2" x2="701.8" y2="338.8" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="319.9" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="705.6" y1="306.1" x2="705.6" y2="343.9" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="313.7" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="709.3" y1="311.2" x2="709.3" y2="348.7" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="313.7" width="2.35" height="27.4" fill="var(--down)"/>
<line x1="713.1" y1="320.1" x2="713.1" y2="342.6" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="327.1" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="716.9" y1="284.7" x2="716.9" y2="319.3" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="298.6" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="720.7" y1="266.8" x2="720.7" y2="295.6" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="277.7" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="724.5" y1="225.1" x2="724.5" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="235.9" width="2.35" height="40.7" fill="var(--up)"/>
<line x1="728.3" y1="215.9" x2="728.3" y2="243.6" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="228.3" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="732.1" y1="245.3" x2="732.1" y2="292.5" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="253.8" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="735.8" y1="229.5" x2="735.8" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="248.0" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="739.6" y1="219.3" x2="739.6" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="230.9" width="2.35" height="19.5" fill="var(--up)"/>
<line x1="743.4" y1="196.8" x2="743.4" y2="269.3" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="228.9" width="2.35" height="35.7" fill="var(--down)"/>
<line x1="747.2" y1="260.2" x2="747.2" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="266.4" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="751.0" y1="254.3" x2="751.0" y2="318.0" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="279.3" width="2.35" height="19.5" fill="var(--down)"/>
<line x1="754.8" y1="257.8" x2="754.8" y2="304.8" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="259.5" width="2.35" height="34.7" fill="var(--up)"/>
<line x1="758.6" y1="219.6" x2="758.6" y2="261.9" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="236.7" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="762.4" y1="210.7" x2="762.4" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="230.9" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="766.1" y1="211.7" x2="766.1" y2="335.0" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="238.7" width="2.35" height="69.5" fill="var(--down)"/>
<line x1="769.9" y1="258.0" x2="769.9" y2="324.6" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="270.8" width="2.35" height="53.0" fill="var(--up)"/>
<line x1="773.7" y1="246.6" x2="773.7" y2="271.7" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="256.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="777.5" y1="262.8" x2="777.5" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="264.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="781.3" y1="247.0" x2="781.3" y2="278.4" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="247.6" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="785.1" y1="207.5" x2="785.1" y2="247.5" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="207.8" width="2.35" height="38.7" fill="var(--up)"/>
<line x1="788.9" y1="192.8" x2="788.9" y2="224.8" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="203.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="792.6" y1="189.3" x2="792.6" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="207.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="796.4" y1="192.9" x2="796.4" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="202.9" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="800.2" y1="191.2" x2="800.2" y2="215.0" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="199.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="804.0" y1="193.6" x2="804.0" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="194.9" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="807.8" y1="153.1" x2="807.8" y2="194.4" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="156.9" width="2.35" height="37.0" fill="var(--up)"/>
<line x1="811.6" y1="150.8" x2="811.6" y2="187.2" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="153.1" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="815.4" y1="173.4" x2="815.4" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="182.9" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="819.1" y1="194.3" x2="819.1" y2="231.0" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="210.8" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="822.9" y1="158.3" x2="822.9" y2="210.2" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="170.1" width="2.35" height="39.5" fill="var(--up)"/>
<line x1="826.7" y1="182.8" x2="826.7" y2="253.8" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="184.8" width="2.35" height="59.2" fill="var(--down)"/>
<line x1="830.5" y1="219.8" x2="830.5" y2="255.8" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="240.2" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="834.3" y1="237.6" x2="834.3" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="241.0" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="838.1" y1="231.4" x2="838.1" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="237.0" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="841.9" y1="237.1" x2="841.9" y2="273.4" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="246.3" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="845.6" y1="233.7" x2="845.6" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="247.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="849.4" y1="235.4" x2="849.4" y2="261.7" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="250.2" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="853.2" y1="240.1" x2="853.2" y2="266.7" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="241.9" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="857.0" y1="255.9" x2="857.0" y2="283.3" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="258.6" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="860.8" y1="214.8" x2="860.8" y2="281.9" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="224.3" width="2.35" height="53.2" fill="var(--up)"/>
<line x1="864.6" y1="189.5" x2="864.6" y2="229.0" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="203.5" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="868.4" y1="187.4" x2="868.4" y2="234.3" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="197.5" width="2.35" height="36.6" fill="var(--down)"/>
<line x1="872.2" y1="201.4" x2="872.2" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="224.0" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="875.9" y1="192.7" x2="875.9" y2="245.2" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="210.6" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="879.7" y1="221.2" x2="879.7" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="226.6" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="883.5" y1="182.8" x2="883.5" y2="230.9" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="183.0" width="2.35" height="44.6" fill="var(--up)"/>
<line x1="887.3" y1="148.3" x2="887.3" y2="183.7" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="162.6" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="891.1" y1="154.6" x2="891.1" y2="213.0" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="165.9" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="894.9" y1="149.2" x2="894.9" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="152.5" width="2.35" height="43.3" fill="var(--up)"/>
<line x1="898.7" y1="138.0" x2="898.7" y2="177.5" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="154.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="902.4" y1="156.4" x2="902.4" y2="214.1" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="157.1" width="2.35" height="51.2" fill="var(--down)"/>
<line x1="906.2" y1="208.2" x2="906.2" y2="238.2" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="208.3" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="910.0" y1="217.1" x2="910.0" y2="234.1" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="225.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="913.8" y1="212.2" x2="913.8" y2="240.4" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="224.9" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="917.6" y1="217.6" x2="917.6" y2="262.4" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="236.5" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="921.4" y1="234.0" x2="921.4" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="251.3" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="925.2" y1="199.2" x2="925.2" y2="257.4" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="208.8" width="2.35" height="28.4" fill="var(--up)"/>
<line x1="928.9" y1="179.7" x2="928.9" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="185.5" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="932.7" y1="193.3" x2="932.7" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="195.4" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="936.5" y1="172.0" x2="936.5" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="175.3" width="2.35" height="33.1" fill="var(--up)"/>
<line x1="940.3" y1="148.5" x2="940.3" y2="205.8" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="156.3" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="944.1" y1="142.9" x2="944.1" y2="186.6" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="146.6" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="947.9" y1="129.3" x2="947.9" y2="160.3" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="137.4" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="951.7" y1="105.2" x2="951.7" y2="147.5" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="115.4" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="955.5" y1="86.1" x2="955.5" y2="166.8" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="112.3" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="959.2" y1="74.6" x2="959.2" y2="129.8" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="81.9" width="2.35" height="44.5" fill="var(--up)"/>
<line x1="963.0" y1="79.9" x2="963.0" y2="167.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="82.8" width="2.35" height="81.9" fill="var(--down)"/>
<line x1="966.8" y1="145.2" x2="966.8" y2="181.7" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="166.3" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="970.6" y1="172.4" x2="970.6" y2="199.8" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="174.4" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="974.4" y1="166.8" x2="974.4" y2="201.0" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="173.1" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="978.2" y1="153.1" x2="978.2" y2="181.3" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="166.2" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="982.0" y1="163.3" x2="982.0" y2="211.1" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="174.2" width="2.35" height="30.0" fill="var(--down)"/>
<line x1="985.7" y1="190.9" x2="985.7" y2="213.2" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="198.5" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="989.5" y1="163.7" x2="989.5" y2="202.8" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="183.5" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="993.3" y1="183.4" x2="993.3" y2="219.3" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="186.2" width="2.35" height="28.9" fill="var(--down)"/>
<line x1="997.1" y1="206.7" x2="997.1" y2="228.4" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="215.4" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="1000.9" y1="224.7" x2="1000.9" y2="255.6" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="230.2" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="1004.7" y1="244.2" x2="1004.7" y2="264.5" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="259.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1008.5" y1="229.1" x2="1008.5" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="238.6" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="1012.2" y1="227.6" x2="1012.2" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="239.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1016.0" y1="238.4" x2="1016.0" y2="288.9" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="240.1" width="2.35" height="39.2" fill="var(--down)"/>
<line x1="1019.8" y1="261.8" x2="1019.8" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="271.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="1023.6" y1="216.3" x2="1023.6" y2="282.3" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="235.1" width="2.35" height="38.4" fill="var(--up)"/>
<line x1="1027.4" y1="231.8" x2="1027.4" y2="254.2" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="232.4" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="1031.2" y1="227.6" x2="1031.2" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="238.5" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="1035.0" y1="212.7" x2="1035.0" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="220.5" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="1038.7" y1="217.8" x2="1038.7" y2="242.0" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="221.0" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="1042.5" y1="198.8" x2="1042.5" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="218.9" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="1046.3" y1="198.3" x2="1046.3" y2="225.6" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="204.3" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="1050.1" y1="208.2" x2="1050.1" y2="218.7" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="209.5" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="60" y1="203.8" x2="1052" y2="203.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="207.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$56 R1</text>
<text x="1058" y="219.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="144.4" x2="1052" y2="144.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="147.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$62 R2</text>
<text x="1058" y="159.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="282.3" x2="1052" y2="282.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="276.3" font-size="11.5" fill="var(--support)" font-weight="600">$49 S1</text>
<text x="1058" y="288.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="393.2" x2="1052" y2="393.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="387.2" font-size="11.5" fill="var(--support)" font-weight="600">$38 S2</text>
<text x="1058" y="399.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="422.2" x2="1052" y2="422.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.2" font-size="11.5" fill="var(--support)" font-weight="600">$35 S3</text>
<text x="1058" y="428.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="212.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="204.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $55 (2026-09-04)</text>
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
| R2 | $62 | 2 | 2025-06·2025-12 고점대 — 2026-03 사상 최고($68.24) 직전의 마지막 저항 |
| R1 | $56 | 2 | 2025-02·2025-03 고점대 — **현재가 바로 위** |
| **현재가** | **$55.17** (2026-09-04 종가) | — | R1과 S1 사이 |
| S1 | $49 | 3 | 2025-09·2026-01·2026-07 — 최근 1년 내 세 차례 확인된 지지 |
| S2 | $38 | 2 | 2023-07·2023-09 — 가스 가격 약세기의 박스권 하단 |
| S3 | $35 | 3 | 2022-05·2023-12·2024-10 — 5년 중 가장 여러 번 확인된 저점대 |
| 참고선 | $68.24 / $17.95 | — | 5년 최고(2026-03-23 주) / 최저(2021-11-29 주). 각각 단발 극단값이라 지지·저항으로 쓰지 않는다 |

**5년 구조는 계단식 상승이다.** S3($35) → S2($38) → S1($49)로 지지대 자체가 올라왔고, 각 지지대는 가스 가격 사이클의 저점 구간과 겹친다. 다만 **저항 쪽 클러스터는 2개뿐**이고 그중 R1($56)은 현재가 바로 위다 — 위쪽으로는 검증된 레벨이 얇다는 뜻이며, 2026-03 고점 $68.24까지는 반복 확인된 레벨이 없다.

---

## 3. 관측된 특이 구간 — 2026-03~2026-07 고점 대비 −30% 조정

- 2026-03-23 주에 5년 최고 **$68.24**를 찍은 뒤 2026-07-10 주 저점 **$47.94**까지 약 4개월간 **−29.8%** 하락했다. 실적 악화가 아니라 **가스 가격의 계절적 약세와 그에 따른 실현가 하락**이 겹친 구간이다(Q1 2026 실현가 $5.08 → Q2 2026 $2.65/Mcfe, [핵심 지표](./04_metrics.md) C절).
- 이 하락이 S1($49)의 세 번째 터치를 만들었고, 그 직후 [일봉 문서](./09_technical_daily.md) 3절의 2026-07-22 갭업으로 반등했다.
- **이 구간이 주는 함의는 하나다** — 이 종목의 연중 변동폭은 실적 사이클이 아니라 **분기 실현가의 계절성**을 따른다. 5년 차트에서 반복적으로 관찰되는 패턴이며, 특정 시점의 주가를 "구조적 재평가"로 읽기 전에 계절 요인부터 걷어내야 한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-06~2026-09-04. 수집 시점: 2026-09-05. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py EQT --name "EQT Corporation" --interval 1wk --close-on 2026-09-03 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **저항 레벨이 2개뿐이다.** 터치 2회 이상 조건을 만족하는 고점 클러스터가 실제로 둘뿐이라 억지로 셋을 만들지 않았다 — 5년 중 상단 구간에 머문 기간이 짧았다는 뜻이기도 하다.
    - **`--close-on 2026-09-03`을 넣었으나 그날이 주봉 시리즈의 마지막 봉과 일치하지 않아** 표에는 스크립트가 잡은 마지막 주봉 종가($55.17, 2026-09-04)가 들어갔다. 위 대조 블록에 그 차이를 남겼다.
    - **기간 내 주식분할은 없었고, 원주가라 배당(19회)은 반영되지 않았다.** 다만 2024.07 Equitrans 재인수로 발행주식수가 42% 늘었다 — 분할이 아니라 소급 조정 대상이 아니지만, **2024년 이전 구간의 주가 레벨을 현재와 직접 비교할 때는 이 사실을 감안해야 한다.**

---

*작성일: 2026-09-05*
