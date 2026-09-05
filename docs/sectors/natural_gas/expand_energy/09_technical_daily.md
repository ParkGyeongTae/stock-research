# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-04 종가 $97.91은 [핵심 지표](./04_metrics.md) A.2 및 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.**
    - **주의**: 이 차트는 **원주가**(배당 미반영)다. 집계 사이트가 표시하는 배당 소급조정 주가와는 다르며, 기간 내 분기배당이 4회 있었다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="exe-chart">
<style>
.exe-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .exe-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .exe-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.exe-chart svg { width:100%; height:auto; display:block; }
.exe-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.exe-chart .title { fill: var(--ink); font-weight:600; }
.exe-chart .grid { stroke: var(--grid); stroke-width:1; }
.exe-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Expand Energy(EXE) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Expand Energy (EXE) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $97.91 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="542.7" x2="1052" y2="542.7" class="grid"/>
<text x="52" y="546.7" font-size="11" text-anchor="end" fill="var(--muted)">90</text>
<line x1="60" y1="414.7" x2="1052" y2="414.7" class="grid"/>
<text x="52" y="418.7" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="286.6" x2="1052" y2="286.6" class="grid"/>
<text x="52" y="290.6" font-size="11" text-anchor="end" fill="var(--muted)">110</text>
<line x1="60" y1="158.5" x2="1052" y2="158.5" class="grid"/>
<text x="52" y="162.5" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="132.8" y1="626.0" x2="132.8" y2="631.0" class="axis"/>
<text x="132.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="223.4" y1="626.0" x2="223.4" y2="631.0" class="axis"/>
<text x="223.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="298.2" y1="626.0" x2="298.2" y2="631.0" class="axis"/>
<text x="298.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="384.8" y1="626.0" x2="384.8" y2="631.0" class="axis"/>
<text x="384.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="463.5" y1="626.0" x2="463.5" y2="631.0" class="axis"/>
<text x="463.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="538.3" y1="626.0" x2="538.3" y2="631.0" class="axis"/>
<text x="538.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="624.9" y1="626.0" x2="624.9" y2="631.0" class="axis"/>
<text x="624.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="707.6" y1="626.0" x2="707.6" y2="631.0" class="axis"/>
<text x="707.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="786.3" y1="626.0" x2="786.3" y2="631.0" class="axis"/>
<text x="786.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="869.0" y1="626.0" x2="869.0" y2="631.0" class="axis"/>
<text x="869.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="955.6" y1="626.0" x2="955.6" y2="631.0" class="axis"/>
<text x="955.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1038.2" y1="626.0" x2="1038.2" y2="631.0" class="axis"/>
<text x="1038.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="73.7" x2="1052" y2="73.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="76.7" font-size="10.5" fill="var(--muted)">$127 52주 최고</text>
<line x1="483.2" y1="56.0" x2="483.2" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="489.2" y="68.0" font-size="10.5" fill="var(--down)">2026-02-09 CEO 교체·본사 이전 발표</text>
<line x1="62.0" y1="456.2" x2="62.0" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="467.7" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="65.9" y1="447.4" x2="65.9" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="456.3" width="2.44" height="28.6" fill="var(--down)"/>
<line x1="69.8" y1="464.6" x2="69.8" y2="485.1" stroke="var(--up)" class="wick"/>
<rect x="68.62" y="482.2" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="73.8" y1="453.1" x2="73.8" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="459.9" width="2.44" height="28.2" fill="var(--up)"/>
<line x1="77.7" y1="452.8" x2="77.7" y2="475.8" stroke="var(--down)" class="wick"/>
<rect x="76.49" y="466.1" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="81.7" y1="445.9" x2="81.7" y2="468.6" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="460.3" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="85.6" y1="446.9" x2="85.6" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="460.5" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="89.5" y1="441.0" x2="89.5" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="446.4" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="93.5" y1="410.6" x2="93.5" y2="446.4" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="418.8" width="2.44" height="25.4" fill="var(--up)"/>
<line x1="97.4" y1="401.8" x2="97.4" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="411.4" width="2.44" height="17.4" fill="var(--down)"/>
<line x1="101.3" y1="426.4" x2="101.3" y2="448.1" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="429.8" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="105.3" y1="432.7" x2="105.3" y2="464.4" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="436.9" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="109.2" y1="397.5" x2="109.2" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="405.4" width="2.44" height="29.1" fill="var(--up)"/>
<line x1="113.1" y1="355.6" x2="113.1" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="374.9" width="2.44" height="26.9" fill="var(--up)"/>
<line x1="117.1" y1="352.9" x2="117.1" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="358.5" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="121.0" y1="334.9" x2="121.0" y2="356.2" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="340.7" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="125.0" y1="312.2" x2="125.0" y2="348.6" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="327.4" width="2.44" height="17.5" fill="var(--up)"/>
<line x1="128.9" y1="307.6" x2="128.9" y2="335.5" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="330.1" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="132.8" y1="282.0" x2="132.8" y2="349.8" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="297.1" width="2.44" height="52.8" fill="var(--up)"/>
<line x1="136.8" y1="285.4" x2="136.8" y2="321.8" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="300.4" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="140.7" y1="305.8" x2="140.7" y2="329.2" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="312.1" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="144.6" y1="286.6" x2="144.6" y2="322.2" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="302.2" width="2.44" height="13.4" fill="var(--down)"/>
<line x1="148.6" y1="295.0" x2="148.6" y2="324.7" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="299.2" width="2.44" height="21.5" fill="var(--up)"/>
<line x1="152.5" y1="287.5" x2="152.5" y2="322.7" stroke="var(--down)" class="wick"/>
<rect x="151.29" y="290.1" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="156.4" y1="291.7" x2="156.4" y2="349.2" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="294.9" width="2.44" height="43.2" fill="var(--down)"/>
<line x1="160.4" y1="332.3" x2="160.4" y2="392.9" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="345.7" width="2.44" height="46.4" fill="var(--down)"/>
<line x1="164.3" y1="375.3" x2="164.3" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="380.3" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="168.3" y1="371.6" x2="168.3" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="397.2" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="172.2" y1="362.8" x2="172.2" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="374.0" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="176.1" y1="362.6" x2="176.1" y2="445.8" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="372.0" width="2.44" height="60.7" fill="var(--down)"/>
<line x1="180.1" y1="402.2" x2="180.1" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="404.7" width="2.44" height="24.0" fill="var(--up)"/>
<line x1="184.0" y1="318.1" x2="184.0" y2="383.4" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="326.3" width="2.44" height="50.0" fill="var(--up)"/>
<line x1="187.9" y1="305.5" x2="187.9" y2="343.9" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="328.2" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="191.9" y1="319.1" x2="191.9" y2="377.4" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="319.1" width="2.44" height="39.3" fill="var(--down)"/>
<line x1="195.8" y1="319.1" x2="195.8" y2="377.7" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="334.6" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="199.7" y1="336.3" x2="199.7" y2="378.3" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="339.3" width="2.44" height="27.0" fill="var(--down)"/>
<line x1="203.7" y1="352.0" x2="203.7" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="354.2" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="207.6" y1="364.7" x2="207.6" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="365.0" width="2.44" height="36.9" fill="var(--down)"/>
<line x1="211.6" y1="366.7" x2="211.6" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="371.6" width="2.44" height="37.8" fill="var(--down)"/>
<line x1="215.5" y1="389.3" x2="215.5" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="408.0" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="219.4" y1="363.1" x2="219.4" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="372.3" width="2.44" height="17.9" fill="var(--up)"/>
<line x1="223.4" y1="282.1" x2="223.4" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="285.5" width="2.44" height="81.3" fill="var(--up)"/>
<line x1="227.3" y1="263.9" x2="227.3" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="285.9" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="231.2" y1="255.3" x2="231.2" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="285.9" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="235.2" y1="252.9" x2="235.2" y2="298.1" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="275.3" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="239.1" y1="249.2" x2="239.1" y2="299.4" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="255.2" width="2.44" height="33.8" fill="var(--up)"/>
<line x1="243.0" y1="219.4" x2="243.0" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="224.7" width="2.44" height="20.1" fill="var(--up)"/>
<line x1="247.0" y1="172.6" x2="247.0" y2="225.1" stroke="var(--up)" class="wick"/>
<rect x="245.76" y="175.9" width="2.44" height="43.2" fill="var(--up)"/>
<line x1="250.9" y1="154.6" x2="250.9" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="165.4" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="254.9" y1="158.5" x2="254.9" y2="189.2" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="168.7" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="258.8" y1="187.1" x2="258.8" y2="251.1" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="193.3" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="262.7" y1="184.7" x2="262.7" y2="220.2" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="195.1" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="266.7" y1="187.8" x2="266.7" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="194.8" width="2.44" height="19.3" fill="var(--up)"/>
<line x1="270.6" y1="188.1" x2="270.6" y2="217.0" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="193.4" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="274.5" y1="143.2" x2="274.5" y2="230.7" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="188.2" width="2.44" height="40.7" fill="var(--down)"/>
<line x1="278.5" y1="208.6" x2="278.5" y2="255.3" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="222.6" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="282.4" y1="191.2" x2="282.4" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="202.7" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="286.3" y1="202.8" x2="286.3" y2="228.9" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="209.6" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="290.3" y1="162.3" x2="290.3" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="174.2" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="294.2" y1="123.9" x2="294.2" y2="167.1" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="133.8" width="2.44" height="29.1" fill="var(--up)"/>
<line x1="298.2" y1="123.9" x2="298.2" y2="156.0" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="126.5" width="2.44" height="11.7" fill="var(--down)"/>
<line x1="302.1" y1="138.9" x2="302.1" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="142.5" width="2.44" height="45.2" fill="var(--down)"/>
<line x1="306.0" y1="117.7" x2="306.0" y2="186.1" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="121.5" width="2.44" height="58.0" fill="var(--up)"/>
<line x1="310.0" y1="95.8" x2="310.0" y2="137.8" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="120.2" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="313.9" y1="73.7" x2="313.9" y2="122.6" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="110.2" width="2.44" height="11.7" fill="var(--down)"/>
<line x1="317.8" y1="127.7" x2="317.8" y2="181.9" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="132.3" width="2.44" height="38.0" fill="var(--down)"/>
<line x1="321.8" y1="163.9" x2="321.8" y2="194.3" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="170.4" width="2.44" height="20.6" fill="var(--down)"/>
<line x1="325.7" y1="184.5" x2="325.7" y2="219.7" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="184.5" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="329.7" y1="204.8" x2="329.7" y2="244.0" stroke="var(--down)" class="wick"/>
<rect x="328.43" y="216.0" width="2.44" height="15.1" fill="var(--down)"/>
<line x1="333.6" y1="222.9" x2="333.6" y2="268.6" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="231.4" width="2.44" height="19.5" fill="var(--down)"/>
<line x1="337.5" y1="251.1" x2="337.5" y2="301.4" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="251.1" width="2.44" height="28.6" fill="var(--down)"/>
<line x1="341.5" y1="296.2" x2="341.5" y2="337.9" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="296.2" width="2.44" height="34.2" fill="var(--down)"/>
<line x1="345.4" y1="288.7" x2="345.4" y2="323.8" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="292.5" width="2.44" height="25.2" fill="var(--up)"/>
<line x1="349.3" y1="279.6" x2="349.3" y2="316.9" stroke="var(--down)" class="wick"/>
<rect x="348.11" y="291.8" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="353.3" y1="290.3" x2="353.3" y2="321.8" stroke="var(--up)" class="wick"/>
<rect x="352.05" y="302.7" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="357.2" y1="292.2" x2="357.2" y2="318.8" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="298.5" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="361.1" y1="267.2" x2="361.1" y2="306.1" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="271.6" width="2.44" height="31.5" fill="var(--up)"/>
<line x1="365.1" y1="278.5" x2="365.1" y2="297.8" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="291.0" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="369.0" y1="287.8" x2="369.0" y2="304.0" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="290.9" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="373.0" y1="259.7" x2="373.0" y2="290.7" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="263.8" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="376.9" y1="242.8" x2="376.9" y2="260.9" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="250.1" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="380.8" y1="262.8" x2="380.8" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="267.0" width="2.44" height="15.0" fill="var(--down)"/>
<line x1="384.8" y1="282.4" x2="384.8" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="286.8" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="388.7" y1="308.5" x2="388.7" y2="377.8" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="308.7" width="2.44" height="18.6" fill="var(--down)"/>
<line x1="392.6" y1="331.3" x2="392.6" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="341.8" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="396.6" y1="308.5" x2="396.6" y2="348.7" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="329.3" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="400.5" y1="320.8" x2="400.5" y2="379.6" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="335.9" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="404.4" y1="349.7" x2="404.4" y2="401.3" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="366.2" width="2.44" height="27.5" fill="var(--down)"/>
<line x1="408.4" y1="364.2" x2="408.4" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="378.3" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="412.3" y1="348.6" x2="412.3" y2="385.3" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="365.2" width="2.44" height="11.3" fill="var(--down)"/>
<line x1="416.3" y1="383.4" x2="416.3" y2="408.6" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="388.8" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="420.2" y1="389.8" x2="420.2" y2="424.0" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="398.9" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="424.1" y1="408.1" x2="424.1" y2="432.6" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="416.2" width="2.44" height="14.5" fill="var(--up)"/>
<line x1="428.1" y1="326.3" x2="428.1" y2="374.4" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="339.8" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="432.0" y1="264.9" x2="432.0" y2="321.9" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="293.0" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="435.9" y1="274.8" x2="435.9" y2="313.3" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="286.6" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="439.9" y1="264.5" x2="439.9" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="269.3" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="443.8" y1="232.4" x2="443.8" y2="299.4" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="256.3" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="447.7" y1="252.0" x2="447.7" y2="322.3" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="256.8" width="2.44" height="44.8" fill="var(--down)"/>
<line x1="451.7" y1="282.8" x2="451.7" y2="314.7" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="290.9" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="455.6" y1="263.7" x2="455.6" y2="298.7" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="269.8" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="459.6" y1="232.9" x2="459.6" y2="280.0" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="255.7" width="2.44" height="21.1" fill="var(--up)"/>
<line x1="463.5" y1="295.4" x2="463.5" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="304.0" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="467.4" y1="304.8" x2="467.4" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="305.8" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="471.4" y1="278.5" x2="471.4" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="285.2" width="2.44" height="11.8" fill="var(--down)"/>
<line x1="475.3" y1="280.0" x2="475.3" y2="316.5" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="294.6" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="479.2" y1="257.4" x2="479.2" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="281.8" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="483.2" y1="331.4" x2="483.2" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="356.9" width="2.44" height="16.3" fill="var(--down)"/>
<line x1="487.1" y1="357.0" x2="487.1" y2="394.4" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="364.2" width="2.44" height="22.2" fill="var(--down)"/>
<line x1="491.0" y1="350.9" x2="491.0" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="370.7" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="495.0" y1="360.9" x2="495.0" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="366.7" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="498.9" y1="347.6" x2="498.9" y2="389.0" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="362.8" width="2.44" height="16.9" fill="var(--up)"/>
<line x1="502.9" y1="359.9" x2="502.9" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="369.6" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="506.8" y1="351.5" x2="506.8" y2="435.8" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="361.2" width="2.44" height="59.6" fill="var(--down)"/>
<line x1="510.7" y1="364.7" x2="510.7" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="365.3" width="2.44" height="30.5" fill="var(--up)"/>
<line x1="514.7" y1="296.9" x2="514.7" y2="368.8" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="311.4" width="2.44" height="47.2" fill="var(--up)"/>
<line x1="518.6" y1="290.4" x2="518.6" y2="386.9" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="312.2" width="2.44" height="61.7" fill="var(--down)"/>
<line x1="522.5" y1="372.6" x2="522.5" y2="403.8" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="373.9" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="526.5" y1="332.6" x2="526.5" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="337.2" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="530.4" y1="321.1" x2="530.4" y2="354.4" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="334.1" width="2.44" height="18.7" fill="var(--up)"/>
<line x1="534.3" y1="289.5" x2="534.3" y2="328.2" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="313.2" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="538.3" y1="269.0" x2="538.3" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="276.4" width="2.44" height="29.5" fill="var(--down)"/>
<line x1="542.2" y1="276.2" x2="542.2" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="276.2" width="2.44" height="36.1" fill="var(--down)"/>
<line x1="546.2" y1="319.5" x2="546.2" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="544.94" y="328.3" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="550.1" y1="318.6" x2="550.1" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="329.2" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="554.0" y1="302.8" x2="554.0" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="312.8" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="558.0" y1="297.3" x2="558.0" y2="328.7" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="313.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="561.9" y1="316.3" x2="561.9" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="323.7" width="2.44" height="31.1" fill="var(--down)"/>
<line x1="565.8" y1="294.2" x2="565.8" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="304.8" width="2.44" height="43.6" fill="var(--up)"/>
<line x1="569.8" y1="298.1" x2="569.8" y2="327.7" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="300.4" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="573.7" y1="289.0" x2="573.7" y2="328.8" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="315.6" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="577.7" y1="287.8" x2="577.7" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="315.9" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="581.6" y1="293.0" x2="581.6" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="302.4" width="2.44" height="30.2" fill="var(--down)"/>
<line x1="585.5" y1="329.7" x2="585.5" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="333.6" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="589.5" y1="263.8" x2="589.5" y2="331.6" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="312.8" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="593.4" y1="300.1" x2="593.4" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="309.7" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="597.3" y1="302.1" x2="597.3" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="316.8" width="2.44" height="41.0" fill="var(--up)"/>
<line x1="601.3" y1="254.7" x2="601.3" y2="310.5" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="290.5" width="2.44" height="19.9" fill="var(--up)"/>
<line x1="605.2" y1="234.0" x2="605.2" y2="289.1" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="236.4" width="2.44" height="43.9" fill="var(--up)"/>
<line x1="609.1" y1="225.0" x2="609.1" y2="276.8" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="242.0" width="2.44" height="31.1" fill="var(--down)"/>
<line x1="613.1" y1="229.4" x2="613.1" y2="268.8" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="241.7" width="2.44" height="27.0" fill="var(--up)"/>
<line x1="617.0" y1="229.0" x2="617.0" y2="280.5" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="233.0" width="2.44" height="35.0" fill="var(--down)"/>
<line x1="621.0" y1="242.0" x2="621.0" y2="305.3" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="255.7" width="2.44" height="33.7" fill="var(--down)"/>
<line x1="624.9" y1="291.8" x2="624.9" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="307.8" width="2.44" height="29.7" fill="var(--down)"/>
<line x1="628.8" y1="323.2" x2="628.8" y2="369.2" stroke="var(--down)" class="wick"/>
<rect x="627.61" y="327.2" width="2.44" height="37.7" fill="var(--down)"/>
<line x1="632.8" y1="357.0" x2="632.8" y2="379.8" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="369.2" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="636.7" y1="354.3" x2="636.7" y2="394.2" stroke="var(--down)" class="wick"/>
<rect x="635.48" y="368.2" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="640.6" y1="409.7" x2="640.6" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="412.2" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="644.6" y1="404.0" x2="644.6" y2="437.8" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="421.1" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="648.5" y1="417.8" x2="648.5" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="427.6" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="652.4" y1="413.6" x2="652.4" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="420.5" width="2.44" height="22.5" fill="var(--down)"/>
<line x1="656.4" y1="446.0" x2="656.4" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="450.9" width="2.44" height="19.0" fill="var(--down)"/>
<line x1="660.3" y1="456.5" x2="660.3" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="465.2" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="664.3" y1="442.3" x2="664.3" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="448.5" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="668.2" y1="457.0" x2="668.2" y2="479.1" stroke="var(--up)" class="wick"/>
<rect x="666.97" y="468.2" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="672.1" y1="448.6" x2="672.1" y2="479.2" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="460.1" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="676.1" y1="463.2" x2="676.1" y2="494.7" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="469.7" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="680.0" y1="459.2" x2="680.0" y2="480.1" stroke="var(--up)" class="wick"/>
<rect x="678.78" y="461.3" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="683.9" y1="440.4" x2="683.9" y2="472.3" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="453.6" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="687.9" y1="458.2" x2="687.9" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="460.3" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="691.8" y1="430.4" x2="691.8" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="454.4" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="695.7" y1="438.1" x2="695.7" y2="460.6" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="448.5" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="699.7" y1="398.1" x2="699.7" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="402.0" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="703.6" y1="376.7" x2="703.6" y2="426.9" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="387.1" width="2.44" height="36.1" fill="var(--up)"/>
<line x1="707.6" y1="392.3" x2="707.6" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="393.9" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="711.5" y1="391.2" x2="711.5" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="404.8" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="715.4" y1="407.9" x2="715.4" y2="430.5" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="417.7" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="719.4" y1="430.5" x2="719.4" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="449.9" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="723.3" y1="443.5" x2="723.3" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="447.7" width="2.44" height="21.1" fill="var(--up)"/>
<line x1="727.2" y1="438.0" x2="727.2" y2="467.2" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="444.4" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="731.2" y1="448.2" x2="731.2" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="451.5" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="735.1" y1="447.8" x2="735.1" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="449.4" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="739.0" y1="460.4" x2="739.0" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="460.4" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="743.0" y1="449.5" x2="743.0" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="456.9" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="746.9" y1="442.6" x2="746.9" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="448.6" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="750.9" y1="429.8" x2="750.9" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="434.5" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="754.8" y1="402.5" x2="754.8" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="403.3" width="2.44" height="22.7" fill="var(--up)"/>
<line x1="758.7" y1="403.3" x2="758.7" y2="438.7" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="406.6" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="762.7" y1="418.4" x2="762.7" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="418.4" width="2.44" height="27.1" fill="var(--down)"/>
<line x1="766.6" y1="439.5" x2="766.6" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="441.0" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="770.5" y1="450.6" x2="770.5" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="769.32" y="456.9" width="2.44" height="27.5" fill="var(--down)"/>
<line x1="774.5" y1="483.8" x2="774.5" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="492.3" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="778.4" y1="493.7" x2="778.4" y2="516.5" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="496.8" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="782.3" y1="490.2" x2="782.3" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="493.7" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="786.3" y1="499.1" x2="786.3" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="504.4" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="790.2" y1="510.0" x2="790.2" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="521.1" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="794.2" y1="511.4" x2="794.2" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="517.1" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="798.1" y1="494.8" x2="798.1" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="499.2" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="802.0" y1="487.3" x2="802.0" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="495.7" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="806.0" y1="513.7" x2="806.0" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="516.2" width="2.44" height="21.1" fill="var(--down)"/>
<line x1="809.9" y1="538.5" x2="809.9" y2="563.8" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="539.9" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="813.8" y1="539.2" x2="813.8" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="550.0" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="817.8" y1="554.3" x2="817.8" y2="583.7" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="561.7" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="821.7" y1="550.2" x2="821.7" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="558.4" width="2.44" height="21.8" fill="var(--up)"/>
<line x1="825.7" y1="546.5" x2="825.7" y2="579.4" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="569.6" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="829.6" y1="553.0" x2="829.6" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="563.7" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="833.5" y1="560.2" x2="833.5" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="574.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="837.5" y1="562.6" x2="837.5" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="578.4" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="841.4" y1="559.3" x2="841.4" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="562.7" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="845.3" y1="551.7" x2="845.3" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="558.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="849.3" y1="555.9" x2="849.3" y2="574.1" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="560.7" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="853.2" y1="549.1" x2="853.2" y2="566.5" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="552.0" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="857.1" y1="530.2" x2="857.1" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="558.4" width="2.44" height="4.0" fill="var(--down)"/>
<line x1="861.1" y1="556.3" x2="861.1" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="567.2" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="865.0" y1="504.2" x2="865.0" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="527.5" width="2.44" height="37.7" fill="var(--up)"/>
<line x1="869.0" y1="518.3" x2="869.0" y2="549.1" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="525.4" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="872.9" y1="528.8" x2="872.9" y2="545.3" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="533.5" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="876.8" y1="536.6" x2="876.8" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="544.9" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="880.8" y1="542.0" x2="880.8" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="548.4" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="884.7" y1="535.1" x2="884.7" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="538.9" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="888.6" y1="542.2" x2="888.6" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="548.0" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="892.6" y1="555.2" x2="892.6" y2="607.0" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="560.0" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="896.5" y1="562.5" x2="896.5" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="572.3" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="900.4" y1="567.6" x2="900.4" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="570.8" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="904.4" y1="542.7" x2="904.4" y2="580.4" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="565.7" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="908.3" y1="557.6" x2="908.3" y2="574.4" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="566.1" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="912.3" y1="542.9" x2="912.3" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="558.9" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="916.2" y1="565.2" x2="916.2" y2="588.7" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="565.2" width="2.44" height="16.6" fill="var(--down)"/>
<line x1="920.1" y1="558.8" x2="920.1" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="560.9" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="924.1" y1="499.1" x2="924.1" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="502.1" width="2.44" height="32.5" fill="var(--up)"/>
<line x1="928.0" y1="487.7" x2="928.0" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="497.1" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="931.9" y1="499.7" x2="931.9" y2="524.2" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="513.0" width="2.44" height="10.2" fill="var(--down)"/>
<line x1="935.9" y1="513.5" x2="935.9" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="518.7" width="2.44" height="17.5" fill="var(--down)"/>
<line x1="939.8" y1="521.4" x2="939.8" y2="567.1" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="524.8" width="2.44" height="36.9" fill="var(--down)"/>
<line x1="943.7" y1="503.3" x2="943.7" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="511.2" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="947.7" y1="497.1" x2="947.7" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="511.7" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="951.6" y1="489.3" x2="951.6" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="491.1" width="2.44" height="19.6" fill="var(--up)"/>
<line x1="955.6" y1="472.2" x2="955.6" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="483.1" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="959.5" y1="491.6" x2="959.5" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="503.4" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="963.4" y1="492.3" x2="963.4" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="498.6" width="2.44" height="33.7" fill="var(--down)"/>
<line x1="967.4" y1="505.7" x2="967.4" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="511.5" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="971.3" y1="493.8" x2="971.3" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="506.4" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="975.2" y1="445.5" x2="975.2" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="445.9" width="2.44" height="45.2" fill="var(--up)"/>
<line x1="979.2" y1="429.0" x2="979.2" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="437.2" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="983.1" y1="438.5" x2="983.1" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="443.1" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="987.0" y1="472.8" x2="987.0" y2="488.8" stroke="var(--down)" class="wick"/>
<rect x="985.83" y="482.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="991.0" y1="469.9" x2="991.0" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="473.4" width="2.44" height="8.1" fill="var(--down)"/>
<line x1="994.9" y1="483.4" x2="994.9" y2="509.1" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="485.9" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="998.9" y1="468.8" x2="998.9" y2="486.8" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="472.9" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="1002.8" y1="452.4" x2="1002.8" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="464.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1006.7" y1="449.5" x2="1006.7" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="456.8" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="1010.7" y1="448.2" x2="1010.7" y2="478.5" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="464.7" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="1014.6" y1="454.4" x2="1014.6" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="461.7" width="2.44" height="2.8" fill="var(--up)"/>
<line x1="1018.5" y1="466.1" x2="1018.5" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="482.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1022.5" y1="436.1" x2="1022.5" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="458.6" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="1026.4" y1="436.2" x2="1026.4" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="440.3" width="2.44" height="20.8" fill="var(--up)"/>
<line x1="1030.3" y1="422.0" x2="1030.3" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="436.4" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="1034.3" y1="419.6" x2="1034.3" y2="443.1" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="430.4" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="1038.2" y1="413.0" x2="1038.2" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="414.9" width="2.44" height="20.9" fill="var(--up)"/>
<line x1="1042.2" y1="413.2" x2="1042.2" y2="426.8" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="417.3" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="1046.1" y1="412.9" x2="1046.1" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="419.1" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="1050.0" y1="421.1" x2="1050.0" y2="449.4" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="421.1" width="2.44" height="20.4" fill="var(--down)"/>
<line x1="60" y1="415.7" x2="1052" y2="415.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="419.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$100 R1</text>
<text x="1058" y="431.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="285.5" x2="1052" y2="285.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="289.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$110 R2</text>
<text x="1058" y="301.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="233.4" x2="1052" y2="233.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="236.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$114 R3</text>
<text x="1058" y="248.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="496.4" x2="1052" y2="496.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="490.4" font-size="11.5" fill="var(--support)" font-weight="600">$94 S1</text>
<text x="1058" y="502.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="598.1" x2="1052" y2="598.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="592.1" font-size="11.5" fill="var(--support)" font-weight="600">$86 S2</text>
<text x="1058" y="604.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="441.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="433.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $98 (2026-09-04)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $114 | 3 | 2025-12-30·2026-01-26·2026-03-26 — 겨울 가격 강세기에 만들어진 고점대. 2026년 3월 이후로는 한 번도 회복하지 못했다 |
| R2 | $110 | 3 | 2025-10-01·2025-10-21·2026-03-02 — FY2025 말 종가($110.36)와 겹치는 구간 |
| R1 | $100 | 2 | 2026-05-19·2026-08-11 — **현재가 바로 위.** 터치 2회로 표본이 얇다 |
| **현재가** | **$97.91** (2026-09-04 종가) | — | R1과 S1 사이 |
| S1 | $94 | 3 | 2026-04-21·2026-05-14·2026-08-17 — 현재가에 가장 근접한 지지대 |
| S2 | $86 | 2 | 2026-06-18·2026-07-10 — 52주 최저($84.99, 2026-07-10)를 포함하는 구간 |
| 참고선 | $127 | — | 52주 최고($126.62, 2025-12-05). 현재가보다 29% 위이고 그 뒤 9개월간 한 번도 접근하지 못해 **근시일 저항으로 보지 않는다** |

**현재가는 R1($100)과 S1($94) 사이의 좁은 구간에 있다.** 위아래 레벨까지 각각 +2.1% / −4.0%로 폭이 좁아, 이 차트만으로는 방향을 읽을 근거가 되지 않는다.

---

## 3. 관측된 특이 구간 — 2026-02-09 CEO 교체·본사 이전 발표

- 2026-02-06(금) 장 마감 후 이사회가 Dell'Osso CEO 교체와 본사 휴스턴 이전을 결정했고, 발표 후 첫 거래일이 2026-02-09(월)이었다([최근 뉴스 / 이슈](./08_news.md) 참고).
- 종가 기준 전일 대비 **−6.46%** ($110.37 → $103.24), 거래량은 평소(일 350만 주 내외) 대비 약 **1.9배**인 **671만 주**. 다음 날에도 −1.00%가 이어졌다.
- **이 갭 이후 주가는 $110대를 회복하지 못했다.** R2($110)를 마지막으로 터치한 것이 2026-03-02이고 이후 6개월간 그 위로 올라간 적이 없다. 다만 같은 기간 헨리허브 전망도 하향됐으므로, **이 갭 하나를 레짐 전환의 원인으로 단정할 수는 없다** — 지배구조 이벤트와 가격 사이클 하강이 겹친 구간으로 읽는 것이 맞다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-05~2026-09-04. 수집 시점: 2026-09-05. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py EXE --name "Expand Energy" --event 2026-02-09:"CEO 교체·본사 이전 발표" --ref-line 126.62:"52주 최고" --close-on 2026-09-04 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3. 관측된 특이 구간의 갭이 레벨 해석을 왜곡한다.** 2026-02-09의 −6.46% 갭 위쪽(R2 $110·R3 $114)은 갭 이전에 형성된 레벨이 대부분이라, 갭 아래에서 거래되는 지금 그대로의 저항으로 보기 어렵다.
    - **R1($100)·S2($86)는 터치 2회뿐이라 표본이 얇다.** 5개 레벨 중 터치 3회 이상인 것은 R3·R2·S1 셋이다.
    - **기간 내 주식분할·유상증자는 없었다.** 2024-10-01 Southwestern 합병은 주식교환이라 기존 주주의 주당 가격 연속성이 유지되며, 이 차트 구간(2025-09-05~) 전체가 합병 이후다.
    - **배당은 반영하지 않았다.** 기간 중 분기배당 4회($0.575씩)가 있었으므로 총수익률 기준 성과는 이 차트보다 약 2.3%p 높다.

---

*작성일: 2026-09-05*
