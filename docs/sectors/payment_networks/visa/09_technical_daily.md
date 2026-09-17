# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-15 종가 $375.62**는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.
- ⚠️ **차트의 마지막 캔들은 미완성 봉이다.** 이 문서는 2026-09-16 미 동부시간 11:01(정규장 개장 중)에 생성돼, 차트 우측 끝에 그날의 **장중 봉**이 들어가 있다. **이 폴더의 모든 문서가 쓰는 기준 종가는 마지막 완료 거래일인 2026-09-15**이며, 아래 §2 현재가 행도 그 값이다(§4 참고).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-16 ~ 2026-09-16)

<style>
.v-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.v-chart svg { width:100%; height:auto; display:block; }
.v-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.v-chart .title { fill: var(--ink); font-weight:600; }
.v-chart .grid { stroke: var(--grid); stroke-width:1; }
.v-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="v-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visa(V) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Visa (V) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-16 ~ 2026-09-16 · 마지막 종가 $372.56 (2026-09-16) · 단위 USD</text>
<line x1="60" y1="569.0" x2="1052" y2="569.0" class="grid"/>
<text x="52" y="573.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="455.0" x2="1052" y2="455.0" class="grid"/>
<text x="52" y="459.0" font-size="11" text-anchor="end" fill="var(--muted)">320</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">340</text>
<line x1="60" y1="227.0" x2="1052" y2="227.0" class="grid"/>
<text x="52" y="231.0" font-size="11" text-anchor="end" fill="var(--muted)">360</text>
<line x1="60" y1="113.0" x2="1052" y2="113.0" class="grid"/>
<text x="52" y="117.0" font-size="11" text-anchor="end" fill="var(--muted)">380</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="105.3" y1="626.0" x2="105.3" y2="631.0" class="axis"/>
<text x="105.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="195.8" y1="626.0" x2="195.8" y2="631.0" class="axis"/>
<text x="195.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="270.6" y1="626.0" x2="270.6" y2="631.0" class="axis"/>
<text x="270.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="357.2" y1="626.0" x2="357.2" y2="631.0" class="axis"/>
<text x="357.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="435.9" y1="626.0" x2="435.9" y2="631.0" class="axis"/>
<text x="435.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="510.7" y1="626.0" x2="510.7" y2="631.0" class="axis"/>
<text x="510.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="597.3" y1="626.0" x2="597.3" y2="631.0" class="axis"/>
<text x="597.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="680.0" y1="626.0" x2="680.0" y2="631.0" class="axis"/>
<text x="680.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="758.7" y1="626.0" x2="758.7" y2="631.0" class="axis"/>
<text x="758.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="841.4" y1="626.0" x2="841.4" y2="631.0" class="axis"/>
<text x="841.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="928.0" y1="626.0" x2="928.0" y2="631.0" class="axis"/>
<text x="928.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1010.7" y1="626.0" x2="1010.7" y2="631.0" class="axis"/>
<text x="1010.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="337.9" x2="62.0" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="340.8" width="2.44" height="21.6" fill="var(--up)"/>
<line x1="65.9" y1="305.7" x2="65.9" y2="343.7" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="305.7" width="2.44" height="35.7" fill="var(--up)"/>
<line x1="69.8" y1="311.0" x2="69.8" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="314.0" width="2.44" height="37.3" fill="var(--down)"/>
<line x1="73.8" y1="325.7" x2="73.8" y2="351.0" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="331.8" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="77.7" y1="313.3" x2="77.7" y2="348.6" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="316.1" width="2.44" height="30.5" fill="var(--up)"/>
<line x1="81.7" y1="311.0" x2="81.7" y2="354.5" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="314.8" width="2.44" height="33.6" fill="var(--down)"/>
<line x1="85.6" y1="341.6" x2="85.6" y2="352.9" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="346.0" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="89.5" y1="339.9" x2="89.5" y2="372.3" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="350.4" width="2.44" height="19.5" fill="var(--down)"/>
<line x1="93.5" y1="343.8" x2="93.5" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="356.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="97.4" y1="337.4" x2="97.4" y2="366.4" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="340.1" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="101.3" y1="309.0" x2="101.3" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="333.1" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="105.3" y1="287.6" x2="105.3" y2="339.2" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="296.4" width="2.44" height="42.9" fill="var(--up)"/>
<line x1="109.2" y1="300.1" x2="109.2" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="107.99" y="305.5" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="113.1" y1="266.0" x2="113.1" y2="306.8" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="284.9" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="117.1" y1="277.6" x2="117.1" y2="316.2" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="283.9" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="121.0" y1="258.7" x2="121.0" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="270.2" width="2.44" height="13.5" fill="var(--up)"/>
<line x1="125.0" y1="255.5" x2="125.0" y2="277.7" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="262.5" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="128.9" y1="267.6" x2="128.9" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="275.6" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="132.8" y1="281.7" x2="132.8" y2="322.5" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="297.5" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="136.8" y1="297.3" x2="136.8" y2="336.8" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="319.8" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="140.7" y1="283.9" x2="140.7" y2="339.7" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="293.2" width="2.44" height="42.1" fill="var(--up)"/>
<line x1="144.6" y1="283.5" x2="144.6" y2="318.2" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="293.2" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="148.6" y1="308.6" x2="148.6" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="312.5" width="2.44" height="54.7" fill="var(--down)"/>
<line x1="152.5" y1="321.3" x2="152.5" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="330.2" width="2.44" height="23.5" fill="var(--up)"/>
<line x1="156.4" y1="312.7" x2="156.4" y2="347.0" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="315.9" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="160.4" y1="286.0" x2="160.4" y2="323.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="299.9" width="2.44" height="23.3" fill="var(--up)"/>
<line x1="164.3" y1="294.4" x2="164.3" y2="315.3" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="296.4" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="168.3" y1="300.2" x2="168.3" y2="315.6" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="305.7" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="172.2" y1="289.2" x2="172.2" y2="310.7" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="294.3" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="176.1" y1="286.7" x2="176.1" y2="312.4" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="289.7" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="180.1" y1="284.6" x2="180.1" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="292.1" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="184.0" y1="278.4" x2="184.0" y2="346.7" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="306.8" width="2.44" height="26.9" fill="var(--down)"/>
<line x1="187.9" y1="285.6" x2="187.9" y2="330.8" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="312.3" width="2.44" height="16.0" fill="var(--up)"/>
<line x1="191.9" y1="323.9" x2="191.9" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="329.1" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="195.8" y1="334.1" x2="195.8" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="335.3" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="199.7" y1="339.2" x2="199.7" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="339.3" width="2.44" height="21.8" fill="var(--up)"/>
<line x1="203.7" y1="329.0" x2="203.7" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="340.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="207.6" y1="348.7" x2="207.6" y2="376.9" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="349.0" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="211.6" y1="350.7" x2="211.6" y2="370.4" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="359.6" width="2.44" height="4.0" fill="var(--down)"/>
<line x1="215.5" y1="348.5" x2="215.5" y2="373.4" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="360.1" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="219.4" y1="346.2" x2="219.4" y2="379.8" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="347.2" width="2.44" height="19.5" fill="var(--up)"/>
<line x1="223.4" y1="316.7" x2="223.4" y2="355.8" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="347.4" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="227.3" y1="332.7" x2="227.3" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="346.5" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="231.2" y1="363.3" x2="231.2" y2="403.5" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="364.4" width="2.44" height="33.5" fill="var(--down)"/>
<line x1="235.2" y1="378.8" x2="235.2" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="391.4" width="2.44" height="30.8" fill="var(--down)"/>
<line x1="239.1" y1="426.5" x2="239.1" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="429.4" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="243.0" y1="429.0" x2="243.0" y2="455.7" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="431.5" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="247.0" y1="407.1" x2="247.0" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="431.5" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="250.9" y1="391.8" x2="250.9" y2="430.5" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="409.5" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="254.9" y1="393.8" x2="254.9" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="402.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="258.8" y1="363.5" x2="258.8" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="372.2" width="2.44" height="32.1" fill="var(--up)"/>
<line x1="262.7" y1="365.5" x2="262.7" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="372.2" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="266.7" y1="369.4" x2="266.7" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="372.7" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="270.6" y1="379.2" x2="270.6" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="269.38" y="381.2" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="274.5" y1="382.0" x2="274.5" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="389.7" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="278.5" y1="384.6" x2="278.5" y2="401.7" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="400.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="282.4" y1="384.4" x2="282.4" y2="430.6" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="390.7" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="286.3" y1="374.6" x2="286.3" y2="418.5" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="390.9" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="290.3" y1="390.4" x2="290.3" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="289.07" y="398.7" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="294.2" y1="408.1" x2="294.2" y2="426.1" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="417.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="298.2" y1="405.1" x2="298.2" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="417.2" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="302.1" y1="299.3" x2="302.1" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="308.9" width="2.44" height="74.3" fill="var(--up)"/>
<line x1="306.0" y1="284.9" x2="306.0" y2="307.0" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="295.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="310.0" y1="292.8" x2="310.0" y2="319.2" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="296.4" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="313.9" y1="297.6" x2="313.9" y2="319.8" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="306.8" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="317.8" y1="296.6" x2="317.8" y2="320.0" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="309.4" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="321.8" y1="298.1" x2="321.8" y2="316.7" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="306.7" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="325.7" y1="284.5" x2="325.7" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="288.3" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="329.7" y1="264.4" x2="329.7" y2="286.3" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="272.1" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="333.6" y1="247.6" x2="333.6" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="264.7" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="337.5" y1="249.9" x2="337.5" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="254.7" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="341.5" y1="245.6" x2="341.5" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="254.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="345.4" y1="246.7" x2="345.4" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="252.7" width="2.44" height="5.0" fill="var(--down)"/>
<line x1="349.3" y1="256.2" x2="349.3" y2="268.8" stroke="var(--down)" class="wick"/>
<rect x="348.11" y="261.2" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="353.3" y1="254.4" x2="353.3" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="263.2" width="2.44" height="16.8" fill="var(--down)"/>
<line x1="357.2" y1="283.7" x2="357.2" y2="321.2" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="284.7" width="2.44" height="19.3" fill="var(--down)"/>
<line x1="361.1" y1="241.0" x2="361.1" y2="317.9" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="262.3" width="2.44" height="53.0" fill="var(--up)"/>
<line x1="365.1" y1="234.9" x2="365.1" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="240.9" width="2.44" height="22.1" fill="var(--up)"/>
<line x1="369.0" y1="236.8" x2="369.0" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="243.2" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="373.0" y1="247.8" x2="373.0" y2="286.8" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="255.5" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="376.9" y1="257.2" x2="376.9" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="271.7" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="380.8" y1="303.9" x2="380.8" y2="356.3" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="322.8" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="384.8" y1="355.1" x2="384.8" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="358.1" width="2.44" height="52.0" fill="var(--down)"/>
<line x1="388.7" y1="398.6" x2="388.7" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="402.7" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="392.6" y1="388.4" x2="392.6" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="401.8" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="396.6" y1="402.3" x2="396.6" y2="424.2" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="407.7" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="400.5" y1="407.6" x2="400.5" y2="446.1" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="421.8" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="404.4" y1="405.6" x2="404.4" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="418.3" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="408.4" y1="407.2" x2="408.4" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="418.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="412.3" y1="410.5" x2="412.3" y2="428.7" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="419.8" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="416.3" y1="386.6" x2="416.3" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="406.6" width="2.44" height="2.8" fill="var(--up)"/>
<line x1="420.2" y1="404.1" x2="420.2" y2="427.0" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="406.7" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="424.1" y1="407.2" x2="424.1" y2="427.2" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="415.2" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="428.1" y1="378.8" x2="428.1" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="387.7" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="432.0" y1="380.9" x2="432.0" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="385.3" width="2.44" height="59.2" fill="var(--down)"/>
<line x1="435.9" y1="371.3" x2="435.9" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="376.1" width="2.44" height="51.4" fill="var(--up)"/>
<line x1="439.9" y1="365.0" x2="439.9" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="388.6" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="443.8" y1="390.5" x2="443.8" y2="429.8" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="398.3" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="447.7" y1="354.7" x2="447.7" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="380.9" width="2.44" height="22.1" fill="var(--down)"/>
<line x1="451.7" y1="368.8" x2="451.7" y2="414.5" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="387.9" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="455.6" y1="381.9" x2="455.6" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="393.7" width="2.44" height="29.5" fill="var(--down)"/>
<line x1="459.6" y1="398.7" x2="459.6" y2="429.1" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="408.4" width="2.44" height="19.7" fill="var(--up)"/>
<line x1="463.5" y1="392.1" x2="463.5" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="402.3" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="467.4" y1="385.2" x2="467.4" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="404.3" width="2.44" height="26.8" fill="var(--down)"/>
<line x1="471.4" y1="418.1" x2="471.4" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="433.2" width="2.44" height="55.6" fill="var(--down)"/>
<line x1="475.3" y1="447.1" x2="475.3" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="457.9" width="2.44" height="29.0" fill="var(--up)"/>
<line x1="479.2" y1="442.0" x2="479.2" y2="473.7" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="453.3" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="483.2" y1="453.9" x2="483.2" y2="479.3" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="461.1" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="487.1" y1="441.6" x2="487.1" y2="467.4" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="449.6" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="491.0" y1="452.0" x2="491.0" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="460.5" width="2.44" height="71.4" fill="var(--down)"/>
<line x1="495.0" y1="516.2" x2="495.0" y2="551.4" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="527.8" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="498.9" y1="489.5" x2="498.9" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="495.0" width="2.44" height="25.3" fill="var(--up)"/>
<line x1="502.9" y1="458.3" x2="502.9" y2="489.5" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="473.8" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="506.8" y1="453.7" x2="506.8" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="454.2" width="2.44" height="32.4" fill="var(--up)"/>
<line x1="510.7" y1="440.2" x2="510.7" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="452.1" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="514.7" y1="443.4" x2="514.7" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="450.3" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="518.6" y1="422.1" x2="518.6" y2="456.1" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="446.8" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="522.5" y1="439.0" x2="522.5" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="456.1" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="526.5" y1="468.2" x2="526.5" y2="498.9" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="470.0" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="530.4" y1="475.5" x2="530.4" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="478.0" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="534.3" y1="471.4" x2="534.3" y2="503.7" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="481.0" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="538.3" y1="483.0" x2="538.3" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="493.5" width="2.44" height="24.5" fill="var(--down)"/>
<line x1="542.2" y1="506.6" x2="542.2" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="522.6" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="546.2" y1="510.0" x2="546.2" y2="532.4" stroke="var(--down)" class="wick"/>
<rect x="544.94" y="525.7" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="550.1" y1="505.6" x2="550.1" y2="526.9" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="511.4" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="554.0" y1="496.7" x2="554.0" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="504.5" width="2.44" height="16.3" fill="var(--down)"/>
<line x1="558.0" y1="523.7" x2="558.0" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="526.8" width="2.44" height="47.8" fill="var(--down)"/>
<line x1="561.9" y1="554.9" x2="561.9" y2="585.9" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="570.7" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="565.8" y1="552.4" x2="565.8" y2="574.6" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="559.8" width="2.44" height="10.1" fill="var(--up)"/>
<line x1="569.8" y1="524.3" x2="569.8" y2="552.8" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="539.4" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="573.7" y1="534.6" x2="573.7" y2="565.5" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="547.6" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="577.7" y1="520.6" x2="577.7" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="537.8" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="581.6" y1="524.1" x2="581.6" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="537.5" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="585.5" y1="542.8" x2="585.5" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="544.4" width="2.44" height="50.2" fill="var(--down)"/>
<line x1="589.5" y1="565.1" x2="589.5" y2="592.4" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="571.6" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="593.4" y1="550.0" x2="593.4" y2="588.4" stroke="var(--up)" class="wick"/>
<rect x="592.18" y="556.2" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="597.3" y1="540.2" x2="597.3" y2="603.8" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="540.2" width="2.44" height="37.3" fill="var(--down)"/>
<line x1="601.3" y1="554.9" x2="601.3" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="564.4" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="605.2" y1="543.8" x2="605.2" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="550.0" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="609.1" y1="540.6" x2="609.1" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="554.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="613.1" y1="505.8" x2="613.1" y2="525.1" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="517.9" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="617.0" y1="514.4" x2="617.0" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="521.7" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="621.0" y1="517.7" x2="621.0" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="519.4" width="2.44" height="24.8" fill="var(--down)"/>
<line x1="624.9" y1="513.4" x2="624.9" y2="555.7" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="515.5" width="2.44" height="31.1" fill="var(--up)"/>
<line x1="628.8" y1="499.9" x2="628.8" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="504.2" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="632.8" y1="473.6" x2="632.8" y2="503.3" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="478.3" width="2.44" height="16.6" fill="var(--up)"/>
<line x1="636.7" y1="466.4" x2="636.7" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="635.48" y="475.8" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="640.6" y1="458.2" x2="640.6" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="472.0" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="644.6" y1="469.0" x2="644.6" y2="498.6" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="475.5" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="648.5" y1="472.7" x2="648.5" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="489.1" width="2.44" height="23.2" fill="var(--down)"/>
<line x1="652.4" y1="504.2" x2="652.4" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="504.6" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="656.4" y1="499.5" x2="656.4" y2="540.4" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="509.1" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="660.3" y1="512.1" x2="660.3" y2="543.4" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="515.3" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="664.3" y1="507.3" x2="664.3" y2="534.5" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="514.0" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="668.2" y1="489.4" x2="668.2" y2="519.2" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="499.5" width="2.44" height="16.5" fill="var(--down)"/>
<line x1="672.1" y1="329.7" x2="672.1" y2="376.4" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="361.5" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="676.1" y1="383.8" x2="676.1" y2="408.9" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="385.9" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="680.0" y1="364.7" x2="680.0" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="381.6" width="2.44" height="27.6" fill="var(--down)"/>
<line x1="683.9" y1="399.2" x2="683.9" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="409.4" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="687.9" y1="423.2" x2="687.9" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="686.65" y="425.9" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="691.8" y1="428.9" x2="691.8" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="433.6" width="2.44" height="28.2" fill="var(--down)"/>
<line x1="695.7" y1="434.0" x2="695.7" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="447.7" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="699.7" y1="448.9" x2="699.7" y2="476.9" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="449.4" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="703.6" y1="425.5" x2="703.6" y2="466.3" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="433.0" width="2.44" height="27.1" fill="var(--up)"/>
<line x1="707.6" y1="404.2" x2="707.6" y2="431.1" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="418.4" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="711.5" y1="424.1" x2="711.5" y2="456.1" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="433.4" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="715.4" y1="436.0" x2="715.4" y2="453.6" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="440.6" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="719.4" y1="403.6" x2="719.4" y2="433.1" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="422.2" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="723.3" y1="378.4" x2="723.3" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="383.0" width="2.44" height="46.8" fill="var(--up)"/>
<line x1="727.2" y1="368.5" x2="727.2" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="379.0" width="2.44" height="19.5" fill="var(--down)"/>
<line x1="731.2" y1="388.5" x2="731.2" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="729.95" y="393.7" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="735.1" y1="383.6" x2="735.1" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="391.6" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="739.0" y1="378.4" x2="739.0" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="395.0" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="743.0" y1="406.5" x2="743.0" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="418.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="746.9" y1="389.7" x2="746.9" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="411.6" width="2.44" height="10.1" fill="var(--up)"/>
<line x1="750.9" y1="414.6" x2="750.9" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="420.7" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="754.8" y1="388.5" x2="754.8" y2="424.5" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="418.7" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="758.7" y1="410.2" x2="758.7" y2="462.5" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="413.6" width="2.44" height="25.6" fill="var(--down)"/>
<line x1="762.7" y1="435.0" x2="762.7" y2="492.7" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="440.7" width="2.44" height="29.6" fill="var(--down)"/>
<line x1="766.6" y1="468.4" x2="766.6" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="468.4" width="2.44" height="29.9" fill="var(--down)"/>
<line x1="770.5" y1="427.9" x2="770.5" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="454.0" width="2.44" height="19.3" fill="var(--up)"/>
<line x1="774.5" y1="420.9" x2="774.5" y2="449.5" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="434.7" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="778.4" y1="432.7" x2="778.4" y2="463.9" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="447.3" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="782.3" y1="423.7" x2="782.3" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="426.2" width="2.44" height="36.4" fill="var(--up)"/>
<line x1="786.3" y1="415.7" x2="786.3" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="417.3" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="790.2" y1="433.9" x2="790.2" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="443.6" width="2.44" height="16.8" fill="var(--down)"/>
<line x1="794.2" y1="421.2" x2="794.2" y2="456.1" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="441.4" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="798.1" y1="418.3" x2="798.1" y2="439.3" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="433.2" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="802.0" y1="379.2" x2="802.0" y2="430.0" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="380.2" width="2.44" height="42.4" fill="var(--up)"/>
<line x1="806.0" y1="359.1" x2="806.0" y2="398.2" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="378.0" width="2.44" height="17.8" fill="var(--down)"/>
<line x1="809.9" y1="384.7" x2="809.9" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="392.3" width="2.44" height="21.4" fill="var(--down)"/>
<line x1="813.8" y1="380.9" x2="813.8" y2="421.6" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="407.5" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="817.8" y1="390.7" x2="817.8" y2="408.9" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="404.7" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="821.7" y1="370.6" x2="821.7" y2="413.8" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="385.3" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="825.7" y1="341.3" x2="825.7" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="383.4" width="2.44" height="11.6" fill="var(--down)"/>
<line x1="829.6" y1="342.6" x2="829.6" y2="389.8" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="362.5" width="2.44" height="22.7" fill="var(--up)"/>
<line x1="833.5" y1="307.9" x2="833.5" y2="350.9" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="331.6" width="2.44" height="19.3" fill="var(--up)"/>
<line x1="837.5" y1="316.5" x2="837.5" y2="346.2" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="323.4" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="841.4" y1="264.8" x2="841.4" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="277.8" width="2.44" height="37.2" fill="var(--up)"/>
<line x1="845.3" y1="214.9" x2="845.3" y2="269.7" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="214.9" width="2.44" height="54.8" fill="var(--up)"/>
<line x1="849.3" y1="198.4" x2="849.3" y2="290.6" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="209.9" width="2.44" height="32.8" fill="var(--down)"/>
<line x1="853.2" y1="249.3" x2="853.2" y2="301.6" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="271.5" width="2.44" height="21.7" fill="var(--up)"/>
<line x1="857.1" y1="274.9" x2="857.1" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="282.3" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="861.1" y1="292.6" x2="861.1" y2="315.8" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="294.3" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="865.0" y1="277.3" x2="865.0" y2="310.6" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="280.4" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="869.0" y1="229.9" x2="869.0" y2="278.0" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="239.8" width="2.44" height="34.3" fill="var(--up)"/>
<line x1="872.9" y1="227.3" x2="872.9" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="249.7" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="876.8" y1="224.5" x2="876.8" y2="289.0" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="254.7" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="880.8" y1="197.7" x2="880.8" y2="243.5" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="197.7" width="2.44" height="40.5" fill="var(--up)"/>
<line x1="884.7" y1="200.6" x2="884.7" y2="244.1" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="206.7" width="2.44" height="28.6" fill="var(--down)"/>
<line x1="888.6" y1="209.9" x2="888.6" y2="247.3" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="223.8" width="2.44" height="19.8" fill="var(--up)"/>
<line x1="892.6" y1="232.0" x2="892.6" y2="257.3" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="244.2" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="896.5" y1="241.1" x2="896.5" y2="271.1" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="246.6" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="900.4" y1="272.3" x2="900.4" y2="292.6" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="272.3" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="904.4" y1="250.7" x2="904.4" y2="278.0" stroke="var(--up)" class="wick"/>
<rect x="903.16" y="251.3" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="908.3" y1="206.1" x2="908.3" y2="237.0" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="212.6" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="912.3" y1="163.4" x2="912.3" y2="211.4" stroke="var(--up)" class="wick"/>
<rect x="911.03" y="189.4" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="916.2" y1="147.4" x2="916.2" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="177.2" width="2.44" height="66.9" fill="var(--up)"/>
<line x1="920.1" y1="187.1" x2="920.1" y2="222.7" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="191.3" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="924.1" y1="187.8" x2="924.1" y2="226.4" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="192.1" width="2.44" height="13.5" fill="var(--up)"/>
<line x1="928.0" y1="158.8" x2="928.0" y2="202.2" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="178.6" width="2.44" height="16.1" fill="var(--down)"/>
<line x1="931.9" y1="163.7" x2="931.9" y2="226.5" stroke="var(--up)" class="wick"/>
<rect x="930.72" y="172.3" width="2.44" height="44.6" fill="var(--up)"/>
<line x1="935.9" y1="156.3" x2="935.9" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="156.9" width="2.44" height="21.4" fill="var(--down)"/>
<line x1="939.8" y1="163.7" x2="939.8" y2="197.1" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="167.3" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="943.7" y1="168.6" x2="943.7" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="178.5" width="2.44" height="34.3" fill="var(--down)"/>
<line x1="947.7" y1="203.2" x2="947.7" y2="233.4" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="215.6" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="951.6" y1="201.1" x2="951.6" y2="227.2" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="210.9" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="955.6" y1="207.9" x2="955.6" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="221.3" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="959.5" y1="195.9" x2="959.5" y2="234.4" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="195.9" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="963.4" y1="188.2" x2="963.4" y2="211.3" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="193.4" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="967.4" y1="206.7" x2="967.4" y2="235.4" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="210.8" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="971.3" y1="193.3" x2="971.3" y2="238.1" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="202.8" width="2.44" height="26.4" fill="var(--up)"/>
<line x1="975.2" y1="166.4" x2="975.2" y2="210.5" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="195.4" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="979.2" y1="176.1" x2="979.2" y2="206.3" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="194.3" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="983.1" y1="159.7" x2="983.1" y2="189.0" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="164.1" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="987.0" y1="93.4" x2="987.0" y2="157.4" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="99.3" width="2.44" height="52.2" fill="var(--up)"/>
<line x1="991.0" y1="89.1" x2="991.0" y2="111.5" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="89.4" width="2.44" height="16.7" fill="var(--up)"/>
<line x1="994.9" y1="81.3" x2="994.9" y2="106.8" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="89.4" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="998.9" y1="102.9" x2="998.9" y2="121.6" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="106.5" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="1002.8" y1="92.0" x2="1002.8" y2="118.5" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="103.9" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="1006.7" y1="98.9" x2="1006.7" y2="119.8" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="105.3" width="2.44" height="11.3" fill="var(--down)"/>
<line x1="1010.7" y1="108.7" x2="1010.7" y2="157.3" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="115.0" width="2.44" height="39.8" fill="var(--down)"/>
<line x1="1014.6" y1="112.0" x2="1014.6" y2="147.1" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="122.1" width="2.44" height="25.0" fill="var(--up)"/>
<line x1="1018.5" y1="100.4" x2="1018.5" y2="130.9" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="112.0" width="2.44" height="8.1" fill="var(--down)"/>
<line x1="1022.5" y1="127.2" x2="1022.5" y2="149.3" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="141.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1026.4" y1="150.1" x2="1026.4" y2="184.6" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="160.9" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="1030.3" y1="173.0" x2="1030.3" y2="193.5" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="178.8" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="1034.3" y1="181.4" x2="1034.3" y2="195.5" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="185.9" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="1038.2" y1="159.7" x2="1038.2" y2="181.5" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="167.4" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="1042.2" y1="129.1" x2="1042.2" y2="160.5" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="139.9" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="1046.1" y1="133.7" x2="1046.1" y2="153.9" stroke="var(--up)" class="wick"/>
<rect x="1044.87" y="138.0" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="1050.0" y1="133.1" x2="1050.0" y2="160.0" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="141.7" width="2.44" height="13.7" fill="var(--down)"/>
<line x1="60" y1="306.9" x2="1052" y2="306.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="300.9" font-size="11.5" fill="var(--support)" font-weight="600">$346 S1</text>
<text x="1058" y="312.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="373.3" x2="1052" y2="373.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="367.3" font-size="11.5" fill="var(--support)" font-weight="600">$334 S2</text>
<text x="1058" y="379.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="453.2" x2="1052" y2="453.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="447.2" font-size="11.5" fill="var(--support)" font-weight="600">$320 S3</text>
<text x="1058" y="459.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="155.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="147.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $373 (2026-09-16)</text>
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
| **현재가** | **$375.62** (2026-09-15 종가) | — | **기간 내 상단 저항이 없다** — 아래 설명 참고 |
| S1 | $346 | 2 | 2026-01-02·2026-07-23 — 현재가에 가장 근접한 지지(−7.9%) |
| S2 | $334 | 2 | 2025-09-25·2025-10-16 — 2025년 가을 지지대 |
| S3 | $320 | 5 | 2025-11-18·12-04·2026-01-20·01-30·05-08 — **1년 중 가장 강한 레벨**(터치 5회)이며, 여러 차례 되돌림의 바닥이 됐다 |
| 참고선 | $385.57 | — | 52주(그리고 5년) 최고. 현재가가 여기서 **−2.6%** 자리다 |
| 참고선 | $293.89 | — | 52주 최저 |

**저항 레벨이 하나도 없다는 것이 이 표의 핵심이다.** 터치 2회 이상 기준을 충족하는 스윙 고점 클러스터가 최근 1년 구간에 존재하지 않는데, **주가가 신고가를 계속 갱신하며 올라와 고점대에 스윙 포인트가 쌓일 시간이 없었기 때문**이다. 즉 현재가 위쪽에는 기술적으로 참조할 가격대가 없고, 아래로는 $346 → $334 → $320의 세 층이 차례로 놓여 있다.

**이 구조는 [밸류에이션](./06_valuation.md)의 결론과 방향이 엇갈린다** — 가격 흐름만 보면 저항 없는 상승 구간이지만, 밸류에이션으로는 FY2026(E) 적정주가 대비 +13.3% 고평가다. 기술적 위치와 가치 판단이 다른 것을 말하고 있으므로, 이 문서를 매수 근거로 읽지 말 것.

---


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-16~2026-09-16. 수집 시점: 2026-09-17. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py V --name "Visa" --close-on 2026-09-15 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - ⚠️ **마지막 캔들은 2026-09-16 장중 미완성 봉이다.** 이 스크립트는 시계열 종료일을 고정하는 인자가 없어 항상 가장 최근 봉까지 그리며, `--close-on`은 시계열을 자르지 않고 대조용 종가 주석만 덧붙인다. 생성 시점이 미 증시 정규장 중이었으므로 차트 우측 끝 캔들의 종가는 확정값이 아니다 — **§2 현재가 행과 다른 문서의 기준 종가는 마지막 완료 거래일 2026-09-15를 쓴다.** 마지막 봉은 스윙 탐지에 전후 구간이 필요해 레벨 계산에는 영향을 주지 않는다.
    - **저항 레벨이 0개**라 이 문서로는 상방 가격대를 논할 수 없다(위 §2 참고). 신고가 구간에서는 클러스터 기반 모델이 구조적으로 상단 정보를 주지 못한다.
    - 원주가 기준이라 **배당은 반영되지 않았다**(기간 내 배당 4회).
    - 최근 1년 구간에 주식분할은 없다(마지막 분할은 2015-03 4:1).

---

*작성일: 2026-09-17*
