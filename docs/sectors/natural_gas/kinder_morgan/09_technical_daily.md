# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-09-04 종가 $31.40은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.**

---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="kmi-chart">
<style>
.kmi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.kmi-chart svg { width:100%; height:auto; display:block; }
.kmi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.kmi-chart .title { fill: var(--ink); font-weight:600; }
.kmi-chart .grid { stroke: var(--grid); stroke-width:1; }
.kmi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kinder Morgan(KMI) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Kinder Morgan (KMI) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $31.40 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="580.4" x2="1052" y2="580.4" class="grid"/>
<text x="52" y="584.4" font-size="11" text-anchor="end" fill="var(--muted)">26</text>
<line x1="60" y1="466.4" x2="1052" y2="466.4" class="grid"/>
<text x="52" y="470.4" font-size="11" text-anchor="end" fill="var(--muted)">28</text>
<line x1="60" y1="352.4" x2="1052" y2="352.4" class="grid"/>
<text x="52" y="356.4" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="238.4" x2="1052" y2="238.4" class="grid"/>
<text x="52" y="242.4" font-size="11" text-anchor="end" fill="var(--muted)">32</text>
<line x1="60" y1="124.4" x2="1052" y2="124.4" class="grid"/>
<text x="52" y="128.4" font-size="11" text-anchor="end" fill="var(--muted)">34</text>
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
<line x1="62.0" y1="531.9" x2="62.0" y2="567.9" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="537.1" width="2.44" height="9.7" fill="var(--down)"/>
<line x1="65.9" y1="518.3" x2="65.9" y2="563.9" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="537.7" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="69.8" y1="529.1" x2="69.8" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="68.62" y="543.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="73.8" y1="497.2" x2="73.8" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="501.7" width="2.44" height="43.3" fill="var(--up)"/>
<line x1="77.7" y1="490.3" x2="77.7" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="490.9" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="81.7" y1="477.2" x2="81.7" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="489.2" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="85.6" y1="480.7" x2="85.6" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="485.2" width="2.44" height="17.7" fill="var(--down)"/>
<line x1="89.5" y1="500.0" x2="89.5" y2="519.4" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="500.0" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="93.5" y1="485.8" x2="93.5" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="490.9" width="2.44" height="16.0" fill="var(--up)"/>
<line x1="97.4" y1="473.2" x2="97.4" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="485.2" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="101.3" y1="482.4" x2="101.3" y2="507.4" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="483.5" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="105.3" y1="497.2" x2="105.3" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="504.0" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="109.2" y1="481.8" x2="109.2" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="496.6" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="113.1" y1="464.7" x2="113.1" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="476.7" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="117.1" y1="455.0" x2="117.1" y2="480.7" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="470.4" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="121.0" y1="437.3" x2="121.0" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="454.4" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="125.0" y1="445.3" x2="125.0" y2="465.8" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="445.3" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="128.9" y1="439.0" x2="128.9" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="448.7" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="132.8" y1="443.6" x2="132.8" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="449.3" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="136.8" y1="414.5" x2="136.8" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="452.7" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="140.7" y1="424.8" x2="140.7" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="440.2" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="144.6" y1="431.1" x2="144.6" y2="470.4" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="432.8" width="2.44" height="37.6" fill="var(--down)"/>
<line x1="148.6" y1="461.8" x2="148.6" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="465.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="152.5" y1="455.6" x2="152.5" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="458.4" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="156.4" y1="447.0" x2="156.4" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="460.7" width="2.44" height="33.1" fill="var(--down)"/>
<line x1="160.4" y1="477.8" x2="160.4" y2="518.3" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="494.9" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="164.3" y1="502.3" x2="164.3" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="504.0" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="168.3" y1="501.7" x2="168.3" y2="523.4" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="505.7" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="172.2" y1="476.1" x2="172.2" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="488.6" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="176.1" y1="481.2" x2="176.1" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="488.1" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="180.1" y1="500.6" x2="180.1" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="501.7" width="2.44" height="16.0" fill="var(--up)"/>
<line x1="184.0" y1="473.8" x2="184.0" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="486.4" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="187.9" y1="487.5" x2="187.9" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="488.1" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="191.9" y1="485.2" x2="191.9" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="190.65" y="491.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="195.8" y1="459.0" x2="195.8" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="466.4" width="2.44" height="99.8" fill="var(--down)"/>
<line x1="199.7" y1="553.0" x2="199.7" y2="594.1" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="553.0" width="2.44" height="35.3" fill="var(--down)"/>
<line x1="203.7" y1="569.6" x2="203.7" y2="591.2" stroke="var(--up)" class="wick"/>
<rect x="202.46" y="571.9" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="207.6" y1="570.1" x2="207.6" y2="590.7" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="570.1" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="211.6" y1="557.6" x2="211.6" y2="588.4" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="571.3" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="215.5" y1="561.6" x2="215.5" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="575.8" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="219.4" y1="564.4" x2="219.4" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="569.6" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="223.4" y1="575.3" x2="223.4" y2="603.2" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="575.8" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="227.3" y1="575.8" x2="227.3" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="582.7" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="231.2" y1="567.9" x2="231.2" y2="599.8" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="585.0" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="235.2" y1="559.9" x2="235.2" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="233.95" y="573.6" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="239.1" y1="545.6" x2="239.1" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="549.1" width="2.44" height="24.5" fill="var(--up)"/>
<line x1="243.0" y1="516.0" x2="243.0" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="520.0" width="2.44" height="29.1" fill="var(--up)"/>
<line x1="247.0" y1="512.0" x2="247.0" y2="535.4" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="515.4" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="250.9" y1="504.0" x2="250.9" y2="528.5" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="522.8" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="254.9" y1="512.0" x2="254.9" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="518.8" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="258.8" y1="495.5" x2="258.8" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="499.5" width="2.44" height="32.5" fill="var(--up)"/>
<line x1="262.7" y1="492.1" x2="262.7" y2="516.6" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="498.9" width="2.44" height="16.5" fill="var(--down)"/>
<line x1="266.7" y1="505.2" x2="266.7" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="518.3" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="270.6" y1="529.1" x2="270.6" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="533.7" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="274.5" y1="502.3" x2="274.5" y2="540.5" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="524.5" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="278.5" y1="519.4" x2="278.5" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="524.5" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="282.4" y1="521.7" x2="282.4" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="522.3" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="286.3" y1="535.4" x2="286.3" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="541.1" width="2.44" height="9.7" fill="var(--down)"/>
<line x1="290.3" y1="518.8" x2="290.3" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="526.2" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="294.2" y1="502.9" x2="294.2" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="505.2" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="298.2" y1="498.3" x2="298.2" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="506.9" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="302.1" y1="505.2" x2="302.1" y2="535.9" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="505.2" width="2.44" height="26.8" fill="var(--down)"/>
<line x1="306.0" y1="502.3" x2="306.0" y2="529.7" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="513.7" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="310.0" y1="474.4" x2="310.0" y2="520.0" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="475.5" width="2.44" height="40.5" fill="var(--up)"/>
<line x1="313.9" y1="466.4" x2="313.9" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="473.8" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="317.8" y1="482.4" x2="317.8" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="482.4" width="2.44" height="24.5" fill="var(--down)"/>
<line x1="321.8" y1="476.7" x2="321.8" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="504.0" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="325.7" y1="503.4" x2="325.7" y2="550.2" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="504.0" width="2.44" height="42.8" fill="var(--down)"/>
<line x1="329.7" y1="533.1" x2="329.7" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="533.7" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="333.6" y1="518.3" x2="333.6" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="525.7" width="2.44" height="13.1" fill="var(--down)"/>
<line x1="337.5" y1="534.2" x2="337.5" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="536.5" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="341.5" y1="542.8" x2="341.5" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="542.8" width="2.44" height="18.8" fill="var(--down)"/>
<line x1="345.4" y1="538.2" x2="345.4" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="543.4" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="349.3" y1="531.4" x2="349.3" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="348.11" y="539.9" width="2.44" height="21.1" fill="var(--down)"/>
<line x1="353.3" y1="538.8" x2="353.3" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="352.05" y="552.5" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="357.2" y1="526.8" x2="357.2" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="529.7" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="361.1" y1="506.9" x2="361.1" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="507.4" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="365.1" y1="502.9" x2="365.1" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="508.0" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="369.0" y1="504.0" x2="369.0" y2="518.8" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="509.2" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="373.0" y1="493.8" x2="373.0" y2="510.9" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="501.7" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="376.9" y1="486.4" x2="376.9" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="490.3" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="380.8" y1="490.3" x2="380.8" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="492.6" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="384.8" y1="472.1" x2="384.8" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="482.9" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="388.7" y1="468.7" x2="388.7" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="468.7" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="392.6" y1="466.4" x2="392.6" y2="546.8" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="466.4" width="2.44" height="67.3" fill="var(--down)"/>
<line x1="396.6" y1="513.7" x2="396.6" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="523.4" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="400.5" y1="496.6" x2="400.5" y2="523.4" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="508.0" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="404.4" y1="495.5" x2="404.4" y2="527.4" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="500.6" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="408.4" y1="509.2" x2="408.4" y2="540.5" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="515.4" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="412.3" y1="494.3" x2="412.3" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="501.7" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="416.3" y1="477.8" x2="416.3" y2="505.7" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="493.2" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="420.2" y1="482.4" x2="420.2" y2="505.2" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="495.5" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="424.1" y1="467.5" x2="424.1" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="468.7" width="2.44" height="23.9" fill="var(--up)"/>
<line x1="428.1" y1="447.0" x2="428.1" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="458.4" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="432.0" y1="428.8" x2="432.0" y2="452.7" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="433.3" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="435.9" y1="342.1" x2="435.9" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="370.1" width="2.44" height="31.9" fill="var(--up)"/>
<line x1="439.9" y1="352.4" x2="439.9" y2="382.0" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="353.5" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="443.8" y1="361.5" x2="443.8" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="363.8" width="2.44" height="26.2" fill="var(--down)"/>
<line x1="447.7" y1="374.6" x2="447.7" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="375.8" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="451.7" y1="334.7" x2="451.7" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="348.4" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="455.6" y1="319.9" x2="455.6" y2="351.8" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="323.9" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="459.6" y1="321.1" x2="459.6" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="324.5" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="463.5" y1="358.1" x2="463.5" y2="383.7" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="359.2" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="467.4" y1="330.2" x2="467.4" y2="371.8" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="334.2" width="2.44" height="33.6" fill="var(--up)"/>
<line x1="471.4" y1="320.5" x2="471.4" y2="378.6" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="329.6" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="475.3" y1="330.2" x2="475.3" y2="369.5" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="333.6" width="2.44" height="21.1" fill="var(--up)"/>
<line x1="479.2" y1="318.8" x2="479.2" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="323.9" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="483.2" y1="288.6" x2="483.2" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="296.0" width="2.44" height="29.1" fill="var(--up)"/>
<line x1="487.1" y1="264.6" x2="487.1" y2="301.1" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="282.9" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="491.0" y1="257.2" x2="491.0" y2="283.4" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="268.0" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="495.0" y1="239.0" x2="495.0" y2="271.5" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="256.1" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="498.9" y1="219.0" x2="498.9" y2="257.2" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="220.2" width="2.44" height="34.8" fill="var(--up)"/>
<line x1="502.9" y1="205.3" x2="502.9" y2="249.2" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="219.6" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="506.8" y1="206.5" x2="506.8" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="209.9" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="510.7" y1="194.5" x2="510.7" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="207.6" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="514.7" y1="194.5" x2="514.7" y2="228.7" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="196.8" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="518.6" y1="167.7" x2="518.6" y2="202.5" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="196.2" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="522.5" y1="197.4" x2="522.5" y2="230.4" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="199.1" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="526.5" y1="192.8" x2="526.5" y2="226.4" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="194.5" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="530.4" y1="167.7" x2="530.4" y2="205.9" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="178.0" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="534.3" y1="161.5" x2="534.3" y2="184.2" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="166.0" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="538.3" y1="117.0" x2="538.3" y2="177.4" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="130.7" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="542.2" y1="110.7" x2="542.2" y2="152.9" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="124.4" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="546.2" y1="123.8" x2="546.2" y2="154.6" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="129.0" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="550.1" y1="119.8" x2="550.1" y2="165.4" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="130.7" width="2.44" height="28.5" fill="var(--down)"/>
<line x1="554.0" y1="143.2" x2="554.0" y2="167.7" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="148.3" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="558.0" y1="143.8" x2="558.0" y2="172.8" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="143.8" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="561.9" y1="159.2" x2="561.9" y2="185.4" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="170.0" width="2.44" height="13.7" fill="var(--down)"/>
<line x1="565.8" y1="164.3" x2="565.8" y2="200.2" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="176.8" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="569.8" y1="129.5" x2="569.8" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="159.7" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="573.7" y1="149.5" x2="573.7" y2="167.7" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="150.1" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="577.7" y1="155.7" x2="577.7" y2="178.0" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="158.6" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="581.6" y1="131.2" x2="581.6" y2="168.3" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="151.8" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="585.5" y1="166.0" x2="585.5" y2="203.6" stroke="var(--down)" class="wick"/>
<rect x="584.30" y="167.7" width="2.44" height="35.9" fill="var(--down)"/>
<line x1="589.5" y1="140.4" x2="589.5" y2="209.9" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="156.3" width="2.44" height="37.0" fill="var(--up)"/>
<line x1="593.4" y1="139.8" x2="593.4" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="153.5" width="2.44" height="37.1" fill="var(--down)"/>
<line x1="597.3" y1="134.7" x2="597.3" y2="213.3" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="140.9" width="2.44" height="51.3" fill="var(--up)"/>
<line x1="601.3" y1="111.3" x2="601.3" y2="146.6" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="128.4" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="605.2" y1="109.6" x2="605.2" y2="143.2" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="125.5" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="609.1" y1="101.6" x2="609.1" y2="137.5" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="120.4" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="613.1" y1="82.8" x2="613.1" y2="134.1" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="122.7" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="617.0" y1="103.9" x2="617.0" y2="151.8" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="108.4" width="2.44" height="35.9" fill="var(--down)"/>
<line x1="621.0" y1="130.7" x2="621.0" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="135.2" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="624.9" y1="163.7" x2="624.9" y2="208.8" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="172.8" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="628.8" y1="152.9" x2="628.8" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="627.61" y="152.9" width="2.44" height="30.2" fill="var(--down)"/>
<line x1="632.8" y1="168.9" x2="632.8" y2="192.2" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="170.6" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="636.7" y1="135.8" x2="636.7" y2="168.9" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="164.3" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="640.6" y1="178.0" x2="640.6" y2="236.7" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="183.7" width="2.44" height="47.9" fill="var(--up)"/>
<line x1="644.6" y1="137.5" x2="644.6" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="183.1" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="648.5" y1="184.8" x2="648.5" y2="212.2" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="192.8" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="652.4" y1="190.0" x2="652.4" y2="254.4" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="193.4" width="2.44" height="41.0" fill="var(--down)"/>
<line x1="656.4" y1="238.4" x2="656.4" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="243.5" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="660.3" y1="246.9" x2="660.3" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="255.5" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="664.3" y1="234.4" x2="664.3" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="250.4" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="668.2" y1="233.3" x2="668.2" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="666.97" y="237.3" width="2.44" height="49.6" fill="var(--up)"/>
<line x1="672.1" y1="214.5" x2="672.1" y2="254.9" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="241.8" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="676.1" y1="228.1" x2="676.1" y2="286.9" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="241.2" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="680.0" y1="237.3" x2="680.0" y2="253.8" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="247.5" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="683.9" y1="215.6" x2="683.9" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="223.0" width="2.44" height="30.8" fill="var(--down)"/>
<line x1="687.9" y1="247.5" x2="687.9" y2="285.7" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="253.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="691.8" y1="239.5" x2="691.8" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="256.6" width="2.44" height="41.6" fill="var(--down)"/>
<line x1="695.7" y1="245.8" x2="695.7" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="250.4" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="699.7" y1="241.2" x2="699.7" y2="261.8" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="246.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="703.6" y1="187.1" x2="703.6" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="188.8" width="2.44" height="61.6" fill="var(--up)"/>
<line x1="707.6" y1="186.0" x2="707.6" y2="216.7" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="191.7" width="2.44" height="16.5" fill="var(--down)"/>
<line x1="711.5" y1="208.8" x2="711.5" y2="230.4" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="211.6" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="715.4" y1="205.9" x2="715.4" y2="233.3" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="213.3" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="719.4" y1="231.0" x2="719.4" y2="276.6" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="237.8" width="2.44" height="24.5" fill="var(--down)"/>
<line x1="723.3" y1="264.1" x2="723.3" y2="302.2" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="265.8" width="2.44" height="22.2" fill="var(--up)"/>
<line x1="727.2" y1="250.4" x2="727.2" y2="282.3" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="264.6" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="731.2" y1="218.5" x2="731.2" y2="266.3" stroke="var(--up)" class="wick"/>
<rect x="729.95" y="224.2" width="2.44" height="33.6" fill="var(--up)"/>
<line x1="735.1" y1="198.5" x2="735.1" y2="225.9" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="207.6" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="739.0" y1="188.8" x2="739.0" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="737.83" y="192.2" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="743.0" y1="154.0" x2="743.0" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="158.6" width="2.44" height="31.9" fill="var(--up)"/>
<line x1="746.9" y1="134.7" x2="746.9" y2="165.4" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="145.5" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="750.9" y1="134.1" x2="750.9" y2="162.0" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="136.9" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="754.8" y1="78.2" x2="754.8" y2="149.5" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="106.7" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="758.7" y1="87.9" x2="758.7" y2="148.9" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="106.7" width="2.44" height="41.0" fill="var(--down)"/>
<line x1="762.7" y1="134.1" x2="762.7" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="142.6" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="766.6" y1="130.7" x2="766.6" y2="161.5" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="136.4" width="2.44" height="15.4" fill="var(--up)"/>
<line x1="770.5" y1="142.1" x2="770.5" y2="190.0" stroke="var(--down)" class="wick"/>
<rect x="769.32" y="145.5" width="2.44" height="43.3" fill="var(--down)"/>
<line x1="774.5" y1="199.1" x2="774.5" y2="231.6" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="205.3" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="778.4" y1="213.3" x2="778.4" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="215.6" width="2.44" height="27.9" fill="var(--down)"/>
<line x1="782.3" y1="250.4" x2="782.3" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="252.1" width="2.44" height="38.8" fill="var(--down)"/>
<line x1="786.3" y1="275.4" x2="786.3" y2="305.7" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="292.0" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="790.2" y1="266.3" x2="790.2" y2="304.5" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="270.3" width="2.44" height="33.6" fill="var(--up)"/>
<line x1="794.2" y1="242.4" x2="794.2" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="266.9" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="798.1" y1="252.1" x2="798.1" y2="274.3" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="255.5" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="802.0" y1="242.4" x2="802.0" y2="264.1" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="256.6" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="806.0" y1="248.1" x2="806.0" y2="281.2" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="262.9" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="809.9" y1="258.4" x2="809.9" y2="293.7" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="275.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="813.8" y1="237.3" x2="813.8" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="247.5" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="817.8" y1="229.8" x2="817.8" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="229.8" width="2.44" height="45.0" fill="var(--down)"/>
<line x1="821.7" y1="224.7" x2="821.7" y2="281.2" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="241.8" width="2.44" height="33.1" fill="var(--up)"/>
<line x1="825.7" y1="254.4" x2="825.7" y2="295.4" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="269.2" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="829.6" y1="255.5" x2="829.6" y2="287.4" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="270.3" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="833.5" y1="264.1" x2="833.5" y2="288.6" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="275.4" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="837.5" y1="257.2" x2="837.5" y2="301.7" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="261.8" width="2.44" height="28.5" fill="var(--up)"/>
<line x1="841.4" y1="221.3" x2="841.4" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="224.2" width="2.44" height="38.2" fill="var(--up)"/>
<line x1="845.3" y1="205.9" x2="845.3" y2="260.1" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="207.6" width="2.44" height="24.5" fill="var(--up)"/>
<line x1="849.3" y1="200.2" x2="849.3" y2="229.3" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="204.8" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="853.2" y1="166.0" x2="853.2" y2="219.6" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="180.8" width="2.44" height="33.1" fill="var(--up)"/>
<line x1="857.1" y1="162.0" x2="857.1" y2="182.5" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="170.6" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="861.1" y1="164.3" x2="861.1" y2="227.6" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="174.0" width="2.44" height="49.0" fill="var(--down)"/>
<line x1="865.0" y1="199.6" x2="865.0" y2="243.0" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="213.3" width="2.44" height="26.8" fill="var(--down)"/>
<line x1="869.0" y1="236.7" x2="869.0" y2="266.3" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="246.9" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="872.9" y1="231.6" x2="872.9" y2="259.5" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="235.0" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="876.8" y1="221.9" x2="876.8" y2="258.4" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="237.3" width="2.44" height="18.8" fill="var(--down)"/>
<line x1="880.8" y1="198.5" x2="880.8" y2="241.8" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="210.5" width="2.44" height="28.5" fill="var(--up)"/>
<line x1="884.7" y1="194.5" x2="884.7" y2="226.4" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="207.1" width="2.44" height="4.0" fill="var(--down)"/>
<line x1="888.6" y1="193.4" x2="888.6" y2="218.5" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="213.9" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="892.6" y1="210.5" x2="892.6" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="217.3" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="896.5" y1="207.6" x2="896.5" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="209.9" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="900.4" y1="204.2" x2="900.4" y2="228.7" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="207.6" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="904.4" y1="201.3" x2="904.4" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="209.9" width="2.44" height="17.1" fill="var(--down)"/>
<line x1="908.3" y1="193.9" x2="908.3" y2="232.1" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="207.6" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="912.3" y1="183.1" x2="912.3" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="186.0" width="2.44" height="35.3" fill="var(--down)"/>
<line x1="916.2" y1="177.4" x2="916.2" y2="224.2" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="205.3" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="920.1" y1="186.0" x2="920.1" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="186.0" width="2.44" height="30.8" fill="var(--down)"/>
<line x1="924.1" y1="196.2" x2="924.1" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="199.1" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="928.0" y1="166.6" x2="928.0" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="181.4" width="2.44" height="13.1" fill="var(--down)"/>
<line x1="931.9" y1="166.6" x2="931.9" y2="204.2" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="186.0" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="935.9" y1="217.3" x2="935.9" y2="257.2" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="223.0" width="2.44" height="29.6" fill="var(--down)"/>
<line x1="939.8" y1="227.0" x2="939.8" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="241.2" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="943.7" y1="222.4" x2="943.7" y2="259.5" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="232.7" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="947.7" y1="241.2" x2="947.7" y2="281.2" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="257.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="951.6" y1="222.4" x2="951.6" y2="264.1" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="228.1" width="2.44" height="35.9" fill="var(--up)"/>
<line x1="955.6" y1="253.8" x2="955.6" y2="280.0" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="258.9" width="2.44" height="13.7" fill="var(--down)"/>
<line x1="959.5" y1="260.6" x2="959.5" y2="313.6" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="273.7" width="2.44" height="22.2" fill="var(--up)"/>
<line x1="963.4" y1="267.5" x2="963.4" y2="300.5" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="277.2" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="967.4" y1="258.9" x2="967.4" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="266.9" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="971.3" y1="283.4" x2="971.3" y2="308.5" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="292.0" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="975.2" y1="272.0" x2="975.2" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="273.2" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="979.2" y1="256.1" x2="979.2" y2="277.2" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="268.0" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="983.1" y1="249.2" x2="983.1" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="253.8" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="987.0" y1="216.2" x2="987.0" y2="262.3" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="233.8" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="991.0" y1="190.5" x2="991.0" y2="231.0" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="191.7" width="2.44" height="33.6" fill="var(--up)"/>
<line x1="994.9" y1="182.5" x2="994.9" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="191.1" width="2.44" height="28.5" fill="var(--down)"/>
<line x1="998.9" y1="178.0" x2="998.9" y2="204.2" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="188.8" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="1002.8" y1="178.0" x2="1002.8" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="181.4" width="2.44" height="52.4" fill="var(--down)"/>
<line x1="1006.7" y1="221.9" x2="1006.7" y2="288.0" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="229.3" width="2.44" height="31.3" fill="var(--down)"/>
<line x1="1010.7" y1="246.4" x2="1010.7" y2="304.5" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="253.2" width="2.44" height="43.3" fill="var(--down)"/>
<line x1="1014.6" y1="287.4" x2="1014.6" y2="323.3" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="295.4" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="1018.5" y1="274.9" x2="1018.5" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="298.8" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="1022.5" y1="223.6" x2="1022.5" y2="306.8" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="237.3" width="2.44" height="65.0" fill="var(--up)"/>
<line x1="1026.4" y1="237.8" x2="1026.4" y2="285.1" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="238.4" width="2.44" height="26.2" fill="var(--down)"/>
<line x1="1030.3" y1="253.8" x2="1030.3" y2="271.5" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="257.2" width="2.44" height="6.3" fill="var(--down)"/>
<line x1="1034.3" y1="216.2" x2="1034.3" y2="258.9" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="224.7" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="1038.2" y1="198.5" x2="1038.2" y2="244.7" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="209.3" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="1042.2" y1="230.4" x2="1042.2" y2="264.6" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="236.1" width="2.44" height="4.0" fill="var(--down)"/>
<line x1="1046.1" y1="233.3" x2="1046.1" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="237.3" width="2.44" height="23.9" fill="var(--down)"/>
<line x1="1050.0" y1="262.3" x2="1050.0" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="270.3" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="60" y1="175.8" x2="1052" y2="175.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="179.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$33 R1</text>
<text x="1058" y="191.3" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="90.6" x2="1052" y2="90.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="94.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$35 R2</text>
<text x="1058" y="106.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="303.0" x2="1052" y2="303.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="297.0" font-size="11.5" fill="var(--support)" font-weight="600">$31 S1</text>
<text x="1058" y="309.0" font-size="9.5" fill="var(--muted)">터치 8회</text>
<line x1="60" y1="569.7" x2="1052" y2="569.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="563.7" font-size="11.5" fill="var(--support)" font-weight="600">$26 S2</text>
<text x="1058" y="575.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="272.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="264.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $31 (2026-09-04)</text>
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
| R2 | $35 | 3 | 2026-03-03·03-27·05-19 — 5월 19일 종가 $34.31이 최근 1년 최고치다. 이후 넉 달간 다시 닿지 못했다 |
| R1 | $33 | 7 | 2026-05-01·06-26·07-09·07-23·07-24·08-18·08-19 — 터치가 가장 많은 저항대. 7월 23~24일은 2026 Q2 실적 발표 직후다 |
| **현재가** | **$31.40** (2026-09-04 종가) | — | R1과 S1 사이, S1 바로 위 |
| S1 | $31 | 8 | 2026-04-17·04-27·05-07·06-01·06-18·07-01·08-04·08-24 — 4월 이후 여덟 차례 되돌아온 구간으로, 현재가가 사실상 이 위에 붙어 있다 |
| S2 | $26 | 4 | 2025-11-03·11-25·12-16·2026-01-06 — 2026년 1월 이후로는 닿지 않았다 |
| 참고선 | $25.84 | — | 최근 1년 최저 종가(2025-11-04). S2 클러스터 안쪽이라 별도 지지로 세지 않는다 |

유효한 클러스터가 위·아래 각각 2개씩이라 R3·S3은 두지 않았다.

---

## 3. 관측된 특이 구간

가격대가 구조적으로 재설정될 만한 갭은 없었다. 다만 실적 발표에 따른 하루 3~5%대 변동이 두 차례 있었고, 둘 다 [최근 뉴스 / 이슈](./08_news.md) 로그의 항목과 이어진다.

- **2025-10-23 (−4.75%, $27.56 → $26.25, 거래량 2,960만 주 — 평소 1,240만 주의 2.4배)**: 전일 발표한 2025 Q3 실적에서 GAAP EPS가 $0.28로 전년 동기와 같아 시장 기대를 밑돌았다. 이 하락이 위 S2($26) 클러스터를 만든 국면의 일부다.
- **2026-01-22 (+3.88%, $28.58 → $29.69, 거래량 2,920만 주 — 평소의 2.4배)**: 전일 FY2025 실적과 2026년 예산(Adjusted EPS $1.36, Adjusted EBITDA $8.6B, 백로그 $10.0B)이 공개된 직후다. 이후 주가는 $26대로 다시 내려오지 않았고, 지지대가 S2($26)에서 S1($31)로 올라섰다.

두 사건 모두 갭이 아니라 연속적인 가격 이동이라, 이전 스윙 레벨을 참고선으로 격하할 필요는 없었다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-05~2026-09-04. 수집 시점: 2026-09-06. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py KMI --name "Kinder Morgan" --close-on 2026-09-04 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **기간 내 분기배당이 4회 지급됐고 이 차트는 원주가라 배당이 반영돼 있지 않다.** 배당수익률이 3.76%인 종목이라 총수익 관점의 성과는 이 차트가 보여주는 가격 변화보다 높다.
    - 해당 기간에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다([핵심 지표](./04_metrics.md) 경고 블록).

---

*작성일: 2026-09-06*
