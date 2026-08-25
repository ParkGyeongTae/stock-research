# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 최근 1년의 단기 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: **2026-08-24 종가 $1,199.08**이 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다. [기술적 분석 — 일봉·1년](./09_technical_daily.md)과도 같은 값이다.
    - ⚠️ **마지막 주봉(2026-08-25 주)은 아직 진행 중인 주간**이다. 그래서 기준 종가는 마지막으로 정규장이 마감된 2026-08-24로 통일했다.
    - ⚠️ **배당 조정 없음 — 이 문서에서 가장 중요한 주의사항이다.** 5년 창 안에 특별배당이 **4회, 합계 주당 $218.50** 지급됐는데 원주가 차트라 전혀 반영돼 있지 않다. 아래 3. 관측된 특이 구간 참고.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-25)

[경고] 이벤트 날짜 2022-08-18 가 거래일에 없음 — 건너뜀
[경고] 이벤트 날짜 2023-11-17 가 거래일에 없음 — 건너뜀
[경고] 이벤트 날짜 2024-10-04 가 거래일에 없음 — 건너뜀
[경고] 이벤트 날짜 2025-09-02 가 거래일에 없음 — 건너뜀
<div class="tdg-chart">
<style>
.tdg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .tdg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .tdg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tdg-chart svg { width:100%; height:auto; display:block; }
.tdg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tdg-chart .title { fill: var(--ink); font-weight:600; }
.tdg-chart .grid { stroke: var(--grid); stroke-width:1; }
.tdg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="TransDigm Group(TDG) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">TransDigm Group (TDG) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-25 · 마지막 종가 $1,185.54 (2026-08-25) · 단위 USD</text>
<line x1="60" y1="559.5" x2="1052" y2="559.5" class="grid"/>
<text x="52" y="563.5" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="464.5" x2="1052" y2="464.5" class="grid"/>
<text x="52" y="468.5" font-size="11" text-anchor="end" fill="var(--muted)">800</text>
<line x1="60" y1="369.5" x2="1052" y2="369.5" class="grid"/>
<text x="52" y="373.5" font-size="11" text-anchor="end" fill="var(--muted)">1,000</text>
<line x1="60" y1="274.5" x2="1052" y2="274.5" class="grid"/>
<text x="52" y="278.5" font-size="11" text-anchor="end" fill="var(--muted)">1,200</text>
<line x1="60" y1="179.5" x2="1052" y2="179.5" class="grid"/>
<text x="52" y="183.5" font-size="11" text-anchor="end" fill="var(--muted)">1,400</text>
<line x1="60" y1="84.5" x2="1052" y2="84.5" class="grid"/>
<text x="52" y="88.5" font-size="11" text-anchor="end" fill="var(--muted)">1,600</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="133.6" y1="56.0" x2="133.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.6" y1="626.0" x2="133.6" y2="631.0" class="axis"/>
<text x="133.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="329.7" y1="56.0" x2="329.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="329.7" y1="626.0" x2="329.7" y2="631.0" class="axis"/>
<text x="329.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="525.8" y1="56.0" x2="525.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="525.8" y1="626.0" x2="525.8" y2="631.0" class="axis"/>
<text x="525.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="725.7" y1="56.0" x2="725.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="725.7" y1="626.0" x2="725.7" y2="631.0" class="axis"/>
<text x="725.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.9" y1="56.0" x2="921.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.9" y1="626.0" x2="921.9" y2="631.0" class="axis"/>
<text x="921.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="553.8" x2="61.9" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="555.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="65.7" y1="552.0" x2="65.7" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="555.6" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="69.4" y1="555.6" x2="69.4" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="557.8" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="73.2" y1="552.0" x2="73.2" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="554.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="77.0" y1="538.0" x2="77.0" y2="559.8" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="538.4" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="80.7" y1="532.6" x2="80.7" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="534.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="84.5" y1="531.8" x2="84.5" y2="544.7" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="534.0" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="88.3" y1="536.5" x2="88.3" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="538.8" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="92.1" y1="532.9" x2="92.1" y2="545.8" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="536.6" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="95.8" y1="535.9" x2="95.8" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="537.9" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="99.6" y1="528.2" x2="99.6" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="528.6" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="103.4" y1="518.6" x2="103.4" y2="542.7" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="527.6" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="107.1" y1="525.2" x2="107.1" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="536.5" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="110.9" y1="539.1" x2="110.9" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="544.2" width="2.34" height="33.7" fill="var(--down)"/>
<line x1="114.7" y1="562.4" x2="114.7" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="567.1" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="118.5" y1="551.6" x2="118.5" y2="565.3" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="557.0" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="122.2" y1="558.6" x2="122.2" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="559.0" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="126.0" y1="543.0" x2="126.0" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="546.2" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="129.8" y1="539.4" x2="129.8" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="542.3" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="133.6" y1="526.7" x2="133.6" y2="544.5" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="533.8" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="137.3" y1="528.1" x2="137.3" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="534.4" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="141.1" y1="538.9" x2="141.1" y2="554.9" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="541.6" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="144.9" y1="543.7" x2="144.9" y2="571.4" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="557.5" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="148.6" y1="545.3" x2="148.6" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="550.2" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="152.4" y1="528.3" x2="152.4" y2="555.1" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="541.3" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="156.2" y1="526.0" x2="156.2" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="536.2" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="160.0" y1="527.4" x2="160.0" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="529.8" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="163.7" y1="520.8" x2="163.7" y2="547.8" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="532.0" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="167.5" y1="537.0" x2="167.5" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="541.9" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="171.3" y1="525.3" x2="171.3" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="530.4" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="175.0" y1="519.3" x2="175.0" y2="537.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="523.6" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="178.8" y1="519.3" x2="178.8" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="524.2" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="182.6" y1="522.4" x2="182.6" y2="540.8" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="527.0" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="186.4" y1="536.6" x2="186.4" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="541.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="190.1" y1="531.8" x2="190.1" y2="548.4" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="540.9" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="193.9" y1="546.7" x2="193.9" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="550.8" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="197.7" y1="548.0" x2="197.7" y2="570.7" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="561.9" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="201.4" y1="564.3" x2="201.4" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="571.0" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="205.2" y1="575.3" x2="205.2" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="579.0" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="209.0" y1="552.8" x2="209.0" y2="582.1" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="553.7" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="212.8" y1="551.0" x2="212.8" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="551.7" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="216.5" y1="543.7" x2="216.5" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="547.5" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="220.3" y1="576.1" x2="220.3" y2="607.0" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="576.1" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="224.1" y1="588.4" x2="224.1" y2="600.6" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="588.6" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="227.8" y1="582.5" x2="227.8" y2="599.9" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="587.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="231.6" y1="587.3" x2="231.6" y2="600.0" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="589.6" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="235.4" y1="583.2" x2="235.4" y2="593.9" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="588.9" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="239.2" y1="560.4" x2="239.2" y2="588.9" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="568.5" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="242.9" y1="547.7" x2="242.9" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="548.9" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="246.7" y1="541.0" x2="246.7" y2="552.4" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="541.3" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="250.5" y1="522.6" x2="250.5" y2="543.6" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="523.1" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="254.3" y1="521.5" x2="254.3" y2="541.8" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="525.5" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="258.0" y1="532.1" x2="258.0" y2="545.2" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="542.5" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="261.8" y1="545.0" x2="261.8" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="548.5" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="265.6" y1="549.3" x2="265.6" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="550.0" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="269.3" y1="545.3" x2="269.3" y2="572.3" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="548.6" width="2.34" height="19.4" fill="var(--down)"/>
<line x1="273.1" y1="561.9" x2="273.1" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="569.2" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="276.9" y1="583.7" x2="276.9" y2="596.0" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="589.4" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="280.7" y1="575.6" x2="280.7" y2="596.0" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="591.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="284.4" y1="586.3" x2="284.4" y2="607.2" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="588.2" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="288.2" y1="584.5" x2="288.2" y2="596.8" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="589.0" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="292.0" y1="567.4" x2="292.0" y2="589.7" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="568.3" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="295.7" y1="566.0" x2="295.7" y2="585.5" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="569.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="299.5" y1="536.5" x2="299.5" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="547.0" width="2.34" height="19.3" fill="var(--up)"/>
<line x1="303.3" y1="545.9" x2="303.3" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="549.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="307.1" y1="539.0" x2="307.1" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="542.1" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="310.8" y1="541.5" x2="310.8" y2="558.5" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="549.1" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="314.6" y1="544.6" x2="314.6" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="552.1" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="318.4" y1="542.0" x2="318.4" y2="559.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="553.8" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="322.1" y1="546.4" x2="322.1" y2="559.7" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="549.8" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="325.9" y1="543.9" x2="325.9" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="545.4" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="329.7" y1="534.6" x2="329.7" y2="548.3" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="536.2" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="333.5" y1="518.8" x2="333.5" y2="538.1" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="519.7" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="337.2" y1="516.3" x2="337.2" y2="531.2" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="519.1" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="341.0" y1="503.9" x2="341.0" y2="525.3" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="506.9" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="344.8" y1="496.1" x2="344.8" y2="510.8" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="505.6" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="348.5" y1="480.3" x2="348.5" y2="509.3" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="497.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="352.3" y1="479.4" x2="352.3" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="491.1" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="356.1" y1="489.6" x2="356.1" y2="498.0" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="492.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="359.9" y1="479.4" x2="359.9" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="480.1" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="363.6" y1="477.8" x2="363.6" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="480.5" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="367.4" y1="494.2" x2="367.4" y2="518.4" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="510.4" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="371.2" y1="500.7" x2="371.2" y2="516.9" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="510.2" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="375.0" y1="492.1" x2="375.0" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="494.4" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="378.7" y1="488.6" x2="378.7" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="493.2" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="382.5" y1="485.4" x2="382.5" y2="504.9" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="487.4" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="386.3" y1="479.7" x2="386.3" y2="488.5" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="481.4" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="390.0" y1="479.0" x2="390.0" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="480.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="393.8" y1="474.3" x2="393.8" y2="487.8" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="480.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="397.6" y1="456.5" x2="397.6" y2="480.6" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="466.6" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="401.4" y1="449.5" x2="401.4" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="453.8" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="405.1" y1="452.0" x2="405.1" y2="479.7" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="453.8" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="408.9" y1="463.5" x2="408.9" y2="479.6" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="467.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="412.7" y1="459.9" x2="412.7" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="464.5" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="416.4" y1="450.2" x2="416.4" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="457.0" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="420.2" y1="436.6" x2="420.2" y2="458.1" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="440.6" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="424.0" y1="417.2" x2="424.0" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="419.8" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="427.8" y1="418.5" x2="427.8" y2="428.4" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="422.3" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="431.5" y1="418.3" x2="431.5" y2="427.2" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="422.3" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="435.3" y1="417.0" x2="435.3" y2="425.8" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="422.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="439.1" y1="417.0" x2="439.1" y2="432.5" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="423.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="442.8" y1="410.2" x2="442.8" y2="427.3" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="418.9" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="446.6" y1="398.0" x2="446.6" y2="435.9" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="416.5" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="450.4" y1="428.2" x2="450.4" y2="448.3" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="429.6" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="454.2" y1="430.3" x2="454.2" y2="441.6" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="433.7" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="457.9" y1="410.4" x2="457.9" y2="434.2" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="411.6" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="461.7" y1="411.2" x2="461.7" y2="433.6" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="411.2" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="465.5" y1="425.9" x2="465.5" y2="435.8" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="427.9" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="469.2" y1="426.3" x2="469.2" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="433.3" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="473.0" y1="435.1" x2="473.0" y2="446.5" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="444.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="476.8" y1="439.9" x2="476.8" y2="463.3" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="440.7" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="480.6" y1="427.1" x2="480.6" y2="441.5" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="437.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="484.3" y1="429.5" x2="484.3" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="433.1" width="2.34" height="20.5" fill="var(--down)"/>
<line x1="488.1" y1="445.9" x2="488.1" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="454.1" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="491.9" y1="421.6" x2="491.9" y2="456.4" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="425.5" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="495.7" y1="371.3" x2="495.7" y2="428.9" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="373.1" width="2.34" height="52.2" fill="var(--up)"/>
<line x1="499.4" y1="363.3" x2="499.4" y2="392.7" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="374.2" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="503.2" y1="379.1" x2="503.2" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="383.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="507.0" y1="379.0" x2="507.0" y2="393.3" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="383.6" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="510.7" y1="376.1" x2="510.7" y2="392.8" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="377.1" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="514.5" y1="362.0" x2="514.5" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="376.3" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="518.3" y1="366.7" x2="518.3" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="369.3" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="522.1" y1="360.7" x2="522.1" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="364.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="525.8" y1="363.1" x2="525.8" y2="382.8" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="366.8" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="529.6" y1="353.4" x2="529.6" y2="381.4" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="353.9" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="533.4" y1="341.0" x2="533.4" y2="361.0" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="342.4" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="537.1" y1="326.8" x2="537.1" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="330.3" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="540.9" y1="308.0" x2="540.9" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="310.7" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="544.7" y1="295.8" x2="544.7" y2="317.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="312.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="548.5" y1="291.1" x2="548.5" y2="321.6" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="300.0" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="552.2" y1="270.9" x2="552.2" y2="302.1" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="274.6" width="2.34" height="25.4" fill="var(--up)"/>
<line x1="556.0" y1="271.2" x2="556.0" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="272.9" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="559.8" y1="279.5" x2="559.8" y2="298.8" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="280.5" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="563.5" y1="278.0" x2="563.5" y2="304.8" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="287.7" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="567.3" y1="256.3" x2="567.3" y2="285.2" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="259.7" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="571.1" y1="256.0" x2="571.1" y2="266.3" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="256.4" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="574.9" y1="252.5" x2="574.9" y2="276.0" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="257.7" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="578.6" y1="255.9" x2="578.6" y2="275.3" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="257.0" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="582.4" y1="251.5" x2="582.4" y2="281.3" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="254.1" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="586.2" y1="241.5" x2="586.2" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="246.4" width="2.34" height="30.0" fill="var(--up)"/>
<line x1="589.9" y1="225.3" x2="589.9" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="229.9" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="593.7" y1="212.4" x2="593.7" y2="255.5" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="222.0" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="597.5" y1="218.5" x2="597.5" y2="246.0" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="218.5" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="601.3" y1="203.1" x2="601.3" y2="229.0" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="203.1" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="605.0" y1="196.8" x2="605.0" y2="224.4" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="200.1" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="608.8" y1="193.9" x2="608.8" y2="222.4" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="199.9" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="612.6" y1="211.3" x2="612.6" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="223.0" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="616.3" y1="203.7" x2="616.3" y2="230.7" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="217.0" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="620.1" y1="211.2" x2="620.1" y2="243.2" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="211.7" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="623.9" y1="227.7" x2="623.9" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="227.7" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="627.7" y1="235.9" x2="627.7" y2="256.9" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="237.5" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="631.4" y1="234.2" x2="631.4" y2="260.1" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="250.7" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="635.2" y1="228.7" x2="635.2" y2="261.1" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="252.8" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="639.0" y1="225.8" x2="639.0" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="254.9" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="642.8" y1="241.5" x2="642.8" y2="285.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="252.6" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="646.5" y1="236.0" x2="646.5" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="236.5" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="650.3" y1="208.3" x2="650.3" y2="237.2" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="214.3" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="654.1" y1="188.6" x2="654.1" y2="231.6" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="192.2" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="657.8" y1="189.3" x2="657.8" y2="230.2" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="194.4" width="2.34" height="35.4" fill="var(--down)"/>
<line x1="661.6" y1="190.8" x2="661.6" y2="232.9" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="194.8" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="665.4" y1="170.0" x2="665.4" y2="196.8" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="175.7" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="669.2" y1="163.8" x2="669.2" y2="181.9" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="175.4" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="672.9" y1="155.1" x2="672.9" y2="209.8" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="180.3" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="676.7" y1="172.6" x2="676.7" y2="206.5" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="174.6" width="2.34" height="27.7" fill="var(--up)"/>
<line x1="680.5" y1="167.8" x2="680.5" y2="192.2" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="171.9" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="684.2" y1="176.6" x2="684.2" y2="209.3" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="179.5" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="688.0" y1="196.7" x2="688.0" y2="227.0" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="196.7" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="691.8" y1="179.5" x2="691.8" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="202.8" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="695.6" y1="186.8" x2="695.6" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="198.0" width="2.34" height="50.8" fill="var(--down)"/>
<line x1="699.3" y1="221.8" x2="699.3" y2="260.2" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="245.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="703.1" y1="239.4" x2="703.1" y2="255.2" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="242.2" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="706.9" y1="218.6" x2="706.9" y2="252.0" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="236.9" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="710.6" y1="237.1" x2="710.6" y2="257.9" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="237.1" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="714.4" y1="230.1" x2="714.4" y2="256.3" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="238.3" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="718.2" y1="225.8" x2="718.2" y2="244.2" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="231.3" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="722.0" y1="232.1" x2="722.0" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="238.6" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="725.7" y1="233.1" x2="725.7" y2="255.3" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="238.1" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="729.5" y1="207.5" x2="729.5" y2="249.3" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="208.0" width="2.34" height="41.3" fill="var(--up)"/>
<line x1="733.3" y1="189.3" x2="733.3" y2="209.5" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="199.5" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="737.0" y1="193.0" x2="737.0" y2="217.2" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="201.7" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="740.8" y1="197.5" x2="740.8" y2="249.1" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="211.0" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="744.6" y1="195.6" x2="744.6" y2="227.9" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="212.2" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="748.4" y1="203.2" x2="748.4" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="219.0" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="752.1" y1="193.8" x2="752.1" y2="231.9" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="195.1" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="755.9" y1="188.0" x2="755.9" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="193.8" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="759.7" y1="201.6" x2="759.7" y2="224.7" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="204.9" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="763.5" y1="191.4" x2="763.5" y2="213.7" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="203.2" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="767.2" y1="176.0" x2="767.2" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="190.3" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="771.0" y1="172.2" x2="771.0" y2="256.5" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="190.2" width="2.34" height="66.3" fill="var(--down)"/>
<line x1="774.8" y1="213.1" x2="774.8" y2="282.3" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="220.8" width="2.34" height="50.2" fill="var(--up)"/>
<line x1="778.5" y1="194.0" x2="778.5" y2="218.8" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="209.1" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="782.3" y1="187.1" x2="782.3" y2="237.6" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="189.9" width="2.34" height="22.2" fill="var(--up)"/>
<line x1="786.1" y1="147.2" x2="786.1" y2="188.9" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="155.6" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="789.9" y1="137.4" x2="789.9" y2="198.7" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="155.8" width="2.34" height="36.3" fill="var(--down)"/>
<line x1="793.6" y1="157.1" x2="793.6" y2="200.5" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="168.5" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="797.4" y1="155.8" x2="797.4" y2="184.3" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="164.5" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="801.2" y1="145.1" x2="801.2" y2="161.4" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="147.0" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="804.9" y1="147.2" x2="804.9" y2="161.3" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="148.2" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="808.7" y1="146.2" x2="808.7" y2="191.4" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="147.6" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="812.5" y1="153.9" x2="812.5" y2="175.0" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="158.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="816.3" y1="130.5" x2="816.3" y2="162.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="132.4" width="2.34" height="23.9" fill="var(--up)"/>
<line x1="820.0" y1="118.5" x2="820.0" y2="141.0" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="121.1" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="823.8" y1="106.4" x2="823.8" y2="127.7" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="111.6" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="827.6" y1="81.0" x2="827.6" y2="113.0" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="85.8" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="831.3" y1="77.2" x2="831.3" y2="106.9" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="81.0" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="835.1" y1="73.2" x2="835.1" y2="106.1" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="76.2" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="838.9" y1="76.5" x2="838.9" y2="193.8" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="89.4" width="2.34" height="94.9" fill="var(--down)"/>
<line x1="842.7" y1="161.5" x2="842.7" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="181.0" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="846.4" y1="171.0" x2="846.4" y2="187.8" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="175.5" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="850.2" y1="166.5" x2="850.2" y2="185.8" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="175.2" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="854.0" y1="218.9" x2="854.0" y2="245.8" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="224.7" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="857.7" y1="215.2" x2="857.7" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="240.6" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="861.5" y1="224.9" x2="861.5" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="235.3" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="865.3" y1="217.5" x2="865.3" y2="241.8" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="229.0" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="869.1" y1="211.3" x2="869.1" y2="238.1" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="227.5" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="872.8" y1="225.3" x2="872.8" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="231.7" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="876.6" y1="216.4" x2="876.6" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="235.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="880.4" y1="197.8" x2="880.4" y2="241.5" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="198.8" width="2.34" height="42.4" fill="var(--up)"/>
<line x1="884.2" y1="195.7" x2="884.2" y2="226.7" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="201.0" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="887.9" y1="221.9" x2="887.9" y2="250.2" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="222.8" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="891.7" y1="198.9" x2="891.7" y2="241.2" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="207.7" width="2.34" height="28.1" fill="var(--up)"/>
<line x1="895.5" y1="195.8" x2="895.5" y2="218.9" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="204.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="899.2" y1="197.1" x2="899.2" y2="211.9" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="198.4" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="903.0" y1="194.9" x2="903.0" y2="211.7" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="202.7" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="906.8" y1="200.0" x2="906.8" y2="237.9" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="205.8" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="910.6" y1="221.1" x2="910.6" y2="256.9" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="223.9" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="914.3" y1="217.6" x2="914.3" y2="238.1" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="222.6" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="918.1" y1="198.5" x2="918.1" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="199.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="921.9" y1="172.6" x2="921.9" y2="200.6" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="183.3" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="925.6" y1="149.6" x2="925.6" y2="191.6" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="155.8" width="2.34" height="27.8" fill="var(--up)"/>
<line x1="929.4" y1="151.0" x2="929.4" y2="182.7" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="158.3" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="933.2" y1="156.3" x2="933.2" y2="179.0" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="166.4" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="937.0" y1="160.1" x2="937.0" y2="252.7" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="165.2" width="2.34" height="68.7" fill="var(--down)"/>
<line x1="940.7" y1="208.1" x2="940.7" y2="238.3" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="233.3" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="944.5" y1="203.2" x2="944.5" y2="237.1" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="208.5" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="948.3" y1="210.5" x2="948.3" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="212.1" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="952.0" y1="210.7" x2="952.0" y2="236.7" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="222.1" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="955.8" y1="232.8" x2="955.8" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="232.8" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="959.6" y1="243.9" x2="959.6" y2="289.1" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="263.7" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="963.4" y1="268.9" x2="963.4" y2="304.4" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="278.3" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="967.1" y1="282.1" x2="967.1" y2="310.8" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="290.2" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="970.9" y1="258.3" x2="970.9" y2="294.2" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="271.1" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="974.7" y1="225.5" x2="974.7" y2="274.0" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="243.2" width="2.34" height="27.9" fill="var(--up)"/>
<line x1="978.4" y1="239.0" x2="978.4" y2="304.8" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="243.5" width="2.34" height="55.6" fill="var(--down)"/>
<line x1="982.2" y1="287.3" x2="982.2" y2="308.6" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="296.1" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="986.0" y1="244.9" x2="986.0" y2="298.6" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="267.3" width="2.34" height="27.7" fill="var(--up)"/>
<line x1="989.8" y1="261.9" x2="989.8" y2="301.4" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="265.6" width="2.34" height="33.1" fill="var(--down)"/>
<line x1="993.5" y1="264.4" x2="993.5" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="268.1" width="2.34" height="31.0" fill="var(--up)"/>
<line x1="997.3" y1="234.1" x2="997.3" y2="269.1" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="246.8" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="1001.1" y1="248.3" x2="1001.1" y2="273.6" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="253.7" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="1004.9" y1="243.4" x2="1004.9" y2="272.9" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="247.9" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="1008.6" y1="209.3" x2="1008.6" y2="243.2" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="213.6" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="1012.4" y1="197.7" x2="1012.4" y2="236.2" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="215.3" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="1016.2" y1="202.9" x2="1016.2" y2="224.7" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="204.0" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="1019.9" y1="198.5" x2="1019.9" y2="236.3" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="198.5" width="2.34" height="32.6" fill="var(--down)"/>
<line x1="1023.7" y1="236.1" x2="1023.7" y2="276.9" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="237.6" width="2.34" height="30.0" fill="var(--down)"/>
<line x1="1027.5" y1="248.0" x2="1027.5" y2="278.3" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="257.1" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="1031.3" y1="218.6" x2="1031.3" y2="257.0" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="248.7" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="1035.0" y1="198.8" x2="1035.0" y2="264.8" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="236.4" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="1038.8" y1="243.3" x2="1038.8" y2="268.7" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="247.5" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="1042.6" y1="247.4" x2="1042.6" y2="284.0" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="247.4" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="1046.3" y1="272.7" x2="1046.3" y2="280.3" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="274.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1050.1" y1="268.6" x2="1050.1" y2="282.1" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="269.1" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="60" y1="194.3" x2="1052" y2="194.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="197.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,369 R1</text>
<text x="1058" y="209.8" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="147.4" x2="1052" y2="147.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="150.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,468 R2</text>
<text x="1058" y="162.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="284.0" x2="1052" y2="284.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="278.0" font-size="11.5" fill="var(--support)" font-weight="600">$1,180 S1</text>
<text x="1058" y="290.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="568.6" x2="1052" y2="568.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="562.6" font-size="11.5" fill="var(--support)" font-weight="600">$581 S2</text>
<text x="1058" y="574.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="607.1" x2="1052" y2="607.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="601.1" font-size="11.5" fill="var(--support)" font-weight="600">$500 S3</text>
<text x="1058" y="613.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="281.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="273.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $1,186 (2026-08-25)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $1,468 | 3 | 2024-09-30·2025-05-05·2026-01-12. 5년 최고($1,623.83)에는 못 미치는 **직전 고점 대역** |
| R1 | $1,369 | 5 | 2024-06-03·2025-01-20·2025-10-27·2025-12-01·2026-06-22. **터치 횟수가 가장 많은 대역**이며, 2024년 이후 반복해서 되돌려졌다 |
| **현재가** | **$1,199.08** (2026-08-24 종가) | — | R1과 S1 사이 |
| S1 | $1,180 | 2 | 2024-08-05·2025-04-07. **현재가 바로 아래에 붙어 있다**(괴리 1.6%) — 지금 주가가 이 대역의 상단에 걸쳐 있다는 뜻 |
| S2 | $581 | 2 | 2022-01-24·2022-03-07 |
| S3 | $500 | 2 | 2022-06-13·2022-10-10. 5년 최저($499.63)와 맞닿은 2022년 저점대 |

> **S1과 S2 사이가 $1,180 → $581로 절반 넘게 비어 있다.** 2022년 하반기 이후 주가가 되돌림 없이 올라온 구간이라 그 사이에 스윙 클러스터가 형성되지 않았기 때문이다. **S1이 무너지면 이 창 안에서 참고할 다음 레벨이 사실상 없다** — S2·S3는 4년 전 가격대이자 아래 3. 관측된 특이 구간의 특별배당 4회 이전 수준이라 현재 레짐과 단절돼 있어, 실질적인 지지로 읽어선 안 된다.

---

## 3. 관측된 특이 구간 — 5년간 4회의 특별배당 (합계 주당 $218.50)

- 5년 창 안에서 배당락이 발생한 시점과 금액은 다음과 같다. 전부 부정기 특별배당이며, 재원은 대체로 신규 차입이었다([재무 / 실적](./05_financials.md) 4. 주주 환원 참고).

| 배당락일 | 주당 금액 |
|----------|-----------|
| 2022-08-18 | $18.50 |
| 2023-11-17 | $35.00 |
| 2024-10-04 | $75.00 |
| 2025-09-02 | $90.00 |
| **합계** | **$218.50** |

- **이 차트는 원주가 기준이라 배당락 하락이 그대로 그려져 있다.** 5년간 주당 $218.50이 현금으로 빠져나간 만큼 차트상의 가격 상승률은 **총주주수익률보다 구조적으로 낮게 나타난다.** 5년 차트로 장기 수익률을 가늠할 때 반드시 감안해야 할 부분이다.
- **배당 규모가 매 회 커지고 있다는 점**도 함께 볼 만하다($18.50 → $35 → $75 → $90). 회사의 레버리지 정책이 강화돼 온 흐름과 방향이 같다([핵심 지표](./04_metrics.md) A.3의 순부채 ÷ EBITDA As Defined 추이 참고).
- **그래서 위 2. 지지선 / 저항선 요약의 S2·S3(2022년 저점대)를 현재 지지로 읽으면 안 된다.** 그 이후 주당 $200 이상이 배당으로 빠져나갔으므로, 같은 기업가치라도 주가 수준 자체가 달라졌다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-23~2026-08-25. 수집 시점: 2026-08-26. 원주가(과거 분할은 소급 반영, 배당은 미반영).
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 일봉 문서(전후 5거래일)와 창 길이만 다르고 나머지 로직은 같다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py TDG --name "TransDigm Group" --interval 1wk --event 2022-08-18:"특별배당 $18.50" --event 2023-11-17:"특별배당 $35" --event 2024-10-04:"특별배당 $75" --event 2025-09-02:"특별배당 $90" --close-on 2026-08-24 --emit all`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 263개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **가격 연속성이 네 번 끊겼다** — 위 3. 관측된 특이 구간의 특별배당 4회(합계 주당 $218.50). 원주가라 소급 조정하지 않았고, 그 결과 **배당 이전 시기의 스윙 레벨은 현재와 같은 잣대로 비교할 수 없다.** 5년 창처럼 기간이 길수록 이 왜곡이 누적되므로, 일봉 문서보다 이 문서에서 더 크게 작용한다.
    - **마지막 주봉(2026-08-25 주)은 진행 중인 주간**이라 확정 봉이 아니다.
    - 주식분할·대규모 유상증자 등 주식수 자체를 바꾸는 이벤트는 이 기간에 없었다.

---

## 관련 문서

- **먼저 읽기** — [최종 보고서](./11_final_report.md): 아래 문서 전체를 종합한 요약이라, 처음이라면 여기부터 봐도 된다
- **회사 이해** — [개요](./01_overview.md) · [역사 / 주요 이벤트](./02_history.md) · [CEO / 경영진](./03_ceo.md)
- **숫자** — [핵심 지표](./04_metrics.md) · [재무 / 실적](./05_financials.md) · [밸류에이션 / 적정주가](./06_valuation.md)
- **판단 · 로그** — [투자 판단](./07_investment.md) · [최근 뉴스 / 이슈](./08_news.md)
- **가격 차트** — [기술적 분석 — 일봉·1년](./09_technical_daily.md)
- **산업 맥락** — [항공우주·방위산업 섹터 개요](../00_overview.md)

---

## 참고 자료

- [Yahoo Finance — TDG 주가 이력](https://finance.yahoo.com/quote/TDG/history/)
- 재현 커맨드·파라미터의 마스터는 저장소 루트의 `chart-generation-guide.md`에 있다
- [FY2025 4분기·연간 실적발표 (2025-11-12) — 최근 특별배당 선언·지급 일자](https://www.sec.gov/Archives/edgar/data/1260221/000126022125000078/exhibit991tdg2025q4earning.htm)

---

*작성일: 2026-08-26*
