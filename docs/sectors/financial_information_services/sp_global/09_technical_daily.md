# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **대조 결과**: 2026-08-14 종가 $418.80은 [밸류에이션 / 적정주가](./06_valuation.md) 2. 최근 3개년 — 적정주가 vs 실제주가·6. 목표주가 요약에 인용된 값과 일치. FY2023(2023-12-29 $416.76)·FY2024(2024-12-31 $471.17)·FY2025(2025-12-31 $494.41) 종가도 동일 API에서 조회해 핵심 지표·밸류에이션 / 적정주가와 일치시켰다.
>
> ⚠️ 2026-07-01 Mobility Global(MBGL) 분사와 관련해 데이터 제공처(Yahoo Finance)가 이 날짜를 **"분할(split) 비율 1057:1000"으로 메타데이터에 표시**한다 — 이는 실제 주식분할이 아니라 분사에 따른 가치 조정을 분할 표기법으로 나타낸 것이다(S&P Global의 실제 발행주식수는 분사 전후로 변하지 않았다, 역사 / 주요 이벤트 참고). 직접 확인한 결과 아래 차트에 쓰인 종가(raw close)는 이 "분할"로 소급조정되지 않은 **실제 당시 거래가**다(2026-06-30 종가 $385.30 → 2026-07-01 종가 $414.97로 실제 데이터에 불연속 없이 이어짐, 인위적 스무딩 없음). 따라서 아래 2. 지지선 / 저항선 요약·4. 방법론 · 한계에서 별도 소급조정을 하지 않았다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="spgi-chart">
<style>
.spgi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .spgi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .spgi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.spgi-chart svg { width:100%; height:auto; display:block; }
.spgi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.spgi-chart .title { fill: var(--ink); font-weight:600; }
.spgi-chart .grid { stroke: var(--grid); stroke-width:1; }
.spgi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="S&P Global(SPGI) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">S&P Global (SPGI) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $418.80 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="565.2" x2="1052" y2="565.2" class="grid"/>
<text x="52" y="569.2" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="489.2" x2="1052" y2="489.2" class="grid"/>
<text x="52" y="493.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="413.2" x2="1052" y2="413.2" class="grid"/>
<text x="52" y="417.2" font-size="11" text-anchor="end" fill="var(--muted)">425</text>
<line x1="60" y1="337.2" x2="1052" y2="337.2" class="grid"/>
<text x="52" y="341.2" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="261.2" x2="1052" y2="261.2" class="grid"/>
<text x="52" y="265.2" font-size="11" text-anchor="end" fill="var(--muted)">475</text>
<line x1="60" y1="185.2" x2="1052" y2="185.2" class="grid"/>
<text x="52" y="189.2" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="109.2" x2="1052" y2="109.2" class="grid"/>
<text x="52" y="113.2" font-size="11" text-anchor="end" fill="var(--muted)">525</text>
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
<line x1="60" y1="-55.1" x2="1052" y2="-55.1" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="-52.1" font-size="10.5" fill="var(--muted)">$579 52주 최고(2025-08-14)</text>
<line x1="927.5" y1="56.0" x2="927.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="933.5" y="68.0" font-size="10.5" fill="var(--down)">2026-07-01 Mobility 분사 완료</text>
<line x1="998.6" y1="56.0" x2="998.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1004.6" y="68.0" font-size="10.5" fill="var(--down)">2026-07-28 2분기 실적, EPS 가이던스 하향(-5.2%)</text>
<line x1="62.0" y1="79.4" x2="62.0" y2="107.0" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="83.1" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="65.9" y1="103.8" x2="65.9" y2="125.3" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="109.7" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="69.9" y1="95.9" x2="69.9" y2="119.1" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="110.6" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="73.8" y1="95.8" x2="73.8" y2="116.3" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="103.1" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="77.8" y1="104.3" x2="77.8" y2="120.5" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="113.7" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="81.7" y1="96.2" x2="81.7" y2="112.5" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="104.2" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="85.7" y1="103.1" x2="85.7" y2="123.7" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="105.2" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="89.6" y1="115.8" x2="89.6" y2="134.1" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="116.7" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="93.6" y1="110.2" x2="93.6" y2="124.3" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="121.4" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="97.5" y1="120.5" x2="97.5" y2="134.1" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="125.5" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="101.5" y1="122.3" x2="101.5" y2="133.9" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="127.9" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="105.5" y1="139.3" x2="105.5" y2="159.5" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="141.7" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="109.4" y1="145.5" x2="109.4" y2="164.1" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="154.3" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="113.4" y1="141.4" x2="113.4" y2="156.8" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="146.4" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="117.3" y1="143.0" x2="117.3" y2="173.6" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="143.9" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="121.3" y1="131.7" x2="121.3" y2="167.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="135.2" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="125.2" y1="126.4" x2="125.2" y2="142.7" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="130.0" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="129.2" y1="126.0" x2="129.2" y2="155.0" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="130.8" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="133.1" y1="117.1" x2="133.1" y2="152.1" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="120.8" width="2.45" height="28.3" fill="var(--up)"/>
<line x1="137.1" y1="122.4" x2="137.1" y2="143.5" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="129.4" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="141.0" y1="129.4" x2="141.0" y2="142.8" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="135.8" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="145.0" y1="145.1" x2="145.0" y2="160.9" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="148.4" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="148.9" y1="130.7" x2="148.9" y2="150.7" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="140.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="152.9" y1="141.8" x2="152.9" y2="258.3" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="144.2" width="2.45" height="100.5" fill="var(--down)"/>
<line x1="156.8" y1="238.4" x2="156.8" y2="259.7" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="244.7" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="160.8" y1="226.5" x2="160.8" y2="251.4" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="243.2" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="164.7" y1="247.0" x2="164.7" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="251.1" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="168.7" y1="286.1" x2="168.7" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="288.6" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="172.6" y1="293.9" x2="172.6" y2="317.9" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="297.9" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="176.6" y1="293.2" x2="176.6" y2="309.3" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="301.7" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="180.5" y1="284.5" x2="180.5" y2="300.6" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="290.3" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="184.5" y1="290.7" x2="184.5" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="290.7" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="188.4" y1="294.1" x2="188.4" y2="324.0" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="299.1" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="192.4" y1="312.1" x2="192.4" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="324.6" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="196.4" y1="318.0" x2="196.4" y2="339.7" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="325.2" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="200.3" y1="323.3" x2="200.3" y2="341.1" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="324.0" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="204.3" y1="310.0" x2="204.3" y2="327.9" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="311.3" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="208.2" y1="306.3" x2="208.2" y2="330.7" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="314.3" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="212.2" y1="290.2" x2="212.2" y2="310.6" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="302.8" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="216.1" y1="283.2" x2="216.1" y2="309.5" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="289.3" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="220.1" y1="295.0" x2="220.1" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="307.7" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="224.0" y1="300.8" x2="224.0" y2="333.3" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="305.4" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="228.0" y1="292.1" x2="228.0" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="304.8" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="231.9" y1="311.1" x2="231.9" y2="353.4" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="315.0" width="2.45" height="32.5" fill="var(--down)"/>
<line x1="235.9" y1="334.9" x2="235.9" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="343.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="239.8" y1="330.1" x2="239.8" y2="345.3" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="331.6" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="243.8" y1="308.3" x2="243.8" y2="331.8" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="313.8" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="247.7" y1="307.8" x2="247.7" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="318.8" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="251.7" y1="315.3" x2="251.7" y2="327.9" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="316.9" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="255.6" y1="289.5" x2="255.6" y2="311.5" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="297.5" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="259.6" y1="274.1" x2="259.6" y2="291.9" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="276.8" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="263.5" y1="272.3" x2="263.5" y2="288.4" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="280.6" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="267.5" y1="295.9" x2="267.5" y2="350.7" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="297.8" width="2.45" height="46.9" fill="var(--down)"/>
<line x1="271.4" y1="266.4" x2="271.4" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="291.4" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="275.4" y1="272.9" x2="275.4" y2="308.7" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="284.5" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="279.3" y1="275.0" x2="279.3" y2="313.8" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="275.7" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="283.3" y1="266.2" x2="283.3" y2="281.5" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="269.4" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="287.3" y1="266.1" x2="287.3" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="275.5" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="291.2" y1="275.1" x2="291.2" y2="299.4" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="281.6" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="295.2" y1="277.5" x2="295.2" y2="307.4" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="277.5" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="299.1" y1="281.8" x2="299.1" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="284.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="303.1" y1="271.0" x2="303.1" y2="285.7" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="273.7" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="307.0" y1="262.0" x2="307.0" y2="280.2" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="273.6" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="311.0" y1="249.1" x2="311.0" y2="291.2" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="258.7" width="2.45" height="32.6" fill="var(--up)"/>
<line x1="314.9" y1="256.0" x2="314.9" y2="285.5" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="261.3" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="318.9" y1="285.8" x2="318.9" y2="302.8" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="288.7" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="322.8" y1="289.0" x2="322.8" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="295.1" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="326.8" y1="287.3" x2="326.8" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="293.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="272.0" x2="330.7" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="285.0" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="334.7" y1="275.8" x2="334.7" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="284.2" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="338.6" y1="283.8" x2="338.6" y2="299.3" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="284.4" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="342.6" y1="277.1" x2="342.6" y2="298.1" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="283.9" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="346.5" y1="271.6" x2="346.5" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="279.8" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="350.5" y1="266.7" x2="350.5" y2="279.6" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="270.5" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="354.4" y1="265.9" x2="354.4" y2="282.2" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="280.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="358.4" y1="277.1" x2="358.4" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="281.8" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="362.3" y1="262.2" x2="362.3" y2="290.8" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="267.5" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="366.3" y1="261.1" x2="366.3" y2="282.7" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="269.7" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="370.2" y1="262.2" x2="370.2" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="271.4" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="374.2" y1="275.0" x2="374.2" y2="297.4" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="276.6" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="378.2" y1="280.3" x2="378.2" y2="295.6" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="288.2" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="382.1" y1="287.7" x2="382.1" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="292.1" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="386.1" y1="271.2" x2="386.1" y2="289.9" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="274.2" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="390.0" y1="255.9" x2="390.0" y2="272.7" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="264.2" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="394.0" y1="257.8" x2="394.0" y2="273.8" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="259.9" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="397.9" y1="257.1" x2="397.9" y2="281.5" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="267.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="401.9" y1="231.5" x2="401.9" y2="266.5" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="236.7" width="2.45" height="27.8" fill="var(--up)"/>
<line x1="405.8" y1="221.5" x2="405.8" y2="250.0" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="236.0" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="409.8" y1="230.6" x2="409.8" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="230.9" width="2.45" height="16.9" fill="var(--up)"/>
<line x1="413.7" y1="196.3" x2="413.7" y2="238.6" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="204.2" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="417.7" y1="189.3" x2="417.7" y2="210.0" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="194.9" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="421.6" y1="187.8" x2="421.6" y2="197.6" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="193.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="425.6" y1="181.9" x2="425.6" y2="196.1" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="182.5" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="429.5" y1="173.8" x2="429.5" y2="183.8" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="180.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="433.5" y1="175.2" x2="433.5" y2="189.6" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="187.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="437.4" y1="186.8" x2="437.4" y2="202.6" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="191.6" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="441.4" y1="196.6" x2="441.4" y2="234.6" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="204.4" width="2.45" height="26.3" fill="var(--down)"/>
<line x1="445.3" y1="158.8" x2="445.3" y2="234.1" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="172.5" width="2.45" height="60.2" fill="var(--up)"/>
<line x1="449.3" y1="147.1" x2="449.3" y2="174.7" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="153.1" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="453.2" y1="142.3" x2="453.2" y2="160.7" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="149.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="457.2" y1="135.6" x2="457.2" y2="163.8" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="147.6" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="461.1" y1="131.0" x2="461.1" y2="147.4" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="141.1" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="465.1" y1="139.0" x2="465.1" y2="156.2" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="139.2" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="469.1" y1="136.1" x2="469.1" y2="162.6" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="137.9" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="473.0" y1="132.0" x2="473.0" y2="153.0" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="137.7" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="477.0" y1="116.9" x2="477.0" y2="146.7" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="136.5" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="480.9" y1="126.7" x2="480.9" y2="143.2" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="133.9" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="484.9" y1="137.7" x2="484.9" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="156.9" width="2.45" height="55.5" fill="var(--down)"/>
<line x1="488.8" y1="172.9" x2="488.8" y2="207.8" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="177.5" width="2.45" height="30.2" fill="var(--up)"/>
<line x1="492.8" y1="150.5" x2="492.8" y2="177.4" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="152.7" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="496.7" y1="147.7" x2="496.7" y2="181.9" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="152.2" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="500.7" y1="155.5" x2="500.7" y2="180.3" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="165.8" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="504.6" y1="163.1" x2="504.6" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="171.5" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="508.6" y1="173.8" x2="508.6" y2="200.8" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="186.3" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="512.5" y1="174.3" x2="512.5" y2="206.3" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="184.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="516.5" y1="174.3" x2="516.5" y2="201.0" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="187.2" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="520.4" y1="176.7" x2="520.4" y2="199.5" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="187.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="524.4" y1="247.4" x2="524.4" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="258.5" width="2.45" height="100.1" fill="var(--down)"/>
<line x1="528.3" y1="351.4" x2="528.3" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="366.4" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="532.3" y1="341.9" x2="532.3" y2="442.0" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="353.4" width="2.45" height="52.6" fill="var(--down)"/>
<line x1="536.2" y1="377.9" x2="536.2" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="404.8" width="2.45" height="37.0" fill="var(--down)"/>
<line x1="540.2" y1="423.5" x2="540.2" y2="451.0" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="427.7" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="544.1" y1="483.4" x2="544.1" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="500.2" width="2.45" height="51.5" fill="var(--down)"/>
<line x1="548.1" y1="514.5" x2="548.1" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="535.5" width="2.45" height="45.9" fill="var(--down)"/>
<line x1="552.0" y1="554.9" x2="552.0" y2="607.7" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="562.8" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="556.0" y1="524.9" x2="556.0" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="527.3" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="560.0" y1="490.3" x2="560.0" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="508.8" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="563.9" y1="489.7" x2="563.9" y2="516.9" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="499.0" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="567.9" y1="496.1" x2="567.9" y2="521.7" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="502.6" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="571.8" y1="501.2" x2="571.8" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="504.5" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="575.8" y1="504.3" x2="575.8" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="516.0" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="579.7" y1="498.2" x2="579.7" y2="553.3" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="502.2" width="2.45" height="45.9" fill="var(--up)"/>
<line x1="583.7" y1="478.9" x2="583.7" y2="501.4" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="486.9" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="587.6" y1="442.1" x2="587.6" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="447.0" width="2.45" height="31.3" fill="var(--up)"/>
<line x1="591.6" y1="429.7" x2="591.6" y2="458.2" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="434.3" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="595.5" y1="426.8" x2="595.5" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="430.9" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="599.5" y1="417.8" x2="599.5" y2="452.0" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="428.3" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="603.4" y1="410.4" x2="603.4" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="423.9" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="607.4" y1="406.2" x2="607.4" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="407.8" width="2.45" height="22.7" fill="var(--up)"/>
<line x1="611.3" y1="403.2" x2="611.3" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="404.2" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="615.3" y1="412.2" x2="615.3" y2="464.4" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="415.0" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="619.2" y1="425.3" x2="619.2" y2="462.7" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="427.4" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="623.2" y1="441.7" x2="623.2" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="452.7" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="627.1" y1="472.1" x2="627.1" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="472.8" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="631.1" y1="475.5" x2="631.1" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="486.1" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="635.0" y1="472.0" x2="635.0" y2="483.7" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="478.3" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="639.0" y1="451.3" x2="639.0" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="460.0" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="642.9" y1="466.0" x2="642.9" y2="480.0" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="472.3" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="646.9" y1="474.3" x2="646.9" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="479.6" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="650.9" y1="473.5" x2="650.9" y2="493.4" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="479.0" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="654.8" y1="458.1" x2="654.8" y2="482.6" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="469.9" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="658.8" y1="480.0" x2="658.8" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="482.9" width="2.45" height="39.6" fill="var(--down)"/>
<line x1="662.7" y1="499.1" x2="662.7" y2="540.4" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="503.8" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="666.7" y1="510.6" x2="666.7" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="519.0" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="670.6" y1="525.3" x2="670.6" y2="545.1" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="531.8" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="674.6" y1="500.4" x2="674.6" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="504.2" width="2.45" height="19.2" fill="var(--up)"/>
<line x1="678.5" y1="477.4" x2="678.5" y2="505.9" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="481.9" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="682.5" y1="475.2" x2="682.5" y2="508.7" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="481.1" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="686.4" y1="458.3" x2="686.4" y2="497.0" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="465.2" width="2.45" height="27.8" fill="var(--up)"/>
<line x1="690.4" y1="452.2" x2="690.4" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="456.7" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="694.3" y1="448.4" x2="694.3" y2="476.1" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="459.9" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="698.3" y1="434.0" x2="698.3" y2="452.4" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="446.6" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="702.2" y1="453.3" x2="702.2" y2="507.5" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="459.4" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="706.2" y1="485.8" x2="706.2" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="491.7" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="710.1" y1="467.9" x2="710.1" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="468.3" width="2.45" height="38.2" fill="var(--up)"/>
<line x1="714.1" y1="453.3" x2="714.1" y2="484.5" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="465.4" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="718.0" y1="454.1" x2="718.0" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="466.8" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="722.0" y1="438.4" x2="722.0" y2="453.2" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="447.0" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="725.9" y1="424.6" x2="725.9" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="431.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="729.9" y1="429.1" x2="729.9" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="431.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="733.8" y1="400.6" x2="733.8" y2="430.7" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="426.3" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="737.8" y1="391.7" x2="737.8" y2="420.9" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="410.4" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="741.8" y1="418.8" x2="741.8" y2="459.9" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="425.4" width="2.45" height="17.1" fill="var(--down)"/>
<line x1="745.7" y1="435.0" x2="745.7" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="439.7" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="749.7" y1="440.2" x2="749.7" y2="458.0" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="447.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="753.6" y1="399.6" x2="753.6" y2="459.6" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="433.5" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="757.6" y1="454.1" x2="757.6" y2="485.3" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="459.3" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="761.5" y1="456.8" x2="761.5" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="465.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="765.5" y1="443.0" x2="765.5" y2="481.1" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="452.8" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="769.4" y1="464.7" x2="769.4" y2="487.8" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="483.6" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="773.4" y1="467.3" x2="773.4" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="482.2" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="777.3" y1="477.3" x2="777.3" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="487.0" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="781.3" y1="459.6" x2="781.3" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="472.3" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="785.2" y1="475.8" x2="785.2" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="481.5" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="789.2" y1="489.5" x2="789.2" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="494.4" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="793.1" y1="468.1" x2="793.1" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="485.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="797.1" y1="497.1" x2="797.1" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="498.9" width="2.45" height="37.1" fill="var(--down)"/>
<line x1="801.0" y1="515.7" x2="801.0" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="528.8" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="805.0" y1="521.5" x2="805.0" y2="550.5" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="537.5" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="808.9" y1="498.4" x2="808.9" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="504.7" width="2.45" height="38.6" fill="var(--up)"/>
<line x1="812.9" y1="490.1" x2="812.9" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="499.2" width="2.45" height="25.7" fill="var(--down)"/>
<line x1="816.8" y1="505.2" x2="816.8" y2="543.8" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="505.9" width="2.45" height="25.5" fill="var(--up)"/>
<line x1="820.8" y1="504.7" x2="820.8" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="509.5" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="824.7" y1="492.7" x2="824.7" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="504.2" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="828.7" y1="506.9" x2="828.7" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="518.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="832.7" y1="500.0" x2="832.7" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="509.3" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="836.6" y1="493.8" x2="836.6" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="503.9" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="840.6" y1="472.9" x2="840.6" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="485.7" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="844.5" y1="465.9" x2="844.5" y2="494.8" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="472.6" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="848.5" y1="476.9" x2="848.5" y2="517.8" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="476.9" width="2.45" height="27.7" fill="var(--down)"/>
<line x1="852.4" y1="507.9" x2="852.4" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="513.6" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="856.4" y1="480.3" x2="856.4" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="496.9" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="860.3" y1="476.4" x2="860.3" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="484.5" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="864.3" y1="486.5" x2="864.3" y2="508.4" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="492.7" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="868.2" y1="478.1" x2="868.2" y2="518.0" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="483.4" width="2.45" height="27.9" fill="var(--up)"/>
<line x1="872.2" y1="467.7" x2="872.2" y2="494.2" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="478.9" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="876.1" y1="480.0" x2="876.1" y2="521.7" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="483.7" width="2.45" height="32.7" fill="var(--down)"/>
<line x1="880.1" y1="497.3" x2="880.1" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="500.4" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="884.0" y1="470.2" x2="884.0" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="485.5" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="888.0" y1="450.2" x2="888.0" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="459.1" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="891.9" y1="456.8" x2="891.9" y2="505.6" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="472.9" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="895.9" y1="503.0" x2="895.9" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="503.0" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="899.8" y1="521.1" x2="899.8" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="533.5" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="903.8" y1="511.6" x2="903.8" y2="555.1" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="519.9" width="2.45" height="34.4" fill="var(--down)"/>
<line x1="907.7" y1="540.5" x2="907.7" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="547.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="911.7" y1="517.4" x2="911.7" y2="569.2" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="547.5" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="915.6" y1="508.6" x2="915.6" y2="574.8" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="531.3" width="2.45" height="37.4" fill="var(--up)"/>
<line x1="919.6" y1="514.0" x2="919.6" y2="539.9" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="518.9" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="923.6" y1="518.8" x2="923.6" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="533.9" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="927.5" y1="429.1" x2="927.5" y2="498.3" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="443.7" width="2.45" height="46.8" fill="var(--up)"/>
<line x1="931.5" y1="367.6" x2="931.5" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="367.9" width="2.45" height="50.6" fill="var(--up)"/>
<line x1="935.4" y1="344.2" x2="935.4" y2="404.8" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="345.7" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="939.4" y1="336.2" x2="939.4" y2="365.8" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="345.4" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="943.3" y1="358.8" x2="943.3" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="361.6" width="2.45" height="34.0" fill="var(--down)"/>
<line x1="947.3" y1="387.8" x2="947.3" y2="420.2" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="389.0" width="2.45" height="19.2" fill="var(--up)"/>
<line x1="951.2" y1="365.7" x2="951.2" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="372.6" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="955.2" y1="368.5" x2="955.2" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="374.2" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="959.1" y1="368.4" x2="959.1" y2="411.0" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="371.0" width="2.45" height="31.5" fill="var(--up)"/>
<line x1="963.1" y1="335.3" x2="963.1" y2="370.0" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="354.0" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="967.0" y1="314.2" x2="967.0" y2="353.6" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="314.8" width="2.45" height="29.8" fill="var(--up)"/>
<line x1="971.0" y1="300.7" x2="971.0" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="318.2" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="974.9" y1="327.9" x2="974.9" y2="359.1" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="328.3" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="978.9" y1="363.9" x2="978.9" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="387.2" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="982.8" y1="380.6" x2="982.8" y2="402.4" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="381.0" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="986.8" y1="411.7" x2="986.8" y2="432.4" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="414.1" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="990.7" y1="405.1" x2="990.7" y2="428.4" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="408.9" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="994.7" y1="358.5" x2="994.7" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="368.1" width="2.45" height="20.8" fill="var(--up)"/>
<line x1="998.6" y1="379.9" x2="998.6" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="415.1" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="1002.6" y1="415.3" x2="1002.6" y2="443.7" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="425.6" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="1006.5" y1="431.6" x2="1006.5" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="442.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1010.5" y1="436.6" x2="1010.5" y2="460.7" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="441.4" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="1014.5" y1="422.4" x2="1014.5" y2="459.9" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="439.8" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="1018.4" y1="432.0" x2="1018.4" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="451.1" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="1022.4" y1="424.8" x2="1022.4" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="432.5" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="1026.3" y1="454.8" x2="1026.3" y2="478.7" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="464.5" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="1030.3" y1="449.1" x2="1030.3" y2="476.4" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="464.3" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="1034.2" y1="450.6" x2="1034.2" y2="473.2" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="455.9" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="1038.2" y1="451.3" x2="1038.2" y2="466.0" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="456.6" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="1042.1" y1="455.0" x2="1042.1" y2="475.6" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="458.5" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="1046.1" y1="415.2" x2="1046.1" y2="455.4" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="420.3" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="1050.0" y1="418.6" x2="1050.0" y2="446.0" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="422.3" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="60" y1="397.5" x2="1052" y2="397.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="401.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$430 R1</text>
<text x="1058" y="413.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="273.5" x2="1052" y2="273.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="277.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$471 R2</text>
<text x="1058" y="289.0" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="117.0" x2="1052" y2="117.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="120.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$522 R3</text>
<text x="1058" y="132.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="498.6" x2="1052" y2="498.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="492.6" font-size="11.5" fill="var(--support)" font-weight="600">$397 S1</text>
<text x="1058" y="504.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="548.1" x2="1052" y2="548.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="542.1" font-size="11.5" fill="var(--support)" font-weight="600">$381 S2</text>
<text x="1058" y="554.1" font-size="9.5" fill="var(--muted)">터치 6회</text>
<circle cx="1052.0" cy="432.0" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $522 | 2 | 2026년 1월 초 반등 고점대(FY2025 어닝 실망 전 마지막 고점) |
| R2 | $471 | 4 | 2025년 10~12월 하락 후 형성된 중간 레인지 상단 |
| R1 | $430 | 2 | 2026년 7월 초(분사 직후)~7월 중순 반등 고점대 |
| **현재가** | **$418.80** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $397 | 3 | 2026년 8월 최근 조정 저점대 |
| S2 | $381 | 6 | 2026년 2월 어닝 쇼크 이후~6월 저점이 반복적으로 형성한 레인지 하단(가장 강한 클러스터) |
| 참고선 | $579 | — | 52주 최고(2025-08-14 장중) — 이후 두 차례 가이던스 실망(3. 관측된 특이 구간)으로 레짐이 완전히 바뀌어 근시일 저항으로 보지 않음 |

> 레벨 개수는 스크립트 기본값(3개)을 그대로 사용했다 — 유효 클러스터가 상단 3개·하단 2개로 자연스럽게 형성됐다.

---

## 3. 관측된 특이 구간

이 1년 동안 실적 발표를 계기로 한 대형 갭다운이 **두 차례** 있었다 — 아래 순서대로, 최근 것부터 기록한다.

### 3-1. 2026-07-28 — 2분기 실적, EPS 가이던스 하향(Mobility 분사 후 첫 실적)

- Mobility Global(MBGL) 분사(2026-07-01) 이후 첫 분기 실적. 최근 뉴스 / 이슈 로그 참고.
- 종가 기준 전일 대비 **−3.5%** ($439.83 → $424.36, 2026-07-27→2026-07-28), 거래량은 평소(일 평균 약 211만 주) 대비 약 **2.0배**인 **약 422만 주**. 장중 프리마켓에서는 −5.2%까지 밀렸다가 정규장에서 낙폭을 일부 만회했다.
- 매출은 컨센서스를 상회했음에도 Adjusted EPS 가이던스($17.50~$17.75)가 시장 기대에 못 미쳐 하락 — 아래 2026-02-10 사례와 함께 "가이던스 실망이 반복되는 패턴"으로 읽을 수 있다(투자 판단 3. 리스크 (약점 / Bear Case) 리스크3 참고).

### 3-2. 2026-02-10 — 4분기 실적 발표, FY2026 최초 가이던스 실망(연중 최대 낙폭)

- 4분기 실적 자체는 매출 $3.92B(컨센서스 상회)로 양호했으나, 이날 처음 제시한 FY2026 Adjusted EPS 가이던스($19.40~$19.65, 당시는 Mobility 포함 기준)가 시장 컨센서스($19.96)를 밑돌면서 급락했다.
- 종가 기준 전일 대비 **−9.7%** ($420.24 → $379.45, 2026-02-09→2026-02-10), 거래량은 평소 대비 약 **5.4배**인 **약 1,151만 주** — 이 문서가 다루는 1년 구간 전체에서 가장 큰 단일 거래일 낙폭·거래량이다. 이틀 뒤인 2026-02-11 장중 $369.69까지 밀리며 **연중 최저가**를 기록했고, 이는 S2 레벨($381) 클러스터 형성의 핵심 구간이다.
- 이후 주가는 3~7월 동안 $370~$450 레인지에서 등락하다 7월 초 분사를 계기로 잠시 반등했으나, 위 3-1의 2차 가이던스 실망으로 다시 밀렸다 — 2025년 8월 고점($579) 대비 2026년 8월 현재가 −28% 수준인 것은 이 두 차례 갭다운이 누적된 결과다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-17. 원주가(배당 미반영) — 위 상단 ⚠️ 참고, 2026-07-01 "분할" 메타데이터는 실제 분할이 아니며 소급조정하지 않았다.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py SPGI --name "S&P Global" --event 2026-07-01:"Mobility 분사 완료" --event 2026-07-28:"2분기 실적, EPS 가이던스 하향(-5.2%)" --ref-line 579.05:"52주 최고(2025-08-14)" --close-on 2026-08-14`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다(기본값 그대로 사용, 조정 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 이 1년 구간 안에 두 차례의 대형 실적 갭다운(3. 관측된 특이 구간)이 있어, 그 이전 형성된 고가 레벨(R2~R3, 참고선 $579)은 지금과는 다른 "레짐"에서 만들어진 가격대라는 점을 감안해야 한다 — 특히 4-A. DCF 민감도 밸류에이션(밸류에이션 / 적정주가)의 하단 시나리오와 S2($381)가 근접한다는 점이 참고할 만하다.
    - 2026-07-01 Mobility 분사는 실제 주식분할이 아니므로 소급조정하지 않았다(위 상단 ⚠️ 참고).

---

## 관련 문서

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Yahoo Finance 일봉 OHLCV (SPGI)](https://query1.finance.yahoo.com/v8/finance/chart/SPGI)
- [S&P Global shares tumble as 2026 guidance disappoints investors — Investing.com (2026-02-10)](https://www.investing.com/news/earnings/sp-global-shares-tumble-as-2026-guidance-disappoints-investors-93CH-4496341)

---

*작성일: 2026-08-17 (최종 수정일: 2026-08-23)*
