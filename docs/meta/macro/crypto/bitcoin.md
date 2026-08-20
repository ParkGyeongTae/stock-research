# 비트코인 (BTC/USD) — 기술적 참고 (주봉 5년)

> 최근 5년 BTC/USD(`BTC-USD`) 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다른 macro 문서(원달러·국채금리 등)와 달리 **모든 회사에 적용되는 지표가 아니다** — [`sectors/digital_asset_finance/`](../../../sectors/digital_asset_finance/00_overview.md) 소속 회사(거래소·커스터디·디지털 자산 보유 기업 등)의 실적·거래대금·평가손익이 BTC 가격과 직접 연동되는 경우에 한해 인용한다. 다른 섹터 회사 문서에서는 이 문서를 인용할 이유가 없다.
>
> 이 레포는 개별 주식 리서치가 중심이고, BTC 자체를 투자 대상으로 다루지 않는다 — [`concepts/macroeconomics.md`](../../concepts/macroeconomics.md) "거시를 어디까지 쓸 것인가"와 같은 원칙을 적용해, `digital_asset_finance` 섹터 회사의 실적을 이해하기 위한 배경 자료로만 쓴다.
>
> ⚠️ BTC/USD는 **24시간 365일 거래**된다 — 다른 macro 문서(주식시장 개장일 기준)와 달리 차트의 "주 마지막 거래일"이 주말(예: 일요일 UTC 자정)일 수 있고, 거래량 단위도 주식과 다르다.

---

## 1. 차트 — 최근 5년 주봉

<div class="btc-usd-chart">
<style>
.btc-usd-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .btc-usd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .btc-usd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.btc-usd-chart svg { width:100%; height:auto; display:block; }
.btc-usd-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.btc-usd-chart .title { fill: var(--ink); font-weight:600; }
.btc-usd-chart .grid { stroke: var(--grid); stroke-width:1; }
.btc-usd-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="비트코인(BTC-USD) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">비트코인 (BTC-USD) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-20 · 마지막 종가 $72,171.72 (2026-08-20) · 단위 USD</text>
<line x1="60" y1="587.4" x2="1052" y2="587.4" class="grid"/>
<text x="52" y="591.4" font-size="11" text-anchor="end" fill="var(--muted)">20,000</text>
<line x1="60" y1="490.7" x2="1052" y2="490.7" class="grid"/>
<text x="52" y="494.7" font-size="11" text-anchor="end" fill="var(--muted)">40,000</text>
<line x1="60" y1="394.1" x2="1052" y2="394.1" class="grid"/>
<text x="52" y="398.1" font-size="11" text-anchor="end" fill="var(--muted)">60,000</text>
<line x1="60" y1="297.5" x2="1052" y2="297.5" class="grid"/>
<text x="52" y="301.5" font-size="11" text-anchor="end" fill="var(--muted)">80,000</text>
<line x1="60" y1="200.9" x2="1052" y2="200.9" class="grid"/>
<text x="52" y="204.9" font-size="11" text-anchor="end" fill="var(--muted)">100,000</text>
<line x1="60" y1="104.3" x2="1052" y2="104.3" class="grid"/>
<text x="52" y="108.3" font-size="11" text-anchor="end" fill="var(--muted)">120,000</text>
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
<line x1="61.9" y1="443.8" x2="61.9" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="445.7" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="65.7" y1="440.1" x2="65.7" y2="459.9" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="445.9" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="69.4" y1="433.4" x2="69.4" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="434.0" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="73.2" y1="428.7" x2="73.2" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="433.9" width="2.34" height="27.6" fill="var(--down)"/>
<line x1="77.0" y1="448.3" x2="77.0" y2="473.4" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="455.7" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="80.7" y1="455.3" x2="80.7" y2="491.8" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="455.7" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="84.5" y1="446.6" x2="84.5" y2="486.7" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="451.1" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="88.3" y1="411.5" x2="88.3" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="419.4" width="2.34" height="31.7" fill="var(--up)"/>
<line x1="92.1" y1="380.8" x2="92.1" y2="421.3" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="386.6" width="2.34" height="32.9" fill="var(--up)"/>
<line x1="95.8" y1="360.7" x2="95.8" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="386.7" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="99.6" y1="376.1" x2="99.6" y2="402.8" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="387.8" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="103.4" y1="373.6" x2="103.4" y2="395.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="378.1" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="107.1" y1="351.7" x2="107.1" y2="382.9" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="367.7" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="110.9" y1="363.8" x2="110.9" y2="414.9" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="367.5" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="114.7" y1="397.2" x2="114.7" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="400.4" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="118.5" y1="398.4" x2="118.5" y2="476.9" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="407.2" width="2.34" height="38.3" fill="var(--down)"/>
<line x1="122.2" y1="433.1" x2="122.2" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="442.0" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="126.0" y1="441.5" x2="126.0" y2="463.7" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="441.9" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="129.8" y1="433.7" x2="129.8" y2="463.8" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="438.5" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="133.6" y1="433.0" x2="133.6" y2="462.6" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="438.6" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="137.3" y1="454.5" x2="137.3" y2="487.5" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="455.3" width="2.34" height="26.2" fill="var(--down)"/>
<line x1="141.1" y1="470.1" x2="141.1" y2="491.7" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="475.7" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="144.9" y1="474.3" x2="144.9" y2="518.0" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="475.7" width="2.34" height="33.0" fill="var(--down)"/>
<line x1="148.6" y1="496.4" x2="148.6" y2="523.7" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="500.8" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="152.4" y1="478.7" x2="152.4" y2="508.3" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="479.1" width="2.34" height="21.7" fill="var(--up)"/>
<line x1="156.2" y1="463.4" x2="156.2" y2="482.3" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="479.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="160.0" y1="468.2" x2="160.0" y2="499.9" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="480.3" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="163.7" y1="490.7" x2="163.7" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="498.4" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="167.5" y1="466.2" x2="167.5" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="498.4" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="171.3" y1="478.8" x2="171.3" y2="504.0" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="498.3" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="175.0" y1="479.6" x2="175.0" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="484.7" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="178.8" y1="457.8" x2="178.8" y2="487.5" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="457.8" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="182.6" y1="451.7" x2="182.6" y2="469.5" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="457.8" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="186.4" y1="456.4" x2="186.4" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="459.6" width="2.34" height="20.5" fill="var(--down)"/>
<line x1="190.1" y1="479.0" x2="190.1" y2="493.8" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="480.1" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="193.9" y1="476.8" x2="193.9" y2="497.0" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="492.1" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="197.7" y1="487.3" x2="197.7" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="493.3" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="201.4" y1="491.2" x2="201.4" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="498.1" width="2.34" height="21.3" fill="var(--down)"/>
<line x1="205.2" y1="518.7" x2="205.2" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="519.4" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="209.0" y1="532.7" x2="209.0" y2="545.3" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="532.8" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="212.8" y1="536.2" x2="212.8" y2="547.4" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="537.6" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="216.5" y1="528.2" x2="216.5" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="539.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="220.3" y1="530.9" x2="220.3" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="539.5" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="224.1" y1="554.5" x2="224.1" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="554.8" width="2.34" height="29.9" fill="var(--down)"/>
<line x1="227.8" y1="578.7" x2="227.8" y2="588.9" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="582.4" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="231.6" y1="580.2" x2="231.6" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="582.4" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="235.4" y1="576.2" x2="235.4" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="583.2" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="239.2" y1="579.6" x2="239.2" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="583.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="242.9" y1="567.1" x2="242.9" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="574.8" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="246.7" y1="565.3" x2="246.7" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="571.2" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="250.5" y1="570.1" x2="250.5" y2="575.3" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="571.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="254.3" y1="563.3" x2="254.3" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="566.5" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="258.0" y1="562.5" x2="258.0" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="566.5" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="261.8" y1="578.6" x2="261.8" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="580.0" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="265.6" y1="584.7" x2="265.6" y2="589.3" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="587.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="269.3" y1="578.8" x2="269.3" y2="593.9" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="578.8" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="273.1" y1="574.4" x2="273.1" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="578.8" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="276.9" y1="588.9" x2="276.9" y2="595.6" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="590.2" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="280.7" y1="585.7" x2="280.7" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="592.0" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="284.4" y1="585.4" x2="284.4" y2="592.1" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="590.0" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="288.2" y1="587.9" x2="288.2" y2="595.5" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="590.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="292.0" y1="589.0" x2="292.0" y2="593.3" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="589.4" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="295.7" y1="582.6" x2="295.7" y2="591.2" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="584.3" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="299.5" y1="580.4" x2="299.5" y2="586.9" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="582.9" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="303.3" y1="582.3" x2="303.3" y2="608.2" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="582.9" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="307.1" y1="601.3" x2="307.1" y2="607.3" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="605.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="310.8" y1="603.0" x2="310.8" y2="608.6" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="604.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="314.6" y1="600.9" x2="314.6" y2="606.4" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="601.2" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="318.4" y1="600.0" x2="318.4" y2="603.1" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="601.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="322.1" y1="595.5" x2="322.1" y2="603.9" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="601.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="325.9" y1="601.8" x2="325.9" y2="604.8" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="602.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="329.7" y1="602.0" x2="329.7" y2="604.7" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="602.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="333.5" y1="601.4" x2="333.5" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="601.4" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="337.2" y1="582.2" x2="337.2" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="583.1" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="341.0" y1="571.5" x2="341.0" y2="584.7" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="574.2" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="344.8" y1="568.4" x2="344.8" y2="575.7" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="569.1" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="348.5" y1="567.2" x2="348.5" y2="574.5" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="569.1" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="352.3" y1="571.1" x2="352.3" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="573.1" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="356.1" y1="562.6" x2="356.1" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="566.5" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="359.9" y1="562.6" x2="359.9" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="566.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="363.6" y1="568.6" x2="363.6" y2="576.7" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="570.2" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="367.4" y1="574.9" x2="367.4" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="575.6" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="371.2" y1="546.6" x2="371.2" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="548.5" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="375.0" y1="544.8" x2="375.0" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="548.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="378.7" y1="543.1" x2="378.7" y2="555.4" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="547.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="382.5" y1="545.1" x2="382.5" y2="552.2" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="547.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="386.3" y1="534.2" x2="386.3" y2="547.8" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="537.5" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="390.0" y1="536.8" x2="390.0" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="537.5" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="393.8" y1="539.1" x2="393.8" y2="553.2" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="542.6" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="397.6" y1="539.9" x2="397.6" y2="550.3" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="542.8" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="401.4" y1="545.5" x2="401.4" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="546.5" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="405.1" y1="550.4" x2="405.1" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="553.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="408.9" y1="547.8" x2="408.9" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="548.3" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="412.7" y1="546.6" x2="412.7" y2="555.6" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="548.3" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="416.4" y1="551.9" x2="416.4" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="552.9" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="420.2" y1="554.7" x2="420.2" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="556.7" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="424.0" y1="532.3" x2="424.0" y2="556.9" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="536.7" width="2.34" height="20.0" fill="var(--up)"/>
<line x1="427.8" y1="533.0" x2="427.8" y2="541.0" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="536.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="431.5" y1="532.0" x2="431.5" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="536.0" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="435.3" y1="530.3" x2="435.3" y2="539.2" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="537.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="439.1" y1="537.4" x2="439.1" y2="541.2" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="537.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="442.8" y1="538.6" x2="442.8" y2="544.2" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="538.7" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="446.6" y1="539.1" x2="446.6" y2="545.5" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="542.5" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="450.4" y1="538.2" x2="450.4" y2="545.2" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="542.5" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="454.2" y1="540.7" x2="454.2" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="542.5" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="457.9" y1="554.6" x2="457.9" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="557.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="461.7" y1="548.3" x2="461.7" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="557.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="465.5" y1="556.4" x2="465.5" y2="561.3" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="558.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="469.2" y1="554.3" x2="469.2" y2="563.5" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="555.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="473.0" y1="551.2" x2="473.0" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="555.8" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="476.8" y1="548.5" x2="476.8" y2="558.3" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="548.8" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="480.6" y1="546.3" x2="480.6" y2="552.5" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="548.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="484.3" y1="548.8" x2="484.3" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="549.0" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="488.1" y1="537.7" x2="488.1" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="539.1" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="491.9" y1="514.2" x2="491.9" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="517.1" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="495.7" y1="510.5" x2="495.7" y2="519.3" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="514.7" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="499.4" y1="500.8" x2="499.4" y2="517.1" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="505.0" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="503.2" y1="500.6" x2="503.2" y2="515.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="503.4" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="507.0" y1="498.4" x2="507.0" y2="511.7" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="502.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="490.1" x2="510.7" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="490.9" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="514.5" y1="468.0" x2="514.5" y2="490.8" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="472.5" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="518.3" y1="472.3" x2="518.3" y2="489.6" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="472.4" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="522.1" y1="469.6" x2="522.1" y2="488.2" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="476.2" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="525.8" y1="472.4" x2="525.8" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="476.2" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="529.6" y1="462.2" x2="529.6" y2="486.8" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="471.7" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="533.4" y1="447.4" x2="533.4" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="471.7" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="537.1" y1="473.5" x2="537.1" y2="489.3" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="482.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="540.9" y1="477.2" x2="540.9" y2="497.9" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="480.9" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="544.7" y1="472.2" x2="544.7" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="478.3" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="548.5" y1="449.5" x2="548.5" y2="479.8" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="450.7" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="552.2" y1="428.8" x2="552.2" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="432.2" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="556.0" y1="428.2" x2="556.0" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="432.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="559.8" y1="375.2" x2="559.8" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="378.8" width="2.34" height="55.2" fill="var(--up)"/>
<line x1="563.5" y1="345.4" x2="563.5" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="350.6" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="567.3" y1="327.7" x2="567.3" y2="372.2" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="350.6" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="571.1" y1="351.2" x2="571.1" y2="390.2" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="353.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="574.9" y1="337.5" x2="574.9" y2="363.1" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="339.4" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="578.6" y1="339.3" x2="578.6" y2="372.1" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="339.4" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="582.4" y1="332.7" x2="582.4" y2="389.7" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="348.9" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="586.2" y1="360.9" x2="586.2" y2="395.8" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="366.4" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="589.9" y1="359.2" x2="589.9" y2="382.4" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="370.3" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="593.7" y1="371.4" x2="593.7" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="374.7" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="597.5" y1="367.6" x2="597.5" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="374.6" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="601.3" y1="357.0" x2="601.3" y2="390.4" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="363.8" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="605.0" y1="336.4" x2="605.0" y2="364.7" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="353.0" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="608.8" y1="342.9" x2="608.8" y2="362.1" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="353.0" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="612.6" y1="336.6" x2="612.6" y2="357.5" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="347.5" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="616.3" y1="345.1" x2="616.3" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="347.5" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="620.1" y1="359.4" x2="620.1" y2="378.8" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="362.1" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="623.9" y1="378.2" x2="623.9" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="378.8" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="627.7" y1="375.9" x2="627.7" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="381.2" width="2.34" height="33.0" fill="var(--down)"/>
<line x1="631.4" y1="387.7" x2="631.4" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="390.3" width="2.34" height="23.9" fill="var(--up)"/>
<line x1="635.2" y1="353.7" x2="635.2" y2="390.7" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="354.7" width="2.34" height="35.5" fill="var(--up)"/>
<line x1="639.0" y1="348.7" x2="639.0" y2="377.4" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="354.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="642.8" y1="345.9" x2="642.8" y2="407.6" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="354.2" width="2.34" height="49.0" fill="var(--down)"/>
<line x1="646.5" y1="381.2" x2="646.5" y2="446.7" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="400.3" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="650.3" y1="386.0" x2="650.3" y2="412.7" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="400.3" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="654.1" y1="370.0" x2="654.1" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="373.2" width="2.34" height="28.3" fill="var(--up)"/>
<line x1="657.8" y1="372.4" x2="657.8" y2="407.6" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="373.2" width="2.34" height="33.9" fill="var(--down)"/>
<line x1="661.6" y1="395.0" x2="661.6" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="407.0" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="665.4" y1="391.0" x2="665.4" y2="420.2" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="398.1" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="669.2" y1="374.2" x2="669.2" y2="406.2" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="376.5" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="672.9" y1="362.8" x2="672.9" y2="381.4" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="366.9" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="676.7" y1="366.9" x2="676.7" y2="394.7" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="366.9" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="680.5" y1="372.7" x2="680.5" y2="399.5" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="380.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="684.2" y1="348.9" x2="684.2" y2="382.3" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="350.7" width="2.34" height="29.7" fill="var(--up)"/>
<line x1="688.0" y1="348.4" x2="688.0" y2="369.1" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="350.7" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="691.8" y1="328.6" x2="691.8" y2="358.0" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="351.9" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="695.6" y1="290.4" x2="695.6" y2="361.3" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="295.2" width="2.34" height="56.7" fill="var(--up)"/>
<line x1="699.3" y1="232.6" x2="699.3" y2="296.2" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="250.0" width="2.34" height="45.3" fill="var(--up)"/>
<line x1="703.1" y1="202.6" x2="703.1" y2="252.1" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="210.5" width="2.34" height="39.5" fill="var(--up)"/>
<line x1="706.9" y1="206.1" x2="706.9" y2="245.5" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="210.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="710.6" y1="182.1" x2="710.6" y2="239.6" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="194.9" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="714.4" y1="176.5" x2="714.4" y2="228.3" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="180.2" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="718.2" y1="161.0" x2="718.2" y2="238.7" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="180.2" width="2.34" height="44.4" fill="var(--down)"/>
<line x1="722.0" y1="201.5" x2="722.0" y2="237.6" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="224.6" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="725.7" y1="206.0" x2="725.7" y2="242.9" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="209.1" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="729.5" y1="187.8" x2="729.5" y2="243.3" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="209.1" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="733.3" y1="170.5" x2="733.3" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="195.7" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="737.0" y1="156.9" x2="737.0" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="188.0" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="740.8" y1="169.9" x2="740.8" y2="219.2" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="188.0" width="2.34" height="24.1" fill="var(--down)"/>
<line x1="744.6" y1="188.8" x2="744.6" y2="243.2" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="212.1" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="748.4" y1="206.6" x2="748.4" y2="229.4" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="217.8" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="752.1" y1="203.3" x2="752.1" y2="232.9" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="218.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="755.9" y1="217.8" x2="755.9" y2="306.0" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="218.9" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="759.7" y1="227.8" x2="759.7" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="228.7" width="2.34" height="65.9" fill="var(--down)"/>
<line x1="763.5" y1="272.1" x2="763.5" y2="313.8" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="285.1" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="767.2" y1="261.6" x2="767.2" y2="291.8" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="268.3" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="771.0" y1="255.2" x2="771.0" y2="289.9" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="268.2" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="774.8" y1="256.6" x2="774.8" y2="311.5" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="286.2" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="778.5" y1="268.5" x2="778.5" y2="324.4" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="279.7" width="2.34" height="26.4" fill="var(--up)"/>
<line x1="782.3" y1="266.5" x2="782.3" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="272.5" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="786.1" y1="221.4" x2="786.1" y2="272.7" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="231.1" width="2.34" height="41.5" fill="var(--up)"/>
<line x1="789.9" y1="211.0" x2="789.9" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="228.4" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="793.6" y1="176.9" x2="793.6" y2="232.8" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="181.1" width="2.34" height="47.3" fill="var(--up)"/>
<line x1="797.4" y1="169.0" x2="797.4" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="169.8" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="801.2" y1="143.1" x2="801.2" y2="190.7" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="157.3" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="804.9" y1="149.0" x2="804.9" y2="185.8" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="157.3" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="808.7" y1="168.0" x2="808.7" y2="198.8" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="172.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="812.5" y1="149.9" x2="812.5" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="172.9" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="816.3" y1="157.8" x2="816.3" y2="209.2" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="174.1" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="820.0" y1="159.7" x2="820.0" y2="202.3" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="160.4" width="2.34" height="35.7" fill="var(--up)"/>
<line x1="823.8" y1="150.0" x2="823.8" y2="176.0" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="156.3" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="827.6" y1="107.0" x2="827.6" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="108.6" width="2.34" height="47.7" fill="var(--up)"/>
<line x1="831.3" y1="89.4" x2="831.3" y2="124.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="108.6" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="835.1" y1="103.0" x2="835.1" y2="129.6" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="107.0" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="838.9" y1="105.2" x2="838.9" y2="143.2" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="106.9" width="2.34" height="25.3" fill="var(--down)"/>
<line x1="842.7" y1="107.6" x2="842.7" y2="139.6" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="107.7" width="2.34" height="24.6" fill="var(--up)"/>
<line x1="846.4" y1="82.8" x2="846.4" y2="119.5" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="107.7" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="850.2" y1="115.8" x2="850.2" y2="147.5" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="116.6" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="854.0" y1="135.0" x2="854.0" y2="165.0" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="135.9" width="2.34" height="25.2" fill="var(--down)"/>
<line x1="857.7" y1="136.4" x2="857.7" y2="165.8" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="147.0" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="861.5" y1="119.9" x2="861.5" y2="149.6" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="126.5" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="865.3" y1="114.4" x2="865.3" y2="131.1" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="126.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="869.1" y1="126.4" x2="869.1" y2="158.8" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="127.0" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="872.8" y1="77.5" x2="872.8" y2="144.9" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="87.3" width="2.34" height="55.0" fill="var(--up)"/>
<line x1="876.6" y1="74.4" x2="876.6" y2="178.8" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="87.3" width="2.34" height="40.3" fill="var(--down)"/>
<line x1="880.4" y1="123.5" x2="880.4" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="127.7" width="2.34" height="31.4" fill="var(--down)"/>
<line x1="884.2" y1="127.2" x2="884.2" y2="168.2" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="131.0" width="2.34" height="28.0" fill="var(--up)"/>
<line x1="887.9" y1="122.3" x2="887.9" y2="170.1" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="131.0" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="891.7" y1="148.9" x2="891.7" y2="205.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="149.5" width="2.34" height="28.6" fill="var(--down)"/>
<line x1="895.5" y1="165.0" x2="895.5" y2="234.9" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="178.1" width="2.34" height="50.9" fill="var(--down)"/>
<line x1="899.2" y1="220.6" x2="899.2" y2="294.3" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="229.0" width="2.34" height="35.6" fill="var(--down)"/>
<line x1="903.0" y1="234.9" x2="903.0" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="247.3" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="906.8" y1="229.6" x2="906.8" y2="278.9" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="247.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="910.6" y1="227.0" x2="910.6" y2="260.6" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="247.2" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="914.3" y1="247.9" x2="914.3" y2="276.1" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="255.9" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="918.1" y1="246.8" x2="918.1" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="255.9" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="921.9" y1="240.9" x2="921.9" y2="265.1" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="242.4" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="925.6" y1="226.2" x2="925.6" y2="252.9" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="242.4" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="929.4" y1="211.2" x2="929.4" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="231.7" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="933.2" y1="231.5" x2="933.2" y2="268.5" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="231.6" width="2.34" height="34.2" fill="var(--down)"/>
<line x1="937.0" y1="247.1" x2="937.0" y2="318.3" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="265.8" width="2.34" height="46.3" fill="var(--down)"/>
<line x1="940.7" y1="301.1" x2="940.7" y2="393.8" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="312.2" width="2.34" height="32.4" fill="var(--down)"/>
<line x1="944.5" y1="339.2" x2="944.5" y2="369.5" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="344.7" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="948.3" y1="345.5" x2="948.3" y2="366.9" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="351.7" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="952.0" y1="346.1" x2="952.0" y2="381.8" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="357.1" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="955.8" y1="326.3" x2="955.8" y2="368.5" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="365.3" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="959.6" y1="326.9" x2="959.6" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="332.4" width="2.34" height="32.9" fill="var(--up)"/>
<line x1="963.4" y1="316.9" x2="963.4" y2="358.5" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="332.3" width="2.34" height="23.9" fill="var(--down)"/>
<line x1="967.1" y1="336.2" x2="967.1" y2="370.1" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="356.2" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="970.9" y1="349.5" x2="970.9" y2="366.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="350.7" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="974.7" y1="327.6" x2="974.7" y2="356.7" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="342.2" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="978.4" y1="305.6" x2="978.4" y2="343.0" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="327.2" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="982.2" y1="300.1" x2="982.2" y2="327.6" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="304.0" width="2.34" height="23.2" fill="var(--up)"/>
<line x1="986.0" y1="300.0" x2="986.0" y2="321.9" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="304.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="989.8" y1="284.0" x2="989.8" y2="306.1" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="287.2" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="993.5" y1="286.3" x2="993.5" y2="313.1" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="287.2" width="2.34" height="22.8" fill="var(--down)"/>
<line x1="997.3" y1="306.7" x2="997.3" y2="325.3" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="310.0" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="1001.1" y1="307.2" x2="1001.1" y2="334.1" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="312.1" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="1004.9" y1="326.7" x2="1004.9" y2="398.4" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="328.5" width="2.34" height="50.0" fill="var(--down)"/>
<line x1="1008.6" y1="366.4" x2="1008.6" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="366.6" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="1012.4" y1="359.1" x2="1012.4" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="366.5" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="1016.2" y1="367.4" x2="1016.2" y2="403.4" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="378.5" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="1019.9" y1="375.1" x2="1019.9" y2="405.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="377.0" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="1023.7" y1="371.6" x2="1023.7" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="376.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1027.5" y1="367.5" x2="1027.5" y2="385.6" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="371.5" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="1031.3" y1="360.8" x2="1031.3" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="368.3" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="1035.0" y1="366.8" x2="1035.0" y2="383.3" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="368.3" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="1038.8" y1="368.0" x2="1038.8" y2="383.4" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="370.7" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="1042.6" y1="368.4" x2="1042.6" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="370.7" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="1046.3" y1="345.8" x2="1046.3" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="349.4" width="2.34" height="31.1" fill="var(--up)"/>
<line x1="1050.1" y1="334.7" x2="1050.1" y2="351.0" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="335.3" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="60" y1="332.1" x2="1052" y2="332.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="335.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$72,848 R1</text>
<text x="1058" y="347.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="158.9" x2="1052" y2="158.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="162.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$108,692 R2</text>
<text x="1058" y="174.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="78.6" x2="1052" y2="78.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="82.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$125,328 R3</text>
<text x="1058" y="94.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="407.9" x2="1052" y2="407.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="401.9" font-size="11.5" fill="var(--support)" font-weight="600">$57,152 S1</text>
<text x="1058" y="413.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="563.9" x2="1052" y2="563.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="557.9" font-size="11.5" fill="var(--support)" font-weight="600">$24,864 S2</text>
<text x="1058" y="569.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="335.3" r="3" fill="var(--ink)"/>
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

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **상승**: 위험선호 확대, 유동성 완화 기대, 디지털 자산에 대한 제도적 수요 확대 신호로 흔히 해석된다.
- **하락**: 위험회피 심리, 유동성 긴축, 규제 리스크 부각 신호로 흔히 해석된다.
- 이 레포에서 다루는 다른 자산보다 변동성이 훨씬 크고 상관관계가 시기마다 달라진다(위험자산과 동행할 때도, 독립적으로 움직일 때도 있다) — [`digital_asset_finance`](../../../sectors/digital_asset_finance/00_overview.md) 섹터 회사의 실적을 이해하는 배경 자료로만 쓰고, 다른 섹터 문서의 근거로 끌어오지 않는다.

---

## 갱신 방법

이 문서는 시점이 지나면 낡는 스냅샷이라, 정기적으로(예: 분기 1회) 재생성해 §1을 교체하는 것을 전제로 한다(§2는 손으로 갱신). 손으로 만들지 말고 아래 명령으로 생성할 것:

```bash
uv run python scripts/gen_technical_chart.py "BTC-USD" --name "비트코인" --interval 1wk \
  --adj-note "BTC/USD 원자료(조정 없음, 24시간 시장이라 주 마지막 거래일 기준 종가)" \
  --close-on <YYYY-MM-DD> --emit chart
```

`--symbol`·`--unit-label`은 기본값($/USD)이 그대로 맞아 생략했다. 커맨드 문법은 [`../../authoring-guide.md`](../../authoring-guide.md) "주가가 아닌 시계열에 쓰기" 참고.

---

## 관련 문서

- [디지털 자산 금융 섹터 개요](../../../sectors/digital_asset_finance/00_overview.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — 거시 지표를 이 레포에서 어디까지 쓰는지
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Bitcoin USD (BTC-USD)](https://finance.yahoo.com/quote/BTC-USD/)

---

*작성일: 2026-08-20*
