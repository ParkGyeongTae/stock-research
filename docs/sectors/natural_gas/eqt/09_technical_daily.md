# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 2026-08-20 종가 $53.89는 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치(둘 다 stockanalysis.com 종가 기준). 차트 우측 상단 "현재가" 라벨은 스크립트 실행 시점(2026-08-21 장중)의 값이라 종가 기준값과 소폭(약 $0.07) 차이가 있을 수 있음 — 장중 스냅샷과 종가를 혼동하지 말 것.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-21 ~ 2026-08-21)

<div class="eqt-chart">
<style>
.eqt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eqt-chart svg { width:100%; height:auto; display:block; }
.eqt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eqt-chart .title { fill: var(--ink); font-weight:600; }
.eqt-chart .grid { stroke: var(--grid); stroke-width:1; }
.eqt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="EQT Corporation(EQT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">EQT Corporation (EQT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-21 ~ 2026-08-21 · 마지막 종가 $53.82 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="548.3" x2="1052" y2="548.3" class="grid"/>
<text x="52" y="552.3" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="418.7" x2="1052" y2="418.7" class="grid"/>
<text x="52" y="422.7" font-size="11" text-anchor="end" fill="var(--muted)">55</text>
<line x1="60" y1="289.2" x2="1052" y2="289.2" class="grid"/>
<text x="52" y="293.2" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="159.6" x2="1052" y2="159.6" class="grid"/>
<text x="52" y="163.6" font-size="11" text-anchor="end" fill="var(--muted)">65</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="89.5" y1="626.0" x2="89.5" y2="631.0" class="axis"/>
<text x="89.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="172.2" y1="626.0" x2="172.2" y2="631.0" class="axis"/>
<text x="172.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="262.7" y1="626.0" x2="262.7" y2="631.0" class="axis"/>
<text x="262.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="337.5" y1="626.0" x2="337.5" y2="631.0" class="axis"/>
<text x="337.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="424.1" y1="626.0" x2="424.1" y2="631.0" class="axis"/>
<text x="424.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="502.9" y1="626.0" x2="502.9" y2="631.0" class="axis"/>
<text x="502.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="577.7" y1="626.0" x2="577.7" y2="631.0" class="axis"/>
<text x="577.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="664.3" y1="626.0" x2="664.3" y2="631.0" class="axis"/>
<text x="664.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="746.9" y1="626.0" x2="746.9" y2="631.0" class="axis"/>
<text x="746.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="825.7" y1="626.0" x2="825.7" y2="631.0" class="axis"/>
<text x="825.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="908.3" y1="626.0" x2="908.3" y2="631.0" class="axis"/>
<text x="908.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="994.9" y1="626.0" x2="994.9" y2="631.0" class="axis"/>
<text x="994.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="963.4" y1="56.0" x2="963.4" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="969.4" y="68.0" font-size="10.5" fill="var(--down)">2026-07-22 Q2 2026 실적 발표 후 급등</text>
<line x1="62.0" y1="491.5" x2="62.0" y2="520.8" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="495.2" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="65.9" y1="474.7" x2="65.9" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="495.2" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="69.8" y1="482.5" x2="69.8" y2="508.9" stroke="var(--up)" class="wick"/>
<rect x="68.62" y="501.4" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="73.8" y1="473.4" x2="73.8" y2="527.5" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="478.1" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="77.7" y1="466.1" x2="77.7" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="76.49" y="477.0" width="2.44" height="36.3" fill="var(--down)"/>
<line x1="81.7" y1="482.5" x2="81.7" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="487.1" width="2.44" height="26.2" fill="var(--up)"/>
<line x1="85.6" y1="484.3" x2="85.6" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="491.0" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="89.5" y1="475.5" x2="89.5" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="486.6" width="2.44" height="30.6" fill="var(--up)"/>
<line x1="93.5" y1="470.5" x2="93.5" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="485.6" width="2.44" height="22.5" fill="var(--down)"/>
<line x1="97.4" y1="495.7" x2="97.4" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="501.6" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="101.3" y1="497.0" x2="101.3" y2="535.1" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="506.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="105.3" y1="481.9" x2="105.3" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="486.4" width="2.44" height="42.2" fill="var(--down)"/>
<line x1="109.2" y1="512.0" x2="109.2" y2="547.2" stroke="var(--down)" class="wick"/>
<rect x="107.99" y="527.5" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="113.1" y1="496.5" x2="113.1" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="518.0" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="117.1" y1="516.7" x2="117.1" y2="536.4" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="523.4" width="2.44" height="5.4" fill="var(--up)"/>
<line x1="121.0" y1="496.2" x2="121.0" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="511.7" width="2.44" height="12.2" fill="var(--down)"/>
<line x1="125.0" y1="520.8" x2="125.0" y2="550.3" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="527.3" width="2.44" height="21.5" fill="var(--down)"/>
<line x1="128.9" y1="535.3" x2="128.9" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="543.1" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="132.8" y1="522.6" x2="132.8" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="548.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="136.8" y1="542.8" x2="136.8" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="544.6" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="140.7" y1="560.7" x2="140.7" y2="586.9" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="566.4" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="144.6" y1="541.0" x2="144.6" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="549.0" width="2.44" height="24.6" fill="var(--up)"/>
<line x1="148.6" y1="512.8" x2="148.6" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="523.7" width="2.44" height="21.5" fill="var(--up)"/>
<line x1="152.5" y1="456.0" x2="152.5" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="468.5" width="2.44" height="48.7" fill="var(--up)"/>
<line x1="156.4" y1="419.8" x2="156.4" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="446.4" width="2.44" height="26.4" fill="var(--up)"/>
<line x1="160.4" y1="420.0" x2="160.4" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="443.1" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="164.3" y1="419.5" x2="164.3" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="432.7" width="2.44" height="13.0" fill="var(--up)"/>
<line x1="168.3" y1="410.7" x2="168.3" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="433.5" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="172.2" y1="364.8" x2="172.2" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="388.7" width="2.44" height="49.5" fill="var(--up)"/>
<line x1="176.1" y1="357.8" x2="176.1" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="393.9" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="180.1" y1="380.4" x2="180.1" y2="417.7" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="392.0" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="184.0" y1="359.1" x2="184.0" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="362.0" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="187.9" y1="352.7" x2="187.9" y2="384.8" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="362.8" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="191.9" y1="362.8" x2="191.9" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="362.8" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="195.8" y1="364.3" x2="195.8" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="364.3" width="2.44" height="56.5" fill="var(--down)"/>
<line x1="199.7" y1="409.4" x2="199.7" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="426.5" width="2.44" height="40.9" fill="var(--down)"/>
<line x1="203.7" y1="448.8" x2="203.7" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="202.46" y="453.4" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="207.6" y1="449.0" x2="207.6" y2="505.3" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="463.0" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="211.6" y1="405.0" x2="211.6" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="407.3" width="2.44" height="38.9" fill="var(--up)"/>
<line x1="215.5" y1="386.9" x2="215.5" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="402.4" width="2.44" height="61.9" fill="var(--down)"/>
<line x1="219.4" y1="430.9" x2="219.4" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="442.6" width="2.44" height="15.3" fill="var(--up)"/>
<line x1="223.4" y1="365.6" x2="223.4" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="381.2" width="2.44" height="28.5" fill="var(--up)"/>
<line x1="227.3" y1="370.0" x2="227.3" y2="403.7" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="396.4" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="231.2" y1="367.4" x2="231.2" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="411.0" width="2.44" height="46.9" fill="var(--down)"/>
<line x1="235.2" y1="425.5" x2="235.2" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="435.6" width="2.44" height="20.5" fill="var(--down)"/>
<line x1="239.1" y1="444.4" x2="239.1" y2="472.9" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="451.1" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="243.0" y1="435.6" x2="243.0" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="448.8" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="247.0" y1="457.3" x2="247.0" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="457.3" width="2.44" height="34.5" fill="var(--down)"/>
<line x1="250.9" y1="460.2" x2="250.9" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="484.3" width="2.44" height="17.4" fill="var(--down)"/>
<line x1="254.9" y1="463.3" x2="254.9" y2="509.2" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="484.8" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="258.8" y1="447.5" x2="258.8" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="455.5" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="262.7" y1="395.2" x2="262.7" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="396.4" width="2.44" height="54.9" fill="var(--up)"/>
<line x1="266.7" y1="374.2" x2="266.7" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="396.7" width="2.44" height="21.2" fill="var(--up)"/>
<line x1="270.6" y1="364.3" x2="270.6" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="393.1" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="274.5" y1="342.6" x2="274.5" y2="404.5" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="372.3" width="2.44" height="13.2" fill="var(--down)"/>
<line x1="278.5" y1="341.3" x2="278.5" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="341.8" width="2.44" height="46.6" fill="var(--up)"/>
<line x1="282.4" y1="307.6" x2="282.4" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="316.6" width="2.44" height="11.7" fill="var(--up)"/>
<line x1="286.3" y1="261.7" x2="286.3" y2="308.9" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="271.3" width="2.44" height="33.4" fill="var(--up)"/>
<line x1="290.3" y1="258.9" x2="290.3" y2="288.4" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="267.4" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="294.2" y1="256.5" x2="294.2" y2="285.3" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="267.2" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="298.2" y1="276.2" x2="298.2" y2="343.6" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="291.8" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="302.1" y1="272.1" x2="302.1" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="299.8" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="306.0" y1="314.8" x2="306.0" y2="349.3" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="321.6" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="310.0" y1="310.2" x2="310.0" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="317.9" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="313.9" y1="276.0" x2="313.9" y2="385.6" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="307.6" width="2.44" height="76.2" fill="var(--down)"/>
<line x1="317.8" y1="357.3" x2="317.8" y2="415.4" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="366.1" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="321.8" y1="348.5" x2="321.8" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="352.9" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="325.7" y1="344.1" x2="325.7" y2="390.0" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="369.5" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="329.7" y1="306.3" x2="329.7" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="315.1" width="2.44" height="42.2" fill="var(--up)"/>
<line x1="333.6" y1="258.9" x2="333.6" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="266.9" width="2.44" height="37.1" fill="var(--up)"/>
<line x1="337.5" y1="257.8" x2="337.5" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="272.1" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="341.5" y1="277.0" x2="341.5" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="277.0" width="2.44" height="48.5" fill="var(--down)"/>
<line x1="345.4" y1="249.8" x2="345.4" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="258.9" width="2.44" height="53.9" fill="var(--up)"/>
<line x1="349.3" y1="237.4" x2="349.3" y2="309.4" stroke="var(--down)" class="wick"/>
<rect x="348.11" y="261.2" width="2.44" height="26.2" fill="var(--down)"/>
<line x1="353.3" y1="231.4" x2="353.3" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="269.8" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="357.2" y1="276.5" x2="357.2" y2="330.4" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="278.3" width="2.44" height="45.6" fill="var(--down)"/>
<line x1="361.1" y1="310.4" x2="361.1" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="359.92" y="322.1" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="365.1" y1="320.5" x2="365.1" y2="367.2" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="321.8" width="2.44" height="38.6" fill="var(--down)"/>
<line x1="369.0" y1="370.3" x2="369.0" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="370.3" width="2.44" height="20.7" fill="var(--down)"/>
<line x1="373.0" y1="383.0" x2="373.0" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="385.3" width="2.44" height="18.7" fill="var(--down)"/>
<line x1="376.9" y1="403.7" x2="376.9" y2="445.7" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="404.0" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="380.8" y1="427.5" x2="380.8" y2="477.3" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="427.5" width="2.44" height="34.7" fill="var(--down)"/>
<line x1="384.8" y1="431.7" x2="384.8" y2="463.5" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="435.3" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="388.7" y1="408.1" x2="388.7" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="438.9" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="392.6" y1="429.3" x2="392.6" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="448.0" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="396.6" y1="435.1" x2="396.6" y2="467.2" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="448.8" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="400.5" y1="425.5" x2="400.5" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="431.2" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="404.4" y1="430.6" x2="404.4" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="443.9" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="408.4" y1="434.0" x2="408.4" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="437.4" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="412.3" y1="425.7" x2="412.3" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="430.6" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="416.3" y1="413.5" x2="416.3" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="415.03" y="418.7" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="420.2" y1="435.8" x2="420.2" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="443.6" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="424.1" y1="453.7" x2="424.1" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="458.6" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="428.1" y1="457.1" x2="428.1" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="461.5" width="2.44" height="11.7" fill="var(--up)"/>
<line x1="432.0" y1="459.7" x2="432.0" y2="490.8" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="459.9" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="435.9" y1="426.8" x2="435.9" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="431.9" width="2.44" height="29.8" fill="var(--up)"/>
<line x1="439.9" y1="429.6" x2="439.9" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="436.6" width="2.44" height="54.7" fill="var(--down)"/>
<line x1="443.8" y1="479.4" x2="443.8" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="493.6" width="2.44" height="26.4" fill="var(--down)"/>
<line x1="447.7" y1="484.8" x2="447.7" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="492.6" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="451.7" y1="466.9" x2="451.7" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="450.46" y="478.6" width="2.44" height="28.5" fill="var(--down)"/>
<line x1="455.6" y1="522.4" x2="455.6" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="526.5" width="2.44" height="15.0" fill="var(--down)"/>
<line x1="459.6" y1="524.2" x2="459.6" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="550.3" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="463.5" y1="522.1" x2="463.5" y2="560.7" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="534.3" width="2.44" height="16.6" fill="var(--up)"/>
<line x1="467.4" y1="460.2" x2="467.4" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="474.9" width="2.44" height="35.0" fill="var(--down)"/>
<line x1="471.4" y1="415.1" x2="471.4" y2="475.7" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="423.1" width="2.44" height="46.1" fill="var(--up)"/>
<line x1="475.3" y1="400.6" x2="475.3" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="405.8" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="479.2" y1="381.7" x2="479.2" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="400.6" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="483.2" y1="369.5" x2="483.2" y2="421.8" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="382.2" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="487.1" y1="388.4" x2="487.1" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="392.6" width="2.44" height="41.5" fill="var(--down)"/>
<line x1="491.0" y1="392.6" x2="491.0" y2="452.4" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="393.9" width="2.44" height="33.2" fill="var(--up)"/>
<line x1="495.0" y1="361.7" x2="495.0" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="362.0" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="498.9" y1="333.7" x2="498.9" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="348.0" width="2.44" height="32.4" fill="var(--up)"/>
<line x1="502.9" y1="393.3" x2="502.9" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="405.8" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="506.8" y1="402.7" x2="506.8" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="403.2" width="2.44" height="26.4" fill="var(--up)"/>
<line x1="510.7" y1="378.3" x2="510.7" y2="422.1" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="387.4" width="2.44" height="21.0" fill="var(--down)"/>
<line x1="514.7" y1="401.1" x2="514.7" y2="444.4" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="410.2" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="518.6" y1="367.2" x2="518.6" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="517.38" y="372.3" width="2.44" height="30.8" fill="var(--up)"/>
<line x1="522.5" y1="373.6" x2="522.5" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="389.4" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="526.5" y1="386.3" x2="526.5" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="525.26" y="388.7" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="530.4" y1="358.1" x2="530.4" y2="398.5" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="368.7" width="2.44" height="23.6" fill="var(--up)"/>
<line x1="534.3" y1="344.6" x2="534.3" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="362.2" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="538.3" y1="314.8" x2="538.3" y2="381.9" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="322.9" width="2.44" height="52.6" fill="var(--up)"/>
<line x1="542.2" y1="317.9" x2="542.2" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="321.8" width="2.44" height="25.7" fill="var(--down)"/>
<line x1="546.2" y1="300.8" x2="546.2" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="324.7" width="2.44" height="60.9" fill="var(--up)"/>
<line x1="550.1" y1="257.1" x2="550.1" y2="314.8" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="295.1" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="554.0" y1="266.1" x2="554.0" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="276.2" width="2.44" height="13.0" fill="var(--up)"/>
<line x1="558.0" y1="256.8" x2="558.0" y2="324.7" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="276.0" width="2.44" height="38.3" fill="var(--down)"/>
<line x1="561.9" y1="312.2" x2="561.9" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="316.4" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="565.8" y1="299.5" x2="565.8" y2="328.0" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="305.2" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="569.8" y1="289.4" x2="569.8" y2="327.5" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="295.9" width="2.44" height="29.5" fill="var(--up)"/>
<line x1="573.7" y1="243.3" x2="573.7" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="252.4" width="2.44" height="25.9" fill="var(--up)"/>
<line x1="577.7" y1="224.7" x2="577.7" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="229.8" width="2.44" height="16.8" fill="var(--down)"/>
<line x1="581.6" y1="209.9" x2="581.6" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="236.1" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="585.5" y1="251.4" x2="585.5" y2="286.1" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="255.2" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="589.5" y1="227.3" x2="589.5" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="245.9" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="593.4" y1="211.5" x2="593.4" y2="244.9" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="230.4" width="2.44" height="8.0" fill="var(--down)"/>
<line x1="597.3" y1="213.3" x2="597.3" y2="250.1" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="228.6" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="601.3" y1="228.0" x2="601.3" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="240.0" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="605.2" y1="189.7" x2="605.2" y2="241.3" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="189.9" width="2.44" height="46.1" fill="var(--up)"/>
<line x1="609.1" y1="151.3" x2="609.1" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="169.0" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="613.1" y1="150.8" x2="613.1" y2="184.0" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="174.1" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="617.0" y1="159.9" x2="617.0" y2="186.8" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="177.5" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="621.0" y1="142.0" x2="621.0" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="164.6" width="2.44" height="9.8" fill="var(--down)"/>
<line x1="624.9" y1="170.0" x2="624.9" y2="234.5" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="174.4" width="2.44" height="23.6" fill="var(--down)"/>
<line x1="628.8" y1="103.9" x2="628.8" y2="189.4" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="167.9" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="632.8" y1="126.7" x2="632.8" y2="174.4" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="159.6" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="636.7" y1="121.0" x2="636.7" y2="211.2" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="153.7" width="2.44" height="49.2" fill="var(--up)"/>
<line x1="640.6" y1="101.1" x2="640.6" y2="154.5" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="141.5" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="644.6" y1="82.2" x2="644.6" y2="149.3" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="83.7" width="2.44" height="62.7" fill="var(--up)"/>
<line x1="648.5" y1="85.0" x2="648.5" y2="115.1" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="85.0" width="2.44" height="26.4" fill="var(--down)"/>
<line x1="652.4" y1="75.7" x2="652.4" y2="100.6" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="93.6" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="656.4" y1="88.6" x2="656.4" y2="189.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="95.9" width="2.44" height="78.2" fill="var(--down)"/>
<line x1="660.3" y1="144.9" x2="660.3" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="159.4" width="2.44" height="35.5" fill="var(--down)"/>
<line x1="664.3" y1="205.2" x2="664.3" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="224.4" width="2.44" height="36.5" fill="var(--down)"/>
<line x1="668.2" y1="233.0" x2="668.2" y2="304.7" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="235.0" width="2.44" height="61.9" fill="var(--down)"/>
<line x1="672.1" y1="265.6" x2="672.1" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="278.8" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="676.1" y1="249.0" x2="676.1" y2="283.7" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="271.0" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="680.0" y1="279.1" x2="680.0" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="678.78" y="284.5" width="2.44" height="32.6" fill="var(--up)"/>
<line x1="683.9" y1="266.9" x2="683.9" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="283.5" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="687.9" y1="302.4" x2="687.9" y2="337.4" stroke="var(--down)" class="wick"/>
<rect x="686.65" y="317.4" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="691.8" y1="315.9" x2="691.8" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="320.8" width="2.44" height="28.0" fill="var(--down)"/>
<line x1="695.7" y1="344.6" x2="695.7" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="354.7" width="2.44" height="19.7" fill="var(--down)"/>
<line x1="699.7" y1="362.5" x2="699.7" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="373.1" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="703.6" y1="328.0" x2="703.6" y2="373.1" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="330.9" width="2.44" height="36.3" fill="var(--up)"/>
<line x1="707.6" y1="325.2" x2="707.6" y2="383.0" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="328.6" width="2.44" height="44.6" fill="var(--up)"/>
<line x1="711.5" y1="327.8" x2="711.5" y2="373.1" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="351.4" width="2.44" height="15.5" fill="var(--down)"/>
<line x1="715.4" y1="356.0" x2="715.4" y2="386.1" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="367.4" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="719.4" y1="308.4" x2="719.4" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="322.3" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="723.3" y1="302.1" x2="723.3" y2="344.1" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="316.9" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="727.2" y1="313.8" x2="727.2" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="317.4" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="731.2" y1="268.5" x2="731.2" y2="330.6" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="300.6" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="735.1" y1="287.6" x2="735.1" y2="307.6" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="303.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="739.0" y1="281.4" x2="739.0" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="300.6" width="2.44" height="11.7" fill="var(--down)"/>
<line x1="743.0" y1="272.1" x2="743.0" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="287.1" width="2.44" height="35.2" fill="var(--up)"/>
<line x1="746.9" y1="288.4" x2="746.9" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="289.2" width="2.44" height="34.7" fill="var(--down)"/>
<line x1="750.9" y1="293.6" x2="750.9" y2="323.1" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="313.0" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="754.8" y1="304.5" x2="754.8" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="322.3" width="2.44" height="2.3" fill="var(--up)"/>
<line x1="758.7" y1="334.0" x2="758.7" y2="366.1" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="354.5" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="762.7" y1="374.4" x2="762.7" y2="410.7" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="377.8" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="766.6" y1="374.2" x2="766.6" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="383.0" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="770.5" y1="366.9" x2="770.5" y2="388.9" stroke="var(--down)" class="wick"/>
<rect x="769.32" y="379.9" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="774.5" y1="373.9" x2="774.5" y2="407.1" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="378.8" width="2.44" height="19.7" fill="var(--down)"/>
<line x1="778.4" y1="393.6" x2="778.4" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="394.6" width="2.44" height="3.6" fill="var(--up)"/>
<line x1="782.3" y1="366.9" x2="782.3" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="378.1" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="786.3" y1="361.2" x2="786.3" y2="390.0" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="363.3" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="790.2" y1="347.0" x2="790.2" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="355.2" width="2.44" height="28.5" fill="var(--up)"/>
<line x1="794.2" y1="294.4" x2="794.2" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="295.1" width="2.44" height="50.8" fill="var(--up)"/>
<line x1="798.1" y1="299.8" x2="798.1" y2="348.8" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="307.1" width="2.44" height="38.3" fill="var(--down)"/>
<line x1="802.0" y1="321.8" x2="802.0" y2="351.9" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="324.9" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="806.0" y1="338.9" x2="806.0" y2="366.7" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="343.1" width="2.44" height="16.1" fill="var(--up)"/>
<line x1="809.9" y1="342.8" x2="809.9" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="349.6" width="2.44" height="37.8" fill="var(--down)"/>
<line x1="813.8" y1="389.7" x2="813.8" y2="417.2" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="398.5" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="817.8" y1="402.7" x2="817.8" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="409.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="821.7" y1="404.7" x2="821.7" y2="430.9" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="406.0" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="825.7" y1="400.9" x2="825.7" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="412.0" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="829.6" y1="405.8" x2="829.6" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="419.0" width="2.44" height="8.0" fill="var(--down)"/>
<line x1="833.5" y1="418.2" x2="833.5" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="420.5" width="2.44" height="11.9" fill="var(--down)"/>
<line x1="837.5" y1="400.1" x2="837.5" y2="425.5" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="412.5" width="2.44" height="11.1" fill="var(--up)"/>
<line x1="841.4" y1="405.5" x2="841.4" y2="453.2" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="413.8" width="2.44" height="37.3" fill="var(--down)"/>
<line x1="845.3" y1="444.1" x2="845.3" y2="477.5" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="457.6" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="849.3" y1="469.0" x2="849.3" y2="489.2" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="471.1" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="853.2" y1="456.6" x2="853.2" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="467.4" width="2.44" height="13.2" fill="var(--down)"/>
<line x1="857.1" y1="458.9" x2="857.1" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="469.5" width="2.44" height="47.7" fill="var(--down)"/>
<line x1="861.1" y1="488.9" x2="861.1" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="498.0" width="2.44" height="10.9" fill="var(--up)"/>
<line x1="865.0" y1="492.1" x2="865.0" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="528.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="869.0" y1="499.3" x2="869.0" y2="541.8" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="512.8" width="2.44" height="22.3" fill="var(--up)"/>
<line x1="872.9" y1="501.4" x2="872.9" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="519.0" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="876.8" y1="510.7" x2="876.8" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="875.61" y="527.5" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="880.8" y1="500.3" x2="880.8" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="500.6" width="2.44" height="17.6" fill="var(--up)"/>
<line x1="884.7" y1="501.6" x2="884.7" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="505.3" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="888.6" y1="492.1" x2="888.6" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="509.9" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="892.6" y1="501.6" x2="892.6" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="505.5" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="896.5" y1="455.0" x2="896.5" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="478.3" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="900.4" y1="472.6" x2="900.4" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="482.2" width="2.44" height="14.2" fill="var(--down)"/>
<line x1="904.4" y1="451.4" x2="904.4" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="903.16" y="466.1" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="908.3" y1="464.1" x2="908.3" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="470.5" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="912.3" y1="465.9" x2="912.3" y2="491.5" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="475.5" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="916.2" y1="477.8" x2="916.2" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="481.9" width="2.44" height="22.0" fill="var(--down)"/>
<line x1="920.1" y1="494.9" x2="920.1" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="502.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="924.1" y1="495.4" x2="924.1" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="499.6" width="2.44" height="18.7" fill="var(--down)"/>
<line x1="928.0" y1="515.6" x2="928.0" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="516.1" width="2.44" height="28.2" fill="var(--down)"/>
<line x1="931.9" y1="542.1" x2="931.9" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="545.4" width="2.44" height="32.6" fill="var(--down)"/>
<line x1="935.9" y1="549.6" x2="935.9" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="555.5" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="939.8" y1="539.7" x2="939.8" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="553.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="943.7" y1="538.4" x2="943.7" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="553.2" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="947.7" y1="553.5" x2="947.7" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="559.9" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="951.6" y1="535.3" x2="951.6" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="546.2" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="955.6" y1="562.0" x2="955.6" y2="585.6" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="564.1" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="959.5" y1="551.4" x2="959.5" y2="571.8" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="553.5" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="963.4" y1="443.1" x2="963.4" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="444.4" width="2.44" height="75.4" fill="var(--up)"/>
<line x1="967.4" y1="423.6" x2="967.4" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="434.5" width="2.44" height="25.9" fill="var(--down)"/>
<line x1="971.3" y1="436.1" x2="971.3" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="453.7" width="2.44" height="16.1" fill="var(--down)"/>
<line x1="975.2" y1="476.0" x2="975.2" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="485.3" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="979.2" y1="471.8" x2="979.2" y2="516.7" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="493.9" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="983.1" y1="465.9" x2="983.1" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="481.7" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="987.0" y1="477.0" x2="987.0" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="478.1" width="2.44" height="18.9" fill="var(--up)"/>
<line x1="991.0" y1="461.5" x2="991.0" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="463.0" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="994.9" y1="451.4" x2="994.9" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="456.0" width="2.44" height="22.0" fill="var(--up)"/>
<line x1="998.9" y1="465.9" x2="998.9" y2="496.5" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="476.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="1002.8" y1="463.8" x2="1002.8" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="470.5" width="2.44" height="45.9" fill="var(--down)"/>
<line x1="1006.7" y1="485.8" x2="1006.7" y2="519.3" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="493.3" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="1010.7" y1="497.0" x2="1010.7" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="504.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="1014.6" y1="440.7" x2="1014.6" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="442.6" width="2.44" height="42.5" fill="var(--up)"/>
<line x1="1018.5" y1="429.3" x2="1018.5" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="435.1" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="1022.5" y1="426.0" x2="1022.5" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="436.9" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="1026.4" y1="440.0" x2="1026.4" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="442.6" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="1030.3" y1="414.8" x2="1030.3" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="1029.13" y="433.8" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="1034.3" y1="433.8" x2="1034.3" y2="486.6" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="435.1" width="2.44" height="35.2" fill="var(--down)"/>
<line x1="1038.2" y1="446.7" x2="1038.2" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="451.6" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="1042.2" y1="443.3" x2="1042.2" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="451.6" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="1046.1" y1="427.3" x2="1046.1" y2="467.4" stroke="var(--up)" class="wick"/>
<rect x="1044.87" y="447.5" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="1050.0" y1="432.2" x2="1050.0" y2="452.8" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="445.2" width="2.44" height="4.1" fill="var(--down)"/>
<line x1="60" y1="420.7" x2="1052" y2="420.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="424.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$55 R1</text>
<text x="1058" y="436.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="350.7" x2="1052" y2="350.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="354.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$58 R2</text>
<text x="1058" y="366.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="273.1" x2="1052" y2="273.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="276.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$61 R3</text>
<text x="1058" y="288.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="460.8" x2="1052" y2="460.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="454.8" font-size="11.5" fill="var(--support)" font-weight="600">$53 S1</text>
<text x="1058" y="466.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="523.0" x2="1052" y2="523.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="517.0" font-size="11.5" fill="var(--support)" font-weight="600">$51 S2</text>
<text x="1058" y="529.0" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="585.6" x2="1052" y2="585.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="579.6" font-size="11.5" fill="var(--support)" font-weight="600">$49 S3</text>
<text x="1058" y="591.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="449.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="441.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $54 (2026-08-21)</text>
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
| R3 | $61 | 3 | 2025-11-13·2026-04-27·2026-05-19 — 2026년 봄 헨리허브 가격 강세 구간의 스윙 고점대 |
| R2 | $58 | 3 | 2025-10-07·2025-10-20·2026-01-30 |
| R1 | $55 | 5 | 2025-12-30·2026-06-04·2026-06-30·2026-07-23·2026-08-14 — 최근 3개월간 반복적으로 저항받은 구간 |
| **현재가** | **$53.82** (2026-08-21 장중, 종가 기준은 $53.89 — 2026-08-20) | — | R1과 S1 사이 |
| S1 | $53 | 2 | 현재가에 가장 근접한 지지 |
| S2 | $51 | 4 | 2025-10-14·2025-10-29·2026-06-16·2026-08-05 |
| S3 | $49 | 4 | 2025-09-16·2026-01-15·2026-07-10·2026-07-20 — Q2 2026 실적 발표 직전 저점대 |

> 레벨 6개(스크립트 기본값 3개에서 확대) — 최근 1년간 헨리허브 가격이 겨울 강세($5대)·여름 약세($2대 후반)를 오가며 EQT 주가도 $49~$68 넓은 밴드에서 움직여, 기본 3개 레벨로는 밴드 상하단을 다 담지 못해 늘렸다(§4에 반영).

---

## 3. 관측된 특이 구간 — 2026-07-22 Q2 2026 실적 발표 후 급등

- 2026-07-21 장 마감 후 Q2 2026 실적 발표([최근 뉴스 / 이슈](./08_news.md) 로그 참고) — 매출·FCF가 시장 예상을 상회.
- 종가 기준 전일 대비 **+8.45%** ($49.80 → $54.01), 거래량은 평소(일 평균 약 819만 주) 대비 약 **2.2배**인 **1,785만 주**.
- 이 갭업 이후 주가는 S3($49)에서 R1($55) 부근까지 레짐이 한 단계 올라섰고, 이전 저항이었던 $53 부근이 새로운 지지(S1)로 재편됐다 — 실적 발표를 계기로 거래 밴드 자체가 위로 이동한 사례.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-08-21~2026-08-21. 수집 시점: 2026-08-21. 원주가(과거 분할은 소급 반영, 배당은 미반영 — 최근 1년 내 배당 4회 지급)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py EQT --name "EQT Corporation" --close-on 2026-08-20 --event 2026-07-22:"Q2 2026 실적 발표 후 급등"` — 레벨 개수만 기본값(3)에서 6으로 확대(위 §2 각주 근거).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 252개 표본에서 스크립트에 고정된 파라미터이며, 최적화된 값이 아니다.
    - 원자재 가격(헨리허브 스팟가스) 자체의 계절 변동성이 이 회사 주가 변동의 상당 부분을 설명한다 — §3의 갭업도 실적 서프라이즈지만 그 배경엔 계절적 가격 강세가 있었다(핵심 지표 B절 참고). 순수 기술적 패턴만으로 이 변동을 해석하면 원자재 사이클이라는 근본 동인을 놓칠 수 있다.
    - 조사 기간(2025-08~2026-08) 중 주식분할·대규모 유상증자는 없었다(2024.07 Equitrans 인수 관련 신주 발행은 이 기간 이전 사건).

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
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — EQT Corporation (EQT)](https://finance.yahoo.com/quote/EQT/)
- [StockAnalysis — EQT 종가 이력](https://stockanalysis.com/stocks/eqt/history/)

---

*작성일: 2026-08-21*
