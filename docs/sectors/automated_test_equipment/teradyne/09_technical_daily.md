# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API(Yahoo Finance)에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 겹치는 시점의 종가를 대조한 결과: `2025-12-31`(FY2025 회계연도 말) 종가 $193.56은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md) §2에 인용된 값과 **일치**한다. `2026-08-14` 종가 $418.79도 [개요](./01_overview.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 현재주가와 **일치**한다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="ter-chart">
<style>
.ter-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ter-chart svg { width:100%; height:auto; display:block; }
.ter-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ter-chart .title { fill: var(--ink); font-weight:600; }
.ter-chart .grid { stroke: var(--grid); stroke-width:1; }
.ter-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Teradyne(TER) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Teradyne (TER) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $418.79 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="612.1" x2="1052" y2="612.1" class="grid"/>
<text x="52" y="616.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="473.1" x2="1052" y2="473.1" class="grid"/>
<text x="52" y="477.1" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="334.0" x2="1052" y2="334.0" class="grid"/>
<text x="52" y="338.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="195.0" x2="1052" y2="195.0" class="grid"/>
<text x="52" y="199.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
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
<line x1="524.4" y1="56.0" x2="524.4" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="530.4" y="68.0" font-size="10.5" fill="var(--down)">2026-02-03 FY2025 4분기 실적 서프라이즈</text>
<line x1="757.6" y1="56.0" x2="757.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="763.6" y="68.0" font-size="10.5" fill="var(--down)">2026-04-29 Q1 2026 실적 호조에도 보수적 가이던스로 급락</text>
<line x1="62.0" y1="595.9" x2="62.0" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="595.9" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="65.9" y1="596.7" x2="65.9" y2="598.9" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="597.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="594.5" x2="69.9" y2="598.9" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="597.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="73.8" y1="596.5" x2="73.8" y2="603.3" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="598.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="77.8" y1="598.2" x2="77.8" y2="601.2" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="599.2" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="81.7" y1="588.2" x2="81.7" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="590.8" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="85.7" y1="587.5" x2="85.7" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="588.4" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="89.6" y1="584.5" x2="89.6" y2="588.9" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="586.2" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="93.6" y1="586.1" x2="93.6" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="586.1" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="97.5" y1="586.1" x2="97.5" y2="588.5" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="587.2" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="101.5" y1="584.0" x2="101.5" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="585.1" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="105.5" y1="582.8" x2="105.5" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="583.4" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="109.4" y1="581.3" x2="109.4" y2="586.5" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="583.2" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="113.4" y1="584.3" x2="113.4" y2="589.9" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="585.1" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="117.3" y1="579.5" x2="117.3" y2="585.2" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="584.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="121.3" y1="582.5" x2="121.3" y2="587.6" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="584.0" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="125.2" y1="584.3" x2="125.2" y2="591.7" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="585.7" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="129.2" y1="586.9" x2="129.2" y2="593.9" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="587.3" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="133.1" y1="586.0" x2="133.1" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="587.3" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="137.1" y1="591.0" x2="137.1" y2="598.8" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="591.2" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="141.0" y1="592.2" x2="141.0" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="592.5" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="145.0" y1="590.4" x2="145.0" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="592.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="148.9" y1="589.4" x2="148.9" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="592.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="152.9" y1="584.9" x2="152.9" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="585.9" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="156.8" y1="583.5" x2="156.8" y2="587.7" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="584.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="160.8" y1="562.8" x2="160.8" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="563.2" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="164.7" y1="558.9" x2="164.7" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="562.0" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="168.7" y1="563.9" x2="168.7" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="564.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="172.6" y1="566.0" x2="172.6" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="566.4" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="176.6" y1="562.1" x2="176.6" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="563.0" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="180.5" y1="560.3" x2="180.5" y2="565.5" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="560.5" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="184.5" y1="559.1" x2="184.5" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="559.8" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="188.4" y1="554.3" x2="188.4" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="554.9" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="192.4" y1="549.0" x2="192.4" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="549.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="196.4" y1="543.3" x2="196.4" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="547.5" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="200.3" y1="541.6" x2="200.3" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="545.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="204.3" y1="542.2" x2="204.3" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="543.9" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="208.2" y1="549.7" x2="208.2" y2="556.2" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="550.1" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="212.2" y1="548.9" x2="212.2" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="549.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="216.1" y1="545.4" x2="216.1" y2="568.0" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="548.4" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="220.1" y1="556.6" x2="220.1" y2="561.2" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="557.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="224.0" y1="558.0" x2="224.0" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="560.7" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="228.0" y1="554.5" x2="228.0" y2="559.7" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="555.1" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="231.9" y1="552.2" x2="231.9" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="553.7" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="235.9" y1="556.9" x2="235.9" y2="561.0" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="559.0" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="239.8" y1="554.5" x2="239.8" y2="558.3" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="555.3" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="243.8" y1="550.5" x2="243.8" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="551.9" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="247.7" y1="552.6" x2="247.7" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="554.4" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="251.7" y1="548.0" x2="251.7" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="549.5" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="255.6" y1="544.0" x2="255.6" y2="550.8" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="546.0" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="259.6" y1="542.5" x2="259.6" y2="547.2" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="545.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="263.5" y1="545.9" x2="263.5" y2="550.8" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="546.7" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="267.5" y1="504.7" x2="267.5" y2="525.7" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="509.3" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="271.4" y1="502.0" x2="271.4" y2="512.4" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="505.2" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="275.4" y1="492.7" x2="275.4" y2="503.7" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="498.4" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="279.3" y1="494.5" x2="279.3" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="496.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="283.3" y1="497.7" x2="283.3" y2="507.7" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="506.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="287.3" y1="488.4" x2="287.3" y2="505.7" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="490.3" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="291.2" y1="484.8" x2="291.2" y2="496.9" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="490.1" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="295.2" y1="497.4" x2="295.2" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="497.7" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="299.1" y1="488.7" x2="299.1" y2="499.9" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="489.2" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="303.1" y1="496.2" x2="303.1" y2="506.9" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="496.2" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="307.0" y1="499.1" x2="307.0" y2="504.8" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="500.6" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="311.0" y1="505.0" x2="311.0" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="506.1" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="314.9" y1="509.5" x2="314.9" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="514.8" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="318.9" y1="510.1" x2="318.9" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="516.9" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="322.8" y1="518.5" x2="322.8" y2="524.5" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="521.0" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="326.8" y1="514.2" x2="326.8" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="517.2" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="330.7" y1="509.5" x2="330.7" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="511.6" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="334.7" y1="527.8" x2="334.7" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="530.2" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="338.6" y1="518.1" x2="338.6" y2="529.4" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="520.4" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="342.6" y1="517.4" x2="342.6" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="518.0" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="346.5" y1="499.6" x2="346.5" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="501.7" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="350.5" y1="497.9" x2="350.5" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="498.3" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="354.4" y1="496.9" x2="354.4" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="501.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="358.4" y1="484.9" x2="358.4" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="487.1" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="362.3" y1="478.4" x2="362.3" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="479.9" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="366.3" y1="471.9" x2="366.3" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="475.0" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="370.2" y1="468.7" x2="370.2" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="472.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="374.2" y1="466.1" x2="374.2" y2="471.0" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="468.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="378.2" y1="470.5" x2="378.2" y2="475.9" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="472.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="382.1" y1="466.5" x2="382.1" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="467.5" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="386.1" y1="467.5" x2="386.1" y2="478.7" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="467.6" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="390.0" y1="469.9" x2="390.0" y2="484.4" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="471.3" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="394.0" y1="472.4" x2="394.0" y2="482.0" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="473.2" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="397.9" y1="479.5" x2="397.9" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="480.9" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="401.9" y1="480.6" x2="401.9" y2="497.9" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="481.4" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="405.8" y1="479.9" x2="405.8" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="483.5" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="409.8" y1="478.0" x2="409.8" y2="484.9" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="479.8" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="413.7" y1="470.3" x2="413.7" y2="477.4" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="471.6" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="417.7" y1="474.0" x2="417.7" y2="479.2" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="475.2" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="421.6" y1="473.6" x2="421.6" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="475.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="425.6" y1="473.8" x2="425.6" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="474.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="429.5" y1="474.3" x2="429.5" y2="479.2" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="476.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="433.5" y1="475.6" x2="433.5" y2="480.0" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="475.8" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="437.4" y1="475.4" x2="437.4" y2="482.2" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="476.2" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="441.4" y1="460.8" x2="441.4" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="462.6" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="445.3" y1="442.5" x2="445.3" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="446.0" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="449.3" y1="431.8" x2="449.3" y2="445.8" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="433.0" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="453.2" y1="435.9" x2="453.2" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="437.5" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="457.2" y1="443.3" x2="457.2" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="443.3" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="461.1" y1="446.1" x2="461.1" y2="451.3" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="449.1" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="465.1" y1="436.6" x2="465.1" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="439.2" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="469.1" y1="430.9" x2="469.1" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="432.4" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="473.0" y1="429.8" x2="473.0" y2="438.9" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="431.1" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="477.0" y1="419.0" x2="477.0" y2="434.9" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="422.8" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="480.9" y1="428.5" x2="480.9" y2="437.4" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="431.9" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="484.9" y1="432.7" x2="484.9" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="439.7" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="488.8" y1="424.6" x2="488.8" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="428.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="492.8" y1="420.2" x2="492.8" y2="436.5" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="420.5" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="496.7" y1="431.1" x2="496.7" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="432.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="500.7" y1="424.3" x2="500.7" y2="435.5" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="428.9" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="504.6" y1="417.4" x2="504.6" y2="423.8" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="418.9" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="508.6" y1="402.0" x2="508.6" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="402.9" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="512.5" y1="398.5" x2="512.5" y2="417.9" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="401.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="516.5" y1="396.3" x2="516.5" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="405.8" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="520.4" y1="397.1" x2="520.4" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="404.2" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="524.4" y1="353.5" x2="524.4" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="357.7" width="2.45" height="34.5" fill="var(--up)"/>
<line x1="528.3" y1="340.3" x2="528.3" y2="385.2" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="356.7" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="532.3" y1="359.9" x2="532.3" y2="386.5" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="374.2" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="536.2" y1="332.1" x2="536.2" y2="360.5" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="333.9" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="540.2" y1="311.1" x2="540.2" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="320.1" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="544.1" y1="317.6" x2="544.1" y2="334.8" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="320.1" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="548.1" y1="298.9" x2="548.1" y2="318.9" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="304.2" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="552.0" y1="295.1" x2="552.0" y2="323.5" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="299.7" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="556.0" y1="308.8" x2="556.0" y2="330.6" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="313.7" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="560.0" y1="311.8" x2="560.0" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="325.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="563.9" y1="303.8" x2="563.9" y2="327.6" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="313.4" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="567.9" y1="308.7" x2="567.9" y2="321.6" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="311.9" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="571.8" y1="296.5" x2="571.8" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="299.5" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="575.8" y1="301.4" x2="575.8" y2="319.5" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="307.2" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="579.7" y1="289.0" x2="579.7" y2="311.0" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="293.6" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="583.7" y1="273.3" x2="583.7" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="274.5" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="587.6" y1="271.6" x2="587.6" y2="294.4" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="273.2" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="591.6" y1="299.3" x2="591.6" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="300.7" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="595.5" y1="298.0" x2="595.5" y2="320.0" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="298.1" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="599.5" y1="318.7" x2="599.5" y2="340.5" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="322.2" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="603.4" y1="313.2" x2="603.4" y2="333.4" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="318.1" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="607.4" y1="319.7" x2="607.4" y2="345.3" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="326.3" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="611.3" y1="340.9" x2="611.3" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="343.6" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="615.3" y1="339.0" x2="615.3" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="339.0" width="2.45" height="43.2" fill="var(--up)"/>
<line x1="619.2" y1="320.4" x2="619.2" y2="341.1" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="333.0" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="623.2" y1="316.5" x2="623.2" y2="334.7" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="331.3" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="627.1" y1="339.3" x2="627.1" y2="356.8" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="340.3" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="631.1" y1="340.2" x2="631.1" y2="355.5" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="348.0" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="635.0" y1="327.1" x2="635.0" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="336.5" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="639.0" y1="334.5" x2="639.0" y2="350.1" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="334.9" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="642.9" y1="323.2" x2="642.9" y2="338.9" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="329.6" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="646.9" y1="328.1" x2="646.9" y2="357.0" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="330.7" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="650.9" y1="329.9" x2="650.9" y2="355.1" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="331.1" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="654.8" y1="313.9" x2="654.8" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="328.6" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="658.8" y1="295.9" x2="658.8" y2="336.8" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="306.0" width="2.45" height="28.0" fill="var(--up)"/>
<line x1="662.7" y1="298.2" x2="662.7" y2="315.3" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="299.3" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="666.7" y1="313.2" x2="666.7" y2="338.7" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="313.2" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="670.6" y1="330.7" x2="670.6" y2="343.5" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="340.2" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="674.6" y1="332.7" x2="674.6" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="332.7" width="2.45" height="34.3" fill="var(--down)"/>
<line x1="678.5" y1="337.7" x2="678.5" y2="364.7" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="339.0" width="2.45" height="25.2" fill="var(--up)"/>
<line x1="682.5" y1="310.7" x2="682.5" y2="333.6" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="317.1" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="686.4" y1="315.3" x2="686.4" y2="348.0" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="320.7" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="690.4" y1="312.0" x2="690.4" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="312.6" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="694.3" y1="305.0" x2="694.3" y2="320.7" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="305.6" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="698.3" y1="252.5" x2="698.3" y2="278.4" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="253.0" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="702.2" y1="237.2" x2="702.2" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="244.8" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="706.2" y1="232.6" x2="706.2" y2="243.0" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="235.4" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="710.1" y1="236.1" x2="710.1" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="236.6" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="714.1" y1="236.7" x2="714.1" y2="247.2" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="241.5" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="718.0" y1="239.2" x2="718.0" y2="261.8" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="243.7" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="722.0" y1="237.7" x2="722.0" y2="253.2" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="242.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="725.9" y1="220.8" x2="725.9" y2="235.2" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="222.3" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="729.9" y1="215.9" x2="729.9" y2="232.6" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="219.1" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="733.8" y1="212.5" x2="733.8" y2="228.5" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="222.9" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="737.8" y1="207.8" x2="737.8" y2="227.9" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="210.5" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="741.8" y1="188.3" x2="741.8" y2="209.8" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="193.6" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="745.7" y1="164.3" x2="745.7" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="169.9" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="749.7" y1="165.2" x2="749.7" y2="209.9" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="165.2" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="753.6" y1="200.1" x2="753.6" y2="230.2" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="210.3" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="757.6" y1="285.4" x2="757.6" y2="331.5" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="313.8" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="761.5" y1="259.6" x2="761.5" y2="296.9" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="273.6" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="765.5" y1="259.0" x2="765.5" y2="283.1" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="270.9" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="769.4" y1="264.8" x2="769.4" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="272.3" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="773.4" y1="242.1" x2="773.4" y2="271.4" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="254.7" width="2.45" height="16.0" fill="var(--up)"/>
<line x1="777.3" y1="218.7" x2="777.3" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="219.4" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="781.3" y1="224.2" x2="781.3" y2="270.7" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="224.9" width="2.45" height="34.0" fill="var(--down)"/>
<line x1="785.2" y1="239.7" x2="785.2" y2="258.6" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="240.9" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="789.2" y1="240.2" x2="789.2" y2="258.6" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="241.4" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="793.1" y1="250.9" x2="793.1" y2="278.1" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="252.8" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="797.1" y1="241.0" x2="797.1" y2="264.5" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="241.9" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="801.0" y1="243.7" x2="801.0" y2="259.5" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="247.9" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="805.0" y1="269.3" x2="805.0" y2="284.9" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="279.0" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="808.9" y1="275.6" x2="808.9" y2="312.3" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="281.4" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="812.9" y1="299.0" x2="812.9" y2="321.0" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="304.1" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="816.8" y1="272.2" x2="816.8" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="272.4" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="820.8" y1="251.4" x2="820.8" y2="273.8" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="259.8" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="824.7" y1="250.2" x2="824.7" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="252.8" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="828.7" y1="208.4" x2="828.7" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="210.1" width="2.45" height="24.3" fill="var(--up)"/>
<line x1="832.7" y1="185.8" x2="832.7" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="192.1" width="2.45" height="36.6" fill="var(--down)"/>
<line x1="836.6" y1="214.1" x2="836.6" y2="243.9" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="219.1" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="840.6" y1="213.1" x2="840.6" y2="239.4" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="215.7" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="844.5" y1="227.4" x2="844.5" y2="250.4" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="237.5" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="848.5" y1="204.9" x2="848.5" y2="242.6" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="205.3" width="2.45" height="30.4" fill="var(--up)"/>
<line x1="852.4" y1="166.4" x2="852.4" y2="203.9" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="181.6" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="856.4" y1="175.7" x2="856.4" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="185.5" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="860.3" y1="204.9" x2="860.3" y2="258.8" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="209.6" width="2.45" height="43.9" fill="var(--down)"/>
<line x1="864.3" y1="222.6" x2="864.3" y2="238.9" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="225.8" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="868.2" y1="201.1" x2="868.2" y2="278.0" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="213.7" width="2.45" height="24.2" fill="var(--down)"/>
<line x1="872.2" y1="230.0" x2="872.2" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="250.3" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="876.1" y1="220.7" x2="876.1" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="220.9" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="880.1" y1="183.9" x2="880.1" y2="222.8" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="190.6" width="2.45" height="29.6" fill="var(--up)"/>
<line x1="884.0" y1="142.5" x2="884.0" y2="163.0" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="150.0" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="888.0" y1="144.6" x2="888.0" y2="182.2" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="150.2" width="2.45" height="31.8" fill="var(--down)"/>
<line x1="891.9" y1="138.4" x2="891.9" y2="183.6" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="154.4" width="2.45" height="28.7" fill="var(--down)"/>
<line x1="895.9" y1="140.1" x2="895.9" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="142.3" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="899.8" y1="112.7" x2="899.8" y2="140.0" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="115.8" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="903.8" y1="155.2" x2="903.8" y2="182.8" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="167.1" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="907.7" y1="149.1" x2="907.7" y2="175.9" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="157.2" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="911.7" y1="94.4" x2="911.7" y2="157.4" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="95.0" width="2.45" height="25.0" fill="var(--up)"/>
<line x1="915.6" y1="116.8" x2="915.6" y2="163.0" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="120.3" width="2.45" height="23.5" fill="var(--down)"/>
<line x1="919.6" y1="98.9" x2="919.6" y2="174.3" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="107.1" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="923.6" y1="72.8" x2="923.6" y2="111.6" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="78.5" width="2.45" height="22.7" fill="var(--up)"/>
<line x1="927.5" y1="106.5" x2="927.5" y2="160.1" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="110.2" width="2.45" height="46.8" fill="var(--down)"/>
<line x1="931.5" y1="153.7" x2="931.5" y2="247.8" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="156.9" width="2.45" height="81.1" fill="var(--down)"/>
<line x1="935.4" y1="195.3" x2="935.4" y2="226.8" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="213.7" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="939.4" y1="249.2" x2="939.4" y2="294.7" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="258.9" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="943.3" y1="258.6" x2="943.3" y2="285.3" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="262.4" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="947.3" y1="215.9" x2="947.3" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="223.9" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="951.2" y1="247.1" x2="951.2" y2="271.5" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="251.2" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="955.2" y1="266.5" x2="955.2" y2="286.3" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="271.5" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="959.1" y1="243.7" x2="959.1" y2="268.5" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="245.7" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="963.1" y1="253.4" x2="963.1" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="255.8" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="967.0" y1="284.8" x2="967.0" y2="309.4" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="289.2" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="971.0" y1="291.4" x2="971.0" y2="338.5" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="303.0" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="974.9" y1="262.8" x2="974.9" y2="290.6" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="285.1" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="978.9" y1="224.0" x2="978.9" y2="256.2" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="231.1" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="982.8" y1="227.9" x2="982.8" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="237.5" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="986.8" y1="224.9" x2="986.8" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="231.5" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="990.7" y1="234.8" x2="990.7" y2="270.8" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="243.7" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="994.7" y1="257.2" x2="994.7" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="264.6" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="998.6" y1="300.7" x2="998.6" y2="332.7" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="305.3" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="1002.6" y1="233.6" x2="1002.6" y2="307.4" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="239.7" width="2.45" height="67.4" fill="var(--down)"/>
<line x1="1006.5" y1="238.1" x2="1006.5" y2="272.2" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="243.0" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="1010.5" y1="206.1" x2="1010.5" y2="247.5" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="218.7" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="1014.5" y1="236.2" x2="1014.5" y2="265.5" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="242.6" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="1018.4" y1="181.5" x2="1018.4" y2="218.8" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="190.1" width="2.45" height="20.8" fill="var(--up)"/>
<line x1="1022.4" y1="182.0" x2="1022.4" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="191.6" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="1026.3" y1="199.8" x2="1026.3" y2="236.7" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="216.0" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="1030.3" y1="198.4" x2="1030.3" y2="232.8" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="198.4" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="1034.2" y1="213.1" x2="1034.2" y2="244.7" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="213.6" width="2.45" height="30.0" fill="var(--down)"/>
<line x1="1038.2" y1="212.0" x2="1038.2" y2="235.1" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="223.4" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="1042.1" y1="183.1" x2="1042.1" y2="204.5" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="191.2" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="1046.1" y1="164.0" x2="1046.1" y2="197.8" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="180.4" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="1050.0" y1="168.6" x2="1050.0" y2="197.2" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="168.9" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="60" y1="165.3" x2="1052" y2="165.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="168.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$421 R1</text>
<text x="1058" y="180.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="334.2" x2="1052" y2="334.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="328.2" font-size="11.5" fill="var(--support)" font-weight="600">$300 S1</text>
<text x="1058" y="340.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="168.9" r="3" fill="var(--ink)"/>
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
| R1 | $421 | 2 | 2026년 4월(4/24)·6월(6/3) 스윙 고점 — 두 차례 큰 폭 조정 이후 반등 상단 |
| **현재가** | **$418.79** (2026-08-14 종가) | — | R1 바로 아래 |
| S1 | $300 | 3 | 2026년 4월(4/29, 실적 서프라이즈에도 급락한 날의 저점)·7월(7/17·7/28) 반복 형성된 지지대 |

> 이 회사는 최근 1년간 52주 최고($487.91)~최저($106.30)까지 가격이 약 4.6배 벌어질 만큼 극단적으로 변동성이 컸다 — AI 반도체 사이클 기대와 실제 실적·가이던스 사이의 간극이 반복적으로 가격에 충격을 준 결과다(§3 참고). 그만큼 유효 클러스터(터치 2회 이상)가 현재가 근처에 R1·S1 단 2개만 남았다 — 스윙이 너무 넓은 밴드에 흩어져 있어 스크립트 기본값(3개)만큼 채우지 못했다. 억지로 레벨을 추가하지 않았다.

---

## 3. 관측된 특이 구간

### 3-A. 2026-02-03 — FY2025 4분기 실적 서프라이즈

- 2026-02-02(월) 장 마감 후 FY2025 4분기·연간 실적 발표 — 매출 $1,083M, Non-GAAP EPS $1.80로 가이던스 상단을 상회([최근 뉴스 / 이슈](./08_news.md) 참고).
- 종가 기준 2026-02-02 $249.53 → 2026-02-03 $282.98로 **+13.4%** 급등, 거래량은 1,180만 주로 직전 20거래일 평균(약 368만 주) 대비 약 3.2배.
- 이 갭 이후 주가는 2월~3월 한동안 $260~$300 박스권에서 등락하다, 4월 말 Q1 실적 발표를 계기로 한 단계 더 뛰어올랐다(§3-B).

### 3-B. 2026-04-29 — Q1 2026 실적 호조에도 보수적 가이던스로 급락("셀 더 뉴스")

- 2026-04-28(화) 장 마감 후 발표된 Q1 FY2026 실적은 매출 +87% YoY, Non-GAAP EPS $2.56(컨센서스 $2.11 상회)로 뚜렷한 서프라이즈였다. 그럼에도 다음 거래일 주가는 급락했다 — 컨센서스 대비 보수적인 향후 가이던스, 반도체 업종 전반의 거시 불확실성, 연초 급등 이후 차익실현이 복합적으로 작용한 "셀 더 뉴스(sell the news)" 반응으로 보도됐다([최근 뉴스 / 이슈](./08_news.md), 하단 출처 참고).
- 종가 기준 2026-04-28 $380.13 → 2026-04-29 $306.33로 **−19.4%** 급락, 거래량은 1,307만 주로 직전 20거래일 평균 대비 약 3.5배(최근 1년 중 최대 거래량 구간).
- 이날 저가($301.86)는 이후 7월 두 차례(7/17, 7/28) 재차 터치되며 S1($300) 지지대로 굳어졌다 — 실적 서프라이즈에도 불구한 하루의 급락이 오히려 이후 몇 달간의 지지선을 만든 역설적인 사례다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영 — 조사 기간 내 분할 없음, 배당은 미반영이나 배당수익률이 0.12%로 미미해 배당락 영향은 무시할 만한 수준)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py TER --name Teradyne --event 2026-02-03:"FY2025 4분기 실적 서프라이즈" --event 2026-04-29:"Q1 2026 실적 호조에도 보수적 가이던스로 급락" --close-on 2025-12-31 --close-on 2026-08-13 --emit all`. 파라미터는 회사 간 비교가 가능하도록 스크립트 기본값 그대로 사용(강제 레벨 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 최근 1년간 두 차례의 정보 이벤트(§3-A·3-B)로 가격 레짐이 반복적으로 단절됐다 — 특히 §3-B는 "실적 호재=주가 상승"이라는 단순 도식이 통하지 않은 사례로, 이 회사가 얼마나 가이던스·거시 심리에 민감한지 보여준다.
    - 조사 기간(2025-08~2026-08) 내 주식분할·유상증자는 없었다.

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

- [Yahoo Finance — Teradyne, Inc. (TER) 일봉 시세](https://finance.yahoo.com/quote/TER/history/)
- [stockanalysis.com — Teradyne 주가 이력 API 교차 확인](https://stockanalysis.com/stocks/TER/history/)
- [The Motley Fool — Why Teradyne Tumbled Today (2026-04-29)](https://www.fool.com/investing/2026/04/29/why-teradyne-tumbled-today/)

---

*작성일: 2026-08-16*
