# Centrus Energy — 기술적 분석 (주봉 캔들차트 · 지지/저항, 5년)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 최근 1년 세부 흐름은 [`09_technical_daily.md`](./09_technical_daily.md)(일봉·1년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, Yahoo Finance 주봉 API에서 직접 수집한 것이다. **겹치는 시점 종가 대조**: 2026-08-18 종가는 이 문서 기준 $175.70(Yahoo Finance), `04_metrics.md`·`06_valuation.md`가 인용한 stockanalysis.com 기준과 정확히 일치.
>
> ⚠️ 5년 구간(2021-08~2026-08) 안에 주식분할은 없었다(10-K 확인, 소급조정 불필요). 다만 2025년 대규모 유상증자·전환사채 발행(`04_metrics.md` 참고)이 있어, 이 기간 가격 변동에는 순수 펀더멘털 외 대규모 신주 물량 소화 등 수급 요인도 섞여 있을 수 있다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-18)

<div class="leu-chart">
<style>
.leu-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .leu-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .leu-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.leu-chart svg { width:100%; height:auto; display:block; }
.leu-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.leu-chart .title { fill: var(--ink); font-weight:600; }
.leu-chart .grid { stroke: var(--grid); stroke-width:1; }
.leu-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Centrus Energy(LEU) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Centrus Energy (LEU) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-18 · 마지막 종가 $175.70 (2026-08-18) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="507.2" x2="1052" y2="507.2" class="grid"/>
<text x="52" y="511.2" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="388.5" x2="1052" y2="388.5" class="grid"/>
<text x="52" y="392.5" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="269.8" x2="1052" y2="269.8" class="grid"/>
<text x="52" y="273.8" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="151.0" x2="1052" y2="151.0" class="grid"/>
<text x="52" y="155.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.3" y1="626.0" x2="137.3" y2="631.0" class="axis"/>
<text x="137.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="333.5" y1="626.0" x2="333.5" y2="631.0" class="axis"/>
<text x="333.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="529.6" y1="626.0" x2="529.6" y2="631.0" class="axis"/>
<text x="529.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="729.5" y1="626.0" x2="729.5" y2="631.0" class="axis"/>
<text x="729.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.6" y1="626.0" x2="925.6" y2="631.0" class="axis"/>
<text x="925.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="925.6" y1="56.0" x2="925.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="931.6" y="68.0" font-size="10.5" fill="var(--down)">2026-01-05 DOE $900M HALEU 증설 계약 발표</text>
<line x1="61.9" y1="596.4" x2="61.9" y2="599.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="598.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="595.8" x2="65.7" y2="598.3" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="596.3" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="69.4" y1="587.2" x2="69.4" y2="596.3" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="588.5" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="73.2" y1="585.0" x2="73.2" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="585.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="77.0" y1="578.6" x2="77.0" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="582.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="80.7" y1="582.6" x2="80.7" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="583.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="84.5" y1="576.5" x2="84.5" y2="583.5" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="576.9" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="88.3" y1="576.3" x2="88.3" y2="582.6" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="576.9" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="92.1" y1="561.0" x2="92.1" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="567.3" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="95.8" y1="557.4" x2="95.8" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="566.7" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="99.6" y1="558.7" x2="99.6" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="558.7" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="103.4" y1="531.9" x2="103.4" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="549.8" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="107.1" y1="520.5" x2="107.1" y2="548.4" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="524.4" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="110.9" y1="522.1" x2="110.9" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="528.4" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="114.7" y1="547.0" x2="114.7" y2="561.7" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="551.7" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="118.5" y1="550.7" x2="118.5" y2="569.5" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="554.5" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="122.2" y1="553.4" x2="122.2" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="557.2" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="126.0" y1="557.4" x2="126.0" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="557.6" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="129.8" y1="560.1" x2="129.8" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="562.0" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="133.6" y1="561.4" x2="133.6" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="562.0" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="137.3" y1="557.5" x2="137.3" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="564.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="141.1" y1="563.7" x2="141.1" y2="572.9" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="564.1" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="144.9" y1="570.7" x2="144.9" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="572.2" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="148.6" y1="570.7" x2="148.6" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="578.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="152.4" y1="572.3" x2="152.4" y2="579.6" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="575.9" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="156.2" y1="567.9" x2="156.2" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="573.4" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="160.0" y1="571.4" x2="160.0" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="573.7" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="163.7" y1="577.2" x2="163.7" y2="585.2" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="577.6" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="167.5" y1="569.8" x2="167.5" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="577.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="171.3" y1="559.8" x2="171.3" y2="579.3" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="576.5" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="175.0" y1="579.3" x2="175.0" y2="591.3" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="579.9" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="178.8" y1="579.1" x2="178.8" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="582.9" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="182.6" y1="582.9" x2="182.6" y2="588.9" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="584.9" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="186.4" y1="584.1" x2="186.4" y2="591.4" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="586.3" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="190.1" y1="587.3" x2="190.1" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="587.4" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="193.9" y1="582.4" x2="193.9" y2="591.1" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="586.8" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="197.7" y1="589.7" x2="197.7" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="591.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="201.4" y1="589.7" x2="201.4" y2="601.9" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="593.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="205.2" y1="595.1" x2="205.2" y2="605.4" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="595.1" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="209.0" y1="595.1" x2="209.0" y2="601.0" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="598.0" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="212.8" y1="595.3" x2="212.8" y2="599.9" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="595.6" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="216.5" y1="592.6" x2="216.5" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="594.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="220.3" y1="584.5" x2="220.3" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="590.2" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="224.1" y1="590.5" x2="224.1" y2="596.4" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="592.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="227.8" y1="590.8" x2="227.8" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="591.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="231.6" y1="589.9" x2="231.6" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="591.4" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="235.4" y1="592.4" x2="235.4" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="593.2" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="239.2" y1="592.2" x2="239.2" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="592.8" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="242.9" y1="588.5" x2="242.9" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="592.0" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="246.7" y1="586.2" x2="246.7" y2="594.2" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="586.6" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="250.5" y1="579.7" x2="250.5" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="579.9" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="254.3" y1="571.4" x2="254.3" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="574.3" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="258.0" y1="574.3" x2="258.0" y2="582.4" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="574.3" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="261.8" y1="569.7" x2="261.8" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="574.8" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="265.6" y1="563.7" x2="265.6" y2="576.1" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="569.8" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="269.3" y1="560.7" x2="269.3" y2="571.0" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="561.2" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="273.1" y1="560.0" x2="273.1" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="560.5" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="276.9" y1="572.0" x2="276.9" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="573.5" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="280.7" y1="574.4" x2="280.7" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="577.3" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="284.4" y1="573.6" x2="284.4" y2="580.5" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="576.1" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="288.2" y1="579.1" x2="288.2" y2="585.9" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="579.2" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="292.0" y1="575.1" x2="292.0" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="575.2" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="295.7" y1="570.1" x2="295.7" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="570.1" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="299.5" y1="568.7" x2="299.5" y2="576.9" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="569.5" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="303.3" y1="570.2" x2="303.3" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="574.1" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="307.1" y1="576.5" x2="307.1" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="579.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="310.8" y1="579.6" x2="310.8" y2="582.5" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="580.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="314.6" y1="579.8" x2="314.6" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="580.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="318.4" y1="580.3" x2="318.4" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="580.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="322.1" y1="583.5" x2="322.1" y2="587.4" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="586.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="325.9" y1="586.2" x2="325.9" y2="589.4" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="586.7" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="329.7" y1="586.6" x2="329.7" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="587.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="333.5" y1="584.7" x2="333.5" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="585.0" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="337.2" y1="581.9" x2="337.2" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="582.1" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="341.0" y1="581.4" x2="341.0" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="582.6" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="344.8" y1="576.8" x2="344.8" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="577.7" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="348.5" y1="574.0" x2="348.5" y2="578.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="577.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="352.3" y1="576.5" x2="352.3" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="576.5" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="356.1" y1="565.8" x2="356.1" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="575.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="359.9" y1="565.2" x2="359.9" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="568.2" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="363.6" y1="567.7" x2="363.6" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="567.8" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="367.4" y1="575.2" x2="367.4" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="575.3" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="371.2" y1="581.8" x2="371.2" y2="588.4" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="582.3" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="375.0" y1="585.1" x2="375.0" y2="590.1" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="586.6" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="378.7" y1="586.7" x2="378.7" y2="588.7" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="587.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="382.5" y1="586.7" x2="382.5" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="587.4" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="386.3" y1="587.1" x2="386.3" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="588.5" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="390.0" y1="588.2" x2="390.0" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="588.5" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="393.8" y1="591.0" x2="393.8" y2="593.5" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="591.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="397.6" y1="591.2" x2="397.6" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="591.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="401.4" y1="587.3" x2="401.4" y2="593.0" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="589.5" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="405.1" y1="588.2" x2="405.1" y2="590.0" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="589.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="408.9" y1="587.0" x2="408.9" y2="590.6" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="589.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="412.7" y1="589.4" x2="412.7" y2="596.5" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="590.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="416.4" y1="586.7" x2="416.4" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="587.8" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="420.2" y1="583.2" x2="420.2" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="584.0" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="424.0" y1="582.8" x2="424.0" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="584.3" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="427.8" y1="586.4" x2="427.8" y2="589.1" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="587.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="431.5" y1="586.7" x2="431.5" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="587.3" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="435.3" y1="586.0" x2="435.3" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="588.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="439.1" y1="582.0" x2="439.1" y2="588.4" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="585.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="442.8" y1="582.2" x2="442.8" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="584.0" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="446.6" y1="574.1" x2="446.6" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="575.8" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="450.4" y1="572.2" x2="450.4" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="575.2" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="454.2" y1="575.1" x2="454.2" y2="578.3" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="575.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="457.9" y1="572.0" x2="457.9" y2="575.8" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="573.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="461.7" y1="567.4" x2="461.7" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="567.7" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="465.5" y1="564.2" x2="465.5" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="565.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="469.2" y1="561.7" x2="469.2" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="562.9" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="473.0" y1="560.4" x2="473.0" y2="567.6" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="561.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="476.8" y1="553.1" x2="476.8" y2="561.3" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="558.6" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="480.6" y1="558.3" x2="480.6" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="558.6" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="484.3" y1="560.0" x2="484.3" y2="565.4" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="560.5" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="488.1" y1="560.7" x2="488.1" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="562.5" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="491.9" y1="561.1" x2="491.9" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="565.6" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="495.7" y1="559.9" x2="495.7" y2="569.9" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="560.8" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="499.4" y1="560.0" x2="499.4" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="560.3" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="503.2" y1="562.0" x2="503.2" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="563.6" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="507.0" y1="562.8" x2="507.0" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="564.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="510.7" y1="564.7" x2="510.7" y2="568.8" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="565.5" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="514.5" y1="563.2" x2="514.5" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="565.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="518.3" y1="559.8" x2="518.3" y2="569.4" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="563.7" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="522.1" y1="556.6" x2="522.1" y2="565.3" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="561.7" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="525.8" y1="558.1" x2="525.8" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="561.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="529.6" y1="560.8" x2="529.6" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="561.3" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="533.4" y1="561.0" x2="533.4" y2="570.7" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="561.3" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="537.1" y1="558.3" x2="537.1" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="561.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="540.9" y1="558.3" x2="540.9" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="560.7" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="544.7" y1="560.7" x2="544.7" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="564.8" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="548.5" y1="562.6" x2="548.5" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="567.2" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="552.2" y1="568.3" x2="552.2" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="571.4" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="556.0" y1="574.2" x2="556.0" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="574.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="559.8" y1="575.1" x2="559.8" y2="578.7" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="576.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="563.5" y1="573.5" x2="563.5" y2="579.4" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="573.7" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="567.3" y1="577.8" x2="567.3" y2="581.1" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="577.9" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="571.1" y1="576.6" x2="571.1" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="578.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="574.9" y1="576.4" x2="574.9" y2="579.4" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="576.7" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="578.6" y1="569.2" x2="578.6" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="572.8" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="582.4" y1="571.5" x2="582.4" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="571.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="586.2" y1="573.1" x2="586.2" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="573.2" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="589.9" y1="575.2" x2="589.9" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="576.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="593.7" y1="571.0" x2="593.7" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="572.5" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="597.5" y1="570.2" x2="597.5" y2="580.6" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="572.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="601.3" y1="570.1" x2="601.3" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="570.7" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="605.0" y1="565.3" x2="605.0" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="569.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="608.8" y1="564.0" x2="608.8" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="566.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="612.6" y1="566.1" x2="612.6" y2="574.8" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="566.3" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="616.3" y1="572.3" x2="616.3" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="573.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="620.1" y1="573.5" x2="620.1" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="574.0" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="623.9" y1="572.2" x2="623.9" y2="576.5" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="574.0" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="627.7" y1="574.4" x2="627.7" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="574.4" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="631.4" y1="567.9" x2="631.4" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="568.1" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="635.2" y1="567.3" x2="635.2" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="567.3" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="639.0" y1="573.0" x2="639.0" y2="576.7" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="573.6" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="642.8" y1="573.0" x2="642.8" y2="581.8" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="575.2" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="646.5" y1="574.0" x2="646.5" y2="586.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="578.6" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="650.3" y1="577.5" x2="650.3" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="577.5" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="654.1" y1="578.1" x2="654.1" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="578.6" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="657.8" y1="578.1" x2="657.8" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="578.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="661.6" y1="579.7" x2="661.6" y2="584.5" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="580.1" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="665.4" y1="578.3" x2="665.4" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="579.1" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="669.2" y1="571.7" x2="669.2" y2="579.5" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="572.6" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="672.9" y1="557.3" x2="672.9" y2="571.5" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="557.5" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="676.7" y1="545.3" x2="676.7" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="545.5" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="680.5" y1="543.5" x2="680.5" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="543.5" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="684.2" y1="506.2" x2="684.2" y2="558.4" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="508.9" width="2.34" height="46.3" fill="var(--up)"/>
<line x1="688.0" y1="501.9" x2="688.0" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="502.5" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="691.8" y1="485.4" x2="691.8" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="495.9" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="695.6" y1="513.2" x2="695.6" y2="539.7" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="515.0" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="699.3" y1="513.2" x2="699.3" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="513.2" width="2.34" height="29.5" fill="var(--down)"/>
<line x1="703.1" y1="521.7" x2="703.1" y2="549.3" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="522.9" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="706.9" y1="516.3" x2="706.9" y2="529.3" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="517.9" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="710.6" y1="515.8" x2="710.6" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="515.8" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="714.4" y1="531.8" x2="714.4" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="532.9" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="718.2" y1="533.4" x2="718.2" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="540.0" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="722.0" y1="537.2" x2="722.0" y2="548.1" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="542.0" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="725.7" y1="528.6" x2="725.7" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="530.0" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="729.5" y1="526.0" x2="729.5" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="526.5" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="733.3" y1="532.0" x2="733.3" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="533.6" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="737.0" y1="507.8" x2="737.0" y2="532.1" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="516.8" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="740.8" y1="522.1" x2="740.8" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="526.8" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="744.6" y1="493.1" x2="744.6" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="496.7" width="2.34" height="36.7" fill="var(--up)"/>
<line x1="748.4" y1="480.0" x2="748.4" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="490.6" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="752.1" y1="488.5" x2="752.1" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="492.7" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="755.9" y1="509.6" x2="755.9" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="510.4" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="759.7" y1="515.2" x2="759.7" y2="535.8" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="516.0" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="763.5" y1="532.7" x2="763.5" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="534.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="767.2" y1="530.9" x2="767.2" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="534.9" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="771.0" y1="533.7" x2="771.0" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="535.2" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="774.8" y1="545.0" x2="774.8" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="550.3" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="778.5" y1="548.3" x2="778.5" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="549.6" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="782.3" y1="544.8" x2="782.3" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="546.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="786.1" y1="542.1" x2="786.1" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="543.4" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="789.9" y1="537.5" x2="789.9" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="538.8" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="793.6" y1="514.3" x2="793.6" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="514.9" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="797.4" y1="505.4" x2="797.4" y2="517.2" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="507.4" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="801.2" y1="485.6" x2="801.2" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="491.5" width="2.34" height="23.7" fill="var(--up)"/>
<line x1="804.9" y1="464.5" x2="804.9" y2="488.5" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="475.3" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="808.7" y1="451.6" x2="808.7" y2="479.6" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="456.1" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="812.5" y1="429.8" x2="812.5" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="433.3" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="816.3" y1="375.1" x2="816.3" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="400.3" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="820.0" y1="382.6" x2="820.0" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="390.0" width="2.34" height="35.8" fill="var(--down)"/>
<line x1="823.8" y1="407.0" x2="823.8" y2="432.1" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="417.4" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="827.6" y1="380.2" x2="827.6" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="380.9" width="2.34" height="38.5" fill="var(--up)"/>
<line x1="831.3" y1="329.8" x2="831.3" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="329.9" width="2.34" height="53.8" fill="var(--up)"/>
<line x1="835.1" y1="328.1" x2="835.1" y2="379.0" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="329.5" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="838.9" y1="333.7" x2="838.9" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="333.9" width="2.34" height="44.7" fill="var(--down)"/>
<line x1="842.7" y1="311.4" x2="842.7" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="361.0" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="846.4" y1="352.9" x2="846.4" y2="415.8" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="365.0" width="2.34" height="43.2" fill="var(--down)"/>
<line x1="850.2" y1="398.0" x2="850.2" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="404.6" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="854.0" y1="370.3" x2="854.0" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="386.4" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="857.7" y1="376.7" x2="857.7" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="382.1" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="861.5" y1="349.7" x2="861.5" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="362.2" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="865.3" y1="267.9" x2="865.3" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="276.3" width="2.34" height="85.3" fill="var(--up)"/>
<line x1="869.1" y1="224.6" x2="869.1" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="263.4" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="872.8" y1="198.3" x2="872.8" y2="270.4" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="218.1" width="2.34" height="31.8" fill="var(--up)"/>
<line x1="876.6" y1="123.4" x2="876.6" y2="223.4" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="194.1" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="880.4" y1="74.7" x2="880.4" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="133.5" width="2.34" height="41.1" fill="var(--down)"/>
<line x1="884.2" y1="140.3" x2="884.2" y2="277.1" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="151.0" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="887.9" y1="148.6" x2="887.9" y2="209.7" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="161.5" width="2.34" height="28.1" fill="var(--down)"/>
<line x1="891.7" y1="196.0" x2="891.7" y2="324.4" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="209.5" width="2.34" height="67.2" fill="var(--down)"/>
<line x1="895.5" y1="249.4" x2="895.5" y2="352.9" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="259.1" width="2.34" height="70.1" fill="var(--down)"/>
<line x1="899.2" y1="286.4" x2="899.2" y2="363.1" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="338.9" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="903.0" y1="313.0" x2="903.0" y2="350.3" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="318.1" width="2.34" height="26.5" fill="var(--up)"/>
<line x1="906.8" y1="285.0" x2="906.8" y2="331.5" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="309.9" width="2.34" height="19.3" fill="var(--up)"/>
<line x1="910.6" y1="300.6" x2="910.6" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="306.3" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="914.3" y1="310.3" x2="914.3" y2="364.5" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="315.1" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="918.1" y1="291.9" x2="918.1" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="305.1" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="921.9" y1="302.2" x2="921.9" y2="342.2" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="302.4" width="2.34" height="29.7" fill="var(--up)"/>
<line x1="925.6" y1="238.4" x2="925.6" y2="298.2" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="262.4" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="929.4" y1="230.0" x2="929.4" y2="286.4" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="232.9" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="933.2" y1="215.6" x2="933.2" y2="281.5" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="242.4" width="2.34" height="31.8" fill="var(--down)"/>
<line x1="937.0" y1="222.6" x2="937.0" y2="299.4" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="268.0" width="2.34" height="27.5" fill="var(--down)"/>
<line x1="940.7" y1="279.7" x2="940.7" y2="352.3" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="294.4" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="944.5" y1="297.2" x2="944.5" y2="408.2" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="318.1" width="2.34" height="71.4" fill="var(--down)"/>
<line x1="948.3" y1="371.4" x2="948.3" y2="403.5" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="384.1" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="952.0" y1="368.4" x2="952.0" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="385.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="955.8" y1="375.6" x2="955.8" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="396.2" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="959.6" y1="356.0" x2="959.6" y2="409.8" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="377.1" width="2.34" height="29.3" fill="var(--up)"/>
<line x1="963.4" y1="363.7" x2="963.4" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="375.8" width="2.34" height="28.4" fill="var(--down)"/>
<line x1="967.1" y1="384.9" x2="967.1" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="402.9" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="970.9" y1="401.0" x2="970.9" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="407.2" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="974.7" y1="396.6" x2="974.7" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="403.7" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="978.4" y1="376.6" x2="978.4" y2="412.2" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="384.2" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="982.2" y1="352.3" x2="982.2" y2="401.4" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="381.8" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="986.0" y1="359.1" x2="986.0" y2="401.0" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="375.8" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="989.8" y1="346.9" x2="989.8" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="379.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="993.5" y1="368.7" x2="993.5" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="382.7" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="997.3" y1="401.2" x2="997.3" y2="432.1" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="409.2" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="1001.1" y1="401.5" x2="1001.1" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="406.2" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="1004.9" y1="382.8" x2="1004.9" y2="438.4" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="416.1" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="1008.6" y1="427.5" x2="1008.6" y2="454.2" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="427.6" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="1012.4" y1="397.6" x2="1012.4" y2="429.7" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="398.7" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="1016.2" y1="398.0" x2="1016.2" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="409.7" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="1019.9" y1="414.6" x2="1019.9" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="429.5" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="1023.7" y1="412.5" x2="1023.7" y2="434.1" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="422.9" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="1027.5" y1="424.1" x2="1027.5" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="427.7" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="1031.3" y1="414.1" x2="1031.3" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="431.4" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="1035.0" y1="410.1" x2="1035.0" y2="438.5" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="415.9" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="1038.8" y1="384.7" x2="1038.8" y2="420.6" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="398.7" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="1042.6" y1="391.0" x2="1042.6" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="399.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1046.3" y1="400.4" x2="1046.3" y2="419.2" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="401.6" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="1050.1" y1="408.2" x2="1050.1" y2="419.2" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="414.8" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="60" y1="431.6" x2="1052" y2="431.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="425.6" font-size="11.5" fill="var(--support)" font-weight="600">$164 S1</text>
<text x="1058" y="437.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="455.7" x2="1052" y2="455.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="449.7" font-size="11.5" fill="var(--support)" font-weight="600">$143 S2</text>
<text x="1058" y="461.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="549.0" x2="1052" y2="549.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="543.0" font-size="11.5" fill="var(--support)" font-weight="600">$65 S3</text>
<text x="1058" y="555.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="417.4" r="3" fill="var(--ink)"/>
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

## 2. 지지/저항 레벨

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$175.70** (2026-08-18 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $164 | 2 | 2026년 상반기 조정 국면의 저점대, 현재가와 가장 근접 |
| S2 | $143 | 2 | 52주 최저($142.13, 2026년 4~5월경)와 거의 일치 |
| S3 | $65 | 2 | 2024년 말~2025년 초, HALEU 상업화·DOE 계약 모멘텀이 본격화되기 전 저점대 |

> 5년 구간 전체를 통틀어 현재가($175.70) 위쪽에는 터치 2회 이상인 저항 클러스터가 없다 — 2025년 10월 고점($464.25)까지의 상승과 이후 조정이 각각 빠르게 진행돼, 그 사이 구간이 반복적으로 재방문되지 않았기 때문으로 보인다("신고가 구간"이라는 표시는 이 5년 window 안에서 반복 저항이 형성되지 않았다는 뜻이며, 실제 최고가를 경신 중이라는 뜻이 아니다 — 현재가는 52주 최고 대비 오히려 −62% 낮은 수준). 아래쪽 지지 3개(S1~S3)는 시간순으로 최근(S1, 2026년) → 중간(S2, 2026년 초) → 과거(S3, 2024년 말~2025년 초)로 이어지는 구조다.

---

## 3. 관측된 특이 구간 — 5년간의 구조적 전환

- **2021~2024년 초 (S3 부근, $65 이하 다수 구간)**: 이 시기 주가는 대체로 낮은 박스권에서 움직였다 — 2023년 10월 HALEU 상업 생산 개시라는 산업사적 이벤트가 있었음에도 주가에 미친 즉각적 임팩트는 제한적이었던 것으로 보인다(장기 투자 스토리가 아직 시장에서 완전히 가격에 반영되지 않았던 시기).
- **2024년 말~2025년: 재평가(re-rating) 랠리 시작**: HALEU 상업화 진전과 원자력·SMR 테마 재조명이 겹치며 주가가 본격적으로 상승하기 시작해, 2025년 10월경 5년 최고 $464.25까지 도달했다.
- **2026년: 대조정과 개별 계약 뉴스**: 2026년 1월 DOE $900M HALEU 증설 계약이라는 강한 펀더멘털 호재에도 불구하고, 그 전후로 밸류에이션 부담에 따른 대규모 조정이 함께 진행돼 현재가는 이 고점 대비 −62% 낮은 수준이다 — 호재 하나로 조정을 되돌리기엔 그 전 랠리의 되돌림 폭이 훨씬 컸다는 뜻으로 해석할 수 있다(`06_valuation.md` §2·`09_technical_daily.md` §3와 같은 결론).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-16~2026-08-18. 수집 시점: 2026-08-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py LEU --name "Centrus Energy" --interval 1wk --event 2026-01-05:"DOE $900M HALEU 증설 계약 발표" --close-on 2026-08-18`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 263개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 상단 저항이 전혀 탐지되지 않은 것은 "천장이 없다"는 뜻이 아니라, 이 5년 구간에서 고가 영역이 반복 재방문되지 않았다는 모델상의 한계다 — 2025년 10월 고점 부근에서 실제로 매물이 쌓였는지는 이 모델로 판단할 수 없다.
    - 2023-10 HALEU 상업 생산 개시 이벤트는 정확한 주간 거래일 매칭에 실패해 차트에 세로선으로 표시하지 못했다(§3 서술로 대체).

---

## 관련 문서

같은 폴더 내 다른 문서로 이동:

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 일봉·1년](./09_technical_daily.md)
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — LEU 주봉 시세](https://finance.yahoo.com/quote/LEU/history/) (수집 2026-08-19)
- [stockanalysis.com — LEU 현재가·통계](https://stockanalysis.com/stocks/leu/) (04_metrics.md/06_valuation.md 대조용)

---

*작성일: 2026-08-19*
