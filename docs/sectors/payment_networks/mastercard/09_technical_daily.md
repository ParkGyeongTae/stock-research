# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-15 종가 $573.27**는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.
- ⚠️ **차트의 마지막 캔들은 미완성 봉이다.** 이 문서는 2026-09-16 미 동부시간 11:01(정규장 개장 중)에 생성돼, 차트 우측 끝에 그날의 **장중 봉**이 들어가 있다. **이 폴더의 모든 문서가 쓰는 기준 종가는 마지막 완료 거래일인 2026-09-15**이며, 아래 §2 현재가 행도 그 값이다(§4 참고).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-16 ~ 2026-09-16)

<style>
.ma-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .ma-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ma-chart svg { width:100%; height:auto; display:block; }
.ma-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ma-chart .title { fill: var(--ink); font-weight:600; }
.ma-chart .grid { stroke: var(--grid); stroke-width:1; }
.ma-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="ma-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mastercard(MA) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Mastercard (MA) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-16 ~ 2026-09-16 · 마지막 종가 $570.85 (2026-09-16) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">460</text>
<line x1="60" y1="548.7" x2="1052" y2="548.7" class="grid"/>
<text x="52" y="552.7" font-size="11" text-anchor="end" fill="var(--muted)">480</text>
<line x1="60" y1="471.4" x2="1052" y2="471.4" class="grid"/>
<text x="52" y="475.4" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="394.1" x2="1052" y2="394.1" class="grid"/>
<text x="52" y="398.1" font-size="11" text-anchor="end" fill="var(--muted)">520</text>
<line x1="60" y1="316.8" x2="1052" y2="316.8" class="grid"/>
<text x="52" y="320.8" font-size="11" text-anchor="end" fill="var(--muted)">540</text>
<line x1="60" y1="239.6" x2="1052" y2="239.6" class="grid"/>
<text x="52" y="243.6" font-size="11" text-anchor="end" fill="var(--muted)">560</text>
<line x1="60" y1="162.3" x2="1052" y2="162.3" class="grid"/>
<text x="52" y="166.3" font-size="11" text-anchor="end" fill="var(--muted)">580</text>
<line x1="60" y1="85.0" x2="1052" y2="85.0" class="grid"/>
<text x="52" y="89.0" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
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
<line x1="62.0" y1="130.9" x2="62.0" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="137.5" width="2.44" height="32.5" fill="var(--up)"/>
<line x1="65.9" y1="89.3" x2="65.9" y2="133.5" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="90.3" width="2.44" height="42.2" fill="var(--up)"/>
<line x1="69.8" y1="78.7" x2="69.8" y2="139.5" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="100.1" width="2.44" height="38.8" fill="var(--down)"/>
<line x1="73.8" y1="128.0" x2="73.8" y2="156.4" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="129.0" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="77.7" y1="133.9" x2="77.7" y2="161.7" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="144.9" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="81.7" y1="135.8" x2="81.7" y2="207.7" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="141.2" width="2.44" height="59.8" fill="var(--down)"/>
<line x1="85.6" y1="194.5" x2="85.6" y2="220.4" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="196.0" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="89.5" y1="191.7" x2="89.5" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="211.3" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="93.5" y1="202.2" x2="93.5" y2="223.9" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="214.0" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="97.4" y1="203.5" x2="97.4" y2="229.9" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="208.1" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="101.3" y1="198.5" x2="101.3" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="205.5" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="105.3" y1="179.8" x2="105.3" y2="220.2" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="186.3" width="2.44" height="31.3" fill="var(--up)"/>
<line x1="109.2" y1="162.9" x2="109.2" y2="197.9" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="172.6" width="2.44" height="17.8" fill="var(--up)"/>
<line x1="113.1" y1="149.8" x2="113.1" y2="176.1" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="160.5" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="117.1" y1="157.9" x2="117.1" y2="203.8" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="165.2" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="121.0" y1="138.8" x2="121.0" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="162.9" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="125.0" y1="150.4" x2="125.0" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="157.2" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="128.9" y1="164.6" x2="128.9" y2="229.9" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="172.9" width="2.44" height="49.0" fill="var(--down)"/>
<line x1="132.8" y1="203.2" x2="132.8" y2="252.4" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="210.3" width="2.44" height="39.0" fill="var(--down)"/>
<line x1="136.8" y1="220.2" x2="136.8" y2="266.6" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="242.5" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="140.7" y1="201.6" x2="140.7" y2="255.0" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="209.0" width="2.44" height="46.1" fill="var(--up)"/>
<line x1="144.6" y1="206.0" x2="144.6" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="222.9" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="148.6" y1="221.6" x2="148.6" y2="288.3" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="228.7" width="2.44" height="49.9" fill="var(--down)"/>
<line x1="152.5" y1="228.7" x2="152.5" y2="270.4" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="235.8" width="2.44" height="32.8" fill="var(--up)"/>
<line x1="156.4" y1="210.9" x2="156.4" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="215.0" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="160.4" y1="177.8" x2="160.4" y2="236.6" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="193.1" width="2.44" height="38.1" fill="var(--up)"/>
<line x1="164.3" y1="176.1" x2="164.3" y2="206.4" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="195.7" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="168.3" y1="173.9" x2="168.3" y2="194.5" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="184.1" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="172.2" y1="159.1" x2="172.2" y2="189.0" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="172.9" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="176.1" y1="178.8" x2="176.1" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="178.8" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="180.1" y1="185.5" x2="180.1" y2="218.5" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="189.0" width="2.44" height="27.6" fill="var(--down)"/>
<line x1="184.0" y1="213.2" x2="184.0" y2="273.5" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="233.3" width="2.44" height="27.2" fill="var(--down)"/>
<line x1="187.9" y1="228.3" x2="187.9" y2="295.1" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="264.0" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="191.9" y1="261.1" x2="191.9" y2="303.2" stroke="var(--up)" class="wick"/>
<rect x="190.65" y="270.5" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="195.8" y1="274.3" x2="195.8" y2="315.5" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="278.2" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="199.7" y1="262.6" x2="199.7" y2="307.3" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="267.6" width="2.44" height="30.6" fill="var(--up)"/>
<line x1="203.7" y1="253.7" x2="203.7" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="202.46" y="265.4" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="207.6" y1="258.9" x2="207.6" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="265.5" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="211.6" y1="244.7" x2="211.6" y2="275.6" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="263.5" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="215.5" y1="260.0" x2="215.5" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="266.8" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="219.4" y1="245.2" x2="219.4" y2="285.9" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="245.9" width="2.44" height="20.7" fill="var(--up)"/>
<line x1="223.4" y1="216.7" x2="223.4" y2="245.7" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="234.8" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="227.3" y1="225.6" x2="227.3" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="240.0" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="231.2" y1="251.2" x2="231.2" y2="301.2" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="254.9" width="2.44" height="39.8" fill="var(--down)"/>
<line x1="235.2" y1="280.8" x2="235.2" y2="331.5" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="293.7" width="2.44" height="35.4" fill="var(--down)"/>
<line x1="239.1" y1="332.3" x2="239.1" y2="376.0" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="341.7" width="2.44" height="23.1" fill="var(--down)"/>
<line x1="243.0" y1="351.6" x2="243.0" y2="374.9" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="354.1" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="247.0" y1="322.8" x2="247.0" y2="366.4" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="342.8" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="250.9" y1="299.8" x2="250.9" y2="349.0" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="315.3" width="2.44" height="30.4" fill="var(--up)"/>
<line x1="254.9" y1="301.2" x2="254.9" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="303.6" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="258.8" y1="276.7" x2="258.8" y2="320.7" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="291.8" width="2.44" height="19.2" fill="var(--up)"/>
<line x1="262.7" y1="283.3" x2="262.7" y2="300.7" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="284.1" width="2.44" height="13.7" fill="var(--down)"/>
<line x1="266.7" y1="272.8" x2="266.7" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="276.2" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="270.6" y1="279.1" x2="270.6" y2="303.7" stroke="var(--down)" class="wick"/>
<rect x="269.38" y="287.3" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="274.5" y1="259.8" x2="274.5" y2="312.8" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="288.7" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="278.5" y1="258.6" x2="278.5" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="263.8" width="2.44" height="24.8" fill="var(--up)"/>
<line x1="282.4" y1="243.4" x2="282.4" y2="318.5" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="251.0" width="2.44" height="56.9" fill="var(--down)"/>
<line x1="286.3" y1="276.5" x2="286.3" y2="312.0" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="295.5" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="290.3" y1="288.5" x2="290.3" y2="326.9" stroke="var(--down)" class="wick"/>
<rect x="289.07" y="290.9" width="2.44" height="24.3" fill="var(--down)"/>
<line x1="294.2" y1="309.5" x2="294.2" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="321.8" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="298.2" y1="297.7" x2="298.2" y2="326.5" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="321.3" width="2.44" height="3.0" fill="var(--up)"/>
<line x1="302.1" y1="219.7" x2="302.1" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="226.5" width="2.44" height="79.6" fill="var(--up)"/>
<line x1="306.0" y1="186.6" x2="306.0" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="193.5" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="310.0" y1="188.2" x2="310.0" y2="211.9" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="189.8" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="313.9" y1="197.1" x2="313.9" y2="230.0" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="198.2" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="317.8" y1="194.1" x2="317.8" y2="225.8" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="218.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="321.8" y1="204.3" x2="321.8" y2="227.8" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="215.6" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="325.7" y1="189.6" x2="325.7" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="192.3" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="329.7" y1="164.4" x2="329.7" y2="197.1" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="178.9" width="2.44" height="13.4" fill="var(--up)"/>
<line x1="333.6" y1="155.6" x2="333.6" y2="178.7" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="176.4" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="337.5" y1="153.4" x2="337.5" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="164.4" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="341.5" y1="157.6" x2="341.5" y2="167.4" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="163.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="345.4" y1="154.6" x2="345.4" y2="172.3" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="163.8" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="349.3" y1="170.9" x2="349.3" y2="184.5" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="172.2" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="353.3" y1="170.1" x2="353.3" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="175.6" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="357.2" y1="197.5" x2="357.2" y2="241.5" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="198.2" width="2.44" height="29.3" fill="var(--down)"/>
<line x1="361.1" y1="176.7" x2="361.1" y2="245.5" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="206.4" width="2.44" height="34.6" fill="var(--up)"/>
<line x1="365.1" y1="157.0" x2="365.1" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="161.0" width="2.44" height="43.8" fill="var(--up)"/>
<line x1="369.0" y1="141.9" x2="369.0" y2="171.5" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="162.6" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="373.0" y1="124.9" x2="373.0" y2="187.4" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="162.0" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="376.9" y1="157.2" x2="376.9" y2="180.3" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="169.6" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="380.8" y1="209.1" x2="380.8" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="215.3" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="384.8" y1="243.6" x2="384.8" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="243.6" width="2.44" height="53.9" fill="var(--down)"/>
<line x1="388.7" y1="283.7" x2="388.7" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="290.5" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="392.6" y1="278.7" x2="392.6" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="283.9" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="396.6" y1="301.3" x2="396.6" y2="321.9" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="315.9" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="400.5" y1="330.7" x2="400.5" y2="361.2" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="348.8" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="404.4" y1="326.9" x2="404.4" y2="375.7" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="341.9" width="2.44" height="23.0" fill="var(--down)"/>
<line x1="408.4" y1="343.2" x2="408.4" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="344.4" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="412.3" y1="347.2" x2="412.3" y2="393.5" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="350.0" width="2.44" height="25.8" fill="var(--down)"/>
<line x1="416.3" y1="354.0" x2="416.3" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="365.7" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="420.2" y1="358.9" x2="420.2" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="364.6" width="2.44" height="28.0" fill="var(--down)"/>
<line x1="424.1" y1="379.3" x2="424.1" y2="400.8" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="386.6" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="428.1" y1="300.5" x2="428.1" y2="393.7" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="302.4" width="2.44" height="46.1" fill="var(--up)"/>
<line x1="432.0" y1="302.3" x2="432.0" y2="335.3" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="312.9" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="435.9" y1="250.7" x2="435.9" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="257.5" width="2.44" height="55.6" fill="var(--up)"/>
<line x1="439.9" y1="239.1" x2="439.9" y2="282.0" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="261.5" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="443.8" y1="252.7" x2="443.8" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="264.6" width="2.44" height="14.6" fill="var(--up)"/>
<line x1="447.7" y1="232.1" x2="447.7" y2="278.4" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="259.5" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="451.7" y1="252.0" x2="451.7" y2="317.6" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="266.3" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="455.6" y1="291.5" x2="455.6" y2="339.3" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="302.5" width="2.44" height="32.4" fill="var(--down)"/>
<line x1="459.6" y1="289.8" x2="459.6" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="315.3" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="463.5" y1="314.1" x2="463.5" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="324.0" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="467.4" y1="305.3" x2="467.4" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="317.1" width="2.44" height="48.2" fill="var(--down)"/>
<line x1="471.4" y1="340.1" x2="471.4" y2="409.5" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="359.1" width="2.44" height="41.3" fill="var(--down)"/>
<line x1="475.3" y1="371.5" x2="475.3" y2="413.5" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="386.7" width="2.44" height="26.8" fill="var(--up)"/>
<line x1="479.2" y1="352.6" x2="479.2" y2="396.5" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="363.3" width="2.44" height="21.2" fill="var(--up)"/>
<line x1="483.2" y1="368.9" x2="483.2" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="375.5" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="487.1" y1="365.2" x2="487.1" y2="399.6" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="369.4" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="491.0" y1="383.6" x2="491.0" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="392.3" width="2.44" height="94.4" fill="var(--down)"/>
<line x1="495.0" y1="474.3" x2="495.0" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="479.2" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="498.9" y1="430.7" x2="498.9" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="435.1" width="2.44" height="25.4" fill="var(--up)"/>
<line x1="502.9" y1="394.5" x2="502.9" y2="436.6" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="414.3" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="506.8" y1="398.9" x2="506.8" y2="445.3" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="404.9" width="2.44" height="29.9" fill="var(--up)"/>
<line x1="510.7" y1="370.3" x2="510.7" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="390.3" width="2.44" height="44.5" fill="var(--up)"/>
<line x1="514.7" y1="367.9" x2="514.7" y2="421.2" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="377.4" width="2.44" height="41.4" fill="var(--up)"/>
<line x1="518.6" y1="370.3" x2="518.6" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="378.1" width="2.44" height="4.8" fill="var(--down)"/>
<line x1="522.5" y1="373.6" x2="522.5" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="376.1" width="2.44" height="13.8" fill="var(--up)"/>
<line x1="526.5" y1="384.3" x2="526.5" y2="424.3" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="385.1" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="530.4" y1="390.7" x2="530.4" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="402.9" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="534.3" y1="396.7" x2="534.3" y2="428.9" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="405.9" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="538.3" y1="412.3" x2="538.3" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="420.9" width="2.44" height="35.1" fill="var(--down)"/>
<line x1="542.2" y1="449.7" x2="542.2" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="471.4" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="546.2" y1="464.2" x2="546.2" y2="489.2" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="479.2" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="550.1" y1="438.3" x2="550.1" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="438.6" width="2.44" height="38.2" fill="var(--up)"/>
<line x1="554.0" y1="405.9" x2="554.0" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="430.7" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="558.0" y1="456.9" x2="558.0" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="456.9" width="2.44" height="59.0" fill="var(--down)"/>
<line x1="561.9" y1="482.7" x2="561.9" y2="520.5" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="505.7" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="565.8" y1="474.4" x2="565.8" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="485.6" width="2.44" height="14.9" fill="var(--up)"/>
<line x1="569.8" y1="444.2" x2="569.8" y2="470.0" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="448.0" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="573.7" y1="460.9" x2="573.7" y2="497.5" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="475.6" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="577.7" y1="447.3" x2="577.7" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="460.8" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="581.6" y1="452.9" x2="581.6" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="468.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="585.5" y1="471.2" x2="585.5" y2="546.8" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="473.5" width="2.44" height="58.8" fill="var(--down)"/>
<line x1="589.5" y1="488.7" x2="589.5" y2="521.7" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="494.6" width="2.44" height="23.1" fill="var(--up)"/>
<line x1="593.4" y1="466.0" x2="593.4" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="471.4" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="597.3" y1="459.8" x2="597.3" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="462.8" width="2.44" height="40.9" fill="var(--down)"/>
<line x1="601.3" y1="471.9" x2="601.3" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="496.8" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="605.2" y1="464.0" x2="605.2" y2="505.5" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="465.6" width="2.44" height="29.9" fill="var(--up)"/>
<line x1="609.1" y1="461.4" x2="609.1" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="478.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="613.1" y1="425.7" x2="613.1" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="440.5" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="617.0" y1="445.6" x2="617.0" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="454.2" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="621.0" y1="454.5" x2="621.0" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="463.7" width="2.44" height="12.9" fill="var(--down)"/>
<line x1="624.9" y1="437.1" x2="624.9" y2="490.7" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="438.3" width="2.44" height="47.7" fill="var(--up)"/>
<line x1="628.8" y1="417.4" x2="628.8" y2="445.6" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="420.6" width="2.44" height="19.9" fill="var(--up)"/>
<line x1="632.8" y1="384.7" x2="632.8" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="394.3" width="2.44" height="15.3" fill="var(--up)"/>
<line x1="636.7" y1="385.5" x2="636.7" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="399.8" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="640.6" y1="365.3" x2="640.6" y2="399.0" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="388.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="644.6" y1="376.8" x2="644.6" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="391.2" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="648.5" y1="382.1" x2="648.5" y2="432.1" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="406.0" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="652.4" y1="418.1" x2="652.4" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="424.8" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="656.4" y1="434.1" x2="656.4" y2="477.7" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="442.9" width="2.44" height="19.3" fill="var(--down)"/>
<line x1="660.3" y1="449.7" x2="660.3" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="455.3" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="664.3" y1="436.5" x2="664.3" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="446.6" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="668.2" y1="405.7" x2="668.2" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="424.1" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="672.1" y1="339.2" x2="672.1" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="355.5" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="676.1" y1="416.7" x2="676.1" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="454.0" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="680.0" y1="436.6" x2="680.0" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="448.2" width="2.44" height="40.7" fill="var(--down)"/>
<line x1="683.9" y1="443.3" x2="683.9" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="682.72" y="453.1" width="2.44" height="37.6" fill="var(--up)"/>
<line x1="687.9" y1="456.4" x2="687.9" y2="497.5" stroke="var(--down)" class="wick"/>
<rect x="686.65" y="467.4" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="691.8" y1="468.6" x2="691.8" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="474.7" width="2.44" height="28.0" fill="var(--down)"/>
<line x1="695.7" y1="457.8" x2="695.7" y2="499.6" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="467.8" width="2.44" height="31.8" fill="var(--up)"/>
<line x1="699.7" y1="469.8" x2="699.7" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="470.9" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="703.6" y1="465.0" x2="703.6" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="479.9" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="707.6" y1="447.0" x2="707.6" y2="472.4" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="469.1" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="711.5" y1="476.8" x2="711.5" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="488.4" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="715.4" y1="492.7" x2="715.4" y2="517.8" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="505.1" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="719.4" y1="462.6" x2="719.4" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="493.8" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="723.3" y1="447.3" x2="723.3" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="449.0" width="2.44" height="55.3" fill="var(--up)"/>
<line x1="727.2" y1="421.6" x2="727.2" y2="477.2" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="442.2" width="2.44" height="30.4" fill="var(--down)"/>
<line x1="731.2" y1="472.6" x2="731.2" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="729.95" y="479.0" width="2.44" height="17.5" fill="var(--up)"/>
<line x1="735.1" y1="466.1" x2="735.1" y2="509.8" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="472.9" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="739.0" y1="455.0" x2="739.0" y2="481.8" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="474.9" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="743.0" y1="483.6" x2="743.0" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="486.9" width="2.44" height="11.6" fill="var(--down)"/>
<line x1="746.9" y1="473.9" x2="746.9" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="490.6" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="750.9" y1="492.4" x2="750.9" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="495.6" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="754.8" y1="471.0" x2="754.8" y2="499.1" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="492.7" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="758.7" y1="482.5" x2="758.7" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="757.51" y="489.8" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="762.7" y1="494.6" x2="762.7" y2="557.7" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="498.2" width="2.44" height="59.4" fill="var(--down)"/>
<line x1="766.6" y1="541.1" x2="766.6" y2="608.5" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="559.0" width="2.44" height="22.4" fill="var(--down)"/>
<line x1="770.5" y1="515.7" x2="770.5" y2="558.5" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="541.9" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="774.5" y1="494.6" x2="774.5" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="505.9" width="2.44" height="27.4" fill="var(--up)"/>
<line x1="778.4" y1="511.9" x2="778.4" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="522.6" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="782.3" y1="489.1" x2="782.3" y2="541.0" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="489.8" width="2.44" height="43.9" fill="var(--up)"/>
<line x1="786.3" y1="476.1" x2="786.3" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="481.2" width="2.44" height="32.4" fill="var(--down)"/>
<line x1="790.2" y1="504.4" x2="790.2" y2="531.7" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="515.2" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="794.2" y1="500.9" x2="794.2" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="510.1" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="798.1" y1="496.3" x2="798.1" y2="523.0" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="507.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="802.0" y1="465.6" x2="802.0" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="466.3" width="2.44" height="36.6" fill="var(--up)"/>
<line x1="806.0" y1="453.5" x2="806.0" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="460.1" width="2.44" height="38.4" fill="var(--down)"/>
<line x1="809.9" y1="486.9" x2="809.9" y2="514.3" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="491.6" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="813.8" y1="488.2" x2="813.8" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="517.2" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="817.8" y1="504.0" x2="817.8" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="514.6" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="821.7" y1="477.5" x2="821.7" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="493.0" width="2.44" height="24.5" fill="var(--up)"/>
<line x1="825.7" y1="452.9" x2="825.7" y2="515.3" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="486.9" width="2.44" height="27.4" fill="var(--down)"/>
<line x1="829.6" y1="454.6" x2="829.6" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="475.2" width="2.44" height="40.3" fill="var(--up)"/>
<line x1="833.5" y1="411.7" x2="833.5" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="434.2" width="2.44" height="27.6" fill="var(--up)"/>
<line x1="837.5" y1="417.3" x2="837.5" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="418.9" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="841.4" y1="353.9" x2="841.4" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="384.7" width="2.44" height="20.1" fill="var(--up)"/>
<line x1="845.3" y1="318.3" x2="845.3" y2="370.7" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="319.2" width="2.44" height="37.3" fill="var(--up)"/>
<line x1="849.3" y1="309.5" x2="849.3" y2="383.8" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="314.0" width="2.44" height="29.5" fill="var(--down)"/>
<line x1="853.2" y1="302.7" x2="853.2" y2="355.5" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="340.7" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="857.1" y1="349.2" x2="857.1" y2="404.9" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="351.2" width="2.44" height="43.5" fill="var(--down)"/>
<line x1="861.1" y1="381.7" x2="861.1" y2="413.0" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="381.8" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="865.0" y1="359.6" x2="865.0" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="366.1" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="869.0" y1="317.1" x2="869.0" y2="352.7" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="325.7" width="2.44" height="27.0" fill="var(--up)"/>
<line x1="872.9" y1="303.5" x2="872.9" y2="347.5" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="324.5" width="2.44" height="11.7" fill="var(--up)"/>
<line x1="876.8" y1="312.1" x2="876.8" y2="359.0" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="322.5" width="2.44" height="12.9" fill="var(--down)"/>
<line x1="880.8" y1="271.7" x2="880.8" y2="318.0" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="272.3" width="2.44" height="38.8" fill="var(--up)"/>
<line x1="884.7" y1="271.6" x2="884.7" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="276.3" width="2.44" height="26.7" fill="var(--down)"/>
<line x1="888.6" y1="286.3" x2="888.6" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="288.1" width="2.44" height="28.8" fill="var(--up)"/>
<line x1="892.6" y1="300.1" x2="892.6" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="302.3" width="2.44" height="21.1" fill="var(--down)"/>
<line x1="896.5" y1="316.8" x2="896.5" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="320.9" width="2.44" height="26.9" fill="var(--down)"/>
<line x1="900.4" y1="352.1" x2="900.4" y2="380.2" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="354.4" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="904.4" y1="316.8" x2="904.4" y2="356.7" stroke="var(--up)" class="wick"/>
<rect x="903.16" y="318.2" width="2.44" height="31.7" fill="var(--up)"/>
<line x1="908.3" y1="263.2" x2="908.3" y2="309.0" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="271.6" width="2.44" height="33.0" fill="var(--up)"/>
<line x1="912.3" y1="221.7" x2="912.3" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="911.03" y="228.9" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="916.2" y1="201.0" x2="916.2" y2="259.2" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="226.7" width="2.44" height="31.9" fill="var(--up)"/>
<line x1="920.1" y1="152.1" x2="920.1" y2="210.1" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="172.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="924.1" y1="180.0" x2="924.1" y2="226.3" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="188.9" width="2.44" height="20.9" fill="var(--up)"/>
<line x1="928.0" y1="147.9" x2="928.0" y2="197.9" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="162.3" width="2.44" height="34.9" fill="var(--down)"/>
<line x1="931.9" y1="188.0" x2="931.9" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="930.72" y="196.7" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="935.9" y1="169.0" x2="935.9" y2="206.3" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="178.7" width="2.44" height="20.3" fill="var(--down)"/>
<line x1="939.8" y1="176.3" x2="939.8" y2="214.9" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="177.9" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="943.7" y1="189.4" x2="943.7" y2="233.3" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="191.0" width="2.44" height="37.2" fill="var(--down)"/>
<line x1="947.7" y1="213.4" x2="947.7" y2="242.0" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="227.3" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="951.6" y1="210.1" x2="951.6" y2="239.6" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="229.1" width="2.44" height="4.9" fill="var(--down)"/>
<line x1="955.6" y1="225.8" x2="955.6" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="240.6" width="2.44" height="8.4" fill="var(--up)"/>
<line x1="959.5" y1="207.6" x2="959.5" y2="248.4" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="212.4" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="963.4" y1="198.3" x2="963.4" y2="222.4" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="203.7" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="967.4" y1="203.7" x2="967.4" y2="234.7" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="219.3" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="971.3" y1="168.1" x2="971.3" y2="227.3" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="184.3" width="2.44" height="40.3" fill="var(--up)"/>
<line x1="975.2" y1="150.9" x2="975.2" y2="199.6" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="186.5" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="979.2" y1="163.8" x2="979.2" y2="194.0" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="186.0" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="983.1" y1="153.5" x2="983.1" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="159.8" width="2.44" height="23.5" fill="var(--up)"/>
<line x1="987.0" y1="85.0" x2="987.0" y2="146.0" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="85.5" width="2.44" height="57.4" fill="var(--up)"/>
<line x1="991.0" y1="80.2" x2="991.0" y2="103.0" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="87.4" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="994.9" y1="83.1" x2="994.9" y2="105.4" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="87.4" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="998.9" y1="108.1" x2="998.9" y2="130.9" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="109.1" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="1002.8" y1="92.6" x2="1002.8" y2="115.6" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="103.1" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="1006.7" y1="103.6" x2="1006.7" y2="129.9" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="109.9" width="2.44" height="16.3" fill="var(--down)"/>
<line x1="1010.7" y1="113.4" x2="1010.7" y2="158.9" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="125.0" width="2.44" height="33.0" fill="var(--down)"/>
<line x1="1014.6" y1="120.9" x2="1014.6" y2="148.0" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="130.8" width="2.44" height="16.0" fill="var(--up)"/>
<line x1="1018.5" y1="112.1" x2="1018.5" y2="147.5" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="121.0" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="1022.5" y1="144.9" x2="1022.5" y2="167.3" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="159.5" width="2.44" height="5.9" fill="var(--down)"/>
<line x1="1026.4" y1="179.0" x2="1026.4" y2="212.5" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="190.6" width="2.44" height="6.9" fill="var(--down)"/>
<line x1="1030.3" y1="197.7" x2="1030.3" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="204.8" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="1034.3" y1="205.8" x2="1034.3" y2="227.3" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="218.8" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="1038.2" y1="190.6" x2="1038.2" y2="223.1" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="204.0" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="1042.2" y1="166.5" x2="1042.2" y2="216.5" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="177.8" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="1046.1" y1="185.5" x2="1046.1" y2="211.3" stroke="var(--up)" class="wick"/>
<rect x="1044.87" y="188.3" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="1050.0" y1="189.2" x2="1050.0" y2="210.2" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="194.8" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="60" y1="169.9" x2="1052" y2="169.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="173.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$578 R1</text>
<text x="1058" y="185.4" font-size="9.5" fill="var(--muted)">터치 8회</text>
<line x1="60" y1="242.3" x2="1052" y2="242.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="236.3" font-size="11.5" fill="var(--support)" font-weight="600">$559 S1</text>
<text x="1058" y="248.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="312.1" x2="1052" y2="312.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.1" font-size="11.5" fill="var(--support)" font-weight="600">$541 S2</text>
<text x="1058" y="318.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="385.7" x2="1052" y2="385.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="379.7" font-size="11.5" fill="var(--support)" font-weight="600">$522 S3</text>
<text x="1058" y="391.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="197.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="189.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $571 (2026-09-16)</text>
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
| R1 | $578 | **8** | 2025-10-07·10-24·11-12·12-12·12-24·2026-01-08·02-05·08-03 — **터치 8회로 이 저장소에서 보기 드물게 강한 저항**이다. 1년에 걸쳐 여덟 번 닿고 여덟 번 막혔다 |
| **현재가** | **$573.27** (2026-09-15 종가) | — | **R1 바로 아래(−0.8%)**. 52주 최고 $601.62 대비 −4.7% |
| S1 | $559 | 2 | 2025-09-29·2026-08-12 |
| S2 | $541 | 3 | 2025-10-16·11-03·12-09 — 2025년 가을 지지대 |
| S3 | $522 | 3 | 2025-11-18·2026-01-28·07-23 |
| 참고선 | $601.62 | — | 52주 최고. R1 위의 단발 고점이라 클러스터를 이루지 못했다 |
| 참고선 | $464.52 | — | 52주 최저 |

**이 표에서 압도적으로 중요한 것은 R1($578)의 터치 8회**다. 2025년 10월부터 2026년 8월까지 열 달에 걸쳐 여덟 번 이 가격대에 닿았고 매번 되돌려졌다 — 주가가 1년 내내 $522~$578의 좁은 박스에 갇혀 있었다는 뜻이다. 현재가 $573.27은 그 상단에서 **0.8% 아래**다.

**이 구조는 [밸류에이션](./06_valuation.md)의 결론과 방향이 엇갈린다** — 밸류에이션으로는 FY2026(E) 적정주가 대비 −4.1%로 저평가에 가깝지만, 가격 흐름은 1년째 상단 저항에 막혀 있다. 동종사 [Visa](../visa/09_technical_daily.md)가 저항 없는 신고가 구간인 것과 정반대이며, **두 회사의 기술적 위치와 가치 판단이 서로 교차한다**는 점이 이 섹터를 볼 때 흥미로운 대목이다.

---


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-16~2026-09-16. 수집 시점: 2026-09-17. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py MA --name "Mastercard" --close-on 2026-09-15 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - ⚠️ **마지막 캔들은 2026-09-16 장중 미완성 봉이다.** 이 스크립트는 시계열 종료일을 고정하는 인자가 없어 항상 가장 최근 봉까지 그리며, `--close-on`은 시계열을 자르지 않고 대조용 종가 주석만 덧붙인다. 생성 시점이 미 증시 정규장 중이었으므로 차트 우측 끝 캔들의 종가는 확정값이 아니다 — **§2 현재가 행과 다른 문서의 기준 종가는 마지막 완료 거래일 2026-09-15를 쓴다.** 마지막 봉은 스윙 탐지에 전후 구간이 필요해 레벨 계산에는 영향을 주지 않는다.
    - **터치 8회의 R1은 이 모델 기준으로는 강한 레벨이지만, 그것이 미래의 돌파 실패를 뜻하지는 않는다.** 반복 터치는 그 가격대에 매물이 쌓여 있었다는 과거 사실일 뿐이다.
    - 원주가 기준이라 **배당은 반영되지 않았다**(기간 내 배당 4회).
    - 최근 1년 구간에 주식분할은 없다.

---

*작성일: 2026-09-17*
