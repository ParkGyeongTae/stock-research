# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **2026-08-18 종가 $8.64는 핵심 지표 A.2·밸류에이션 / 적정주가 6. 목표주가 요약에 인용된 stockanalysis.com 값과 일치한다.**
>
> ⚠️ 이 회사는 최근 1년간 52주 최고 $57.42 → 최저 $7.21로 극단적인 변동성을 보였다(약 −87% 낙폭) — 아래 지지/저항 레벨은 유효 클러스터(터치 2회 이상)가 1개(R1)뿐일 정도로 스윙 구조 자체가 불안정하다. 이 회사를 볼 때 기술적 레벨보다 최근 뉴스 / 이슈의 이벤트 로그(특히 2025-11-06 실적발표)가 가격 움직임을 훨씬 더 잘 설명한다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-19 ~ 2026-08-18)

<div class="smr-chart">
<style>
.smr-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .smr-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .smr-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.smr-chart svg { width:100%; height:auto; display:block; }
.smr-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.smr-chart .title { fill: var(--ink); font-weight:600; }
.smr-chart .grid { stroke: var(--grid); stroke-width:1; }
.smr-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NuScale Power(SMR) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">NuScale Power (SMR) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-19 ~ 2026-08-18 · 마지막 종가 $8.64 (2026-08-18) · 단위 USD</text>
<line x1="60" y1="573.2" x2="1052" y2="573.2" class="grid"/>
<text x="52" y="577.2" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="467.7" x2="1052" y2="467.7" class="grid"/>
<text x="52" y="471.7" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="362.1" x2="1052" y2="362.1" class="grid"/>
<text x="52" y="366.1" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="256.6" x2="1052" y2="256.6" class="grid"/>
<text x="52" y="260.6" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="151.0" x2="1052" y2="151.0" class="grid"/>
<text x="52" y="155.0" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="97.5" y1="626.0" x2="97.5" y2="631.0" class="axis"/>
<text x="97.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="180.5" y1="626.0" x2="180.5" y2="631.0" class="axis"/>
<text x="180.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="271.4" y1="626.0" x2="271.4" y2="631.0" class="axis"/>
<text x="271.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="346.5" y1="626.0" x2="346.5" y2="631.0" class="axis"/>
<text x="346.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="433.5" y1="626.0" x2="433.5" y2="631.0" class="axis"/>
<text x="433.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="512.5" y1="626.0" x2="512.5" y2="631.0" class="axis"/>
<text x="512.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="587.6" y1="626.0" x2="587.6" y2="631.0" class="axis"/>
<text x="587.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="674.6" y1="626.0" x2="674.6" y2="631.0" class="axis"/>
<text x="674.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="757.6" y1="626.0" x2="757.6" y2="631.0" class="axis"/>
<text x="757.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="836.6" y1="626.0" x2="836.6" y2="631.0" class="axis"/>
<text x="836.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="919.6" y1="626.0" x2="919.6" y2="631.0" class="axis"/>
<text x="919.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1006.5" y1="626.0" x2="1006.5" y2="631.0" class="axis"/>
<text x="1006.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="72.7" x2="1052" y2="72.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="75.7" font-size="10.5" fill="var(--muted)">$57 52주 최고</text>
<line x1="283.3" y1="56.0" x2="283.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="289.3" y="68.0" font-size="10.5" fill="var(--down)">2025-11-06 3분기 실적발표(Milestone Contribution 갭다운)</text>
<line x1="62.0" y1="306.0" x2="62.0" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="308.8" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="65.9" y1="319.6" x2="65.9" y2="355.6" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="322.1" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="69.9" y1="311.8" x2="69.9" y2="330.0" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="313.2" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="73.8" y1="303.8" x2="73.8" y2="334.6" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="308.9" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="77.8" y1="293.9" x2="77.8" y2="316.7" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="298.4" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="81.7" y1="275.6" x2="81.7" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="297.2" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="85.7" y1="294.2" x2="85.7" y2="310.9" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="298.1" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="89.6" y1="286.1" x2="89.6" y2="303.4" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="293.7" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="93.6" y1="292.7" x2="93.6" y2="316.7" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="295.6" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="97.5" y1="272.5" x2="97.5" y2="334.7" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="285.7" width="2.45" height="43.7" fill="var(--up)"/>
<line x1="101.5" y1="223.7" x2="101.5" y2="272.4" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="252.1" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="105.5" y1="245.2" x2="105.5" y2="299.8" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="247.4" width="2.45" height="51.1" fill="var(--down)"/>
<line x1="109.4" y1="281.4" x2="109.4" y2="314.6" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="281.4" width="2.45" height="32.9" fill="var(--down)"/>
<line x1="113.4" y1="303.3" x2="113.4" y2="321.8" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="310.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="117.3" y1="305.5" x2="117.3" y2="320.1" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="305.7" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="121.3" y1="291.4" x2="121.3" y2="316.6" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="293.9" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="125.2" y1="303.0" x2="125.2" y2="315.7" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="307.4" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="129.2" y1="293.2" x2="129.2" y2="312.2" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="295.2" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="133.1" y1="262.3" x2="133.1" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="266.2" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="137.1" y1="267.1" x2="137.1" y2="290.8" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="274.5" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="141.0" y1="288.2" x2="141.0" y2="308.0" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="288.5" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="145.0" y1="245.7" x2="145.0" y2="295.1" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="276.4" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="148.9" y1="182.7" x2="148.9" y2="267.1" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="185.1" width="2.45" height="79.9" fill="var(--up)"/>
<line x1="152.9" y1="179.9" x2="152.9" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="203.8" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="156.8" y1="206.9" x2="156.8" y2="245.3" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="209.1" width="2.45" height="30.2" fill="var(--down)"/>
<line x1="160.8" y1="231.3" x2="160.8" y2="264.9" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="232.8" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="164.7" y1="264.5" x2="164.7" y2="296.8" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="277.7" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="168.7" y1="268.7" x2="168.7" y2="288.6" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="277.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="172.6" y1="253.1" x2="172.6" y2="279.6" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="259.2" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="176.6" y1="279.7" x2="176.6" y2="299.6" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="285.1" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="180.5" y1="287.7" x2="180.5" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="292.3" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="184.5" y1="260.9" x2="184.5" y2="288.6" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="261.7" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="188.4" y1="243.4" x2="188.4" y2="270.6" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="255.3" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="192.4" y1="214.8" x2="192.4" y2="242.6" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="236.1" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="196.4" y1="212.2" x2="196.4" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="232.2" width="2.45" height="32.7" fill="var(--down)"/>
<line x1="200.3" y1="249.9" x2="200.3" y2="278.5" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="258.0" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="204.3" y1="239.6" x2="204.3" y2="273.2" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="250.1" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="208.2" y1="205.6" x2="208.2" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="245.8" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="212.2" y1="189.0" x2="212.2" y2="238.6" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="203.6" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="216.1" y1="178.2" x2="216.1" y2="239.4" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="195.4" width="2.45" height="26.2" fill="var(--up)"/>
<line x1="220.1" y1="86.0" x2="220.1" y2="172.6" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="114.8" width="2.45" height="54.8" fill="var(--up)"/>
<line x1="224.0" y1="72.7" x2="224.0" y2="177.3" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="84.2" width="2.45" height="91.7" fill="var(--down)"/>
<line x1="228.0" y1="165.0" x2="228.0" y2="228.4" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="172.1" width="2.45" height="39.6" fill="var(--down)"/>
<line x1="231.9" y1="189.1" x2="231.9" y2="220.6" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="189.1" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="235.9" y1="238.2" x2="235.9" y2="274.3" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="244.6" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="239.8" y1="268.2" x2="239.8" y2="333.7" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="270.1" width="2.45" height="42.2" fill="var(--down)"/>
<line x1="243.8" y1="274.9" x2="243.8" y2="315.9" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="282.3" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="247.7" y1="253.4" x2="247.7" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="267.1" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="251.7" y1="260.9" x2="251.7" y2="289.0" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="268.5" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="255.6" y1="209.3" x2="255.6" y2="265.3" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="234.2" width="2.45" height="24.9" fill="var(--up)"/>
<line x1="259.6" y1="209.8" x2="259.6" y2="251.0" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="223.1" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="263.5" y1="210.4" x2="263.5" y2="249.2" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="232.8" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="267.5" y1="198.1" x2="267.5" y2="234.6" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="205.2" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="271.4" y1="214.4" x2="271.4" y2="252.4" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="217.1" width="2.45" height="30.7" fill="var(--down)"/>
<line x1="275.4" y1="254.9" x2="275.4" y2="302.8" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="261.8" width="2.45" height="40.8" fill="var(--down)"/>
<line x1="279.3" y1="263.4" x2="279.3" y2="286.0" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="275.3" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="283.3" y1="283.9" x2="283.3" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="285.7" width="2.45" height="50.5" fill="var(--down)"/>
<line x1="287.3" y1="356.8" x2="287.3" y2="396.3" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="358.5" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="291.2" y1="340.0" x2="291.2" y2="387.9" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="340.4" width="2.45" height="38.3" fill="var(--down)"/>
<line x1="295.2" y1="381.9" x2="295.2" y2="400.1" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="383.2" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="299.1" y1="385.5" x2="299.1" y2="408.7" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="393.3" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="303.1" y1="408.9" x2="303.1" y2="438.4" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="408.9" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="307.0" y1="431.2" x2="307.0" y2="451.2" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="441.8" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="311.0" y1="440.8" x2="311.0" y2="461.8" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="443.4" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="314.9" y1="442.6" x2="314.9" y2="460.3" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="451.4" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="318.9" y1="445.0" x2="318.9" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="445.6" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="322.8" y1="439.3" x2="322.8" y2="482.7" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="440.0" width="2.45" height="41.4" fill="var(--down)"/>
<line x1="326.8" y1="478.0" x2="326.8" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="478.0" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="330.7" y1="467.9" x2="330.7" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="468.3" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="334.7" y1="470.0" x2="334.7" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="470.0" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="338.6" y1="475.6" x2="338.6" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="477.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="342.6" y1="464.7" x2="342.6" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="467.7" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="346.5" y1="474.7" x2="346.5" y2="488.3" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="475.3" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="350.5" y1="471.4" x2="350.5" y2="484.5" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="479.2" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="354.4" y1="464.3" x2="354.4" y2="486.6" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="466.2" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="358.4" y1="432.3" x2="358.4" y2="472.9" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="437.6" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="362.3" y1="442.1" x2="362.3" y2="453.9" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="443.0" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="366.3" y1="436.4" x2="366.3" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="442.9" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="370.2" y1="447.1" x2="370.2" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="453.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="374.2" y1="455.9" x2="374.2" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="461.1" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="378.2" y1="454.4" x2="378.2" y2="480.2" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="454.8" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="382.1" y1="458.2" x2="382.1" y2="485.3" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="458.8" width="2.45" height="26.4" fill="var(--down)"/>
<line x1="386.1" y1="481.3" x2="386.1" y2="495.4" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="481.6" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="390.0" y1="493.0" x2="390.0" y2="503.4" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="498.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="394.0" y1="496.7" x2="394.0" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="498.5" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="397.9" y1="501.1" x2="397.9" y2="513.5" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="504.8" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="401.9" y1="503.5" x2="401.9" y2="510.5" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="509.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="405.8" y1="496.6" x2="405.8" y2="508.3" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="504.2" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="409.8" y1="506.6" x2="409.8" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="508.3" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="413.7" y1="508.5" x2="413.7" y2="514.9" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="509.0" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="417.7" y1="511.0" x2="417.7" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="511.0" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="421.6" y1="517.4" x2="421.6" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="525.9" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="425.6" y1="523.2" x2="425.6" y2="530.3" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="524.3" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="429.5" y1="526.5" x2="429.5" y2="531.2" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="527.7" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="433.5" y1="504.9" x2="433.5" y2="527.6" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="506.6" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="437.4" y1="472.4" x2="437.4" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="480.5" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="441.4" y1="465.3" x2="441.4" y2="487.0" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="472.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="445.3" y1="464.8" x2="445.3" y2="483.7" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="473.3" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="449.3" y1="467.9" x2="449.3" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="471.1" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="453.2" y1="443.5" x2="453.2" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="451.9" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="457.2" y1="463.1" x2="457.2" y2="472.7" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="464.3" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="461.1" y1="464.5" x2="461.1" y2="477.5" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="466.8" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="465.1" y1="467.8" x2="465.1" y2="483.8" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="469.5" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="469.1" y1="468.5" x2="469.1" y2="480.0" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="469.3" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="473.0" y1="461.9" x2="473.0" y2="479.7" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="465.7" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="477.0" y1="466.8" x2="477.0" y2="479.4" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="474.2" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="480.9" y1="455.5" x2="480.9" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="466.0" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="484.9" y1="456.5" x2="484.9" y2="470.1" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="460.9" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="488.8" y1="458.8" x2="488.8" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="459.0" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="492.8" y1="467.0" x2="492.8" y2="485.9" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="472.9" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="496.7" y1="474.8" x2="496.7" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="476.1" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="500.7" y1="457.9" x2="500.7" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="462.6" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="504.6" y1="466.9" x2="504.6" y2="487.4" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="470.0" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="508.6" y1="476.9" x2="508.6" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="483.8" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="512.5" y1="494.9" x2="512.5" y2="506.0" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="496.5" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="516.5" y1="489.2" x2="516.5" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="490.0" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="520.4" y1="492.4" x2="520.4" y2="518.5" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="492.6" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="524.4" y1="510.5" x2="524.4" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="510.7" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="528.3" y1="490.1" x2="528.3" y2="515.5" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="493.7" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="532.3" y1="490.6" x2="532.3" y2="502.1" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="492.2" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="536.2" y1="491.2" x2="536.2" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="494.8" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="540.2" y1="500.4" x2="540.2" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="501.1" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="544.1" y1="504.2" x2="544.1" y2="531.3" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="504.4" width="2.45" height="26.7" fill="var(--down)"/>
<line x1="548.1" y1="522.9" x2="548.1" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="527.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="552.0" y1="526.2" x2="552.0" y2="538.0" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="528.1" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="556.0" y1="524.6" x2="556.0" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="528.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="560.0" y1="524.0" x2="560.0" y2="536.2" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="524.2" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="563.9" y1="525.1" x2="563.9" y2="538.1" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="528.4" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="567.9" y1="539.4" x2="567.9" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="540.3" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="571.8" y1="536.4" x2="571.8" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="537.0" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="575.8" y1="535.5" x2="575.8" y2="541.2" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="536.2" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="579.7" y1="536.5" x2="579.7" y2="545.4" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="538.1" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="583.7" y1="536.8" x2="583.7" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="539.4" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="587.6" y1="536.5" x2="587.6" y2="549.3" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="541.0" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="591.6" y1="543.2" x2="591.6" y2="554.9" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="546.5" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="595.5" y1="540.6" x2="595.5" y2="546.8" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="546.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="599.5" y1="545.9" x2="599.5" y2="554.8" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="549.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="603.4" y1="549.7" x2="603.4" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="553.9" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="607.4" y1="548.6" x2="607.4" y2="560.3" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="550.4" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="611.3" y1="546.3" x2="611.3" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="550.3" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="615.3" y1="546.3" x2="615.3" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="548.1" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="619.2" y1="548.5" x2="619.2" y2="555.2" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="551.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="623.2" y1="549.4" x2="623.2" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="552.3" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="627.1" y1="550.2" x2="627.1" y2="556.0" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="552.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="631.1" y1="544.8" x2="631.1" y2="553.0" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="547.5" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="635.0" y1="547.4" x2="635.0" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="551.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="639.0" y1="550.4" x2="639.0" y2="558.5" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="552.2" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="642.9" y1="551.6" x2="642.9" y2="560.8" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="553.6" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="646.9" y1="551.1" x2="646.9" y2="559.2" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="555.3" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="650.9" y1="556.2" x2="650.9" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="557.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="654.8" y1="552.1" x2="654.8" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="554.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="658.8" y1="556.2" x2="658.8" y2="563.4" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="558.5" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="662.7" y1="564.8" x2="662.7" y2="571.6" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="565.2" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="666.7" y1="565.8" x2="666.7" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="568.2" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="670.6" y1="563.5" x2="670.6" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="564.4" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="674.6" y1="562.7" x2="674.6" y2="572.1" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="563.7" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="678.5" y1="569.5" x2="678.5" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="571.6" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="682.5" y1="567.8" x2="682.5" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="571.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="686.4" y1="572.6" x2="686.4" y2="582.3" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="573.4" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="690.4" y1="571.0" x2="690.4" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="574.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="694.3" y1="574.9" x2="694.3" y2="580.8" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="577.2" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="698.3" y1="576.2" x2="698.3" y2="582.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="578.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="702.2" y1="576.9" x2="702.2" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="577.7" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="706.2" y1="559.9" x2="706.2" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="569.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="710.1" y1="551.9" x2="710.1" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="555.2" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="714.1" y1="547.7" x2="714.1" y2="562.4" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="547.8" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="718.0" y1="538.4" x2="718.0" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="545.3" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="722.0" y1="542.6" x2="722.0" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="543.8" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="725.9" y1="542.1" x2="725.9" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="542.1" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="729.9" y1="534.9" x2="729.9" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="535.5" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="733.8" y1="528.9" x2="733.8" y2="549.9" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="530.7" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="737.8" y1="536.4" x2="737.8" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="539.4" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="741.8" y1="544.3" x2="741.8" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="545.3" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="745.7" y1="550.1" x2="745.7" y2="557.2" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="552.5" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="749.7" y1="552.3" x2="749.7" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="552.3" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="753.6" y1="546.6" x2="753.6" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="547.3" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="757.6" y1="547.8" x2="757.6" y2="553.7" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="549.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="761.5" y1="547.0" x2="761.5" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="550.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="765.5" y1="548.0" x2="765.5" y2="556.5" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="549.9" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="769.4" y1="534.5" x2="769.4" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="536.1" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="773.4" y1="539.1" x2="773.4" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="541.4" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="777.3" y1="546.2" x2="777.3" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="546.3" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="781.3" y1="534.9" x2="781.3" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="538.5" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="785.2" y1="541.6" x2="785.2" y2="557.6" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="541.7" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="789.2" y1="547.5" x2="789.2" y2="554.9" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="551.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="793.1" y1="548.7" x2="793.1" y2="558.4" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="551.5" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="797.1" y1="556.0" x2="797.1" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="556.0" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="801.0" y1="560.4" x2="801.0" y2="571.3" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="560.6" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="805.0" y1="570.1" x2="805.0" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="570.4" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="808.9" y1="566.4" x2="808.9" y2="573.4" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="569.1" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="812.9" y1="558.5" x2="812.9" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="559.2" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="816.8" y1="554.1" x2="816.8" y2="561.2" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="558.4" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="820.8" y1="544.8" x2="820.8" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="549.8" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="824.7" y1="548.0" x2="824.7" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="550.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="828.7" y1="545.8" x2="828.7" y2="557.0" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="550.1" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="832.7" y1="540.5" x2="832.7" y2="555.9" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="545.0" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="836.6" y1="537.3" x2="836.6" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="542.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="840.6" y1="527.8" x2="840.6" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="531.5" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="844.5" y1="536.1" x2="844.5" y2="552.3" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="537.1" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="848.5" y1="548.9" x2="848.5" y2="553.9" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="550.4" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="852.4" y1="549.6" x2="852.4" y2="571.6" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="550.0" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="856.4" y1="562.9" x2="856.4" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="563.7" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="860.3" y1="562.5" x2="860.3" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="565.4" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="864.3" y1="571.2" x2="864.3" y2="580.9" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="574.1" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="868.2" y1="575.4" x2="868.2" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="577.8" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="872.2" y1="570.1" x2="872.2" y2="576.8" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="574.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="876.1" y1="560.0" x2="876.1" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="566.5" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="880.1" y1="564.5" x2="880.1" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="568.0" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="884.0" y1="563.8" x2="884.0" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="569.6" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="888.0" y1="554.2" x2="888.0" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="554.9" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="891.9" y1="553.7" x2="891.9" y2="562.2" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="560.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="895.9" y1="554.0" x2="895.9" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="564.1" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="899.8" y1="565.9" x2="899.8" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="566.3" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="903.8" y1="567.6" x2="903.8" y2="575.2" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="568.5" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="907.7" y1="570.2" x2="907.7" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="572.2" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="911.7" y1="567.7" x2="911.7" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="570.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="915.6" y1="569.6" x2="915.6" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="571.3" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="919.6" y1="567.4" x2="919.6" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="571.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="923.6" y1="564.0" x2="923.6" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="571.1" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="927.5" y1="572.0" x2="927.5" y2="578.0" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="576.2" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="931.5" y1="578.9" x2="931.5" y2="587.6" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="579.7" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="935.4" y1="583.0" x2="935.4" y2="588.5" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="586.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="939.4" y1="581.8" x2="939.4" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="583.5" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="943.3" y1="581.2" x2="943.3" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="582.0" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="947.3" y1="584.1" x2="947.3" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="585.2" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="951.2" y1="587.1" x2="951.2" y2="590.4" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="588.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="955.2" y1="584.7" x2="955.2" y2="593.6" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="588.1" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="959.1" y1="593.0" x2="959.1" y2="599.4" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="593.1" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="963.1" y1="595.4" x2="963.1" y2="602.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="597.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="967.0" y1="593.5" x2="967.0" y2="598.8" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="594.8" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="971.0" y1="586.5" x2="971.0" y2="593.3" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="586.8" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="974.9" y1="584.3" x2="974.9" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="587.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="978.9" y1="584.6" x2="978.9" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="585.8" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="982.8" y1="585.8" x2="982.8" y2="593.6" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="587.1" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="986.8" y1="587.6" x2="986.8" y2="593.7" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="588.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="990.7" y1="589.9" x2="990.7" y2="596.4" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="592.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="994.7" y1="590.8" x2="994.7" y2="599.2" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="594.3" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="998.6" y1="587.2" x2="998.6" y2="596.6" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="588.0" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="1002.6" y1="583.7" x2="1002.6" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="585.1" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="1006.5" y1="582.4" x2="1006.5" y2="591.3" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="583.7" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="1010.5" y1="576.3" x2="1010.5" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="578.6" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="1014.5" y1="578.4" x2="1014.5" y2="582.8" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="579.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1018.4" y1="574.6" x2="1018.4" y2="582.2" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="578.8" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="1022.4" y1="573.0" x2="1022.4" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="575.1" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="1026.3" y1="574.6" x2="1026.3" y2="581.9" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="575.4" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="1030.3" y1="573.8" x2="1030.3" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="574.4" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="1034.2" y1="573.9" x2="1034.2" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="575.0" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="1038.2" y1="571.8" x2="1038.2" y2="579.5" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="574.8" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="1042.1" y1="573.7" x2="1042.1" y2="581.7" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="575.6" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="1046.1" y1="577.3" x2="1046.1" y2="582.4" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="578.6" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="1050.0" y1="581.8" x2="1050.0" y2="588.2" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="584.9" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="60" y1="528.4" x2="1052" y2="528.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="531.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$14.25 R1</text>
<text x="1058" y="543.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="602.7" x2="1052" y2="602.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="596.7" font-size="11.5" fill="var(--support)" font-weight="600">$7.21 S1 (52주 최저)</text>
<text x="1058" y="608.7" font-size="9.5" fill="var(--muted)">터치 1회</text>
<circle cx="1052.0" cy="587.6" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $14.25 | 2 | 2025년 12월 말~2026년 1월 초 구간 — 11월 실적 충격 이후 낙폭과대 인식에 따른 단기 반등·박스권(FY2025 회계연도 말 종가 $14.17과 근접) |
| **현재가** | **$8.64** (2026-08-18 종가) | — | R1과 S1 (52주 최저) 사이 |
| S1 (52주 최저) | $7.21 | 1 | 강제 포함(사유 기입) |
| 참고선 | $57 | — | 52주 최고(2025년 10월경) — 11월 실적 충격 이후 거래 레짐이 완전히 바뀌어 근시일 저항으로 보기 어려움, 참고선으로만 표기 |

> 레벨이 R1 하나뿐인 것은 스크립트 결함이 아니라 이 종목의 실제 가격 구조를 반영한다 — 최근 1년의 절반은 급등(2025년 여름~10월), 나머지 절반은 급락(2025년 11월 이후)이 지배해 "터치 2회 이상"을 만족하는 클러스터가 거의 형성되지 않았다. S1(52주 최저)은 터치 1회뿐이지만 하방 참고점으로서 의미가 있어 `--force-level`로 강제 포함했다.

---

## 3. 관측된 특이 구간 — 2025-11-06 3분기 실적발표(Milestone Contribution 갭다운)

- ENTRA1·TVA 간 최대 6GW(NPM 72기) 비구속적 협력 합의로 파트너십 마일스톤 계약(PMA)상 지급 조건이 충족돼, $507.4M 규모의 일회성 "Milestone Contribution 1" 비용이 3분기 G&A로 인식됐다 — 자세한 내용은 [최근 뉴스 / 이슈](./08_news.md), [핵심 지표](./04_metrics.md) 상단 각주 참고.
- 종가 기준 전일 대비 약 **−14.4%** ($37.91 → $32.46, 2025-11-05→11-06), 이후 며칠에 걸쳐 추가 하락하며 낙폭이 누적됐다. 거래량도 평소 대비 수 배로 급증했다(정확한 배수는 확인 필요).
- 이 사건 이후 거래 레짐이 완전히 바뀌었다 — 사건 이전(2025년 8~10월)의 스윙 고점대(52주 최고 $57.42 부근)는 2. 지지선 / 저항선 요약에서 근시일 저항으로 보지 않고 참고선으로만 남겼다. 사건 이후 주가는 $14.25(R1) 근방에서 잠시 머물다 2026년 들어 추가로 하락해 2026-08-18 기준 $8.64까지 내려왔다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-19~2026-08-18. 수집 시점: 2026-08-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 2. 지지선 / 저항선 요약 비고).
- **생성**: `scripts/gen_technical_chart.py SMR --name "NuScale Power" --event 2025-11-06:"3분기 실적발표(Milestone Contribution 갭다운)" --ref-line 57.42:"52주 최고" --force-level '7.21:(52주 최저)' --close-on 2026-08-18` (재현용)
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - 2025-11-06 실적발표로 가격대가 구조적으로 재설정된 불연속 구간이 있다(3. 관측된 특이 구간 — 2025-11-06 3분기 실적발표(Milestone Contribution 갭다운)) — 이 구간을 전후로 스윙 레벨의 의미가 달라진다.
    - 이 기간 중 주식분할은 없었으나(핵심 지표 상단 각주), 대규모 신주 발행이 반복돼 시가총액 기준 밸류에이션과 이 문서의 "주가 자체" 기술적 분석은 별개로 봐야 한다 — 후자는 발행주식수 변화와 무관한 가격 패턴만 다룬다.

---

*작성일: 2026-08-23*
