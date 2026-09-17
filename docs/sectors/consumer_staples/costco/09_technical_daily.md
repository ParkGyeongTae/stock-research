# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-15 종가 $901.35**는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.
- ⚠️ **차트의 마지막 캔들은 미완성 봉이다.** 이 문서는 2026-09-16 미 동부시간 10:01(정규장 개장 중)에 생성돼, 차트 우측 끝에 그날의 **장중 봉**이 들어가 있다. **이 폴더의 모든 문서가 쓰는 기준 종가는 마지막 완료 거래일인 2026-09-15의 $901.35**이며, 아래 §2 현재가 행도 그 값이다(§4 참고).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-16 ~ 2026-09-16)

<style>
.cost-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .cost-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cost-chart svg { width:100%; height:auto; display:block; }
.cost-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cost-chart .title { fill: var(--ink); font-weight:600; }
.cost-chart .grid { stroke: var(--grid); stroke-width:1; }
.cost-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="cost-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코스트코(COST) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코스트코 (COST) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-16 ~ 2026-09-16 · 마지막 종가 $898.49 (2026-09-16) · 단위 USD</text>
<line x1="60" y1="594.3" x2="1052" y2="594.3" class="grid"/>
<text x="52" y="598.3" font-size="11" text-anchor="end" fill="var(--muted)">850</text>
<line x1="60" y1="488.8" x2="1052" y2="488.8" class="grid"/>
<text x="52" y="492.8" font-size="11" text-anchor="end" fill="var(--muted)">900</text>
<line x1="60" y1="383.2" x2="1052" y2="383.2" class="grid"/>
<text x="52" y="387.2" font-size="11" text-anchor="end" fill="var(--muted)">950</text>
<line x1="60" y1="277.7" x2="1052" y2="277.7" class="grid"/>
<text x="52" y="281.7" font-size="11" text-anchor="end" fill="var(--muted)">1,000</text>
<line x1="60" y1="172.1" x2="1052" y2="172.1" class="grid"/>
<text x="52" y="176.1" font-size="11" text-anchor="end" fill="var(--muted)">1,050</text>
<line x1="60" y1="66.6" x2="1052" y2="66.6" class="grid"/>
<text x="52" y="70.6" font-size="11" text-anchor="end" fill="var(--muted)">1,100</text>
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
<line x1="62.0" y1="363.0" x2="62.0" y2="381.5" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="364.0" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="65.9" y1="353.7" x2="65.9" y2="375.9" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="355.7" width="2.44" height="20.1" fill="var(--up)"/>
<line x1="69.8" y1="356.7" x2="69.8" y2="381.8" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="367.7" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="73.8" y1="367.5" x2="73.8" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="372.7" width="2.44" height="8.1" fill="var(--down)"/>
<line x1="77.7" y1="383.2" x2="77.7" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="76.49" y="388.8" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="81.7" y1="393.8" x2="81.7" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="396.7" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="85.6" y1="375.5" x2="85.6" y2="397.8" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="393.2" width="2.44" height="2.1" fill="var(--up)"/>
<line x1="89.5" y1="376.9" x2="89.5" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="378.0" width="2.44" height="19.3" fill="var(--down)"/>
<line x1="93.5" y1="430.4" x2="93.5" y2="478.1" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="434.8" width="2.44" height="20.3" fill="var(--down)"/>
<line x1="97.4" y1="452.4" x2="97.4" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="453.2" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="101.3" y1="424.4" x2="101.3" y2="460.6" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="434.7" width="2.44" height="19.8" fill="var(--up)"/>
<line x1="105.3" y1="438.1" x2="105.3" y2="465.2" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="440.2" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="109.2" y1="449.7" x2="109.2" y2="467.6" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="453.4" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="113.1" y1="450.6" x2="113.1" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="111.92" y="455.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="117.1" y1="455.5" x2="117.1" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="456.1" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="121.0" y1="451.5" x2="121.0" y2="480.6" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="457.5" width="2.44" height="12.8" fill="var(--up)"/>
<line x1="125.0" y1="454.2" x2="125.0" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="457.5" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="128.9" y1="396.4" x2="128.9" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="398.2" width="2.44" height="22.3" fill="var(--up)"/>
<line x1="132.8" y1="392.8" x2="132.8" y2="427.6" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="395.0" width="2.44" height="30.4" fill="var(--down)"/>
<line x1="136.8" y1="412.8" x2="136.8" y2="440.2" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="413.7" width="2.44" height="13.8" fill="var(--up)"/>
<line x1="140.7" y1="388.7" x2="140.7" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="390.6" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="144.6" y1="353.7" x2="144.6" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="372.7" width="2.44" height="19.0" fill="var(--up)"/>
<line x1="148.6" y1="366.5" x2="148.6" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="371.5" width="2.44" height="63.2" fill="var(--down)"/>
<line x1="152.5" y1="406.8" x2="152.5" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="412.1" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="156.4" y1="404.8" x2="156.4" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="412.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="160.4" y1="397.2" x2="160.4" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="409.6" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="164.3" y1="376.9" x2="164.3" y2="420.2" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="394.5" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="168.3" y1="392.8" x2="168.3" y2="416.0" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="392.8" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="172.2" y1="398.0" x2="172.2" y2="425.1" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="404.3" width="2.44" height="16.6" fill="var(--down)"/>
<line x1="176.1" y1="418.7" x2="176.1" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="425.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="180.1" y1="423.9" x2="180.1" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="432.1" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="184.0" y1="446.8" x2="184.0" y2="469.1" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="448.7" width="2.44" height="13.9" fill="var(--down)"/>
<line x1="187.9" y1="440.2" x2="187.9" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="446.2" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="191.9" y1="446.6" x2="191.9" y2="468.3" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="454.6" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="195.8" y1="427.2" x2="195.8" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="429.6" width="2.44" height="33.0" fill="var(--up)"/>
<line x1="199.7" y1="401.9" x2="199.7" y2="427.6" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="402.8" width="2.44" height="15.9" fill="var(--up)"/>
<line x1="203.7" y1="393.2" x2="203.7" y2="430.8" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="404.3" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="207.6" y1="436.0" x2="207.6" y2="471.3" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="437.4" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="211.6" y1="410.7" x2="211.6" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="210.34" y="426.4" width="2.44" height="14.3" fill="var(--down)"/>
<line x1="215.5" y1="442.3" x2="215.5" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="448.7" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="219.4" y1="448.9" x2="219.4" y2="461.3" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="453.9" width="2.44" height="5.6" fill="var(--down)"/>
<line x1="223.4" y1="450.6" x2="223.4" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="222.14" y="456.1" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="227.3" y1="432.3" x2="227.3" y2="464.0" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="435.8" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="231.2" y1="427.8" x2="231.2" y2="456.9" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="431.5" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="235.2" y1="436.2" x2="235.2" y2="470.2" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="442.3" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="239.1" y1="448.9" x2="239.1" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="462.2" width="2.44" height="37.0" fill="var(--down)"/>
<line x1="243.0" y1="499.3" x2="243.0" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="499.3" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="247.0" y1="479.1" x2="247.0" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="502.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="250.9" y1="477.5" x2="250.9" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="490.9" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="254.9" y1="485.9" x2="254.9" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="490.9" width="2.44" height="27.2" fill="var(--down)"/>
<line x1="258.8" y1="497.8" x2="258.8" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="500.7" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="262.7" y1="463.4" x2="262.7" y2="498.0" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="471.3" width="2.44" height="25.8" fill="var(--up)"/>
<line x1="266.7" y1="458.8" x2="266.7" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="460.1" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="270.6" y1="449.6" x2="270.6" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="269.38" y="460.9" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="274.5" y1="440.2" x2="274.5" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="442.3" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="278.5" y1="433.2" x2="278.5" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="441.8" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="282.4" y1="472.0" x2="282.4" y2="513.9" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="473.9" width="2.44" height="23.6" fill="var(--down)"/>
<line x1="286.3" y1="476.3" x2="286.3" y2="503.6" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="494.6" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="290.3" y1="501.4" x2="290.3" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="289.07" y="502.5" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="294.2" y1="512.0" x2="294.2" y2="527.8" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="513.2" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="298.2" y1="510.8" x2="298.2" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="514.5" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="302.1" y1="518.3" x2="302.1" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="521.5" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="306.0" y1="512.8" x2="306.0" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="521.6" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="310.0" y1="515.2" x2="310.0" y2="591.4" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="526.5" width="2.44" height="45.5" fill="var(--down)"/>
<line x1="313.9" y1="565.6" x2="313.9" y2="606.9" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="572.4" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="317.8" y1="555.1" x2="317.8" y2="577.0" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="567.6" width="2.44" height="8.8" fill="var(--up)"/>
<line x1="321.8" y1="566.6" x2="321.8" y2="589.0" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="572.6" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="325.7" y1="576.5" x2="325.7" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="580.5" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="329.7" y1="582.7" x2="329.7" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="328.43" y="585.9" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="333.6" y1="583.8" x2="333.6" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="584.2" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="337.5" y1="539.4" x2="337.5" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="548.2" width="2.44" height="28.0" fill="var(--up)"/>
<line x1="341.5" y1="536.1" x2="341.5" y2="554.2" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="545.0" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="345.4" y1="542.6" x2="345.4" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="545.2" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="349.3" y1="556.7" x2="349.3" y2="570.2" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="561.3" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="353.3" y1="556.3" x2="353.3" y2="570.4" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="563.6" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="357.2" y1="566.7" x2="357.2" y2="589.1" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="570.8" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="361.1" y1="533.6" x2="361.1" y2="571.4" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="540.0" width="2.44" height="24.9" fill="var(--up)"/>
<line x1="365.1" y1="501.3" x2="365.1" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="511.8" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="369.0" y1="502.3" x2="369.0" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="505.7" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="373.0" y1="421.9" x2="373.0" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="456.5" width="2.44" height="29.9" fill="var(--up)"/>
<line x1="376.9" y1="425.8" x2="376.9" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="436.3" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="380.8" y1="394.1" x2="380.8" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="397.8" width="2.44" height="47.9" fill="var(--up)"/>
<line x1="384.8" y1="398.2" x2="384.8" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="400.3" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="388.7" y1="371.4" x2="388.7" y2="407.9" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="381.2" width="2.44" height="26.7" fill="var(--up)"/>
<line x1="392.6" y1="365.7" x2="392.6" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="369.0" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="396.6" y1="351.6" x2="396.6" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="354.5" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="400.5" y1="341.2" x2="400.5" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="353.1" width="2.44" height="12.4" fill="var(--up)"/>
<line x1="404.4" y1="299.5" x2="404.4" y2="363.0" stroke="var(--up)" class="wick"/>
<rect x="403.22" y="313.9" width="2.44" height="49.1" fill="var(--up)"/>
<line x1="408.4" y1="311.4" x2="408.4" y2="337.7" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="324.3" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="412.3" y1="309.7" x2="412.3" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="313.0" width="2.44" height="24.9" fill="var(--up)"/>
<line x1="416.3" y1="292.4" x2="416.3" y2="327.6" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="306.3" width="2.44" height="18.5" fill="var(--down)"/>
<line x1="420.2" y1="324.1" x2="420.2" y2="358.5" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="324.8" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="424.1" y1="340.8" x2="424.1" y2="371.4" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="342.0" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="428.1" y1="361.5" x2="428.1" y2="386.4" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="366.4" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="432.0" y1="380.9" x2="432.0" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="385.7" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="435.9" y1="340.3" x2="435.9" y2="422.8" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="344.5" width="2.44" height="50.9" fill="var(--up)"/>
<line x1="439.9" y1="297.4" x2="439.9" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="324.3" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="443.8" y1="289.1" x2="443.8" y2="330.0" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="312.9" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="447.7" y1="275.7" x2="447.7" y2="304.4" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="287.2" width="2.44" height="13.1" fill="var(--down)"/>
<line x1="451.7" y1="274.8" x2="451.7" y2="312.5" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="275.2" width="2.44" height="27.5" fill="var(--up)"/>
<line x1="455.6" y1="257.4" x2="455.6" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="274.9" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="459.6" y1="283.0" x2="459.6" y2="343.1" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="286.1" width="2.44" height="52.3" fill="var(--down)"/>
<line x1="463.5" y1="299.7" x2="463.5" y2="347.1" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="323.8" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="467.4" y1="258.2" x2="467.4" y2="323.8" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="280.1" width="2.44" height="42.5" fill="var(--up)"/>
<line x1="471.4" y1="229.4" x2="471.4" y2="290.8" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="238.7" width="2.44" height="39.0" fill="var(--up)"/>
<line x1="475.3" y1="217.6" x2="475.3" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="230.5" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="479.2" y1="243.9" x2="479.2" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="256.6" width="2.44" height="29.4" fill="var(--down)"/>
<line x1="483.2" y1="261.1" x2="483.2" y2="311.2" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="293.9" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="487.1" y1="304.3" x2="487.1" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="308.8" width="2.44" height="4.5" fill="var(--up)"/>
<line x1="491.0" y1="296.0" x2="491.0" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="307.2" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="495.0" y1="280.0" x2="495.0" y2="309.2" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="281.0" width="2.44" height="25.4" fill="var(--up)"/>
<line x1="498.9" y1="272.4" x2="498.9" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="497.70" y="282.6" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="502.9" y1="266.0" x2="502.9" y2="312.4" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="284.2" width="2.44" height="21.5" fill="var(--down)"/>
<line x1="506.8" y1="247.7" x2="506.8" y2="299.7" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="254.9" width="2.44" height="42.8" fill="var(--up)"/>
<line x1="510.7" y1="233.7" x2="510.7" y2="272.4" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="254.6" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="514.7" y1="244.4" x2="514.7" y2="276.3" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="261.3" width="2.44" height="11.0" fill="var(--up)"/>
<line x1="518.6" y1="248.1" x2="518.6" y2="284.0" stroke="var(--up)" class="wick"/>
<rect x="517.38" y="263.4" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="522.5" y1="279.2" x2="522.5" y2="322.4" stroke="var(--down)" class="wick"/>
<rect x="521.32" y="285.1" width="2.44" height="29.4" fill="var(--down)"/>
<line x1="526.5" y1="272.4" x2="526.5" y2="361.1" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="281.7" width="2.44" height="65.6" fill="var(--up)"/>
<line x1="530.4" y1="262.0" x2="530.4" y2="303.0" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="266.5" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="534.3" y1="256.3" x2="534.3" y2="286.1" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="276.6" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="538.3" y1="283.2" x2="538.3" y2="303.2" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="285.4" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="542.2" y1="264.6" x2="542.2" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="270.7" width="2.44" height="31.1" fill="var(--up)"/>
<line x1="546.2" y1="250.6" x2="546.2" y2="273.4" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="259.9" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="550.1" y1="251.0" x2="550.1" y2="287.3" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="255.5" width="2.44" height="18.5" fill="var(--down)"/>
<line x1="554.0" y1="260.6" x2="554.0" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="264.0" width="2.44" height="21.8" fill="var(--down)"/>
<line x1="558.0" y1="290.4" x2="558.0" y2="323.8" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="298.0" width="2.44" height="22.1" fill="var(--down)"/>
<line x1="561.9" y1="301.3" x2="561.9" y2="340.1" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="307.6" width="2.44" height="23.3" fill="var(--down)"/>
<line x1="565.8" y1="318.3" x2="565.8" y2="339.9" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="330.3" width="2.44" height="5.8" fill="var(--down)"/>
<line x1="569.8" y1="305.9" x2="569.8" y2="352.5" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="307.9" width="2.44" height="42.1" fill="var(--down)"/>
<line x1="573.7" y1="317.2" x2="573.7" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="332.9" width="2.44" height="24.8" fill="var(--up)"/>
<line x1="577.7" y1="318.2" x2="577.7" y2="345.1" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="324.1" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="581.6" y1="304.7" x2="581.6" y2="335.3" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="320.6" width="2.44" height="8.4" fill="var(--up)"/>
<line x1="585.5" y1="304.9" x2="585.5" y2="323.9" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="311.7" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="589.5" y1="266.0" x2="589.5" y2="309.3" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="284.9" width="2.44" height="18.9" fill="var(--up)"/>
<line x1="593.4" y1="259.5" x2="593.4" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="284.0" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="597.3" y1="271.1" x2="597.3" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="284.9" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="601.3" y1="243.9" x2="601.3" y2="279.3" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="246.1" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="605.2" y1="234.0" x2="605.2" y2="269.2" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="238.5" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="609.1" y1="233.6" x2="609.1" y2="267.4" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="234.9" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="613.1" y1="213.4" x2="613.1" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="213.8" width="2.44" height="54.5" fill="var(--up)"/>
<line x1="617.0" y1="202.0" x2="617.0" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="210.0" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="621.0" y1="216.4" x2="621.0" y2="287.2" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="221.7" width="2.44" height="59.2" fill="var(--down)"/>
<line x1="624.9" y1="277.6" x2="624.9" y2="321.2" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="280.9" width="2.44" height="37.2" fill="var(--down)"/>
<line x1="628.8" y1="324.9" x2="628.8" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="330.9" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="632.8" y1="308.5" x2="632.8" y2="344.6" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="309.9" width="2.44" height="30.5" fill="var(--up)"/>
<line x1="636.7" y1="286.6" x2="636.7" y2="316.5" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="304.7" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="640.6" y1="276.3" x2="640.6" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="277.9" width="2.44" height="31.4" fill="var(--up)"/>
<line x1="644.6" y1="253.8" x2="644.6" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="269.5" width="2.44" height="12.7" fill="var(--down)"/>
<line x1="648.5" y1="263.9" x2="648.5" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="265.4" width="2.44" height="24.2" fill="var(--up)"/>
<line x1="652.4" y1="260.5" x2="652.4" y2="281.3" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="267.2" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="656.4" y1="242.6" x2="656.4" y2="262.8" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="247.3" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="660.3" y1="249.3" x2="660.3" y2="272.4" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="252.3" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="664.3" y1="247.2" x2="664.3" y2="284.8" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="259.4" width="2.44" height="22.4" fill="var(--down)"/>
<line x1="668.2" y1="251.0" x2="668.2" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="255.5" width="2.44" height="34.8" fill="var(--down)"/>
<line x1="672.1" y1="279.8" x2="672.1" y2="309.1" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="280.5" width="2.44" height="21.7" fill="var(--up)"/>
<line x1="676.1" y1="240.3" x2="676.1" y2="285.4" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="247.0" width="2.44" height="38.2" fill="var(--up)"/>
<line x1="680.0" y1="211.7" x2="680.0" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="245.2" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="683.9" y1="225.5" x2="683.9" y2="273.0" stroke="var(--up)" class="wick"/>
<rect x="682.72" y="250.7" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="687.9" y1="233.8" x2="687.9" y2="258.5" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="243.0" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="691.8" y1="251.8" x2="691.8" y2="293.7" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="253.8" width="2.44" height="32.8" fill="var(--down)"/>
<line x1="695.7" y1="250.9" x2="695.7" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="252.2" width="2.44" height="39.2" fill="var(--up)"/>
<line x1="699.7" y1="243.9" x2="699.7" y2="266.9" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="252.9" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="703.6" y1="262.9" x2="703.6" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="702.40" y="265.4" width="2.44" height="13.4" fill="var(--down)"/>
<line x1="707.6" y1="222.8" x2="707.6" y2="275.3" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="231.5" width="2.44" height="40.8" fill="var(--up)"/>
<line x1="711.5" y1="187.9" x2="711.5" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="207.8" width="2.44" height="32.0" fill="var(--up)"/>
<line x1="715.4" y1="189.4" x2="715.4" y2="222.6" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="190.6" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="719.4" y1="156.3" x2="719.4" y2="194.9" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="173.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="723.3" y1="109.1" x2="723.3" y2="182.7" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="116.2" width="2.44" height="55.9" fill="var(--up)"/>
<line x1="727.2" y1="73.9" x2="727.2" y2="125.5" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="78.5" width="2.44" height="36.6" fill="var(--up)"/>
<line x1="731.2" y1="88.2" x2="731.2" y2="125.7" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="89.0" width="2.44" height="32.4" fill="var(--down)"/>
<line x1="735.1" y1="141.0" x2="735.1" y2="195.3" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="143.8" width="2.44" height="27.4" fill="var(--down)"/>
<line x1="739.0" y1="181.3" x2="739.0" y2="224.5" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="193.2" width="2.44" height="24.8" fill="var(--down)"/>
<line x1="743.0" y1="219.6" x2="743.0" y2="285.8" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="222.5" width="2.44" height="49.0" fill="var(--down)"/>
<line x1="746.9" y1="249.1" x2="746.9" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="269.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="750.9" y1="252.3" x2="750.9" y2="289.8" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="253.2" width="2.44" height="34.6" fill="var(--down)"/>
<line x1="754.8" y1="280.2" x2="754.8" y2="392.8" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="306.0" width="2.44" height="63.9" fill="var(--down)"/>
<line x1="758.7" y1="363.8" x2="758.7" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="372.7" width="2.44" height="18.8" fill="var(--down)"/>
<line x1="762.7" y1="371.8" x2="762.7" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="374.2" width="2.44" height="25.3" fill="var(--up)"/>
<line x1="766.6" y1="342.7" x2="766.6" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="358.2" width="2.44" height="18.9" fill="var(--up)"/>
<line x1="770.5" y1="298.8" x2="770.5" y2="344.8" stroke="var(--down)" class="wick"/>
<rect x="769.32" y="305.2" width="2.44" height="30.8" fill="var(--down)"/>
<line x1="774.5" y1="283.1" x2="774.5" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="325.2" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="778.4" y1="322.0" x2="778.4" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="331.0" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="782.3" y1="315.7" x2="782.3" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="332.1" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="786.3" y1="308.8" x2="786.3" y2="353.0" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="312.8" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="790.2" y1="300.6" x2="790.2" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="305.3" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="794.2" y1="309.8" x2="794.2" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="314.9" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="798.1" y1="305.1" x2="798.1" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="321.0" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="802.0" y1="287.4" x2="802.0" y2="334.3" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="305.8" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="806.0" y1="312.1" x2="806.0" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="319.9" width="2.44" height="30.4" fill="var(--down)"/>
<line x1="809.9" y1="353.7" x2="809.9" y2="386.8" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="356.4" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="813.8" y1="370.1" x2="813.8" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="380.4" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="817.8" y1="348.6" x2="817.8" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="352.6" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="821.7" y1="345.3" x2="821.7" y2="368.4" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="357.8" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="825.7" y1="371.1" x2="825.7" y2="407.3" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="384.1" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="829.6" y1="358.6" x2="829.6" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="376.4" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="833.5" y1="341.3" x2="833.5" y2="399.3" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="365.2" width="2.44" height="25.1" fill="var(--down)"/>
<line x1="837.5" y1="391.7" x2="837.5" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="400.1" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="841.4" y1="403.4" x2="841.4" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="403.4" width="2.44" height="33.3" fill="var(--down)"/>
<line x1="845.3" y1="377.6" x2="845.3" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="379.7" width="2.44" height="52.1" fill="var(--up)"/>
<line x1="849.3" y1="371.6" x2="849.3" y2="401.4" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="382.7" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="853.2" y1="343.1" x2="853.2" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="346.2" width="2.44" height="42.3" fill="var(--down)"/>
<line x1="857.1" y1="348.4" x2="857.1" y2="387.4" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="364.2" width="2.44" height="12.4" fill="var(--down)"/>
<line x1="861.1" y1="414.9" x2="861.1" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="415.0" width="2.44" height="46.4" fill="var(--down)"/>
<line x1="865.0" y1="453.5" x2="865.0" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="454.5" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="869.0" y1="423.4" x2="869.0" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="433.0" width="2.44" height="16.9" fill="var(--up)"/>
<line x1="872.9" y1="426.7" x2="872.9" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="442.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="876.8" y1="430.6" x2="876.8" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="451.3" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="880.8" y1="392.2" x2="880.8" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="392.6" width="2.44" height="45.5" fill="var(--up)"/>
<line x1="884.7" y1="353.0" x2="884.7" y2="417.5" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="358.9" width="2.44" height="43.6" fill="var(--down)"/>
<line x1="888.6" y1="389.6" x2="888.6" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="407.0" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="892.6" y1="421.2" x2="892.6" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="424.9" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="896.5" y1="417.8" x2="896.5" y2="444.5" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="423.6" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="900.4" y1="432.8" x2="900.4" y2="453.4" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="433.8" width="2.44" height="11.7" fill="var(--up)"/>
<line x1="904.4" y1="411.4" x2="904.4" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="903.16" y="414.8" width="2.44" height="21.2" fill="var(--up)"/>
<line x1="908.3" y1="369.3" x2="908.3" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="379.9" width="2.44" height="28.4" fill="var(--up)"/>
<line x1="912.3" y1="304.0" x2="912.3" y2="349.7" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="339.8" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="916.2" y1="322.4" x2="916.2" y2="355.8" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="332.5" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="920.1" y1="360.5" x2="920.1" y2="383.9" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="372.6" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="924.1" y1="371.5" x2="924.1" y2="409.6" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="379.2" width="2.44" height="13.0" fill="var(--up)"/>
<line x1="928.0" y1="345.3" x2="928.0" y2="385.9" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="351.2" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="931.9" y1="381.4" x2="931.9" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="930.72" y="387.8" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="935.9" y1="368.5" x2="935.9" y2="414.4" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="368.5" width="2.44" height="31.7" fill="var(--down)"/>
<line x1="939.8" y1="349.1" x2="939.8" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="363.1" width="2.44" height="22.0" fill="var(--down)"/>
<line x1="943.7" y1="383.7" x2="943.7" y2="409.6" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="387.8" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="947.7" y1="377.1" x2="947.7" y2="403.2" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="377.4" width="2.44" height="21.7" fill="var(--up)"/>
<line x1="951.6" y1="372.9" x2="951.6" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="383.1" width="2.44" height="12.1" fill="var(--down)"/>
<line x1="955.6" y1="380.3" x2="955.6" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="384.1" width="2.44" height="25.7" fill="var(--up)"/>
<line x1="959.5" y1="356.7" x2="959.5" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="358.2" width="2.44" height="16.0" fill="var(--up)"/>
<line x1="963.4" y1="350.8" x2="963.4" y2="366.9" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="359.8" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="967.4" y1="369.0" x2="967.4" y2="384.4" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="373.0" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="971.3" y1="336.9" x2="971.3" y2="372.6" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="349.2" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="975.2" y1="322.6" x2="975.2" y2="370.6" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="361.6" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="979.2" y1="395.4" x2="979.2" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="977.95" y="418.0" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="983.1" y1="383.4" x2="983.1" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="388.0" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="987.0" y1="331.5" x2="987.0" y2="380.3" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="338.0" width="2.44" height="38.8" fill="var(--up)"/>
<line x1="991.0" y1="343.0" x2="991.0" y2="362.3" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="349.7" width="2.44" height="12.3" fill="var(--down)"/>
<line x1="994.9" y1="352.7" x2="994.9" y2="373.6" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="360.9" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="998.9" y1="385.7" x2="998.9" y2="418.6" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="386.9" width="2.44" height="28.7" fill="var(--down)"/>
<line x1="1002.8" y1="375.3" x2="1002.8" y2="410.4" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="392.8" width="2.44" height="13.8" fill="var(--up)"/>
<line x1="1006.7" y1="384.7" x2="1006.7" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="393.4" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="1010.7" y1="378.8" x2="1010.7" y2="412.9" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="388.8" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="1014.6" y1="406.7" x2="1014.6" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="407.5" width="2.44" height="21.1" fill="var(--down)"/>
<line x1="1018.5" y1="423.8" x2="1018.5" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="430.1" width="2.44" height="5.0" fill="var(--down)"/>
<line x1="1022.5" y1="429.6" x2="1022.5" y2="458.1" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="433.7" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="1026.4" y1="456.8" x2="1026.4" y2="475.9" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="462.6" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="1030.3" y1="469.3" x2="1030.3" y2="492.1" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="474.0" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="1034.3" y1="463.2" x2="1034.3" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="474.8" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="1038.2" y1="473.2" x2="1038.2" y2="487.2" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="477.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="1042.2" y1="442.4" x2="1042.2" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="448.9" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="1046.1" y1="453.1" x2="1046.1" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="453.1" width="2.44" height="32.9" fill="var(--down)"/>
<line x1="1050.0" y1="484.6" x2="1050.0" y2="492.7" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="486.6" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="60" y1="413.2" x2="1052" y2="413.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$936 R1</text>
<text x="1058" y="428.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="322.1" x2="1052" y2="322.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="325.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$979 R2</text>
<text x="1058" y="337.6" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="223.1" x2="1052" y2="223.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="226.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,026 R3</text>
<text x="1058" y="238.6" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="598.0" x2="1052" y2="598.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="592.0" font-size="11.5" fill="var(--support)" font-weight="600">$848 S1</text>
<text x="1058" y="604.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="492.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="484.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $898 (2026-09-16)</text>
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
| R3 | $1,026 | 5 | 2026-02-17·03-02·03-13·04-09·05-01 — **사상 최고가 부근에서 형성된 고점대**로, 2026년 상반기 내내 반복해서 막힌 자리다 |
| R2 | $979 | 7 | 2025-10-15·2026-01-26·06-16·06-29·07-17·07-28·08-19 — **1년 중 가장 많이 터치된 레벨**(7회)이며, 상반기에는 지지로 하반기에는 저항으로 역할이 바뀌었다 |
| R1 | $936 | 2 | 2025-11-05·12-03 — 터치 2회로 근거가 얕다. 현재가 바로 위 저항 |
| **현재가** | **$901.35** (2026-09-15 종가) | — | R1과 S1 사이. 52주 최고 대비 **−17.8%** |
| S1 | $848 | 2 | 2025-12-16·2026-01-02 — 52주 최저($844.06)와 거의 겹쳐, 이 구간이 1년 저점대다 |
| 참고선 | $1,096.50 | — | 52주 최고(2026년 상반기). R3보다 위의 단발 고점이라 클러스터를 이루지 못해 근시일 저항으로 보지 않는다 |
| 참고선 | $844.06 | — | 52주 최저. S1 클러스터에 거의 포함되므로 별도 지지로 세지 않는다 |

**레벨이 4개인 것은 유효 클러스터가 그만큼이기 때문이다.** 터치 2회 이상 기준을 충족하는 지지 클러스터가 S1 하나뿐이라 S2·S3를 만들지 않았다 — 최근 1년 주가가 $844~$1,097의 비교적 좁은 구간에 머물러 하단에 스윙 저점이 쌓이지 않았다. 더 아래 구조를 보려면 [주봉 문서](./10_technical_weekly.md)를 참고할 것.

**현재가는 1년 구간의 하단부에 있다.** 2026년 상반기에 $1,026(R3)까지 올라간 뒤 하락해, 지금은 R1($936)과 S1($848)의 중간보다 약간 위다. 다만 이 위치는 **아래쪽 지지 근거가 얕다** — S1의 터치가 2회뿐이다.

---


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-16~2026-09-16. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py COST --name "코스트코" --close-on 2026-09-15 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - ⚠️ **마지막 캔들은 2026-09-16 장중 미완성 봉이다.** 이 스크립트는 시계열 종료일을 고정하는 인자가 없어 항상 가장 최근 봉까지 그리며, `--close-on`은 시계열을 자르지 않고 대조용 종가 주석만 덧붙인다. 생성 시점이 미 증시 정규장 중이었으므로 차트 우측 끝 캔들의 종가는 확정값이 아니다 — **§2 현재가 행과 다른 문서의 기준 종가는 마지막 완료 거래일 2026-09-15 $901.35**를 쓴다. 마지막 봉은 스윙 탐지에 전후 5거래일이 필요해 레벨 계산에는 영향을 주지 않는다.
    - 원주가 기준이라 **배당은 반영되지 않았다**(기간 내 배당 4회). 총수익률로 보면 실제 성과는 이 차트보다 약간 높다.
    - 코스트코는 2000-01 이후 주식분할이 없어 가격 연속성을 깨는 이벤트가 없다.

---

*작성일: 2026-09-16*
