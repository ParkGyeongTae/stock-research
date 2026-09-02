# 이더리움 (ETH/USD)

!!! note ""
    최근 5년간 이더리움 대 달러(ETH/USD, `ETH-USD`) 주간 가격을 지지선·저항선과 함께 정리한 참고 자료다. 이더리움은 비트코인과 달리 스마트 컨트랙트를 실행하는 범용 블록체인 플랫폼이라, 가격이 단순한 투기·저장 수요뿐 아니라 디파이(DeFi)·NFT 같은 온체인 활동 수요, 지분증명(PoS) 스테이킹 수익률과도 함께 움직인다. 가상자산 거래소·보관(커스터디) 서비스, 이더리움을 보유하거나 스테이킹 인프라를 제공하는 회사들의 실적·평가손익은 이 가격에 그대로 연동되는 경우가 많다.

    ⚠️ 이더리움도 비트코인처럼 **주식과 달리 1년 365일, 하루 24시간 거래**된다. 그래서 이 차트의 "한 주의 마지막 거래일"이 주식시장처럼 금요일이 아니라 주말이 될 수 있고, 거래량을 세는 단위도 주식과 다르다.

---

## 1. 차트 — 최근 5년 주봉

<div class="eth-usd-chart">
<style>
.eth-usd-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .eth-usd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eth-usd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eth-usd-chart svg { width:100%; height:auto; display:block; }
.eth-usd-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eth-usd-chart .title { fill: var(--ink); font-weight:600; }
.eth-usd-chart .grid { stroke: var(--grid); stroke-width:1; }
.eth-usd-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="이더리움(ETH-USD) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">이더리움 (ETH-USD) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-29 · 마지막 종가 $2,432.80 (2026-08-29) · 단위 USD</text>
<line x1="60" y1="593.2" x2="1052" y2="593.2" class="grid"/>
<text x="52" y="597.2" font-size="11" text-anchor="end" fill="var(--muted)">1,000.00</text>
<line x1="60" y1="462.2" x2="1052" y2="462.2" class="grid"/>
<text x="52" y="466.2" font-size="11" text-anchor="end" fill="var(--muted)">2,000.00</text>
<line x1="60" y1="331.2" x2="1052" y2="331.2" class="grid"/>
<text x="52" y="335.2" font-size="11" text-anchor="end" fill="var(--muted)">3,000.00</text>
<line x1="60" y1="200.1" x2="1052" y2="200.1" class="grid"/>
<text x="52" y="204.1" font-size="11" text-anchor="end" fill="var(--muted)">4,000.00</text>
<line x1="60" y1="69.1" x2="1052" y2="69.1" class="grid"/>
<text x="52" y="73.1" font-size="11" text-anchor="end" fill="var(--muted)">5,000.00</text>
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
<line x1="61.9" y1="294.1" x2="61.9" y2="310.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="298.8" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="65.7" y1="197.2" x2="65.7" y2="311.3" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="206.4" width="2.34" height="95.0" fill="var(--up)"/>
<line x1="69.4" y1="204.3" x2="69.4" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="206.5" width="2.34" height="70.9" fill="var(--down)"/>
<line x1="73.2" y1="242.9" x2="73.2" y2="315.2" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="277.8" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="77.0" y1="286.2" x2="77.0" y2="373.6" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="288.0" width="2.34" height="35.0" fill="var(--down)"/>
<line x1="80.7" y1="267.7" x2="80.7" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="276.4" width="2.34" height="46.2" fill="var(--up)"/>
<line x1="84.5" y1="243.6" x2="84.5" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="275.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="88.3" y1="205.1" x2="88.3" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="220.2" width="2.34" height="56.0" fill="var(--up)"/>
<line x1="92.1" y1="152.2" x2="92.1" y2="241.2" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="188.6" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="95.8" y1="140.4" x2="95.8" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="162.4" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="99.6" y1="113.0" x2="99.6" y2="179.0" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="118.8" width="2.34" height="43.5" fill="var(--up)"/>
<line x1="103.4" y1="87.5" x2="103.4" y2="136.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="118.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="107.1" y1="83.3" x2="107.1" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="118.0" width="2.34" height="46.8" fill="var(--down)"/>
<line x1="110.9" y1="128.0" x2="110.9" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="161.6" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="114.7" y1="97.8" x2="114.7" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="161.2" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="118.5" y1="136.9" x2="118.5" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="174.1" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="122.2" y1="181.0" x2="122.2" y2="244.1" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="182.3" width="2.34" height="28.0" fill="var(--down)"/>
<line x1="126.0" y1="180.6" x2="126.0" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="191.3" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="129.8" y1="183.6" x2="129.8" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="191.7" width="2.34" height="30.8" fill="var(--down)"/>
<line x1="133.6" y1="216.3" x2="133.6" y2="328.4" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="222.5" width="2.34" height="88.0" fill="var(--down)"/>
<line x1="137.3" y1="278.6" x2="137.3" y2="338.0" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="285.2" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="141.1" y1="284.5" x2="141.1" y2="418.9" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="285.2" width="2.34" height="106.9" fill="var(--down)"/>
<line x1="144.9" y1="369.7" x2="144.9" y2="439.6" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="383.1" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="148.6" y1="323.1" x2="148.6" y2="398.1" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="323.6" width="2.34" height="59.5" fill="var(--up)"/>
<line x1="152.4" y1="295.6" x2="152.4" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="323.6" width="2.34" height="22.8" fill="var(--down)"/>
<line x1="156.2" y1="306.9" x2="156.2" y2="385.4" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="346.9" width="2.34" height="33.0" fill="var(--down)"/>
<line x1="160.0" y1="350.9" x2="160.0" y2="421.7" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="380.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="163.7" y1="327.3" x2="163.7" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="380.8" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="167.5" y1="362.4" x2="167.5" y2="402.5" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="389.4" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="171.3" y1="333.8" x2="171.3" y2="396.0" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="349.5" width="2.34" height="44.8" fill="var(--up)"/>
<line x1="175.0" y1="293.0" x2="175.0" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="293.0" width="2.34" height="56.5" fill="var(--up)"/>
<line x1="178.8" y1="256.0" x2="178.8" y2="301.8" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="262.7" width="2.34" height="30.2" fill="var(--up)"/>
<line x1="182.6" y1="259.5" x2="182.6" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="262.7" width="2.34" height="40.7" fill="var(--down)"/>
<line x1="186.4" y1="303.1" x2="186.4" y2="336.7" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="303.7" width="2.34" height="28.3" fill="var(--down)"/>
<line x1="190.1" y1="308.4" x2="190.1" y2="345.1" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="332.0" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="193.9" y1="327.7" x2="193.9" y2="366.9" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="341.3" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="197.7" y1="336.8" x2="197.7" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="353.8" width="2.34" height="40.6" fill="var(--down)"/>
<line x1="201.4" y1="393.0" x2="201.4" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="394.3" width="2.34" height="48.8" fill="var(--down)"/>
<line x1="205.2" y1="443.1" x2="205.2" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="443.1" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="209.0" y1="451.7" x2="209.0" y2="498.7" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="456.7" width="2.34" height="30.2" fill="var(--down)"/>
<line x1="212.8" y1="461.5" x2="212.8" y2="495.4" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="486.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="216.5" y1="473.3" x2="216.5" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="487.7" width="2.34" height="47.2" fill="var(--down)"/>
<line x1="220.3" y1="534.4" x2="220.3" y2="606.9" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="535.1" width="2.34" height="41.4" fill="var(--down)"/>
<line x1="224.1" y1="557.6" x2="224.1" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="567.1" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="227.8" y1="562.6" x2="227.8" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="567.1" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="231.6" y1="558.8" x2="231.6" y2="586.9" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="571.2" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="235.4" y1="543.7" x2="235.4" y2="590.7" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="548.9" width="2.34" height="22.3" fill="var(--up)"/>
<line x1="239.2" y1="507.5" x2="239.2" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="514.7" width="2.34" height="34.2" fill="var(--up)"/>
<line x1="242.9" y1="491.7" x2="242.9" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="503.9" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="246.7" y1="495.7" x2="246.7" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="501.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="250.5" y1="459.2" x2="250.5" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="470.5" width="2.34" height="31.1" fill="var(--up)"/>
<line x1="254.3" y1="461.3" x2="254.3" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="470.5" width="2.34" height="41.6" fill="var(--down)"/>
<line x1="258.0" y1="499.1" x2="258.0" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="512.1" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="261.8" y1="509.0" x2="261.8" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="517.6" width="2.34" height="19.3" fill="var(--up)"/>
<line x1="265.6" y1="490.4" x2="265.6" y2="527.7" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="493.4" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="269.3" y1="491.3" x2="269.3" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="493.4" width="2.34" height="55.9" fill="var(--down)"/>
<line x1="273.1" y1="542.4" x2="273.1" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="549.3" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="276.9" y1="541.2" x2="276.9" y2="558.1" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="554.7" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="280.7" y1="543.4" x2="280.7" y2="557.7" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="551.0" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="284.4" y1="548.7" x2="284.4" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="551.0" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="288.2" y1="545.1" x2="288.2" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="545.6" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="292.0" y1="507.8" x2="292.0" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="515.8" width="2.34" height="29.8" fill="var(--up)"/>
<line x1="295.7" y1="506.6" x2="295.7" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="515.9" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="299.5" y1="514.0" x2="299.5" y2="582.3" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="518.3" width="2.34" height="45.9" fill="var(--down)"/>
<line x1="303.3" y1="556.0" x2="303.3" y2="575.2" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="564.2" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="307.1" y1="563.5" x2="307.1" y2="582.6" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="567.7" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="310.8" y1="553.7" x2="310.8" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="556.5" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="314.6" y1="553.6" x2="314.6" y2="563.8" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="556.6" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="318.4" y1="547.9" x2="318.4" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="558.7" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="322.1" y1="563.5" x2="322.1" y2="572.2" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="564.5" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="325.9" y1="563.0" x2="325.9" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="564.6" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="329.7" y1="555.6" x2="329.7" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="555.6" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="333.5" y1="519.4" x2="333.5" y2="555.7" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="520.8" width="2.34" height="34.7" fill="var(--up)"/>
<line x1="337.2" y1="504.9" x2="337.2" y2="526.5" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="510.9" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="341.0" y1="507.6" x2="341.0" y2="523.7" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="508.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="344.8" y1="500.9" x2="344.8" y2="521.6" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="508.6" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="348.5" y1="503.0" x2="348.5" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="510.5" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="352.3" y1="497.2" x2="352.3" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="503.9" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="356.1" y1="499.4" x2="356.1" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="503.8" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="359.9" y1="505.2" x2="359.9" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="509.3" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="363.6" y1="513.7" x2="363.6" y2="543.6" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="515.9" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="367.4" y1="482.7" x2="367.4" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="490.3" width="2.34" height="25.5" fill="var(--up)"/>
<line x1="371.2" y1="481.4" x2="371.2" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="490.3" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="375.0" y1="482.6" x2="375.0" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="489.0" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="378.7" y1="470.4" x2="378.7" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="480.6" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="382.5" y1="444.2" x2="382.5" y2="482.1" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="446.5" width="2.34" height="34.1" fill="var(--up)"/>
<line x1="386.3" y1="446.3" x2="386.3" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="446.5" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="390.0" y1="467.1" x2="390.0" y2="489.4" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="478.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="393.8" y1="459.9" x2="393.8" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="478.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="397.6" y1="477.0" x2="397.6" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="478.9" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="401.4" y1="482.4" x2="401.4" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="487.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="405.1" y1="473.3" x2="405.1" y2="493.2" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="473.9" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="408.9" y1="471.8" x2="408.9" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="474.1" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="412.7" y1="475.8" x2="412.7" y2="498.7" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="476.6" width="2.34" height="18.0" fill="var(--down)"/>
<line x1="416.4" y1="492.8" x2="416.4" y2="511.5" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="494.6" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="420.2" y1="471.0" x2="420.2" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="475.2" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="424.0" y1="467.7" x2="424.0" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="470.4" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="427.8" y1="465.5" x2="427.8" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="470.3" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="431.5" y1="458.8" x2="431.5" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="472.2" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="435.3" y1="470.6" x2="435.3" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="472.2" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="439.1" y1="476.7" x2="439.1" y2="483.6" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="476.8" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="442.8" y1="478.3" x2="442.8" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="480.3" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="446.6" y1="478.7" x2="446.6" y2="487.8" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="483.3" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="450.4" y1="481.4" x2="450.4" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="483.3" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="454.2" y1="502.0" x2="454.2" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="503.5" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="457.9" y1="495.9" x2="457.9" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="507.1" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="461.7" y1="507.1" x2="461.7" y2="514.1" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="509.9" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="465.5" y1="507.8" x2="465.5" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="511.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="469.2" y1="505.6" x2="469.2" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="511.6" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="473.0" y1="494.9" x2="473.0" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="497.1" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="476.8" y1="495.8" x2="476.8" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="497.2" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="480.6" y1="510.0" x2="480.6" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="510.2" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="484.3" y1="505.8" x2="484.3" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="506.3" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="488.1" y1="479.9" x2="488.1" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="489.0" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="491.9" y1="473.8" x2="491.9" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="476.1" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="495.7" y1="444.6" x2="495.7" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="456.3" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="499.4" y1="447.0" x2="499.4" y2="473.9" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="456.3" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="503.2" y1="444.8" x2="503.2" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="453.9" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="507.0" y1="434.3" x2="507.0" y2="463.8" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="436.8" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="510.7" y1="409.6" x2="510.7" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="416.0" width="2.34" height="20.8" fill="var(--up)"/>
<line x1="514.5" y1="415.7" x2="514.5" y2="442.5" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="416.0" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="518.3" y1="417.4" x2="518.3" y2="446.5" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="427.4" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="522.1" y1="403.9" x2="522.1" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="425.3" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="525.8" y1="405.7" x2="525.8" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="425.1" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="529.6" y1="369.1" x2="529.6" y2="439.7" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="400.3" width="2.34" height="32.7" fill="var(--up)"/>
<line x1="533.4" y1="381.8" x2="533.4" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="400.4" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="537.1" y1="401.5" x2="537.1" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="402.6" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="540.9" y1="411.3" x2="540.9" y2="431.1" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="424.3" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="544.7" y1="391.8" x2="544.7" y2="426.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="395.7" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="548.5" y1="345.2" x2="548.5" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="347.0" width="2.34" height="48.7" fill="var(--up)"/>
<line x1="552.2" y1="315.8" x2="552.2" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="316.4" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="556.0" y1="263.2" x2="556.0" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="266.8" width="2.34" height="49.6" fill="var(--up)"/>
<line x1="559.8" y1="200.3" x2="559.8" y2="301.8" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="215.7" width="2.34" height="51.3" fill="var(--up)"/>
<line x1="563.5" y1="188.0" x2="563.5" y2="276.9" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="215.7" width="2.34" height="31.3" fill="var(--down)"/>
<line x1="567.3" y1="247.0" x2="567.3" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="247.0" width="2.34" height="24.6" fill="var(--down)"/>
<line x1="571.1" y1="242.2" x2="571.1" y2="275.9" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="246.3" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="574.9" y1="246.2" x2="574.9" y2="304.2" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="246.3" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="578.6" y1="235.8" x2="578.6" y2="349.2" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="271.7" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="582.4" y1="294.8" x2="582.4" y2="348.4" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="310.6" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="586.2" y1="285.2" x2="586.2" y2="321.8" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="296.7" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="589.9" y1="293.8" x2="589.9" y2="355.3" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="296.8" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="593.7" y1="302.3" x2="593.7" y2="346.8" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="313.2" width="2.34" height="27.4" fill="var(--down)"/>
<line x1="597.5" y1="311.9" x2="597.5" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="321.8" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="601.3" y1="207.5" x2="601.3" y2="324.6" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="223.0" width="2.34" height="98.8" fill="var(--up)"/>
<line x1="605.0" y1="203.6" x2="605.0" y2="239.2" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="222.9" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="608.8" y1="214.9" x2="608.8" y2="250.5" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="228.9" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="612.6" y1="238.0" x2="612.6" y2="283.2" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="238.7" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="616.3" y1="248.1" x2="616.3" y2="282.5" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="249.6" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="620.1" y1="267.9" x2="620.1" y2="299.2" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="274.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="623.9" y1="263.9" x2="623.9" y2="354.0" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="274.5" width="2.34" height="65.9" fill="var(--down)"/>
<line x1="627.7" y1="296.3" x2="627.7" y2="353.9" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="299.2" width="2.34" height="41.2" fill="var(--up)"/>
<line x1="631.4" y1="259.5" x2="631.4" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="260.9" width="2.34" height="38.1" fill="var(--up)"/>
<line x1="635.2" y1="257.8" x2="635.2" y2="319.5" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="260.9" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="639.0" y1="279.2" x2="639.0" y2="378.4" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="295.6" width="2.34" height="76.7" fill="var(--down)"/>
<line x1="642.8" y1="367.6" x2="642.8" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="372.3" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="646.5" y1="360.6" x2="646.5" y2="394.9" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="381.8" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="650.3" y1="354.8" x2="650.3" y2="391.6" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="364.0" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="654.1" y1="362.2" x2="654.1" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="364.0" width="2.34" height="42.1" fill="var(--down)"/>
<line x1="657.8" y1="388.4" x2="657.8" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="406.1" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="661.6" y1="401.6" x2="661.6" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="420.2" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="665.4" y1="379.4" x2="665.4" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="385.8" width="2.34" height="34.3" fill="var(--up)"/>
<line x1="669.2" y1="366.8" x2="669.2" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="375.8" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="672.9" y1="375.4" x2="672.9" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="375.8" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="676.7" y1="394.0" x2="676.7" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="400.9" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="680.5" y1="363.1" x2="680.5" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="364.4" width="2.34" height="36.5" fill="var(--up)"/>
<line x1="684.2" y1="361.9" x2="684.2" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="364.4" width="2.34" height="31.5" fill="var(--down)"/>
<line x1="688.0" y1="367.8" x2="688.0" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="396.0" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="691.8" y1="298.4" x2="691.8" y2="415.1" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="306.1" width="2.34" height="96.3" fill="var(--up)"/>
<line x1="695.6" y1="273.0" x2="695.6" y2="329.1" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="306.1" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="699.3" y1="265.7" x2="699.3" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="283.5" width="2.34" height="37.7" fill="var(--up)"/>
<line x1="703.1" y1="233.2" x2="703.1" y2="297.7" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="238.0" width="2.34" height="45.4" fill="var(--up)"/>
<line x1="706.9" y1="187.9" x2="706.9" y2="265.1" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="199.4" width="2.34" height="38.7" fill="var(--up)"/>
<line x1="710.6" y1="199.0" x2="710.6" y2="263.0" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="199.3" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="714.4" y1="186.1" x2="714.4" y2="318.3" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="206.5" width="2.34" height="88.3" fill="var(--down)"/>
<line x1="718.2" y1="260.0" x2="718.2" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="285.4" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="722.0" y1="242.9" x2="722.0" y2="292.0" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="248.1" width="2.34" height="37.3" fill="var(--up)"/>
<line x1="725.7" y1="233.7" x2="725.7" y2="310.3" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="248.1" width="2.34" height="48.2" fill="var(--down)"/>
<line x1="729.5" y1="262.3" x2="729.5" y2="341.6" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="296.3" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="733.3" y1="273.0" x2="733.3" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="300.2" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="737.0" y1="273.8" x2="737.0" y2="363.2" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="300.3" width="2.34" height="48.1" fill="var(--down)"/>
<line x1="740.8" y1="341.7" x2="740.8" y2="441.3" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="348.5" width="2.34" height="31.4" fill="var(--down)"/>
<line x1="744.6" y1="358.1" x2="744.6" y2="390.0" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="375.3" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="748.4" y1="350.7" x2="748.4" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="354.6" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="752.1" y1="352.3" x2="752.1" y2="452.2" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="354.7" width="2.34" height="39.4" fill="var(--down)"/>
<line x1="755.9" y1="393.8" x2="755.9" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="394.1" width="2.34" height="66.0" fill="var(--down)"/>
<line x1="759.7" y1="442.5" x2="759.7" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="460.2" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="763.5" y1="453.2" x2="763.5" y2="478.9" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="461.5" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="767.2" y1="448.8" x2="767.2" y2="492.4" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="461.5" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="771.0" y1="468.6" x2="771.0" y2="522.6" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="487.6" width="2.34" height="30.1" fill="var(--down)"/>
<line x1="774.8" y1="503.2" x2="774.8" y2="542.6" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="515.1" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="778.5" y1="502.8" x2="778.5" y2="522.5" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="515.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="782.3" y1="481.0" x2="782.3" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="489.3" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="786.1" y1="478.9" x2="786.1" y2="496.8" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="487.3" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="789.9" y1="383.2" x2="789.9" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="395.3" width="2.34" height="91.9" fill="var(--up)"/>
<line x1="793.6" y1="365.6" x2="793.6" y2="417.0" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="395.3" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="797.4" y1="366.4" x2="797.4" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="389.9" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="801.2" y1="359.4" x2="801.2" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="390.0" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="804.9" y1="373.4" x2="804.9" y2="411.4" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="391.9" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="808.7" y1="347.2" x2="808.7" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="390.6" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="812.5" y1="373.1" x2="812.5" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="390.5" width="2.34" height="41.8" fill="var(--down)"/>
<line x1="816.3" y1="393.6" x2="816.3" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="396.6" width="2.34" height="35.7" fill="var(--up)"/>
<line x1="820.0" y1="379.0" x2="820.0" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="387.4" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="823.8" y1="326.2" x2="823.8" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="334.7" width="2.34" height="52.7" fill="var(--up)"/>
<line x1="827.6" y1="223.8" x2="827.6" y2="339.8" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="231.7" width="2.34" height="103.0" fill="var(--up)"/>
<line x1="831.3" y1="216.3" x2="831.3" y2="263.7" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="216.5" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="835.1" y1="207.9" x2="835.1" y2="284.3" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="216.5" width="2.34" height="49.5" fill="var(--down)"/>
<line x1="838.9" y1="156.6" x2="838.9" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="166.8" width="2.34" height="99.1" fill="var(--up)"/>
<line x1="842.7" y1="96.8" x2="842.7" y2="178.0" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="138.1" width="2.34" height="28.7" fill="var(--up)"/>
<line x1="846.4" y1="75.2" x2="846.4" y2="191.6" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="98.0" width="2.34" height="40.1" fill="var(--up)"/>
<line x1="850.2" y1="95.8" x2="850.2" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="98.0" width="2.34" height="51.1" fill="var(--down)"/>
<line x1="854.0" y1="135.9" x2="854.0" y2="171.1" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="149.1" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="857.7" y1="100.1" x2="857.7" y2="163.7" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="120.3" width="2.34" height="39.9" fill="var(--up)"/>
<line x1="861.5" y1="112.3" x2="861.5" y2="144.0" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="120.2" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="865.3" y1="140.2" x2="865.3" y2="222.5" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="141.0" width="2.34" height="40.6" fill="var(--down)"/>
<line x1="869.1" y1="119.4" x2="869.1" y2="188.6" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="132.6" width="2.34" height="49.0" fill="var(--up)"/>
<line x1="872.8" y1="101.2" x2="872.8" y2="270.9" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="132.6" width="2.34" height="46.0" fill="var(--down)"/>
<line x1="876.6" y1="161.8" x2="876.6" y2="242.2" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="178.6" width="2.34" height="23.5" fill="var(--down)"/>
<line x1="880.4" y1="176.9" x2="880.4" y2="237.1" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="179.4" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="884.2" y1="167.3" x2="884.2" y2="241.8" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="179.4" width="2.34" height="32.4" fill="var(--down)"/>
<line x1="887.9" y1="211.6" x2="887.9" y2="322.9" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="211.7" width="2.34" height="43.1" fill="var(--down)"/>
<line x1="891.7" y1="245.2" x2="891.7" y2="330.2" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="254.7" width="2.34" height="64.3" fill="var(--down)"/>
<line x1="895.5" y1="302.6" x2="895.5" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="319.0" width="2.34" height="38.2" fill="var(--down)"/>
<line x1="899.2" y1="318.7" x2="899.2" y2="362.2" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="332.2" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="903.0" y1="299.9" x2="903.0" y2="367.8" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="323.1" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="906.8" y1="272.6" x2="906.8" y2="326.6" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="323.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="910.6" y1="308.2" x2="910.6" y2="360.4" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="323.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="914.3" y1="321.6" x2="914.3" y2="345.7" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="331.0" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="918.1" y1="310.1" x2="918.1" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="312.7" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="921.9" y1="291.4" x2="921.9" y2="324.3" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="312.6" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="925.6" y1="279.0" x2="925.6" y2="322.3" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="294.3" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="929.4" y1="294.1" x2="929.4" y2="359.2" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="294.2" width="2.34" height="61.1" fill="var(--down)"/>
<line x1="933.2" y1="325.8" x2="933.2" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="355.3" width="2.34" height="71.8" fill="var(--down)"/>
<line x1="937.0" y1="410.7" x2="937.0" y2="495.1" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="427.1" width="2.34" height="23.4" fill="var(--down)"/>
<line x1="940.7" y1="443.2" x2="940.7" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="450.7" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="944.5" y1="457.3" x2="944.5" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="466.7" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="948.3" y1="443.1" x2="948.3" y2="487.9" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="467.7" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="952.0" y1="436.2" x2="952.0" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="470.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="955.8" y1="435.1" x2="955.8" y2="471.3" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="439.0" width="2.34" height="31.6" fill="var(--up)"/>
<line x1="959.6" y1="411.8" x2="959.6" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="438.9" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="963.4" y1="436.2" x2="963.4" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="455.3" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="967.1" y1="440.5" x2="967.1" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="447.9" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="970.9" y1="419.3" x2="970.9" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="437.0" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="974.7" y1="401.3" x2="974.7" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="427.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="978.4" y1="406.8" x2="978.4" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="413.8" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="982.2" y1="409.3" x2="982.2" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="413.7" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="986.0" y1="406.8" x2="986.0" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="413.8" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="989.8" y1="413.2" x2="989.8" y2="449.5" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="413.8" width="2.34" height="31.7" fill="var(--down)"/>
<line x1="993.5" y1="441.8" x2="993.5" y2="460.8" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="445.5" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="997.3" y1="444.1" x2="997.3" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="449.4" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="1001.1" y1="459.9" x2="1001.1" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="461.7" width="2.34" height="41.6" fill="var(--down)"/>
<line x1="1004.9" y1="497.7" x2="1004.9" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="498.3" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="1008.6" y1="482.2" x2="1008.6" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="498.3" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="1012.4" y1="491.4" x2="1012.4" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="500.9" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="1016.2" y1="487.6" x2="1016.2" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="490.6" width="2.34" height="27.9" fill="var(--up)"/>
<line x1="1019.9" y1="484.5" x2="1019.9" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="487.7" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="1023.7" y1="469.5" x2="1023.7" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="479.0" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="1027.5" y1="467.0" x2="1027.5" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="468.3" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="1031.3" y1="465.3" x2="1031.3" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="468.3" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="1035.0" y1="470.4" x2="1035.0" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="474.2" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="1038.8" y1="471.5" x2="1038.8" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="474.2" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="1042.6" y1="390.7" x2="1042.6" y2="479.1" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="401.4" width="2.34" height="77.3" fill="var(--up)"/>
<line x1="1046.3" y1="388.3" x2="1046.3" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="395.3" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="1050.1" y1="403.8" x2="1050.1" y2="405.7" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="404.2" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="60" y1="256.9" x2="1052" y2="256.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="260.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$3,567.02 R1</text>
<text x="1058" y="272.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="187.1" x2="1052" y2="187.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="190.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$4,099.62 R2</text>
<text x="1058" y="202.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="79.2" x2="1052" y2="79.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="82.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$4,922.72 R3</text>
<text x="1058" y="94.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="446.8" x2="1052" y2="446.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="440.8" font-size="11.5" fill="var(--support)" font-weight="600">$2,117.72 S1</text>
<text x="1058" y="452.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="525.8" x2="1052" y2="525.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="519.8" font-size="11.5" fill="var(--support)" font-weight="600">$1,514.87 S2</text>
<text x="1058" y="531.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="543.1" x2="1052" y2="543.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="537.1" font-size="11.5" fill="var(--support)" font-weight="600">$1,382.66 S3</text>
<text x="1058" y="549.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="405.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="397.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $2,432.80 (2026-08-29)</text>
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

## 2. 해석

- **상승**: 투자자들이 위험을 더 감수하려 하거나(위험선호 확대), 시중에 돈이 풀리는 국면(유동성 완화 기대)이거나, 디파이·NFT 등 온체인 활동 수요가 늘었다는 신호로 흔히 해석한다.
- **하락**: 위험을 피하려는 심리, 시중 유동성 긴축, 규제 리스크가 부각됐다는 신호로 흔히 해석한다.
- 다른 자산보다 가격이 훨씬 크게 오르내리고(변동성이 크고), 다른 자산과의 관계(상관관계)도 시기마다 달라진다 — 위험자산과 같이 움직일 때도 있고 따로 움직일 때도 있다. 그래서 디지털 자산 금융 섹터 회사의 실적을 이해하는 배경 자료로만 참고하고, 다른 섹터 문서의 판단 근거로 그대로 가져다 쓰지 않는다.
- **PoS 전환과 수수료 소각(EIP-1559)**: 이더리움은 2022년 9월 "The Merge"로 작업증명(PoW)에서 지분증명(PoS)으로 전환했고, 그 이후 신규 발행량이 큰 폭으로 줄었다. 여기에 EIP-1559 업그레이드로 거래 수수료 일부가 소각(burn)되는 구조가 더해져, 네트워크 사용량이 많은 시기에는 유통량이 오히려 줄어드는(디플레이셔너리) 구간도 나타난다. 미국 현물 ETF 승인(2024년) 이후 기관 자금이 들어오는 통로가 넓어진 것도 함께 감안한다.
- 비트코인과의 상대적인 강약(이더리움/비트코인 비율)은 [디지털자산 2종 비교](./comparison.md)에서 함께 볼 수 있다.

---

*작성일: 2026-08-29*
