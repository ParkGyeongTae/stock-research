# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> Circle은 2025-06-05 상장해 아직 5년 거래 이력이 없다 — 이 문서는 상장 이후 실제 거래 가능한 전체 기간(2025-06-02~2026-08-14, 64주)만 다룬다. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 최근 1년을 보여준다면, 이 문서는 **상장 직후 형성된 사상 최고가($298.99, 2025-06-23)와 그 이후의 폭락 사이클** 등 일봉 문서의 1년 창(2025-08-15~)에는 잡히지 않는 초기 구간까지 포함한다는 점에서 여전히 참고 가치가 있다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ **템플릿 예외 사유 명시**: 템플릿은 "상장 후 거래 기간이 2년 미만이면 이 문서를 만들지 말거나 기간을 실제 거래 구간으로 줄이라"고 규정한다. Circle은 상장 후 약 14개월(64주, 스크립트 최소 표본 60개를 간신히 충족)로 2년에 못 미치지만, ①표본이 최소 기준을 충족했고 ②일봉 문서가 다루지 못하는 상장 초기 국면(사상 최고가·첫 폭락)이 이 회사의 투자 판단에서 핵심적인 참고 정보라 완전히 생략하기보다 **기간을 실제 거래 구간(2025-06-02~2026-08-14)으로 줄여 작성**하는 쪽을 택했다. 표본이 짧은 만큼 아래 레벨의 신뢰도는 다른 회사 문서보다 낮게 볼 것(4. 방법론 · 한계 참고).
>
> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 주봉 API에서 직접 수집했다. 두 문서에서 겹치는 시점의 종가를 대조한 결과: 2026-08-14 종가 $71.60은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)의 동일 시점 종가와 일치(같은 스크립트·같은 원자료 출처).

---

## 1. 차트 — 상장 이후 주봉 (2025-06-02 ~ 2026-08-14)

<div class="crcl-chart">
<style>
.crcl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.crcl-chart svg { width:100%; height:auto; display:block; }
.crcl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.crcl-chart .title { fill: var(--ink); font-weight:600; }
.crcl-chart .grid { stroke: var(--grid); stroke-width:1; }
.crcl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Circle(CRCL) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Circle (CRCL) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-06-02 ~ 2026-08-14 · 마지막 종가 $71.60 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="604.9" x2="1052" y2="604.9" class="grid"/>
<text x="52" y="608.9" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="499.3" x2="1052" y2="499.3" class="grid"/>
<text x="52" y="503.3" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="393.8" x2="1052" y2="393.8" class="grid"/>
<text x="52" y="397.8" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="288.2" x2="1052" y2="288.2" class="grid"/>
<text x="52" y="292.2" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="182.7" x2="1052" y2="182.7" class="grid"/>
<text x="52" y="186.7" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="77.1" x2="1052" y2="77.1" class="grid"/>
<text x="52" y="81.1" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="67.8" y1="626.0" x2="67.8" y2="631.0" class="axis"/>
<text x="67.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="548.2" y1="626.0" x2="548.2" y2="631.0" class="axis"/>
<text x="548.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="79.2" x2="1052" y2="79.2" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="82.2" font-size="10.5" fill="var(--muted)">$299 상장 후 최고가(2025-06-23)</text>
<line x1="610.2" y1="56.0" x2="610.2" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="616.2" y="68.0" font-size="10.5" fill="var(--down)">2026-02-02 상장 후 첫 폭락 저점(고점 대비 -83.3%)</text>
<line x1="67.8" y1="449.7" x2="67.8" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="64.75" y="483.1" width="6.00" height="81.7" fill="var(--up)"/>
<line x1="83.2" y1="417.9" x2="83.2" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="80.25" y="428.5" width="6.00" height="1.8" fill="var(--up)"/>
<line x1="98.8" y1="185.0" x2="98.8" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="95.75" y="203.2" width="6.00" height="195.8" fill="var(--up)"/>
<line x1="114.2" y1="79.2" x2="114.2" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="111.25" y="207.0" width="6.00" height="122.5" fill="var(--down)"/>
<line x1="129.8" y1="300.9" x2="129.8" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="126.75" y="311.9" width="6.00" height="14.8" fill="var(--up)"/>
<line x1="145.2" y1="255.3" x2="145.2" y2="325.2" stroke="var(--down)" class="wick"/>
<rect x="142.25" y="301.4" width="6.00" height="13.6" fill="var(--down)"/>
<line x1="160.8" y1="155.3" x2="160.8" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="157.75" y="238.0" width="6.00" height="72.9" fill="var(--up)"/>
<line x1="176.2" y1="220.9" x2="176.2" y2="314.6" stroke="var(--down)" class="wick"/>
<rect x="173.25" y="232.5" width="6.00" height="70.8" fill="var(--down)"/>
<line x1="191.8" y1="292.7" x2="191.8" y2="357.3" stroke="var(--down)" class="wick"/>
<rect x="188.75" y="294.6" width="6.00" height="61.0" fill="var(--down)"/>
<line x1="207.2" y1="347.1" x2="207.2" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="204.25" y="347.1" width="6.00" height="27.6" fill="var(--down)"/>
<line x1="222.8" y1="309.5" x2="222.8" y2="422.5" stroke="var(--down)" class="wick"/>
<rect x="219.75" y="370.5" width="6.00" height="24.8" fill="var(--down)"/>
<line x1="238.2" y1="394.9" x2="238.2" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="235.25" y="396.5" width="6.00" height="28.8" fill="var(--down)"/>
<line x1="253.8" y1="423.4" x2="253.8" y2="448.3" stroke="var(--down)" class="wick"/>
<rect x="250.75" y="426.8" width="6.00" height="5.0" fill="var(--down)"/>
<line x1="269.2" y1="432.4" x2="269.2" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="266.25" y="439.0" width="6.00" height="29.6" fill="var(--down)"/>
<line x1="284.8" y1="422.3" x2="284.8" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="281.75" y="445.9" width="6.00" height="23.9" fill="var(--up)"/>
<line x1="300.2" y1="398.6" x2="300.2" y2="446.4" stroke="var(--up)" class="wick"/>
<rect x="297.25" y="406.1" width="6.00" height="30.1" fill="var(--up)"/>
<line x1="315.8" y1="411.5" x2="315.8" y2="451.1" stroke="var(--down)" class="wick"/>
<rect x="312.75" y="415.1" width="6.00" height="27.2" fill="var(--down)"/>
<line x1="331.2" y1="380.1" x2="331.2" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="328.25" y="402.7" width="6.00" height="34.4" fill="var(--up)"/>
<line x1="346.8" y1="373.8" x2="346.8" y2="430.5" stroke="var(--down)" class="wick"/>
<rect x="343.75" y="385.3" width="6.00" height="44.5" fill="var(--down)"/>
<line x1="362.2" y1="412.0" x2="362.2" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="359.25" y="419.0" width="6.00" height="24.4" fill="var(--down)"/>
<line x1="377.8" y1="406.4" x2="377.8" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="374.75" y="410.6" width="6.00" height="25.9" fill="var(--up)"/>
<line x1="393.2" y1="399.2" x2="393.2" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="390.25" y="400.3" width="6.00" height="42.1" fill="var(--down)"/>
<line x1="408.8" y1="445.0" x2="408.8" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="405.75" y="445.0" width="6.00" height="47.7" fill="var(--down)"/>
<line x1="424.2" y1="477.1" x2="424.2" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="421.25" y="482.9" width="6.00" height="54.7" fill="var(--down)"/>
<line x1="439.8" y1="537.5" x2="439.8" y2="573.4" stroke="var(--down)" class="wick"/>
<rect x="436.75" y="537.8" width="6.00" height="22.1" fill="var(--down)"/>
<line x1="455.2" y1="538.4" x2="455.2" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="452.25" y="541.7" width="6.00" height="16.7" fill="var(--up)"/>
<line x1="470.8" y1="524.1" x2="470.8" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="467.75" y="529.7" width="6.00" height="17.2" fill="var(--up)"/>
<line x1="486.2" y1="517.7" x2="486.2" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="483.25" y="526.9" width="6.00" height="7.3" fill="var(--down)"/>
<line x1="501.8" y1="528.3" x2="501.8" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="498.75" y="528.6" width="6.00" height="4.8" fill="var(--up)"/>
<line x1="517.2" y1="517.9" x2="517.2" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="514.25" y="525.2" width="6.00" height="13.7" fill="var(--down)"/>
<line x1="532.8" y1="531.9" x2="532.8" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="529.75" y="534.2" width="6.00" height="8.9" fill="var(--up)"/>
<line x1="548.2" y1="524.5" x2="548.2" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="545.25" y="531.9" width="6.00" height="3.5" fill="var(--down)"/>
<line x1="563.8" y1="523.7" x2="563.8" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="560.75" y="539.1" width="6.00" height="5.3" fill="var(--down)"/>
<line x1="579.2" y1="546.9" x2="579.2" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="576.25" y="550.6" width="6.00" height="9.2" fill="var(--down)"/>
<line x1="594.8" y1="547.9" x2="594.8" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="591.75" y="562.6" width="6.00" height="12.8" fill="var(--down)"/>
<line x1="610.2" y1="579.8" x2="610.2" y2="605.1" stroke="var(--down)" class="wick"/>
<rect x="607.25" y="580.6" width="6.00" height="9.4" fill="var(--down)"/>
<line x1="625.8" y1="579.1" x2="625.8" y2="593.7" stroke="var(--up)" class="wick"/>
<rect x="622.75" y="583.7" width="6.00" height="7.8" fill="var(--up)"/>
<line x1="641.2" y1="572.2" x2="641.2" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="638.25" y="577.4" width="6.00" height="7.9" fill="var(--up)"/>
<line x1="656.8" y1="519.2" x2="656.8" y2="584.9" stroke="var(--up)" class="wick"/>
<rect x="653.75" y="534.3" width="6.00" height="45.1" fill="var(--up)"/>
<line x1="672.2" y1="478.0" x2="672.2" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="669.25" y="495.3" width="6.00" height="44.6" fill="var(--up)"/>
<line x1="687.8" y1="449.9" x2="687.8" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="684.75" y="466.9" width="6.00" height="21.5" fill="var(--up)"/>
<line x1="703.2" y1="422.0" x2="703.2" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="700.25" y="444.4" width="6.00" height="12.4" fill="var(--up)"/>
<line x1="718.8" y1="441.3" x2="718.8" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="715.75" y="448.3" width="6.00" height="64.4" fill="var(--down)"/>
<line x1="734.2" y1="500.5" x2="734.2" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="731.25" y="507.2" width="6.00" height="12.7" fill="var(--down)"/>
<line x1="749.8" y1="495.5" x2="749.8" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="746.75" y="513.9" width="6.00" height="10.7" fill="var(--down)"/>
<line x1="765.2" y1="475.7" x2="765.2" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="762.25" y="486.9" width="6.00" height="41.3" fill="var(--up)"/>
<line x1="780.8" y1="485.6" x2="780.8" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="777.75" y="494.1" width="6.00" height="6.0" fill="var(--down)"/>
<line x1="796.2" y1="499.3" x2="796.2" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="793.25" y="500.0" width="6.00" height="2.4" fill="var(--up)"/>
<line x1="811.8" y1="451.1" x2="811.8" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="808.75" y="470.5" width="6.00" height="13.8" fill="var(--up)"/>
<line x1="827.2" y1="414.9" x2="827.2" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="824.25" y="459.5" width="6.00" height="10.2" fill="var(--down)"/>
<line x1="842.8" y1="459.5" x2="842.8" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="839.75" y="471.6" width="6.00" height="2.2" fill="var(--up)"/>
<line x1="858.2" y1="468.8" x2="858.2" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="855.25" y="471.9" width="6.00" height="1.6" fill="var(--up)"/>
<line x1="873.8" y1="479.3" x2="873.8" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="870.75" y="480.9" width="6.00" height="60.0" fill="var(--down)"/>
<line x1="889.2" y1="526.0" x2="889.2" y2="546.6" stroke="var(--down)" class="wick"/>
<rect x="886.25" y="533.1" width="6.00" height="13.0" fill="var(--down)"/>
<line x1="904.8" y1="526.1" x2="904.8" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="901.75" y="535.5" width="6.00" height="5.6" fill="var(--down)"/>
<line x1="920.2" y1="531.3" x2="920.2" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="917.25" y="538.9" width="6.00" height="16.2" fill="var(--down)"/>
<line x1="935.8" y1="549.7" x2="935.8" y2="580.0" stroke="var(--down)" class="wick"/>
<rect x="932.75" y="551.7" width="6.00" height="22.3" fill="var(--down)"/>
<line x1="951.2" y1="556.6" x2="951.2" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="948.25" y="570.8" width="6.00" height="3.3" fill="var(--up)"/>
<line x1="966.8" y1="569.3" x2="966.8" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="963.75" y="574.4" width="6.00" height="8.4" fill="var(--down)"/>
<line x1="982.2" y1="557.0" x2="982.2" y2="583.9" stroke="var(--up)" class="wick"/>
<rect x="979.25" y="578.8" width="6.00" height="3.0" fill="var(--up)"/>
<line x1="997.8" y1="570.6" x2="997.8" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="994.75" y="576.1" width="6.00" height="2.2" fill="var(--down)"/>
<line x1="1013.2" y1="566.0" x2="1013.2" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="1010.25" y="569.7" width="6.00" height="16.2" fill="var(--up)"/>
<line x1="1028.8" y1="550.2" x2="1028.8" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="1025.75" y="559.3" width="6.00" height="9.4" fill="var(--up)"/>
<line x1="1044.2" y1="552.9" x2="1044.2" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="1041.25" y="553.3" width="6.00" height="6.0" fill="var(--down)"/>
<line x1="60" y1="418.4" x2="1052" y2="418.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="421.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$138 R1</text>
<text x="1058" y="433.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="373.8" x2="1052" y2="373.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="377.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$159 R2 (2025년 10월 스윙 고점)</text>
<text x="1058" y="389.3" font-size="9.5" fill="var(--muted)">터치 1회</text>
<line x1="60" y1="573.4" x2="1052" y2="573.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="567.4" font-size="11.5" fill="var(--support)" font-weight="600">$65 S1 (2025년 11월 스윙 저점)</text>
<text x="1058" y="579.4" font-size="9.5" fill="var(--muted)">터치 1회</text>
<line x1="60" y1="605.1" x2="1052" y2="605.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="599.1" font-size="11.5" fill="var(--support)" font-weight="600">$50 S2 (상장 후 최저가, 2026년 2월)</text>
<text x="1058" y="611.1" font-size="9.5" fill="var(--muted)">터치 1회</text>
<circle cx="1052.0" cy="559.3" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다 — 둘을 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $159 | 1 | 2025년 10월(2025-10-06) 스윙 고점. 터치 1회지만 R1과 함께 상장 후 형성된 레인지 상단을 보여줘 예외 포함 |
| R1 | $138 | 2 | 2026년 3월·5월(2026-03-16·2026-05-11) 스윙 고점대 — 기술적 분석 — 일봉·1년의 레벨과 함께 최근 레짐의 상단을 보여줌 |
| **현재가** | **$71.60** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $65 | 1 | 2025년 11월(2025-11-17) 스윙 저점. 터치 1회지만 상장 후 첫 조정 국면의 저점대라 예외 포함 |
| S2 | $50 | 1 | 2026년 2월(2026-02-02) 형성된 상장 후 최저가. 터치 1회지만 3. 관측된 특이 구간 — 2026-02-02 상장 후 첫 폭락 저점이라는 구조적 의미가 커 예외 포함 |
| 참고선 | $299 | — | 상장 후 최고가(2025-06-23). 이후 두 차례(3. 관측된 특이 구간 — 2026-02-02 상장 후 첫 폭락 저점, 기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-06-30 OUSD 컨소시엄 출범 + 지수 제외 겹친 급락)의 대형 조정을 거치며 현재가와 4배 이상 괴리돼 있어 근시일 저항으로 보지 않음 |

> 표시 기준은 "현재가에서 가까운 순으로 각 방향 3개"다(4. 방법론 · 한계 생성 스크립트 기본값). 표본 자체가 64주뿐이라 R1(2회 터치)을 제외한 모든 레벨이 `--force-level`·`--ref-line`으로 강제 포함한 예외다 — 다른 회사 문서 대비 레벨의 통계적 근거가 약하다는 뜻이다(상단 경고 참고).

---

## 3. 관측된 특이 구간 — 2026-02-02 상장 후 첫 폭락 저점

- 2025-06-23 상장 후 첫 랠리 정점(주간 고점 $298.99)에서 2026-02-02 주간 저점 $49.90까지 약 7개월간 **-83.3%** 폭락했다(주간 종가 기준이 아닌 고가·저가 기준). 역사 / 주요 이벤트·투자 판단가 다루는 경쟁 심화(Tether USAT 출시, 2026-01)와 시기가 겹치지만, 애초에 IPO 직후 형성된 배수 자체가 극단적으로 높았던 데 따른 재평가(de-rating) 성격이 강해 보인다 — 단일 사건으로 설명되지 않는 다요인 조정이다.
- 이후 2026년 5월(주간 고점 $140.00)까지 반등했으나, 기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-06-30 OUSD 컨소시엄 출범 + 지수 제외 겹친 급락이 다루는 2026-06-30 OUSD 컨소시엄 출범·지수 제외 겹친 급락으로 다시 큰 폭 조정받았다(주간 저점 $57.84, 2026-08-03, 고점 대비 -58.7%) — **상장 후 14개월 사이에 이미 두 차례의 대형 조정(-83.3%, -58.7%)을 겪은 셈**이다. 이는 회사 펀더멘털의 구조적 문제라기보다, 신규 상장·초기 유통물량이 적은 종목 특유의 높은 변동성과 두 차례의 서로 다른 계기(자체 재평가, 경쟁 컨소시엄 출범)가 겹친 결과로 해석하는 것이 합리적이다.
- 두 번째 조정(2026-06-30 이후)의 상세 내용은 기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-06-30 OUSD 컨소시엄 출범 + 지수 제외 겹친 급락에 이미 기록돼 있어 여기서 중복 서술하지 않는다 — 이 문서(3. 관측된 특이 구간 — 2026-02-02 상장 후 첫 폭락 저점)는 일봉 문서가 다루지 않는 첫 번째 조정(상장~2026년 2월)에 초점을 맞춘다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 64개 주, 2025-06-02~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영) — Circle은 이 구간 내 일반적 의미의 주식분할·병합 이력이 없다(핵심 지표 상단 경고·기술적 분석 — 일봉·1년 4. 방법론 · 한계와 동일 확인). IPO 시 우선주의 보통주 전환·Class B 신설은 스톡스플릿이 아니므로 소급조정 대상이 아니다.
- **표본 크기 한계**: 64주는 스크립트 최소 표본(60개)을 간신히 충족하는 수준이다 — 5년(약 260주) 표본을 쓰는 다른 회사 문서 대비 스윙 클러스터의 통계적 신뢰도가 훨씬 낮다. 상단 경고에서 밝혔듯 대부분의 레벨이 강제 포함 예외다.
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py CRCL --name Circle --interval 1wk --ref-line 298.99:"상장 후 최고가(2025-06-23)" --force-level '159.47:(2025년 10월 스윙 고점)' --force-level '64.92:(2025년 11월 스윙 저점)' --force-level '49.90:(상장 후 최저가, 2026년 2월)' --event '2026-02-02:상장 후 첫 폭락 저점(고점 대비 -83.3%)' --close-on 2026-08-13 --close-on 2026-08-14`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다(기간만 실제 거래 구간으로 단축).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 최적화된 값이 아니다.
    - 상장 후 14개월 사이 이미 두 차례 대형 조정(3. 관측된 특이 구간 — 2026-02-02 상장 후 첫 폭락 저점)을 겪어, 스윙 레벨 자체가 "안정적인 거래 레인지"라기보다 "여전히 가격 발견(price discovery) 중인 신규 상장주"의 특성을 반영한다고 보는 것이 정확하다.
    - 기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-06-30 OUSD 컨소시엄 출범 + 지수 제외 겹친 급락의 2026-06-30 이후 급락처럼 뉴스 이벤트로 인한 불연속 구간은 통상적인 지지/저항 해석이 적용되기 어렵다.

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-23)*
