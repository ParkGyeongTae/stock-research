# Circle Internet Group (서클) — 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, Yahoo Finance 일봉 API에서 직접 수집했다(1년 일봉은 `04_metrics.md`가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점의 종가 대조**: 2026-08-13 종가 $75.38은 `04_metrics.md` A.2·`06_valuation.md`에서 인용한 stockanalysis.com 기준값($75.38)과 정확히 일치한다. FY2025 회계연도 말(2025-12-31) 종가 $79.30 역시 `04_metrics.md` A.2 "FY2025" 열 값과 정확히 일치한다.
>
> ⚠️ 이 차트의 기간(2025-08-15~2026-08-14)은 IPO(2025-06-05)·상장 첫날 종가($83.23)·상장 후 최고가($298.99, 2025-06-23) 시점을 포함하지 않는다 — 그 이전 연혁은 [`02_history.md`](./02_history.md) 참고. 차트 기간 내 52주 최고가($159.47, 2025-10-10)는 상장 후 전고점($298.99) 대비 이미 크게 낮은 수준에서 시작한다는 점에 유의.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="crcl-chart">
<style>
.crcl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.crcl-chart svg { width:100%; height:auto; display:block; }
.crcl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.crcl-chart .title { fill: var(--ink); font-weight:600; }
.crcl-chart .grid { stroke: var(--grid); stroke-width:1; }
.crcl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Circle(CRCL) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Circle (CRCL) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $71.60 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="558.4" x2="1052" y2="558.4" class="grid"/>
<text x="52" y="562.4" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="461.8" x2="1052" y2="461.8" class="grid"/>
<text x="52" y="465.8" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="365.2" x2="1052" y2="365.2" class="grid"/>
<text x="52" y="369.2" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="268.5" x2="1052" y2="268.5" class="grid"/>
<text x="52" y="272.5" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="171.9" x2="1052" y2="171.9" class="grid"/>
<text x="52" y="175.9" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="75.3" x2="1052" y2="75.3" class="grid"/>
<text x="52" y="79.3" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="105.5" y1="626.0" x2="105.5" y2="631.0" class="axis"/>
<text x="105.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="188.4" y1="626.0" x2="188.4" y2="631.0" class="axis"/>
<text x="188.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="354.4" y1="626.0" x2="354.4" y2="631.0" class="axis"/>
<text x="354.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="441.4" y1="626.0" x2="441.4" y2="631.0" class="axis"/>
<text x="441.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="595.5" y1="626.0" x2="595.5" y2="631.0" class="axis"/>
<text x="595.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="682.5" y1="626.0" x2="682.5" y2="631.0" class="axis"/>
<text x="682.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="765.5" y1="626.0" x2="765.5" y2="631.0" class="axis"/>
<text x="765.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="844.5" y1="626.0" x2="844.5" y2="631.0" class="axis"/>
<text x="844.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="927.5" y1="626.0" x2="927.5" y2="631.0" class="axis"/>
<text x="927.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1014.5" y1="626.0" x2="1014.5" y2="631.0" class="axis"/>
<text x="1014.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="923.6" y1="56.0" x2="923.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="929.6" y="68.0" font-size="10.5" fill="var(--down)">2026-06-30 OUSD 컨소시엄 출범+FTSE Russell 지수 제외 겹쳐 급락</text>
<line x1="62.0" y1="116.5" x2="62.0" y2="175.6" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="127.2" width="2.45" height="39.2" fill="var(--up)"/>
<line x1="65.9" y1="126.3" x2="65.9" y2="165.4" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="129.9" width="2.45" height="34.4" fill="var(--down)"/>
<line x1="69.9" y1="149.5" x2="69.9" y2="205.2" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="152.7" width="2.45" height="42.3" fill="var(--down)"/>
<line x1="73.8" y1="174.3" x2="73.8" y2="224.6" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="182.5" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="77.8" y1="186.5" x2="77.8" y2="212.6" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="196.1" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="81.7" y1="149.2" x2="81.7" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="195.9" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="85.7" y1="194.5" x2="85.7" y2="245.8" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="199.2" width="2.45" height="44.1" fill="var(--down)"/>
<line x1="89.6" y1="219.0" x2="89.6" y2="248.4" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="224.8" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="93.6" y1="219.0" x2="93.6" y2="239.5" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="224.8" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="97.5" y1="206.8" x2="97.5" y2="231.5" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="215.7" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="101.5" y1="191.4" x2="101.5" y2="225.1" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="210.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="105.5" y1="212.1" x2="105.5" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="227.2" width="2.45" height="40.7" fill="var(--down)"/>
<line x1="109.4" y1="257.6" x2="109.4" y2="285.0" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="258.4" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="113.4" y1="267.0" x2="113.4" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="279.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="117.3" y1="274.3" x2="117.3" y2="326.4" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="279.3" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="121.3" y1="279.3" x2="121.3" y2="316.6" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="297.5" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="125.2" y1="264.9" x2="125.2" y2="304.2" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="278.3" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="129.2" y1="244.5" x2="129.2" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="268.7" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="133.1" y1="188.9" x2="133.1" y2="300.9" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="202.4" width="2.45" height="94.1" fill="var(--up)"/>
<line x1="137.1" y1="196.6" x2="137.1" y2="246.8" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="196.8" width="2.45" height="46.0" fill="var(--down)"/>
<line x1="141.0" y1="192.3" x2="141.0" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="200.7" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="145.0" y1="159.6" x2="145.0" y2="201.3" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="173.9" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="148.9" y1="140.5" x2="148.9" y2="228.6" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="196.1" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="152.9" y1="154.6" x2="152.9" y2="200.6" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="169.9" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="156.8" y1="134.7" x2="156.8" y2="174.2" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="147.5" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="160.8" y1="168.5" x2="160.8" y2="198.2" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="172.5" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="164.7" y1="164.2" x2="164.7" y2="216.9" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="178.4" width="2.45" height="37.2" fill="var(--down)"/>
<line x1="168.7" y1="189.6" x2="168.7" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="202.2" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="172.6" y1="219.0" x2="172.6" y2="247.8" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="225.1" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="176.6" y1="227.5" x2="176.6" y2="254.9" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="234.8" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="180.5" y1="182.6" x2="180.5" y2="227.5" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="202.6" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="184.5" y1="181.6" x2="184.5" y2="208.8" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="190.3" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="188.4" y1="185.1" x2="188.4" y2="231.8" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="202.8" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="192.4" y1="113.7" x2="192.4" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="125.0" width="2.45" height="78.6" fill="var(--up)"/>
<line x1="196.4" y1="92.4" x2="196.4" y2="151.9" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="131.4" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="200.3" y1="103.5" x2="200.3" y2="145.1" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="104.3" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="204.3" y1="87.1" x2="204.3" y2="151.7" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="114.0" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="208.2" y1="113.2" x2="208.2" y2="154.8" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="121.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="212.2" y1="104.9" x2="212.2" y2="143.9" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="119.8" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="216.1" y1="77.9" x2="216.1" y2="207.7" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="119.3" width="2.45" height="86.7" fill="var(--down)"/>
<line x1="220.1" y1="165.3" x2="220.1" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="181.3" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="224.0" y1="178.6" x2="224.0" y2="223.5" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="198.7" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="228.0" y1="166.6" x2="228.0" y2="207.8" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="184.9" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="231.9" y1="187.1" x2="231.9" y2="230.5" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="191.6" width="2.45" height="36.0" fill="var(--down)"/>
<line x1="235.9" y1="231.1" x2="235.9" y2="253.6" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="237.2" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="239.8" y1="192.6" x2="239.8" y2="228.7" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="216.3" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="243.8" y1="205.7" x2="243.8" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="218.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="247.7" y1="215.4" x2="247.7" y2="256.5" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="227.1" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="251.7" y1="220.2" x2="251.7" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="220.9" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="255.6" y1="152.5" x2="255.6" y2="215.3" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="162.0" width="2.45" height="43.9" fill="var(--up)"/>
<line x1="259.6" y1="136.0" x2="259.6" y2="181.1" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="138.5" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="263.5" y1="155.6" x2="263.5" y2="192.0" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="156.2" width="2.45" height="34.5" fill="var(--down)"/>
<line x1="267.5" y1="191.0" x2="267.5" y2="221.8" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="191.3" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="271.4" y1="220.2" x2="271.4" y2="256.5" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="220.4" width="2.45" height="35.1" fill="var(--down)"/>
<line x1="275.4" y1="223.1" x2="275.4" y2="245.0" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="234.8" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="279.3" y1="240.8" x2="279.3" y2="279.0" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="240.8" width="2.45" height="38.1" fill="var(--down)"/>
<line x1="283.3" y1="282.1" x2="283.3" y2="322.2" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="298.5" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="287.3" y1="293.4" x2="287.3" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="301.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="291.2" y1="300.6" x2="291.2" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="302.1" width="2.45" height="63.0" fill="var(--down)"/>
<line x1="295.2" y1="349.1" x2="295.2" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="350.0" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="299.1" y1="314.3" x2="299.1" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="327.5" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="303.1" y1="353.1" x2="303.1" y2="375.1" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="355.2" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="307.0" y1="386.8" x2="307.0" y2="433.5" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="394.9" width="2.45" height="36.5" fill="var(--down)"/>
<line x1="311.0" y1="421.1" x2="311.0" y2="455.1" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="432.7" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="314.9" y1="437.4" x2="314.9" y2="454.5" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="444.9" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="318.9" y1="452.6" x2="318.9" y2="485.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="453.1" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="322.8" y1="470.7" x2="322.8" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="478.2" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="326.8" y1="478.2" x2="326.8" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="478.7" width="2.45" height="32.7" fill="var(--down)"/>
<line x1="330.7" y1="503.3" x2="330.7" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="503.8" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="334.7" y1="498.8" x2="334.7" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="503.6" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="338.6" y1="493.5" x2="338.6" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="496.8" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="342.6" y1="509.5" x2="342.6" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="509.5" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="346.5" y1="494.2" x2="346.5" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="497.3" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="350.5" y1="454.6" x2="350.5" y2="490.6" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="462.1" width="2.45" height="22.3" fill="var(--up)"/>
<line x1="354.4" y1="462.5" x2="354.4" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="473.9" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="358.4" y1="458.2" x2="358.4" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="469.5" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="362.3" y1="429.9" x2="362.3" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="431.4" width="2.45" height="38.2" fill="var(--up)"/>
<line x1="366.3" y1="421.8" x2="366.3" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="425.7" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="370.2" y1="429.6" x2="370.2" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="432.3" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="374.2" y1="426.0" x2="374.2" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="428.2" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="378.2" y1="413.6" x2="378.2" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="418.9" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="382.1" y1="415.6" x2="382.1" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="421.1" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="386.1" y1="417.0" x2="386.1" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="420.4" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="390.0" y1="407.2" x2="390.0" y2="452.0" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="415.7" width="2.45" height="29.3" fill="var(--down)"/>
<line x1="394.0" y1="441.6" x2="394.0" y2="487.2" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="443.2" width="2.45" height="40.5" fill="var(--down)"/>
<line x1="397.9" y1="444.9" x2="397.9" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="447.3" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="401.9" y1="434.0" x2="401.9" y2="466.2" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="447.9" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="405.8" y1="440.2" x2="405.8" y2="461.4" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="448.5" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="409.8" y1="431.3" x2="409.8" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="432.2" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="413.7" y1="407.7" x2="413.7" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="424.4" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="417.7" y1="434.9" x2="417.7" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="438.6" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="421.6" y1="447.1" x2="421.6" y2="462.4" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="448.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="425.6" y1="449.7" x2="425.6" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="450.2" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="429.5" y1="447.1" x2="429.5" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="459.3" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="433.5" y1="447.8" x2="433.5" y2="463.5" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="460.9" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="437.4" y1="459.9" x2="437.4" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="462.0" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="441.4" y1="439.6" x2="441.4" y2="463.6" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="445.0" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="445.3" y1="422.8" x2="445.3" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="438.6" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="449.3" y1="431.8" x2="449.3" y2="452.4" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="432.8" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="453.2" y1="444.4" x2="453.2" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="446.4" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="457.2" y1="448.6" x2="457.2" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="453.1" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="461.1" y1="440.8" x2="461.1" y2="464.4" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="447.8" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="465.1" y1="446.7" x2="465.1" y2="462.5" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="447.8" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="469.1" y1="441.1" x2="469.1" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="445.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="473.0" y1="420.9" x2="473.0" y2="453.3" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="437.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="477.0" y1="443.5" x2="477.0" y2="480.6" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="445.0" width="2.45" height="33.2" fill="var(--down)"/>
<line x1="480.9" y1="461.7" x2="480.9" y2="483.1" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="468.5" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="484.9" y1="474.0" x2="484.9" y2="497.4" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="482.5" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="488.8" y1="487.9" x2="488.8" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="496.1" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="492.8" y1="491.7" x2="492.8" y2="506.4" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="492.9" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="496.7" y1="497.7" x2="496.7" y2="510.6" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="503.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="500.7" y1="498.3" x2="500.7" y2="510.8" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="505.7" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="504.6" y1="507.5" x2="504.6" y2="522.1" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="508.2" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="508.6" y1="476.3" x2="508.6" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="496.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="512.5" y1="507.2" x2="512.5" y2="530.6" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="508.6" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="516.5" y1="525.0" x2="516.5" y2="549.3" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="526.5" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="520.4" y1="549.3" x2="520.4" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="551.1" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="524.4" y1="557.6" x2="524.4" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="557.6" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="528.3" y1="576.3" x2="528.3" y2="599.3" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="576.8" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="532.3" y1="585.0" x2="532.3" y2="607.2" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="589.1" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="536.2" y1="569.0" x2="536.2" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="572.7" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="540.2" y1="554.1" x2="540.2" y2="578.9" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="557.9" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="544.1" y1="548.7" x2="544.1" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="559.6" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="548.1" y1="562.4" x2="548.1" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="562.7" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="552.0" y1="564.4" x2="552.0" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="564.4" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="556.0" y1="547.7" x2="556.0" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="558.2" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="560.0" y1="544.4" x2="560.0" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="550.5" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="563.9" y1="535.7" x2="563.9" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="543.2" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="567.9" y1="544.6" x2="567.9" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="547.4" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="571.8" y1="531.8" x2="571.8" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="543.8" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="575.8" y1="543.3" x2="575.8" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="548.3" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="579.7" y1="544.1" x2="579.7" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="551.8" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="583.7" y1="445.6" x2="583.7" y2="504.3" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="446.6" width="2.45" height="45.3" fill="var(--up)"/>
<line x1="587.6" y1="410.6" x2="587.6" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="426.9" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="591.6" y1="437.7" x2="591.6" y2="457.1" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="444.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="595.5" y1="381.5" x2="595.5" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="383.8" width="2.45" height="74.1" fill="var(--up)"/>
<line x1="599.5" y1="344.4" x2="599.5" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="366.9" width="2.45" height="39.3" fill="var(--up)"/>
<line x1="603.4" y1="334.5" x2="603.4" y2="358.4" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="339.7" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="607.4" y1="316.3" x2="607.4" y2="349.2" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="337.4" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="611.3" y1="334.8" x2="611.3" y2="364.8" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="351.5" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="615.3" y1="304.0" x2="615.3" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="308.0" width="2.45" height="32.0" fill="var(--up)"/>
<line x1="619.2" y1="259.8" x2="619.2" y2="303.3" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="277.8" width="2.45" height="22.5" fill="var(--up)"/>
<line x1="623.2" y1="252.1" x2="623.2" y2="308.5" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="269.5" width="2.45" height="33.8" fill="var(--down)"/>
<line x1="627.1" y1="279.3" x2="627.1" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="296.7" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="631.1" y1="271.9" x2="631.1" y2="301.6" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="276.6" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="635.0" y1="237.1" x2="635.0" y2="269.7" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="240.4" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="639.0" y1="188.1" x2="639.0" y2="255.3" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="209.1" width="2.45" height="40.1" fill="var(--up)"/>
<line x1="642.9" y1="193.7" x2="642.9" y2="229.9" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="206.5" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="646.9" y1="221.5" x2="646.9" y2="261.7" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="228.3" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="650.9" y1="208.7" x2="650.9" y2="254.5" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="230.0" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="654.8" y1="232.4" x2="654.8" y2="262.2" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="236.5" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="658.8" y1="234.3" x2="658.8" y2="373.3" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="237.9" width="2.45" height="121.6" fill="var(--down)"/>
<line x1="662.7" y1="315.6" x2="662.7" y2="357.4" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="332.5" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="666.7" y1="348.0" x2="666.7" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="355.9" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="670.6" y1="375.9" x2="670.6" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="376.1" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="674.6" y1="382.1" x2="674.6" y2="421.8" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="383.2" width="2.45" height="30.7" fill="var(--down)"/>
<line x1="678.5" y1="375.8" x2="678.5" y2="416.4" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="387.3" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="682.5" y1="367.8" x2="682.5" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="372.8" width="2.45" height="37.1" fill="var(--down)"/>
<line x1="686.4" y1="411.6" x2="686.4" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="412.2" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="690.4" y1="390.8" x2="690.4" y2="408.5" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="398.5" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="694.3" y1="388.0" x2="694.3" y2="423.1" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="393.6" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="698.3" y1="356.4" x2="698.3" y2="399.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="358.9" width="2.45" height="33.1" fill="var(--down)"/>
<line x1="702.2" y1="394.4" x2="702.2" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="398.7" width="2.45" height="38.5" fill="var(--down)"/>
<line x1="706.2" y1="411.9" x2="706.2" y2="438.0" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="422.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="710.1" y1="371.5" x2="710.1" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="371.5" width="2.45" height="59.6" fill="var(--up)"/>
<line x1="714.1" y1="314.4" x2="714.1" y2="358.3" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="338.6" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="718.0" y1="323.1" x2="718.0" y2="351.0" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="328.5" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="722.0" y1="326.3" x2="722.0" y2="356.9" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="329.1" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="725.9" y1="311.1" x2="725.9" y2="352.1" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="315.1" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="729.9" y1="333.8" x2="729.9" y2="372.4" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="334.4" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="733.8" y1="340.5" x2="733.8" y2="385.5" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="342.3" width="2.45" height="42.1" fill="var(--down)"/>
<line x1="737.8" y1="337.2" x2="737.8" y2="368.2" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="344.1" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="741.8" y1="347.5" x2="741.8" y2="375.3" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="359.3" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="745.7" y1="350.7" x2="745.7" y2="376.9" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="354.2" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="749.7" y1="370.9" x2="749.7" y2="392.7" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="372.1" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="753.6" y1="387.4" x2="753.6" y2="402.5" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="392.4" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="757.6" y1="383.2" x2="757.6" y2="412.5" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="386.6" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="761.5" y1="387.9" x2="761.5" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="387.9" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="765.5" y1="365.1" x2="765.5" y2="402.8" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="366.6" width="2.45" height="33.5" fill="var(--up)"/>
<line x1="769.4" y1="268.6" x2="769.4" y2="331.8" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="270.8" width="2.45" height="59.9" fill="var(--up)"/>
<line x1="773.4" y1="261.8" x2="773.4" y2="305.0" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="261.8" width="2.45" height="34.8" fill="var(--down)"/>
<line x1="777.3" y1="254.7" x2="777.3" y2="301.4" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="259.8" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="781.3" y1="266.2" x2="781.3" y2="318.8" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="276.9" width="2.45" height="24.2" fill="var(--down)"/>
<line x1="785.2" y1="292.7" x2="785.2" y2="322.1" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="296.3" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="789.2" y1="197.1" x2="789.2" y2="339.3" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="211.7" width="2.45" height="62.4" fill="var(--up)"/>
<line x1="793.1" y1="171.9" x2="793.1" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="220.3" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="797.1" y1="216.7" x2="797.1" y2="277.2" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="236.8" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="801.0" y1="208.5" x2="801.0" y2="276.4" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="249.8" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="805.0" y1="276.9" x2="805.0" y2="310.1" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="280.8" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="808.9" y1="293.8" x2="808.9" y2="330.3" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="306.7" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="812.9" y1="291.0" x2="812.9" y2="323.3" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="311.9" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="816.8" y1="300.0" x2="816.8" y2="321.4" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="309.0" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="820.8" y1="278.5" x2="820.8" y2="314.8" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="293.3" width="2.45" height="18.7" fill="var(--up)"/>
<line x1="824.7" y1="274.1" x2="824.7" y2="306.2" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="287.3" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="828.7" y1="302.2" x2="828.7" y2="345.2" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="306.1" width="2.45" height="38.9" fill="var(--down)"/>
<line x1="832.7" y1="333.3" x2="832.7" y2="353.9" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="350.7" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="836.6" y1="324.7" x2="836.6" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="325.3" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="840.6" y1="295.4" x2="840.6" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="302.4" width="2.45" height="24.0" fill="var(--up)"/>
<line x1="844.5" y1="319.3" x2="844.5" y2="344.6" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="323.0" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="848.5" y1="346.9" x2="848.5" y2="372.2" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="356.1" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="852.4" y1="369.1" x2="852.4" y2="412.8" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="369.1" width="2.45" height="43.7" fill="var(--down)"/>
<line x1="856.4" y1="388.4" x2="856.4" y2="417.3" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="409.2" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="860.3" y1="422.6" x2="860.3" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="422.6" width="2.45" height="37.8" fill="var(--down)"/>
<line x1="864.3" y1="441.8" x2="864.3" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="442.4" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="868.2" y1="426.1" x2="868.2" y2="472.1" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="456.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="872.2" y1="441.0" x2="872.2" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="466.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="876.1" y1="442.9" x2="876.1" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="449.1" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="880.1" y1="451.9" x2="880.1" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="452.1" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="884.0" y1="426.5" x2="884.0" y2="450.1" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="445.5" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="888.0" y1="447.7" x2="888.0" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="449.7" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="891.9" y1="436.5" x2="891.9" y2="469.0" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="458.9" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="895.9" y1="455.0" x2="895.9" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="460.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="899.8" y1="438.3" x2="899.8" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="455.7" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="903.8" y1="470.4" x2="903.8" y2="487.4" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="480.6" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="907.7" y1="483.0" x2="907.7" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="483.0" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="911.7" y1="502.5" x2="911.7" y2="522.1" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="503.8" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="915.6" y1="488.6" x2="915.6" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="492.8" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="919.6" y1="480.4" x2="919.6" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="481.3" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="923.6" y1="494.6" x2="923.6" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="499.2" width="2.45" height="46.5" fill="var(--down)"/>
<line x1="927.5" y1="528.2" x2="927.5" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="540.5" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="931.5" y1="513.7" x2="931.5" y2="540.7" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="536.1" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="935.4" y1="510.2" x2="935.4" y2="544.1" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="516.6" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="939.4" y1="514.7" x2="939.4" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="520.9" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="943.3" y1="536.7" x2="943.3" y2="549.3" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="538.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="947.3" y1="535.2" x2="947.3" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="543.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="951.2" y1="496.3" x2="951.2" y2="533.9" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="506.9" width="2.45" height="21.8" fill="var(--down)"/>
<line x1="955.2" y1="528.9" x2="955.2" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="537.0" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="959.1" y1="541.5" x2="959.1" y2="561.8" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="542.8" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="963.1" y1="525.3" x2="963.1" y2="542.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="530.9" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="967.0" y1="534.7" x2="967.0" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="537.0" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="971.0" y1="546.8" x2="971.0" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="556.2" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="974.9" y1="524.7" x2="974.9" y2="554.2" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="532.0" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="978.9" y1="497.1" x2="978.9" y2="516.6" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="504.9" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="982.8" y1="509.0" x2="982.8" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="520.0" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="986.8" y1="532.2" x2="986.8" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="534.2" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="990.7" y1="543.0" x2="990.7" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="547.0" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="994.7" y1="528.2" x2="994.7" y2="545.8" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="531.0" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="998.6" y1="530.0" x2="998.6" y2="552.4" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="537.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="1002.6" y1="536.8" x2="1002.6" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="543.1" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="1006.5" y1="536.0" x2="1006.5" y2="553.5" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="537.9" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="1010.5" y1="541.4" x2="1010.5" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="545.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1014.5" y1="551.7" x2="1014.5" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="556.7" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="1018.4" y1="537.3" x2="1018.4" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="542.7" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="1022.4" y1="538.1" x2="1022.4" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="542.5" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="1026.3" y1="529.8" x2="1026.3" y2="558.3" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="542.5" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="1030.3" y1="517.8" x2="1030.3" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="526.2" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="1034.2" y1="522.2" x2="1034.2" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="523.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1038.2" y1="493.9" x2="1038.2" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="504.5" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="1042.1" y1="498.6" x2="1042.1" y2="515.8" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="501.2" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="1046.1" y1="481.6" x2="1046.1" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="484.1" width="2.45" height="25.5" fill="var(--up)"/>
<line x1="1050.0" y1="487.8" x2="1050.0" y2="504.3" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="488.5" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="60" y1="496.7" x2="1052" y2="496.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="500.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$73 R1</text>
<text x="1058" y="512.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="421.9" x2="1052" y2="421.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="425.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$88 R2</text>
<text x="1058" y="437.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="407.4" x2="1052" y2="407.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="410.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$91 R3</text>
<text x="1058" y="422.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="566.8" x2="1052" y2="566.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="560.8" font-size="11.5" fill="var(--support)" font-weight="600">$58 S1</text>
<text x="1058" y="572.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="502.3" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $91 | 2 | 2025년 12월 중순 스윙 고점대(2025-12-12·2025-12-22) |
| R2 | $88 | 2 | 2026년 1월 초중순 스윙 고점대(2026-01-05·2026-01-14) |
| R1 | $73 | 2 | 2026년 7월 스윙 고점대(2026-07-10·2026-07-21) — 6월 급락 이후 반등이 반복적으로 막힌 구간 |
| **현재가** | **$71.60** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $58 | 2 | 2026년 7월 중순~8월 초 스윙 저점대(2026-07-17·2026-08-03) — §3 급락 이후 형성된 최근 저점 |
| 참고선 | $299 | — | 상장 후 역대 최고가(2025-06-23, 차트 기간 밖 — `02_history.md` 참고). 1년 넘게 이어진 하락 추세로 현재가와 4배 이상 벌어져 있어 근시일 지지/저항으로 보지 않음 |

> 레벨은 상단 3개(R1~R3)·하단 1개(S1)로 총 4개가 나왔다. 하단은 6월 급락 이전 구간에서는 터치 2회 이상인 자연 클러스터가 없어(등락이 컸던 구간이라 반복 테스트된 저점이 드물었음) `--force-level`을 쓰지 않고 스크립트 기본값 그대로 뒀다 — 급락 후 형성된 S1이 유일한 자연 지지 클러스터다. 52주 최저($49.90, 2026-02-05)는 이 지지/저항 클러스터와 무관하게 별도로 형성된 단일 저점이라(§4 한계) 레벨로 잡히지 않았다.

---

## 3. 관측된 특이 구간 — 2026-06-30 OUSD 컨소시엄 출범 + 지수 제외 겹친 급락

- 2026-06-30, Stripe·Visa·Mastercard·Google·BlackRock·Coinbase 등 140여개 기업이 참여하는 경쟁 스테이블코인 컨소시엄 **Open USD(OUSD)** 출범이 발표됐고, 같은 시기 FTSE Russell 성장주 지수에서 Circle이 제외되며 지수 추종 자금의 기계적 매도가 겹쳤다([`02_history.md`](./02_history.md) 2026-06-30 항목, [`08_news.md`](./08_news.md) 참고).
- 종가 기준 전일(2026-06-29, $75.96) 대비 **-17.55%** ($75.96 → $62.63), 거래량은 38,127,200주로 최근 1년 일평균(약 1,395만 주) 대비 약 **2.73배**. 다음 거래일(2026-07-01)에도 $61.95로 추가 하락한 뒤 반등을 시작했다.
- 이 급락은 §2의 S1($58) 지지 클러스터가 형성되는 직접적 계기가 됐다 — 급락 전에는 이 가격대에서 반복 테스트된 지지선 자체가 없었고, 급락 이후 2026-07-17·2026-08-03에 비슷한 수준에서 저점이 두 차례 형성되며 처음으로 지지 클러스터가 만들어졌다. 다만 이 구간의 52주 최저($49.90)는 이보다 앞선 2026-02-05에 별도로 기록된 것으로, 6월 급락이 만든 신저가는 아니다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영) — Circle은 2025년 IPO 시 우선주의 보통주 전환·Class B 신설이 있었을 뿐 일반적 의미의 주식분할·병합 이력은 없어(`04_metrics.md` 상단 경고 참고) 이 구간에는 소급조정 이슈가 없다.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py CRCL --name Circle --event 2026-06-30:"OUSD 컨소시엄 출범+FTSE Russell 지수 제외 겹쳐 급락" --close-on 2026-08-13 --close-on 2025-12-31`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다(기본값 그대로 사용, `--levels`·`--min-touches`·`--force-level` 조정 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 적용한 것이며, 최적화된 값이 아니다.
    - 상장 후 거래일 자체가 아직 1년을 살짝 넘긴 수준(2025-06-05 상장)이라, 다른 커버리지 기업 대비 표본이 짧다. 특히 52주 최저($49.90, 2026-02-05)가 §2의 어느 클러스터와도 묶이지 않는 단일 저점으로 남아 있는 것은 이 짧은 이력 탓일 수 있다 — 앞으로 이 가격대가 다시 테스트되는지 지켜볼 필요가 있다.
    - 차트 기간이 상장 후 전고점($298.99, 2025-06-23)을 포함하지 않아, "1년 전 대비" 프레이밍이 상장 초기 급등·급락을 가리는 착시를 줄 수 있다 — 상장 이후 전체 흐름은 `02_history.md`·`08_news.md`를 함께 참고할 것.

---

## 관련 문서

같은 폴더 내 다른 문서로 이동:

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 주봉·상장 이후](./10_technical_weekly.md)

---

## 참고 자료

- [Yahoo Finance — CRCL Historical Data](https://finance.yahoo.com/quote/CRCL/history) (수집 2026-08-16)
- [stockanalysis.com — CRCL Price History](https://stockanalysis.com/stocks/crcl/history/) (대조용)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-16)*
