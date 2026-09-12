# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 2026-09-11 종가 **$90.60**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.

:::
---

## 1. 차트 — 상장 이후 주봉 (2025-06-02 ~ 2026-09-11)

<div class="crcl-chart">
<style>
.crcl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.crcl-chart svg { width:100%; height:auto; display:block; }
.crcl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.crcl-chart .title { fill: var(--ink); font-weight:600; }
.crcl-chart .grid { stroke: var(--grid); stroke-width:1; }
.crcl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Circle(CRCL) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Circle (CRCL) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-06-02 ~ 2026-09-11 · 마지막 종가 $90.60 (2026-09-11) · 단위 USD</text>
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
<line x1="67.3" y1="56.0" x2="67.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="67.3" y1="626.0" x2="67.3" y2="631.0" class="axis"/>
<text x="67.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="519.5" y1="56.0" x2="519.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="519.5" y1="626.0" x2="519.5" y2="631.0" class="axis"/>
<text x="519.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="79.2" x2="1052" y2="79.2" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="82.2" font-size="10.5" fill="var(--muted)">$299 상장 후 최고(2025-06)</text>
<line x1="67.3" y1="449.7" x2="67.3" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="64.29" y="483.1" width="6.00" height="81.7" fill="var(--up)"/>
<line x1="81.9" y1="417.9" x2="81.9" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="78.88" y="428.5" width="6.00" height="1.8" fill="var(--up)"/>
<line x1="96.5" y1="185.0" x2="96.5" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="93.47" y="203.2" width="6.00" height="195.8" fill="var(--up)"/>
<line x1="111.1" y1="79.2" x2="111.1" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="108.06" y="207.0" width="6.00" height="122.5" fill="var(--down)"/>
<line x1="125.6" y1="300.9" x2="125.6" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="122.65" y="311.9" width="6.00" height="14.8" fill="var(--up)"/>
<line x1="140.2" y1="255.3" x2="140.2" y2="325.2" stroke="var(--down)" class="wick"/>
<rect x="137.24" y="301.4" width="6.00" height="13.6" fill="var(--down)"/>
<line x1="154.8" y1="155.3" x2="154.8" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="151.82" y="238.0" width="6.00" height="72.9" fill="var(--up)"/>
<line x1="169.4" y1="220.9" x2="169.4" y2="314.6" stroke="var(--down)" class="wick"/>
<rect x="166.41" y="232.5" width="6.00" height="70.8" fill="var(--down)"/>
<line x1="184.0" y1="292.7" x2="184.0" y2="357.3" stroke="var(--down)" class="wick"/>
<rect x="181.00" y="294.6" width="6.00" height="61.0" fill="var(--down)"/>
<line x1="198.6" y1="347.1" x2="198.6" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="195.59" y="347.1" width="6.00" height="27.6" fill="var(--down)"/>
<line x1="213.2" y1="309.5" x2="213.2" y2="422.5" stroke="var(--down)" class="wick"/>
<rect x="210.18" y="370.5" width="6.00" height="24.8" fill="var(--down)"/>
<line x1="227.8" y1="394.9" x2="227.8" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="224.76" y="396.5" width="6.00" height="28.8" fill="var(--down)"/>
<line x1="242.4" y1="423.4" x2="242.4" y2="448.3" stroke="var(--down)" class="wick"/>
<rect x="239.35" y="426.8" width="6.00" height="5.0" fill="var(--down)"/>
<line x1="256.9" y1="432.4" x2="256.9" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="253.94" y="439.0" width="6.00" height="29.6" fill="var(--down)"/>
<line x1="271.5" y1="422.3" x2="271.5" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="268.53" y="445.9" width="6.00" height="23.9" fill="var(--up)"/>
<line x1="286.1" y1="398.6" x2="286.1" y2="446.4" stroke="var(--up)" class="wick"/>
<rect x="283.12" y="406.1" width="6.00" height="30.1" fill="var(--up)"/>
<line x1="300.7" y1="411.5" x2="300.7" y2="451.1" stroke="var(--down)" class="wick"/>
<rect x="297.71" y="415.1" width="6.00" height="27.2" fill="var(--down)"/>
<line x1="315.3" y1="380.1" x2="315.3" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="312.29" y="402.7" width="6.00" height="34.4" fill="var(--up)"/>
<line x1="329.9" y1="373.8" x2="329.9" y2="430.5" stroke="var(--down)" class="wick"/>
<rect x="326.88" y="385.3" width="6.00" height="44.5" fill="var(--down)"/>
<line x1="344.5" y1="412.0" x2="344.5" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="341.47" y="419.0" width="6.00" height="24.4" fill="var(--down)"/>
<line x1="359.1" y1="406.4" x2="359.1" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="356.06" y="410.6" width="6.00" height="25.9" fill="var(--up)"/>
<line x1="373.6" y1="399.2" x2="373.6" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="370.65" y="400.3" width="6.00" height="42.1" fill="var(--down)"/>
<line x1="388.2" y1="445.0" x2="388.2" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="385.24" y="445.0" width="6.00" height="47.7" fill="var(--down)"/>
<line x1="402.8" y1="477.1" x2="402.8" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="399.82" y="482.9" width="6.00" height="54.7" fill="var(--down)"/>
<line x1="417.4" y1="537.5" x2="417.4" y2="573.4" stroke="var(--down)" class="wick"/>
<rect x="414.41" y="537.8" width="6.00" height="22.1" fill="var(--down)"/>
<line x1="432.0" y1="538.4" x2="432.0" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="429.00" y="541.7" width="6.00" height="16.7" fill="var(--up)"/>
<line x1="446.6" y1="524.1" x2="446.6" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="443.59" y="529.7" width="6.00" height="17.2" fill="var(--up)"/>
<line x1="461.2" y1="517.7" x2="461.2" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="458.18" y="526.9" width="6.00" height="7.3" fill="var(--down)"/>
<line x1="475.8" y1="528.3" x2="475.8" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="472.76" y="528.6" width="6.00" height="4.8" fill="var(--up)"/>
<line x1="490.4" y1="517.9" x2="490.4" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="487.35" y="525.2" width="6.00" height="13.7" fill="var(--down)"/>
<line x1="504.9" y1="531.9" x2="504.9" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="501.94" y="534.2" width="6.00" height="8.9" fill="var(--up)"/>
<line x1="519.5" y1="524.5" x2="519.5" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="516.53" y="531.9" width="6.00" height="3.5" fill="var(--down)"/>
<line x1="534.1" y1="523.7" x2="534.1" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="531.12" y="539.1" width="6.00" height="5.3" fill="var(--down)"/>
<line x1="548.7" y1="546.9" x2="548.7" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="545.71" y="550.6" width="6.00" height="9.2" fill="var(--down)"/>
<line x1="563.3" y1="547.9" x2="563.3" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="560.29" y="562.6" width="6.00" height="12.8" fill="var(--down)"/>
<line x1="577.9" y1="579.8" x2="577.9" y2="605.1" stroke="var(--down)" class="wick"/>
<rect x="574.88" y="580.6" width="6.00" height="9.4" fill="var(--down)"/>
<line x1="592.5" y1="579.1" x2="592.5" y2="593.7" stroke="var(--up)" class="wick"/>
<rect x="589.47" y="583.7" width="6.00" height="7.8" fill="var(--up)"/>
<line x1="607.1" y1="572.2" x2="607.1" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="604.06" y="577.4" width="6.00" height="7.9" fill="var(--up)"/>
<line x1="621.6" y1="519.2" x2="621.6" y2="584.9" stroke="var(--up)" class="wick"/>
<rect x="618.65" y="534.3" width="6.00" height="45.1" fill="var(--up)"/>
<line x1="636.2" y1="478.0" x2="636.2" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="633.24" y="495.3" width="6.00" height="44.6" fill="var(--up)"/>
<line x1="650.8" y1="449.9" x2="650.8" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="647.82" y="466.9" width="6.00" height="21.5" fill="var(--up)"/>
<line x1="665.4" y1="422.0" x2="665.4" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="662.41" y="444.4" width="6.00" height="12.4" fill="var(--up)"/>
<line x1="680.0" y1="441.3" x2="680.0" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="677.00" y="448.3" width="6.00" height="64.4" fill="var(--down)"/>
<line x1="694.6" y1="500.5" x2="694.6" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="691.59" y="507.2" width="6.00" height="12.7" fill="var(--down)"/>
<line x1="709.2" y1="495.5" x2="709.2" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="706.18" y="513.9" width="6.00" height="10.7" fill="var(--down)"/>
<line x1="723.8" y1="475.7" x2="723.8" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="720.76" y="486.9" width="6.00" height="41.3" fill="var(--up)"/>
<line x1="738.4" y1="485.6" x2="738.4" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="735.35" y="494.1" width="6.00" height="6.0" fill="var(--down)"/>
<line x1="752.9" y1="499.3" x2="752.9" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="749.94" y="500.0" width="6.00" height="2.4" fill="var(--up)"/>
<line x1="767.5" y1="451.1" x2="767.5" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="764.53" y="470.5" width="6.00" height="13.8" fill="var(--up)"/>
<line x1="782.1" y1="414.9" x2="782.1" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="779.12" y="459.5" width="6.00" height="10.2" fill="var(--down)"/>
<line x1="796.7" y1="459.5" x2="796.7" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="793.71" y="471.6" width="6.00" height="2.2" fill="var(--up)"/>
<line x1="811.3" y1="468.8" x2="811.3" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="808.29" y="471.9" width="6.00" height="1.6" fill="var(--up)"/>
<line x1="825.9" y1="479.3" x2="825.9" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="822.88" y="480.9" width="6.00" height="60.0" fill="var(--down)"/>
<line x1="840.5" y1="526.0" x2="840.5" y2="546.6" stroke="var(--down)" class="wick"/>
<rect x="837.47" y="533.1" width="6.00" height="13.0" fill="var(--down)"/>
<line x1="855.1" y1="526.1" x2="855.1" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="852.06" y="535.5" width="6.00" height="5.6" fill="var(--down)"/>
<line x1="869.6" y1="531.3" x2="869.6" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="866.65" y="538.9" width="6.00" height="16.2" fill="var(--down)"/>
<line x1="884.2" y1="549.7" x2="884.2" y2="580.0" stroke="var(--down)" class="wick"/>
<rect x="881.24" y="551.7" width="6.00" height="22.3" fill="var(--down)"/>
<line x1="898.8" y1="556.6" x2="898.8" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="895.82" y="570.8" width="6.00" height="3.3" fill="var(--up)"/>
<line x1="913.4" y1="569.3" x2="913.4" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="910.41" y="574.4" width="6.00" height="8.4" fill="var(--down)"/>
<line x1="928.0" y1="557.0" x2="928.0" y2="583.9" stroke="var(--up)" class="wick"/>
<rect x="925.00" y="578.8" width="6.00" height="3.0" fill="var(--up)"/>
<line x1="942.6" y1="570.6" x2="942.6" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="939.59" y="576.1" width="6.00" height="2.2" fill="var(--down)"/>
<line x1="957.2" y1="566.0" x2="957.2" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="954.18" y="569.7" width="6.00" height="16.2" fill="var(--up)"/>
<line x1="971.8" y1="550.2" x2="971.8" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="968.76" y="559.3" width="6.00" height="9.4" fill="var(--up)"/>
<line x1="986.4" y1="514.2" x2="986.4" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="983.35" y="524.7" width="6.00" height="35.4" fill="var(--up)"/>
<line x1="1000.9" y1="507.3" x2="1000.9" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="997.94" y="520.6" width="6.00" height="5.9" fill="var(--down)"/>
<line x1="1015.5" y1="492.4" x2="1015.5" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="1012.53" y="495.0" width="6.00" height="31.7" fill="var(--up)"/>
<line x1="1030.1" y1="497.6" x2="1030.1" y2="521.5" stroke="var(--down)" class="wick"/>
<rect x="1027.12" y="498.0" width="6.00" height="21.2" fill="var(--down)"/>
<line x1="1044.7" y1="508.2" x2="1044.7" y2="520.1" stroke="var(--down)" class="wick"/>
<rect x="1041.71" y="516.2" width="6.00" height="3.0" fill="var(--down)"/>
<line x1="60" y1="418.4" x2="1052" y2="418.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="421.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$138 R1</text>
<text x="1058" y="433.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="519.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="511.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $91 (2026-09-11)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **[기술적 분석 — 일봉·1년](./09_technical_daily.md)의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $138 | 2 | 2026-03-16·2026-05-11 주 — OUSD 급락 이전 마지막 반등 고점대. 현재가 대비 52% 위 |
| **현재가** | **$90.60** (2026-09-11 종가) | — | 기간 내 하단 지지 없음(신저가 구간) — 가장 가까운 저항은 R1 |
| 참고선 | $299 | — | 상장 후 최고(2025-06) — 상장 직후 유통 물량이 극히 제한된 상태에서 형성된 가격이라 현재 펀더멘털과 무관하다 |

**이 표는 레벨이 하나뿐이라 사실상 비어 있는 것과 같다.** 68주라는 짧은 표본에서 터치 2회 이상을 만족하는 클러스터가 R1($138) 하나밖에 나오지 않았다. 현재가 아래에 지지 클러스터가 없다는 것은 **지지가 견고하다는 뜻이 아니라 "아래쪽에 반복 확인된 가격대가 없다"는 뜻**이며, 스크립트가 자동으로 붙인 "신저가 구간"이라는 비고도 문자 그대로 읽으면 안 된다 — 상장 후 최저가는 $49.90(2026-02-05)이고 현재가는 그보다 81% 높다. 아래 4. 방법론 · 한계 참고.

---

## 3. 관측된 특이 구간 — 2025-06 상장 직후 급등과 이후 장기 하락

- 2025-06-05 NYSE 상장(공모가 $31) 직후 몇 주 만에 **$298.99**까지 올랐다(참고선). 이후 1년 넘게 하락이 이어져 2026-02-05 $49.90까지 내려갔고, 고점 대비 하락폭은 약 83%다.
- 주봉 기준으로 이 구간은 **단일 추세 하락**이라 중간에 반복 확인된 가격대가 거의 만들어지지 않았다 — 위 표에 레벨이 하나뿐인 구조적 이유다.
- 상장 직후 고점 $298.99는 상장 초기 유통 물량이 극히 제한된 상태에서 형성된 가격이라, **현재 펀더멘털과 무관한 구간**으로 보고 참고선으로만 처리했다. 일봉 문서가 다루는 2026-06-30 OUSD 급락은 단기 이벤트라 여기서 중복 서술하지 않는다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 68개 주, 2025-06-02~2026-09-11. 수집 시점: 2026-09-13. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py CRCL --name Circle --interval 1wk --ref-line 298.99:"상장 후 최고(2025-06)" --close-on 2026-09-11 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **표본이 5년이 아니라 68주다.** 2025-06-05 상장이라 주봉 표본이 템플릿이 상정한 5년의 4분의 1 수준이고, 그 결과 유효 클러스터가 1개뿐이다. **이 문서의 레벨 표는 다른 회사의 주봉 문서와 같은 무게로 읽으면 안 된다.**
    - **"신저가 구간"이라는 비고는 스크립트의 자동 생성 문구이며 사실과 다르다.** 현재가 아래에 터치 2회 이상 클러스터가 없을 때 붙는 라벨일 뿐, 실제로는 상장 후 최저가($49.90) 대비 81% 높은 위치다. 값을 임의로 고치지 않고 그대로 두되 이 각주로 바로잡는다.
    - 표본 기간에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트는 없었다.

---

*작성일: 2026-09-13*
