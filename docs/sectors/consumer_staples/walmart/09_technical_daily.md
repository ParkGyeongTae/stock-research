# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-15 종가 $108.09**는 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.
- ⚠️ **차트의 마지막 캔들은 미완성 봉이다.** 이 문서는 2026-09-16 미 동부시간 10:01(정규장 개장 중)에 생성돼, 차트 우측 끝에 그날의 **장중 봉**이 들어가 있다. **이 폴더의 모든 문서가 쓰는 기준 종가는 마지막 완료 거래일인 2026-09-15의 $108.09**이며, 아래 §2 현재가 행도 그 값이다(§4 참고).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-16 ~ 2026-09-16)

<style>
.wmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.wmt-chart svg { width:100%; height:auto; display:block; }
.wmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.wmt-chart .title { fill: var(--ink); font-weight:600; }
.wmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.wmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="wmt-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="월마트(WMT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">월마트 (WMT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-16 ~ 2026-09-16 · 마지막 종가 $107.74 (2026-09-16) · 단위 USD</text>
<line x1="60" y1="589.5" x2="1052" y2="589.5" class="grid"/>
<text x="52" y="593.5" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="516.4" x2="1052" y2="516.4" class="grid"/>
<text x="52" y="520.4" font-size="11" text-anchor="end" fill="var(--muted)">105</text>
<line x1="60" y1="443.3" x2="1052" y2="443.3" class="grid"/>
<text x="52" y="447.3" font-size="11" text-anchor="end" fill="var(--muted)">110</text>
<line x1="60" y1="370.2" x2="1052" y2="370.2" class="grid"/>
<text x="52" y="374.2" font-size="11" text-anchor="end" fill="var(--muted)">115</text>
<line x1="60" y1="297.2" x2="1052" y2="297.2" class="grid"/>
<text x="52" y="301.2" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="224.1" x2="1052" y2="224.1" class="grid"/>
<text x="52" y="228.1" font-size="11" text-anchor="end" fill="var(--muted)">125</text>
<line x1="60" y1="151.0" x2="1052" y2="151.0" class="grid"/>
<text x="52" y="155.0" font-size="11" text-anchor="end" fill="var(--muted)">130</text>
<line x1="60" y1="77.9" x2="1052" y2="77.9" class="grid"/>
<text x="52" y="81.9" font-size="11" text-anchor="end" fill="var(--muted)">135</text>
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
<line x1="62.0" y1="527.9" x2="62.0" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="533.2" width="2.44" height="6.3" fill="var(--down)"/>
<line x1="65.9" y1="500.2" x2="65.9" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="527.1" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="69.8" y1="521.6" x2="69.8" y2="558.5" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="534.2" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="73.8" y1="531.9" x2="73.8" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="533.8" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="77.7" y1="542.7" x2="77.7" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="548.2" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="81.7" y1="550.3" x2="81.7" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="552.6" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="85.6" y1="538.7" x2="85.6" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="545.0" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="89.5" y1="538.2" x2="89.5" y2="551.8" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="542.4" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="93.5" y1="538.5" x2="93.5" y2="553.4" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="543.3" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="97.4" y1="541.1" x2="97.4" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="544.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="101.3" y1="531.9" x2="101.3" y2="549.7" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="544.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="105.3" y1="547.7" x2="105.3" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="552.0" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="109.2" y1="558.2" x2="109.2" y2="591.4" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="564.6" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="113.1" y1="548.2" x2="113.1" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="559.2" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="117.1" y1="544.6" x2="117.1" y2="566.4" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="550.0" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="121.0" y1="542.0" x2="121.0" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="542.1" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="125.0" y1="541.8" x2="125.0" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="545.3" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="128.9" y1="539.0" x2="128.9" y2="584.1" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="543.7" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="132.8" y1="536.4" x2="132.8" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="559.5" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="136.8" y1="553.7" x2="136.8" y2="573.8" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="558.5" width="2.44" height="11.0" fill="var(--up)"/>
<line x1="140.7" y1="473.7" x2="140.7" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="484.1" width="2.44" height="46.2" fill="var(--up)"/>
<line x1="144.6" y1="449.7" x2="144.6" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="457.5" width="2.44" height="25.0" fill="var(--up)"/>
<line x1="148.6" y1="449.4" x2="148.6" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="455.0" width="2.44" height="39.9" fill="var(--down)"/>
<line x1="152.5" y1="469.6" x2="152.5" y2="498.6" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="476.5" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="156.4" y1="468.9" x2="156.4" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="474.7" width="2.44" height="11.7" fill="var(--down)"/>
<line x1="160.4" y1="480.1" x2="160.4" y2="499.1" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="482.3" width="2.44" height="16.2" fill="var(--down)"/>
<line x1="164.3" y1="475.9" x2="164.3" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="485.1" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="168.3" y1="478.8" x2="168.3" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="482.0" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="172.2" y1="484.7" x2="172.2" y2="508.9" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="486.1" width="2.44" height="13.2" fill="var(--down)"/>
<line x1="176.1" y1="496.5" x2="176.1" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="496.8" width="2.44" height="27.3" fill="var(--down)"/>
<line x1="180.1" y1="529.0" x2="180.1" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="530.1" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="184.0" y1="535.8" x2="184.0" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="546.9" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="187.9" y1="540.2" x2="187.9" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="556.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="191.9" y1="558.8" x2="191.9" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="564.6" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="195.8" y1="563.2" x2="195.8" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="566.2" width="2.44" height="11.3" fill="var(--up)"/>
<line x1="199.7" y1="551.2" x2="199.7" y2="568.1" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="556.3" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="203.7" y1="550.3" x2="203.7" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="564.0" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="207.6" y1="561.3" x2="207.6" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="564.9" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="211.6" y1="546.1" x2="211.6" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="551.6" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="215.5" y1="550.4" x2="215.5" y2="566.1" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="554.1" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="219.4" y1="534.8" x2="219.4" y2="555.6" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="539.2" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="223.4" y1="536.8" x2="223.4" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="539.2" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="227.3" y1="532.0" x2="227.3" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="537.0" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="231.2" y1="553.1" x2="231.2" y2="605.8" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="553.2" width="2.44" height="33.3" fill="var(--up)"/>
<line x1="235.2" y1="540.9" x2="235.2" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="233.95" y="546.3" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="239.1" y1="540.6" x2="239.1" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="545.9" width="2.44" height="23.2" fill="var(--down)"/>
<line x1="243.0" y1="564.5" x2="243.0" y2="594.1" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="566.4" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="247.0" y1="473.9" x2="247.0" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="245.76" y="485.5" width="2.44" height="46.3" fill="var(--up)"/>
<line x1="250.9" y1="470.3" x2="250.9" y2="520.5" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="472.8" width="2.44" height="38.9" fill="var(--down)"/>
<line x1="254.9" y1="497.8" x2="254.9" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="511.1" width="2.44" height="19.0" fill="var(--down)"/>
<line x1="258.8" y1="481.0" x2="258.8" y2="527.6" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="487.2" width="2.44" height="34.9" fill="var(--up)"/>
<line x1="262.7" y1="449.3" x2="262.7" y2="484.7" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="456.5" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="266.7" y1="433.1" x2="266.7" y2="457.9" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="435.9" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="270.6" y1="417.6" x2="270.6" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="420.9" width="2.44" height="14.9" fill="var(--up)"/>
<line x1="274.5" y1="404.6" x2="274.5" y2="431.8" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="408.1" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="278.5" y1="371.8" x2="278.5" y2="410.9" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="378.9" width="2.44" height="27.9" fill="var(--up)"/>
<line x1="282.4" y1="371.8" x2="282.4" y2="397.1" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="372.6" width="2.44" height="17.8" fill="var(--up)"/>
<line x1="286.3" y1="351.7" x2="286.3" y2="374.9" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="368.6" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="290.3" y1="370.4" x2="290.3" y2="409.7" stroke="var(--down)" class="wick"/>
<rect x="289.07" y="376.5" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="294.2" y1="359.7" x2="294.2" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="369.4" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="298.2" y1="352.3" x2="298.2" y2="399.6" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="365.1" width="2.44" height="31.7" fill="var(--down)"/>
<line x1="302.1" y1="357.5" x2="302.1" y2="401.7" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="362.6" width="2.44" height="34.8" fill="var(--up)"/>
<line x1="306.0" y1="341.7" x2="306.0" y2="369.9" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="345.4" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="310.0" y1="334.4" x2="310.0" y2="360.9" stroke="var(--down)" class="wick"/>
<rect x="308.75" y="342.0" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="313.9" y1="342.8" x2="313.9" y2="371.0" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="347.1" width="2.44" height="17.0" fill="var(--down)"/>
<line x1="317.8" y1="349.9" x2="317.8" y2="369.2" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="360.6" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="321.8" y1="348.6" x2="321.8" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="370.1" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="325.7" y1="366.1" x2="325.7" y2="391.7" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="368.2" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="329.7" y1="380.2" x2="329.7" y2="410.9" stroke="var(--down)" class="wick"/>
<rect x="328.43" y="384.7" width="2.44" height="20.6" fill="var(--down)"/>
<line x1="333.6" y1="409.0" x2="333.6" y2="433.1" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="414.2" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="337.5" y1="418.3" x2="337.5" y2="435.3" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="419.8" width="2.44" height="10.4" fill="var(--up)"/>
<line x1="341.5" y1="414.5" x2="341.5" y2="423.4" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="417.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="345.4" y1="402.7" x2="345.4" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="406.3" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="349.3" y1="404.0" x2="349.3" y2="416.4" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="415.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="353.3" y1="410.4" x2="353.3" y2="424.0" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="418.0" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="357.2" y1="402.5" x2="357.2" y2="426.9" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="403.0" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="361.1" y1="388.8" x2="361.1" y2="411.9" stroke="var(--down)" class="wick"/>
<rect x="359.92" y="402.1" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="365.1" y1="373.3" x2="365.1" y2="414.2" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="379.9" width="2.44" height="28.4" fill="var(--up)"/>
<line x1="369.0" y1="374.2" x2="369.0" y2="412.6" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="382.1" width="2.44" height="21.5" fill="var(--down)"/>
<line x1="373.0" y1="392.6" x2="373.0" y2="446.1" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="398.4" width="2.44" height="26.0" fill="var(--up)"/>
<line x1="376.9" y1="363.5" x2="376.9" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="377.1" width="2.44" height="33.2" fill="var(--up)"/>
<line x1="380.8" y1="314.1" x2="380.8" y2="349.6" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="326.8" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="384.8" y1="289.7" x2="384.8" y2="330.3" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="291.9" width="2.44" height="36.1" fill="var(--up)"/>
<line x1="388.7" y1="279.0" x2="388.7" y2="311.3" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="294.4" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="392.6" y1="284.4" x2="392.6" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="297.4" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="396.6" y1="288.4" x2="396.6" y2="342.5" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="301.5" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="400.5" y1="273.5" x2="400.5" y2="332.1" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="284.1" width="2.44" height="31.9" fill="var(--down)"/>
<line x1="404.4" y1="290.0" x2="404.4" y2="333.0" stroke="var(--up)" class="wick"/>
<rect x="403.22" y="306.5" width="2.44" height="18.7" fill="var(--up)"/>
<line x1="408.4" y1="304.2" x2="408.4" y2="331.5" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="307.5" width="2.44" height="21.3" fill="var(--down)"/>
<line x1="412.3" y1="317.5" x2="412.3" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="323.9" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="416.3" y1="314.0" x2="416.3" y2="335.3" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="329.2" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="420.2" y1="331.8" x2="420.2" y2="363.2" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="333.7" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="424.1" y1="334.3" x2="424.1" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="346.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="428.1" y1="331.4" x2="428.1" y2="354.6" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="335.0" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="432.0" y1="305.8" x2="432.0" y2="346.8" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="309.7" width="2.44" height="32.6" fill="var(--up)"/>
<line x1="435.9" y1="235.8" x2="435.9" y2="311.0" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="237.8" width="2.44" height="66.6" fill="var(--up)"/>
<line x1="439.9" y1="177.7" x2="439.9" y2="243.8" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="184.5" width="2.44" height="59.3" fill="var(--up)"/>
<line x1="443.8" y1="159.6" x2="443.8" y2="193.5" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="178.3" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="447.7" y1="156.8" x2="447.7" y2="201.3" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="171.8" width="2.44" height="24.0" fill="var(--down)"/>
<line x1="451.7" y1="126.2" x2="451.7" y2="194.1" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="133.8" width="2.44" height="56.9" fill="var(--up)"/>
<line x1="455.6" y1="124.8" x2="455.6" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="130.2" width="2.44" height="35.1" fill="var(--down)"/>
<line x1="459.6" y1="160.6" x2="459.6" y2="203.8" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="166.5" width="2.44" height="32.7" fill="var(--down)"/>
<line x1="463.5" y1="154.8" x2="463.5" y2="200.3" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="169.0" width="2.44" height="30.3" fill="var(--up)"/>
<line x1="467.4" y1="85.4" x2="467.4" y2="161.1" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="97.8" width="2.44" height="62.3" fill="var(--up)"/>
<line x1="471.4" y1="83.0" x2="471.4" y2="125.4" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="94.1" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="475.3" y1="82.5" x2="475.3" y2="177.9" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="105.5" width="2.44" height="62.3" fill="var(--down)"/>
<line x1="479.2" y1="167.5" x2="479.2" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="178.3" width="2.44" height="22.1" fill="var(--down)"/>
<line x1="483.2" y1="149.5" x2="483.2" y2="232.8" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="172.9" width="2.44" height="53.1" fill="var(--down)"/>
<line x1="487.1" y1="246.3" x2="487.1" y2="281.8" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="253.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="491.0" y1="197.8" x2="491.0" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="212.2" width="2.44" height="33.5" fill="var(--up)"/>
<line x1="495.0" y1="179.6" x2="495.0" y2="225.4" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="198.5" width="2.44" height="12.4" fill="var(--up)"/>
<line x1="498.9" y1="189.0" x2="498.9" y2="217.9" stroke="var(--down)" class="wick"/>
<rect x="497.70" y="200.5" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="502.9" y1="190.0" x2="502.9" y2="239.6" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="209.8" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="506.8" y1="171.5" x2="506.8" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="181.0" width="2.44" height="35.5" fill="var(--up)"/>
<line x1="510.7" y1="169.3" x2="510.7" y2="194.1" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="188.1" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="514.7" y1="174.8" x2="514.7" y2="214.3" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="181.5" width="2.44" height="20.3" fill="var(--up)"/>
<line x1="518.6" y1="177.7" x2="518.6" y2="206.0" stroke="var(--up)" class="wick"/>
<rect x="517.38" y="183.0" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="522.5" y1="214.1" x2="522.5" y2="273.0" stroke="var(--down)" class="wick"/>
<rect x="521.32" y="218.5" width="2.44" height="30.3" fill="var(--down)"/>
<line x1="526.5" y1="235.9" x2="526.5" y2="273.5" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="241.6" width="2.44" height="19.0" fill="var(--up)"/>
<line x1="530.4" y1="231.2" x2="530.4" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="233.7" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="534.3" y1="208.0" x2="534.3" y2="248.2" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="222.3" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="538.3" y1="216.9" x2="538.3" y2="252.6" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="219.5" width="2.44" height="26.6" fill="var(--down)"/>
<line x1="542.2" y1="218.4" x2="542.2" y2="263.8" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="219.3" width="2.44" height="44.3" fill="var(--up)"/>
<line x1="546.2" y1="199.4" x2="546.2" y2="224.5" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="201.9" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="550.1" y1="195.1" x2="550.1" y2="226.6" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="198.4" width="2.44" height="11.3" fill="var(--down)"/>
<line x1="554.0" y1="192.1" x2="554.0" y2="226.1" stroke="var(--down)" class="wick"/>
<rect x="552.81" y="200.0" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="558.0" y1="229.8" x2="558.0" y2="270.4" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="233.9" width="2.44" height="34.3" fill="var(--down)"/>
<line x1="561.9" y1="257.0" x2="561.9" y2="307.8" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="262.1" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="565.8" y1="278.2" x2="565.8" y2="326.1" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="287.9" width="2.44" height="23.5" fill="var(--down)"/>
<line x1="569.8" y1="280.6" x2="569.8" y2="311.0" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="286.6" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="573.7" y1="237.1" x2="573.7" y2="290.0" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="267.2" width="2.44" height="20.8" fill="var(--up)"/>
<line x1="577.7" y1="246.1" x2="577.7" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="252.4" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="581.6" y1="241.6" x2="581.6" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="244.4" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="585.5" y1="234.7" x2="585.5" y2="270.6" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="254.9" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="589.5" y1="220.3" x2="589.5" y2="251.3" stroke="var(--down)" class="wick"/>
<rect x="588.24" y="242.9" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="593.4" y1="224.1" x2="593.4" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="592.18" y="234.6" width="2.44" height="12.4" fill="var(--up)"/>
<line x1="597.3" y1="220.7" x2="597.3" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="227.9" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="601.3" y1="210.9" x2="601.3" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="212.5" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="605.2" y1="195.1" x2="605.2" y2="218.7" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="197.9" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="609.1" y1="204.2" x2="609.1" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="206.7" width="2.44" height="54.1" fill="var(--down)"/>
<line x1="613.1" y1="190.5" x2="613.1" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="191.0" width="2.44" height="72.8" fill="var(--up)"/>
<line x1="617.0" y1="155.5" x2="617.0" y2="197.5" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="163.7" width="2.44" height="29.8" fill="var(--up)"/>
<line x1="621.0" y1="166.6" x2="621.0" y2="206.2" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="169.7" width="2.44" height="28.5" fill="var(--down)"/>
<line x1="624.9" y1="205.1" x2="624.9" y2="239.4" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="205.2" width="2.44" height="25.1" fill="var(--down)"/>
<line x1="628.8" y1="221.2" x2="628.8" y2="259.9" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="223.3" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="632.8" y1="223.1" x2="632.8" y2="250.7" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="227.6" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="636.7" y1="210.3" x2="636.7" y2="239.1" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="226.7" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="640.6" y1="186.5" x2="640.6" y2="247.9" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="187.5" width="2.44" height="42.8" fill="var(--up)"/>
<line x1="644.6" y1="158.7" x2="644.6" y2="190.2" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="181.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="648.5" y1="154.4" x2="648.5" y2="187.8" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="156.8" width="2.44" height="25.9" fill="var(--up)"/>
<line x1="652.4" y1="144.4" x2="652.4" y2="168.0" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="151.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="656.4" y1="115.0" x2="656.4" y2="143.8" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="121.3" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="660.3" y1="120.0" x2="660.3" y2="161.5" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="122.6" width="2.44" height="29.5" fill="var(--down)"/>
<line x1="664.3" y1="153.8" x2="664.3" y2="189.0" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="156.6" width="2.44" height="29.7" fill="var(--down)"/>
<line x1="668.2" y1="154.4" x2="668.2" y2="198.1" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="160.6" width="2.44" height="25.6" fill="var(--down)"/>
<line x1="672.1" y1="179.1" x2="672.1" y2="210.8" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="180.1" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="676.1" y1="115.5" x2="676.1" y2="181.0" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="122.8" width="2.44" height="57.1" fill="var(--up)"/>
<line x1="680.0" y1="101.7" x2="680.0" y2="136.7" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="122.9" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="683.9" y1="125.4" x2="683.9" y2="155.7" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="145.0" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="687.9" y1="125.7" x2="687.9" y2="146.6" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="139.5" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="691.8" y1="134.2" x2="691.8" y2="157.9" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="138.4" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="695.7" y1="142.2" x2="695.7" y2="170.4" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="148.1" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="699.7" y1="130.4" x2="699.7" y2="147.3" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="144.7" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="703.6" y1="142.2" x2="703.6" y2="203.9" stroke="var(--down)" class="wick"/>
<rect x="702.40" y="148.4" width="2.44" height="37.9" fill="var(--down)"/>
<line x1="707.6" y1="134.6" x2="707.6" y2="184.3" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="145.9" width="2.44" height="33.2" fill="var(--up)"/>
<line x1="711.5" y1="114.0" x2="711.5" y2="169.0" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="129.5" width="2.44" height="33.3" fill="var(--up)"/>
<line x1="715.4" y1="110.4" x2="715.4" y2="138.4" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="115.0" width="2.44" height="16.1" fill="var(--up)"/>
<line x1="719.4" y1="93.3" x2="719.4" y2="139.5" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="97.1" width="2.44" height="32.7" fill="var(--down)"/>
<line x1="723.3" y1="100.3" x2="723.3" y2="134.5" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="102.2" width="2.44" height="26.6" fill="var(--up)"/>
<line x1="727.2" y1="75.6" x2="727.2" y2="120.9" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="89.6" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="731.2" y1="97.7" x2="731.2" y2="146.2" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="108.5" width="2.44" height="30.1" fill="var(--down)"/>
<line x1="735.1" y1="212.4" x2="735.1" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="232.7" width="2.44" height="44.9" fill="var(--down)"/>
<line x1="739.0" y1="268.7" x2="739.0" y2="313.1" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="277.6" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="743.0" y1="281.8" x2="743.0" y2="327.6" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="287.1" width="2.44" height="31.0" fill="var(--down)"/>
<line x1="746.9" y1="305.5" x2="746.9" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="318.5" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="750.9" y1="309.3" x2="750.9" y2="336.2" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="312.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="754.8" y1="310.6" x2="754.8" y2="374.5" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="324.8" width="2.44" height="34.5" fill="var(--down)"/>
<line x1="758.7" y1="355.9" x2="758.7" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="374.2" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="762.7" y1="376.5" x2="762.7" y2="403.4" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="386.7" width="2.44" height="11.8" fill="var(--down)"/>
<line x1="766.6" y1="336.8" x2="766.6" y2="400.0" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="342.6" width="2.44" height="55.4" fill="var(--up)"/>
<line x1="770.5" y1="298.0" x2="770.5" y2="336.8" stroke="var(--down)" class="wick"/>
<rect x="769.32" y="298.6" width="2.44" height="31.6" fill="var(--down)"/>
<line x1="774.5" y1="284.1" x2="774.5" y2="324.9" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="313.5" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="778.4" y1="294.5" x2="778.4" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="299.6" width="2.44" height="23.1" fill="var(--up)"/>
<line x1="782.3" y1="289.8" x2="782.3" y2="326.4" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="291.6" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="786.3" y1="285.2" x2="786.3" y2="333.3" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="288.5" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="790.2" y1="270.0" x2="790.2" y2="305.0" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="288.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="794.2" y1="273.6" x2="794.2" y2="304.0" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="282.0" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="798.1" y1="275.4" x2="798.1" y2="317.9" stroke="var(--up)" class="wick"/>
<rect x="796.87" y="285.2" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="802.0" y1="254.2" x2="802.0" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="280.5" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="806.0" y1="282.4" x2="806.0" y2="334.4" stroke="var(--down)" class="wick"/>
<rect x="804.75" y="303.3" width="2.44" height="21.2" fill="var(--down)"/>
<line x1="809.9" y1="319.4" x2="809.9" y2="343.9" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="323.5" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="813.8" y1="320.5" x2="813.8" y2="341.7" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="338.4" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="817.8" y1="293.5" x2="817.8" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="301.4" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="821.7" y1="291.3" x2="821.7" y2="312.8" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="303.6" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="825.7" y1="317.9" x2="825.7" y2="364.7" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="334.1" width="2.44" height="24.7" fill="var(--down)"/>
<line x1="829.6" y1="328.1" x2="829.6" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="336.8" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="833.5" y1="343.9" x2="833.5" y2="381.9" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="348.7" width="2.44" height="27.3" fill="var(--down)"/>
<line x1="837.5" y1="375.9" x2="837.5" y2="400.5" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="385.3" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="841.4" y1="432.9" x2="841.4" y2="483.5" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="441.4" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="845.3" y1="407.5" x2="845.3" y2="455.6" stroke="var(--up)" class="wick"/>
<rect x="844.11" y="416.4" width="2.44" height="36.7" fill="var(--up)"/>
<line x1="849.3" y1="408.7" x2="849.3" y2="452.5" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="422.8" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="853.2" y1="392.2" x2="853.2" y2="424.3" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="399.9" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="857.1" y1="386.9" x2="857.1" y2="416.9" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="397.3" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="861.1" y1="403.0" x2="861.1" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="411.0" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="865.0" y1="382.5" x2="865.0" y2="415.1" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="386.3" width="2.44" height="28.5" fill="var(--up)"/>
<line x1="869.0" y1="362.3" x2="869.0" y2="384.7" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="373.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="872.9" y1="357.4" x2="872.9" y2="392.2" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="369.1" width="2.44" height="20.2" fill="var(--down)"/>
<line x1="876.8" y1="374.2" x2="876.8" y2="413.1" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="395.8" width="2.44" height="10.5" fill="var(--down)"/>
<line x1="880.8" y1="361.6" x2="880.8" y2="391.3" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="371.0" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="884.7" y1="325.1" x2="884.7" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="341.6" width="2.44" height="39.8" fill="var(--down)"/>
<line x1="888.6" y1="379.0" x2="888.6" y2="412.0" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="385.4" width="2.44" height="25.7" fill="var(--down)"/>
<line x1="892.6" y1="417.0" x2="892.6" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="891.35" y="421.2" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="896.5" y1="443.3" x2="896.5" y2="462.0" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="450.2" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="900.4" y1="464.4" x2="900.4" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="466.7" width="2.44" height="13.0" fill="var(--up)"/>
<line x1="904.4" y1="449.2" x2="904.4" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="903.16" y="451.1" width="2.44" height="19.7" fill="var(--up)"/>
<line x1="908.3" y1="406.6" x2="908.3" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="417.9" width="2.44" height="26.6" fill="var(--up)"/>
<line x1="912.3" y1="355.2" x2="912.3" y2="401.8" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="385.4" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="916.2" y1="374.8" x2="916.2" y2="407.5" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="381.6" width="2.44" height="14.5" fill="var(--up)"/>
<line x1="920.1" y1="399.0" x2="920.1" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="419.8" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="924.1" y1="415.4" x2="924.1" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="425.8" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="928.0" y1="395.2" x2="928.0" y2="441.0" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="398.0" width="2.44" height="34.9" fill="var(--down)"/>
<line x1="931.9" y1="418.8" x2="931.9" y2="464.4" stroke="var(--up)" class="wick"/>
<rect x="930.72" y="420.7" width="2.44" height="37.1" fill="var(--up)"/>
<line x1="935.9" y1="397.1" x2="935.9" y2="423.4" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="407.5" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="939.8" y1="376.7" x2="939.8" y2="428.1" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="383.8" width="2.44" height="29.2" fill="var(--down)"/>
<line x1="943.7" y1="409.8" x2="943.7" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="416.3" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="947.7" y1="403.8" x2="947.7" y2="432.2" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="404.4" width="2.44" height="23.1" fill="var(--up)"/>
<line x1="951.6" y1="394.5" x2="951.6" y2="411.3" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="395.7" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="955.6" y1="354.9" x2="955.6" y2="410.0" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="355.5" width="2.44" height="53.2" fill="var(--up)"/>
<line x1="959.5" y1="350.9" x2="959.5" y2="373.0" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="353.1" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="963.4" y1="349.0" x2="963.4" y2="375.5" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="360.6" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="967.4" y1="367.6" x2="967.4" y2="386.0" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="380.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="971.3" y1="351.1" x2="971.3" y2="377.8" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="351.2" width="2.44" height="16.1" fill="var(--down)"/>
<line x1="975.2" y1="342.9" x2="975.2" y2="385.0" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="367.5" width="2.44" height="13.0" fill="var(--down)"/>
<line x1="979.2" y1="487.2" x2="979.2" y2="547.8" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="496.2" width="2.44" height="37.1" fill="var(--down)"/>
<line x1="983.1" y1="526.9" x2="983.1" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="535.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="987.0" y1="493.0" x2="987.0" y2="531.0" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="494.6" width="2.44" height="34.3" fill="var(--up)"/>
<line x1="991.0" y1="500.7" x2="991.0" y2="525.2" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="507.9" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="994.9" y1="500.5" x2="994.9" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="508.9" width="2.44" height="17.1" fill="var(--down)"/>
<line x1="998.9" y1="534.7" x2="998.9" y2="556.3" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="536.7" width="2.44" height="14.3" fill="var(--down)"/>
<line x1="1002.8" y1="539.8" x2="1002.8" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="544.3" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="1006.7" y1="516.5" x2="1006.7" y2="548.0" stroke="var(--up)" class="wick"/>
<rect x="1005.51" y="518.3" width="2.44" height="26.2" fill="var(--up)"/>
<line x1="1010.7" y1="492.4" x2="1010.7" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="502.9" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="1014.6" y1="490.4" x2="1014.6" y2="509.7" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="500.5" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="1018.5" y1="452.8" x2="1018.5" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="466.4" width="2.44" height="29.2" fill="var(--up)"/>
<line x1="1022.5" y1="454.6" x2="1022.5" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="469.6" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="1026.4" y1="488.6" x2="1026.4" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="490.4" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="1030.3" y1="499.6" x2="1030.3" y2="514.0" stroke="var(--up)" class="wick"/>
<rect x="1029.13" y="504.3" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="1034.3" y1="484.8" x2="1034.3" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="499.3" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="1038.2" y1="484.1" x2="1038.2" y2="505.9" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="485.0" width="2.44" height="13.9" fill="var(--up)"/>
<line x1="1042.2" y1="447.1" x2="1042.2" y2="472.5" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="456.8" width="2.44" height="14.6" fill="var(--up)"/>
<line x1="1046.1" y1="454.4" x2="1046.1" y2="474.6" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="463.6" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="1050.0" y1="466.1" x2="1050.0" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="467.9" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="60" y1="451.1" x2="1052" y2="451.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="454.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$109 R1</text>
<text x="1058" y="466.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="339.4" x2="1052" y2="339.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="342.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$117 R2</text>
<text x="1058" y="354.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="263.8" x2="1052" y2="263.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="267.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$122 R3</text>
<text x="1058" y="279.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="582.9" x2="1052" y2="582.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="576.9" font-size="11.5" fill="var(--support)" font-weight="600">$100 S1</text>
<text x="1058" y="588.9" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="476.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="468.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $108 (2026-09-16)</text>
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
| R3 | $122 | 2 | 2026-01-20·06-16 — 사상 최고가($135.16)로 가는 길목의 고점대 |
| R2 | $117 | 4 | 2025-12-15·2026-07-17·07-28·**08-19** — 1년 중 가장 여러 번 막힌 자리이고, **마지막 터치 다음 날이 8월 20일 갭다운**이다(아래 3절) |
| R1 | $109 | 2 | 2025-10-16·**2026-09-03** — 갭다운 이후 되돌림이 멈춘 자리. 현재가 바로 위 |
| **현재가** | **$108.09** (2026-09-15 종가) | — | R1 바로 아래. 52주 최고 $135.16 대비 **−20.0%** |
| S1 | $100 | 5 | 2025-09-23·10-02·11-06·11-14·**2026-08-21** — **1년 중 가장 강한 레벨**(터치 5회)이며, 2025년 가을의 지지대가 갭다운 직후 다시 지지로 작동했다 |
| 참고선 | $135.16 | — | 52주 최고(2026-05-18). R3 위의 단발 고점이라 클러스터를 이루지 못해 근시일 저항으로 보지 않는다 |
| 참고선 | $98.88 | — | 52주 최저. S1 클러스터에 인접해 별도 지지로 세지 않는다 |

**레벨이 4개인 것은 유효 클러스터가 그만큼이기 때문이다.** 터치 2회 이상 기준을 충족하는 지지 클러스터가 S1 하나뿐이라 S2·S3를 만들지 않았다.

**현재가는 $100(S1)과 $109(R1) 사이의 좁은 구간에 있다.** 8월 20일 갭다운으로 $103.84까지 밀린 뒤 $108.09로 되돌렸지만 R1을 넘지 못했고, 아래로는 터치 5회의 $100이 받치는 구조다. **이 두 레벨 사이 9% 구간이 현재의 거래 레인지**로 읽힌다.

## 3. 관측된 특이 구간 — 2026-08-20 Q2 FY27 실적 발표 갭다운

- 2026-08-20 Q2 FY27 실적 발표 직후의 하락이다. 조정 EPS·매출은 컨센서스를 상회하고 연간 가이던스도 상향했으나, **Q3 가이던스(순매출 +3.0~3.75%, 조정 영업이익 +2.0~4.0%)가 시장 기대에 크게 못 미친 것**이 계기였다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−9.15%** ($114.30 → $103.84)로, 2022년 이후 최대 일간 낙폭이다. 이후 8월 21일 저가가 S1($100) 클러스터에 닿았다.
- **이 사건이 위 §2 표의 구조를 만들었다.** R2($117)의 네 번째이자 마지막 터치가 갭다운 전날인 8월 19일이고, S1($100)의 다섯 번째 터치가 갭다운 이틀 뒤인 8월 21일이다 — 즉 **1년 내내 형성돼 있던 상단 저항과 하단 지지를 이 한 번의 발표가 이틀 만에 오갔다.** 갭 구간($104~$114)에는 스윙 포인트가 쌓이지 않아 클러스터가 형성되지 않았고, 그래서 현재가 위아래로 레벨이 성기다.

---


## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-16~2026-09-16. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py WMT --name "월마트" --close-on 2026-09-15 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - ⚠️ **마지막 캔들은 2026-09-16 장중 미완성 봉이다.** 이 스크립트는 시계열 종료일을 고정하는 인자가 없어 항상 가장 최근 봉까지 그리며, `--close-on`은 시계열을 자르지 않고 대조용 종가 주석만 덧붙인다. 생성 시점이 미 증시 정규장 중이었으므로 차트 우측 끝 캔들의 종가는 확정값이 아니다 — **§2 현재가 행과 다른 문서의 기준 종가는 마지막 완료 거래일 2026-09-15 $108.09**를 쓴다. 마지막 봉은 스윙 탐지에 전후 5거래일이 필요해 레벨 계산에는 영향을 주지 않는다.
    - **3절의 갭 구간($104~$114)이 레벨 해석을 왜곡한다.** 하루 만에 통과한 가격대라 스윙 포인트가 쌓이지 않았고, 그 결과 현재가 주변의 레벨이 실제 거래 밀도보다 성기게 잡힌다 — R1($109)의 터치가 2회뿐인 것이 그 영향이다.
    - 원주가 기준이라 **배당은 반영되지 않았다**(기간 내 배당 4회).
    - 최근 1년 구간에는 주식분할이 없다(직전 분할은 2024-02-26 3:1로, 주봉 문서의 구간에 포함된다).

---

*작성일: 2026-09-16*
