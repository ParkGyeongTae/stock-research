# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL·10-Q)와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-04 종가 $292.70은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치**한다(스크립트 `--close-on` 출력으로 확인).

---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="cdns-chart">
<style>
.cdns-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cdns-chart svg { width:100%; height:auto; display:block; }
.cdns-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cdns-chart .title { fill: var(--ink); font-weight:600; }
.cdns-chart .grid { stroke: var(--grid); stroke-width:1; }
.cdns-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cadence(CDNS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cadence (CDNS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $292.70 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="565.5" x2="1052" y2="565.5" class="grid"/>
<text x="52" y="569.5" font-size="11" text-anchor="end" fill="var(--muted)">275</text>
<line x1="60" y1="479.2" x2="1052" y2="479.2" class="grid"/>
<text x="52" y="483.2" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="392.8" x2="1052" y2="392.8" class="grid"/>
<text x="52" y="396.8" font-size="11" text-anchor="end" fill="var(--muted)">325</text>
<line x1="60" y1="306.5" x2="1052" y2="306.5" class="grid"/>
<text x="52" y="310.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="220.1" x2="1052" y2="220.1" class="grid"/>
<text x="52" y="224.1" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="133.7" x2="1052" y2="133.7" class="grid"/>
<text x="52" y="137.7" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="60" y1="76.1" x2="1052" y2="76.1" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="79.1" font-size="10.5" fill="var(--muted)">$417 52주 최고</text>
<line x1="786.3" y1="56.0" x2="786.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="792.3" y="68.0" font-size="10.5" fill="var(--down)">2026-06-01 ChipStack 발표 급등</text>
<line x1="912.3" y1="56.0" x2="912.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="918.3" y="68.0" font-size="10.5" fill="var(--down)">2026-07-17 AI 모델 우려 급락</text>
<line x1="935.9" y1="56.0" x2="935.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="941.9" y="68.0" font-size="10.5" fill="var(--down)">2026-07-27 2Q26 실적·가이던스 상향</text>
<line x1="62.0" y1="288.1" x2="62.0" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="296.0" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="65.9" y1="267.2" x2="65.9" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="269.7" width="2.44" height="24.1" fill="var(--up)"/>
<line x1="69.8" y1="262.5" x2="69.8" y2="284.3" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="265.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="73.8" y1="311.5" x2="73.8" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="311.6" width="2.44" height="34.4" fill="var(--down)"/>
<line x1="77.7" y1="279.6" x2="77.7" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="290.2" width="2.44" height="42.6" fill="var(--up)"/>
<line x1="81.7" y1="288.9" x2="81.7" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="294.5" width="2.44" height="34.5" fill="var(--down)"/>
<line x1="85.6" y1="299.5" x2="85.6" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="301.2" width="2.44" height="28.8" fill="var(--up)"/>
<line x1="89.5" y1="297.6" x2="89.5" y2="313.5" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="305.9" width="2.44" height="4.0" fill="var(--down)"/>
<line x1="93.5" y1="306.9" x2="93.5" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="306.9" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="97.4" y1="251.0" x2="97.4" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="255.1" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="101.3" y1="222.5" x2="101.3" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="225.8" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="105.3" y1="223.9" x2="105.3" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="225.7" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="109.2" y1="231.0" x2="109.2" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="107.99" y="234.0" width="2.44" height="16.2" fill="var(--down)"/>
<line x1="113.1" y1="248.7" x2="113.1" y2="286.4" stroke="var(--down)" class="wick"/>
<rect x="111.92" y="248.7" width="2.44" height="33.7" fill="var(--down)"/>
<line x1="117.1" y1="289.1" x2="117.1" y2="306.4" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="297.7" width="2.44" height="5.0" fill="var(--down)"/>
<line x1="121.0" y1="302.7" x2="121.0" y2="316.9" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="306.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="125.0" y1="296.5" x2="125.0" y2="314.0" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="296.5" width="2.44" height="15.1" fill="var(--down)"/>
<line x1="128.9" y1="299.4" x2="128.9" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="302.1" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="132.8" y1="288.7" x2="132.8" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="299.6" width="2.44" height="12.8" fill="var(--up)"/>
<line x1="136.8" y1="288.7" x2="136.8" y2="319.1" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="290.7" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="140.7" y1="295.6" x2="140.7" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="315.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="144.6" y1="289.7" x2="144.6" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="294.8" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="148.6" y1="295.0" x2="148.6" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="297.1" width="2.44" height="24.9" fill="var(--down)"/>
<line x1="152.5" y1="291.7" x2="152.5" y2="320.0" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="306.5" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="156.4" y1="310.7" x2="156.4" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="311.0" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="160.4" y1="305.6" x2="160.4" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="313.0" width="2.44" height="72.9" fill="var(--down)"/>
<line x1="164.3" y1="361.0" x2="164.3" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="367.8" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="168.3" y1="376.1" x2="168.3" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="390.2" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="172.2" y1="373.3" x2="172.2" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="373.3" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="176.1" y1="385.7" x2="176.1" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="388.7" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="180.1" y1="381.7" x2="180.1" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="388.9" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="184.0" y1="371.7" x2="184.0" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="376.8" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="187.9" y1="357.9" x2="187.9" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="363.6" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="191.9" y1="353.1" x2="191.9" y2="388.8" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="363.7" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="195.8" y1="347.3" x2="195.8" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="350.4" width="2.44" height="27.5" fill="var(--up)"/>
<line x1="199.7" y1="302.6" x2="199.7" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="323.4" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="203.7" y1="280.4" x2="203.7" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="280.4" width="2.44" height="21.2" fill="var(--down)"/>
<line x1="207.6" y1="313.1" x2="207.6" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="336.5" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="211.6" y1="316.8" x2="211.6" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="336.1" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="215.5" y1="333.4" x2="215.5" y2="363.8" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="341.0" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="219.4" y1="338.5" x2="219.4" y2="354.1" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="345.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="223.4" y1="335.1" x2="223.4" y2="372.1" stroke="var(--down)" class="wick"/>
<rect x="222.14" y="335.1" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="227.3" y1="354.6" x2="227.3" y2="390.8" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="364.4" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="231.2" y1="366.7" x2="231.2" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="368.8" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="235.2" y1="385.0" x2="235.2" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="393.0" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="239.1" y1="387.3" x2="239.1" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="392.6" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="243.0" y1="372.6" x2="243.0" y2="398.6" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="379.2" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="247.0" y1="386.6" x2="247.0" y2="423.1" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="387.5" width="2.44" height="27.7" fill="var(--down)"/>
<line x1="250.9" y1="404.5" x2="250.9" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="406.9" width="2.44" height="18.6" fill="var(--down)"/>
<line x1="254.9" y1="418.8" x2="254.9" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="423.9" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="258.8" y1="411.3" x2="258.8" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="427.6" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="262.7" y1="424.5" x2="262.7" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="432.4" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="266.7" y1="443.5" x2="266.7" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="265.45" y="452.5" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="270.6" y1="444.2" x2="270.6" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="455.8" width="2.44" height="8.8" fill="var(--up)"/>
<line x1="274.5" y1="421.5" x2="274.5" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="437.2" width="2.44" height="34.6" fill="var(--down)"/>
<line x1="278.5" y1="465.7" x2="278.5" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="472.5" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="282.4" y1="459.4" x2="282.4" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="463.7" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="286.3" y1="459.3" x2="286.3" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="466.5" width="2.44" height="10.1" fill="var(--up)"/>
<line x1="290.3" y1="450.9" x2="290.3" y2="465.3" stroke="var(--down)" class="wick"/>
<rect x="289.07" y="454.8" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="294.2" y1="437.9" x2="294.2" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="438.3" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="298.2" y1="434.1" x2="298.2" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="435.5" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="302.1" y1="413.3" x2="302.1" y2="440.4" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="417.2" width="2.44" height="22.2" fill="var(--up)"/>
<line x1="306.0" y1="347.9" x2="306.0" y2="425.0" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="354.4" width="2.44" height="70.2" fill="var(--up)"/>
<line x1="310.0" y1="342.4" x2="310.0" y2="360.6" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="350.3" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="313.9" y1="337.4" x2="313.9" y2="354.3" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="346.4" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="317.8" y1="338.1" x2="317.8" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="347.9" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="321.8" y1="347.8" x2="321.8" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="353.9" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="325.7" y1="336.5" x2="325.7" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="347.7" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="329.7" y1="347.9" x2="329.7" y2="377.8" stroke="var(--down)" class="wick"/>
<rect x="328.43" y="348.1" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="333.6" y1="357.4" x2="333.6" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="359.6" width="2.44" height="39.4" fill="var(--down)"/>
<line x1="337.5" y1="383.2" x2="337.5" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="396.0" width="2.44" height="19.5" fill="var(--down)"/>
<line x1="341.5" y1="399.7" x2="341.5" y2="422.5" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="411.7" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="345.4" y1="410.5" x2="345.4" y2="441.4" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="413.5" width="2.44" height="20.7" fill="var(--down)"/>
<line x1="349.3" y1="401.8" x2="349.3" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="348.11" y="415.7" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="353.3" y1="412.6" x2="353.3" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="427.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="415.8" x2="357.2" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="418.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="361.1" y1="419.1" x2="361.1" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="420.7" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="365.1" y1="416.6" x2="365.1" y2="426.1" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="417.8" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="369.0" y1="412.5" x2="369.0" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="413.9" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="373.0" y1="404.3" x2="373.0" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="417.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="376.9" y1="413.5" x2="376.9" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="421.0" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="380.8" y1="423.9" x2="380.8" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="424.7" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="384.8" y1="423.9" x2="384.8" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="424.9" width="2.44" height="18.3" fill="var(--down)"/>
<line x1="388.7" y1="430.2" x2="388.7" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="439.6" width="2.44" height="35.4" fill="var(--down)"/>
<line x1="392.6" y1="423.8" x2="392.6" y2="476.1" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="428.6" width="2.44" height="45.4" fill="var(--up)"/>
<line x1="396.6" y1="393.8" x2="396.6" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="408.2" width="2.44" height="21.2" fill="var(--up)"/>
<line x1="400.5" y1="412.0" x2="400.5" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="414.2" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="404.4" y1="380.4" x2="404.4" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="403.22" y="384.8" width="2.44" height="25.6" fill="var(--up)"/>
<line x1="408.4" y1="380.7" x2="408.4" y2="406.6" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="389.8" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="412.3" y1="383.6" x2="412.3" y2="417.0" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="399.5" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="416.3" y1="408.3" x2="416.3" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="411.8" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="420.2" y1="380.2" x2="420.2" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="408.0" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="424.1" y1="401.6" x2="424.1" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="403.8" width="2.44" height="15.1" fill="var(--down)"/>
<line x1="428.1" y1="439.6" x2="428.1" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="442.7" width="2.44" height="12.3" fill="var(--down)"/>
<line x1="432.0" y1="423.4" x2="432.0" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="431.4" width="2.44" height="21.8" fill="var(--up)"/>
<line x1="435.9" y1="417.6" x2="435.9" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="420.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="439.9" y1="397.9" x2="439.9" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="415.9" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="443.8" y1="397.6" x2="443.8" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="403.1" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="447.7" y1="399.7" x2="447.7" y2="419.7" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="404.2" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="451.7" y1="392.2" x2="451.7" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="404.5" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="455.6" y1="420.5" x2="455.6" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="421.8" width="2.44" height="48.2" fill="var(--down)"/>
<line x1="459.6" y1="483.1" x2="459.6" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="484.5" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="463.5" y1="491.8" x2="463.5" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="496.1" width="2.44" height="20.4" fill="var(--down)"/>
<line x1="467.4" y1="527.6" x2="467.4" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="535.0" width="2.44" height="53.0" fill="var(--down)"/>
<line x1="471.4" y1="564.5" x2="471.4" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="577.9" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="475.3" y1="560.7" x2="475.3" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="577.0" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="479.2" y1="529.8" x2="479.2" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="536.1" width="2.44" height="25.4" fill="var(--up)"/>
<line x1="483.2" y1="507.6" x2="483.2" y2="549.8" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="510.3" width="2.44" height="25.9" fill="var(--up)"/>
<line x1="487.1" y1="475.5" x2="487.1" y2="503.4" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="482.6" width="2.44" height="16.7" fill="var(--up)"/>
<line x1="491.0" y1="471.4" x2="491.0" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="475.1" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="495.0" y1="470.3" x2="495.0" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="483.6" width="2.44" height="35.9" fill="var(--down)"/>
<line x1="498.9" y1="476.7" x2="498.9" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="481.0" width="2.44" height="41.5" fill="var(--up)"/>
<line x1="502.9" y1="492.3" x2="502.9" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="497.2" width="2.44" height="39.1" fill="var(--down)"/>
<line x1="506.8" y1="438.8" x2="506.8" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="461.9" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="510.7" y1="450.4" x2="510.7" y2="506.3" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="450.4" width="2.44" height="40.6" fill="var(--down)"/>
<line x1="514.7" y1="467.3" x2="514.7" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="492.0" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="518.6" y1="501.3" x2="518.6" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="508.8" width="2.44" height="40.2" fill="var(--down)"/>
<line x1="522.5" y1="500.4" x2="522.5" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="511.6" width="2.44" height="44.3" fill="var(--up)"/>
<line x1="526.5" y1="469.6" x2="526.5" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="472.8" width="2.44" height="25.4" fill="var(--up)"/>
<line x1="530.4" y1="458.6" x2="530.4" y2="503.7" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="461.9" width="2.44" height="25.5" fill="var(--down)"/>
<line x1="534.3" y1="472.6" x2="534.3" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="474.3" width="2.44" height="43.7" fill="var(--up)"/>
<line x1="538.3" y1="462.7" x2="538.3" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="467.6" width="2.44" height="19.3" fill="var(--up)"/>
<line x1="542.2" y1="463.7" x2="542.2" y2="494.7" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="477.0" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="546.2" y1="449.5" x2="546.2" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="460.4" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="550.1" y1="440.4" x2="550.1" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="468.8" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="554.0" y1="472.2" x2="554.0" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="489.8" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="558.0" y1="478.2" x2="558.0" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="485.9" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="561.9" y1="482.4" x2="561.9" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="482.4" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="565.8" y1="493.0" x2="565.8" y2="524.1" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="497.2" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="569.8" y1="491.2" x2="569.8" y2="516.5" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="510.5" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="573.7" y1="506.7" x2="573.7" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="511.0" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="577.7" y1="495.0" x2="577.7" y2="520.6" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="504.3" width="2.44" height="11.7" fill="var(--up)"/>
<line x1="581.6" y1="475.9" x2="581.6" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="500.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="585.5" y1="495.4" x2="585.5" y2="515.5" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="507.1" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="589.5" y1="504.7" x2="589.5" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="588.24" y="517.5" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="593.4" y1="522.7" x2="593.4" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="526.1" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="597.3" y1="481.6" x2="597.3" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="505.0" width="2.44" height="11.5" fill="var(--up)"/>
<line x1="601.3" y1="512.0" x2="601.3" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="515.4" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="605.2" y1="512.4" x2="605.2" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="518.3" width="2.44" height="25.2" fill="var(--down)"/>
<line x1="609.1" y1="533.9" x2="609.1" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="546.1" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="613.1" y1="546.8" x2="613.1" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="554.3" width="2.44" height="22.4" fill="var(--down)"/>
<line x1="617.0" y1="560.8" x2="617.0" y2="587.0" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="575.3" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="621.0" y1="553.1" x2="621.0" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="619.73" y="555.6" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="624.9" y1="542.7" x2="624.9" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="547.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="628.8" y1="547.4" x2="628.8" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="552.7" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="632.8" y1="549.1" x2="632.8" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="550.4" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="636.7" y1="548.3" x2="636.7" y2="569.3" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="550.1" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="640.6" y1="509.1" x2="640.6" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="513.8" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="644.6" y1="520.0" x2="644.6" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="521.9" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="648.5" y1="543.4" x2="648.5" y2="605.7" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="545.8" width="2.44" height="52.1" fill="var(--down)"/>
<line x1="652.4" y1="519.5" x2="652.4" y2="599.3" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="519.9" width="2.44" height="76.5" fill="var(--up)"/>
<line x1="656.4" y1="488.9" x2="656.4" y2="512.8" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="502.3" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="660.3" y1="453.4" x2="660.3" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="465.0" width="2.44" height="31.4" fill="var(--up)"/>
<line x1="664.3" y1="434.7" x2="664.3" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="446.5" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="668.2" y1="417.0" x2="668.2" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="422.8" width="2.44" height="18.3" fill="var(--down)"/>
<line x1="672.1" y1="406.7" x2="672.1" y2="446.0" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="415.3" width="2.44" height="20.4" fill="var(--up)"/>
<line x1="676.1" y1="371.3" x2="676.1" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="389.9" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="680.0" y1="361.7" x2="680.0" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="365.7" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="683.9" y1="386.0" x2="683.9" y2="441.2" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="389.8" width="2.44" height="39.8" fill="var(--down)"/>
<line x1="687.9" y1="358.9" x2="687.9" y2="412.3" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="365.6" width="2.44" height="44.3" fill="var(--up)"/>
<line x1="691.8" y1="347.3" x2="691.8" y2="375.5" stroke="var(--up)" class="wick"/>
<rect x="690.59" y="353.0" width="2.44" height="19.8" fill="var(--up)"/>
<line x1="695.7" y1="346.0" x2="695.7" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="376.6" width="2.44" height="15.2" fill="var(--down)"/>
<line x1="699.7" y1="370.8" x2="699.7" y2="425.6" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="375.7" width="2.44" height="21.6" fill="var(--up)"/>
<line x1="703.6" y1="375.3" x2="703.6" y2="410.9" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="377.0" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="707.6" y1="332.8" x2="707.6" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="337.8" width="2.44" height="15.3" fill="var(--up)"/>
<line x1="711.5" y1="303.0" x2="711.5" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="308.1" width="2.44" height="24.6" fill="var(--up)"/>
<line x1="715.4" y1="289.6" x2="715.4" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="293.9" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="719.4" y1="287.5" x2="719.4" y2="315.1" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="289.5" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="723.3" y1="262.5" x2="723.3" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="722.08" y="278.8" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="727.2" y1="254.6" x2="727.2" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="262.6" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="731.2" y1="254.6" x2="731.2" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="729.95" y="257.4" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="735.1" y1="265.0" x2="735.1" y2="287.2" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="268.1" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="739.0" y1="268.4" x2="739.0" y2="304.6" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="275.2" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="743.0" y1="288.5" x2="743.0" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="296.6" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="746.9" y1="299.5" x2="746.9" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="300.2" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="750.9" y1="306.2" x2="750.9" y2="335.9" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="317.1" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="754.8" y1="312.9" x2="754.8" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="331.8" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="758.7" y1="301.7" x2="758.7" y2="370.2" stroke="var(--up)" class="wick"/>
<rect x="757.51" y="303.4" width="2.44" height="53.5" fill="var(--up)"/>
<line x1="762.7" y1="264.3" x2="762.7" y2="314.9" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="277.2" width="2.44" height="29.6" fill="var(--up)"/>
<line x1="766.6" y1="197.5" x2="766.6" y2="266.6" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="225.0" width="2.44" height="40.5" fill="var(--up)"/>
<line x1="770.5" y1="191.6" x2="770.5" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="196.8" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="774.5" y1="189.7" x2="774.5" y2="236.2" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="206.4" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="778.4" y1="206.1" x2="778.4" y2="247.8" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="220.5" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="782.3" y1="209.6" x2="782.3" y2="229.5" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="220.1" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="786.3" y1="82.2" x2="786.3" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="84.8" width="2.44" height="73.1" fill="var(--up)"/>
<line x1="790.2" y1="76.1" x2="790.2" y2="130.1" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="77.1" width="2.44" height="36.0" fill="var(--up)"/>
<line x1="794.2" y1="95.6" x2="794.2" y2="130.2" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="99.2" width="2.44" height="6.9" fill="var(--down)"/>
<line x1="798.1" y1="79.0" x2="798.1" y2="127.1" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="93.4" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="802.0" y1="109.5" x2="802.0" y2="225.1" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="126.8" width="2.44" height="89.2" fill="var(--down)"/>
<line x1="806.0" y1="145.1" x2="806.0" y2="196.4" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="153.6" width="2.44" height="38.8" fill="var(--up)"/>
<line x1="809.9" y1="110.7" x2="809.9" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="145.3" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="813.8" y1="136.4" x2="813.8" y2="195.9" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="185.1" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="817.8" y1="169.9" x2="817.8" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="816.56" y="189.9" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="821.7" y1="169.0" x2="821.7" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="185.7" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="825.7" y1="141.3" x2="825.7" y2="170.6" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="152.7" width="2.44" height="12.1" fill="var(--up)"/>
<line x1="829.6" y1="139.7" x2="829.6" y2="178.0" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="175.7" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="833.5" y1="122.1" x2="833.5" y2="180.5" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="169.7" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="837.5" y1="129.7" x2="837.5" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="164.5" width="2.44" height="12.8" fill="var(--down)"/>
<line x1="841.4" y1="161.4" x2="841.4" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="161.4" width="2.44" height="10.2" fill="var(--down)"/>
<line x1="845.3" y1="180.2" x2="845.3" y2="212.0" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="191.9" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="849.3" y1="204.1" x2="849.3" y2="231.9" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="217.7" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="853.2" y1="208.0" x2="853.2" y2="259.0" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="208.0" width="2.44" height="35.4" fill="var(--down)"/>
<line x1="857.1" y1="196.3" x2="857.1" y2="276.2" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="212.2" width="2.44" height="51.9" fill="var(--up)"/>
<line x1="861.1" y1="178.0" x2="861.1" y2="232.6" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="197.7" width="2.44" height="30.3" fill="var(--down)"/>
<line x1="865.0" y1="197.4" x2="865.0" y2="242.8" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="219.0" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="869.0" y1="179.5" x2="869.0" y2="214.6" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="189.4" width="2.44" height="21.2" fill="var(--down)"/>
<line x1="872.9" y1="196.7" x2="872.9" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="219.1" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="876.8" y1="210.2" x2="876.8" y2="245.8" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="217.4" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="880.8" y1="202.9" x2="880.8" y2="252.5" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="217.2" width="2.44" height="16.5" fill="var(--down)"/>
<line x1="884.7" y1="222.0" x2="884.7" y2="250.8" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="223.3" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="888.6" y1="180.9" x2="888.6" y2="243.1" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="182.3" width="2.44" height="54.6" fill="var(--up)"/>
<line x1="892.6" y1="170.0" x2="892.6" y2="202.1" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="175.4" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="896.5" y1="164.8" x2="896.5" y2="219.7" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="166.1" width="2.44" height="43.9" fill="var(--down)"/>
<line x1="900.4" y1="192.5" x2="900.4" y2="234.3" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="213.9" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="904.4" y1="184.5" x2="904.4" y2="240.6" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="191.2" width="2.44" height="41.0" fill="var(--down)"/>
<line x1="908.3" y1="240.4" x2="908.3" y2="276.3" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="251.1" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="912.3" y1="333.1" x2="912.3" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="359.8" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="916.2" y1="344.1" x2="916.2" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="365.1" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="920.1" y1="316.4" x2="920.1" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="325.0" width="2.44" height="56.2" fill="var(--up)"/>
<line x1="924.1" y1="319.1" x2="924.1" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="344.2" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="928.0" y1="340.0" x2="928.0" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="357.6" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="931.9" y1="356.4" x2="931.9" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="357.4" width="2.44" height="31.1" fill="var(--down)"/>
<line x1="935.9" y1="333.2" x2="935.9" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="345.8" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="939.8" y1="287.1" x2="939.8" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="324.7" width="2.44" height="33.0" fill="var(--up)"/>
<line x1="943.7" y1="303.0" x2="943.7" y2="366.7" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="309.9" width="2.44" height="56.1" fill="var(--down)"/>
<line x1="947.7" y1="332.4" x2="947.7" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="352.7" width="2.44" height="13.1" fill="var(--down)"/>
<line x1="951.6" y1="324.5" x2="951.6" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="340.9" width="2.44" height="16.4" fill="var(--up)"/>
<line x1="955.6" y1="325.6" x2="955.6" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="327.9" width="2.44" height="26.4" fill="var(--down)"/>
<line x1="959.5" y1="309.5" x2="959.5" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="338.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="963.4" y1="313.5" x2="963.4" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="313.5" width="2.44" height="37.6" fill="var(--down)"/>
<line x1="967.4" y1="335.0" x2="967.4" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="346.5" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="971.3" y1="312.9" x2="971.3" y2="356.3" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="330.6" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="975.2" y1="334.0" x2="975.2" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="350.3" width="2.44" height="18.7" fill="var(--down)"/>
<line x1="979.2" y1="371.2" x2="979.2" y2="399.1" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="373.6" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="983.1" y1="363.7" x2="983.1" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="375.5" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="987.0" y1="381.4" x2="987.0" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="985.83" y="396.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="991.0" y1="386.4" x2="991.0" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="393.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="994.9" y1="363.5" x2="994.9" y2="399.5" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="397.0" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="998.9" y1="397.6" x2="998.9" y2="426.6" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="404.9" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="1002.8" y1="415.3" x2="1002.8" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="423.6" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="1006.7" y1="418.7" x2="1006.7" y2="439.6" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="425.7" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="1010.7" y1="410.9" x2="1010.7" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="413.5" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="1014.6" y1="419.3" x2="1014.6" y2="439.7" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="424.2" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="1018.5" y1="364.0" x2="1018.5" y2="419.8" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="369.0" width="2.44" height="46.5" fill="var(--up)"/>
<line x1="1022.5" y1="339.9" x2="1022.5" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="359.4" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="1026.4" y1="314.3" x2="1026.4" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="314.9" width="2.44" height="25.9" fill="var(--up)"/>
<line x1="1030.3" y1="315.3" x2="1030.3" y2="347.6" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="315.3" width="2.44" height="24.3" fill="var(--down)"/>
<line x1="1034.3" y1="332.8" x2="1034.3" y2="354.1" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="345.2" width="2.44" height="8.8" fill="var(--up)"/>
<line x1="1038.2" y1="365.7" x2="1038.2" y2="438.2" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="371.4" width="2.44" height="62.7" fill="var(--down)"/>
<line x1="1042.2" y1="433.5" x2="1042.2" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="435.6" width="2.44" height="20.6" fill="var(--down)"/>
<line x1="1046.1" y1="441.0" x2="1046.1" y2="471.0" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="452.8" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="1050.0" y1="450.5" x2="1050.0" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="458.6" width="2.44" height="45.8" fill="var(--down)"/>
<line x1="60" y1="439.6" x2="1052" y2="439.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="443.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$311 R1</text>
<text x="1058" y="455.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="392.2" x2="1052" y2="392.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="395.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$325 R2</text>
<text x="1058" y="407.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="325.4" x2="1052" y2="325.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="328.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$345 R3</text>
<text x="1058" y="340.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="600.2" x2="1052" y2="600.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="594.2" font-size="11.5" fill="var(--support)" font-weight="600">$265 S1 (52주 최저)</text>
<text x="1058" y="606.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="504.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="496.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $293 (2026-09-04)</text>
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
| R3 | $345 | 2 | 2025-12-10·2026-08-27 스윙 고점대 — FY2025 실적 전후와 2026 Q2 실적 후 반등의 상단이 같은 가격대에서 겹친다 |
| R2 | $325 | 3 | 2025-12-29·2026-01-15·2026-01-28 스윙 고점대 — 연말·연초 횡보 구간의 상단 |
| R1 | $311 | 2 | 2026-02-18·2026-03-05 스윙 고점대 — 현재가에 가장 가까운 저항 |
| **현재가** | **$292.70** (2026-09-04 종가) | — | R1과 S1 (52주 최저) 사이 |
| S1 (52주 최저) | $265 | 3 | 2026-02-03·2026-03-30·2026-04-10 스윙 저점대. 이 구간의 최저가($262.75)를 `--force-level`로 넣었으나 결과적으로 터치 3회 클러스터로 잡혔다 |
| 참고선 | $417 | — | 52주 최고(2026-06-02 $416.69). 2026-07-17 갭다운 이후 한 번도 회복되지 않아 **현재 레짐과 단절된 수준**이라 저항으로 보지 않는다 |

> 유효 클러스터가 저항 3개·지지 1개로 잡혀 **S2·S3는 두지 않았다** — 현재가 아래로는 52주 최저 부근($265) 외에 터치 2회 이상의 스윙 저점 군집이 없다. 이는 **주가가 지난 1년 대부분을 지금보다 높은 가격대에서 보냈다**는 뜻이기도 하다.

---

## 3. 관측된 특이 구간

### 3-1. 2026-07-17 — Moonshot Kimi K3 발표發 급락

- 중국 Moonshot AI가 오픈소스 EDA 도구만으로 칩 설계 플로우를 자율 완주했다고 공개한 날이다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−9.47%** ($364.65 → $330.11), 거래량은 평소(일 222만 주 내외) 대비 약 **2.3배**인 **519만 주**.
- 이 하루로 6월 초 형성된 $400대 가격대가 무너졌고, 이후 주가는 한 번도 그 위로 복귀하지 못했다. 그래서 **52주 최고 $416.69는 지지/저항이 아니라 참고선으로만 처리**했다 — 현재 레짐과 단절돼 있다.

### 3-2. 2026-08-28 ~ 09-04 — 6거래일 연속 하락

- 회사 고유의 악재 없이 국채 금리 상승·유가 반등에 따른 고밸류 성장주 전반의 디레이팅이 원인으로 지목된 구간이다.
- 종가 $347.55(8/27) → **$292.70**(9/4), 6거래일 누적 **−15.78%**. 특히 9월 1일 −7.60%($338.78 → $313.04), 9월 4일 −4.00%($304.88 → $292.70)로 마지막 날 거래량이 **422만 주(평소의 1.9배)**로 늘었다.
- 이 구간에서 R1($311)이 저항으로 바뀌었고, 현재가는 **R1과 52주 최저 부근($265) 사이의 빈 구간**에 놓였다 — 아래쪽에 최근 1년의 터치 이력이 거의 없다는 뜻이므로, 지지 레벨의 신뢰도를 낮게 볼 것.

---

## 4. 방법론 · 한계

@@FACTS@@
- **생성**: `scripts/gen_technical_chart.py CDNS --name Cadence --event 2026-06-01:"ChipStack 발표 급등" --event 2026-07-17:"AI 모델 우려 급락" --event 2026-07-27:"2Q26 실적·가이던스 상향" --ref-line 416.69:"52주 최고" --force-level '262.75:(52주 최저)' --close-on 2026-09-04 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3-1의 갭다운이 레벨 해석을 크게 왜곡한다.** 2026-07-17 이후 가격대가 통째로 아래로 이동해, 그 이전에 형성된 고점 클러스터($417 부근)는 현재 레짐에서 저항으로 기능한다고 보기 어렵다. 그래서 참고선으로만 두었다.
    - **레벨을 4개만 두었다.** 지지 쪽 유효 클러스터가 하나뿐이라 `--levels` 기본값 3을 억지로 채우지 않았고, 52주 최저는 `--force-level`로 지정했으나 결과적으로 터치 3회 클러스터로 잡혔다.
    - 해당 기간에 주식분할·대규모 유상증자는 없었다. Hexagon D&E 인수 대가로 발행한 신주 3.2백만 주(2026-02)는 발행주식수의 1.2% 수준이라 가격 연속성에 영향을 주지 않는다.

---

*작성일: 2026-09-08*
