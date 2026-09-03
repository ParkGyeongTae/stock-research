# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-03 종가 $528.24**는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다. 기간 중 배당 4회가 있었으나 이 차트는 원주가(배당 미반영)라 연말 종가 계열과도 계보가 같다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-04 ~ 2026-09-03)

<div class="noc-chart">
<style>
.noc-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.noc-chart svg { width:100%; height:auto; display:block; }
.noc-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.noc-chart .title { fill: var(--ink); font-weight:600; }
.noc-chart .grid { stroke: var(--grid); stroke-width:1; }
.noc-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="노스롭 그루먼(NOC) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">노스롭 그루먼 (NOC) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-04 ~ 2026-09-03 · 마지막 종가 $528.24 (2026-09-03) · 단위 USD</text>
<line x1="60" y1="571.7" x2="1052" y2="571.7" class="grid"/>
<text x="52" y="575.7" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="481.2" x2="1052" y2="481.2" class="grid"/>
<text x="52" y="485.2" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="390.8" x2="1052" y2="390.8" class="grid"/>
<text x="52" y="394.8" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="300.3" x2="1052" y2="300.3" class="grid"/>
<text x="52" y="304.3" font-size="11" text-anchor="end" fill="var(--muted)">650</text>
<line x1="60" y1="209.8" x2="1052" y2="209.8" class="grid"/>
<text x="52" y="213.8" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="119.3" x2="1052" y2="119.3" class="grid"/>
<text x="52" y="123.3" font-size="11" text-anchor="end" fill="var(--muted)">750</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="136.8" y1="626.0" x2="136.8" y2="631.0" class="axis"/>
<text x="136.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="227.3" y1="626.0" x2="227.3" y2="631.0" class="axis"/>
<text x="227.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="302.1" y1="626.0" x2="302.1" y2="631.0" class="axis"/>
<text x="302.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="388.7" y1="626.0" x2="388.7" y2="631.0" class="axis"/>
<text x="388.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="467.4" y1="626.0" x2="467.4" y2="631.0" class="axis"/>
<text x="467.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="542.2" y1="626.0" x2="542.2" y2="631.0" class="axis"/>
<text x="542.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="628.8" y1="626.0" x2="628.8" y2="631.0" class="axis"/>
<text x="628.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="711.5" y1="626.0" x2="711.5" y2="631.0" class="axis"/>
<text x="711.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="790.2" y1="626.0" x2="790.2" y2="631.0" class="axis"/>
<text x="790.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="872.9" y1="626.0" x2="872.9" y2="631.0" class="axis"/>
<text x="872.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="959.5" y1="626.0" x2="959.5" y2="631.0" class="axis"/>
<text x="959.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1042.2" y1="626.0" x2="1042.2" y2="631.0" class="axis"/>
<text x="1042.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="75.9" x2="1052" y2="75.9" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="78.9" font-size="10.5" fill="var(--muted)">$774 52주 최고</text>
<line x1="680.0" y1="56.0" x2="680.0" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="686.0" y="68.0" font-size="10.5" fill="var(--down)">2026-04-21 Q1 2026 실적</text>
<line x1="924.1" y1="56.0" x2="924.1" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="930.1" y="68.0" font-size="10.5" fill="var(--down)">2026-07-21 Q2 2026 실적·가이던스 상향</text>
<line x1="62.0" y1="423.4" x2="62.0" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="423.9" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="65.9" y1="424.8" x2="65.9" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="425.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="69.8" y1="423.1" x2="69.8" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="68.62" y="423.5" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="73.8" y1="426.1" x2="73.8" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="426.1" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="77.7" y1="425.4" x2="77.7" y2="445.0" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="427.2" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="81.7" y1="416.5" x2="81.7" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="421.6" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="85.6" y1="421.3" x2="85.6" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="422.7" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="89.5" y1="433.3" x2="89.5" y2="443.0" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="436.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="93.5" y1="413.9" x2="93.5" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="428.1" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="97.4" y1="417.9" x2="97.4" y2="433.5" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="428.6" width="2.44" height="3.7" fill="var(--down)"/>
<line x1="101.3" y1="432.4" x2="101.3" y2="448.1" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="438.3" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="105.3" y1="433.9" x2="105.3" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="439.6" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="109.2" y1="431.2" x2="109.2" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="433.9" width="2.44" height="4.5" fill="var(--up)"/>
<line x1="113.1" y1="425.7" x2="113.1" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="432.2" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="117.1" y1="409.6" x2="117.1" y2="432.4" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="415.6" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="121.0" y1="402.1" x2="121.0" y2="422.4" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="408.9" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="125.0" y1="399.9" x2="125.0" y2="414.6" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="400.7" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="128.9" y1="383.3" x2="128.9" y2="406.1" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="393.8" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="132.8" y1="372.4" x2="132.8" y2="403.2" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="373.9" width="2.44" height="29.4" fill="var(--up)"/>
<line x1="136.8" y1="371.1" x2="136.8" y2="385.3" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="377.7" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="140.7" y1="377.6" x2="140.7" y2="387.2" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="381.7" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="144.6" y1="371.5" x2="144.6" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="373.5" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="148.6" y1="355.1" x2="148.6" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="357.2" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="152.5" y1="340.4" x2="152.5" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="151.29" y="349.4" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="156.4" y1="321.0" x2="156.4" y2="344.5" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="322.1" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="160.4" y1="316.8" x2="160.4" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="322.0" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="164.3" y1="327.0" x2="164.3" y2="355.6" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="330.4" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="168.3" y1="347.2" x2="168.3" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="354.6" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="172.2" y1="341.2" x2="172.2" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="342.0" width="2.44" height="13.5" fill="var(--up)"/>
<line x1="176.1" y1="341.8" x2="176.1" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="345.4" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="180.1" y1="369.4" x2="180.1" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="370.9" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="184.0" y1="387.8" x2="184.0" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="396.2" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="187.9" y1="385.5" x2="187.9" y2="397.6" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="387.1" width="2.44" height="4.2" fill="var(--up)"/>
<line x1="191.9" y1="381.9" x2="191.9" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="190.65" y="391.9" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="195.8" y1="380.0" x2="195.8" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="396.1" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="199.7" y1="373.0" x2="199.7" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="380.4" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="203.7" y1="375.4" x2="203.7" y2="396.0" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="379.3" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="207.6" y1="380.5" x2="207.6" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="381.9" width="2.44" height="16.1" fill="var(--down)"/>
<line x1="211.6" y1="392.7" x2="211.6" y2="406.6" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="399.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="215.5" y1="401.2" x2="215.5" y2="422.4" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="408.9" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="219.4" y1="405.7" x2="219.4" y2="431.0" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="416.2" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="223.4" y1="415.0" x2="223.4" y2="434.5" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="420.7" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="227.3" y1="424.8" x2="227.3" y2="442.0" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="426.2" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="231.2" y1="427.7" x2="231.2" y2="447.9" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="432.1" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="235.2" y1="427.8" x2="235.2" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="440.0" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="239.1" y1="430.5" x2="239.1" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="441.5" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="243.0" y1="441.5" x2="243.0" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="441.5" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="247.0" y1="450.4" x2="247.0" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="454.5" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="250.9" y1="443.6" x2="250.9" y2="465.0" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="450.9" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="254.9" y1="446.6" x2="254.9" y2="466.0" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="453.8" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="258.8" y1="457.0" x2="258.8" y2="468.9" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="457.3" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="262.7" y1="459.5" x2="262.7" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="466.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="266.7" y1="457.6" x2="266.7" y2="469.9" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="457.7" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="270.6" y1="439.1" x2="270.6" y2="455.6" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="450.9" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="274.5" y1="450.1" x2="274.5" y2="467.7" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="454.1" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="278.5" y1="439.1" x2="278.5" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="443.5" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="282.4" y1="442.0" x2="282.4" y2="457.6" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="448.2" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="286.3" y1="451.8" x2="286.3" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="453.1" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="290.3" y1="436.9" x2="290.3" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="446.1" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="294.2" y1="422.2" x2="294.2" y2="450.3" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="445.8" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="298.2" y1="438.4" x2="298.2" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="441.0" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="302.1" y1="447.8" x2="302.1" y2="492.7" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="449.2" width="2.44" height="40.2" fill="var(--down)"/>
<line x1="306.0" y1="478.9" x2="306.0" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="486.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="310.0" y1="473.1" x2="310.0" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="475.2" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="313.9" y1="463.1" x2="313.9" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="475.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="317.8" y1="477.1" x2="317.8" y2="491.8" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="478.5" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="321.8" y1="474.7" x2="321.8" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="474.8" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="325.7" y1="467.2" x2="325.7" y2="480.8" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="473.8" width="2.44" height="6.3" fill="var(--down)"/>
<line x1="329.7" y1="465.7" x2="329.7" y2="487.5" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="471.5" width="2.44" height="11.5" fill="var(--up)"/>
<line x1="333.6" y1="447.5" x2="333.6" y2="468.7" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="463.1" width="2.44" height="4.5" fill="var(--up)"/>
<line x1="337.5" y1="442.2" x2="337.5" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="445.5" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="341.5" y1="434.6" x2="341.5" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="434.6" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="345.4" y1="437.4" x2="345.4" y2="452.6" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="438.7" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="349.3" y1="440.9" x2="349.3" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="455.6" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="353.3" y1="445.2" x2="353.3" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="455.9" width="2.44" height="8.1" fill="var(--down)"/>
<line x1="357.2" y1="443.3" x2="357.2" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="447.8" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="361.1" y1="417.4" x2="361.1" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="418.5" width="2.44" height="28.5" fill="var(--up)"/>
<line x1="365.1" y1="416.1" x2="365.1" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="417.4" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="369.0" y1="413.8" x2="369.0" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="422.7" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="373.0" y1="422.0" x2="373.0" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="422.0" width="2.44" height="9.7" fill="var(--down)"/>
<line x1="376.9" y1="425.6" x2="376.9" y2="432.6" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="430.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="380.8" y1="426.7" x2="380.8" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="429.0" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="384.8" y1="432.4" x2="384.8" y2="445.0" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="435.6" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="388.7" y1="416.4" x2="388.7" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="416.7" width="2.44" height="29.1" fill="var(--up)"/>
<line x1="392.6" y1="370.2" x2="392.6" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="370.3" width="2.44" height="31.4" fill="var(--up)"/>
<line x1="396.6" y1="356.0" x2="396.6" y2="378.4" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="364.4" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="400.5" y1="358.2" x2="400.5" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="361.0" width="2.44" height="71.3" fill="var(--down)"/>
<line x1="404.4" y1="320.5" x2="404.4" y2="416.2" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="358.4" width="2.44" height="49.0" fill="var(--down)"/>
<line x1="408.4" y1="355.0" x2="408.4" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="356.7" width="2.44" height="50.9" fill="var(--up)"/>
<line x1="412.3" y1="326.1" x2="412.3" y2="348.5" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="337.7" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="416.3" y1="318.8" x2="416.3" y2="355.2" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="319.9" width="2.44" height="24.7" fill="var(--down)"/>
<line x1="420.2" y1="292.1" x2="420.2" y2="345.8" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="294.6" width="2.44" height="50.9" fill="var(--up)"/>
<line x1="424.1" y1="285.1" x2="424.1" y2="331.1" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="291.9" width="2.44" height="25.8" fill="var(--up)"/>
<line x1="428.1" y1="264.7" x2="428.1" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="269.7" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="432.0" y1="255.5" x2="432.0" y2="294.8" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="271.5" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="435.9" y1="264.8" x2="435.9" y2="291.9" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="274.7" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="439.9" y1="262.1" x2="439.9" y2="282.2" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="263.3" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="443.8" y1="250.9" x2="443.8" y2="266.8" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="256.5" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="447.7" y1="261.5" x2="447.7" y2="283.8" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="264.1" width="2.44" height="16.3" fill="var(--down)"/>
<line x1="451.7" y1="240.6" x2="451.7" y2="325.6" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="248.3" width="2.44" height="52.6" fill="var(--up)"/>
<line x1="455.6" y1="226.6" x2="455.6" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="229.5" width="2.44" height="26.5" fill="var(--up)"/>
<line x1="459.6" y1="199.9" x2="459.6" y2="235.1" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="218.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="463.5" y1="214.0" x2="463.5" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="223.8" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="467.4" y1="227.1" x2="467.4" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="236.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="471.4" y1="195.9" x2="471.4" y2="236.0" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="200.8" width="2.44" height="19.5" fill="var(--up)"/>
<line x1="475.3" y1="192.8" x2="475.3" y2="250.7" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="199.4" width="2.44" height="29.0" fill="var(--down)"/>
<line x1="479.2" y1="202.2" x2="479.2" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="216.1" width="2.44" height="29.4" fill="var(--up)"/>
<line x1="483.2" y1="188.3" x2="483.2" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="193.3" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="487.1" y1="181.6" x2="487.1" y2="213.4" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="187.8" width="2.44" height="25.6" fill="var(--down)"/>
<line x1="491.0" y1="205.6" x2="491.0" y2="238.1" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="205.6" width="2.44" height="31.3" fill="var(--down)"/>
<line x1="495.0" y1="231.3" x2="495.0" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="241.8" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="498.9" y1="215.7" x2="498.9" y2="246.1" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="218.7" width="2.44" height="25.9" fill="var(--up)"/>
<line x1="502.9" y1="193.5" x2="502.9" y2="216.6" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="205.2" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="506.8" y1="195.3" x2="506.8" y2="212.1" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="205.2" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="510.7" y1="163.6" x2="510.7" y2="205.3" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="164.9" width="2.44" height="26.9" fill="var(--up)"/>
<line x1="514.7" y1="127.4" x2="514.7" y2="160.5" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="143.1" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="518.6" y1="141.5" x2="518.6" y2="177.2" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="146.5" width="2.44" height="20.7" fill="var(--down)"/>
<line x1="522.5" y1="152.9" x2="522.5" y2="174.7" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="163.9" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="526.5" y1="147.2" x2="526.5" y2="190.9" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="159.6" width="2.44" height="2.1" fill="var(--up)"/>
<line x1="530.4" y1="158.2" x2="530.4" y2="226.0" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="160.2" width="2.44" height="43.0" fill="var(--down)"/>
<line x1="534.3" y1="184.8" x2="534.3" y2="209.5" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="190.1" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="538.3" y1="160.4" x2="538.3" y2="183.0" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="165.7" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="542.2" y1="86.4" x2="542.2" y2="137.8" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="86.7" width="2.44" height="41.7" fill="var(--up)"/>
<line x1="546.2" y1="75.9" x2="546.2" y2="115.9" stroke="var(--down)" class="wick"/>
<rect x="544.94" y="85.2" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="550.1" y1="104.4" x2="550.1" y2="141.5" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="105.8" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="554.0" y1="115.8" x2="554.0" y2="147.6" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="120.0" width="2.44" height="17.4" fill="var(--down)"/>
<line x1="558.0" y1="103.6" x2="558.0" y2="141.0" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="108.2" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="561.9" y1="91.1" x2="561.9" y2="129.2" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="95.8" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="565.8" y1="128.4" x2="565.8" y2="155.2" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="141.0" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="569.8" y1="133.6" x2="569.8" y2="158.1" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="149.8" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="573.7" y1="126.2" x2="573.7" y2="161.7" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="143.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="577.7" y1="125.0" x2="577.7" y2="158.5" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="137.5" width="2.44" height="11.3" fill="var(--down)"/>
<line x1="581.6" y1="142.1" x2="581.6" y2="162.5" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="144.7" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="585.5" y1="143.1" x2="585.5" y2="172.2" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="147.5" width="2.44" height="18.8" fill="var(--down)"/>
<line x1="589.5" y1="153.4" x2="589.5" y2="173.6" stroke="var(--down)" class="wick"/>
<rect x="588.24" y="155.5" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="593.4" y1="159.1" x2="593.4" y2="197.1" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="175.3" width="2.44" height="8.9" fill="var(--down)"/>
<line x1="597.3" y1="178.4" x2="597.3" y2="208.0" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="183.2" width="2.44" height="14.1" fill="var(--down)"/>
<line x1="601.3" y1="197.6" x2="601.3" y2="248.3" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="199.2" width="2.44" height="46.8" fill="var(--down)"/>
<line x1="605.2" y1="229.2" x2="605.2" y2="267.4" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="242.1" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="609.1" y1="222.9" x2="609.1" y2="242.7" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="225.7" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="613.1" y1="215.4" x2="613.1" y2="232.5" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="224.3" width="2.44" height="4.2" fill="var(--up)"/>
<line x1="617.0" y1="220.9" x2="617.0" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="223.8" width="2.44" height="24.0" fill="var(--down)"/>
<line x1="621.0" y1="222.5" x2="621.0" y2="275.1" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="229.6" width="2.44" height="31.6" fill="var(--down)"/>
<line x1="624.9" y1="236.0" x2="624.9" y2="269.0" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="241.9" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="628.8" y1="205.9" x2="628.8" y2="237.4" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="215.2" width="2.44" height="13.9" fill="var(--up)"/>
<line x1="632.8" y1="194.3" x2="632.8" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="205.3" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="636.7" y1="204.3" x2="636.7" y2="231.6" stroke="var(--down)" class="wick"/>
<rect x="635.48" y="208.0" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="640.6" y1="215.6" x2="640.6" y2="234.4" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="227.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="644.6" y1="226.5" x2="644.6" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="232.5" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="648.5" y1="212.5" x2="648.5" y2="237.0" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="226.9" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="652.4" y1="233.3" x2="652.4" y2="273.1" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="236.3" width="2.44" height="21.0" fill="var(--down)"/>
<line x1="656.4" y1="239.0" x2="656.4" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="243.6" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="660.3" y1="243.0" x2="660.3" y2="255.9" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="245.8" width="2.44" height="3.0" fill="var(--up)"/>
<line x1="664.3" y1="240.8" x2="664.3" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="244.8" width="2.44" height="3.7" fill="var(--down)"/>
<line x1="668.2" y1="245.3" x2="668.2" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="247.6" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="672.1" y1="250.1" x2="672.1" y2="276.7" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="262.2" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="676.1" y1="258.1" x2="676.1" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="269.5" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="680.0" y1="294.9" x2="680.0" y2="372.0" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="318.4" width="2.44" height="52.2" fill="var(--down)"/>
<line x1="683.9" y1="363.6" x2="683.9" y2="420.6" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="370.7" width="2.44" height="38.9" fill="var(--down)"/>
<line x1="687.9" y1="397.1" x2="687.9" y2="421.1" stroke="var(--down)" class="wick"/>
<rect x="686.65" y="404.2" width="2.44" height="8.9" fill="var(--down)"/>
<line x1="691.8" y1="421.9" x2="691.8" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="422.8" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="695.7" y1="412.0" x2="695.7" y2="445.8" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="432.4" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="699.7" y1="421.5" x2="699.7" y2="443.9" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="423.4" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="703.6" y1="423.1" x2="703.6" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="702.40" y="430.6" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="707.6" y1="425.6" x2="707.6" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="427.9" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="711.5" y1="425.4" x2="711.5" y2="448.5" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="429.2" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="715.4" y1="431.5" x2="715.4" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="449.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="719.4" y1="444.1" x2="719.4" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="445.0" width="2.44" height="20.7" fill="var(--down)"/>
<line x1="723.3" y1="462.0" x2="723.3" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="463.9" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="727.2" y1="460.8" x2="727.2" y2="484.3" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="464.5" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="731.2" y1="472.1" x2="731.2" y2="491.7" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="472.2" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="735.1" y1="473.5" x2="735.1" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="484.5" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="739.0" y1="464.1" x2="739.0" y2="487.4" stroke="var(--up)" class="wick"/>
<rect x="737.83" y="466.2" width="2.44" height="15.0" fill="var(--up)"/>
<line x1="743.0" y1="473.4" x2="743.0" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="473.4" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="746.9" y1="470.4" x2="746.9" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="474.8" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="750.9" y1="476.2" x2="750.9" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="483.6" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="754.8" y1="476.3" x2="754.8" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="481.2" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="758.7" y1="468.4" x2="758.7" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="757.51" y="469.8" width="2.44" height="6.1" fill="var(--up)"/>
<line x1="762.7" y1="470.3" x2="762.7" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="470.3" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="766.6" y1="470.5" x2="766.6" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="474.7" width="2.44" height="3.7" fill="var(--down)"/>
<line x1="770.5" y1="467.3" x2="770.5" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="471.1" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="774.5" y1="465.0" x2="774.5" y2="480.6" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="467.3" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="778.4" y1="471.3" x2="778.4" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="477.0" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="782.3" y1="462.1" x2="782.3" y2="478.8" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="464.4" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="786.3" y1="456.0" x2="786.3" y2="479.4" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="456.5" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="790.2" y1="463.3" x2="790.2" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="463.3" width="2.44" height="37.5" fill="var(--down)"/>
<line x1="794.2" y1="502.2" x2="794.2" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="505.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="798.1" y1="502.2" x2="798.1" y2="525.2" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="511.0" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="802.0" y1="489.5" x2="802.0" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="490.0" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="806.0" y1="477.7" x2="806.0" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="481.2" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="809.9" y1="486.9" x2="809.9" y2="514.7" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="495.7" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="813.8" y1="483.5" x2="813.8" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="483.6" width="2.44" height="18.7" fill="var(--up)"/>
<line x1="817.8" y1="476.0" x2="817.8" y2="497.5" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="476.0" width="2.44" height="19.5" fill="var(--down)"/>
<line x1="821.7" y1="463.7" x2="821.7" y2="496.8" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="476.7" width="2.44" height="15.7" fill="var(--up)"/>
<line x1="825.7" y1="473.9" x2="825.7" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="475.8" width="2.44" height="4.8" fill="var(--down)"/>
<line x1="829.6" y1="488.3" x2="829.6" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="490.8" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="833.5" y1="473.6" x2="833.5" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="479.0" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="837.5" y1="465.3" x2="837.5" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="481.0" width="2.44" height="2.1" fill="var(--up)"/>
<line x1="841.4" y1="474.9" x2="841.4" y2="543.9" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="477.4" width="2.44" height="55.4" fill="var(--down)"/>
<line x1="845.3" y1="542.6" x2="845.3" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="543.5" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="849.3" y1="536.2" x2="849.3" y2="554.6" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="537.2" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="853.2" y1="540.7" x2="853.2" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="544.3" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="857.1" y1="549.2" x2="857.1" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="569.9" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="861.1" y1="558.5" x2="861.1" y2="575.1" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="568.5" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="865.0" y1="564.8" x2="865.0" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="568.1" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="869.0" y1="554.4" x2="869.0" y2="580.6" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="554.9" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="872.9" y1="525.9" x2="872.9" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="535.6" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="876.8" y1="483.0" x2="876.8" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="483.0" width="2.44" height="38.2" fill="var(--up)"/>
<line x1="880.8" y1="483.9" x2="880.8" y2="504.1" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="485.3" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="884.7" y1="476.5" x2="884.7" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="479.4" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="888.6" y1="484.6" x2="888.6" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="488.4" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="892.6" y1="500.0" x2="892.6" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="503.8" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="896.5" y1="497.4" x2="896.5" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="500.0" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="900.4" y1="489.3" x2="900.4" y2="505.0" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="496.0" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="904.4" y1="491.9" x2="904.4" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="505.0" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="908.3" y1="506.7" x2="908.3" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="514.0" width="2.44" height="12.1" fill="var(--down)"/>
<line x1="912.3" y1="518.4" x2="912.3" y2="540.7" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="525.0" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="916.2" y1="501.2" x2="916.2" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="526.3" width="2.44" height="6.3" fill="var(--down)"/>
<line x1="920.1" y1="511.9" x2="920.1" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="528.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="924.1" y1="546.1" x2="924.1" y2="609.7" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="549.5" width="2.44" height="40.3" fill="var(--up)"/>
<line x1="928.0" y1="507.2" x2="928.0" y2="538.3" stroke="var(--up)" class="wick"/>
<rect x="926.78" y="526.0" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="931.9" y1="487.1" x2="931.9" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="504.4" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="935.9" y1="490.9" x2="935.9" y2="509.4" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="495.3" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="939.8" y1="477.6" x2="939.8" y2="495.3" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="485.6" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="943.7" y1="453.3" x2="943.7" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="466.8" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="947.7" y1="472.3" x2="947.7" y2="509.8" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="473.4" width="2.44" height="34.9" fill="var(--down)"/>
<line x1="951.6" y1="508.3" x2="951.6" y2="535.9" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="508.7" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="955.6" y1="489.9" x2="955.6" y2="517.3" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="494.8" width="2.44" height="13.8" fill="var(--up)"/>
<line x1="959.5" y1="467.5" x2="959.5" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="484.0" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="963.4" y1="472.2" x2="963.4" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="478.4" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="967.4" y1="467.5" x2="967.4" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="467.7" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="971.3" y1="447.4" x2="971.3" y2="465.0" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="449.1" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="975.2" y1="440.1" x2="975.2" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="442.2" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="979.2" y1="424.1" x2="979.2" y2="439.4" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="430.8" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="983.1" y1="425.6" x2="983.1" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="434.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="987.0" y1="426.9" x2="987.0" y2="445.9" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="431.8" width="2.44" height="11.3" fill="var(--up)"/>
<line x1="991.0" y1="427.1" x2="991.0" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="429.3" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="994.9" y1="415.4" x2="994.9" y2="437.0" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="416.3" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="998.9" y1="418.0" x2="998.9" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="423.6" width="2.44" height="21.1" fill="var(--down)"/>
<line x1="1002.8" y1="400.7" x2="1002.8" y2="433.8" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="410.4" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="1006.7" y1="406.1" x2="1006.7" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="420.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1010.7" y1="416.1" x2="1010.7" y2="456.9" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="425.6" width="2.44" height="30.5" fill="var(--down)"/>
<line x1="1014.6" y1="449.6" x2="1014.6" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="452.0" width="2.44" height="27.3" fill="var(--down)"/>
<line x1="1018.5" y1="475.8" x2="1018.5" y2="487.6" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="475.8" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="1022.5" y1="481.6" x2="1022.5" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="485.2" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="1026.4" y1="474.7" x2="1026.4" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="481.3" width="2.44" height="12.4" fill="var(--up)"/>
<line x1="1030.3" y1="484.3" x2="1030.3" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="486.6" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="1034.3" y1="485.4" x2="1034.3" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="486.0" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="1038.2" y1="497.0" x2="1038.2" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="499.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1042.2" y1="481.7" x2="1042.2" y2="517.2" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="493.7" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="1046.1" y1="506.8" x2="1046.1" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="508.7" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="1050.0" y1="508.9" x2="1050.0" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="518.9" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="60" y1="462.4" x2="1052" y2="462.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="465.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$560 R1</text>
<text x="1058" y="477.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="412.6" x2="1052" y2="412.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$588 R2</text>
<text x="1058" y="428.1" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="188.0" x2="1052" y2="188.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="191.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$712 R3</text>
<text x="1058" y="203.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="530.5" x2="1052" y2="530.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="524.5" font-size="11.5" fill="var(--support)" font-weight="600">$523 S1</text>
<text x="1058" y="536.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="609.7" x2="1052" y2="609.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="603.7" font-size="11.5" fill="var(--support)" font-weight="600">$479 S2 52주 최저</text>
<text x="1058" y="615.7" font-size="9.5" fill="var(--muted)">터치 1회</text>
<circle cx="1052.0" cy="520.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="512.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $528 (2026-09-03)</text>
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
| R3 | $712 | 2 | 2026-02-09·2026-04-02 — 2026년 3월 고점($768) 직전과 4월 급락 직전의 스윙 고점대 |
| R2 | $588 | 4 | 2025-09-16·2025-11-26·2025-12-24·2026-08-18 — 2025년 하반기 상승 구간의 중간대이자 2026년 8월 반등의 상단 |
| R1 | $560 | 4 | 2026-05-29·2026-06-11·2026-07-07·2026-07-28 — 4월 급락 이후 여름 반등의 상단 |
| **현재가** | **$528.24** (2026-09-03 종가) | — | R1과 S1 사이 |
| S1 | $523 | 2 | 2026-06-03·2026-07-30 — 6월 급락기와 7월 실적 직후의 저점대. 현재가 바로 아래 |
| S2 52주 최저 | $479 | 1 | **강제 포함** — 2026-06-29 전후의 장중 52주 최저. 터치 1회라 클러스터 기준(2회)에 미달하지만 하방 참조점이라 포함(§4 참고) |
| 참고선 | $774 | — | 52주 최고(2026-03-02 전후 장중 $774.00). 이후 −31% 하락하며 거래 레짐이 바뀌어 근시일 저항으로 보지 않는다 |

현재가 $528.24는 **S1($523)에 바로 붙어 있고 R1($560)까지 6.0% 남은 자리**다. 위쪽으로는 R1·R2·R3가 촘촘하지만 아래쪽은 S1 다음이 52주 최저($479)까지 비어 있어, **레벨 구조만 보면 상단이 두껍고 하단이 얇은 배치**다.

---

## 3. 관측된 특이 구간

이 1년 구간에는 가격대를 다시 잡은 사건이 둘 있다.

**① 2026-04-21 — 2026 Q1 실적 발표**

- 매출·EPS는 컨센서스를 웃돌았으나 FY2026 CapEx를 $1.85B로 상향하고 가이던스는 유지하는 데 그쳤다([최근 뉴스 / 이슈](./08_news.md) 로그).
- 종가 기준 전일 대비 **−6.98%** ($656.98 → $611.13), 거래량은 평소(일 84.9만 주 내외) 대비 약 **1.9배**인 **160만 주**. 다음 거래일에도 −3.5%가 이어졌다.
- 이 갭 이후 주가는 $600선을 회복하지 못했다. **R3($712)를 근시일 저항이 아니라 이전 레짐의 잔재로 읽어야 하는 이유**가 이 구간이다.

**② 2026-06-18 — 지정학 프리미엄 축소에 따른 섹터 동반 하락**

- 종가 기준 전일 대비 **−5.21%** ($550.15 → $521.50), 거래량 **240만 주**로 평소의 약 **2.8배**. 이후 6영업일간 추가로 밀려 2026-06-29에 종가 $496.02(52주 최저권)를 찍었다.
- 회사 고유 사건이 아니라 방산 섹터 전반의 위험 프리미엄이 축소된 결과로 전해진다(2차 출처 기반). 이 구간을 지나며 **S1($523)·52주 최저($479)라는 현재의 하단 구조가 만들어졌다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-04~2026-09-03. 수집 시점: 2026-09-04. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py NOC --name "노스롭 그루먼" --close-on 2026-09-03 --event 2026-04-21:"Q1 2026 실적" --event 2026-07-21:"Q2 2026 실적·가이던스 상향" --ref-line 774:"52주 최고" --force-level 479:"52주 최저" --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **S2($479)는 `--force-level`로 강제 포함한 레벨이다** — 터치 1회로 클러스터 기준(2회)에 미달한다. 지지대로서의 강도가 아니라 "1년 내 최저가가 어디였는가"라는 참조점으로만 읽을 것.
    - 위 3절의 두 갭(−6.98%, −5.21%)으로 가격 연속성이 두 번 끊겼다. **R2·R3는 갭 이전 레짐에서 형성된 레벨**이라 현재 구간의 저항으로 그대로 대입하기 어렵다.
    - 기간 중 주식분할·유상증자는 없었다. 분기배당 4회가 있었으나 원주가 기준이라 반영하지 않았다.

---

*작성일: 2026-09-04*
