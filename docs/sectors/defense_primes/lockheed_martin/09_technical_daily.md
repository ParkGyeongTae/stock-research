# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트의 기간이 담지 못하는 것
이 회사에서 가장 중요한 가격 사건인 **2025-07-22의 하루 −10.8%**(세전 $1,681M 손실충당 발표)는 **이 차트의 시작일(2025-09-12)보다 앞서 있어 들어 있지 않다.** 그 사건은 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)에서 볼 수 있고, 내용은 [최근 뉴스 / 이슈](./08_news.md)에 있다.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$524.19**는 [핵심 지표](./04_metrics.md) A.2. 밸류에이션 지표와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 현재가와 일치한다.
- **최근 1년 범위**: 최고 $692.00 · 최저 $437.25 · 일평균 거래량 1,430,088주.

:::

---

## 1. 차트 — 최근 1년 일봉 (2025-09-12 ~ 2026-09-11)

<div class="lmt-chart">
<style>
.lmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lmt-chart svg { width:100%; height:auto; display:block; }
.lmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lmt-chart .title { fill: var(--ink); font-weight:600; }
.lmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.lmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="록히드마틴(LMT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">록히드마틴 (LMT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-12 ~ 2026-09-11 · 마지막 종가 $524.19 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="574.2" x2="1052" y2="574.2" class="grid"/>
<text x="52" y="578.2" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="470.5" x2="1052" y2="470.5" class="grid"/>
<text x="52" y="474.5" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="366.9" x2="1052" y2="366.9" class="grid"/>
<text x="52" y="370.9" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="263.3" x2="1052" y2="263.3" class="grid"/>
<text x="52" y="267.3" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="159.6" x2="1052" y2="159.6" class="grid"/>
<text x="52" y="163.6" font-size="11" text-anchor="end" fill="var(--muted)">650</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="113.4" y1="626.0" x2="113.4" y2="631.0" class="axis"/>
<text x="113.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="204.3" y1="626.0" x2="204.3" y2="631.0" class="axis"/>
<text x="204.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="366.3" y1="626.0" x2="366.3" y2="631.0" class="axis"/>
<text x="366.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="445.3" y1="626.0" x2="445.3" y2="631.0" class="axis"/>
<text x="445.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="607.4" y1="626.0" x2="607.4" y2="631.0" class="axis"/>
<text x="607.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="690.4" y1="626.0" x2="690.4" y2="631.0" class="axis"/>
<text x="690.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="769.4" y1="626.0" x2="769.4" y2="631.0" class="axis"/>
<text x="769.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="852.4" y1="626.0" x2="852.4" y2="631.0" class="axis"/>
<text x="852.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="939.4" y1="626.0" x2="939.4" y2="631.0" class="axis"/>
<text x="939.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1022.4" y1="626.0" x2="1022.4" y2="631.0" class="axis"/>
<text x="1022.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="526.6" x2="62.0" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="530.0" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="65.9" y1="523.8" x2="65.9" y2="534.8" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="526.0" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="69.9" y1="515.2" x2="69.9" y2="529.3" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="523.8" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="73.8" y1="517.8" x2="73.8" y2="527.3" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="522.5" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="77.8" y1="523.7" x2="77.8" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="525.2" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="81.7" y1="518.2" x2="81.7" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="524.0" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="85.7" y1="507.7" x2="85.7" y2="526.5" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="511.2" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="89.6" y1="497.9" x2="89.6" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="498.2" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="93.6" y1="480.4" x2="93.6" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="497.2" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="97.5" y1="489.7" x2="97.5" y2="503.6" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="492.1" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="101.5" y1="489.7" x2="101.5" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="495.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="105.5" y1="472.6" x2="105.5" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="476.8" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="109.4" y1="470.8" x2="109.4" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="472.2" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="113.4" y1="462.1" x2="113.4" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="472.6" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="117.3" y1="463.1" x2="117.3" y2="476.7" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="471.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="121.3" y1="456.4" x2="121.3" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="461.2" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="125.2" y1="438.6" x2="125.2" y2="456.8" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="441.0" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="129.2" y1="437.4" x2="129.2" y2="451.6" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="441.1" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="133.1" y1="437.4" x2="133.1" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="438.9" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="137.1" y1="439.1" x2="137.1" y2="462.6" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="441.8" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="141.0" y1="442.7" x2="141.0" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="452.2" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="145.0" y1="455.1" x2="145.0" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="462.6" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="148.9" y1="456.0" x2="148.9" y2="472.6" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="459.8" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="152.9" y1="460.2" x2="152.9" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="464.3" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="156.8" y1="467.8" x2="156.8" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="469.0" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="160.8" y1="477.4" x2="160.8" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="480.6" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="164.7" y1="458.3" x2="164.7" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="458.3" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="168.7" y1="456.9" x2="168.7" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="492.3" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="172.6" y1="486.3" x2="172.6" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="488.2" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="176.6" y1="483.0" x2="176.6" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="495.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="180.5" y1="487.5" x2="180.5" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="490.7" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="184.5" y1="496.8" x2="184.5" y2="512.3" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="497.7" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="188.4" y1="492.5" x2="188.4" y2="504.5" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="498.8" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="192.4" y1="493.7" x2="192.4" y2="504.4" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="501.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="196.4" y1="482.0" x2="196.4" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="491.9" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="200.3" y1="483.8" x2="200.3" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="487.4" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="204.3" y1="488.1" x2="204.3" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="489.2" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="208.2" y1="494.4" x2="208.2" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="501.7" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="212.2" y1="499.9" x2="212.2" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="505.7" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="216.1" y1="524.1" x2="216.1" y2="540.8" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="526.3" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="220.1" y1="534.0" x2="220.1" y2="561.3" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="535.0" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="224.0" y1="559.5" x2="224.0" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="561.7" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="228.0" y1="549.8" x2="228.0" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="559.5" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="231.9" y1="553.9" x2="231.9" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="559.6" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="235.9" y1="551.6" x2="235.9" y2="563.6" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="557.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="239.8" y1="540.2" x2="239.8" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="541.5" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="243.8" y1="529.4" x2="243.8" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="531.1" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="247.7" y1="501.6" x2="247.7" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="521.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="251.7" y1="527.7" x2="251.7" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="528.6" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="255.6" y1="517.3" x2="255.6" y2="543.0" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="524.7" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="259.6" y1="534.0" x2="259.6" y2="553.5" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="535.6" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="263.5" y1="551.0" x2="263.5" y2="574.1" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="554.6" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="267.5" y1="565.8" x2="267.5" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="569.2" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="271.4" y1="559.1" x2="271.4" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="565.6" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="275.4" y1="557.9" x2="275.4" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="557.9" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="279.3" y1="565.7" x2="279.3" y2="598.0" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="567.4" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="283.3" y1="589.2" x2="283.3" y2="600.6" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="591.1" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="287.3" y1="577.4" x2="287.3" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="580.8" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="291.2" y1="575.2" x2="291.2" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="577.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="295.2" y1="568.3" x2="295.2" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="569.6" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="299.1" y1="541.9" x2="299.1" y2="571.1" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="542.3" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="303.1" y1="526.9" x2="303.1" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="539.2" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="307.0" y1="526.3" x2="307.0" y2="562.0" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="537.0" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="311.0" y1="512.6" x2="311.0" y2="532.1" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="522.6" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="314.9" y1="510.3" x2="314.9" y2="531.1" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="511.5" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="318.9" y1="502.1" x2="318.9" y2="517.7" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="502.8" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="322.8" y1="512.4" x2="322.8" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="512.8" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="326.8" y1="518.4" x2="326.8" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="522.8" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="330.7" y1="519.9" x2="330.7" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="527.7" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="334.7" y1="520.9" x2="334.7" y2="543.3" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="524.2" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="338.6" y1="501.6" x2="338.6" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="504.6" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="342.6" y1="501.7" x2="342.6" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="503.7" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="346.5" y1="488.8" x2="346.5" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="500.1" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="350.5" y1="497.4" x2="350.5" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="501.2" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="354.4" y1="492.5" x2="354.4" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="493.6" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="358.4" y1="487.7" x2="358.4" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="492.6" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="362.3" y1="491.9" x2="362.3" y2="504.7" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="493.3" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="366.3" y1="476.4" x2="366.3" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="476.6" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="370.2" y1="437.6" x2="370.2" y2="464.3" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="446.6" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="374.2" y1="390.3" x2="374.2" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="424.9" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="378.2" y1="403.4" x2="378.2" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="418.1" width="2.45" height="58.9" fill="var(--down)"/>
<line x1="382.1" y1="381.7" x2="382.1" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="404.4" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="386.1" y1="375.1" x2="386.1" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="381.6" width="2.45" height="35.3" fill="var(--up)"/>
<line x1="390.0" y1="358.1" x2="390.0" y2="387.0" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="364.3" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="394.0" y1="339.3" x2="394.0" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="346.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="397.9" y1="308.8" x2="397.9" y2="354.2" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="319.9" width="2.45" height="32.6" fill="var(--up)"/>
<line x1="401.9" y1="305.6" x2="401.9" y2="346.7" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="309.1" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="405.8" y1="298.7" x2="405.8" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="299.7" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="409.8" y1="290.5" x2="409.8" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="304.7" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="413.7" y1="286.1" x2="413.7" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="291.8" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="417.7" y1="271.7" x2="417.7" y2="299.5" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="275.9" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="421.6" y1="271.1" x2="421.6" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="274.4" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="425.6" y1="283.2" x2="425.6" y2="313.8" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="284.0" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="429.5" y1="271.8" x2="429.5" y2="317.5" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="273.7" width="2.45" height="31.0" fill="var(--up)"/>
<line x1="433.5" y1="264.7" x2="433.5" y2="298.5" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="268.9" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="437.4" y1="168.6" x2="437.4" y2="247.6" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="216.6" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="441.4" y1="177.9" x2="441.4" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="192.3" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="445.3" y1="178.3" x2="445.3" y2="231.8" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="188.7" width="2.45" height="33.2" fill="var(--up)"/>
<line x1="449.3" y1="166.7" x2="449.3" y2="225.0" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="180.4" width="2.45" height="24.3" fill="var(--down)"/>
<line x1="453.2" y1="196.8" x2="453.2" y2="271.1" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="199.4" width="2.45" height="58.2" fill="var(--down)"/>
<line x1="457.2" y1="234.3" x2="457.2" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="244.2" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="461.1" y1="213.3" x2="461.1" y2="240.1" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="214.4" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="465.1" y1="182.5" x2="465.1" y2="211.4" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="183.9" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="469.1" y1="183.9" x2="469.1" y2="208.3" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="185.6" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="473.0" y1="193.6" x2="473.0" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="198.5" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="477.0" y1="171.6" x2="477.0" y2="201.1" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="185.7" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="480.9" y1="146.5" x2="480.9" y2="182.4" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="154.3" width="2.45" height="28.1" fill="var(--up)"/>
<line x1="484.9" y1="146.7" x2="484.9" y2="176.2" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="153.4" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="488.8" y1="137.8" x2="488.8" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="144.8" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="492.8" y1="118.7" x2="492.8" y2="148.2" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="125.4" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="496.7" y1="121.8" x2="496.7" y2="162.9" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="124.9" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="500.7" y1="132.1" x2="500.7" y2="152.0" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="137.6" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="504.6" y1="120.0" x2="504.6" y2="154.3" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="129.7" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="508.6" y1="131.6" x2="508.6" y2="192.7" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="133.9" width="2.45" height="31.0" fill="var(--down)"/>
<line x1="512.5" y1="164.8" x2="512.5" y2="184.4" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="167.0" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="516.5" y1="133.8" x2="516.5" y2="165.6" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="142.9" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="520.4" y1="72.6" x2="520.4" y2="130.6" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="86.1" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="524.4" y1="84.0" x2="524.4" y2="144.0" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="93.3" width="2.45" height="29.4" fill="var(--down)"/>
<line x1="528.3" y1="116.1" x2="528.3" y2="154.4" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="118.2" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="532.3" y1="132.7" x2="532.3" y2="165.4" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="134.6" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="536.2" y1="112.3" x2="536.2" y2="146.4" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="114.5" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="540.2" y1="105.6" x2="540.2" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="106.6" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="544.1" y1="139.1" x2="544.1" y2="167.5" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="143.2" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="548.1" y1="145.1" x2="548.1" y2="171.8" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="160.7" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="552.0" y1="136.8" x2="552.0" y2="166.6" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="153.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="556.0" y1="138.9" x2="556.0" y2="179.3" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="154.1" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="560.0" y1="156.4" x2="560.0" y2="182.4" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="169.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="563.9" y1="170.0" x2="563.9" y2="195.3" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="170.1" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="567.9" y1="168.2" x2="567.9" y2="187.7" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="175.6" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="571.8" y1="180.4" x2="571.8" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="182.3" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="575.8" y1="183.5" x2="575.8" y2="216.9" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="188.9" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="579.7" y1="201.8" x2="579.7" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="203.0" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="583.7" y1="231.6" x2="583.7" y2="252.9" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="236.4" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="587.6" y1="207.5" x2="587.6" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="213.1" width="2.45" height="24.3" fill="var(--up)"/>
<line x1="591.6" y1="195.0" x2="591.6" y2="222.2" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="206.6" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="595.5" y1="198.1" x2="595.5" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="210.0" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="599.5" y1="214.9" x2="599.5" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="219.7" width="2.45" height="46.6" fill="var(--down)"/>
<line x1="603.4" y1="242.5" x2="603.4" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="253.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="607.4" y1="223.7" x2="607.4" y2="250.6" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="226.7" width="2.45" height="18.3" fill="var(--up)"/>
<line x1="611.3" y1="208.3" x2="611.3" y2="230.1" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="216.0" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="615.3" y1="184.7" x2="615.3" y2="219.0" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="184.7" width="2.45" height="30.7" fill="var(--up)"/>
<line x1="619.2" y1="187.0" x2="619.2" y2="209.8" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="189.5" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="623.2" y1="199.7" x2="623.2" y2="251.9" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="204.2" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="627.1" y1="186.8" x2="627.1" y2="215.4" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="205.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="631.1" y1="218.3" x2="631.1" y2="248.4" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="223.3" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="635.0" y1="216.6" x2="635.0" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="222.5" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="639.0" y1="228.0" x2="639.0" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="228.0" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="642.9" y1="231.0" x2="642.9" y2="248.1" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="240.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="646.9" y1="236.3" x2="646.9" y2="260.4" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="241.1" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="650.9" y1="243.8" x2="650.9" y2="287.3" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="254.3" width="2.45" height="25.2" fill="var(--down)"/>
<line x1="654.8" y1="267.4" x2="654.8" y2="308.4" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="276.5" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="658.8" y1="302.7" x2="658.8" y2="327.9" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="304.1" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="662.7" y1="312.9" x2="662.7" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="313.3" width="2.45" height="42.4" fill="var(--down)"/>
<line x1="666.7" y1="390.1" x2="666.7" y2="424.4" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="400.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="670.6" y1="415.0" x2="670.6" y2="463.1" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="418.7" width="2.45" height="23.9" fill="var(--down)"/>
<line x1="674.6" y1="413.2" x2="674.6" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="441.4" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="678.5" y1="431.8" x2="678.5" y2="454.9" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="432.3" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="682.5" y1="437.4" x2="682.5" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="441.6" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="686.4" y1="432.8" x2="686.4" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="433.3" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="690.4" y1="430.0" x2="690.4" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="433.3" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="694.3" y1="419.8" x2="694.3" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="432.9" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="698.3" y1="429.1" x2="698.3" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="429.1" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="702.2" y1="440.6" x2="702.2" y2="469.9" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="441.0" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="706.2" y1="438.4" x2="706.2" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="439.4" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="710.1" y1="445.7" x2="710.1" y2="461.2" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="452.7" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="714.1" y1="438.1" x2="714.1" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="445.2" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="718.0" y1="423.9" x2="718.0" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="427.0" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="722.0" y1="427.3" x2="722.0" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="429.2" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="725.9" y1="426.1" x2="725.9" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="427.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="729.9" y1="418.9" x2="729.9" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="426.3" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="733.8" y1="411.7" x2="733.8" y2="444.1" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="411.9" width="2.45" height="21.8" fill="var(--up)"/>
<line x1="737.8" y1="407.8" x2="737.8" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="413.5" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="741.8" y1="414.9" x2="741.8" y2="435.3" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="415.3" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="745.7" y1="409.4" x2="745.7" y2="435.3" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="422.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="749.7" y1="399.5" x2="749.7" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="401.6" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="753.6" y1="395.9" x2="753.6" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="395.9" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="757.6" y1="401.0" x2="757.6" y2="420.3" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="404.3" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="761.5" y1="385.1" x2="761.5" y2="406.0" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="393.4" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="765.5" y1="393.3" x2="765.5" y2="412.6" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="395.4" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="769.4" y1="416.7" x2="769.4" y2="437.6" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="420.8" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="773.4" y1="435.9" x2="773.4" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="440.5" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="777.3" y1="419.7" x2="777.3" y2="448.7" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="445.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="781.3" y1="423.5" x2="781.3" y2="441.2" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="431.1" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="785.2" y1="412.5" x2="785.2" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="421.3" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="789.2" y1="414.4" x2="789.2" y2="435.6" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="422.9" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="793.1" y1="408.0" x2="793.1" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="408.1" width="2.45" height="23.1" fill="var(--up)"/>
<line x1="797.1" y1="397.6" x2="797.1" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="399.6" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="801.0" y1="364.9" x2="801.0" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="369.6" width="2.45" height="41.6" fill="var(--up)"/>
<line x1="805.0" y1="365.1" x2="805.0" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="373.1" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="808.9" y1="396.3" x2="808.9" y2="411.3" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="397.1" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="812.9" y1="390.7" x2="812.9" y2="414.6" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="396.0" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="816.8" y1="388.7" x2="816.8" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="403.6" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="820.8" y1="394.1" x2="820.8" y2="459.8" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="396.8" width="2.45" height="51.0" fill="var(--down)"/>
<line x1="824.7" y1="449.8" x2="824.7" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="452.9" width="2.45" height="30.9" fill="var(--down)"/>
<line x1="828.7" y1="461.6" x2="828.7" y2="477.7" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="462.9" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="832.7" y1="463.6" x2="832.7" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="464.5" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="836.6" y1="444.5" x2="836.6" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="460.1" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="840.6" y1="432.7" x2="840.6" y2="462.5" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="455.2" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="844.5" y1="449.5" x2="844.5" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="452.9" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="848.5" y1="450.9" x2="848.5" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="450.9" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="852.4" y1="420.3" x2="852.4" y2="440.8" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="425.3" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="856.4" y1="375.2" x2="856.4" y2="410.4" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="375.4" width="2.45" height="35.0" fill="var(--up)"/>
<line x1="860.3" y1="375.4" x2="860.3" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="377.3" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="864.3" y1="372.2" x2="864.3" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="375.2" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="868.2" y1="392.5" x2="868.2" y2="418.0" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="392.5" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="872.2" y1="418.7" x2="872.2" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="423.9" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="876.1" y1="420.8" x2="876.1" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="422.4" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="880.1" y1="413.6" x2="880.1" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="418.7" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="884.0" y1="416.1" x2="884.0" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="432.5" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="888.0" y1="427.7" x2="888.0" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="439.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="891.9" y1="428.8" x2="891.9" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="439.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="895.9" y1="413.9" x2="895.9" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="431.2" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="899.8" y1="437.7" x2="899.8" y2="454.5" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="448.5" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="903.8" y1="454.5" x2="903.8" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="455.8" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="907.7" y1="427.0" x2="907.7" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="437.8" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="911.7" y1="313.0" x2="911.7" y2="377.3" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="328.4" width="2.45" height="48.9" fill="var(--up)"/>
<line x1="915.6" y1="287.3" x2="915.6" y2="328.4" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="299.3" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="919.6" y1="288.2" x2="919.6" y2="308.9" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="300.8" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="923.6" y1="276.2" x2="923.6" y2="311.5" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="286.1" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="927.5" y1="290.2" x2="927.5" y2="328.1" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="294.4" width="2.45" height="32.7" fill="var(--down)"/>
<line x1="931.5" y1="315.6" x2="931.5" y2="353.3" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="316.9" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="935.4" y1="296.7" x2="935.4" y2="323.6" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="299.0" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="939.4" y1="285.2" x2="939.4" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="291.7" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="943.3" y1="278.8" x2="943.3" y2="308.3" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="285.4" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="947.3" y1="276.4" x2="947.3" y2="310.7" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="277.8" width="2.45" height="31.9" fill="var(--down)"/>
<line x1="951.2" y1="287.1" x2="951.2" y2="309.3" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="295.8" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="955.2" y1="287.3" x2="955.2" y2="310.9" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="288.2" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="959.1" y1="249.5" x2="959.1" y2="284.6" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="256.7" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="963.1" y1="257.6" x2="963.1" y2="278.0" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="262.6" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="967.0" y1="241.8" x2="967.0" y2="288.1" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="249.3" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="971.0" y1="243.0" x2="971.0" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="243.0" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="974.9" y1="244.1" x2="974.9" y2="265.1" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="245.3" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="978.9" y1="248.7" x2="978.9" y2="276.6" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="251.9" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="982.8" y1="236.8" x2="982.8" y2="263.1" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="248.4" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="986.8" y1="250.7" x2="986.8" y2="286.0" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="252.9" width="2.45" height="32.9" fill="var(--down)"/>
<line x1="990.7" y1="280.5" x2="990.7" y2="326.4" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="290.9" width="2.45" height="31.5" fill="var(--down)"/>
<line x1="994.7" y1="319.3" x2="994.7" y2="339.8" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="322.4" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="998.6" y1="330.6" x2="998.6" y2="349.2" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="337.6" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="1002.6" y1="329.6" x2="1002.6" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="337.6" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="1006.5" y1="325.5" x2="1006.5" y2="353.5" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="334.5" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="1010.5" y1="333.7" x2="1010.5" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="334.0" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="1014.5" y1="328.7" x2="1014.5" y2="344.7" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="329.7" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="1018.4" y1="338.5" x2="1018.4" y2="349.5" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="338.5" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="1022.4" y1="335.9" x2="1022.4" y2="384.4" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="351.3" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="1026.3" y1="371.1" x2="1026.3" y2="408.1" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="375.9" width="2.45" height="29.2" fill="var(--down)"/>
<line x1="1030.3" y1="391.9" x2="1030.3" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="395.9" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="1034.2" y1="400.7" x2="1034.2" y2="420.7" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="408.8" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="1038.2" y1="384.3" x2="1038.2" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="395.6" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="1042.1" y1="380.2" x2="1042.1" y2="420.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="389.9" width="2.45" height="30.0" fill="var(--down)"/>
<line x1="1046.1" y1="406.3" x2="1046.1" y2="420.6" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="408.1" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="1050.0" y1="400.1" x2="1050.0" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="403.7" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="60" y1="374.0" x2="1052" y2="374.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="377.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$547 R1</text>
<text x="1058" y="389.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="175.7" x2="1052" y2="175.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="179.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$642 R2</text>
<text x="1058" y="191.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="459.8" x2="1052" y2="459.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="453.8" font-size="11.5" fill="var(--support)" font-weight="600">$505 S1</text>
<text x="1058" y="465.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="504.9" x2="1052" y2="504.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="498.9" font-size="11.5" fill="var(--support)" font-weight="600">$483 S2</text>
<text x="1058" y="510.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="420.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="412.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $524 (2026-09-11)</text>
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

각 레벨은 "전후 일정 기간 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $642 | 2 | 2026-02-03·2026-04-06 — 2026년 상반기 고점대. 3월 최고 $692.00 직전·직후의 두 스윙 |
| R1 | $547 | 3 | 2026-05-28·2026-06-11·2026-07-07 — 5~7월 반등이 세 번 막힌 대역. 현재가에서 가장 가까운 저항(+4.3%) |
| **현재가** | **$524.19** (2026-09-11 종가) | — | R1 $547와 S1 $505 사이. **위아래 저항·지지와의 거리가 각각 +4.3% · −3.7%로 거의 대칭**인 중립 자리 |
| S1 | $505 | 2 | 2026-05-06·2026-06-02 — 2026년 5~6월의 조정 저점대. 현재가에서 −3.7% |
| S2 | $483 | 4 | 2025-10-27·2026-01-02·2026-06-22·2026-07-21 — 최근 1년 중 가장 여러 번(4회) 닿은 지지. **2026-07-23 실적 급등 직전의 자리**이기도 하다 |

---

## 3. 관측된 특이 구간

### 2026-07-23 — 2026 Q2 실적 발표 후 급등 (최근 5년 최대 상승일)

- 수주잔고가 사상 최대 $230.4B(book-to-bill 3.2배)를 기록하고 FY2026 가이던스가 매출·EPS·FCF 세 항목 모두 상향된 것이 계기였다([최근 뉴스 / 이슈](./08_news.md)).
- 종가 기준 전일 대비 **+10.5%** ($514.36 → $568.59).
- **이 급등 직전의 가격대가 S2 $483**이고, 급등 후 만들어진 고점대가 R1 $547 부근이다. 현재가 $524.19는 **그 급등 구간의 한가운데로 되돌아온 자리**다 — 7월 실적이 만든 상승분의 절반 이상이 되돌려졌다.

### 2026-04-23 — 2026 Q1 실적 발표 후 하락

- 매출 YoY +0.3%에 **분기 FCF −$291M**(CFO $220M − CapEx $511M)으로 현금흐름이 마이너스였던 것이 계기다.
- 종가 기준 전일 대비 **−4.6%** ($555.43 → $529.79).
- 이 하락 이후 $555 위의 가격대는 7월 실적 급등 때 한 번 회복됐다가 다시 빠졌다 — **R1 $547 대역이 2026년 하반기의 실질적 천장으로 작동하고 있다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-12~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `uv run python scripts/gen_technical_chart.py LMT --name "록히드마틴" --close-on 2026-09-11 --emit all`

- **이번 재생성에서 차트를 다시 뽑지 않은 이유**: 이 문서를 재생성한 2026-09-14는 미 증시 정규장이 아직 마감하지 않은 시점이었다. `gen_technical_chart.py`에는 시계열 종료일을 고정하는 옵션이 없어 지금 다시 실행하면 **미완성 장중 봉이 마지막 캔들로 섞이고 그 값이 "종가"로 표기된다**(실제로 재실행 시 `2026-09-14 종가`로 장중 가격이 나왔다). 그래서 **마지막으로 완료된 거래일(2026-09-11)까지를 담은 직전 생성 결과를 그대로 유지**했다. 다음 갱신은 정규장 마감 이후에 재실행할 것.
- **한계**: 원주가 기준이라 기간 내 배당 4회가 반영돼 있지 않다 — 배당수익률이 2.6%대이므로 총수익률은 표시된 가격 변동보다 약 2.6%p 높다. 또한 위 `::: warning`대로 **1년 창이 2025-07-22의 −10.8%를 담지 못해**, 이 차트만 보면 이 종목의 하방 변동성이 실제보다 작아 보인다.

---

*작성일: 2026-09-14*
