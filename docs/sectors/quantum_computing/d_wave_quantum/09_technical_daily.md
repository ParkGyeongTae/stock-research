# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-02 종가 $16.49는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다. 2022-08 상장 이후 주식분할이 없어 원주가와 수정주가가 같다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-03 ~ 2026-09-02)

<div class="qbts-chart">
<style>
.qbts-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .qbts-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .qbts-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.qbts-chart svg { width:100%; height:auto; display:block; }
.qbts-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.qbts-chart .title { fill: var(--ink); font-weight:600; }
.qbts-chart .grid { stroke: var(--grid); stroke-width:1; }
.qbts-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="D-Wave Quantum(QBTS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">D-Wave Quantum (QBTS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-03 ~ 2026-09-02 · 마지막 종가 $16.49 (2026-09-02) · 단위 USD</text>
<line x1="60" y1="571.3" x2="1052" y2="571.3" class="grid"/>
<text x="52" y="575.3" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="493.3" x2="1052" y2="493.3" class="grid"/>
<text x="52" y="497.3" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="415.2" x2="1052" y2="415.2" class="grid"/>
<text x="52" y="419.2" font-size="11" text-anchor="end" fill="var(--muted)">25</text>
<line x1="60" y1="337.1" x2="1052" y2="337.1" class="grid"/>
<text x="52" y="341.1" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="259.0" x2="1052" y2="259.0" class="grid"/>
<text x="52" y="263.0" font-size="11" text-anchor="end" fill="var(--muted)">35</text>
<line x1="60" y1="180.9" x2="1052" y2="180.9" class="grid"/>
<text x="52" y="184.9" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="102.8" x2="1052" y2="102.8" class="grid"/>
<text x="52" y="106.8" font-size="11" text-anchor="end" fill="var(--muted)">45</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="140.7" y1="626.0" x2="140.7" y2="631.0" class="axis"/>
<text x="140.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="231.2" y1="626.0" x2="231.2" y2="631.0" class="axis"/>
<text x="231.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="306.0" y1="626.0" x2="306.0" y2="631.0" class="axis"/>
<text x="306.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="392.6" y1="626.0" x2="392.6" y2="631.0" class="axis"/>
<text x="392.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="471.4" y1="626.0" x2="471.4" y2="631.0" class="axis"/>
<text x="471.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="546.2" y1="626.0" x2="546.2" y2="631.0" class="axis"/>
<text x="546.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="632.8" y1="626.0" x2="632.8" y2="631.0" class="axis"/>
<text x="632.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="715.4" y1="626.0" x2="715.4" y2="631.0" class="axis"/>
<text x="715.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="794.2" y1="626.0" x2="794.2" y2="631.0" class="axis"/>
<text x="794.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="876.8" y1="626.0" x2="876.8" y2="631.0" class="axis"/>
<text x="876.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="963.4" y1="626.0" x2="963.4" y2="631.0" class="axis"/>
<text x="963.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1046.1" y1="626.0" x2="1046.1" y2="631.0" class="axis"/>
<text x="1046.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="553.9" x2="62.0" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="558.8" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="65.9" y1="558.7" x2="65.9" y2="573.2" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="564.0" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="69.8" y1="556.4" x2="69.8" y2="572.9" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="564.2" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="73.8" y1="559.6" x2="73.8" y2="567.8" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="563.5" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="77.7" y1="552.0" x2="77.7" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="553.4" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="81.7" y1="549.2" x2="81.7" y2="557.8" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="552.6" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="85.6" y1="544.5" x2="85.6" y2="556.4" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="547.6" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="89.5" y1="524.8" x2="89.5" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="528.2" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="93.5" y1="515.4" x2="93.5" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="519.5" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="97.4" y1="506.1" x2="97.4" y2="526.1" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="509.2" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="101.3" y1="448.8" x2="101.3" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="453.6" width="2.44" height="55.6" fill="var(--up)"/>
<line x1="105.3" y1="417.5" x2="105.3" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="430.5" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="109.2" y1="378.8" x2="109.2" y2="441.4" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="385.8" width="2.44" height="55.6" fill="var(--up)"/>
<line x1="113.1" y1="395.5" x2="113.1" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="404.7" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="117.1" y1="368.5" x2="117.1" y2="405.8" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="375.8" width="2.44" height="25.6" fill="var(--up)"/>
<line x1="121.0" y1="349.9" x2="121.0" y2="393.9" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="361.5" width="2.44" height="11.2" fill="var(--down)"/>
<line x1="125.0" y1="378.9" x2="125.0" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="394.3" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="128.9" y1="360.5" x2="128.9" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="387.7" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="132.8" y1="359.4" x2="132.8" y2="415.6" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="383.6" width="2.44" height="26.7" fill="var(--down)"/>
<line x1="136.8" y1="407.8" x2="136.8" y2="435.9" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="416.1" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="140.7" y1="402.4" x2="140.7" y2="432.2" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="405.3" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="144.6" y1="343.2" x2="144.6" y2="399.1" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="349.4" width="2.44" height="47.0" fill="var(--up)"/>
<line x1="148.6" y1="285.9" x2="148.6" y2="337.9" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="294.9" width="2.44" height="32.8" fill="var(--up)"/>
<line x1="152.5" y1="236.9" x2="152.5" y2="308.2" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="258.7" width="2.44" height="47.0" fill="var(--up)"/>
<line x1="156.4" y1="213.7" x2="156.4" y2="277.0" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="228.4" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="160.4" y1="188.0" x2="160.4" y2="297.9" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="241.5" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="164.3" y1="233.4" x2="164.3" y2="280.9" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="257.9" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="168.3" y1="245.9" x2="168.3" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="248.4" width="2.44" height="41.5" fill="var(--down)"/>
<line x1="172.2" y1="150.2" x2="172.2" y2="296.2" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="171.2" width="2.44" height="99.0" fill="var(--up)"/>
<line x1="176.1" y1="98.2" x2="176.1" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="174.91" y="133.1" width="2.44" height="39.7" fill="var(--up)"/>
<line x1="180.1" y1="75.5" x2="180.1" y2="161.9" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="81.0" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="184.0" y1="100.8" x2="184.0" y2="186.7" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="107.5" width="2.44" height="66.2" fill="var(--down)"/>
<line x1="187.9" y1="189.2" x2="187.9" y2="242.5" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="204.4" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="191.9" y1="185.9" x2="191.9" y2="282.1" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="188.4" width="2.44" height="80.0" fill="var(--down)"/>
<line x1="195.8" y1="274.9" x2="195.8" y2="319.6" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="280.6" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="199.7" y1="316.6" x2="199.7" y2="393.8" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="335.4" width="2.44" height="44.0" fill="var(--down)"/>
<line x1="203.7" y1="283.5" x2="203.7" y2="342.4" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="296.5" width="2.44" height="24.0" fill="var(--down)"/>
<line x1="207.6" y1="256.0" x2="207.6" y2="301.2" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="287.2" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="211.6" y1="223.4" x2="211.6" y2="286.7" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="258.4" width="2.44" height="16.4" fill="var(--up)"/>
<line x1="215.5" y1="234.5" x2="215.5" y2="308.2" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="254.4" width="2.44" height="51.5" fill="var(--down)"/>
<line x1="219.4" y1="264.5" x2="219.4" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="270.6" width="2.44" height="27.9" fill="var(--up)"/>
<line x1="223.4" y1="231.1" x2="223.4" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="241.7" width="2.44" height="50.0" fill="var(--up)"/>
<line x1="227.3" y1="221.0" x2="227.3" y2="258.2" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="226.8" width="2.44" height="16.7" fill="var(--up)"/>
<line x1="231.2" y1="218.1" x2="231.2" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="221.2" width="2.44" height="67.6" fill="var(--down)"/>
<line x1="235.2" y1="297.6" x2="235.2" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="321.2" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="239.1" y1="311.6" x2="239.1" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="321.2" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="243.0" y1="326.3" x2="243.0" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="329.4" width="2.44" height="32.9" fill="var(--down)"/>
<line x1="247.0" y1="341.5" x2="247.0" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="245.76" y="344.9" width="2.44" height="32.3" fill="var(--up)"/>
<line x1="250.9" y1="312.1" x2="250.9" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="335.4" width="2.44" height="11.6" fill="var(--down)"/>
<line x1="254.9" y1="336.8" x2="254.9" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="352.9" width="2.44" height="3.0" fill="var(--up)"/>
<line x1="258.8" y1="343.8" x2="258.8" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="355.5" width="2.44" height="37.8" fill="var(--down)"/>
<line x1="262.7" y1="407.4" x2="262.7" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="407.7" width="2.44" height="32.6" fill="var(--down)"/>
<line x1="266.7" y1="415.3" x2="266.7" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="436.9" width="2.44" height="31.7" fill="var(--up)"/>
<line x1="270.6" y1="431.9" x2="270.6" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="269.38" y="442.8" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="274.5" y1="439.4" x2="274.5" y2="464.5" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="447.5" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="278.5" y1="423.9" x2="278.5" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="439.5" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="282.4" y1="420.0" x2="282.4" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="431.3" width="2.44" height="54.0" fill="var(--down)"/>
<line x1="286.3" y1="481.5" x2="286.3" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="486.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="290.3" y1="441.1" x2="290.3" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="444.7" width="2.44" height="40.4" fill="var(--up)"/>
<line x1="294.2" y1="447.8" x2="294.2" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="452.8" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="298.2" y1="446.7" x2="298.2" y2="462.0" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="451.3" width="2.44" height="4.4" fill="var(--down)"/>
<line x1="302.1" y1="447.1" x2="302.1" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="450.3" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="306.0" y1="458.2" x2="306.0" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="461.9" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="310.0" y1="447.9" x2="310.0" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="454.2" width="2.44" height="14.6" fill="var(--up)"/>
<line x1="313.9" y1="410.7" x2="313.9" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="413.9" width="2.44" height="34.7" fill="var(--up)"/>
<line x1="317.8" y1="354.3" x2="317.8" y2="419.9" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="356.9" width="2.44" height="57.5" fill="var(--up)"/>
<line x1="321.8" y1="354.6" x2="321.8" y2="396.4" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="359.4" width="2.44" height="24.5" fill="var(--down)"/>
<line x1="325.7" y1="350.4" x2="325.7" y2="389.6" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="361.5" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="329.7" y1="356.5" x2="329.7" y2="381.9" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="363.2" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="333.6" y1="359.3" x2="333.6" y2="388.3" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="365.5" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="337.5" y1="360.7" x2="337.5" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="368.6" width="2.44" height="14.5" fill="var(--up)"/>
<line x1="341.5" y1="366.3" x2="341.5" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="374.9" width="2.44" height="23.1" fill="var(--down)"/>
<line x1="345.4" y1="389.7" x2="345.4" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="393.3" width="2.44" height="41.5" fill="var(--down)"/>
<line x1="349.3" y1="406.0" x2="349.3" y2="433.1" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="407.1" width="2.44" height="24.7" fill="var(--up)"/>
<line x1="353.3" y1="379.4" x2="353.3" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="399.6" width="2.44" height="34.4" fill="var(--down)"/>
<line x1="357.2" y1="402.1" x2="357.2" y2="427.4" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="416.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="361.1" y1="383.0" x2="361.1" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="386.8" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="365.1" y1="299.8" x2="365.1" y2="374.3" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="302.9" width="2.44" height="70.7" fill="var(--up)"/>
<line x1="369.0" y1="307.7" x2="369.0" y2="358.2" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="327.6" width="2.44" height="23.3" fill="var(--down)"/>
<line x1="373.0" y1="342.1" x2="373.0" y2="384.9" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="342.6" width="2.44" height="33.3" fill="var(--down)"/>
<line x1="376.9" y1="376.1" x2="376.9" y2="418.8" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="376.1" width="2.44" height="34.5" fill="var(--down)"/>
<line x1="380.8" y1="387.7" x2="380.8" y2="414.1" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="397.2" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="384.8" y1="376.3" x2="384.8" y2="399.2" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="391.1" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="388.7" y1="377.2" x2="388.7" y2="399.1" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="397.1" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="392.6" y1="362.9" x2="392.6" y2="408.5" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="366.3" width="2.44" height="18.5" fill="var(--up)"/>
<line x1="396.6" y1="316.3" x2="396.6" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="327.1" width="2.44" height="31.0" fill="var(--up)"/>
<line x1="400.5" y1="315.5" x2="400.5" y2="347.4" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="317.3" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="404.4" y1="303.4" x2="404.4" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="319.9" width="2.44" height="14.1" fill="var(--down)"/>
<line x1="408.4" y1="329.6" x2="408.4" y2="358.2" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="339.2" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="412.3" y1="319.3" x2="412.3" y2="367.2" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="340.7" width="2.44" height="25.9" fill="var(--down)"/>
<line x1="416.3" y1="355.2" x2="416.3" y2="375.7" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="355.8" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="420.2" y1="341.3" x2="420.2" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="350.4" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="424.1" y1="334.3" x2="424.1" y2="376.0" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="334.8" width="2.44" height="26.7" fill="var(--up)"/>
<line x1="428.1" y1="315.9" x2="428.1" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="329.6" width="2.44" height="27.5" fill="var(--down)"/>
<line x1="432.0" y1="335.1" x2="432.0" y2="364.1" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="351.9" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="435.9" y1="360.8" x2="435.9" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="375.0" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="439.9" y1="366.0" x2="439.9" y2="419.2" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="375.0" width="2.44" height="23.9" fill="var(--down)"/>
<line x1="443.8" y1="374.7" x2="443.8" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="377.2" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="447.7" y1="380.8" x2="447.7" y2="411.5" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="384.7" width="2.44" height="20.6" fill="var(--down)"/>
<line x1="451.7" y1="399.1" x2="451.7" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="405.8" width="2.44" height="28.9" fill="var(--down)"/>
<line x1="455.6" y1="415.5" x2="455.6" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="419.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="459.6" y1="404.4" x2="459.6" y2="422.6" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="415.6" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="463.5" y1="414.8" x2="463.5" y2="454.7" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="423.0" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="467.4" y1="444.1" x2="467.4" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="445.9" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="471.4" y1="469.1" x2="471.4" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="469.5" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="475.3" y1="468.7" x2="475.3" y2="490.0" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="469.2" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="479.2" y1="472.5" x2="479.2" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="472.5" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="483.2" y1="499.2" x2="483.2" y2="541.4" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="503.7" width="2.44" height="33.1" fill="var(--down)"/>
<line x1="487.1" y1="478.0" x2="487.1" y2="527.0" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="482.0" width="2.44" height="44.0" fill="var(--up)"/>
<line x1="491.0" y1="472.3" x2="491.0" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="474.4" width="2.44" height="12.3" fill="var(--up)"/>
<line x1="495.0" y1="469.5" x2="495.0" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="481.1" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="498.9" y1="481.5" x2="498.9" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="497.70" y="481.5" width="2.44" height="17.4" fill="var(--down)"/>
<line x1="502.9" y1="497.3" x2="502.9" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="499.7" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="506.8" y1="492.2" x2="506.8" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="498.4" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="510.7" y1="504.2" x2="510.7" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="507.3" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="514.7" y1="499.2" x2="514.7" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="507.8" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="518.6" y1="501.2" x2="518.6" y2="518.7" stroke="var(--up)" class="wick"/>
<rect x="517.38" y="502.9" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="522.5" y1="503.3" x2="522.5" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="521.32" y="510.1" width="2.44" height="13.4" fill="var(--down)"/>
<line x1="526.5" y1="518.9" x2="526.5" y2="533.7" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="523.7" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="530.4" y1="510.8" x2="530.4" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="514.2" width="2.44" height="13.0" fill="var(--up)"/>
<line x1="534.3" y1="496.2" x2="534.3" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="498.7" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="538.3" y1="466.7" x2="538.3" y2="497.6" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="482.8" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="542.2" y1="501.1" x2="542.2" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="502.4" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="546.2" y1="509.4" x2="546.2" y2="527.1" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="509.8" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="550.1" y1="513.4" x2="550.1" y2="532.9" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="520.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="554.0" y1="507.8" x2="554.0" y2="521.7" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="510.3" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="558.0" y1="511.1" x2="558.0" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="511.5" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="561.9" y1="499.4" x2="561.9" y2="520.9" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="515.3" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="565.8" y1="507.3" x2="565.8" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="508.3" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="569.8" y1="500.8" x2="569.8" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="504.7" width="2.44" height="8.0" fill="var(--down)"/>
<line x1="573.7" y1="501.5" x2="573.7" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="510.3" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="577.7" y1="512.2" x2="577.7" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="516.1" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="581.6" y1="513.7" x2="581.6" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="522.6" width="2.44" height="8.9" fill="var(--down)"/>
<line x1="585.5" y1="517.9" x2="585.5" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="524.8" width="2.44" height="8.1" fill="var(--down)"/>
<line x1="589.5" y1="528.5" x2="589.5" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="588.24" y="532.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="593.4" y1="535.1" x2="593.4" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="536.2" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="597.3" y1="549.8" x2="597.3" y2="565.7" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="554.2" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="601.3" y1="554.9" x2="601.3" y2="567.9" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="558.2" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="605.2" y1="548.5" x2="605.2" y2="562.8" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="550.9" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="609.1" y1="551.3" x2="609.1" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="554.8" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="613.1" y1="544.4" x2="613.1" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="551.7" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="617.0" y1="558.3" x2="617.0" y2="578.1" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="559.2" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="621.0" y1="577.1" x2="621.0" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="579.0" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="624.9" y1="588.6" x2="624.9" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="589.9" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="628.8" y1="579.3" x2="628.8" y2="600.5" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="580.2" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="632.8" y1="571.5" x2="632.8" y2="592.4" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="573.8" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="636.7" y1="581.1" x2="636.7" y2="602.4" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="582.0" width="2.44" height="19.1" fill="var(--up)"/>
<line x1="640.6" y1="576.5" x2="640.6" y2="590.4" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="583.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="644.6" y1="587.7" x2="644.6" y2="596.6" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="588.2" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="648.5" y1="565.9" x2="648.5" y2="585.4" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="567.4" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="652.4" y1="577.4" x2="652.4" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="580.7" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="656.4" y1="574.9" x2="656.4" y2="586.4" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="583.1" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="660.3" y1="574.7" x2="660.3" y2="589.9" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="576.8" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="664.3" y1="538.8" x2="664.3" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="540.6" width="2.44" height="26.2" fill="var(--up)"/>
<line x1="668.2" y1="477.0" x2="668.2" y2="528.1" stroke="var(--up)" class="wick"/>
<rect x="666.97" y="480.6" width="2.44" height="35.7" fill="var(--up)"/>
<line x1="672.1" y1="454.7" x2="672.1" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="462.0" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="676.1" y1="454.4" x2="676.1" y2="471.6" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="465.1" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="680.0" y1="463.1" x2="680.0" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="678.78" y="467.3" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="683.9" y1="464.4" x2="683.9" y2="488.9" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="464.8" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="687.9" y1="465.2" x2="687.9" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="473.9" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="691.8" y1="475.2" x2="691.8" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="483.1" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="695.7" y1="498.3" x2="695.7" y2="526.1" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="498.4" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="699.7" y1="509.0" x2="699.7" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="512.0" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="703.6" y1="517.5" x2="703.6" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="702.40" y="522.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="707.6" y1="518.1" x2="707.6" y2="538.4" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="520.3" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="711.5" y1="487.6" x2="711.5" y2="521.1" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="488.9" width="2.44" height="30.8" fill="var(--up)"/>
<line x1="715.4" y1="482.9" x2="715.4" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="485.6" width="2.44" height="6.1" fill="var(--up)"/>
<line x1="719.4" y1="466.4" x2="719.4" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="478.9" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="723.3" y1="466.7" x2="723.3" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="469.2" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="727.2" y1="430.2" x2="727.2" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="433.4" width="2.44" height="29.8" fill="var(--up)"/>
<line x1="731.2" y1="435.8" x2="731.2" y2="465.0" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="445.6" width="2.44" height="16.6" fill="var(--down)"/>
<line x1="735.1" y1="451.6" x2="735.1" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="453.1" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="739.0" y1="418.6" x2="739.0" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="737.83" y="430.3" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="743.0" y1="432.2" x2="743.0" y2="479.5" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="455.5" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="746.9" y1="455.9" x2="746.9" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="456.1" width="2.44" height="14.7" fill="var(--down)"/>
<line x1="750.9" y1="453.8" x2="750.9" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="460.0" width="2.44" height="19.8" fill="var(--up)"/>
<line x1="754.8" y1="473.7" x2="754.8" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="475.5" width="2.44" height="12.3" fill="var(--down)"/>
<line x1="758.7" y1="490.1" x2="758.7" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="491.5" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="762.7" y1="506.8" x2="762.7" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="512.5" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="766.6" y1="501.8" x2="766.6" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="504.2" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="770.5" y1="402.2" x2="770.5" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="403.6" width="2.44" height="62.2" fill="var(--up)"/>
<line x1="774.5" y1="312.9" x2="774.5" y2="397.8" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="346.5" width="2.44" height="47.8" fill="var(--up)"/>
<line x1="778.4" y1="345.2" x2="778.4" y2="394.4" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="347.2" width="2.44" height="23.9" fill="var(--down)"/>
<line x1="782.3" y1="367.5" x2="782.3" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="376.4" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="786.3" y1="333.7" x2="786.3" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="345.1" width="2.44" height="26.5" fill="var(--up)"/>
<line x1="790.2" y1="334.6" x2="790.2" y2="377.4" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="334.9" width="2.44" height="20.9" fill="var(--up)"/>
<line x1="794.2" y1="319.6" x2="794.2" y2="371.0" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="349.9" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="798.1" y1="316.8" x2="798.1" y2="352.9" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="338.5" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="802.0" y1="337.9" x2="802.0" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="345.1" width="2.44" height="30.3" fill="var(--down)"/>
<line x1="806.0" y1="355.5" x2="806.0" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="374.0" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="809.9" y1="390.3" x2="809.9" y2="442.0" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="390.8" width="2.44" height="42.3" fill="var(--down)"/>
<line x1="813.8" y1="388.2" x2="813.8" y2="430.8" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="402.2" width="2.44" height="17.6" fill="var(--up)"/>
<line x1="817.8" y1="389.3" x2="817.8" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="403.4" width="2.44" height="34.9" fill="var(--down)"/>
<line x1="821.7" y1="418.6" x2="821.7" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="442.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="825.7" y1="424.4" x2="825.7" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="433.6" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="829.6" y1="423.3" x2="829.6" y2="448.6" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="436.5" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="833.5" y1="381.6" x2="833.5" y2="416.6" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="395.5" width="2.44" height="21.1" fill="var(--up)"/>
<line x1="837.5" y1="397.8" x2="837.5" y2="432.6" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="403.5" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="841.4" y1="422.2" x2="841.4" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="428.5" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="845.3" y1="419.7" x2="845.3" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="420.0" width="2.44" height="16.1" fill="var(--up)"/>
<line x1="849.3" y1="405.3" x2="849.3" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="423.5" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="853.2" y1="388.5" x2="853.2" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="414.7" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="857.1" y1="424.1" x2="857.1" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="424.2" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="861.1" y1="433.8" x2="861.1" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="438.6" width="2.44" height="24.8" fill="var(--down)"/>
<line x1="865.0" y1="448.6" x2="865.0" y2="478.7" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="450.2" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="869.0" y1="426.7" x2="869.0" y2="454.8" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="433.4" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="872.9" y1="419.4" x2="872.9" y2="442.5" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="431.0" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="876.8" y1="422.4" x2="876.8" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="437.1" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="880.8" y1="420.2" x2="880.8" y2="457.3" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="436.2" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="884.7" y1="436.7" x2="884.7" y2="458.1" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="453.3" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="888.6" y1="455.9" x2="888.6" y2="485.1" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="459.5" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="892.6" y1="470.0" x2="892.6" y2="491.2" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="483.3" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="896.5" y1="470.1" x2="896.5" y2="485.1" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="475.1" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="900.4" y1="467.6" x2="900.4" y2="494.0" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="470.1" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="904.4" y1="498.1" x2="904.4" y2="516.4" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="498.1" width="2.44" height="16.1" fill="var(--down)"/>
<line x1="908.3" y1="504.9" x2="908.3" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="509.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="912.3" y1="503.1" x2="912.3" y2="526.5" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="508.3" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="916.2" y1="524.5" x2="916.2" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="524.5" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="920.1" y1="533.6" x2="920.1" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="544.3" width="2.44" height="4.2" fill="var(--up)"/>
<line x1="924.1" y1="531.5" x2="924.1" y2="545.0" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="540.1" width="2.44" height="4.4" fill="var(--down)"/>
<line x1="928.0" y1="524.2" x2="928.0" y2="540.1" stroke="var(--up)" class="wick"/>
<rect x="926.78" y="527.6" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="931.9" y1="525.0" x2="931.9" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="530.7" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="935.9" y1="526.8" x2="935.9" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="538.5" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="939.8" y1="539.5" x2="939.8" y2="552.9" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="540.0" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="943.7" y1="500.4" x2="943.7" y2="528.4" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="500.9" width="2.44" height="25.8" fill="var(--up)"/>
<line x1="947.7" y1="510.6" x2="947.7" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="514.3" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="951.6" y1="533.9" x2="951.6" y2="554.6" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="535.6" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="955.6" y1="522.5" x2="955.6" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="524.8" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="959.5" y1="510.1" x2="959.5" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="518.6" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="963.4" y1="491.2" x2="963.4" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="493.6" width="2.44" height="29.5" fill="var(--up)"/>
<line x1="967.4" y1="463.6" x2="967.4" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="464.7" width="2.44" height="23.3" fill="var(--up)"/>
<line x1="971.3" y1="462.0" x2="971.3" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="468.0" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="975.2" y1="484.0" x2="975.2" y2="519.3" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="502.6" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="979.2" y1="478.9" x2="979.2" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="481.4" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="983.1" y1="479.4" x2="983.1" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="486.4" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="987.0" y1="484.8" x2="987.0" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="985.83" y="489.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="991.0" y1="477.6" x2="991.0" y2="492.3" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="480.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="994.9" y1="465.9" x2="994.9" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="479.2" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="998.9" y1="470.5" x2="998.9" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="475.0" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="1002.8" y1="472.1" x2="1002.8" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="479.7" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="1006.7" y1="482.2" x2="1006.7" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="496.4" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="1010.7" y1="497.1" x2="1010.7" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="503.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1014.6" y1="502.2" x2="1014.6" y2="517.6" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="505.4" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="1018.5" y1="484.0" x2="1018.5" y2="507.3" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="487.2" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="1022.5" y1="494.0" x2="1022.5" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="497.2" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="1026.4" y1="500.6" x2="1026.4" y2="514.7" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="503.4" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="1030.3" y1="508.3" x2="1030.3" y2="533.1" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="513.1" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="1034.3" y1="518.7" x2="1034.3" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="526.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1038.2" y1="528.9" x2="1038.2" y2="545.2" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="531.4" width="2.44" height="8.9" fill="var(--down)"/>
<line x1="1042.2" y1="534.6" x2="1042.2" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="537.0" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="1046.1" y1="541.7" x2="1046.1" y2="549.6" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="547.1" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1050.0" y1="544.7" x2="1050.0" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="1048.81" y="548.1" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="60" y1="464.9" x2="1052" y2="464.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="468.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$22 R1</text>
<text x="1058" y="480.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="350.1" x2="1052" y2="350.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="353.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$29 R2</text>
<text x="1058" y="365.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="309.8" x2="1052" y2="309.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="313.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$32 R3</text>
<text x="1058" y="325.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="555.0" x2="1052" y2="555.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="549.0" font-size="11.5" fill="var(--support)" font-weight="600">$16.05 S1</text>
<text x="1058" y="561.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="548.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="540.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $16.49 (2026-09-02)</text>
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
| R3 | $32 | 5 | 2025-12-22·2026-01-07·2026-01-15·2026-05-22·2026-06-02 — 이 1년에서 가장 두껍게 눌린 고점대 |
| R2 | $29 | 2 | 2025-09-24·2025-12-08 스윙 고점대 |
| R1 | $22 | 3 | 2026-02-26·2026-08-05·2026-08-13 — 현재가에 가장 가까운 저항 |
| **현재가** | **$16.49** (2026-09-02 종가) | — | R1과 S1 사이 |
| S1 | $16.05 | 2 | 2026-07-17·2026-07-29 — 현재가 바로 아래(약 -2.7%)에 붙어 있는 지지 |
| 참고선 | $46.75 / $12.75 | — | 최근 1년 장중 최고/최저. 최고가는 2026-01 인수 발표 국면의 단발 극단값이라 터치가 쌓이지 않아 저항으로 보지 않는다 |

현재가($16.49)는 S1($16.05)에 불과 2.7% 위로 바짝 붙어 있고, 위쪽 첫 저항 R1($22)까지는 33% 떨어져 있다 — **아래쪽 지지는 가깝고 위쪽 저항은 먼 비대칭 구조**다. 다만 S1은 터치 2회로 얕은 클러스터라 강한 지지로 보기는 어렵다.

---

## 3. 관측된 특이 구간 — 2026-01 인수 발표 이후의 하락 레짐

- 최근 1년 고가 $46.75(장중)에서 현재 $16.49까지 **약 -65%** 하락했다. 고점 국면은 2026-01 Quantum Circuits 인수 발표 전후이며, 그 이후로는 R3($32) → R2($29) → R1($22)로 저항대가 계단식으로 낮아지는 흐름이 이어졌다.
- R3($32)는 2025-12-22부터 2026-06-02까지 다섯 차례 눌린 자리로, 이 1년 창에서 가장 두꺼운 클러스터다. **인수 발표로 형성된 기대 가격대가 반년에 걸쳐 반복적으로 거부당한 구간**으로 읽을 수 있다.
- 2026-08-05~08-13 구간에 R1($22) 부근을 두 차례 시도했다가 밀렸는데, 이 시기는 Q2 실적 발표(08-06)와 Nature 논문·NRC 자금 뉴스가 겹친 때다([최근 뉴스 / 이슈](./08_news.md)) — **호재성 뉴스가 나온 구간에서도 $22를 넘지 못했다**는 점이 이 레벨의 성격을 보여준다.
- 다만 가격이 왜 그렇게 움직였는지의 인과는 확인하지 못했다. 위 서술은 시점의 병치이지 인과 주장이 아니다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-03~2026-09-02. 수집 시점: 2026-09-03. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py QBTS --name "D-Wave Quantum" --close-on 2026-09-02 --emit all` (일봉·1년 기본 파라미터, 옵션 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 이 1년 안에 -65% 하락이 들어 있어 고가권 클러스터(R3·R2)와 저가권 클러스터(S1)가 서로 다른 레짐에서 만들어졌다. 하나의 연속된 구조로 읽지 말 것.
    - 해당 기간 주식분할은 없었다. 다만 증자·M&A 대가로 발행주식수가 계속 늘었으므로 **주가 연속성은 유지되지만 주당 가치의 기준은 계속 바뀌었다** — 가격 레벨만으로 기업가치 변화를 읽지 말 것([핵심 지표](./04_metrics.md) A.4).

---

*작성일: 2026-09-03*
