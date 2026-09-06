# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL)와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-04 종가 $119.02는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.** 세 문서가 같은 기준일·같은 종가를 쓴다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="nrg-chart">
<style>
.nrg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .nrg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .nrg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.nrg-chart svg { width:100%; height:auto; display:block; }
.nrg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.nrg-chart .title { fill: var(--ink); font-weight:600; }
.nrg-chart .grid { stroke: var(--grid); stroke-width:1; }
.nrg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NRG Energy(NRG) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">NRG Energy (NRG) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $119.02 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="524.7" x2="1052" y2="524.7" class="grid"/>
<text x="52" y="528.7" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="398.0" x2="1052" y2="398.0" class="grid"/>
<text x="52" y="402.0" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="271.3" x2="1052" y2="271.3" class="grid"/>
<text x="52" y="275.3" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="144.7" x2="1052" y2="144.7" class="grid"/>
<text x="52" y="148.7" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
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
<line x1="62.0" y1="333.1" x2="62.0" y2="379.8" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="341.3" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="65.9" y1="336.9" x2="65.9" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="342.7" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="69.8" y1="319.3" x2="69.8" y2="348.5" stroke="var(--up)" class="wick"/>
<rect x="68.62" y="320.4" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="73.8" y1="257.0" x2="73.8" y2="303.6" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="263.7" width="2.44" height="39.6" fill="var(--up)"/>
<line x1="77.7" y1="260.0" x2="77.7" y2="285.6" stroke="var(--down)" class="wick"/>
<rect x="76.49" y="262.1" width="2.44" height="22.4" fill="var(--down)"/>
<line x1="81.7" y1="234.5" x2="81.7" y2="290.2" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="240.7" width="2.44" height="45.2" fill="var(--up)"/>
<line x1="85.6" y1="214.2" x2="85.6" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="232.8" width="2.44" height="6.1" fill="var(--up)"/>
<line x1="89.5" y1="225.5" x2="89.5" y2="257.1" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="229.4" width="2.44" height="15.2" fill="var(--down)"/>
<line x1="93.5" y1="226.5" x2="93.5" y2="256.7" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="237.3" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="97.4" y1="223.3" x2="97.4" y2="259.5" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="226.5" width="2.44" height="18.3" fill="var(--down)"/>
<line x1="101.3" y1="234.7" x2="101.3" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="239.4" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="105.3" y1="195.1" x2="105.3" y2="249.2" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="201.9" width="2.44" height="38.1" fill="var(--up)"/>
<line x1="109.2" y1="198.1" x2="109.2" y2="238.5" stroke="var(--down)" class="wick"/>
<rect x="107.99" y="200.7" width="2.44" height="23.6" fill="var(--down)"/>
<line x1="113.1" y1="213.4" x2="113.1" y2="236.5" stroke="var(--down)" class="wick"/>
<rect x="111.92" y="222.5" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="117.1" y1="239.9" x2="117.1" y2="284.6" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="252.6" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="121.0" y1="211.5" x2="121.0" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="217.1" width="2.44" height="30.3" fill="var(--up)"/>
<line x1="125.0" y1="207.4" x2="125.0" y2="241.8" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="212.4" width="2.44" height="25.1" fill="var(--down)"/>
<line x1="128.9" y1="234.4" x2="128.9" y2="264.7" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="237.1" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="132.8" y1="236.8" x2="132.8" y2="267.7" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="259.2" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="136.8" y1="217.0" x2="136.8" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="225.1" width="2.44" height="27.4" fill="var(--up)"/>
<line x1="140.7" y1="194.0" x2="140.7" y2="234.4" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="219.2" width="2.44" height="12.3" fill="var(--down)"/>
<line x1="144.6" y1="208.2" x2="144.6" y2="251.7" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="214.5" width="2.44" height="31.8" fill="var(--down)"/>
<line x1="148.6" y1="234.6" x2="148.6" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="244.0" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="152.5" y1="212.2" x2="152.5" y2="249.2" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="223.7" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="156.4" y1="208.1" x2="156.4" y2="227.5" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="219.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="160.4" y1="215.4" x2="160.4" y2="268.9" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="222.4" width="2.44" height="46.2" fill="var(--down)"/>
<line x1="164.3" y1="215.7" x2="164.3" y2="245.0" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="215.8" width="2.44" height="29.0" fill="var(--up)"/>
<line x1="168.3" y1="214.5" x2="168.3" y2="251.8" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="235.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="172.2" y1="186.7" x2="172.2" y2="221.6" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="199.6" width="2.44" height="19.9" fill="var(--up)"/>
<line x1="176.1" y1="182.7" x2="176.1" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="188.4" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="180.1" y1="192.8" x2="180.1" y2="234.1" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="216.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="184.0" y1="189.6" x2="184.0" y2="231.4" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="196.5" width="2.44" height="30.4" fill="var(--down)"/>
<line x1="187.9" y1="221.2" x2="187.9" y2="270.1" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="230.0" width="2.44" height="18.6" fill="var(--down)"/>
<line x1="191.9" y1="237.3" x2="191.9" y2="282.0" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="245.9" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="195.8" y1="246.1" x2="195.8" y2="269.4" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="247.2" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="199.7" y1="204.4" x2="199.7" y2="226.5" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="205.7" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="203.7" y1="186.8" x2="203.7" y2="209.2" stroke="var(--up)" class="wick"/>
<rect x="202.46" y="191.6" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="207.6" y1="183.3" x2="207.6" y2="234.3" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="185.8" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="211.6" y1="141.2" x2="211.6" y2="204.8" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="154.2" width="2.44" height="30.5" fill="var(--up)"/>
<line x1="215.5" y1="144.2" x2="215.5" y2="189.8" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="167.3" width="2.44" height="20.8" fill="var(--down)"/>
<line x1="219.4" y1="163.8" x2="219.4" y2="205.7" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="174.5" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="223.4" y1="165.2" x2="223.4" y2="200.6" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="179.6" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="227.3" y1="195.2" x2="227.3" y2="227.6" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="197.5" width="2.44" height="23.2" fill="var(--down)"/>
<line x1="231.2" y1="174.6" x2="231.2" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="187.8" width="2.44" height="34.8" fill="var(--up)"/>
<line x1="235.2" y1="163.1" x2="235.2" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="233.95" y="207.4" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="239.1" y1="192.2" x2="239.1" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="192.2" width="2.44" height="47.6" fill="var(--up)"/>
<line x1="243.0" y1="165.4" x2="243.0" y2="245.4" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="172.2" width="2.44" height="56.6" fill="var(--down)"/>
<line x1="247.0" y1="226.1" x2="247.0" y2="266.5" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="243.0" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="250.9" y1="211.4" x2="250.9" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="215.3" width="2.44" height="30.3" fill="var(--up)"/>
<line x1="254.9" y1="212.9" x2="254.9" y2="240.0" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="222.3" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="258.8" y1="200.4" x2="258.8" y2="271.0" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="238.5" width="2.44" height="25.0" fill="var(--up)"/>
<line x1="262.7" y1="212.8" x2="262.7" y2="257.2" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="238.5" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="266.7" y1="216.2" x2="266.7" y2="264.1" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="230.5" width="2.44" height="32.2" fill="var(--up)"/>
<line x1="270.6" y1="185.7" x2="270.6" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="215.6" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="274.5" y1="178.0" x2="274.5" y2="269.1" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="183.0" width="2.44" height="85.4" fill="var(--down)"/>
<line x1="278.5" y1="262.5" x2="278.5" y2="300.5" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="268.0" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="282.4" y1="220.9" x2="282.4" y2="278.0" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="227.9" width="2.44" height="41.2" fill="var(--up)"/>
<line x1="286.3" y1="218.6" x2="286.3" y2="265.0" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="225.8" width="2.44" height="21.4" fill="var(--down)"/>
<line x1="290.3" y1="208.6" x2="290.3" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="217.2" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="294.2" y1="196.8" x2="294.2" y2="218.1" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="208.0" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="298.2" y1="223.4" x2="298.2" y2="247.5" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="223.5" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="302.1" y1="220.2" x2="302.1" y2="253.9" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="227.4" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="306.0" y1="227.0" x2="306.0" y2="269.9" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="228.5" width="2.44" height="19.1" fill="var(--up)"/>
<line x1="310.0" y1="206.8" x2="310.0" y2="233.3" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="212.1" width="2.44" height="20.4" fill="var(--up)"/>
<line x1="313.9" y1="206.4" x2="313.9" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="215.2" width="2.44" height="37.2" fill="var(--down)"/>
<line x1="317.8" y1="225.9" x2="317.8" y2="257.3" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="244.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="321.8" y1="198.1" x2="321.8" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="228.6" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="325.7" y1="207.6" x2="325.7" y2="250.8" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="219.7" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="329.7" y1="202.7" x2="329.7" y2="244.3" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="203.9" width="2.44" height="35.6" fill="var(--up)"/>
<line x1="333.6" y1="192.8" x2="333.6" y2="267.7" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="195.3" width="2.44" height="66.9" fill="var(--down)"/>
<line x1="337.5" y1="252.0" x2="337.5" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="259.4" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="341.5" y1="257.0" x2="341.5" y2="287.5" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="270.4" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="345.4" y1="264.5" x2="345.4" y2="347.5" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="267.9" width="2.44" height="70.0" fill="var(--down)"/>
<line x1="349.3" y1="282.7" x2="349.3" y2="321.4" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="305.3" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="353.3" y1="286.7" x2="353.3" y2="304.9" stroke="var(--up)" class="wick"/>
<rect x="352.05" y="295.4" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="357.2" y1="283.4" x2="357.2" y2="307.1" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="283.4" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="361.1" y1="273.2" x2="361.1" y2="292.6" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="283.3" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="365.1" y1="264.1" x2="365.1" y2="290.7" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="267.8" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="369.0" y1="261.7" x2="369.0" y2="281.5" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="265.8" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="373.0" y1="245.6" x2="373.0" y2="269.1" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="265.3" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="376.9" y1="258.7" x2="376.9" y2="274.1" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="262.2" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="380.8" y1="263.7" x2="380.8" y2="276.5" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="266.0" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="384.8" y1="229.2" x2="384.8" y2="265.3" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="232.3" width="2.44" height="29.0" fill="var(--up)"/>
<line x1="388.7" y1="206.5" x2="388.7" y2="277.7" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="217.6" width="2.44" height="43.7" fill="var(--down)"/>
<line x1="392.6" y1="263.7" x2="392.6" y2="297.7" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="263.7" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="396.6" y1="284.8" x2="396.6" y2="346.1" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="287.1" width="2.44" height="54.5" fill="var(--down)"/>
<line x1="400.5" y1="341.1" x2="400.5" y2="385.5" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="347.0" width="2.44" height="28.7" fill="var(--down)"/>
<line x1="404.4" y1="323.3" x2="404.4" y2="349.7" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="330.6" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="408.4" y1="336.3" x2="408.4" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="341.7" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="412.3" y1="319.8" x2="412.3" y2="344.9" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="330.9" width="2.44" height="8.4" fill="var(--up)"/>
<line x1="416.3" y1="330.7" x2="416.3" y2="350.4" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="335.7" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="420.2" y1="276.1" x2="420.2" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="280.8" width="2.44" height="41.0" fill="var(--up)"/>
<line x1="424.1" y1="291.7" x2="424.1" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="310.9" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="428.1" y1="318.3" x2="428.1" y2="363.0" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="341.6" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="432.0" y1="322.5" x2="432.0" y2="352.1" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="326.7" width="2.44" height="3.7" fill="var(--down)"/>
<line x1="435.9" y1="312.1" x2="435.9" y2="337.5" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="316.8" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="439.9" y1="320.5" x2="439.9" y2="354.2" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="328.5" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="443.8" y1="326.2" x2="443.8" y2="341.1" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="333.3" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="447.7" y1="294.0" x2="447.7" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="296.4" width="2.44" height="42.6" fill="var(--up)"/>
<line x1="451.7" y1="287.2" x2="451.7" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="290.3" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="455.6" y1="289.1" x2="455.6" y2="327.2" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="300.5" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="459.6" y1="290.5" x2="459.6" y2="329.2" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="315.0" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="463.5" y1="313.6" x2="463.5" y2="343.7" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="321.3" width="2.44" height="19.0" fill="var(--down)"/>
<line x1="467.4" y1="305.8" x2="467.4" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="320.9" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="471.4" y1="312.7" x2="471.4" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="322.6" width="2.44" height="50.2" fill="var(--down)"/>
<line x1="475.3" y1="350.8" x2="475.3" y2="386.5" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="369.9" width="2.44" height="13.0" fill="var(--up)"/>
<line x1="479.2" y1="312.1" x2="479.2" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="313.6" width="2.44" height="27.6" fill="var(--up)"/>
<line x1="483.2" y1="281.8" x2="483.2" y2="317.0" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="298.4" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="487.1" y1="279.6" x2="487.1" y2="309.3" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="290.2" width="2.44" height="3.7" fill="var(--down)"/>
<line x1="491.0" y1="265.3" x2="491.0" y2="292.7" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="267.3" width="2.44" height="13.8" fill="var(--up)"/>
<line x1="495.0" y1="231.8" x2="495.0" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="257.3" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="498.9" y1="191.0" x2="498.9" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="193.1" width="2.44" height="67.5" fill="var(--up)"/>
<line x1="502.9" y1="159.2" x2="502.9" y2="202.6" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="186.2" width="2.44" height="2.1" fill="var(--up)"/>
<line x1="506.8" y1="167.2" x2="506.8" y2="204.5" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="179.5" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="510.7" y1="174.6" x2="510.7" y2="210.2" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="176.3" width="2.44" height="28.7" fill="var(--up)"/>
<line x1="514.7" y1="144.0" x2="514.7" y2="182.7" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="149.9" width="2.44" height="25.6" fill="var(--up)"/>
<line x1="518.6" y1="131.7" x2="518.6" y2="175.6" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="160.2" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="522.5" y1="114.0" x2="522.5" y2="247.5" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="119.1" width="2.44" height="68.1" fill="var(--up)"/>
<line x1="526.5" y1="81.6" x2="526.5" y2="139.0" stroke="var(--down)" class="wick"/>
<rect x="525.26" y="103.1" width="2.44" height="18.8" fill="var(--down)"/>
<line x1="530.4" y1="121.4" x2="530.4" y2="185.3" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="125.7" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="534.3" y1="137.8" x2="534.3" y2="181.3" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="144.8" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="538.3" y1="134.7" x2="538.3" y2="182.4" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="172.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="542.2" y1="245.6" x2="542.2" y2="284.0" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="253.3" width="2.44" height="5.0" fill="var(--down)"/>
<line x1="546.2" y1="230.6" x2="546.2" y2="259.3" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="248.9" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="550.1" y1="238.7" x2="550.1" y2="283.8" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="258.7" width="2.44" height="9.8" fill="var(--down)"/>
<line x1="554.0" y1="274.9" x2="554.0" y2="307.9" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="279.0" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="558.0" y1="299.2" x2="558.0" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="300.3" width="2.44" height="30.0" fill="var(--up)"/>
<line x1="561.9" y1="275.3" x2="561.9" y2="303.0" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="296.7" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="565.8" y1="306.2" x2="565.8" y2="350.3" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="308.0" width="2.44" height="35.3" fill="var(--down)"/>
<line x1="569.8" y1="318.8" x2="569.8" y2="358.4" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="321.4" width="2.44" height="34.8" fill="var(--up)"/>
<line x1="573.7" y1="304.5" x2="573.7" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="306.0" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="577.7" y1="286.8" x2="577.7" y2="324.0" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="296.7" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="581.6" y1="297.9" x2="581.6" y2="318.1" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="304.6" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="585.5" y1="256.0" x2="585.5" y2="290.3" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="277.0" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="589.5" y1="252.5" x2="589.5" y2="304.3" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="262.5" width="2.44" height="30.2" fill="var(--up)"/>
<line x1="593.4" y1="255.5" x2="593.4" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="261.8" width="2.44" height="99.5" fill="var(--down)"/>
<line x1="597.3" y1="304.9" x2="597.3" y2="353.8" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="323.5" width="2.44" height="23.9" fill="var(--up)"/>
<line x1="601.3" y1="302.6" x2="601.3" y2="332.0" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="327.5" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="605.2" y1="304.1" x2="605.2" y2="332.4" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="317.9" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="609.1" y1="331.2" x2="609.1" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="341.6" width="2.44" height="17.5" fill="var(--down)"/>
<line x1="613.1" y1="331.1" x2="613.1" y2="359.9" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="349.0" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="617.0" y1="326.7" x2="617.0" y2="398.7" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="331.6" width="2.44" height="58.6" fill="var(--down)"/>
<line x1="621.0" y1="354.4" x2="621.0" y2="388.5" stroke="var(--up)" class="wick"/>
<rect x="619.73" y="359.1" width="2.44" height="25.7" fill="var(--up)"/>
<line x1="624.9" y1="329.1" x2="624.9" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="335.3" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="628.8" y1="316.9" x2="628.8" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="317.6" width="2.44" height="43.3" fill="var(--up)"/>
<line x1="632.8" y1="310.5" x2="632.8" y2="336.2" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="319.2" width="2.44" height="16.8" fill="var(--down)"/>
<line x1="636.7" y1="314.0" x2="636.7" y2="339.8" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="315.3" width="2.44" height="24.5" fill="var(--up)"/>
<line x1="640.6" y1="264.4" x2="640.6" y2="288.1" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="268.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="644.6" y1="226.6" x2="644.6" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="260.1" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="648.5" y1="227.7" x2="648.5" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="245.6" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="652.4" y1="205.3" x2="652.4" y2="265.7" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="206.5" width="2.44" height="52.3" fill="var(--up)"/>
<line x1="656.4" y1="173.0" x2="656.4" y2="212.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="195.1" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="660.3" y1="205.0" x2="660.3" y2="234.5" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="207.5" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="664.3" y1="201.4" x2="664.3" y2="231.3" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="216.2" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="668.2" y1="199.4" x2="668.2" y2="231.5" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="214.3" width="2.44" height="8.0" fill="var(--down)"/>
<line x1="672.1" y1="209.4" x2="672.1" y2="295.1" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="213.4" width="2.44" height="75.7" fill="var(--down)"/>
<line x1="676.1" y1="280.8" x2="676.1" y2="336.8" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="291.9" width="2.44" height="43.6" fill="var(--down)"/>
<line x1="680.0" y1="315.2" x2="680.0" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="323.3" width="2.44" height="13.9" fill="var(--down)"/>
<line x1="683.9" y1="306.0" x2="683.9" y2="342.3" stroke="var(--up)" class="wick"/>
<rect x="682.72" y="306.0" width="2.44" height="27.6" fill="var(--up)"/>
<line x1="687.9" y1="267.1" x2="687.9" y2="309.4" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="272.5" width="2.44" height="31.3" fill="var(--up)"/>
<line x1="691.8" y1="262.7" x2="691.8" y2="287.9" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="265.7" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="695.7" y1="276.1" x2="695.7" y2="304.8" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="293.1" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="699.7" y1="295.7" x2="699.7" y2="343.2" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="304.1" width="2.44" height="36.8" fill="var(--down)"/>
<line x1="703.6" y1="297.6" x2="703.6" y2="329.4" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="299.3" width="2.44" height="28.8" fill="var(--up)"/>
<line x1="707.6" y1="290.4" x2="707.6" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="304.1" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="711.5" y1="294.4" x2="711.5" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="304.1" width="2.44" height="11.5" fill="var(--up)"/>
<line x1="715.4" y1="276.1" x2="715.4" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="287.6" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="719.4" y1="285.1" x2="719.4" y2="341.0" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="314.5" width="2.44" height="16.1" fill="var(--down)"/>
<line x1="723.3" y1="326.2" x2="723.3" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="722.08" y="329.2" width="2.44" height="57.0" fill="var(--down)"/>
<line x1="727.2" y1="366.6" x2="727.2" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="375.5" width="2.44" height="34.5" fill="var(--down)"/>
<line x1="731.2" y1="403.6" x2="731.2" y2="417.2" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="410.4" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="735.1" y1="408.1" x2="735.1" y2="435.7" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="414.8" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="739.0" y1="410.7" x2="739.0" y2="466.1" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="416.1" width="2.44" height="38.4" fill="var(--down)"/>
<line x1="743.0" y1="430.3" x2="743.0" y2="456.9" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="431.4" width="2.44" height="23.9" fill="var(--up)"/>
<line x1="746.9" y1="447.1" x2="746.9" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="448.7" width="2.44" height="26.5" fill="var(--down)"/>
<line x1="750.9" y1="474.7" x2="750.9" y2="498.3" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="478.1" width="2.44" height="11.8" fill="var(--down)"/>
<line x1="754.8" y1="498.3" x2="754.8" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="499.3" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="758.7" y1="434.5" x2="758.7" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="757.51" y="436.1" width="2.44" height="43.1" fill="var(--up)"/>
<line x1="762.7" y1="415.8" x2="762.7" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="417.5" width="2.44" height="24.6" fill="var(--up)"/>
<line x1="766.6" y1="398.9" x2="766.6" y2="422.3" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="412.9" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="770.5" y1="378.5" x2="770.5" y2="405.1" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="395.3" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="774.5" y1="388.3" x2="774.5" y2="422.8" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="399.9" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="778.4" y1="404.7" x2="778.4" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="413.8" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="782.3" y1="409.3" x2="782.3" y2="436.6" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="423.3" width="2.44" height="12.2" fill="var(--down)"/>
<line x1="786.3" y1="450.9" x2="786.3" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="454.4" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="790.2" y1="424.3" x2="790.2" y2="467.0" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="439.1" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="794.2" y1="417.4" x2="794.2" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="437.5" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="798.1" y1="430.7" x2="798.1" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="439.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="802.0" y1="447.7" x2="802.0" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="451.3" width="2.44" height="15.1" fill="var(--down)"/>
<line x1="806.0" y1="463.4" x2="806.0" y2="478.4" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="465.5" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="809.9" y1="452.3" x2="809.9" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="808.68" y="461.6" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="813.8" y1="473.4" x2="813.8" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="478.4" width="2.44" height="42.1" fill="var(--down)"/>
<line x1="817.8" y1="497.1" x2="817.8" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="816.56" y="501.2" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="821.7" y1="461.3" x2="821.7" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="490.0" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="825.7" y1="452.3" x2="825.7" y2="483.9" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="458.8" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="829.6" y1="426.2" x2="829.6" y2="458.1" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="448.0" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="833.5" y1="428.3" x2="833.5" y2="456.1" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="447.8" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="837.5" y1="394.5" x2="837.5" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="429.3" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="841.4" y1="404.1" x2="841.4" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="404.9" width="2.44" height="22.6" fill="var(--up)"/>
<line x1="845.3" y1="405.2" x2="845.3" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="412.8" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="849.3" y1="379.1" x2="849.3" y2="417.9" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="384.0" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="853.2" y1="351.3" x2="853.2" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="353.0" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="857.1" y1="331.4" x2="857.1" y2="366.3" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="338.7" width="2.44" height="26.5" fill="var(--up)"/>
<line x1="861.1" y1="328.5" x2="861.1" y2="358.9" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="337.6" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="865.0" y1="329.9" x2="865.0" y2="365.3" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="339.9" width="2.44" height="19.7" fill="var(--down)"/>
<line x1="869.0" y1="360.9" x2="869.0" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="362.8" width="2.44" height="30.1" fill="var(--down)"/>
<line x1="872.9" y1="385.0" x2="872.9" y2="428.7" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="392.8" width="2.44" height="26.1" fill="var(--down)"/>
<line x1="876.8" y1="385.0" x2="876.8" y2="410.7" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="391.6" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="880.8" y1="388.8" x2="880.8" y2="419.8" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="392.1" width="2.44" height="18.5" fill="var(--down)"/>
<line x1="884.7" y1="406.0" x2="884.7" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="411.6" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="888.6" y1="377.8" x2="888.6" y2="401.9" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="395.0" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="892.6" y1="376.0" x2="892.6" y2="396.5" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="388.0" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="896.5" y1="395.8" x2="896.5" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="401.3" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="900.4" y1="368.0" x2="900.4" y2="417.9" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="381.2" width="2.44" height="27.2" fill="var(--down)"/>
<line x1="904.4" y1="375.6" x2="904.4" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="393.9" width="2.44" height="17.4" fill="var(--down)"/>
<line x1="908.3" y1="405.9" x2="908.3" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="417.0" width="2.44" height="26.9" fill="var(--down)"/>
<line x1="912.3" y1="446.8" x2="912.3" y2="470.7" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="457.8" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="916.2" y1="449.6" x2="916.2" y2="466.5" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="457.7" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="920.1" y1="433.7" x2="920.1" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="445.2" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="924.1" y1="394.3" x2="924.1" y2="454.3" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="398.1" width="2.44" height="56.2" fill="var(--up)"/>
<line x1="928.0" y1="377.8" x2="928.0" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="926.78" y="379.1" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="931.9" y1="371.5" x2="931.9" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="380.5" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="935.9" y1="385.2" x2="935.9" y2="427.1" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="385.4" width="2.44" height="34.8" fill="var(--down)"/>
<line x1="939.8" y1="426.0" x2="939.8" y2="481.6" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="431.4" width="2.44" height="45.4" fill="var(--down)"/>
<line x1="943.7" y1="470.2" x2="943.7" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="481.0" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="947.7" y1="426.3" x2="947.7" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="436.2" width="2.44" height="31.5" fill="var(--up)"/>
<line x1="951.6" y1="411.0" x2="951.6" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="419.7" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="955.6" y1="393.4" x2="955.6" y2="451.6" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="407.7" width="2.44" height="23.9" fill="var(--up)"/>
<line x1="959.5" y1="397.8" x2="959.5" y2="572.2" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="398.0" width="2.44" height="145.4" fill="var(--down)"/>
<line x1="963.4" y1="494.8" x2="963.4" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="520.0" width="2.44" height="14.9" fill="var(--up)"/>
<line x1="967.4" y1="505.9" x2="967.4" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="516.6" width="2.44" height="14.1" fill="var(--down)"/>
<line x1="971.3" y1="503.7" x2="971.3" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="531.0" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="975.2" y1="515.5" x2="975.2" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="531.6" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="979.2" y1="509.4" x2="979.2" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="526.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="983.1" y1="498.1" x2="983.1" y2="525.1" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="512.0" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="987.0" y1="511.6" x2="987.0" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="985.83" y="524.7" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="991.0" y1="485.0" x2="991.0" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="485.1" width="2.44" height="39.5" fill="var(--up)"/>
<line x1="994.9" y1="477.0" x2="994.9" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="477.8" width="2.44" height="31.9" fill="var(--down)"/>
<line x1="998.9" y1="508.7" x2="998.9" y2="555.8" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="512.5" width="2.44" height="40.3" fill="var(--down)"/>
<line x1="1002.8" y1="519.7" x2="1002.8" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="521.0" width="2.44" height="27.7" fill="var(--up)"/>
<line x1="1006.7" y1="517.7" x2="1006.7" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="524.9" width="2.44" height="29.1" fill="var(--down)"/>
<line x1="1010.7" y1="542.2" x2="1010.7" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="546.3" width="2.44" height="22.0" fill="var(--down)"/>
<line x1="1014.6" y1="559.8" x2="1014.6" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="567.0" width="2.44" height="9.8" fill="var(--down)"/>
<line x1="1018.5" y1="552.3" x2="1018.5" y2="569.6" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="562.6" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="1022.5" y1="541.2" x2="1022.5" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="549.1" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="1026.4" y1="541.7" x2="1026.4" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="549.0" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="1030.3" y1="555.8" x2="1030.3" y2="583.9" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="558.2" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="1034.3" y1="581.8" x2="1034.3" y2="597.2" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="586.1" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="1038.2" y1="574.4" x2="1038.2" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="591.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1042.2" y1="575.8" x2="1042.2" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="581.1" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="1046.1" y1="562.7" x2="1046.1" y2="587.2" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="573.8" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="1050.0" y1="529.4" x2="1050.0" y2="579.8" stroke="var(--up)" class="wick"/>
<rect x="1048.81" y="530.9" width="2.44" height="49.0" fill="var(--up)"/>
<line x1="60" y1="372.7" x2="1052" y2="372.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="376.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$144 R1</text>
<text x="1058" y="388.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="279.8" x2="1052" y2="279.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="283.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$159 R2</text>
<text x="1058" y="295.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="188.9" x2="1052" y2="188.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="192.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$173 R3</text>
<text x="1058" y="204.4" font-size="9.5" fill="var(--muted)">터치 7회</text>
<circle cx="1052.0" cy="530.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="522.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $119 (2026-09-04)</text>
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

!!! warning "이 표에는 지지선이 하나도 없다 — 표본 부족이 아니라 신저가 구간이기 때문이다"
    현재가 $119.02는 **1년 창 안에서 형성된 모든 스윙 저점 클러스터보다 아래**에 있다. 알고리즘이 잡아낸 클러스터 3개가 전부 저항선(R1~R3)인 이유이며, **하방에 참고할 가격대가 없다**는 뜻이다. 이 경우 지지 판단은 5년 구조를 보는 [기술적 분석 (주봉)](./10_technical_weekly.md)로 넘긴다.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $173 | 7 | 2025-09-22·10-03·10-16·11-20·12-12·2026-01-05·2026-04-14 — **터치 7회로 가장 두꺼운 클러스터.** 2025년 가을부터 2026년 4월까지 반복해서 닿았고 결국 뚫지 못한 자리다. 52주 최고($189.96)는 이보다 위지만 클러스터를 이루지 못했다 |
| R2 | $159 | 3 | 2026-01-15·2026-01-28·2026-05-05 — **LS Power 인수 종결(2026-01-29) 전후 구간.** FY2025 말 종가 $159.24와 사실상 같은 자리다 |
| R1 | $144 | 3 | 2026-05-26·2026-07-14·2026-07-24 — 하락 과정에서 세 번 저항으로 작동한 자리. **현재가에서 가장 가까운 저항(+21.0%)** |
| **현재가** | **$119.02** (2026-09-04 종가) | — | **기간 내 하단 지지 없음(신저가 구간)** — 가장 가까운 클러스터는 위쪽 R1이다 |
| 참고선 | $108.34 | — | **52주 최저**. 터치 2회 미만이라 클러스터로 잡히지 않았고, 지지대가 아니라 기간 내 최저 관측치로만 본다 |

---

## 3. 관측된 특이 구간 — 저항이 세 계단 내려오는 동안 지지가 하나도 만들어지지 않았다

이 종목에도 하루 만에 가격대를 재설정한 단일 이벤트는 없다. 대신 **1년 내내 한 방향으로 밀린 결과, 저항 클러스터만 세 개 쌓이고 지지 클러스터는 하나도 만들어지지 않은 것**이 이 차트의 구조다.

- R3($173, 2025년 9월~2026년 4월, 터치 7회) → R2($159, 2026년 1~5월) → R1($144, 2026년 5~7월)로 계단식 하락했고, **각 계단에서 반등이 나왔지만 직전 고점을 회복한 적이 없다.**
- **가격 하락과 사업 규모 확대가 정확히 반대로 갔다.** 같은 기간에 LS Power 인수 종결(2026-01-29, 설비용량 두 배), CEO 교체(2026-04-30), 첫 1.2 GW 데이터센터 계약(2026-08-04)이 전부 있었다 — [최근 뉴스 / 이슈](./08_news.md) 로그 그대로다. **주가가 반응한 것은 이 사건들이 아니라 그 대가로 늘어난 부채**라는 해석이 [밸류에이션 / 적정주가](./06_valuation.md) 2절·[투자 판단](./07_investment.md) 3. 리스크의 내용과 일치한다.
- **2025년에 붙었던 프리미엄의 해소로 보는 것이 이 1년의 가장 단순한 설명이다.** FY2025 말 주가 $159.24는 같은 방법론의 적정주가($117.08) 대비 +36.0% 고평가였고([밸류에이션 / 적정주가](./06_valuation.md) 2절), 현재가 $119.02는 그 적정주가 근처로 되돌아온 자리다. **R2($159)가 FY2025 말 종가와 같은 위치라는 점이 이 해석을 뒷받침한다.**
- 하방에 클러스터가 없다는 사실은 **"여기서 지지받는다"고 말할 근거도, "여기서 무너진다"고 말할 근거도 없다**는 뜻이다. 52주 최저 $108.34가 유일한 아래쪽 참고점이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-05~2026-09-04. 수집 시점: 2026-09-07. **원주가(과거 분할은 소급 반영, 배당은 미반영)**
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py NRG --name "NRG Energy" --close-on 2026-09-04 --emit all` (재현용, 옵션 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨을 3개가 아니라 저항 3개만 표시한 것은 강제한 결과가 아니다** — 터치 2회 이상 조건을 만족하는 하단 클러스터가 실제로 없었다. `--force-level`은 쓰지 않았다.
    - **기간 내 배당이 4회 있었으나 원주가라 반영되지 않았다.** 배당수익률 1.60%로 [Vistra](../vistra/09_technical_daily.md)(0.62%)보다 높아, 배당 재투자 기준 수익률과의 차이도 그만큼 크다.
    - **해당 기간에 주식분할은 없었으나 주식수가 늘었다.** LS Power 인수 대가로 신주가 발행돼 희석 가중평균 주식수가 2026 Q2에 전년 동기 대비 **+8.2%** 증가했다([핵심 지표](./04_metrics.md) A.4 각주 20). **주당 가격 하락폭이 시가총액 하락폭보다 크다는 뜻**이며, 이 차트는 주당 가격만 보여준다.

---

*작성일: 2026-09-07*
