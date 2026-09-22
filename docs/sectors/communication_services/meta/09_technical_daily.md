# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-22 종가 **$736.59**는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 기준 종가와 **일치한다.**

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-23 ~ 2026-09-22)


<style>
.meta-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .meta-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.meta-chart svg { width:100%; height:auto; display:block; }
.meta-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.meta-chart .title { fill: var(--ink); font-weight:600; }
.meta-chart .grid { stroke: var(--grid); stroke-width:1; }
.meta-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="meta-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Meta(META) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Meta (META) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-23 ~ 2026-09-22 · 마지막 종가 $736.59 (2026-09-22) · 단위 USD</text>
<line x1="60" y1="541.6" x2="1052" y2="541.6" class="grid"/>
<text x="52" y="545.6" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="436.0" x2="1052" y2="436.0" class="grid"/>
<text x="52" y="440.0" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="330.4" x2="1052" y2="330.4" class="grid"/>
<text x="52" y="334.4" font-size="11" text-anchor="end" fill="var(--muted)">650</text>
<line x1="60" y1="224.9" x2="1052" y2="224.9" class="grid"/>
<text x="52" y="228.9" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="60" y1="119.3" x2="1052" y2="119.3" class="grid"/>
<text x="52" y="123.3" font-size="11" text-anchor="end" fill="var(--muted)">750</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="85.7" y1="626.0" x2="85.7" y2="631.0" class="axis"/>
<text x="85.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="176.6" y1="626.0" x2="176.6" y2="631.0" class="axis"/>
<text x="176.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="251.7" y1="626.0" x2="251.7" y2="631.0" class="axis"/>
<text x="251.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="338.6" y1="626.0" x2="338.6" y2="631.0" class="axis"/>
<text x="338.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="417.7" y1="626.0" x2="417.7" y2="631.0" class="axis"/>
<text x="417.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="492.8" y1="626.0" x2="492.8" y2="631.0" class="axis"/>
<text x="492.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="579.7" y1="626.0" x2="579.7" y2="631.0" class="axis"/>
<text x="579.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="662.7" y1="626.0" x2="662.7" y2="631.0" class="axis"/>
<text x="662.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="741.8" y1="626.0" x2="741.8" y2="631.0" class="axis"/>
<text x="741.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="824.7" y1="626.0" x2="824.7" y2="631.0" class="axis"/>
<text x="824.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="911.7" y1="626.0" x2="911.7" y2="631.0" class="axis"/>
<text x="911.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="994.7" y1="626.0" x2="994.7" y2="631.0" class="axis"/>
<text x="994.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="75.8" x2="62.0" y2="117.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="78.7" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="65.9" y1="95.9" x2="65.9" y2="114.0" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="96.8" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="69.9" y1="105.0" x2="69.9" y2="130.8" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="112.0" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="73.8" y1="115.3" x2="73.8" y2="146.0" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="119.3" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="77.8" y1="117.7" x2="77.8" y2="142.2" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="122.0" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="81.7" y1="134.2" x2="81.7" y2="169.4" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="135.7" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="85.7" y1="178.8" x2="85.7" y2="203.4" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="179.5" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="89.6" y1="166.3" x2="89.6" y2="186.6" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="167.8" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="93.6" y1="159.4" x2="93.6" y2="203.4" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="162.3" width="2.45" height="40.3" fill="var(--down)"/>
<line x1="97.5" y1="189.3" x2="97.5" y2="244.9" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="191.8" width="2.45" height="22.1" fill="var(--up)"/>
<line x1="101.5" y1="185.8" x2="101.5" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="187.5" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="105.5" y1="183.4" x2="105.5" y2="208.4" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="187.2" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="109.4" y1="154.1" x2="109.4" y2="198.6" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="154.1" width="2.45" height="32.2" fill="var(--up)"/>
<line x1="113.4" y1="150.4" x2="113.4" y2="215.4" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="159.6" width="2.45" height="54.1" fill="var(--down)"/>
<line x1="117.3" y1="182.8" x2="117.3" y2="208.8" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="191.7" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="121.3" y1="192.1" x2="121.3" y2="226.3" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="206.6" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="125.2" y1="174.4" x2="125.2" y2="204.8" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="187.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="129.2" y1="171.1" x2="129.2" y2="216.7" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="187.8" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="133.1" y1="185.7" x2="133.1" y2="212.0" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="189.2" width="2.45" height="20.8" fill="var(--up)"/>
<line x1="137.1" y1="153.6" x2="137.1" y2="182.3" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="157.0" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="141.0" y1="143.6" x2="141.0" y2="164.2" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="148.8" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="145.0" y1="139.2" x2="145.0" y2="174.2" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="153.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="148.9" y1="135.4" x2="148.9" y2="155.0" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="151.6" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="152.9" y1="137.9" x2="152.9" y2="159.1" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="143.9" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="156.8" y1="107.2" x2="156.8" y2="123.5" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="117.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="160.8" y1="101.6" x2="160.8" y2="128.8" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="113.8" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="164.7" y1="100.0" x2="164.7" y2="135.1" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="109.3" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="168.7" y1="265.1" x2="168.7" y2="330.1" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="290.0" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="172.6" y1="277.9" x2="172.6" y2="339.8" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="278.7" width="2.45" height="55.2" fill="var(--down)"/>
<line x1="176.6" y1="310.7" x2="176.6" y2="359.6" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="317.8" width="2.45" height="38.6" fill="var(--down)"/>
<line x1="180.5" y1="347.9" x2="180.5" y2="381.1" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="376.8" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="184.5" y1="346.8" x2="184.5" y2="380.0" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="360.1" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="188.4" y1="360.0" x2="188.4" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="360.3" width="2.45" height="35.7" fill="var(--down)"/>
<line x1="192.4" y1="389.3" x2="192.4" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="390.2" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="196.4" y1="362.1" x2="196.4" y2="397.8" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="369.0" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="200.3" y1="373.6" x2="200.3" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="376.9" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="204.3" y1="374.8" x2="204.3" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="376.6" width="2.45" height="40.4" fill="var(--down)"/>
<line x1="208.2" y1="398.7" x2="208.2" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="408.4" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="212.2" y1="407.1" x2="212.2" y2="446.1" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="416.0" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="216.1" y1="411.3" x2="216.1" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="416.9" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="220.1" y1="428.3" x2="220.1" y2="470.2" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="440.9" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="224.0" y1="445.9" x2="224.0" y2="475.6" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="449.3" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="228.0" y1="421.8" x2="228.0" y2="471.2" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="428.6" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="231.9" y1="440.0" x2="231.9" y2="474.3" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="448.1" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="235.9" y1="400.7" x2="235.9" y2="441.0" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="408.5" width="2.45" height="30.3" fill="var(--up)"/>
<line x1="239.8" y1="357.8" x2="239.8" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="359.5" width="2.45" height="25.8" fill="var(--up)"/>
<line x1="243.8" y1="355.0" x2="243.8" y2="369.2" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="356.4" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="247.7" y1="334.6" x2="247.7" y2="361.1" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="334.8" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="251.7" y1="340.3" x2="251.7" y2="356.3" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="349.7" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="255.6" y1="334.9" x2="255.6" y2="355.6" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="336.6" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="259.6" y1="332.9" x2="259.6" y2="356.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="342.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="263.5" y1="275.3" x2="263.5" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="275.6" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="267.5" y1="278.3" x2="267.5" y2="304.3" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="281.0" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="271.4" y1="274.1" x2="271.4" y2="298.6" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="289.6" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="275.4" y1="299.9" x2="275.4" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="301.4" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="279.3" y1="320.9" x2="279.3" y2="344.4" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="330.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="283.3" y1="319.3" x2="283.3" y2="349.9" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="324.7" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="287.3" y1="201.7" x2="287.3" y2="354.5" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="330.9" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="291.2" y1="324.1" x2="291.2" y2="354.3" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="335.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="295.2" y1="304.0" x2="295.2" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="315.3" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="299.1" y1="306.7" x2="299.1" y2="332.1" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="318.6" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="303.1" y1="287.0" x2="303.1" y2="316.8" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="299.9" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="307.0" y1="286.1" x2="307.0" y2="313.2" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="295.8" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="311.0" y1="280.7" x2="311.0" y2="316.4" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="305.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="314.9" y1="296.7" x2="314.9" y2="313.0" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="298.9" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="318.9" y1="292.1" x2="318.9" y2="304.7" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="293.4" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="322.8" y1="290.4" x2="322.8" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="292.3" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="326.8" y1="308.8" x2="326.8" y2="321.2" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="312.1" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="330.7" y1="283.5" x2="330.7" y2="313.9" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="296.8" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="334.7" y1="298.8" x2="334.7" y2="310.5" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="299.3" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="338.6" y1="300.1" x2="338.6" y2="344.2" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="303.6" width="2.45" height="26.0" fill="var(--down)"/>
<line x1="342.6" y1="299.7" x2="342.6" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="311.9" width="2.45" height="16.4" fill="var(--up)"/>
<line x1="346.5" y1="297.7" x2="346.5" y2="326.4" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="308.0" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="350.5" y1="311.1" x2="350.5" y2="341.4" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="318.5" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="354.4" y1="336.6" x2="354.4" y2="360.6" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="338.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="358.4" y1="320.0" x2="358.4" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="324.0" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="362.3" y1="322.1" x2="362.3" y2="349.0" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="325.1" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="366.3" y1="346.8" x2="366.3" y2="385.1" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="346.8" width="2.45" height="23.6" fill="var(--down)"/>
<line x1="370.2" y1="375.9" x2="370.2" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="380.1" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="374.2" y1="385.0" x2="374.2" y2="406.0" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="392.1" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="378.2" y1="374.6" x2="378.2" y2="393.6" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="385.0" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="382.1" y1="411.9" x2="382.1" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="419.4" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="386.1" y1="397.4" x2="386.1" y2="435.8" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="408.6" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="390.0" y1="308.1" x2="390.0" y2="380.0" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="335.4" width="2.45" height="38.6" fill="var(--up)"/>
<line x1="394.0" y1="295.6" x2="394.0" y2="342.2" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="312.0" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="397.9" y1="277.1" x2="397.9" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="283.2" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="401.9" y1="273.8" x2="401.9" y2="299.5" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="278.5" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="405.8" y1="272.0" x2="405.8" y2="296.5" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="278.7" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="409.8" y1="132.0" x2="409.8" y2="198.4" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="144.0" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="413.7" y1="157.0" x2="413.7" y2="196.2" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="166.8" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="417.7" y1="179.9" x2="417.7" y2="217.5" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="194.1" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="421.6" y1="189.0" x2="421.6" y2="253.6" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="209.3" width="2.45" height="33.1" fill="var(--down)"/>
<line x1="425.6" y1="248.5" x2="425.6" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="250.8" width="2.45" height="39.6" fill="var(--down)"/>
<line x1="429.5" y1="263.9" x2="429.5" y2="323.1" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="287.8" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="433.5" y1="284.0" x2="433.5" y2="337.8" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="297.7" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="437.4" y1="260.1" x2="437.4" y2="311.9" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="273.0" width="2.45" height="29.6" fill="var(--up)"/>
<line x1="441.4" y1="265.7" x2="441.4" y2="288.7" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="272.2" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="445.3" y1="268.7" x2="445.3" y2="315.5" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="279.8" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="449.3" y1="275.6" x2="449.3" y2="340.4" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="288.3" width="2.45" height="42.6" fill="var(--down)"/>
<line x1="453.2" y1="327.4" x2="453.2" y2="363.0" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="340.8" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="457.2" y1="346.1" x2="457.2" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="352.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="461.1" y1="341.0" x2="461.1" y2="376.6" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="344.8" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="465.1" y1="336.4" x2="465.1" y2="358.5" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="341.5" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="469.1" y1="302.3" x2="469.1" y2="354.1" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="318.5" width="2.45" height="33.7" fill="var(--up)"/>
<line x1="473.0" y1="314.2" x2="473.0" y2="360.0" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="325.1" width="2.45" height="32.3" fill="var(--down)"/>
<line x1="477.0" y1="349.2" x2="477.0" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="353.0" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="480.9" y1="322.3" x2="480.9" y2="347.0" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="322.7" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="484.9" y1="307.2" x2="484.9" y2="335.7" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="315.6" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="488.8" y1="331.6" x2="488.8" y2="355.5" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="334.3" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="492.8" y1="309.5" x2="492.8" y2="363.2" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="322.9" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="496.7" y1="311.4" x2="496.7" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="319.7" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="500.7" y1="282.4" x2="500.7" y2="314.3" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="293.0" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="504.6" y1="286.7" x2="504.6" y2="329.8" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="305.3" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="508.6" y1="331.6" x2="508.6" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="334.9" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="512.5" y1="335.2" x2="512.5" y2="379.5" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="336.0" width="2.45" height="26.6" fill="var(--up)"/>
<line x1="516.5" y1="308.7" x2="516.5" y2="332.6" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="321.9" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="520.4" y1="311.2" x2="520.4" y2="333.9" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="320.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="524.4" y1="323.1" x2="524.4" y2="358.1" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="333.1" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="528.3" y1="374.4" x2="528.3" y2="415.8" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="385.6" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="532.3" y1="362.6" x2="532.3" y2="387.2" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="368.4" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="536.2" y1="358.8" x2="536.2" y2="390.2" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="376.9" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="540.2" y1="388.2" x2="540.2" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="401.5" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="544.1" y1="408.6" x2="544.1" y2="431.2" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="410.3" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="548.1" y1="427.6" x2="548.1" y2="462.9" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="428.5" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="552.0" y1="417.8" x2="552.0" y2="438.1" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="423.8" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="556.0" y1="433.9" x2="556.0" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="437.9" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="560.0" y1="428.3" x2="560.0" y2="449.9" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="438.7" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="563.9" y1="471.9" x2="563.9" y2="555.6" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="473.0" width="2.45" height="73.8" fill="var(--down)"/>
<line x1="567.9" y1="555.1" x2="567.9" y2="604.3" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="562.5" width="2.45" height="30.4" fill="var(--down)"/>
<line x1="571.8" y1="563.6" x2="571.8" y2="586.9" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="570.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="575.8" y1="491.5" x2="575.8" y2="548.4" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="494.8" width="2.45" height="46.8" fill="var(--up)"/>
<line x1="579.7" y1="451.7" x2="579.7" y2="491.3" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="477.9" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="583.7" y1="481.4" x2="583.7" y2="521.1" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="489.9" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="587.6" y1="472.3" x2="587.6" y2="495.1" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="483.1" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="591.6" y1="488.3" x2="591.6" y2="510.4" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="488.7" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="595.5" y1="372.8" x2="595.5" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="409.8" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="599.5" y1="356.8" x2="599.5" y2="387.4" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="376.1" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="603.4" y1="354.6" x2="603.4" y2="384.6" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="363.2" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="607.4" y1="362.1" x2="607.4" y2="384.5" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="363.1" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="611.3" y1="296.1" x2="611.3" y2="352.9" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="304.1" width="2.45" height="40.7" fill="var(--up)"/>
<line x1="615.3" y1="270.3" x2="615.3" y2="300.4" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="284.9" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="619.2" y1="272.2" x2="619.2" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="273.7" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="623.2" y1="242.8" x2="623.2" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="249.1" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="627.1" y1="260.0" x2="627.1" y2="292.4" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="264.2" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="631.1" y1="275.1" x2="631.1" y2="293.9" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="286.1" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="635.0" y1="270.5" x2="635.0" y2="288.8" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="278.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="639.0" y1="289.2" x2="639.0" y2="324.0" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="301.5" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="642.9" y1="265.7" x2="642.9" y2="322.3" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="277.6" width="2.45" height="31.1" fill="var(--up)"/>
<line x1="646.9" y1="261.8" x2="646.9" y2="286.4" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="270.0" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="650.9" y1="271.0" x2="650.9" y2="297.4" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="279.3" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="654.8" y1="279.2" x2="654.8" y2="301.3" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="290.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="658.8" y1="392.0" x2="658.8" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="395.2" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="662.7" y1="396.1" x2="662.7" y2="423.1" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="405.0" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="666.7" y1="406.4" x2="666.7" y2="430.2" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="414.0" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="670.6" y1="405.7" x2="670.6" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="407.9" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="674.6" y1="393.9" x2="674.6" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="408.8" width="2.45" height="25.0" fill="var(--up)"/>
<line x1="678.5" y1="383.3" x2="678.5" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="400.5" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="682.5" y1="400.6" x2="682.5" y2="423.2" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="403.9" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="686.4" y1="425.6" x2="686.4" y2="440.1" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="426.4" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="690.4" y1="428.1" x2="690.4" y2="451.6" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="429.7" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="694.3" y1="394.0" x2="694.3" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="400.9" width="2.45" height="37.6" fill="var(--up)"/>
<line x1="698.3" y1="385.9" x2="698.3" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="397.1" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="702.2" y1="391.2" x2="702.2" y2="416.3" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="406.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="706.2" y1="403.1" x2="706.2" y2="428.2" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="412.3" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="710.1" y1="406.6" x2="710.1" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="417.2" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="714.1" y1="419.1" x2="714.1" y2="440.6" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="425.3" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="718.0" y1="415.7" x2="718.0" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="420.4" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="722.0" y1="404.7" x2="722.0" y2="421.3" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="414.3" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="725.9" y1="405.5" x2="725.9" y2="424.8" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="409.9" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="729.9" y1="354.7" x2="729.9" y2="417.0" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="361.6" width="2.45" height="54.6" fill="var(--up)"/>
<line x1="733.8" y1="345.2" x2="733.8" y2="374.1" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="352.6" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="737.8" y1="363.2" x2="737.8" y2="386.7" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="365.3" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="741.8" y1="360.5" x2="741.8" y2="437.0" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="371.8" width="2.45" height="63.2" fill="var(--down)"/>
<line x1="745.7" y1="417.3" x2="745.7" y2="443.0" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="429.2" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="749.7" y1="385.0" x2="749.7" y2="435.4" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="387.5" width="2.45" height="42.2" fill="var(--up)"/>
<line x1="753.6" y1="346.5" x2="753.6" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="377.8" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="757.6" y1="374.5" x2="757.6" y2="472.1" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="386.5" width="2.45" height="64.3" fill="var(--down)"/>
<line x1="761.5" y1="452.9" x2="761.5" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="452.9" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="765.5" y1="441.0" x2="765.5" y2="476.1" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="455.0" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="769.4" y1="454.3" x2="769.4" y2="498.1" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="476.7" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="773.4" y1="494.8" x2="773.4" y2="526.8" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="502.6" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="777.3" y1="486.5" x2="777.3" y2="518.5" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="493.1" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="781.3" y1="433.3" x2="781.3" y2="479.7" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="449.8" width="2.45" height="28.7" fill="var(--up)"/>
<line x1="785.2" y1="423.7" x2="785.2" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="435.6" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="789.2" y1="449.1" x2="789.2" y2="507.4" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="452.9" width="2.45" height="51.6" fill="var(--down)"/>
<line x1="793.1" y1="477.8" x2="793.1" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="484.1" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="797.1" y1="487.1" x2="797.1" y2="520.8" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="495.1" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="801.0" y1="494.7" x2="801.0" y2="518.3" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="515.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="805.0" y1="501.4" x2="805.0" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="516.5" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="808.9" y1="528.2" x2="808.9" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="529.8" width="2.45" height="26.8" fill="var(--down)"/>
<line x1="812.9" y1="527.1" x2="812.9" y2="561.8" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="541.0" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="816.8" y1="497.4" x2="816.8" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="515.0" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="820.8" y1="508.7" x2="820.8" y2="538.5" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="513.5" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="824.7" y1="376.3" x2="824.7" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="408.7" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="828.7" y1="414.9" x2="828.7" y2="477.3" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="419.3" width="2.45" height="52.8" fill="var(--down)"/>
<line x1="832.7" y1="428.4" x2="832.7" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="435.4" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="836.6" y1="382.4" x2="836.6" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="403.1" width="2.45" height="16.9" fill="var(--up)"/>
<line x1="840.6" y1="402.2" x2="840.6" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="405.6" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="844.5" y1="365.8" x2="844.5" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="369.5" width="2.45" height="100.3" fill="var(--up)"/>
<line x1="848.5" y1="271.6" x2="848.5" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="289.9" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="852.4" y1="274.2" x2="852.4" y2="321.6" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="306.4" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="856.4" y1="295.6" x2="856.4" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="307.1" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="860.3" y1="254.3" x2="860.3" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="264.3" width="2.45" height="37.4" fill="var(--up)"/>
<line x1="864.3" y1="263.1" x2="864.3" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="272.9" width="2.45" height="26.9" fill="var(--down)"/>
<line x1="868.2" y1="325.8" x2="868.2" y2="381.1" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="335.3" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="872.2" y1="323.5" x2="872.2" y2="360.0" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="337.4" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="876.1" y1="318.0" x2="876.1" y2="344.8" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="321.6" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="880.1" y1="332.6" x2="880.1" y2="385.3" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="335.3" width="2.45" height="43.3" fill="var(--down)"/>
<line x1="884.0" y1="405.1" x2="884.0" y2="441.9" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="418.2" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="888.0" y1="414.9" x2="888.0" y2="447.7" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="424.8" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="891.9" y1="412.2" x2="891.9" y2="450.5" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="420.8" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="895.9" y1="433.9" x2="895.9" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="442.7" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="899.8" y1="436.1" x2="899.8" y2="473.5" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="450.2" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="903.8" y1="562.9" x2="903.8" y2="595.4" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="564.7" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="907.7" y1="524.0" x2="907.7" y2="562.2" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="527.4" width="2.45" height="27.7" fill="var(--up)"/>
<line x1="911.7" y1="441.2" x2="911.7" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="456.6" width="2.45" height="59.1" fill="var(--up)"/>
<line x1="915.6" y1="451.2" x2="915.6" y2="481.9" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="461.5" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="919.6" y1="433.9" x2="919.6" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="435.0" width="2.45" height="24.7" fill="var(--down)"/>
<line x1="923.6" y1="445.9" x2="923.6" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="457.3" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="927.5" y1="438.7" x2="927.5" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="452.7" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="931.5" y1="418.7" x2="931.5" y2="452.8" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="437.8" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="935.4" y1="409.8" x2="935.4" y2="449.9" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="437.9" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="939.4" y1="426.5" x2="939.4" y2="482.0" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="433.7" width="2.45" height="46.9" fill="var(--down)"/>
<line x1="943.3" y1="444.8" x2="943.3" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="446.6" width="2.45" height="30.1" fill="var(--up)"/>
<line x1="947.3" y1="432.1" x2="947.3" y2="458.6" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="442.4" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="951.2" y1="456.6" x2="951.2" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="457.6" width="2.45" height="43.9" fill="var(--down)"/>
<line x1="955.2" y1="519.1" x2="955.2" y2="555.9" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="525.8" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="959.1" y1="533.0" x2="959.1" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="549.9" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="963.1" y1="541.6" x2="963.1" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="548.0" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="967.0" y1="533.4" x2="967.0" y2="555.8" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="541.8" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="971.0" y1="517.4" x2="971.0" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="522.5" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="974.9" y1="497.6" x2="974.9" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="499.2" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="978.9" y1="450.1" x2="978.9" y2="516.5" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="456.5" width="2.45" height="29.9" fill="var(--down)"/>
<line x1="982.8" y1="460.5" x2="982.8" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="485.7" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="986.8" y1="458.8" x2="986.8" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="482.4" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="990.7" y1="481.0" x2="990.7" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="483.2" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="994.7" y1="467.8" x2="994.7" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="481.3" width="2.45" height="42.6" fill="var(--up)"/>
<line x1="998.6" y1="435.2" x2="998.6" y2="484.6" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="451.1" width="2.45" height="29.7" fill="var(--up)"/>
<line x1="1002.6" y1="394.9" x2="1002.6" y2="426.8" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="413.5" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="1006.5" y1="399.1" x2="1006.5" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="400.6" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="1010.5" y1="383.6" x2="1010.5" y2="415.4" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="401.8" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="1014.5" y1="313.9" x2="1014.5" y2="354.6" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="322.7" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="1018.4" y1="301.9" x2="1018.4" y2="347.0" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="322.6" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="1022.4" y1="300.4" x2="1022.4" y2="338.5" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="323.0" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="1026.3" y1="291.2" x2="1026.3" y2="332.1" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="297.5" width="2.45" height="16.4" fill="var(--up)"/>
<line x1="1030.3" y1="269.5" x2="1030.3" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="287.7" width="2.45" height="23.1" fill="var(--up)"/>
<line x1="1034.2" y1="255.9" x2="1034.2" y2="284.2" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="267.3" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="1038.2" y1="260.4" x2="1038.2" y2="294.5" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="262.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1042.1" y1="245.7" x2="1042.1" y2="307.6" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="248.9" width="2.45" height="48.3" fill="var(--down)"/>
<line x1="1046.1" y1="113.0" x2="1046.1" y2="268.0" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="137.8" width="2.45" height="128.7" fill="var(--up)"/>
<line x1="1050.0" y1="104.0" x2="1050.0" y2="161.6" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="147.6" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="60" y1="141.2" x2="1052" y2="141.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="144.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$740 R1</text>
<text x="1058" y="156.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="235.6" x2="1052" y2="235.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="229.6" font-size="11.5" fill="var(--support)" font-weight="600">$695 S1</text>
<text x="1058" y="241.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="365.5" x2="1052" y2="365.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="359.5" font-size="11.5" fill="var(--support)" font-weight="600">$633 S2</text>
<text x="1058" y="371.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="458.9" x2="1052" y2="458.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="452.9" font-size="11.5" fill="var(--support)" font-weight="600">$589 S3</text>
<text x="1058" y="464.9" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="147.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="139.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $737 (2026-09-22)</text>
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
| R1 | $740 | 2 | 2025-10-10·2026-01-29 — 1년 전 고점대. 2026-09-21 급등으로 거의 다시 닿았다(현재가 대비 +0.5%) |
| **현재가** | **$736.59** (2026-09-22 종가) | — | R1과 S1 사이 |
| S1 | $695 | 2 | 2025-10-06·2025-10-14 — 2025년 10월 급락 직전의 지지대. 현재가 대비 −5.6%이며, 9월 급등 이전 3개월간 이 위로 올라오지 못했다 |
| S2 | $633 | 2 | 2025-12-12·2026-02-18 — 연말·연초에 두 번 확인된 구간 |
| S3 | $589 | 5 | 2025-11-19·2026-01-20·2026-05-12·2026-05-21·2026-07-09 — 1년 중 터치 5회로 가장 두꺼운 지지대. 2분기 실적 발표 후 갭다운이 멈춘 자리도 이 부근이다 |

---

## 3. 관측된 특이 구간

이 1년 구간에는 성격이 반대인 두 사건이 있다.

**① 2026-07-30 2분기 실적 발표 후 갭다운**

- 2026-07-29 장 마감 후 2분기 실적과 함께 FY2026 총비용 가이던스 $165~169B 상향, CapEx $130~145B을 제시했다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−7.95%** ($585.61 → $539.03), 거래량은 평소(일 1,736만 주 내외) 대비 약 **2.4배**인 **4,227만 주**.
- 매출은 +28%로 견조했으므로 하락의 원인은 지출이다 — **이후 약 7주간 $540~690 박스에 갇혔고, 그 상단이 현재 S1($695)으로 잡혀 있다.**

**② 2026-09-21 Muse 흥행으로 하루 +11.34%**

- 개인 AI 에이전트 **Muse**가 미국 App Store·Google Play 무료 앱 1위에 오르고 Wells Fargo가 목표주가를 $640 → $796으로 상향했다.
- 종가 기준 전일 대비 **+11.34%** ($665.75 → $741.25)로 최근 1년 중 최대 상승일이며, 거래량은 평소 대비 약 **2.8배**인 **4,872만 주**. 하루 만에 ①이 만든 박스를 위로 이탈해 R1($740) 부근까지 올라왔다.
- **두 사건 사이에 확정 실적은 한 건도 없었다.** 즉 이 1년 차트에서 가장 큰 두 번의 가격 재설정은 각각 "비용 가이던스"와 "제품 반응"이 만든 것이고, 이익 숫자가 만든 것이 아니다 — [밸류에이션 / 적정주가](./06_valuation.md)의 괴리율 부호가 11일 만에 뒤집힌 배경이 여기 있다.


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-23~2026-09-22. 수집 시점: 2026-09-23. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py` (`META --name Meta --close-on 2026-09-22 --emit all`)

**한계**
- **원주가라 배당이 반영돼 있지 않다.** 기간 내 배당 5회(분기 $0.525). 상장 이후 분할이 없어 소급조정 이슈는 없다.
- **현재가가 R1에 거의 닿아 있다**($736.59 vs $740, +0.5%). 클러스터 허용오차(±2.5%) 안쪽이라 사실상 저항선 위인지 아래인지 구분되지 않는 위치다 — 이 구간에서 레벨 돌파 여부를 판정하지 않는 편이 안전하다.
- **S1~R1 사이가 비어 있다.** $695~$740 구간에 스윙이 쌓이지 않았는데, 2026-09-21에 이 구간을 하루 만에 갭으로 통과했기 때문이다. 되돌림이 오면 참고할 중간 레벨이 없다.

---

*작성일: 2026-09-23*
