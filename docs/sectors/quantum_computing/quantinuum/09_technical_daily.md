# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 상장(2026-06-04) 이후 전 구간의 일봉 가격 흐름. **거래일이 62일뿐이라 스윙 클러스터가 하나도 형성되지 않았다** — 이 문서는 지지/저항을 제시하지 못하며, 가격 구간과 그 형성 경위만 기록한다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-02 종가 $48.00은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다. 상장 이후 주식분할이 없어 원주가와 수정주가가 같다.
    - **기간**: 차트 구간이 2026-06-04~2026-09-02(62거래일)로, 다른 회사 문서의 "최근 1년"과 다르다. 상장 이전 데이터가 존재하지 않기 때문이다.

---

## 1. 차트 — 상장 이후 전 구간 일봉 (2026-06-04 ~ 2026-09-02)

<div class="qnt-chart">
<style>
.qnt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .qnt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .qnt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.qnt-chart svg { width:100%; height:auto; display:block; }
.qnt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.qnt-chart .title { fill: var(--ink); font-weight:600; }
.qnt-chart .grid { stroke: var(--grid); stroke-width:1; }
.qnt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Quantinuum(QNT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Quantinuum (QNT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2026-06-04 ~ 2026-09-02 · 마지막 종가 $48.00 (2026-09-02) · 단위 USD</text>
<line x1="60" y1="559.7" x2="1052" y2="559.7" class="grid"/>
<text x="52" y="563.7" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="427.2" x2="1052" y2="427.2" class="grid"/>
<text x="52" y="431.2" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="294.6" x2="1052" y2="294.6" class="grid"/>
<text x="52" y="298.6" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="162.0" x2="1052" y2="162.0" class="grid"/>
<text x="52" y="166.0" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="68.0" y1="626.0" x2="68.0" y2="631.0" class="axis"/>
<text x="68.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="356.0" y1="626.0" x2="356.0" y2="631.0" class="axis"/>
<text x="356.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="708.0" y1="626.0" x2="708.0" y2="631.0" class="axis"/>
<text x="708.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1028.0" y1="626.0" x2="1028.0" y2="631.0" class="axis"/>
<text x="1028.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="68.0" y1="276.7" x2="68.0" y2="428.6" stroke="var(--down)" class="wick"/>
<rect x="65.00" y="321.1" width="6.00" height="101.0" fill="var(--down)"/>
<line x1="84.0" y1="428.6" x2="84.0" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="81.00" y="429.8" width="6.00" height="46.9" fill="var(--down)"/>
<line x1="100.0" y1="403.3" x2="100.0" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="97.00" y="444.9" width="6.00" height="3.4" fill="var(--down)"/>
<line x1="116.0" y1="390.3" x2="116.0" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="113.00" y="409.9" width="6.00" height="84.3" fill="var(--down)"/>
<line x1="132.0" y1="488.8" x2="132.0" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="129.00" y="495.8" width="6.00" height="45.3" fill="var(--down)"/>
<line x1="148.0" y1="462.4" x2="148.0" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="145.00" y="473.7" width="6.00" height="66.1" fill="var(--up)"/>
<line x1="164.0" y1="460.6" x2="164.0" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="161.00" y="478.2" width="6.00" height="11.8" fill="var(--down)"/>
<line x1="180.0" y1="413.9" x2="180.0" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="177.00" y="454.9" width="6.00" height="8.5" fill="var(--up)"/>
<line x1="196.0" y1="436.0" x2="196.0" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="193.00" y="443.7" width="6.00" height="44.0" fill="var(--down)"/>
<line x1="212.0" y1="352.9" x2="212.0" y2="484.2" stroke="var(--up)" class="wick"/>
<rect x="209.00" y="390.7" width="6.00" height="92.7" fill="var(--up)"/>
<line x1="228.0" y1="258.3" x2="228.0" y2="400.7" stroke="var(--up)" class="wick"/>
<rect x="225.00" y="297.3" width="6.00" height="84.7" fill="var(--up)"/>
<line x1="244.0" y1="190.5" x2="244.0" y2="337.7" stroke="var(--down)" class="wick"/>
<rect x="241.00" y="301.2" width="6.00" height="16.3" fill="var(--down)"/>
<line x1="260.0" y1="142.4" x2="260.0" y2="346.3" stroke="var(--up)" class="wick"/>
<rect x="257.00" y="195.7" width="6.00" height="145.0" fill="var(--up)"/>
<line x1="276.0" y1="181.9" x2="276.0" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="273.00" y="193.7" width="6.00" height="86.3" fill="var(--down)"/>
<line x1="292.0" y1="257.4" x2="292.0" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="289.00" y="259.7" width="6.00" height="12.6" fill="var(--down)"/>
<line x1="308.0" y1="171.3" x2="308.0" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="305.00" y="220.8" width="6.00" height="110.3" fill="var(--up)"/>
<line x1="324.0" y1="155.4" x2="324.0" y2="286.5" stroke="var(--down)" class="wick"/>
<rect x="321.00" y="168.7" width="6.00" height="88.3" fill="var(--down)"/>
<line x1="340.0" y1="131.6" x2="340.0" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="337.00" y="139.0" width="6.00" height="116.1" fill="var(--up)"/>
<line x1="356.0" y1="137.7" x2="356.0" y2="224.6" stroke="var(--down)" class="wick"/>
<rect x="353.00" y="160.3" width="6.00" height="22.8" fill="var(--down)"/>
<line x1="372.0" y1="154.0" x2="372.0" y2="274.5" stroke="var(--down)" class="wick"/>
<rect x="369.00" y="188.6" width="6.00" height="45.6" fill="var(--down)"/>
<line x1="388.0" y1="72.0" x2="388.0" y2="238.9" stroke="var(--up)" class="wick"/>
<rect x="385.00" y="120.0" width="6.00" height="115.7" fill="var(--up)"/>
<line x1="404.0" y1="120.0" x2="404.0" y2="213.7" stroke="var(--down)" class="wick"/>
<rect x="401.00" y="120.0" width="6.00" height="73.8" fill="var(--down)"/>
<line x1="420.0" y1="176.9" x2="420.0" y2="227.0" stroke="var(--down)" class="wick"/>
<rect x="417.00" y="214.4" width="6.00" height="5.8" fill="var(--down)"/>
<line x1="436.0" y1="192.7" x2="436.0" y2="250.2" stroke="var(--down)" class="wick"/>
<rect x="433.00" y="201.8" width="6.00" height="46.3" fill="var(--down)"/>
<line x1="452.0" y1="246.4" x2="452.0" y2="304.3" stroke="var(--down)" class="wick"/>
<rect x="449.00" y="249.9" width="6.00" height="38.7" fill="var(--down)"/>
<line x1="468.0" y1="287.7" x2="468.0" y2="388.3" stroke="var(--down)" class="wick"/>
<rect x="465.00" y="294.6" width="6.00" height="78.3" fill="var(--down)"/>
<line x1="484.0" y1="330.3" x2="484.0" y2="387.3" stroke="var(--up)" class="wick"/>
<rect x="481.00" y="339.3" width="6.00" height="21.6" fill="var(--up)"/>
<line x1="500.0" y1="301.2" x2="500.0" y2="443.3" stroke="var(--down)" class="wick"/>
<rect x="497.00" y="333.8" width="6.00" height="86.6" fill="var(--down)"/>
<line x1="516.0" y1="431.1" x2="516.0" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="513.00" y="440.2" width="6.00" height="33.1" fill="var(--down)"/>
<line x1="532.0" y1="442.3" x2="532.0" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="529.00" y="479.3" width="6.00" height="19.8" fill="var(--up)"/>
<line x1="548.0" y1="415.4" x2="548.0" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="545.00" y="462.3" width="6.00" height="3.8" fill="var(--up)"/>
<line x1="564.0" y1="436.4" x2="564.0" y2="490.1" stroke="var(--up)" class="wick"/>
<rect x="561.00" y="446.0" width="6.00" height="3.0" fill="var(--up)"/>
<line x1="580.0" y1="427.6" x2="580.0" y2="510.7" stroke="var(--down)" class="wick"/>
<rect x="577.00" y="460.3" width="6.00" height="34.7" fill="var(--down)"/>
<line x1="596.0" y1="458.2" x2="596.0" y2="519.0" stroke="var(--up)" class="wick"/>
<rect x="593.00" y="474.1" width="6.00" height="36.6" fill="var(--up)"/>
<line x1="612.0" y1="470.4" x2="612.0" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="609.00" y="474.8" width="6.00" height="54.6" fill="var(--down)"/>
<line x1="628.0" y1="469.7" x2="628.0" y2="545.0" stroke="var(--down)" class="wick"/>
<rect x="625.00" y="513.3" width="6.00" height="8.9" fill="var(--down)"/>
<line x1="644.0" y1="521.4" x2="644.0" y2="597.8" stroke="var(--down)" class="wick"/>
<rect x="641.00" y="533.2" width="6.00" height="29.4" fill="var(--down)"/>
<line x1="660.0" y1="548.9" x2="660.0" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="657.00" y="565.4" width="6.00" height="29.6" fill="var(--down)"/>
<line x1="676.0" y1="527.4" x2="676.0" y2="586.2" stroke="var(--up)" class="wick"/>
<rect x="673.00" y="539.2" width="6.00" height="45.5" fill="var(--up)"/>
<line x1="692.0" y1="502.3" x2="692.0" y2="554.2" stroke="var(--down)" class="wick"/>
<rect x="689.00" y="520.5" width="6.00" height="20.5" fill="var(--down)"/>
<line x1="708.0" y1="470.1" x2="708.0" y2="567.9" stroke="var(--up)" class="wick"/>
<rect x="705.00" y="484.8" width="6.00" height="56.3" fill="var(--up)"/>
<line x1="724.0" y1="443.5" x2="724.0" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="721.00" y="451.8" width="6.00" height="8.5" fill="var(--up)"/>
<line x1="740.0" y1="457.0" x2="740.0" y2="491.3" stroke="var(--down)" class="wick"/>
<rect x="737.00" y="465.2" width="6.00" height="2.9" fill="var(--down)"/>
<line x1="756.0" y1="422.3" x2="756.0" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="753.00" y="442.0" width="6.00" height="51.4" fill="var(--up)"/>
<line x1="772.0" y1="394.4" x2="772.0" y2="448.4" stroke="var(--down)" class="wick"/>
<rect x="769.00" y="427.2" width="6.00" height="17.1" fill="var(--down)"/>
<line x1="788.0" y1="434.5" x2="788.0" y2="480.7" stroke="var(--down)" class="wick"/>
<rect x="785.00" y="444.3" width="6.00" height="28.1" fill="var(--down)"/>
<line x1="804.0" y1="461.6" x2="804.0" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="801.00" y="469.3" width="6.00" height="10.1" fill="var(--down)"/>
<line x1="820.0" y1="262.8" x2="820.0" y2="460.0" stroke="var(--up)" class="wick"/>
<rect x="817.00" y="271.5" width="6.00" height="160.3" fill="var(--up)"/>
<line x1="836.0" y1="275.1" x2="836.0" y2="346.4" stroke="var(--down)" class="wick"/>
<rect x="833.00" y="299.1" width="6.00" height="15.4" fill="var(--down)"/>
<line x1="852.0" y1="288.0" x2="852.0" y2="389.3" stroke="var(--down)" class="wick"/>
<rect x="849.00" y="315.8" width="6.00" height="63.8" fill="var(--down)"/>
<line x1="868.0" y1="329.1" x2="868.0" y2="395.7" stroke="var(--up)" class="wick"/>
<rect x="865.00" y="347.5" width="6.00" height="32.7" fill="var(--up)"/>
<line x1="884.0" y1="369.8" x2="884.0" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="881.00" y="382.1" width="6.00" height="51.7" fill="var(--down)"/>
<line x1="900.0" y1="430.9" x2="900.0" y2="483.0" stroke="var(--down)" class="wick"/>
<rect x="897.00" y="431.7" width="6.00" height="48.5" fill="var(--down)"/>
<line x1="916.0" y1="464.3" x2="916.0" y2="505.9" stroke="var(--down)" class="wick"/>
<rect x="913.00" y="483.0" width="6.00" height="11.8" fill="var(--down)"/>
<line x1="932.0" y1="467.5" x2="932.0" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="929.00" y="472.2" width="6.00" height="18.6" fill="var(--up)"/>
<line x1="948.0" y1="487.5" x2="948.0" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="945.00" y="493.4" width="6.00" height="38.8" fill="var(--down)"/>
<line x1="964.0" y1="500.9" x2="964.0" y2="525.0" stroke="var(--up)" class="wick"/>
<rect x="961.00" y="508.2" width="6.00" height="13.4" fill="var(--up)"/>
<line x1="980.0" y1="505.1" x2="980.0" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="977.00" y="516.1" width="6.00" height="9.7" fill="var(--up)"/>
<line x1="996.0" y1="496.4" x2="996.0" y2="514.4" stroke="var(--up)" class="wick"/>
<rect x="993.00" y="506.7" width="6.00" height="1.0" fill="var(--up)"/>
<line x1="1012.0" y1="535.3" x2="1012.0" y2="566.9" stroke="var(--up)" class="wick"/>
<rect x="1009.00" y="558.4" width="6.00" height="1.3" fill="var(--up)"/>
<line x1="1028.0" y1="572.0" x2="1028.0" y2="594.1" stroke="var(--down)" class="wick"/>
<rect x="1025.00" y="572.8" width="6.00" height="17.9" fill="var(--down)"/>
<line x1="1044.0" y1="581.1" x2="1044.0" y2="605.6" stroke="var(--up)" class="wick"/>
<rect x="1041.00" y="586.2" width="6.00" height="9.3" fill="var(--up)"/>
<circle cx="1052.0" cy="586.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="578.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $48 (2026-09-02)</text>
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
| **현재가** | **$48.00** (2026-09-02 종가) | — | 유효한 클러스터 없음 — §4에 표본 부족 사유 기입 |
| 참고선 | $86.79 / $46.54 | — | 상장 후 장중 최고/최저. 각각 2026-06 상장 직후 국면과 최근 저점이며, 터치가 쌓이지 않아 지지·저항이 아니라 구간의 양 끝으로만 읽는다 |
| 참고선 | $60.00 | — | IPO 공모가. 기술적 레벨은 아니지만 공모 참여자의 손익분기라 시장이 의식하는 가격대 |

**터치 2회 이상인 클러스터가 하나도 없다.** 62거래일 동안 가격이 $86.79 → $46.54로 한 방향으로 내려오면서 같은 가격대를 되돌아와 확인한 적이 거의 없기 때문이다. 위 표의 두 행은 클러스터가 아니라 **참고선**이며, 지지·저항으로 읽어서는 안 된다. 근시일 기술적 판단에 쓸 수 있는 레벨은 현재로선 없다고 보는 것이 정확하다.

---

## 3. 관측된 특이 구간 — 상장 후 3개월의 단방향 하락

- **2026-06-04 상장**: 공모가 $60.00, 시초가 $68.00(+13.3%), 장중 고가 $71.35, 종가 $60.38. 공모 밴드를 두 차례 올린 끝에 $60에 확정했고 20배 초과 청약이 있었다고 보도됐다([최근 뉴스 / 이슈](./08_news.md)).
- 이후 **$86.79까지 올랐다가 $46.54까지 되돌렸다.** 고점 대비 -46.4%이며, 상장 3개월 만의 낙폭치고 크다.
- **2026-08-11 첫 실적 발표 당일 주가는 +8.3% 올랐다.** 매출 +279%(분기 YoY)와 Oracle 파트너십이 재료였다. 그 이후 현재($48.00)까지 다시 내려온 흐름은 시장이 헤드라인 대신 **상반기 -37.7% 역성장과 FY2026 보합 가이던스**를 반영했을 가능성을 시사하지만, **가격 움직임의 인과는 확인하지 못했다.** 위 서술은 시점의 병치이지 인과 주장이 아니다.
- 현재가 $48.00은 공모가($60.00)를 20.0% 밑돈다 — 공모 참여자가 전원 손실 구간에 있다는 뜻이며, 이는 향후 매도 압력의 배경이 될 수 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 62개 거래일, 2026-06-04~2026-09-02. 수집 시점: 2026-09-03. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py QNT --name "Quantinuum" --close-on 2026-09-02 --emit all` (일봉 기본 파라미터, 옵션 변경 없음. 수집 기간이 62거래일인 것은 상장일 제약이며 옵션으로 줄인 것이 아니다)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **표본 부족이 이 문서의 결정적 한계다.** 62거래일은 전후 5거래일 창으로 스윙을 탐지하기에는 충분하지만, 그 스윙들이 같은 가격대에 2회 이상 모이려면 가격이 구간을 오가야 한다. 이 종목은 상장 후 사실상 한 방향으로 내려와 클러스터가 만들어지지 않았다. **거래 이력이 1년을 넘기는 2027년 중반 이후에 다시 생성할 것.**
    - 상장 직후 구간은 수급이 공모 배정·초기 회전에 크게 좌우되므로, 기술적 레벨로서의 의미가 평상시보다 더 약하다.
    - 해당 기간 주식분할은 없었다. 다만 **전체 주식의 13.7%(Class A)만 유통되는 구조**라 같은 거래량이라도 가격 충격이 크다는 점을 감안할 것([핵심 지표](./04_metrics.md) A.2 각주 ⁷).

---

*작성일: 2026-09-03*
