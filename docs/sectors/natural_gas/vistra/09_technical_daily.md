# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL)와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-04 종가 $149.30은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.** 세 문서가 같은 기준일·같은 종가를 쓴다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="vst-chart">
<style>
.vst-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .vst-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .vst-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.vst-chart svg { width:100%; height:auto; display:block; }
.vst-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.vst-chart .title { fill: var(--ink); font-weight:600; }
.vst-chart .grid { stroke: var(--grid); stroke-width:1; }
.vst-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vistra(VST) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Vistra (VST) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $149.30 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="565.4" x2="1052" y2="565.4" class="grid"/>
<text x="52" y="569.4" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="444.1" x2="1052" y2="444.1" class="grid"/>
<text x="52" y="448.1" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="322.8" x2="1052" y2="322.8" class="grid"/>
<text x="52" y="326.8" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="60" y1="201.5" x2="1052" y2="201.5" class="grid"/>
<text x="52" y="205.5" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="80.3" x2="1052" y2="80.3" class="grid"/>
<text x="52" y="84.3" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
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
<line x1="62.0" y1="253.5" x2="62.0" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="260.7" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="65.9" y1="258.8" x2="65.9" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="264.7" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="69.8" y1="228.8" x2="69.8" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="68.62" y="239.2" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="73.8" y1="123.4" x2="73.8" y2="201.5" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="145.7" width="2.44" height="52.7" fill="var(--up)"/>
<line x1="77.7" y1="129.4" x2="77.7" y2="182.7" stroke="var(--down)" class="wick"/>
<rect x="76.49" y="148.3" width="2.44" height="28.7" fill="var(--down)"/>
<line x1="81.7" y1="139.6" x2="81.7" y2="189.3" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="142.7" width="2.44" height="41.1" fill="var(--up)"/>
<line x1="85.6" y1="93.0" x2="85.6" y2="142.7" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="119.5" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="89.5" y1="117.9" x2="89.5" y2="157.2" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="117.9" width="2.44" height="26.5" fill="var(--down)"/>
<line x1="93.5" y1="117.9" x2="93.5" y2="173.2" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="133.0" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="97.4" y1="113.8" x2="97.4" y2="152.7" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="120.8" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="101.3" y1="117.6" x2="101.3" y2="170.1" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="132.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="105.3" y1="81.3" x2="105.3" y2="154.2" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="92.9" width="2.44" height="42.0" fill="var(--up)"/>
<line x1="109.2" y1="124.1" x2="109.2" y2="180.6" stroke="var(--down)" class="wick"/>
<rect x="107.99" y="140.2" width="2.44" height="35.6" fill="var(--down)"/>
<line x1="113.1" y1="164.0" x2="113.1" y2="190.2" stroke="var(--down)" class="wick"/>
<rect x="111.92" y="181.8" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="117.1" y1="175.7" x2="117.1" y2="225.7" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="191.7" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="121.0" y1="156.1" x2="121.0" y2="195.6" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="157.8" width="2.44" height="36.5" fill="var(--up)"/>
<line x1="125.0" y1="158.3" x2="125.0" y2="215.5" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="189.4" width="2.44" height="24.6" fill="var(--down)"/>
<line x1="128.9" y1="198.5" x2="128.9" y2="257.9" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="206.4" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="132.8" y1="171.6" x2="132.8" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="192.4" width="2.44" height="39.5" fill="var(--up)"/>
<line x1="136.8" y1="171.2" x2="136.8" y2="209.4" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="177.0" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="140.7" y1="139.7" x2="140.7" y2="192.4" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="175.2" width="2.44" height="14.3" fill="var(--down)"/>
<line x1="144.6" y1="153.4" x2="144.6" y2="217.1" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="164.2" width="2.44" height="34.9" fill="var(--down)"/>
<line x1="148.6" y1="178.3" x2="148.6" y2="226.5" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="192.0" width="2.44" height="11.8" fill="var(--down)"/>
<line x1="152.5" y1="161.4" x2="152.5" y2="200.8" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="161.8" width="2.44" height="30.1" fill="var(--up)"/>
<line x1="156.4" y1="134.4" x2="156.4" y2="169.2" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="140.9" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="160.4" y1="126.5" x2="160.4" y2="220.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="142.3" width="2.44" height="78.2" fill="var(--down)"/>
<line x1="164.3" y1="141.2" x2="164.3" y2="199.1" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="143.6" width="2.44" height="51.1" fill="var(--up)"/>
<line x1="168.3" y1="147.9" x2="168.3" y2="193.0" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="166.4" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="172.2" y1="104.3" x2="172.2" y2="162.7" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="135.7" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="176.1" y1="97.8" x2="176.1" y2="148.9" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="111.8" width="2.44" height="26.6" fill="var(--down)"/>
<line x1="180.1" y1="140.6" x2="180.1" y2="201.2" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="155.0" width="2.44" height="38.3" fill="var(--down)"/>
<line x1="184.0" y1="168.2" x2="184.0" y2="245.1" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="176.5" width="2.44" height="60.0" fill="var(--down)"/>
<line x1="187.9" y1="241.4" x2="187.9" y2="289.0" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="244.7" width="2.44" height="38.6" fill="var(--down)"/>
<line x1="191.9" y1="265.2" x2="191.9" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="277.0" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="195.8" y1="248.8" x2="195.8" y2="288.2" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="253.9" width="2.44" height="34.3" fill="var(--up)"/>
<line x1="199.7" y1="189.4" x2="199.7" y2="234.3" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="192.6" width="2.44" height="29.5" fill="var(--up)"/>
<line x1="203.7" y1="179.3" x2="203.7" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="179.3" width="2.44" height="26.4" fill="var(--down)"/>
<line x1="207.6" y1="217.8" x2="207.6" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="217.8" width="2.44" height="40.8" fill="var(--down)"/>
<line x1="211.6" y1="197.1" x2="211.6" y2="265.4" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="205.4" width="2.44" height="42.9" fill="var(--up)"/>
<line x1="215.5" y1="208.7" x2="215.5" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="233.8" width="2.44" height="30.1" fill="var(--down)"/>
<line x1="219.4" y1="244.6" x2="219.4" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="250.0" width="2.44" height="22.4" fill="var(--down)"/>
<line x1="223.4" y1="230.7" x2="223.4" y2="275.2" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="243.7" width="2.44" height="13.5" fill="var(--up)"/>
<line x1="227.3" y1="253.1" x2="227.3" y2="295.5" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="273.7" width="2.44" height="14.3" fill="var(--down)"/>
<line x1="231.2" y1="247.2" x2="231.2" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="265.9" width="2.44" height="19.0" fill="var(--up)"/>
<line x1="235.2" y1="267.5" x2="235.2" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="233.95" y="294.8" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="239.1" y1="255.7" x2="239.1" y2="343.4" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="256.1" width="2.44" height="75.8" fill="var(--up)"/>
<line x1="243.0" y1="220.9" x2="243.0" y2="297.6" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="233.1" width="2.44" height="39.5" fill="var(--down)"/>
<line x1="247.0" y1="274.7" x2="247.0" y2="330.0" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="286.9" width="2.44" height="41.0" fill="var(--down)"/>
<line x1="250.9" y1="314.9" x2="250.9" y2="339.2" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="320.8" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="254.9" y1="335.2" x2="254.9" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="341.5" width="2.44" height="32.4" fill="var(--down)"/>
<line x1="258.8" y1="322.8" x2="258.8" y2="410.2" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="355.0" width="2.44" height="45.5" fill="var(--up)"/>
<line x1="262.7" y1="325.7" x2="262.7" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="350.5" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="266.7" y1="338.5" x2="266.7" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="356.6" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="270.6" y1="313.7" x2="270.6" y2="357.9" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="328.0" width="2.44" height="24.1" fill="var(--up)"/>
<line x1="274.5" y1="266.5" x2="274.5" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="293.6" width="2.44" height="66.9" fill="var(--down)"/>
<line x1="278.5" y1="361.1" x2="278.5" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="371.3" width="2.44" height="20.7" fill="var(--down)"/>
<line x1="282.4" y1="351.9" x2="282.4" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="352.3" width="2.44" height="33.8" fill="var(--up)"/>
<line x1="286.3" y1="354.8" x2="286.3" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="358.7" width="2.44" height="19.6" fill="var(--down)"/>
<line x1="290.3" y1="336.5" x2="290.3" y2="364.7" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="342.2" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="294.2" y1="318.1" x2="294.2" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="328.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="298.2" y1="344.2" x2="298.2" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="347.0" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="302.1" y1="347.4" x2="302.1" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="350.7" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="306.0" y1="360.1" x2="306.0" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="367.3" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="310.0" y1="334.6" x2="310.0" y2="380.6" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="346.6" width="2.44" height="25.3" fill="var(--up)"/>
<line x1="313.9" y1="343.2" x2="313.9" y2="404.9" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="343.9" width="2.44" height="56.7" fill="var(--down)"/>
<line x1="317.8" y1="396.7" x2="317.8" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="396.7" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="321.8" y1="384.0" x2="321.8" y2="415.4" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="411.5" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="325.7" y1="407.6" x2="325.7" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="411.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="329.7" y1="353.8" x2="329.7" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="355.6" width="2.44" height="76.1" fill="var(--up)"/>
<line x1="333.6" y1="322.8" x2="333.6" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="351.9" width="2.44" height="30.9" fill="var(--down)"/>
<line x1="337.5" y1="365.3" x2="337.5" y2="401.8" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="365.5" width="2.44" height="28.6" fill="var(--down)"/>
<line x1="341.5" y1="359.6" x2="341.5" y2="404.4" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="362.5" width="2.44" height="41.2" fill="var(--up)"/>
<line x1="345.4" y1="352.3" x2="345.4" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="359.1" width="2.44" height="85.1" fill="var(--down)"/>
<line x1="349.3" y1="371.8" x2="349.3" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="406.7" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="353.3" y1="374.9" x2="353.3" y2="427.7" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="403.5" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="357.2" y1="418.0" x2="357.2" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="419.8" width="2.44" height="14.7" fill="var(--down)"/>
<line x1="361.1" y1="421.6" x2="361.1" y2="443.3" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="434.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="365.1" y1="428.4" x2="365.1" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="432.2" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="369.0" y1="425.9" x2="369.0" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="434.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="373.0" y1="418.6" x2="373.0" y2="444.5" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="432.9" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="376.9" y1="425.5" x2="376.9" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="428.2" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="380.8" y1="416.8" x2="380.8" y2="436.7" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="426.6" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="384.8" y1="387.8" x2="384.8" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="412.4" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="388.7" y1="373.4" x2="388.7" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="387.3" width="2.44" height="39.1" fill="var(--down)"/>
<line x1="392.6" y1="367.6" x2="392.6" y2="421.2" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="386.3" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="396.6" y1="391.6" x2="396.6" y2="483.3" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="391.6" width="2.44" height="85.2" fill="var(--down)"/>
<line x1="400.5" y1="469.6" x2="400.5" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="472.9" width="2.44" height="28.2" fill="var(--down)"/>
<line x1="404.4" y1="354.7" x2="404.4" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="357.2" width="2.44" height="48.3" fill="var(--down)"/>
<line x1="408.4" y1="342.6" x2="408.4" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="367.8" width="2.44" height="48.0" fill="var(--up)"/>
<line x1="412.3" y1="350.4" x2="412.3" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="359.2" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="416.3" y1="376.3" x2="416.3" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="387.1" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="420.2" y1="307.3" x2="420.2" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="321.7" width="2.44" height="43.5" fill="var(--up)"/>
<line x1="424.1" y1="376.7" x2="424.1" y2="425.8" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="398.3" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="428.1" y1="407.7" x2="428.1" y2="466.8" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="436.4" width="2.44" height="27.0" fill="var(--down)"/>
<line x1="432.0" y1="432.1" x2="432.0" y2="481.9" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="444.0" width="2.44" height="6.1" fill="var(--up)"/>
<line x1="435.9" y1="422.9" x2="435.9" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="432.4" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="439.9" y1="426.7" x2="439.9" y2="456.2" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="443.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="443.8" y1="411.9" x2="443.8" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="440.5" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="447.7" y1="416.1" x2="447.7" y2="455.3" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="418.3" width="2.44" height="28.8" fill="var(--up)"/>
<line x1="451.7" y1="404.3" x2="451.7" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="407.7" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="455.6" y1="396.3" x2="455.6" y2="451.6" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="407.9" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="459.6" y1="416.8" x2="459.6" y2="463.1" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="435.0" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="463.5" y1="444.2" x2="463.5" y2="480.3" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="458.3" width="2.44" height="20.6" fill="var(--down)"/>
<line x1="467.4" y1="465.3" x2="467.4" y2="502.3" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="467.6" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="471.4" y1="482.5" x2="471.4" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="485.4" width="2.44" height="64.7" fill="var(--down)"/>
<line x1="475.3" y1="541.7" x2="475.3" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="546.7" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="479.2" y1="491.0" x2="479.2" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="504.7" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="483.2" y1="469.7" x2="483.2" y2="518.2" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="486.7" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="487.1" y1="435.5" x2="487.1" y2="475.6" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="441.7" width="2.44" height="4.9" fill="var(--down)"/>
<line x1="491.0" y1="411.9" x2="491.0" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="413.8" width="2.44" height="29.4" fill="var(--down)"/>
<line x1="495.0" y1="406.4" x2="495.0" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="425.3" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="498.9" y1="373.4" x2="498.9" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="374.4" width="2.44" height="55.1" fill="var(--up)"/>
<line x1="502.9" y1="343.1" x2="502.9" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="361.1" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="506.8" y1="350.1" x2="506.8" y2="385.8" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="359.1" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="510.7" y1="367.9" x2="510.7" y2="394.1" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="368.3" width="2.44" height="15.7" fill="var(--up)"/>
<line x1="514.7" y1="362.2" x2="514.7" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="513.45" y="369.5" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="518.6" y1="372.3" x2="518.6" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="379.6" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="522.5" y1="373.3" x2="522.5" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="373.6" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="526.5" y1="347.4" x2="526.5" y2="383.0" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="350.9" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="530.4" y1="339.6" x2="530.4" y2="419.2" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="342.1" width="2.44" height="33.1" fill="var(--up)"/>
<line x1="534.3" y1="333.1" x2="534.3" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="353.1" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="538.3" y1="343.9" x2="538.3" y2="408.7" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="382.2" width="2.44" height="25.5" fill="var(--down)"/>
<line x1="542.2" y1="422.7" x2="542.2" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="433.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="546.2" y1="418.6" x2="546.2" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="423.7" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="550.1" y1="395.8" x2="550.1" y2="433.9" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="399.2" width="2.44" height="33.5" fill="var(--up)"/>
<line x1="554.0" y1="393.3" x2="554.0" y2="454.4" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="417.1" width="2.44" height="35.2" fill="var(--down)"/>
<line x1="558.0" y1="416.0" x2="558.0" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="422.1" width="2.44" height="46.8" fill="var(--up)"/>
<line x1="561.9" y1="390.8" x2="561.9" y2="418.0" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="411.6" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="565.8" y1="419.9" x2="565.8" y2="473.5" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="422.3" width="2.44" height="26.9" fill="var(--down)"/>
<line x1="569.8" y1="424.7" x2="569.8" y2="464.1" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="446.6" width="2.44" height="15.2" fill="var(--up)"/>
<line x1="573.7" y1="412.3" x2="573.7" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="433.4" width="2.44" height="17.0" fill="var(--down)"/>
<line x1="577.7" y1="422.9" x2="577.7" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="432.0" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="581.6" y1="411.0" x2="581.6" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="417.8" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="585.5" y1="365.3" x2="585.5" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="382.7" width="2.44" height="26.5" fill="var(--up)"/>
<line x1="589.5" y1="385.9" x2="589.5" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="399.4" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="593.4" y1="404.9" x2="593.4" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="404.9" width="2.44" height="124.0" fill="var(--down)"/>
<line x1="597.3" y1="468.9" x2="597.3" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="495.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="601.3" y1="479.9" x2="601.3" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="488.2" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="605.2" y1="456.5" x2="605.2" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="474.4" width="2.44" height="21.2" fill="var(--down)"/>
<line x1="609.1" y1="488.5" x2="609.1" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="490.8" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="613.1" y1="442.9" x2="613.1" y2="494.1" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="471.5" width="2.44" height="22.6" fill="var(--up)"/>
<line x1="617.0" y1="450.6" x2="617.0" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="461.7" width="2.44" height="58.0" fill="var(--down)"/>
<line x1="621.0" y1="495.8" x2="621.0" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="619.73" y="502.7" width="2.44" height="39.0" fill="var(--up)"/>
<line x1="624.9" y1="466.3" x2="624.9" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="480.7" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="628.8" y1="477.1" x2="628.8" y2="504.0" stroke="var(--down)" class="wick"/>
<rect x="627.61" y="497.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="632.8" y1="485.9" x2="632.8" y2="505.5" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="495.1" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="636.7" y1="479.5" x2="636.7" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="482.4" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="640.6" y1="436.1" x2="640.6" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="439.5" width="2.44" height="29.5" fill="var(--down)"/>
<line x1="644.6" y1="428.7" x2="644.6" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="469.0" width="2.44" height="19.0" fill="var(--down)"/>
<line x1="648.5" y1="452.4" x2="648.5" y2="485.9" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="476.0" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="652.4" y1="439.7" x2="652.4" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="455.0" width="2.44" height="33.7" fill="var(--up)"/>
<line x1="656.4" y1="412.1" x2="656.4" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="420.0" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="660.3" y1="404.5" x2="660.3" y2="431.0" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="410.7" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="664.3" y1="402.1" x2="664.3" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="410.6" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="668.2" y1="392.6" x2="668.2" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="406.1" width="2.44" height="17.0" fill="var(--down)"/>
<line x1="672.1" y1="419.5" x2="672.1" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="425.6" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="676.1" y1="437.4" x2="676.1" y2="479.7" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="439.5" width="2.44" height="35.5" fill="var(--down)"/>
<line x1="680.0" y1="449.7" x2="680.0" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="457.4" width="2.44" height="12.2" fill="var(--down)"/>
<line x1="683.9" y1="450.9" x2="683.9" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="682.72" y="463.2" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="687.9" y1="410.9" x2="687.9" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="417.7" width="2.44" height="48.6" fill="var(--up)"/>
<line x1="691.8" y1="393.0" x2="691.8" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="690.59" y="404.2" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="695.7" y1="423.9" x2="695.7" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="428.9" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="699.7" y1="437.2" x2="699.7" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="438.9" width="2.44" height="42.9" fill="var(--down)"/>
<line x1="703.6" y1="446.3" x2="703.6" y2="470.0" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="457.2" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="707.6" y1="443.2" x2="707.6" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="454.3" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="711.5" y1="429.7" x2="711.5" y2="459.6" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="438.9" width="2.44" height="19.2" fill="var(--up)"/>
<line x1="715.4" y1="421.0" x2="715.4" y2="445.3" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="425.9" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="719.4" y1="426.0" x2="719.4" y2="464.7" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="435.0" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="723.3" y1="393.2" x2="723.3" y2="481.9" stroke="var(--down)" class="wick"/>
<rect x="722.08" y="425.7" width="2.44" height="55.1" fill="var(--down)"/>
<line x1="727.2" y1="474.4" x2="727.2" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="474.4" width="2.44" height="44.1" fill="var(--down)"/>
<line x1="731.2" y1="488.0" x2="731.2" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="729.95" y="492.3" width="2.44" height="24.6" fill="var(--up)"/>
<line x1="735.1" y1="502.8" x2="735.1" y2="531.0" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="507.8" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="739.0" y1="527.3" x2="739.0" y2="568.3" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="527.3" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="743.0" y1="545.4" x2="743.0" y2="565.8" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="553.8" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="746.9" y1="558.8" x2="746.9" y2="578.6" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="566.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="750.9" y1="568.2" x2="750.9" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="571.4" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="754.8" y1="585.4" x2="754.8" y2="609.9" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="590.8" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="758.7" y1="535.6" x2="758.7" y2="578.6" stroke="var(--up)" class="wick"/>
<rect x="757.51" y="541.1" width="2.44" height="36.4" fill="var(--up)"/>
<line x1="762.7" y1="509.1" x2="762.7" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="510.3" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="766.6" y1="458.8" x2="766.6" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="466.7" width="2.44" height="31.8" fill="var(--up)"/>
<line x1="770.5" y1="399.2" x2="770.5" y2="454.9" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="416.4" width="2.44" height="34.3" fill="var(--up)"/>
<line x1="774.5" y1="413.6" x2="774.5" y2="453.7" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="414.0" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="778.4" y1="422.7" x2="778.4" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="442.4" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="782.3" y1="430.2" x2="782.3" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="442.7" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="786.3" y1="452.9" x2="786.3" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="462.3" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="790.2" y1="439.4" x2="790.2" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="456.4" width="2.44" height="12.3" fill="var(--up)"/>
<line x1="794.2" y1="456.8" x2="794.2" y2="486.8" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="465.2" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="798.1" y1="480.2" x2="798.1" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="482.3" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="802.0" y1="478.7" x2="802.0" y2="519.9" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="492.6" width="2.44" height="19.6" fill="var(--down)"/>
<line x1="806.0" y1="509.0" x2="806.0" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="515.0" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="809.9" y1="502.9" x2="809.9" y2="556.0" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="514.3" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="813.8" y1="541.1" x2="813.8" y2="578.0" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="545.0" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="817.8" y1="523.5" x2="817.8" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="816.56" y="526.7" width="2.44" height="32.7" fill="var(--up)"/>
<line x1="821.7" y1="501.7" x2="821.7" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="516.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="825.7" y1="471.7" x2="825.7" y2="503.2" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="483.4" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="829.6" y1="435.1" x2="829.6" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="452.5" width="2.44" height="32.5" fill="var(--up)"/>
<line x1="833.5" y1="429.3" x2="833.5" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="451.2" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="837.5" y1="381.4" x2="837.5" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="421.3" width="2.44" height="10.1" fill="var(--up)"/>
<line x1="841.4" y1="380.4" x2="841.4" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="400.1" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="845.3" y1="408.8" x2="845.3" y2="449.3" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="429.6" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="849.3" y1="409.9" x2="849.3" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="425.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="853.2" y1="375.3" x2="853.2" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="397.0" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="857.1" y1="396.0" x2="857.1" y2="424.7" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="408.6" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="861.1" y1="410.1" x2="861.1" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="421.6" width="2.44" height="8.0" fill="var(--down)"/>
<line x1="865.0" y1="411.0" x2="865.0" y2="465.2" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="428.4" width="2.44" height="24.0" fill="var(--down)"/>
<line x1="869.0" y1="460.3" x2="869.0" y2="498.4" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="468.3" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="872.9" y1="466.9" x2="872.9" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="480.8" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="876.8" y1="460.8" x2="876.8" y2="492.5" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="460.9" width="2.44" height="28.8" fill="var(--up)"/>
<line x1="880.8" y1="447.7" x2="880.8" y2="480.4" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="467.6" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="884.7" y1="465.4" x2="884.7" y2="496.7" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="475.5" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="888.6" y1="436.9" x2="888.6" y2="459.6" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="450.1" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="892.6" y1="444.0" x2="892.6" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="451.0" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="896.5" y1="447.5" x2="896.5" y2="467.1" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="455.5" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="900.4" y1="394.3" x2="900.4" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="438.0" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="904.4" y1="402.0" x2="904.4" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="428.9" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="908.3" y1="455.6" x2="908.3" y2="513.7" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="457.0" width="2.44" height="32.2" fill="var(--down)"/>
<line x1="912.3" y1="460.8" x2="912.3" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="911.03" y="471.7" width="2.44" height="30.8" fill="var(--up)"/>
<line x1="916.2" y1="452.8" x2="916.2" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="456.3" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="920.1" y1="417.0" x2="920.1" y2="444.0" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="430.0" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="924.1" y1="396.7" x2="924.1" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="403.2" width="2.44" height="40.2" fill="var(--up)"/>
<line x1="928.0" y1="389.1" x2="928.0" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="926.78" y="389.6" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="931.9" y1="384.9" x2="931.9" y2="430.1" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="391.4" width="2.44" height="32.2" fill="var(--down)"/>
<line x1="935.9" y1="406.8" x2="935.9" y2="471.1" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="410.7" width="2.44" height="51.1" fill="var(--down)"/>
<line x1="939.8" y1="480.5" x2="939.8" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="481.0" width="2.44" height="32.0" fill="var(--down)"/>
<line x1="943.7" y1="509.1" x2="943.7" y2="552.3" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="512.5" width="2.44" height="35.9" fill="var(--down)"/>
<line x1="947.7" y1="492.8" x2="947.7" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="513.1" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="951.6" y1="485.7" x2="951.6" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="493.5" width="2.44" height="22.2" fill="var(--down)"/>
<line x1="955.6" y1="462.5" x2="955.6" y2="527.8" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="468.7" width="2.44" height="43.5" fill="var(--up)"/>
<line x1="959.5" y1="462.3" x2="959.5" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="470.8" width="2.44" height="75.0" fill="var(--down)"/>
<line x1="963.4" y1="532.0" x2="963.4" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="541.7" width="2.44" height="20.1" fill="var(--down)"/>
<line x1="967.4" y1="547.0" x2="967.4" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="553.2" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="971.3" y1="549.0" x2="971.3" y2="597.2" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="561.8" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="975.2" y1="535.9" x2="975.2" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="548.0" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="979.2" y1="523.5" x2="979.2" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="535.5" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="983.1" y1="508.5" x2="983.1" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="510.8" width="2.44" height="14.1" fill="var(--down)"/>
<line x1="987.0" y1="518.2" x2="987.0" y2="536.2" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="526.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="991.0" y1="503.6" x2="991.0" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="516.1" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="994.9" y1="505.5" x2="994.9" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="508.5" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="998.9" y1="531.8" x2="998.9" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="538.1" width="2.44" height="24.1" fill="var(--down)"/>
<line x1="1002.8" y1="548.6" x2="1002.8" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="549.0" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="1006.7" y1="544.1" x2="1006.7" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="549.0" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="1010.7" y1="563.4" x2="1010.7" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="565.4" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="1014.6" y1="582.3" x2="1014.6" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="590.3" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="1018.5" y1="563.8" x2="1018.5" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="571.2" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="1022.5" y1="540.9" x2="1022.5" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="565.2" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="1026.4" y1="550.2" x2="1026.4" y2="574.8" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="553.2" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="1030.3" y1="558.7" x2="1030.3" y2="585.9" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="560.0" width="2.44" height="23.0" fill="var(--down)"/>
<line x1="1034.3" y1="577.9" x2="1034.3" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="581.3" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="1038.2" y1="569.7" x2="1038.2" y2="596.3" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="577.0" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="1042.2" y1="540.2" x2="1042.2" y2="583.9" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="544.4" width="2.44" height="34.2" fill="var(--up)"/>
<line x1="1046.1" y1="512.1" x2="1046.1" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="535.0" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="1050.0" y1="508.1" x2="1050.0" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="1048.81" y="509.0" width="2.44" height="32.9" fill="var(--up)"/>
<line x1="60" y1="388.5" x2="1052" y2="388.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="392.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$169 R1</text>
<text x="1058" y="404.0" font-size="9.5" fill="var(--muted)">터치 10회</text>
<line x1="60" y1="326.6" x2="1052" y2="326.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="330.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$179 R2</text>
<text x="1058" y="342.1" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="89.6" x2="1052" y2="89.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="93.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$218 R3</text>
<text x="1058" y="105.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="513.2" x2="1052" y2="513.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="507.2" font-size="11.5" fill="var(--support)" font-weight="600">$149 S1</text>
<text x="1058" y="519.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="543.6" x2="1052" y2="543.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="537.6" font-size="11.5" fill="var(--support)" font-weight="600">$144 S2</text>
<text x="1058" y="549.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="576.2" x2="1052" y2="576.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="570.2" font-size="11.5" fill="var(--support)" font-weight="600">$138 S3</text>
<text x="1058" y="582.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="509.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="501.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $149 (2026-09-04)</text>
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
| R3 | $218 | 2 | 2025-09-22·2025-10-16 — **52주 최고($219.82) 구간**. AI 전력 수요 기대가 정점이던 시기이며, 이후 1년간 한 번도 재도달하지 못했다 |
| R2 | $179 | 4 | 2025-12-12·2026-01-15·2026-02-17·2026-02-27 — Cogentrix 인수 계약(2025-12-31)과 Meta PPA 발표(2026-01-09) 전후에 네 번 눌린 자리 |
| R1 | $169 | 10 | 2026-01-29·03-10·03-18·04-17·04-27·05-07·05-26·06-25·07-14·07-24 — **1년 중 가장 두꺼운 클러스터(터치 10회)**. 2026년 대부분을 이 선 아래에서 보냈다 |
| **현재가** | **$149.30** (2026-09-04 종가) | — | R1과 S1 사이. S1($149)에 거의 붙어 있다 |
| S1 | $149 | 3 | 2026-01-08·2026-07-02·2026-07-17 — **현재가가 이 지지대 위에 걸쳐 있다.** 이 아래로 내려가면 다음 지지는 S2($144) |
| S2 | $144 | 2 | 2026-03-20·2026-03-31 |
| S3 | $138 | 2 | 2026-02-05·2026-06-10 — 그 아래 52주 최저 $132.66까지 유효한 클러스터가 없다 |
| 참고선 | $132.66 | — | **52주 최저**. 터치 2회 미만이라 클러스터로 잡히지 않았고, 지지대가 아니라 기간 내 최저 관측치로만 본다 |

---

## 3. 관측된 특이 구간 — 저항이 계단식으로 내려온 1년

이 종목에는 하루 만에 가격대를 재설정한 단일 이벤트(실적 갭·인수 발표 갭)가 없었다. 대신 **저항선이 $218 → $179 → $169로 계단식으로 내려온 것**이 이 1년의 구조다.

- R3($218, 2025년 9~10월)에서 R2($179, 2025년 12월~2026년 2월)를 거쳐 R1($169, 2026년 1월~7월)로 내려왔고, **R1의 터치가 10회로 압도적으로 두껍다** — 2026년 대부분의 시간을 그 아래에서 보냈다는 뜻이다.
- 주목할 점은 **이 하락 구간에 회사의 실적과 계약이 오히려 좋아졌다는 것**이다. Meta PPA 2,609 MW 체결(2026-01-09), Cogentrix FERC 승인(2026-08), 2026 Q2 Adjusted EBITDA +31% — 전부 [최근 뉴스 / 이슈](./08_news.md)의 로그에 있다. **가격과 펀더멘털이 반대로 움직인 1년**이었고, [밸류에이션 / 적정주가](./06_valuation.md) 5. 결론이 "주가 하락의 대부분은 실적이 아니라 배수 축소에서 왔다"고 정리한 것과 같은 관찰이다.
- 현재가 $149.30은 **S1($149) 위에 간신히 걸쳐 있다.** 이 클러스터를 잃으면 S2($144)·S3($138)를 거쳐 52주 최저($132.66)까지 사이에 두꺼운 지지가 없다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-05~2026-09-04. 수집 시점: 2026-09-07. **원주가(과거 분할은 소급 반영, 배당은 미반영)**
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py VST --name "Vistra" --close-on 2026-09-04 --emit all` (재현용, 옵션 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **기간 내 배당이 4회 있었으나 원주가라 반영되지 않았다.** 배당수익률이 0.62%로 낮아 레벨 해석에 미치는 영향은 작지만, 배당 재투자 기준 수익률과는 차이가 난다.
    - **해당 기간에 주식분할·대규모 유상증자는 없었다.** 다만 진행 중인 Cogentrix 인수 대가로 **신주 500만 주(발행주식수의 약 1.5%)가 발행될 예정**이라, 종결 이후의 가격은 그만큼 희석된 기준이 된다.
    - 하단 클러스터(S1~S3)가 전부 터치 2~3회로 얇다 — **1년 내내 하락 추세였던 종목이라 아래쪽에 반복 검증된 가격대가 쌓일 시간이 없었다.** 이 구간의 지지선은 상단 R1(터치 10회)보다 신뢰도가 낮다.

---

*작성일: 2026-09-11*
