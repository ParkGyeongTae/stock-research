# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-03 종가 $532.95는 [핵심 지표](./04_metrics.md) A.2 "올해(현재)" 열과 [밸류에이션 / 적정주가](./06_valuation.md) 기준일 종가와 정확히 일치**한다. 세 문서 모두 원주가(분할 소급 반영·배당 미반영) 기준이다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-04 ~ 2026-09-03)

<div class="lmt-chart">
<style>
.lmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lmt-chart svg { width:100%; height:auto; display:block; }
.lmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lmt-chart .title { fill: var(--ink); font-weight:600; }
.lmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.lmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="록히드마틴(LMT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">록히드마틴 (LMT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-04 ~ 2026-09-03 · 마지막 종가 $532.95 (2026-09-03) · 단위 USD</text>
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
<line x1="62.0" y1="559.3" x2="62.0" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="560.0" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="65.9" y1="545.2" x2="65.9" y2="560.1" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="545.4" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="69.8" y1="547.4" x2="69.8" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="547.4" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="73.8" y1="557.9" x2="73.8" y2="569.2" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="558.4" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="77.7" y1="544.4" x2="77.7" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="545.4" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="81.7" y1="527.8" x2="81.7" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="531.2" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="85.6" y1="526.6" x2="85.6" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="530.0" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="89.5" y1="523.8" x2="89.5" y2="534.8" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="526.0" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="93.5" y1="515.2" x2="93.5" y2="529.3" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="523.8" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="97.4" y1="517.8" x2="97.4" y2="527.3" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="522.5" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="101.3" y1="523.7" x2="101.3" y2="536.9" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="525.2" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="105.3" y1="518.2" x2="105.3" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="524.0" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="109.2" y1="507.7" x2="109.2" y2="526.5" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="511.2" width="2.44" height="13.9" fill="var(--up)"/>
<line x1="113.1" y1="497.9" x2="113.1" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="498.2" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="117.1" y1="480.4" x2="117.1" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="497.2" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="121.0" y1="489.7" x2="121.0" y2="503.6" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="492.1" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="125.0" y1="489.7" x2="125.0" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="495.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="128.9" y1="472.6" x2="128.9" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="476.8" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="132.8" y1="470.8" x2="132.8" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="472.2" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="136.8" y1="462.1" x2="136.8" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="472.6" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="140.7" y1="463.1" x2="140.7" y2="476.7" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="471.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="144.6" y1="456.4" x2="144.6" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="461.2" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="148.6" y1="438.6" x2="148.6" y2="456.8" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="441.0" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="152.5" y1="437.4" x2="152.5" y2="451.6" stroke="var(--down)" class="wick"/>
<rect x="151.29" y="441.1" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="156.4" y1="437.4" x2="156.4" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="438.9" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="160.4" y1="439.1" x2="160.4" y2="462.6" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="441.8" width="2.44" height="12.7" fill="var(--down)"/>
<line x1="164.3" y1="442.7" x2="164.3" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="452.2" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="168.3" y1="455.1" x2="168.3" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="462.6" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="172.2" y1="456.0" x2="172.2" y2="472.6" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="459.8" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="176.1" y1="460.2" x2="176.1" y2="500.6" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="464.3" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="180.1" y1="467.8" x2="180.1" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="469.0" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="184.0" y1="477.4" x2="184.0" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="480.6" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="187.9" y1="458.3" x2="187.9" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="458.3" width="2.44" height="19.6" fill="var(--up)"/>
<line x1="191.9" y1="456.9" x2="191.9" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="190.65" y="492.3" width="2.44" height="14.1" fill="var(--up)"/>
<line x1="195.8" y1="486.3" x2="195.8" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="488.2" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="199.7" y1="483.0" x2="199.7" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="495.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="203.7" y1="487.5" x2="203.7" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="490.7" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="207.6" y1="496.8" x2="207.6" y2="512.3" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="497.7" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="211.6" y1="492.5" x2="211.6" y2="504.5" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="498.8" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="215.5" y1="493.7" x2="215.5" y2="504.4" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="501.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="219.4" y1="482.0" x2="219.4" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="491.9" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="223.4" y1="483.8" x2="223.4" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="487.4" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="227.3" y1="488.1" x2="227.3" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="489.2" width="2.44" height="6.3" fill="var(--down)"/>
<line x1="231.2" y1="494.4" x2="231.2" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="501.7" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="235.2" y1="499.9" x2="235.2" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="505.7" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="239.1" y1="524.1" x2="239.1" y2="540.8" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="526.3" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="243.0" y1="534.0" x2="243.0" y2="561.3" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="535.0" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="247.0" y1="559.5" x2="247.0" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="561.7" width="2.44" height="8.1" fill="var(--down)"/>
<line x1="250.9" y1="549.8" x2="250.9" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="559.5" width="2.44" height="11.0" fill="var(--up)"/>
<line x1="254.9" y1="553.9" x2="254.9" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="559.6" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="258.8" y1="551.6" x2="258.8" y2="563.6" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="557.6" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="262.7" y1="540.2" x2="262.7" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="541.5" width="2.44" height="20.6" fill="var(--up)"/>
<line x1="266.7" y1="529.4" x2="266.7" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="531.1" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="270.6" y1="501.6" x2="270.6" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="269.38" y="521.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="274.5" y1="527.7" x2="274.5" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="528.6" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="278.5" y1="517.3" x2="278.5" y2="543.0" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="524.7" width="2.44" height="11.6" fill="var(--down)"/>
<line x1="282.4" y1="534.0" x2="282.4" y2="553.5" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="535.6" width="2.44" height="16.2" fill="var(--down)"/>
<line x1="286.3" y1="551.0" x2="286.3" y2="574.1" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="554.6" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="290.3" y1="565.8" x2="290.3" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="569.2" width="2.44" height="2.8" fill="var(--up)"/>
<line x1="294.2" y1="559.1" x2="294.2" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="565.6" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="298.2" y1="557.9" x2="298.2" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="557.9" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="302.1" y1="565.7" x2="302.1" y2="598.0" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="567.4" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="306.0" y1="589.2" x2="306.0" y2="600.6" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="591.1" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="310.0" y1="577.4" x2="310.0" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="580.8" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="313.9" y1="575.2" x2="313.9" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="577.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="317.8" y1="568.3" x2="317.8" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="569.6" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="321.8" y1="541.9" x2="321.8" y2="571.1" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="542.3" width="2.44" height="24.6" fill="var(--up)"/>
<line x1="325.7" y1="526.9" x2="325.7" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="539.2" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="329.7" y1="526.3" x2="329.7" y2="562.0" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="537.0" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="333.6" y1="512.6" x2="333.6" y2="532.1" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="522.6" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="337.5" y1="510.3" x2="337.5" y2="531.1" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="511.5" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="341.5" y1="502.1" x2="341.5" y2="517.7" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="502.8" width="2.44" height="11.3" fill="var(--up)"/>
<line x1="345.4" y1="512.4" x2="345.4" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="512.8" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="349.3" y1="518.4" x2="349.3" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="522.8" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="353.3" y1="519.9" x2="353.3" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="527.7" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="357.2" y1="520.9" x2="357.2" y2="543.3" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="524.2" width="2.44" height="16.1" fill="var(--up)"/>
<line x1="361.1" y1="501.6" x2="361.1" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="504.6" width="2.44" height="17.8" fill="var(--up)"/>
<line x1="365.1" y1="501.7" x2="365.1" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="503.7" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="369.0" y1="488.8" x2="369.0" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="500.1" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="373.0" y1="497.4" x2="373.0" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="501.2" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="376.9" y1="492.5" x2="376.9" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="493.6" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="380.8" y1="487.7" x2="380.8" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="492.6" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="384.8" y1="491.9" x2="384.8" y2="504.7" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="493.3" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="388.7" y1="476.4" x2="388.7" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="476.6" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="392.6" y1="437.6" x2="392.6" y2="464.3" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="446.6" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="396.6" y1="390.3" x2="396.6" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="424.9" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="400.5" y1="403.4" x2="400.5" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="418.1" width="2.44" height="58.9" fill="var(--down)"/>
<line x1="404.4" y1="381.7" x2="404.4" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="404.4" width="2.44" height="27.9" fill="var(--down)"/>
<line x1="408.4" y1="375.1" x2="408.4" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="381.6" width="2.44" height="35.3" fill="var(--up)"/>
<line x1="412.3" y1="358.1" x2="412.3" y2="387.0" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="364.3" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="416.3" y1="339.3" x2="416.3" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="346.1" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="420.2" y1="308.8" x2="420.2" y2="354.2" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="319.9" width="2.44" height="32.6" fill="var(--up)"/>
<line x1="424.1" y1="305.6" x2="424.1" y2="346.7" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="309.1" width="2.44" height="19.1" fill="var(--up)"/>
<line x1="428.1" y1="298.7" x2="428.1" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="299.7" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="432.0" y1="290.5" x2="432.0" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="304.7" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="435.9" y1="286.1" x2="435.9" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="291.8" width="2.44" height="21.1" fill="var(--up)"/>
<line x1="439.9" y1="271.7" x2="439.9" y2="299.5" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="275.9" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="443.8" y1="271.1" x2="443.8" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="274.4" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="447.7" y1="283.2" x2="447.7" y2="313.8" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="284.0" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="451.7" y1="271.8" x2="451.7" y2="317.5" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="273.7" width="2.44" height="31.0" fill="var(--up)"/>
<line x1="455.6" y1="264.7" x2="455.6" y2="298.5" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="268.9" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="459.6" y1="168.6" x2="459.6" y2="247.6" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="216.6" width="2.44" height="27.5" fill="var(--up)"/>
<line x1="463.5" y1="177.9" x2="463.5" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="192.3" width="2.44" height="27.4" fill="var(--up)"/>
<line x1="467.4" y1="178.3" x2="467.4" y2="231.8" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="188.7" width="2.44" height="33.2" fill="var(--up)"/>
<line x1="471.4" y1="166.7" x2="471.4" y2="225.0" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="180.4" width="2.44" height="24.3" fill="var(--down)"/>
<line x1="475.3" y1="196.8" x2="475.3" y2="271.1" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="199.4" width="2.44" height="58.2" fill="var(--down)"/>
<line x1="479.2" y1="234.3" x2="479.2" y2="273.6" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="244.2" width="2.44" height="13.4" fill="var(--up)"/>
<line x1="483.2" y1="213.3" x2="483.2" y2="240.1" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="214.4" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="487.1" y1="182.5" x2="487.1" y2="211.4" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="183.9" width="2.44" height="27.0" fill="var(--up)"/>
<line x1="491.0" y1="183.9" x2="491.0" y2="208.3" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="185.6" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="495.0" y1="193.6" x2="495.0" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="198.5" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="498.9" y1="171.6" x2="498.9" y2="201.1" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="185.7" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="502.9" y1="146.5" x2="502.9" y2="182.4" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="154.3" width="2.44" height="28.1" fill="var(--up)"/>
<line x1="506.8" y1="146.7" x2="506.8" y2="176.2" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="153.4" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="510.7" y1="137.8" x2="510.7" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="144.8" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="514.7" y1="118.7" x2="514.7" y2="148.2" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="125.4" width="2.44" height="20.7" fill="var(--up)"/>
<line x1="518.6" y1="121.8" x2="518.6" y2="162.9" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="124.9" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="522.5" y1="132.1" x2="522.5" y2="152.0" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="137.6" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="526.5" y1="120.0" x2="526.5" y2="154.3" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="129.7" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="530.4" y1="131.6" x2="530.4" y2="192.7" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="133.9" width="2.44" height="31.0" fill="var(--down)"/>
<line x1="534.3" y1="164.8" x2="534.3" y2="184.4" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="167.0" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="538.3" y1="133.8" x2="538.3" y2="165.6" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="142.9" width="2.44" height="20.7" fill="var(--up)"/>
<line x1="542.2" y1="72.6" x2="542.2" y2="130.6" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="86.1" width="2.44" height="18.2" fill="var(--down)"/>
<line x1="546.2" y1="84.0" x2="546.2" y2="144.0" stroke="var(--down)" class="wick"/>
<rect x="544.94" y="93.3" width="2.44" height="29.4" fill="var(--down)"/>
<line x1="550.1" y1="116.1" x2="550.1" y2="154.4" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="118.2" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="554.0" y1="132.7" x2="554.0" y2="165.4" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="134.6" width="2.44" height="14.7" fill="var(--down)"/>
<line x1="558.0" y1="112.3" x2="558.0" y2="146.4" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="114.5" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="561.9" y1="105.6" x2="561.9" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="106.6" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="565.8" y1="139.1" x2="565.8" y2="167.5" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="143.2" width="2.44" height="13.9" fill="var(--down)"/>
<line x1="569.8" y1="145.1" x2="569.8" y2="171.8" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="160.7" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="573.7" y1="136.8" x2="573.7" y2="166.6" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="153.8" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="577.7" y1="138.9" x2="577.7" y2="179.3" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="154.1" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="581.6" y1="156.4" x2="581.6" y2="182.4" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="169.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="585.5" y1="170.0" x2="585.5" y2="195.3" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="170.1" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="589.5" y1="168.2" x2="589.5" y2="187.7" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="175.6" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="593.4" y1="180.4" x2="593.4" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="182.3" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="597.3" y1="183.5" x2="597.3" y2="216.9" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="188.9" width="2.44" height="17.5" fill="var(--down)"/>
<line x1="601.3" y1="201.8" x2="601.3" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="203.0" width="2.44" height="26.6" fill="var(--down)"/>
<line x1="605.2" y1="231.6" x2="605.2" y2="252.9" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="236.4" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="609.1" y1="207.5" x2="609.1" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="213.1" width="2.44" height="24.3" fill="var(--up)"/>
<line x1="613.1" y1="195.0" x2="613.1" y2="222.2" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="206.6" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="617.0" y1="198.1" x2="617.0" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="210.0" width="2.44" height="20.4" fill="var(--down)"/>
<line x1="621.0" y1="214.9" x2="621.0" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="219.7" width="2.44" height="46.6" fill="var(--down)"/>
<line x1="624.9" y1="242.5" x2="624.9" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="253.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="628.8" y1="223.7" x2="628.8" y2="250.6" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="226.7" width="2.44" height="18.3" fill="var(--up)"/>
<line x1="632.8" y1="208.3" x2="632.8" y2="230.1" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="216.0" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="636.7" y1="184.7" x2="636.7" y2="219.0" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="184.7" width="2.44" height="30.7" fill="var(--up)"/>
<line x1="640.6" y1="187.0" x2="640.6" y2="209.8" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="189.5" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="644.6" y1="199.7" x2="644.6" y2="251.9" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="204.2" width="2.44" height="33.6" fill="var(--up)"/>
<line x1="648.5" y1="186.8" x2="648.5" y2="215.4" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="205.3" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="652.4" y1="218.3" x2="652.4" y2="248.4" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="223.3" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="656.4" y1="216.6" x2="656.4" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="222.5" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="660.3" y1="228.0" x2="660.3" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="228.0" width="2.44" height="11.2" fill="var(--down)"/>
<line x1="664.3" y1="231.0" x2="664.3" y2="248.1" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="240.3" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="668.2" y1="236.3" x2="668.2" y2="260.4" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="241.1" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="672.1" y1="243.8" x2="672.1" y2="287.3" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="254.3" width="2.44" height="25.2" fill="var(--down)"/>
<line x1="676.1" y1="267.4" x2="676.1" y2="308.4" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="276.5" width="2.44" height="25.5" fill="var(--down)"/>
<line x1="680.0" y1="302.7" x2="680.0" y2="327.9" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="304.1" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="683.9" y1="312.9" x2="683.9" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="313.3" width="2.44" height="42.4" fill="var(--down)"/>
<line x1="687.9" y1="390.1" x2="687.9" y2="424.4" stroke="var(--down)" class="wick"/>
<rect x="686.65" y="400.3" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="691.8" y1="415.0" x2="691.8" y2="463.1" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="418.7" width="2.44" height="23.9" fill="var(--down)"/>
<line x1="695.7" y1="413.2" x2="695.7" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="441.4" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="699.7" y1="431.8" x2="699.7" y2="454.9" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="432.3" width="2.44" height="12.7" fill="var(--down)"/>
<line x1="703.6" y1="437.4" x2="703.6" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="702.40" y="441.6" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="707.6" y1="432.8" x2="707.6" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="433.3" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="711.5" y1="430.0" x2="711.5" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="433.3" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="715.4" y1="419.8" x2="715.4" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="432.9" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="719.4" y1="429.1" x2="719.4" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="429.1" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="723.3" y1="440.6" x2="723.3" y2="469.9" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="441.0" width="2.44" height="11.0" fill="var(--up)"/>
<line x1="727.2" y1="438.4" x2="727.2" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="439.4" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="731.2" y1="445.7" x2="731.2" y2="461.2" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="452.7" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="735.1" y1="438.1" x2="735.1" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="445.2" width="2.44" height="15.0" fill="var(--up)"/>
<line x1="739.0" y1="423.9" x2="739.0" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="737.83" y="427.0" width="2.44" height="17.6" fill="var(--up)"/>
<line x1="743.0" y1="427.3" x2="743.0" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="429.2" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="746.9" y1="426.1" x2="746.9" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="427.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="750.9" y1="418.9" x2="750.9" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="426.3" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="754.8" y1="411.7" x2="754.8" y2="444.1" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="411.9" width="2.44" height="21.8" fill="var(--up)"/>
<line x1="758.7" y1="407.8" x2="758.7" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="413.5" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="762.7" y1="414.9" x2="762.7" y2="435.3" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="415.3" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="766.6" y1="409.4" x2="766.6" y2="435.3" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="422.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="770.5" y1="399.5" x2="770.5" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="401.6" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="774.5" y1="395.9" x2="774.5" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="395.9" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="778.4" y1="401.0" x2="778.4" y2="420.3" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="404.3" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="782.3" y1="385.1" x2="782.3" y2="406.0" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="393.4" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="786.3" y1="393.3" x2="786.3" y2="412.6" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="395.4" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="790.2" y1="416.7" x2="790.2" y2="437.6" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="420.8" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="794.2" y1="435.9" x2="794.2" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="440.5" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="798.1" y1="419.7" x2="798.1" y2="448.7" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="445.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="802.0" y1="423.5" x2="802.0" y2="441.2" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="431.1" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="806.0" y1="412.5" x2="806.0" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="421.3" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="809.9" y1="414.4" x2="809.9" y2="435.6" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="422.9" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="813.8" y1="408.0" x2="813.8" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="408.1" width="2.44" height="23.1" fill="var(--up)"/>
<line x1="817.8" y1="397.6" x2="817.8" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="399.6" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="821.7" y1="364.9" x2="821.7" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="369.6" width="2.44" height="41.6" fill="var(--up)"/>
<line x1="825.7" y1="365.1" x2="825.7" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="373.1" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="829.6" y1="396.3" x2="829.6" y2="411.3" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="397.1" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="833.5" y1="390.7" x2="833.5" y2="414.6" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="396.0" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="837.5" y1="388.7" x2="837.5" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="403.6" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="841.4" y1="394.1" x2="841.4" y2="459.8" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="396.8" width="2.44" height="51.0" fill="var(--down)"/>
<line x1="845.3" y1="449.8" x2="845.3" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="452.9" width="2.44" height="30.9" fill="var(--down)"/>
<line x1="849.3" y1="461.6" x2="849.3" y2="477.7" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="462.9" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="853.2" y1="463.6" x2="853.2" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="464.5" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="857.1" y1="444.5" x2="857.1" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="460.1" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="861.1" y1="432.7" x2="861.1" y2="462.5" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="455.2" width="2.44" height="4.5" fill="var(--up)"/>
<line x1="865.0" y1="449.5" x2="865.0" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="452.9" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="869.0" y1="450.9" x2="869.0" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="450.9" width="2.44" height="11.3" fill="var(--up)"/>
<line x1="872.9" y1="420.3" x2="872.9" y2="440.8" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="425.3" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="876.8" y1="375.2" x2="876.8" y2="410.4" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="375.4" width="2.44" height="35.0" fill="var(--up)"/>
<line x1="880.8" y1="375.4" x2="880.8" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="377.3" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="884.7" y1="372.2" x2="884.7" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="375.2" width="2.44" height="22.0" fill="var(--down)"/>
<line x1="888.6" y1="392.5" x2="888.6" y2="418.0" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="392.5" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="892.6" y1="418.7" x2="892.6" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="423.9" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="896.5" y1="420.8" x2="896.5" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="422.4" width="2.44" height="14.1" fill="var(--up)"/>
<line x1="900.4" y1="413.6" x2="900.4" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="418.7" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="904.4" y1="416.1" x2="904.4" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="432.5" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="908.3" y1="427.7" x2="908.3" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="439.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="912.3" y1="428.8" x2="912.3" y2="447.1" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="439.5" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="916.2" y1="413.9" x2="916.2" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="431.2" width="2.44" height="21.2" fill="var(--down)"/>
<line x1="920.1" y1="437.7" x2="920.1" y2="454.5" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="448.5" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="924.1" y1="454.5" x2="924.1" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="455.8" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="928.0" y1="427.0" x2="928.0" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="437.8" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="931.9" y1="313.0" x2="931.9" y2="377.3" stroke="var(--up)" class="wick"/>
<rect x="930.72" y="328.4" width="2.44" height="48.9" fill="var(--up)"/>
<line x1="935.9" y1="287.3" x2="935.9" y2="328.4" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="299.3" width="2.44" height="29.0" fill="var(--up)"/>
<line x1="939.8" y1="288.2" x2="939.8" y2="308.9" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="300.8" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="943.7" y1="276.2" x2="943.7" y2="311.5" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="286.1" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="947.7" y1="290.2" x2="947.7" y2="328.1" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="294.4" width="2.44" height="32.7" fill="var(--down)"/>
<line x1="951.6" y1="315.6" x2="951.6" y2="353.3" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="316.9" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="955.6" y1="296.7" x2="955.6" y2="323.6" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="299.0" width="2.44" height="17.9" fill="var(--up)"/>
<line x1="959.5" y1="285.2" x2="959.5" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="291.7" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="963.4" y1="278.8" x2="963.4" y2="308.3" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="285.4" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="967.4" y1="276.4" x2="967.4" y2="310.7" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="277.8" width="2.44" height="31.9" fill="var(--down)"/>
<line x1="971.3" y1="287.1" x2="971.3" y2="309.3" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="295.8" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="975.2" y1="287.3" x2="975.2" y2="310.9" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="288.2" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="979.2" y1="249.5" x2="979.2" y2="284.6" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="256.7" width="2.44" height="23.6" fill="var(--up)"/>
<line x1="983.1" y1="257.6" x2="983.1" y2="278.0" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="262.6" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="987.0" y1="241.8" x2="987.0" y2="288.1" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="249.3" width="2.44" height="23.3" fill="var(--up)"/>
<line x1="991.0" y1="243.0" x2="991.0" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="243.0" width="2.44" height="24.4" fill="var(--down)"/>
<line x1="994.9" y1="244.1" x2="994.9" y2="265.1" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="245.3" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="998.9" y1="248.7" x2="998.9" y2="276.6" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="251.9" width="2.44" height="24.4" fill="var(--down)"/>
<line x1="1002.8" y1="236.8" x2="1002.8" y2="263.1" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="248.4" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="1006.7" y1="250.7" x2="1006.7" y2="286.0" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="252.9" width="2.44" height="32.9" fill="var(--down)"/>
<line x1="1010.7" y1="280.5" x2="1010.7" y2="326.4" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="290.9" width="2.44" height="31.5" fill="var(--down)"/>
<line x1="1014.6" y1="319.3" x2="1014.6" y2="339.8" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="322.4" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="1018.5" y1="330.6" x2="1018.5" y2="349.2" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="337.6" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="1022.5" y1="329.6" x2="1022.5" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="337.6" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="1026.4" y1="325.5" x2="1026.4" y2="353.5" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="334.5" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="1030.3" y1="333.7" x2="1030.3" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="1029.13" y="334.0" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="1034.3" y1="328.7" x2="1034.3" y2="344.7" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="329.7" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="1038.2" y1="338.5" x2="1038.2" y2="349.5" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="338.5" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="1042.2" y1="335.9" x2="1042.2" y2="384.4" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="351.3" width="2.44" height="27.0" fill="var(--down)"/>
<line x1="1046.1" y1="371.1" x2="1046.1" y2="408.1" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="375.9" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="1050.0" y1="391.9" x2="1050.0" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="395.9" width="2.44" height="6.3" fill="var(--down)"/>
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
<circle cx="1052.0" cy="402.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="394.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $533 (2026-09-03)</text>
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
| R2 | $642 | 2 | 2026-02-03 · 2026-04-06 — FY2025 실적 발표(2026-01-29) 이후 상승 구간의 고점대. 현재가에서 **+20.5%** 떨어져 있어 근시일 저항으로 보기 어렵다 |
| R1 | $547 | 3 | 2026-05-28 · 2026-06-11 · 2026-07-07 — **현재가 바로 위**(+2.6%)의 가장 가까운 저항. 2026년 3월 고점 이후 되돌림 구간에서 세 번 눌린 자리다 |
| **현재가** | **$532.95** (2026-09-03 종가) | — | R1과 S1 사이 |
| S1 | $505 | 2 | 2026-05-06 · 2026-06-02 — 현재가에서 **−5.2%**, 가장 근접한 지지 |
| S2 | $483 | 4 | 2025-10-27 · 2026-01-02 · 2026-06-22 · 2026-07-21 — **터치 4회로 이 구간에서 가장 두터운 레벨**. FY2025 회계연도 말 종가 $483.67과 사실상 같은 가격대다([핵심 지표](./04_metrics.md) A.2) |
| 참고선 | $692.00 | — | 최근 1년 최고가(2026-03-02). 단일 고점이라 클러스터를 이루지 않았고 현재가에서 **+29.8%** 떨어져 있어 근시일 저항으로 보지 않는다 |
| 참고선 | $437.25 | — | 최근 1년 최저가(2025-12-01 부근). 현재가에서 −18.0%. 아래 3절의 재평가 이후 형성된 저점이라 참고선으로만 둔다 |

**유효한 클러스터가 4개(R2·R1·S1·S2)뿐이라 R3·S3는 만들지 않았다** — 스크립트가 터치 2회 이상 조건으로 잡아낸 것이 이 4개다. `--force-level`은 쓰지 않았다.

---

## 3. 관측된 특이 구간 — 2026-07-23 2026 Q2 실적 발표

- 2026년 2분기 실적 발표일. 수주잔고 사상 최대 $230.4B, book-to-bill 3.2배, FY2026 가이던스 3개 항목 동시 상향([최근 뉴스 / 이슈](./08_news.md) 로그).
- 종가 기준 전일 대비 **+10.5%** ($514.36 → $568.59), 거래량은 평소(일 143만 주 내외) 대비 약 **2.3배**인 **328만 주**. **최근 5년 내 최대 상승일**이다.
- 이 날을 기점으로 거래 레짐이 바뀌었다기보다, **6월 이후 $505~$547 박스를 위로 이탈했다가 8월에 다시 그 박스로 되돌아온** 형태다. 8월 말 $563.85에서 9월 초 $532.95까지 3거래일에 −5.5% 밀리며 R1($547) 아래로 내려왔다.

**참고 — 이 차트 구간 직전의 반대 사례**: 정확히 1년 전인 2025-07-22에 손실충당 발표로 하루 **−10.8%**($460.53 → $410.74)가 있었다. 그 날은 최근 1년 일봉 구간(2025-09-04 시작) 밖이라 이 차트에 나타나지 않지만, 아래 [주봉 차트](./10_technical_weekly.md)에서는 보인다. 현재의 지지 클러스터 S2($483)가 그 급락 이후 회복 과정에서 만들어진 가격대다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-04~2026-09-03. 수집 시점: 2026-09-04. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py LMT --name "록히드마틴" --close-on 2026-09-03 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **기간 내 배당 4회(분기당 $3.30~3.45)가 반영되지 않은 원주가**다. 배당락일마다 이론적으로 배당금만큼 가격이 낮아지므로, 연 $13.35~13.80(현재가의 2.6%)만큼 레벨이 아래로 눌린 셈이다.
    - 이 기간에 주식분할·대규모 유상증자는 없었다. 자사주매입은 있었으나 가격 연속성을 깨지 않는다.
    - 3절의 +10.5% 갭이 R1($547) 클러스터의 형성 시점(2026-05~07)과 겹친다 — 갭으로 건너뛴 구간이라 그 사이 가격대($514~$547)에는 실제 거래가 얇다.

---

*작성일: 2026-09-04*
