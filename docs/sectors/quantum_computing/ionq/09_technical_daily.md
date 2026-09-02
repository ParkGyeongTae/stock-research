# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-02 종가 $37.64는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다. 상장 이후 주식분할이 없어 원주가와 수정주가가 같다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-03 ~ 2026-09-02)

<div class="ionq-chart">
<style>
.ionq-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ionq-chart svg { width:100%; height:auto; display:block; }
.ionq-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ionq-chart .title { fill: var(--ink); font-weight:600; }
.ionq-chart .grid { stroke: var(--grid); stroke-width:1; }
.ionq-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="IonQ(IONQ) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">IonQ (IONQ) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-03 ~ 2026-09-02 · 마지막 종가 $37.64 (2026-09-02) · 단위 USD</text>
<line x1="60" y1="571.7" x2="1052" y2="571.7" class="grid"/>
<text x="52" y="575.7" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="481.2" x2="1052" y2="481.2" class="grid"/>
<text x="52" y="485.2" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="390.8" x2="1052" y2="390.8" class="grid"/>
<text x="52" y="394.8" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="300.3" x2="1052" y2="300.3" class="grid"/>
<text x="52" y="304.3" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="209.8" x2="1052" y2="209.8" class="grid"/>
<text x="52" y="213.8" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="119.3" x2="1052" y2="119.3" class="grid"/>
<text x="52" y="123.3" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
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
<line x1="62.0" y1="452.2" x2="62.0" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="457.3" width="2.44" height="15.2" fill="var(--down)"/>
<line x1="65.9" y1="453.8" x2="65.9" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="462.1" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="69.8" y1="456.5" x2="69.8" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="459.0" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="73.8" y1="457.8" x2="73.8" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="462.3" width="2.44" height="9.8" fill="var(--down)"/>
<line x1="77.7" y1="442.7" x2="77.7" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="445.0" width="2.44" height="23.6" fill="var(--up)"/>
<line x1="81.7" y1="434.4" x2="81.7" y2="449.0" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="442.2" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="85.6" y1="415.8" x2="85.6" y2="450.7" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="417.5" width="2.44" height="25.8" fill="var(--up)"/>
<line x1="89.5" y1="335.8" x2="89.5" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="340.0" width="2.44" height="75.2" fill="var(--up)"/>
<line x1="93.5" y1="301.3" x2="93.5" y2="336.9" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="308.3" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="97.4" y1="274.5" x2="97.4" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="279.8" width="2.44" height="29.7" fill="var(--up)"/>
<line x1="101.3" y1="242.5" x2="101.3" y2="290.5" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="251.1" width="2.44" height="19.3" fill="var(--up)"/>
<line x1="105.3" y1="205.9" x2="105.3" y2="251.2" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="222.7" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="109.2" y1="198.0" x2="109.2" y2="249.3" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="206.1" width="2.44" height="40.1" fill="var(--up)"/>
<line x1="113.1" y1="181.1" x2="113.1" y2="244.6" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="192.3" width="2.44" height="34.7" fill="var(--up)"/>
<line x1="117.1" y1="154.4" x2="117.1" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="163.3" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="121.0" y1="156.0" x2="121.0" y2="200.7" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="162.3" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="125.0" y1="189.1" x2="125.0" y2="237.8" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="199.3" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="128.9" y1="206.0" x2="128.9" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="224.2" width="2.44" height="10.2" fill="var(--down)"/>
<line x1="132.8" y1="219.9" x2="132.8" y2="271.2" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="224.5" width="2.44" height="37.3" fill="var(--down)"/>
<line x1="136.8" y1="255.0" x2="136.8" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="267.8" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="140.7" y1="256.4" x2="140.7" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="272.3" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="144.6" y1="213.4" x2="144.6" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="213.4" width="2.44" height="43.3" fill="var(--up)"/>
<line x1="148.6" y1="175.8" x2="148.6" y2="224.7" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="180.1" width="2.44" height="24.3" fill="var(--up)"/>
<line x1="152.5" y1="126.3" x2="152.5" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="128.5" width="2.44" height="63.2" fill="var(--up)"/>
<line x1="156.4" y1="92.5" x2="156.4" y2="160.2" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="110.6" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="160.4" y1="97.5" x2="160.4" y2="186.3" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="128.8" width="2.44" height="42.1" fill="var(--down)"/>
<line x1="164.3" y1="137.4" x2="164.3" y2="176.8" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="142.0" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="168.3" y1="143.0" x2="168.3" y2="204.0" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="146.5" width="2.44" height="57.5" fill="var(--down)"/>
<line x1="172.2" y1="77.4" x2="172.2" y2="184.5" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="100.4" width="2.44" height="72.2" fill="var(--up)"/>
<line x1="176.1" y1="109.6" x2="176.1" y2="156.2" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="120.7" width="2.44" height="20.8" fill="var(--down)"/>
<line x1="180.1" y1="117.3" x2="180.1" y2="202.6" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="119.9" width="2.44" height="68.1" fill="var(--down)"/>
<line x1="184.0" y1="174.8" x2="184.0" y2="250.5" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="174.8" width="2.44" height="74.9" fill="var(--down)"/>
<line x1="187.9" y1="248.5" x2="187.9" y2="289.4" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="251.4" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="191.9" y1="250.5" x2="191.9" y2="312.1" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="252.2" width="2.44" height="48.6" fill="var(--down)"/>
<line x1="195.8" y1="292.1" x2="195.8" y2="325.5" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="296.3" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="199.7" y1="306.2" x2="199.7" y2="370.2" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="316.6" width="2.44" height="24.9" fill="var(--down)"/>
<line x1="203.7" y1="273.8" x2="203.7" y2="327.4" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="290.3" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="207.6" y1="263.1" x2="207.6" y2="301.0" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="282.1" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="211.6" y1="250.5" x2="211.6" y2="279.7" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="273.1" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="215.5" y1="258.9" x2="215.5" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="275.0" width="2.44" height="51.1" fill="var(--down)"/>
<line x1="219.4" y1="281.3" x2="219.4" y2="319.1" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="290.2" width="2.44" height="20.4" fill="var(--up)"/>
<line x1="223.4" y1="283.6" x2="223.4" y2="316.6" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="298.7" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="227.3" y1="273.4" x2="227.3" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="278.8" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="231.2" y1="275.9" x2="231.2" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="279.0" width="2.44" height="35.7" fill="var(--down)"/>
<line x1="235.2" y1="326.0" x2="235.2" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="338.6" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="239.1" y1="332.8" x2="239.1" y2="362.7" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="341.8" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="243.0" y1="309.4" x2="243.0" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="323.5" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="247.0" y1="306.6" x2="247.0" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="245.76" y="306.9" width="2.44" height="42.1" fill="var(--up)"/>
<line x1="250.9" y1="309.2" x2="250.9" y2="347.2" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="313.9" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="254.9" y1="336.2" x2="254.9" y2="357.1" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="349.4" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="258.8" y1="340.1" x2="258.8" y2="391.8" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="347.7" width="2.44" height="36.6" fill="var(--down)"/>
<line x1="262.7" y1="391.7" x2="262.7" y2="442.3" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="395.8" width="2.44" height="36.6" fill="var(--down)"/>
<line x1="266.7" y1="401.8" x2="266.7" y2="455.7" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="416.3" width="2.44" height="38.0" fill="var(--up)"/>
<line x1="270.6" y1="397.5" x2="270.6" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="410.8" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="274.5" y1="388.2" x2="274.5" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="398.7" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="278.5" y1="384.6" x2="278.5" y2="414.9" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="398.5" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="282.4" y1="394.7" x2="282.4" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="403.7" width="2.44" height="68.5" fill="var(--down)"/>
<line x1="286.3" y1="456.3" x2="286.3" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="458.1" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="290.3" y1="414.9" x2="290.3" y2="458.7" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="420.1" width="2.44" height="36.3" fill="var(--up)"/>
<line x1="294.2" y1="409.7" x2="294.2" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="417.4" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="298.2" y1="406.6" x2="298.2" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="414.3" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="302.1" y1="392.1" x2="302.1" y2="412.7" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="397.1" width="2.44" height="14.5" fill="var(--up)"/>
<line x1="306.0" y1="401.0" x2="306.0" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="403.1" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="310.0" y1="393.7" x2="310.0" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="412.7" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="313.9" y1="400.7" x2="313.9" y2="433.2" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="403.0" width="2.44" height="15.7" fill="var(--up)"/>
<line x1="317.8" y1="342.6" x2="317.8" y2="406.1" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="347.7" width="2.44" height="55.1" fill="var(--up)"/>
<line x1="321.8" y1="352.2" x2="321.8" y2="380.5" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="354.6" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="325.7" y1="347.2" x2="325.7" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="351.3" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="329.7" y1="339.6" x2="329.7" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="350.6" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="333.6" y1="358.1" x2="333.6" y2="379.5" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="361.8" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="337.5" y1="364.7" x2="337.5" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="367.7" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="341.5" y1="363.6" x2="341.5" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="371.9" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="345.4" y1="381.7" x2="345.4" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="383.7" width="2.44" height="42.6" fill="var(--down)"/>
<line x1="349.3" y1="391.7" x2="349.3" y2="418.8" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="393.7" width="2.44" height="24.7" fill="var(--up)"/>
<line x1="353.3" y1="371.3" x2="353.3" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="388.8" width="2.44" height="39.5" fill="var(--down)"/>
<line x1="357.2" y1="402.4" x2="357.2" y2="426.6" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="407.7" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="361.1" y1="395.8" x2="361.1" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="404.5" width="2.44" height="12.1" fill="var(--up)"/>
<line x1="365.1" y1="340.1" x2="365.1" y2="393.7" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="355.8" width="2.44" height="36.0" fill="var(--up)"/>
<line x1="369.0" y1="349.7" x2="369.0" y2="380.4" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="366.1" width="2.44" height="12.1" fill="var(--down)"/>
<line x1="373.0" y1="373.8" x2="373.0" y2="402.3" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="375.4" width="2.44" height="17.0" fill="var(--down)"/>
<line x1="376.9" y1="393.7" x2="376.9" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="394.5" width="2.44" height="32.5" fill="var(--down)"/>
<line x1="380.8" y1="420.1" x2="380.8" y2="439.1" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="431.8" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="384.8" y1="419.4" x2="384.8" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="423.2" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="388.7" y1="423.0" x2="388.7" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="429.9" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="392.6" y1="417.1" x2="392.6" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="420.0" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="396.6" y1="387.9" x2="396.6" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="402.4" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="400.5" y1="383.8" x2="400.5" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="383.9" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="404.4" y1="373.9" x2="404.4" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="390.8" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="408.4" y1="368.1" x2="408.4" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="386.7" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="412.3" y1="367.1" x2="412.3" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="377.6" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="416.3" y1="381.5" x2="416.3" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="382.2" width="2.44" height="21.4" fill="var(--up)"/>
<line x1="420.2" y1="373.4" x2="420.2" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="380.3" width="2.44" height="20.1" fill="var(--down)"/>
<line x1="424.1" y1="382.4" x2="424.1" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="382.8" width="2.44" height="21.2" fill="var(--up)"/>
<line x1="428.1" y1="376.5" x2="428.1" y2="413.0" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="379.2" width="2.44" height="33.7" fill="var(--down)"/>
<line x1="432.0" y1="373.7" x2="432.0" y2="413.2" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="383.5" width="2.44" height="24.5" fill="var(--up)"/>
<line x1="435.9" y1="352.4" x2="435.9" y2="403.8" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="384.8" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="439.9" y1="366.7" x2="439.9" y2="429.8" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="375.3" width="2.44" height="30.6" fill="var(--down)"/>
<line x1="443.8" y1="389.1" x2="443.8" y2="409.4" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="396.8" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="447.7" y1="395.2" x2="447.7" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="397.6" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="451.7" y1="385.4" x2="451.7" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="406.0" width="2.44" height="44.8" fill="var(--down)"/>
<line x1="455.6" y1="423.0" x2="455.6" y2="453.8" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="431.6" width="2.44" height="8.4" fill="var(--up)"/>
<line x1="459.6" y1="418.8" x2="459.6" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="424.9" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="463.5" y1="428.2" x2="463.5" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="428.2" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="467.4" y1="449.7" x2="467.4" y2="491.1" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="450.5" width="2.44" height="30.9" fill="var(--down)"/>
<line x1="471.4" y1="474.7" x2="471.4" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="475.5" width="2.44" height="18.7" fill="var(--down)"/>
<line x1="475.3" y1="482.9" x2="475.3" y2="511.7" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="484.8" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="479.2" y1="494.4" x2="479.2" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="494.8" width="2.44" height="28.6" fill="var(--down)"/>
<line x1="483.2" y1="532.1" x2="483.2" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="536.2" width="2.44" height="31.6" fill="var(--down)"/>
<line x1="487.1" y1="516.5" x2="487.1" y2="559.5" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="526.6" width="2.44" height="28.0" fill="var(--up)"/>
<line x1="491.0" y1="520.7" x2="491.0" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="522.1" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="495.0" y1="512.3" x2="495.0" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="524.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="498.9" y1="516.9" x2="498.9" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="497.70" y="517.0" width="2.44" height="22.1" fill="var(--down)"/>
<line x1="502.9" y1="538.2" x2="502.9" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="538.2" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="506.8" y1="529.6" x2="506.8" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="534.5" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="510.7" y1="532.6" x2="510.7" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="540.2" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="514.7" y1="527.5" x2="514.7" y2="550.1" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="541.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="518.6" y1="539.3" x2="518.6" y2="553.8" stroke="var(--up)" class="wick"/>
<rect x="517.38" y="540.7" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="522.5" y1="536.6" x2="522.5" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="521.32" y="547.6" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="526.5" y1="556.6" x2="526.5" y2="570.2" stroke="var(--down)" class="wick"/>
<rect x="525.26" y="562.5" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="530.4" y1="554.0" x2="530.4" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="557.1" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="534.3" y1="531.9" x2="534.3" y2="555.1" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="539.2" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="538.3" y1="464.0" x2="538.3" y2="492.5" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="473.3" width="2.44" height="16.6" fill="var(--up)"/>
<line x1="542.2" y1="485.2" x2="542.2" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="486.5" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="546.2" y1="495.4" x2="546.2" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="496.3" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="550.1" y1="498.2" x2="550.1" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="507.9" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="554.0" y1="497.2" x2="554.0" y2="512.5" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="502.2" width="2.44" height="5.0" fill="var(--down)"/>
<line x1="558.0" y1="511.3" x2="558.0" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="512.0" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="561.9" y1="504.0" x2="561.9" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="519.9" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="565.8" y1="516.7" x2="565.8" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="518.6" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="569.8" y1="509.1" x2="569.8" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="517.9" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="573.7" y1="518.4" x2="573.7" y2="540.0" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="523.9" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="577.7" y1="529.1" x2="577.7" y2="544.3" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="535.7" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="581.6" y1="530.3" x2="581.6" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="539.3" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="585.5" y1="531.8" x2="585.5" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="539.9" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="589.5" y1="534.2" x2="589.5" y2="544.0" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="541.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="593.4" y1="535.5" x2="593.4" y2="550.4" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="544.1" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="597.3" y1="548.6" x2="597.3" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="554.5" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="601.3" y1="551.4" x2="601.3" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="555.4" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="605.2" y1="538.9" x2="605.2" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="543.6" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="609.1" y1="540.4" x2="609.1" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="547.3" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="613.1" y1="533.9" x2="613.1" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="541.1" width="2.44" height="12.8" fill="var(--down)"/>
<line x1="617.0" y1="557.1" x2="617.0" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="559.1" width="2.44" height="14.1" fill="var(--down)"/>
<line x1="621.0" y1="575.3" x2="621.0" y2="595.5" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="575.8" width="2.44" height="18.5" fill="var(--down)"/>
<line x1="624.9" y1="588.4" x2="624.9" y2="608.9" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="591.7" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="628.8" y1="579.1" x2="628.8" y2="598.4" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="582.3" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="632.8" y1="572.5" x2="632.8" y2="593.7" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="575.0" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="636.7" y1="576.3" x2="636.7" y2="601.2" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="578.0" width="2.44" height="22.6" fill="var(--up)"/>
<line x1="640.6" y1="569.0" x2="640.6" y2="583.4" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="577.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="644.6" y1="581.8" x2="644.6" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="583.3" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="648.5" y1="561.8" x2="648.5" y2="585.2" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="565.7" width="2.44" height="15.1" fill="var(--down)"/>
<line x1="652.4" y1="578.5" x2="652.4" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="583.0" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="656.4" y1="577.4" x2="656.4" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="582.7" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="660.3" y1="573.2" x2="660.3" y2="591.0" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="573.9" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="664.3" y1="518.6" x2="664.3" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="519.6" width="2.44" height="36.0" fill="var(--up)"/>
<line x1="668.2" y1="451.0" x2="668.2" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="666.97" y="451.8" width="2.44" height="44.2" fill="var(--up)"/>
<line x1="672.1" y1="432.1" x2="672.1" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="438.9" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="676.1" y1="420.7" x2="676.1" y2="447.9" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="426.1" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="680.0" y1="403.7" x2="680.0" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="678.78" y="406.0" width="2.44" height="27.0" fill="var(--up)"/>
<line x1="683.9" y1="402.3" x2="683.9" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="403.4" width="2.44" height="21.0" fill="var(--down)"/>
<line x1="687.9" y1="398.6" x2="687.9" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="414.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="691.8" y1="410.3" x2="691.8" y2="463.9" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="421.4" width="2.44" height="27.0" fill="var(--down)"/>
<line x1="695.7" y1="441.5" x2="695.7" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="441.6" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="699.7" y1="444.4" x2="699.7" y2="471.2" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="446.5" width="2.44" height="15.0" fill="var(--up)"/>
<line x1="703.6" y1="442.6" x2="703.6" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="453.4" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="707.6" y1="457.4" x2="707.6" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="457.4" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="711.5" y1="431.7" x2="711.5" y2="467.8" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="434.9" width="2.44" height="28.8" fill="var(--up)"/>
<line x1="715.4" y1="424.2" x2="715.4" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="425.1" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="719.4" y1="398.5" x2="719.4" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="422.2" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="723.3" y1="405.8" x2="723.3" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="408.9" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="727.2" y1="359.2" x2="727.2" y2="403.7" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="367.5" width="2.44" height="31.4" fill="var(--up)"/>
<line x1="731.2" y1="373.6" x2="731.2" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="390.4" width="2.44" height="21.3" fill="var(--down)"/>
<line x1="735.1" y1="395.8" x2="735.1" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="397.6" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="739.0" y1="313.5" x2="739.0" y2="409.9" stroke="var(--up)" class="wick"/>
<rect x="737.83" y="328.4" width="2.44" height="79.2" fill="var(--up)"/>
<line x1="743.0" y1="308.0" x2="743.0" y2="371.1" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="325.2" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="746.9" y1="334.8" x2="746.9" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="337.0" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="750.9" y1="316.8" x2="750.9" y2="355.4" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="323.2" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="754.8" y1="348.2" x2="754.8" y2="379.1" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="350.0" width="2.44" height="23.1" fill="var(--down)"/>
<line x1="758.7" y1="370.9" x2="758.7" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="374.4" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="762.7" y1="395.8" x2="762.7" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="404.9" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="766.6" y1="366.0" x2="766.6" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="368.4" width="2.44" height="29.1" fill="var(--up)"/>
<line x1="770.5" y1="290.2" x2="770.5" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="310.3" width="2.44" height="38.7" fill="var(--up)"/>
<line x1="774.5" y1="247.8" x2="774.5" y2="318.4" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="267.4" width="2.44" height="51.0" fill="var(--up)"/>
<line x1="778.4" y1="255.0" x2="778.4" y2="299.5" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="261.4" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="782.3" y1="238.7" x2="782.3" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="251.4" width="2.44" height="24.7" fill="var(--up)"/>
<line x1="786.3" y1="196.5" x2="786.3" y2="257.6" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="208.5" width="2.44" height="47.7" fill="var(--up)"/>
<line x1="790.2" y1="190.2" x2="790.2" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="191.1" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="794.2" y1="187.9" x2="794.2" y2="237.2" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="213.0" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="798.1" y1="186.0" x2="798.1" y2="218.0" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="197.1" width="2.44" height="18.5" fill="var(--up)"/>
<line x1="802.0" y1="176.8" x2="802.0" y2="232.3" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="206.9" width="2.44" height="19.0" fill="var(--down)"/>
<line x1="806.0" y1="214.7" x2="806.0" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="236.5" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="809.9" y1="266.0" x2="809.9" y2="337.9" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="268.5" width="2.44" height="60.9" fill="var(--down)"/>
<line x1="813.8" y1="256.0" x2="813.8" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="275.0" width="2.44" height="29.5" fill="var(--up)"/>
<line x1="817.8" y1="264.6" x2="817.8" y2="361.2" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="278.6" width="2.44" height="51.7" fill="var(--down)"/>
<line x1="821.7" y1="293.5" x2="821.7" y2="332.0" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="320.7" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="825.7" y1="305.1" x2="825.7" y2="347.8" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="318.5" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="829.6" y1="298.2" x2="829.6" y2="335.0" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="319.7" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="833.5" y1="268.1" x2="833.5" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="287.6" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="837.5" y1="292.2" x2="837.5" y2="337.3" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="300.7" width="2.44" height="35.2" fill="var(--down)"/>
<line x1="841.4" y1="320.8" x2="841.4" y2="350.5" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="328.3" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="845.3" y1="330.5" x2="845.3" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="331.5" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="849.3" y1="282.3" x2="849.3" y2="340.7" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="315.5" width="2.44" height="15.7" fill="var(--up)"/>
<line x1="853.2" y1="287.0" x2="853.2" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="319.7" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="857.1" y1="324.3" x2="857.1" y2="369.4" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="324.3" width="2.44" height="33.9" fill="var(--down)"/>
<line x1="861.1" y1="344.8" x2="861.1" y2="389.3" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="348.9" width="2.44" height="36.8" fill="var(--down)"/>
<line x1="865.0" y1="368.3" x2="865.0" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="393.9" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="869.0" y1="352.8" x2="869.0" y2="393.9" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="355.7" width="2.44" height="29.5" fill="var(--up)"/>
<line x1="872.9" y1="347.0" x2="872.9" y2="369.0" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="361.3" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="876.8" y1="347.7" x2="876.8" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="371.1" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="880.8" y1="351.0" x2="880.8" y2="407.2" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="380.7" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="884.7" y1="378.7" x2="884.7" y2="401.7" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="399.4" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="888.6" y1="409.3" x2="888.6" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="413.0" width="2.44" height="19.7" fill="var(--down)"/>
<line x1="892.6" y1="424.9" x2="892.6" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="435.3" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="896.5" y1="427.0" x2="896.5" y2="441.7" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="431.5" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="900.4" y1="431.9" x2="900.4" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="433.1" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="904.4" y1="461.5" x2="904.4" y2="493.7" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="462.5" width="2.44" height="28.9" fill="var(--down)"/>
<line x1="908.3" y1="477.2" x2="908.3" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="480.9" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="912.3" y1="480.6" x2="912.3" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="481.2" width="2.44" height="22.5" fill="var(--down)"/>
<line x1="916.2" y1="506.2" x2="916.2" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="508.4" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="920.1" y1="518.2" x2="920.1" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="526.6" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="924.1" y1="514.7" x2="924.1" y2="533.6" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="526.0" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="928.0" y1="516.8" x2="928.0" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="926.78" y="521.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="931.9" y1="517.5" x2="931.9" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="527.5" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="935.9" y1="521.8" x2="935.9" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="534.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="939.8" y1="532.8" x2="939.8" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="534.6" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="943.7" y1="506.8" x2="943.7" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="518.2" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="947.7" y1="529.6" x2="947.7" y2="552.5" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="533.9" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="951.6" y1="532.6" x2="951.6" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="538.1" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="955.6" y1="515.8" x2="955.6" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="519.5" width="2.44" height="23.6" fill="var(--up)"/>
<line x1="959.5" y1="502.5" x2="959.5" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="513.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="963.4" y1="479.8" x2="963.4" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="491.6" width="2.44" height="27.3" fill="var(--up)"/>
<line x1="967.4" y1="462.7" x2="967.4" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="465.7" width="2.44" height="18.9" fill="var(--up)"/>
<line x1="971.3" y1="464.0" x2="971.3" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="472.6" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="975.2" y1="464.2" x2="975.2" y2="484.4" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="468.8" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="979.2" y1="439.5" x2="979.2" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="441.2" width="2.44" height="36.6" fill="var(--up)"/>
<line x1="983.1" y1="443.2" x2="983.1" y2="461.3" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="451.9" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="987.0" y1="444.9" x2="987.0" y2="461.5" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="450.1" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="991.0" y1="431.1" x2="991.0" y2="455.5" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="434.2" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="994.9" y1="409.4" x2="994.9" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="436.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="998.9" y1="415.5" x2="998.9" y2="441.8" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="424.6" width="2.44" height="14.1" fill="var(--up)"/>
<line x1="1002.8" y1="416.0" x2="1002.8" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="419.4" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="1006.7" y1="422.8" x2="1006.7" y2="448.7" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="441.8" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="1010.7" y1="443.3" x2="1010.7" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="450.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1014.6" y1="448.8" x2="1014.6" y2="478.3" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="450.1" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="1018.5" y1="431.8" x2="1018.5" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="437.3" width="2.44" height="24.1" fill="var(--up)"/>
<line x1="1022.5" y1="449.1" x2="1022.5" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="451.1" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="1026.4" y1="457.1" x2="1026.4" y2="472.3" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="462.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1030.3" y1="464.0" x2="1030.3" y2="481.6" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="471.6" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="1034.3" y1="454.6" x2="1034.3" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="459.0" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="1038.2" y1="463.9" x2="1038.2" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="465.6" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="1042.2" y1="476.3" x2="1042.2" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="487.5" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="1046.1" y1="488.0" x2="1046.1" y2="503.0" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="500.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1050.0" y1="497.3" x2="1050.0" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="1048.81" y="502.6" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="60" y1="404.0" x2="1052" y2="404.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="407.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$49 R1</text>
<text x="1058" y="419.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="344.0" x2="1052" y2="344.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="347.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$55 R2</text>
<text x="1058" y="359.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="571.0" x2="1052" y2="571.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="565.0" font-size="11.5" fill="var(--support)" font-weight="600">$30 S1</text>
<text x="1058" y="577.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="502.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="494.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $38 (2026-09-02)</text>
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
| R2 | $55 | 3 | 2025-12-09·2025-12-22·2026-01-20 스윙 고점대 — 2025-10 고점에서 내려오는 도중 세 차례 되돌림이 멈춘 자리 |
| R1 | $49 | 2 | 2026-04-22·2026-08-13 스윙 고점대 — 현재가에 가장 가까운 저항 |
| **현재가** | **$37.64** (2026-09-02 종가) | — | R1과 S1 사이 |
| S1 | $30 | 2 | 2026-02-05·2026-02-23 스윙 저점대 — 현재가에 가장 근접한 지지 |
| 참고선 | $84.64 / $25.89 | — | 최근 1년 장중 최고/최저. 각각 2025-10 고점 국면과 2026-03~04 저점 국면의 단발 극단값이라 터치가 쌓이지 않아 지지·저항으로 보지 않는다 |

유효 클러스터가 3개(R2·R1·S1)뿐이라 R3·S2·S3는 두지 않았다 — 터치 2회 기준을 채운 가격대가 그것뿐이다. 현재가($37.64)는 R1($49)과 S1($30) 사이의 넓은 공백 구간에 있어, 근시일 기준으로 바로 위·아래에 밀집한 레벨이 없다.

---

## 3. 관측된 특이 구간 — 2025-10 고점 이후의 레짐 전환

- 2025-10-13 종가 $82.09(장중 최고 $84.64 부근)로 사상 최고를 찍은 뒤, 2026-03~04 초 $25.89(장중 최저)까지 약 6개월에 걸쳐 **-69%** 하락했다. 같은 기간 매출은 오히려 계속 늘었으므로 이 하락은 실적이 아니라 성장주 전반의 밸류에이션 압축과 이 회사 고유의 희석·통합 우려가 겹친 결과로 보이나, **단일 계기를 특정할 근거는 확인하지 못했다.**
- 2026-04-07 $28.49 → 2026-04-15 $43.25로 6거래일 만에 **+52%** 급반등했다. 이 반등의 계기도 확인하지 못해 단정하지 않는다.
- 2026-08-05 2026 Q2 실적 발표(장 마감 후) 전후로는 08-04 $41.72 → 08-05 $39.93(-4.3%) → 08-06 $39.72로 소폭 하락했다가 08-14 $46.26까지 회복한 뒤, 다시 09-02 $37.64로 내려왔다([최근 뉴스 / 이슈](./08_news.md) 참고).
- 이 1년 구간은 $84.64~$25.89로 고·저가 차이가 3.3배에 달해, **같은 종목의 같은 1년 안에서도 거래 레짐이 여러 번 바뀌었다.** 위 §2의 레벨을 하나의 연속된 구조로 읽지 말 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-03~2026-09-02. 수집 시점: 2026-09-03. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py IONQ --name "IonQ" --close-on 2026-09-02 --emit all` (일봉·1년 기본 파라미터, 옵션 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - §3에서 짚은 대로 이 1년 안에 -69% 하락과 +52% 반등이 모두 들어 있어, 서로 다른 레짐의 스윙 포인트가 한 클러스터 집합에 섞여 있다. 레벨 간 간격이 넓고 터치 횟수가 2~3회로 얕은 것도 그 때문이다.
    - 해당 기간 주식분할은 없었다. 다만 M&A 대가 신주 발행으로 발행주식수가 계속 늘었으므로 **주가 연속성은 유지되지만 주당 가치의 기준은 계속 바뀌었다** — 가격 레벨만으로 기업가치 변화를 읽지 말 것.

---

*작성일: 2026-09-03*
