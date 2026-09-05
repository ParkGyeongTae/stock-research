# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-04 종가 **$292.00**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="lng-chart">
<style>
.lng-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .lng-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .lng-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lng-chart svg { width:100%; height:auto; display:block; }
.lng-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lng-chart .title { fill: var(--ink); font-weight:600; }
.lng-chart .grid { stroke: var(--grid); stroke-width:1; }
.lng-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cheniere Energy(LNG) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cheniere Energy (LNG) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $292.00 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="544.6" x2="1052" y2="544.6" class="grid"/>
<text x="52" y="548.6" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="451.5" x2="1052" y2="451.5" class="grid"/>
<text x="52" y="455.5" font-size="11" text-anchor="end" fill="var(--muted)">220</text>
<line x1="60" y1="358.4" x2="1052" y2="358.4" class="grid"/>
<text x="52" y="362.4" font-size="11" text-anchor="end" fill="var(--muted)">240</text>
<line x1="60" y1="265.4" x2="1052" y2="265.4" class="grid"/>
<text x="52" y="269.4" font-size="11" text-anchor="end" fill="var(--muted)">260</text>
<line x1="60" y1="172.3" x2="1052" y2="172.3" class="grid"/>
<text x="52" y="176.3" font-size="11" text-anchor="end" fill="var(--muted)">280</text>
<line x1="60" y1="79.3" x2="1052" y2="79.3" class="grid"/>
<text x="52" y="83.3" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
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
<line x1="62.0" y1="367.8" x2="62.0" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="375.1" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="65.9" y1="368.4" x2="65.9" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="377.9" width="2.44" height="11.3" fill="var(--down)"/>
<line x1="69.8" y1="370.9" x2="69.8" y2="386.6" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="383.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="73.8" y1="365.9" x2="73.8" y2="384.5" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="372.2" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="77.7" y1="366.2" x2="77.7" y2="381.7" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="372.1" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="81.7" y1="357.8" x2="81.7" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="368.9" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="85.6" y1="365.7" x2="85.6" y2="392.4" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="375.2" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="89.5" y1="379.8" x2="89.5" y2="391.5" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="381.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="93.5" y1="373.1" x2="93.5" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="380.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="97.4" y1="369.8" x2="97.4" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="384.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="101.3" y1="376.2" x2="101.3" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="378.6" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="105.3" y1="392.7" x2="105.3" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="399.4" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="109.2" y1="371.1" x2="109.2" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="382.1" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="113.1" y1="360.1" x2="113.1" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="374.2" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="117.1" y1="359.0" x2="117.1" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="369.5" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="121.0" y1="356.6" x2="121.0" y2="371.4" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="365.8" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="125.0" y1="365.5" x2="125.0" y2="387.4" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="365.5" width="2.44" height="14.1" fill="var(--down)"/>
<line x1="128.9" y1="378.1" x2="128.9" y2="392.1" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="381.8" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="132.8" y1="377.1" x2="132.8" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="382.6" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="136.8" y1="379.0" x2="136.8" y2="400.0" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="395.2" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="140.7" y1="386.4" x2="140.7" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="393.1" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="144.6" y1="380.2" x2="144.6" y2="401.2" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="389.8" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="148.6" y1="374.1" x2="148.6" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="380.1" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="152.5" y1="370.3" x2="152.5" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="378.3" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="156.4" y1="366.3" x2="156.4" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="374.8" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="160.4" y1="388.0" x2="160.4" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="402.4" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="164.3" y1="406.4" x2="164.3" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="414.3" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="168.3" y1="417.4" x2="168.3" y2="435.9" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="422.6" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="172.2" y1="402.7" x2="172.2" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="414.3" width="2.44" height="12.9" fill="var(--down)"/>
<line x1="176.1" y1="422.5" x2="176.1" y2="461.3" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="428.2" width="2.44" height="23.0" fill="var(--down)"/>
<line x1="180.1" y1="447.5" x2="180.1" y2="464.5" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="453.9" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="184.0" y1="442.3" x2="184.0" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="445.4" width="2.44" height="4.2" fill="var(--up)"/>
<line x1="187.9" y1="431.8" x2="187.9" y2="444.3" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="441.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="191.9" y1="426.6" x2="191.9" y2="444.5" stroke="var(--up)" class="wick"/>
<rect x="190.65" y="430.8" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="195.8" y1="415.6" x2="195.8" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="415.6" width="2.44" height="28.8" fill="var(--down)"/>
<line x1="199.7" y1="435.2" x2="199.7" y2="455.7" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="442.2" width="2.44" height="11.2" fill="var(--down)"/>
<line x1="203.7" y1="446.9" x2="203.7" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="449.1" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="207.6" y1="451.5" x2="207.6" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="457.4" width="2.44" height="12.7" fill="var(--down)"/>
<line x1="211.6" y1="467.2" x2="211.6" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="470.1" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="215.5" y1="469.7" x2="215.5" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="491.0" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="219.4" y1="484.1" x2="219.4" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="486.4" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="223.4" y1="478.4" x2="223.4" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="222.14" y="490.9" width="2.44" height="8.9" fill="var(--down)"/>
<line x1="227.3" y1="499.9" x2="227.3" y2="516.7" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="508.7" width="2.44" height="4.4" fill="var(--down)"/>
<line x1="231.2" y1="503.8" x2="231.2" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="505.8" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="235.2" y1="496.9" x2="235.2" y2="511.3" stroke="var(--up)" class="wick"/>
<rect x="233.95" y="507.2" width="2.44" height="2.8" fill="var(--up)"/>
<line x1="239.1" y1="504.2" x2="239.1" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="507.8" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="243.0" y1="489.7" x2="243.0" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="490.8" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="247.0" y1="478.3" x2="247.0" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="245.76" y="488.7" width="2.44" height="2.1" fill="var(--up)"/>
<line x1="250.9" y1="472.2" x2="250.9" y2="492.1" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="481.5" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="254.9" y1="467.7" x2="254.9" y2="489.0" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="479.5" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="258.8" y1="465.7" x2="258.8" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="473.9" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="262.7" y1="461.7" x2="262.7" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="473.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="266.7" y1="466.4" x2="266.7" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="265.45" y="471.9" width="2.44" height="14.7" fill="var(--down)"/>
<line x1="270.6" y1="496.3" x2="270.6" y2="519.0" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="499.8" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="274.5" y1="471.8" x2="274.5" y2="508.1" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="497.3" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="278.5" y1="500.6" x2="278.5" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="277.26" y="503.6" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="282.4" y1="521.3" x2="282.4" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="523.3" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="286.3" y1="521.1" x2="286.3" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="521.7" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="290.3" y1="510.4" x2="290.3" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="517.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="294.2" y1="497.6" x2="294.2" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="505.2" width="2.44" height="12.1" fill="var(--up)"/>
<line x1="298.2" y1="492.4" x2="298.2" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="494.8" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="302.1" y1="491.5" x2="302.1" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="493.8" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="306.0" y1="498.6" x2="306.0" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="500.6" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="310.0" y1="501.1" x2="310.0" y2="514.0" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="505.2" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="313.9" y1="500.4" x2="313.9" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="506.1" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="317.8" y1="522.9" x2="317.8" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="529.6" width="2.44" height="11.2" fill="var(--down)"/>
<line x1="321.8" y1="533.9" x2="321.8" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="542.9" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="325.7" y1="545.0" x2="325.7" y2="584.8" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="549.2" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="329.7" y1="570.4" x2="329.7" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="328.43" y="579.1" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="333.6" y1="573.8" x2="333.6" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="580.4" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="337.5" y1="595.3" x2="337.5" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="595.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="341.5" y1="590.6" x2="341.5" y2="608.8" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="594.5" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="345.4" y1="582.3" x2="345.4" y2="599.4" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="589.5" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="349.3" y1="576.8" x2="349.3" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="591.8" width="2.44" height="2.8" fill="var(--up)"/>
<line x1="353.3" y1="584.8" x2="353.3" y2="596.0" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="588.8" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="357.2" y1="587.3" x2="357.2" y2="596.7" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="591.1" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="361.1" y1="581.3" x2="361.1" y2="597.9" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="583.2" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="365.1" y1="580.8" x2="365.1" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="583.1" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="369.0" y1="588.5" x2="369.0" y2="599.8" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="589.1" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="373.0" y1="578.5" x2="373.0" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="579.0" width="2.44" height="12.4" fill="var(--up)"/>
<line x1="376.9" y1="569.8" x2="376.9" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="575.1" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="380.8" y1="569.0" x2="380.8" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="570.7" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="384.8" y1="545.5" x2="384.8" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="554.8" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="388.7" y1="540.8" x2="388.7" y2="583.5" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="545.9" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="392.6" y1="549.6" x2="392.6" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="552.0" width="2.44" height="17.7" fill="var(--down)"/>
<line x1="396.6" y1="548.2" x2="396.6" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="562.9" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="400.5" y1="549.0" x2="400.5" y2="565.8" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="560.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="404.4" y1="547.7" x2="404.4" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="554.2" width="2.44" height="17.4" fill="var(--down)"/>
<line x1="408.4" y1="563.2" x2="408.4" y2="577.8" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="571.7" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="412.3" y1="566.3" x2="412.3" y2="581.7" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="570.9" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="416.3" y1="527.2" x2="416.3" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="545.9" width="2.44" height="17.6" fill="var(--up)"/>
<line x1="420.2" y1="526.8" x2="420.2" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="531.8" width="2.44" height="7.4" fill="var(--up)"/>
<line x1="424.1" y1="505.0" x2="424.1" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="513.4" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="428.1" y1="503.1" x2="428.1" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="510.7" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="432.0" y1="509.4" x2="432.0" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="510.6" width="2.44" height="8.4" fill="var(--up)"/>
<line x1="435.9" y1="500.4" x2="435.9" y2="521.8" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="507.3" width="2.44" height="5.6" fill="var(--down)"/>
<line x1="439.9" y1="501.1" x2="439.9" y2="515.8" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="506.2" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="443.8" y1="496.7" x2="443.8" y2="519.7" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="499.0" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="447.7" y1="508.5" x2="447.7" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="513.3" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="451.7" y1="493.7" x2="451.7" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="507.2" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="455.6" y1="481.1" x2="455.6" y2="494.7" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="484.1" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="459.6" y1="479.2" x2="459.6" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="485.2" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="463.5" y1="496.0" x2="463.5" y2="514.3" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="501.0" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="467.4" y1="493.5" x2="467.4" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="493.6" width="2.44" height="11.0" fill="var(--up)"/>
<line x1="471.4" y1="480.0" x2="471.4" y2="515.8" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="480.1" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="475.3" y1="484.6" x2="475.3" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="485.0" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="479.2" y1="481.2" x2="479.2" y2="499.1" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="483.6" width="2.44" height="14.6" fill="var(--up)"/>
<line x1="483.2" y1="471.2" x2="483.2" y2="484.5" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="471.8" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="487.1" y1="457.7" x2="487.1" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="459.1" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="491.0" y1="447.3" x2="491.0" y2="461.6" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="452.0" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="495.0" y1="437.9" x2="495.0" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="452.1" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="498.9" y1="443.2" x2="498.9" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="447.8" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="502.9" y1="435.0" x2="502.9" y2="462.9" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="439.9" width="2.44" height="16.2" fill="var(--down)"/>
<line x1="506.8" y1="431.7" x2="506.8" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="434.2" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="510.7" y1="414.1" x2="510.7" y2="432.7" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="422.7" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="514.7" y1="418.2" x2="514.7" y2="432.9" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="421.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="518.6" y1="407.3" x2="518.6" y2="437.3" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="420.1" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="522.5" y1="441.4" x2="522.5" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="447.0" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="526.5" y1="442.4" x2="526.5" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="525.26" y="447.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="530.4" y1="374.4" x2="530.4" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="393.3" width="2.44" height="50.1" fill="var(--up)"/>
<line x1="534.3" y1="374.1" x2="534.3" y2="400.4" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="378.3" width="2.44" height="21.5" fill="var(--up)"/>
<line x1="538.3" y1="300.3" x2="538.3" y2="337.8" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="316.9" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="542.2" y1="285.0" x2="542.2" y2="339.1" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="302.6" width="2.44" height="27.6" fill="var(--down)"/>
<line x1="546.2" y1="313.5" x2="546.2" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="316.7" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="550.1" y1="297.4" x2="550.1" y2="328.9" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="309.6" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="554.0" y1="268.9" x2="554.0" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="288.0" width="2.44" height="12.3" fill="var(--up)"/>
<line x1="558.0" y1="272.5" x2="558.0" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="291.5" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="561.9" y1="311.9" x2="561.9" y2="344.6" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="311.9" width="2.44" height="19.7" fill="var(--down)"/>
<line x1="565.8" y1="306.7" x2="565.8" y2="334.9" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="310.4" width="2.44" height="17.8" fill="var(--up)"/>
<line x1="569.8" y1="273.1" x2="569.8" y2="308.8" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="294.1" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="573.7" y1="269.2" x2="573.7" y2="312.8" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="289.1" width="2.44" height="12.2" fill="var(--down)"/>
<line x1="577.7" y1="295.2" x2="577.7" y2="320.5" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="299.5" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="581.6" y1="288.2" x2="581.6" y2="309.6" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="302.6" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="585.5" y1="231.7" x2="585.5" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="236.4" width="2.44" height="63.3" fill="var(--up)"/>
<line x1="589.5" y1="81.6" x2="589.5" y2="213.7" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="163.6" width="2.44" height="38.4" fill="var(--up)"/>
<line x1="593.4" y1="126.8" x2="593.4" y2="170.5" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="157.8" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="597.3" y1="135.3" x2="597.3" y2="212.1" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="138.8" width="2.44" height="61.7" fill="var(--up)"/>
<line x1="601.3" y1="86.1" x2="601.3" y2="134.9" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="104.5" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="605.2" y1="128.2" x2="605.2" y2="162.1" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="139.9" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="609.1" y1="114.7" x2="609.1" y2="143.0" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="119.3" width="2.44" height="17.9" fill="var(--up)"/>
<line x1="613.1" y1="84.5" x2="613.1" y2="112.7" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="93.6" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="617.0" y1="75.1" x2="617.0" y2="115.3" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="75.1" width="2.44" height="33.7" fill="var(--down)"/>
<line x1="621.0" y1="105.0" x2="621.0" y2="178.6" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="128.7" width="2.44" height="26.1" fill="var(--down)"/>
<line x1="624.9" y1="154.8" x2="624.9" y2="207.1" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="172.5" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="628.8" y1="140.7" x2="628.8" y2="184.8" stroke="var(--down)" class="wick"/>
<rect x="627.61" y="150.3" width="2.44" height="16.6" fill="var(--down)"/>
<line x1="632.8" y1="149.9" x2="632.8" y2="172.1" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="153.5" width="2.44" height="13.4" fill="var(--up)"/>
<line x1="636.7" y1="121.7" x2="636.7" y2="160.9" stroke="var(--down)" class="wick"/>
<rect x="635.48" y="150.5" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="640.6" y1="189.0" x2="640.6" y2="264.8" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="194.6" width="2.44" height="66.1" fill="var(--up)"/>
<line x1="644.6" y1="169.4" x2="644.6" y2="254.9" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="183.8" width="2.44" height="54.7" fill="var(--down)"/>
<line x1="648.5" y1="229.2" x2="648.5" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="239.6" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="652.4" y1="209.8" x2="652.4" y2="271.5" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="224.6" width="2.44" height="33.3" fill="var(--down)"/>
<line x1="656.4" y1="262.6" x2="656.4" y2="285.0" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="262.7" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="660.3" y1="260.0" x2="660.3" y2="283.6" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="273.8" width="2.44" height="6.7" fill="var(--down)"/>
<line x1="664.3" y1="239.7" x2="664.3" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="252.6" width="2.44" height="23.0" fill="var(--up)"/>
<line x1="668.2" y1="288.7" x2="668.2" y2="328.5" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="295.9" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="672.1" y1="280.0" x2="672.1" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="301.0" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="676.1" y1="272.8" x2="676.1" y2="303.5" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="275.7" width="2.44" height="17.2" fill="var(--up)"/>
<line x1="680.0" y1="263.9" x2="680.0" y2="285.8" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="270.0" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="683.9" y1="263.3" x2="683.9" y2="288.5" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="273.7" width="2.44" height="4.8" fill="var(--down)"/>
<line x1="687.9" y1="278.5" x2="687.9" y2="296.7" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="278.9" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="691.8" y1="259.0" x2="691.8" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="690.59" y="268.2" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="695.7" y1="235.6" x2="695.7" y2="260.2" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="242.2" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="699.7" y1="202.0" x2="699.7" y2="227.1" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="208.5" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="703.6" y1="193.5" x2="703.6" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="195.8" width="2.44" height="26.9" fill="var(--up)"/>
<line x1="707.6" y1="195.7" x2="707.6" y2="245.6" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="199.4" width="2.44" height="19.2" fill="var(--down)"/>
<line x1="711.5" y1="196.3" x2="711.5" y2="214.9" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="205.6" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="715.4" y1="201.4" x2="715.4" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="212.1" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="719.4" y1="234.6" x2="719.4" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="258.8" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="723.3" y1="311.4" x2="723.3" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="326.9" width="2.44" height="30.8" fill="var(--up)"/>
<line x1="727.2" y1="326.7" x2="727.2" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="339.8" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="731.2" y1="340.3" x2="731.2" y2="356.4" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="354.1" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="735.1" y1="327.6" x2="735.1" y2="351.5" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="338.4" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="739.0" y1="335.2" x2="739.0" y2="364.9" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="338.7" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="743.0" y1="348.2" x2="743.0" y2="365.4" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="353.4" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="746.9" y1="320.5" x2="746.9" y2="353.5" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="339.8" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="750.9" y1="317.8" x2="750.9" y2="354.3" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="322.4" width="2.44" height="31.8" fill="var(--up)"/>
<line x1="754.8" y1="319.2" x2="754.8" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="322.0" width="2.44" height="5.0" fill="var(--down)"/>
<line x1="758.7" y1="303.9" x2="758.7" y2="346.8" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="327.0" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="762.7" y1="327.0" x2="762.7" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="330.5" width="2.44" height="25.8" fill="var(--down)"/>
<line x1="766.6" y1="353.1" x2="766.6" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="354.5" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="770.5" y1="367.8" x2="770.5" y2="388.1" stroke="var(--down)" class="wick"/>
<rect x="769.32" y="377.1" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="774.5" y1="387.2" x2="774.5" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="400.5" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="778.4" y1="385.1" x2="778.4" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="395.9" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="782.3" y1="410.7" x2="782.3" y2="433.7" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="412.3" width="2.44" height="16.6" fill="var(--down)"/>
<line x1="786.3" y1="391.8" x2="786.3" y2="418.9" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="414.8" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="790.2" y1="359.8" x2="790.2" y2="412.8" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="377.0" width="2.44" height="35.8" fill="var(--up)"/>
<line x1="794.2" y1="351.3" x2="794.2" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="369.0" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="798.1" y1="351.8" x2="798.1" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="353.5" width="2.44" height="28.7" fill="var(--up)"/>
<line x1="802.0" y1="353.3" x2="802.0" y2="375.7" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="353.3" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="806.0" y1="356.9" x2="806.0" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="360.2" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="809.9" y1="360.1" x2="809.9" y2="389.5" stroke="var(--up)" class="wick"/>
<rect x="808.68" y="361.2" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="813.8" y1="330.7" x2="813.8" y2="366.8" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="350.0" width="2.44" height="15.2" fill="var(--up)"/>
<line x1="817.8" y1="331.0" x2="817.8" y2="361.9" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="345.8" width="2.44" height="12.0" fill="var(--down)"/>
<line x1="821.7" y1="339.9" x2="821.7" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="352.5" width="2.44" height="24.1" fill="var(--up)"/>
<line x1="825.7" y1="375.2" x2="825.7" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="380.6" width="2.44" height="24.3" fill="var(--up)"/>
<line x1="829.6" y1="378.7" x2="829.6" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="393.3" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="833.5" y1="396.4" x2="833.5" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="398.4" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="837.5" y1="407.3" x2="837.5" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="414.2" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="841.4" y1="395.0" x2="841.4" y2="427.8" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="401.0" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="845.3" y1="377.5" x2="845.3" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="385.3" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="849.3" y1="391.3" x2="849.3" y2="410.1" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="397.7" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="853.2" y1="372.9" x2="853.2" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="381.2" width="2.44" height="29.5" fill="var(--up)"/>
<line x1="857.1" y1="348.8" x2="857.1" y2="390.3" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="350.8" width="2.44" height="37.4" fill="var(--up)"/>
<line x1="861.1" y1="336.3" x2="861.1" y2="352.7" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="340.0" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="865.0" y1="335.5" x2="865.0" y2="365.1" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="340.0" width="2.44" height="23.1" fill="var(--down)"/>
<line x1="869.0" y1="339.7" x2="869.0" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="340.2" width="2.44" height="26.0" fill="var(--up)"/>
<line x1="872.9" y1="311.6" x2="872.9" y2="353.2" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="322.2" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="876.8" y1="322.1" x2="876.8" y2="342.4" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="330.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="880.8" y1="277.2" x2="880.8" y2="318.9" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="288.7" width="2.44" height="27.9" fill="var(--up)"/>
<line x1="884.7" y1="259.6" x2="884.7" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="261.0" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="888.6" y1="244.8" x2="888.6" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="259.4" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="892.6" y1="242.4" x2="892.6" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="251.4" width="2.44" height="20.3" fill="var(--down)"/>
<line x1="896.5" y1="239.5" x2="896.5" y2="260.7" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="250.1" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="900.4" y1="231.2" x2="900.4" y2="261.9" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="242.0" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="904.4" y1="247.9" x2="904.4" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="253.9" width="2.44" height="30.8" fill="var(--down)"/>
<line x1="908.3" y1="262.7" x2="908.3" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="270.0" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="912.3" y1="247.9" x2="912.3" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="252.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="916.2" y1="231.7" x2="916.2" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="242.4" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="920.1" y1="232.4" x2="920.1" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="246.3" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="924.1" y1="229.4" x2="924.1" y2="260.2" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="231.0" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="928.0" y1="202.0" x2="928.0" y2="225.5" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="208.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="931.9" y1="186.8" x2="931.9" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="212.3" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="935.9" y1="242.6" x2="935.9" y2="289.1" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="246.8" width="2.44" height="37.8" fill="var(--down)"/>
<line x1="939.8" y1="287.6" x2="939.8" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="290.9" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="943.7" y1="259.7" x2="943.7" y2="281.0" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="271.9" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="947.7" y1="270.5" x2="947.7" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="274.4" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="951.6" y1="241.6" x2="951.6" y2="292.3" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="248.8" width="2.44" height="29.7" fill="var(--up)"/>
<line x1="955.6" y1="261.6" x2="955.6" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="267.2" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="959.5" y1="267.2" x2="959.5" y2="308.4" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="278.0" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="963.4" y1="269.8" x2="963.4" y2="293.4" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="269.8" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="967.4" y1="226.4" x2="967.4" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="230.2" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="971.3" y1="239.5" x2="971.3" y2="284.4" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="245.0" width="2.44" height="38.4" fill="var(--down)"/>
<line x1="975.2" y1="235.0" x2="975.2" y2="276.9" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="239.0" width="2.44" height="37.9" fill="var(--up)"/>
<line x1="979.2" y1="222.4" x2="979.2" y2="241.4" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="238.0" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="983.1" y1="214.6" x2="983.1" y2="256.0" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="227.7" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="987.0" y1="218.0" x2="987.0" y2="242.1" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="235.2" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="991.0" y1="207.1" x2="991.0" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="211.2" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="994.9" y1="202.9" x2="994.9" y2="243.3" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="202.9" width="2.44" height="30.2" fill="var(--down)"/>
<line x1="998.9" y1="196.7" x2="998.9" y2="218.1" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="201.3" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="1002.8" y1="193.3" x2="1002.8" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="198.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1006.7" y1="169.5" x2="1006.7" y2="191.2" stroke="var(--up)" class="wick"/>
<rect x="1005.51" y="176.2" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="1010.7" y1="164.2" x2="1010.7" y2="188.8" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="172.5" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="1014.6" y1="167.1" x2="1014.6" y2="192.7" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="168.7" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="1018.5" y1="166.5" x2="1018.5" y2="190.9" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="177.9" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="1022.5" y1="151.3" x2="1022.5" y2="200.2" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="153.3" width="2.44" height="41.4" fill="var(--up)"/>
<line x1="1026.4" y1="152.6" x2="1026.4" y2="191.3" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="155.2" width="2.44" height="13.4" fill="var(--down)"/>
<line x1="1030.3" y1="158.5" x2="1030.3" y2="173.0" stroke="var(--up)" class="wick"/>
<rect x="1029.13" y="161.5" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="1034.3" y1="110.6" x2="1034.3" y2="151.1" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="117.9" width="2.44" height="23.3" fill="var(--up)"/>
<line x1="1038.2" y1="83.1" x2="1038.2" y2="137.8" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="94.5" width="2.44" height="12.1" fill="var(--down)"/>
<line x1="1042.2" y1="88.9" x2="1042.2" y2="136.2" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="98.5" width="2.44" height="27.1" fill="var(--up)"/>
<line x1="1046.1" y1="96.9" x2="1046.1" y2="128.3" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="97.9" width="2.44" height="24.0" fill="var(--down)"/>
<line x1="1050.0" y1="115.0" x2="1050.0" y2="140.6" stroke="var(--up)" class="wick"/>
<rect x="1048.81" y="116.5" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="60" y1="78.4" x2="1052" y2="78.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="81.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$300 R1</text>
<text x="1058" y="93.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="311.8" x2="1052" y2="311.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="305.8" font-size="11.5" fill="var(--support)" font-weight="600">$250 S1</text>
<text x="1058" y="317.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="426.6" x2="1052" y2="426.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="420.6" font-size="11.5" fill="var(--support)" font-weight="600">$225 S2</text>
<text x="1058" y="432.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="466.3" x2="1052" y2="466.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="460.3" font-size="11.5" fill="var(--support)" font-weight="600">$217 S3</text>
<text x="1058" y="472.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="116.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="108.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $292 (2026-09-04)</text>
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
| R1 | $300 | 2 | 2026-03-19·2026-03-30 — 카타르 피격 직후 급등이 만든 고점대. 1년 최고($300.89)와 사실상 같은 자리다 |
| **현재가** | **$292.00** (2026-09-04 종가) | — | R1과 S1 사이 |
| S1 | $250 | 3 | 2026-04-17·2026-07-15·2026-07-28 — 피격 이후 새 레짐에서 세 번 확인된 저점대. 현재가에 가장 가까운 지지 |
| S2 | $225 | 3 | 2025-09-19·2026-05-29·2026-06-18 — 피격 전후에 걸쳐 있어 성격이 섞인 클러스터 |
| S3 | $217 | 2 | 2025-10-17·2026-02-26 — 전부 피격 이전 구간. 현 레짐에서의 유효성은 낮게 볼 것 |
| 참고선 | $186.20 | — | 1년 최저(2025-10월대). 피격 이전 레짐의 바닥이라 근시일 지지로 보지 않고 참고선으로만 둔다 |

현재가는 R1($300)과 S1($250) 사이에 있으며, **저항까지 2.7%·지지까지 −14.4%**로 위쪽에 훨씬 가깝다.

---

## 3. 관측된 특이 구간 — 2026-03-18~19 카타르 라스라판 LNG 설비 피격

- 2026년 3월 18~19일 이란 미사일 공격으로 카타르 라스라판 LNG 단지의 트레인 두 기가 손상돼 세계 LNG 공급의 약 20%가 불가항력으로 이탈했다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 **3월 17일 $251.50 → 18일 $266.22(+5.85%) → 19일 $281.87(+5.88%)**로 이틀간 **+12.1%** 올랐다. 거래량은 평소(일 220만 주 내외) 대비 18일 509만 주(2.3배), **19일 1,219만 주(5.6배)**로 이 기간 최대였다.
- **이 급등은 회사 고유 이벤트가 아니다.** 같은 이틀간 유럽 TTF 가스 선물이 $51.56 → $61.85(+20%)로 뛰었고 Venture Global +14.5%, NextDecade +21.7%가 함께 올랐지만 S&P 500은 오히려 하락했다. 헨리허브(미국 가스)는 $3.03 → $3.17로 거의 움직이지 않았다 — **미국 가스가 아니라 국제 LNG 수급이 이 주식을 움직였다**는 것이 이 구간의 요점이다.
- 이 사건 이후 거래 레짐이 한 단계 올라섰다. 사건 이전 6개월은 $186~$252 구간이었으나 이후 5개월 반은 $240~$301 구간에서 거래되고 있다. 그래서 사건 이전 저점대인 1년 최저($186.20)는 지지 클러스터가 아니라 **참고선**으로만 처리했다.

**최근 2주는 갭 없는 완만한 상승이다.** 2026-08-21 $277.51에서 09-04 $292.00까지 **+5.2%** 올랐고, 그 사이 08-31 CCL Stage 3 완공 발표일(+3.3%, 거래량 0.9배)과 09-02 사상 최고 종가 **$295.86**(거래량 1.2배)이 있었다. **하루 5% 이상의 갭이나 3배 이상의 거래량 급증 없이 오른 구간**이라 3월과 달리 별도 특이 구간으로 잡지 않았다 — 레벨 클러스터에도 새 저항이 형성되지 않았다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-05~2026-09-04. 수집 시점: 2026-09-05. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py` (`LNG --name "Cheniere Energy" --close-on 2026-09-04 --emit all`). 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 252개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **3. 관측된 특이 구간의 3월 급등으로 가격대가 구조적으로 재설정됐다.** 사건 전후를 하나의 표본으로 묶어 계산했으므로, 사건 이전 구간에서 나온 S2·S3는 현재 레짐에서의 유효성이 사건 이후 형성된 S1보다 낮다고 보아야 한다.
    - **현재가가 1년 최고($300.89) 근처라 위쪽 표본이 얇다.** R1($300)의 터치 2회는 전부 3월 말 한 구간에서 나왔으므로, 저항으로서의 신뢰도는 터치 3회인 S1보다 낮다.
    - 기간 내 주식분할·대규모 유상증자는 없었다. 다만 **분기배당 4회가 지급됐고 이 차트는 원주가라 배당을 반영하지 않는다** — 배당수익률이 0.76% 수준이라 영향은 작지만, 수정주가 기반 차트와는 미세하게 다르다.

---

*작성일: 2026-09-05*
