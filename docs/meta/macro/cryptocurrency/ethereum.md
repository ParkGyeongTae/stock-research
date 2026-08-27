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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-23 · 마지막 종가 $2,464.08 (2026-08-23) · 단위 USD</text>
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
<line x1="133.8" y1="56.0" x2="133.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.8" y1="626.0" x2="133.8" y2="631.0" class="axis"/>
<text x="133.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="330.7" y1="56.0" x2="330.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="330.7" y1="626.0" x2="330.7" y2="631.0" class="axis"/>
<text x="330.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="527.6" y1="56.0" x2="527.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="527.6" y1="626.0" x2="527.6" y2="631.0" class="axis"/>
<text x="527.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="728.3" y1="56.0" x2="728.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="728.3" y1="626.0" x2="728.3" y2="631.0" class="axis"/>
<text x="728.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.2" y1="56.0" x2="925.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="925.2" y1="626.0" x2="925.2" y2="631.0" class="axis"/>
<text x="925.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="282.2" x2="61.9" y2="323.3" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="299.5" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="65.7" y1="197.2" x2="65.7" y2="311.3" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="206.4" width="2.35" height="95.0" fill="var(--up)"/>
<line x1="69.5" y1="204.3" x2="69.5" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="206.5" width="2.35" height="70.9" fill="var(--down)"/>
<line x1="73.3" y1="242.9" x2="73.3" y2="315.2" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="277.8" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="77.0" y1="286.2" x2="77.0" y2="373.6" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="288.0" width="2.35" height="35.0" fill="var(--down)"/>
<line x1="80.8" y1="267.7" x2="80.8" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="276.4" width="2.35" height="46.2" fill="var(--up)"/>
<line x1="84.6" y1="243.6" x2="84.6" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="275.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="88.4" y1="205.1" x2="88.4" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="220.2" width="2.35" height="56.0" fill="var(--up)"/>
<line x1="92.2" y1="152.2" x2="92.2" y2="241.2" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="188.6" width="2.35" height="31.5" fill="var(--up)"/>
<line x1="96.0" y1="140.4" x2="96.0" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="162.4" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="99.8" y1="113.0" x2="99.8" y2="179.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="118.8" width="2.35" height="43.5" fill="var(--up)"/>
<line x1="103.5" y1="87.5" x2="103.5" y2="136.6" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="118.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="107.3" y1="83.3" x2="107.3" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="118.0" width="2.35" height="46.8" fill="var(--down)"/>
<line x1="111.1" y1="128.0" x2="111.1" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="161.6" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="114.9" y1="97.8" x2="114.9" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="161.2" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="118.7" y1="136.9" x2="118.7" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="174.1" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="122.5" y1="181.0" x2="122.5" y2="244.1" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="182.3" width="2.35" height="28.0" fill="var(--down)"/>
<line x1="126.3" y1="180.6" x2="126.3" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="191.3" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="130.0" y1="183.6" x2="130.0" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="191.7" width="2.35" height="30.8" fill="var(--down)"/>
<line x1="133.8" y1="216.3" x2="133.8" y2="328.4" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="222.5" width="2.35" height="88.0" fill="var(--down)"/>
<line x1="137.6" y1="278.6" x2="137.6" y2="338.0" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="285.2" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="141.4" y1="284.5" x2="141.4" y2="418.9" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="285.2" width="2.35" height="106.9" fill="var(--down)"/>
<line x1="145.2" y1="369.7" x2="145.2" y2="439.6" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="383.1" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="149.0" y1="323.1" x2="149.0" y2="398.1" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="323.6" width="2.35" height="59.5" fill="var(--up)"/>
<line x1="152.8" y1="295.6" x2="152.8" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="323.6" width="2.35" height="22.8" fill="var(--down)"/>
<line x1="156.5" y1="306.9" x2="156.5" y2="385.4" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="346.9" width="2.35" height="33.0" fill="var(--down)"/>
<line x1="160.3" y1="350.9" x2="160.3" y2="421.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="380.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="164.1" y1="327.3" x2="164.1" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="380.8" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="167.9" y1="362.4" x2="167.9" y2="402.5" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="389.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="171.7" y1="333.8" x2="171.7" y2="396.0" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="349.5" width="2.35" height="44.8" fill="var(--up)"/>
<line x1="175.5" y1="293.0" x2="175.5" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="293.0" width="2.35" height="56.5" fill="var(--up)"/>
<line x1="179.3" y1="256.0" x2="179.3" y2="301.8" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="262.7" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="183.1" y1="259.5" x2="183.1" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="262.7" width="2.35" height="40.7" fill="var(--down)"/>
<line x1="186.8" y1="303.1" x2="186.8" y2="336.7" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="303.7" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="190.6" y1="308.4" x2="190.6" y2="345.1" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="332.0" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="194.4" y1="327.7" x2="194.4" y2="366.9" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="341.3" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="198.2" y1="336.8" x2="198.2" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="353.8" width="2.35" height="40.6" fill="var(--down)"/>
<line x1="202.0" y1="393.0" x2="202.0" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="394.3" width="2.35" height="48.8" fill="var(--down)"/>
<line x1="205.8" y1="443.1" x2="205.8" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="443.1" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="209.6" y1="451.7" x2="209.6" y2="498.7" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="456.7" width="2.35" height="30.2" fill="var(--down)"/>
<line x1="213.3" y1="461.5" x2="213.3" y2="495.4" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="486.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="217.1" y1="473.3" x2="217.1" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="487.7" width="2.35" height="47.2" fill="var(--down)"/>
<line x1="220.9" y1="534.4" x2="220.9" y2="606.9" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="535.1" width="2.35" height="41.4" fill="var(--down)"/>
<line x1="224.7" y1="557.6" x2="224.7" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="567.1" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="228.5" y1="562.6" x2="228.5" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="567.1" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="232.3" y1="558.8" x2="232.3" y2="586.9" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="571.2" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="236.1" y1="543.7" x2="236.1" y2="590.7" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="548.9" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="239.8" y1="507.5" x2="239.8" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="514.7" width="2.35" height="34.2" fill="var(--up)"/>
<line x1="243.6" y1="491.7" x2="243.6" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="503.9" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="247.4" y1="495.7" x2="247.4" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="501.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="251.2" y1="459.2" x2="251.2" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="470.5" width="2.35" height="31.1" fill="var(--up)"/>
<line x1="255.0" y1="461.3" x2="255.0" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="470.5" width="2.35" height="41.6" fill="var(--down)"/>
<line x1="258.8" y1="499.1" x2="258.8" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="512.1" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="262.6" y1="509.0" x2="262.6" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="517.6" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="266.4" y1="490.4" x2="266.4" y2="527.7" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="493.4" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="270.1" y1="491.3" x2="270.1" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="493.4" width="2.35" height="55.9" fill="var(--down)"/>
<line x1="273.9" y1="542.4" x2="273.9" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="549.3" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="277.7" y1="541.2" x2="277.7" y2="558.1" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="554.7" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="281.5" y1="543.4" x2="281.5" y2="557.7" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="551.0" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="285.3" y1="548.7" x2="285.3" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="551.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="289.1" y1="545.1" x2="289.1" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="545.6" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="292.9" y1="507.8" x2="292.9" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="515.8" width="2.35" height="29.8" fill="var(--up)"/>
<line x1="296.6" y1="506.6" x2="296.6" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="515.9" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="300.4" y1="514.0" x2="300.4" y2="582.3" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="518.3" width="2.35" height="45.9" fill="var(--down)"/>
<line x1="304.2" y1="556.0" x2="304.2" y2="575.2" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="564.2" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="308.0" y1="563.5" x2="308.0" y2="582.6" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="567.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="311.8" y1="553.7" x2="311.8" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="556.5" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="315.6" y1="553.6" x2="315.6" y2="563.8" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="556.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="319.4" y1="547.9" x2="319.4" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="558.7" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="323.1" y1="563.5" x2="323.1" y2="572.2" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="564.5" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="326.9" y1="563.0" x2="326.9" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="564.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="330.7" y1="555.6" x2="330.7" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="555.6" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="334.5" y1="519.4" x2="334.5" y2="555.7" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="520.8" width="2.35" height="34.7" fill="var(--up)"/>
<line x1="338.3" y1="504.9" x2="338.3" y2="526.5" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="510.9" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="342.1" y1="507.6" x2="342.1" y2="523.7" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="508.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="345.9" y1="500.9" x2="345.9" y2="521.6" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="508.6" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="349.6" y1="503.0" x2="349.6" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="510.5" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="353.4" y1="497.2" x2="353.4" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="503.9" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="357.2" y1="499.4" x2="357.2" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="503.8" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="361.0" y1="505.2" x2="361.0" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="509.3" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="364.8" y1="513.7" x2="364.8" y2="543.6" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="515.9" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="368.6" y1="482.7" x2="368.6" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="490.3" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="372.4" y1="481.4" x2="372.4" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="490.3" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="376.2" y1="482.6" x2="376.2" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="489.0" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="379.9" y1="470.4" x2="379.9" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="480.6" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="383.7" y1="444.2" x2="383.7" y2="482.1" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="446.5" width="2.35" height="34.1" fill="var(--up)"/>
<line x1="387.5" y1="446.3" x2="387.5" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="446.5" width="2.35" height="33.8" fill="var(--down)"/>
<line x1="391.3" y1="467.1" x2="391.3" y2="489.4" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="478.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="395.1" y1="459.9" x2="395.1" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="478.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="477.0" x2="398.9" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="478.9" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="402.7" y1="482.4" x2="402.7" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="487.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="406.4" y1="473.3" x2="406.4" y2="493.2" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="473.9" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="410.2" y1="471.8" x2="410.2" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="474.1" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="414.0" y1="475.8" x2="414.0" y2="498.7" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="476.6" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="417.8" y1="492.8" x2="417.8" y2="511.5" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="494.6" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="421.6" y1="471.0" x2="421.6" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="475.2" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="425.4" y1="467.7" x2="425.4" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="470.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="429.2" y1="465.5" x2="429.2" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="470.3" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="432.9" y1="458.8" x2="432.9" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="472.2" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="436.7" y1="470.6" x2="436.7" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="472.2" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="440.5" y1="476.7" x2="440.5" y2="483.6" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="476.8" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="444.3" y1="478.3" x2="444.3" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="480.3" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="448.1" y1="478.7" x2="448.1" y2="487.8" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="483.3" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="451.9" y1="481.4" x2="451.9" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="483.3" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="455.7" y1="502.0" x2="455.7" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="503.5" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="459.5" y1="495.9" x2="459.5" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="507.1" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="463.2" y1="507.1" x2="463.2" y2="514.1" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="509.9" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="467.0" y1="507.8" x2="467.0" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="511.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="470.8" y1="505.6" x2="470.8" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="511.6" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="474.6" y1="494.9" x2="474.6" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="497.1" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="478.4" y1="495.8" x2="478.4" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="497.2" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="482.2" y1="510.0" x2="482.2" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="510.2" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="486.0" y1="505.8" x2="486.0" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="506.3" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="489.7" y1="479.9" x2="489.7" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="489.0" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="493.5" y1="473.8" x2="493.5" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="476.1" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="497.3" y1="444.6" x2="497.3" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="456.3" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="501.1" y1="447.0" x2="501.1" y2="473.9" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="456.3" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="504.9" y1="444.8" x2="504.9" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="453.9" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="508.7" y1="434.3" x2="508.7" y2="463.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="436.8" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="512.5" y1="409.6" x2="512.5" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="416.0" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="516.2" y1="415.7" x2="516.2" y2="442.5" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="416.0" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="520.0" y1="417.4" x2="520.0" y2="446.5" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="427.4" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="523.8" y1="403.9" x2="523.8" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="425.3" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="527.6" y1="405.7" x2="527.6" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="425.1" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="531.4" y1="369.1" x2="531.4" y2="439.7" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="400.3" width="2.35" height="32.7" fill="var(--up)"/>
<line x1="535.2" y1="381.8" x2="535.2" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="400.4" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="539.0" y1="401.5" x2="539.0" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="402.6" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="542.7" y1="411.3" x2="542.7" y2="431.1" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="424.3" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="546.5" y1="391.8" x2="546.5" y2="426.8" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="395.7" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="550.3" y1="345.2" x2="550.3" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="347.0" width="2.35" height="48.7" fill="var(--up)"/>
<line x1="554.1" y1="315.8" x2="554.1" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="316.4" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="557.9" y1="263.2" x2="557.9" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="266.8" width="2.35" height="49.6" fill="var(--up)"/>
<line x1="561.7" y1="200.3" x2="561.7" y2="301.8" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="215.7" width="2.35" height="51.3" fill="var(--up)"/>
<line x1="565.5" y1="188.0" x2="565.5" y2="276.9" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="215.7" width="2.35" height="31.3" fill="var(--down)"/>
<line x1="569.3" y1="247.0" x2="569.3" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="247.0" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="573.0" y1="242.2" x2="573.0" y2="275.9" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="246.3" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="576.8" y1="246.2" x2="576.8" y2="304.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="246.3" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="580.6" y1="235.8" x2="580.6" y2="349.2" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="271.7" width="2.35" height="38.9" fill="var(--down)"/>
<line x1="584.4" y1="294.8" x2="584.4" y2="348.4" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="310.6" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="588.2" y1="285.2" x2="588.2" y2="321.8" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="296.7" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="592.0" y1="293.8" x2="592.0" y2="355.3" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="296.8" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="595.8" y1="302.3" x2="595.8" y2="346.8" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="313.2" width="2.35" height="27.4" fill="var(--down)"/>
<line x1="599.5" y1="311.9" x2="599.5" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="321.8" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="603.3" y1="207.5" x2="603.3" y2="324.6" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="223.0" width="2.35" height="98.8" fill="var(--up)"/>
<line x1="607.1" y1="203.6" x2="607.1" y2="239.2" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="222.9" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="610.9" y1="214.9" x2="610.9" y2="250.5" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="228.9" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="614.7" y1="238.0" x2="614.7" y2="283.2" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="238.7" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="618.5" y1="248.1" x2="618.5" y2="282.5" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="249.6" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="622.3" y1="267.9" x2="622.3" y2="299.2" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="274.4" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="626.0" y1="263.9" x2="626.0" y2="354.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="274.5" width="2.35" height="65.9" fill="var(--down)"/>
<line x1="629.8" y1="296.3" x2="629.8" y2="353.9" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="299.2" width="2.35" height="41.2" fill="var(--up)"/>
<line x1="633.6" y1="259.5" x2="633.6" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="260.9" width="2.35" height="38.1" fill="var(--up)"/>
<line x1="637.4" y1="257.8" x2="637.4" y2="319.5" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="260.9" width="2.35" height="34.7" fill="var(--down)"/>
<line x1="641.2" y1="279.2" x2="641.2" y2="378.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="295.6" width="2.35" height="76.7" fill="var(--down)"/>
<line x1="645.0" y1="367.6" x2="645.0" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="372.3" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="648.8" y1="360.6" x2="648.8" y2="394.9" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="381.8" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="652.5" y1="354.8" x2="652.5" y2="391.6" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="364.0" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="656.3" y1="362.2" x2="656.3" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="364.0" width="2.35" height="42.1" fill="var(--down)"/>
<line x1="660.1" y1="388.4" x2="660.1" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="406.1" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="663.9" y1="401.6" x2="663.9" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="420.2" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="667.7" y1="379.4" x2="667.7" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="385.8" width="2.35" height="34.3" fill="var(--up)"/>
<line x1="671.5" y1="366.8" x2="671.5" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="375.8" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="675.3" y1="375.4" x2="675.3" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="375.8" width="2.35" height="28.7" fill="var(--down)"/>
<line x1="679.1" y1="394.0" x2="679.1" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="400.9" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="682.8" y1="363.1" x2="682.8" y2="404.1" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="364.4" width="2.35" height="36.5" fill="var(--up)"/>
<line x1="686.6" y1="361.9" x2="686.6" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="364.4" width="2.35" height="31.5" fill="var(--down)"/>
<line x1="690.4" y1="367.8" x2="690.4" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="396.0" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="694.2" y1="298.4" x2="694.2" y2="415.1" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="306.1" width="2.35" height="96.3" fill="var(--up)"/>
<line x1="698.0" y1="273.0" x2="698.0" y2="329.1" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="306.1" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="701.8" y1="265.7" x2="701.8" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="283.5" width="2.35" height="37.7" fill="var(--up)"/>
<line x1="705.6" y1="233.2" x2="705.6" y2="297.7" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="238.0" width="2.35" height="45.4" fill="var(--up)"/>
<line x1="709.3" y1="187.9" x2="709.3" y2="265.1" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="199.4" width="2.35" height="38.7" fill="var(--up)"/>
<line x1="713.1" y1="199.0" x2="713.1" y2="263.0" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="199.3" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="716.9" y1="186.1" x2="716.9" y2="318.3" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="206.5" width="2.35" height="88.3" fill="var(--down)"/>
<line x1="720.7" y1="260.0" x2="720.7" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="285.4" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="724.5" y1="242.9" x2="724.5" y2="292.0" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="248.1" width="2.35" height="37.3" fill="var(--up)"/>
<line x1="728.3" y1="233.7" x2="728.3" y2="310.3" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="248.1" width="2.35" height="48.2" fill="var(--down)"/>
<line x1="732.1" y1="262.3" x2="732.1" y2="341.6" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="296.3" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="735.8" y1="273.0" x2="735.8" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="300.2" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="739.6" y1="273.8" x2="739.6" y2="363.2" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="300.3" width="2.35" height="48.1" fill="var(--down)"/>
<line x1="743.4" y1="341.7" x2="743.4" y2="441.3" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="348.5" width="2.35" height="31.4" fill="var(--down)"/>
<line x1="747.2" y1="358.1" x2="747.2" y2="390.0" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="375.3" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="751.0" y1="350.7" x2="751.0" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="354.6" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="754.8" y1="352.3" x2="754.8" y2="452.2" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="354.7" width="2.35" height="39.4" fill="var(--down)"/>
<line x1="758.6" y1="393.8" x2="758.6" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="394.1" width="2.35" height="66.0" fill="var(--down)"/>
<line x1="762.4" y1="442.5" x2="762.4" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="460.2" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="766.1" y1="453.2" x2="766.1" y2="478.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="461.5" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="769.9" y1="448.8" x2="769.9" y2="492.4" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="461.5" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="773.7" y1="468.6" x2="773.7" y2="522.6" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="487.6" width="2.35" height="30.1" fill="var(--down)"/>
<line x1="777.5" y1="503.2" x2="777.5" y2="542.6" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="515.1" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="781.3" y1="502.8" x2="781.3" y2="522.5" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="515.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="785.1" y1="481.0" x2="785.1" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="489.3" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="788.9" y1="478.9" x2="788.9" y2="496.8" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="487.3" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="792.6" y1="383.2" x2="792.6" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="395.3" width="2.35" height="91.9" fill="var(--up)"/>
<line x1="796.4" y1="365.6" x2="796.4" y2="417.0" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="395.3" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="800.2" y1="366.4" x2="800.2" y2="415.9" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="389.9" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="804.0" y1="359.4" x2="804.0" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="390.0" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="807.8" y1="373.4" x2="807.8" y2="411.4" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="391.9" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="811.6" y1="347.2" x2="811.6" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="390.6" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="815.4" y1="373.1" x2="815.4" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="390.5" width="2.35" height="41.8" fill="var(--down)"/>
<line x1="819.1" y1="393.6" x2="819.1" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="396.6" width="2.35" height="35.7" fill="var(--up)"/>
<line x1="822.9" y1="379.0" x2="822.9" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="387.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="826.7" y1="326.2" x2="826.7" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="334.7" width="2.35" height="52.7" fill="var(--up)"/>
<line x1="830.5" y1="223.8" x2="830.5" y2="339.8" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="231.7" width="2.35" height="103.0" fill="var(--up)"/>
<line x1="834.3" y1="216.3" x2="834.3" y2="263.7" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="216.5" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="838.1" y1="207.9" x2="838.1" y2="284.3" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="216.5" width="2.35" height="49.5" fill="var(--down)"/>
<line x1="841.9" y1="156.6" x2="841.9" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="166.8" width="2.35" height="99.1" fill="var(--up)"/>
<line x1="845.6" y1="96.8" x2="845.6" y2="178.0" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="138.1" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="849.4" y1="75.2" x2="849.4" y2="191.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="98.0" width="2.35" height="40.1" fill="var(--up)"/>
<line x1="853.2" y1="95.8" x2="853.2" y2="165.5" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="98.0" width="2.35" height="51.1" fill="var(--down)"/>
<line x1="857.0" y1="135.9" x2="857.0" y2="171.1" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="149.1" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="860.8" y1="100.1" x2="860.8" y2="163.7" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="120.3" width="2.35" height="39.9" fill="var(--up)"/>
<line x1="864.6" y1="112.3" x2="864.6" y2="144.0" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="120.2" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="868.4" y1="140.2" x2="868.4" y2="222.5" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="141.0" width="2.35" height="40.6" fill="var(--down)"/>
<line x1="872.2" y1="119.4" x2="872.2" y2="188.6" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="132.6" width="2.35" height="49.0" fill="var(--up)"/>
<line x1="875.9" y1="101.2" x2="875.9" y2="270.9" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="132.6" width="2.35" height="46.0" fill="var(--down)"/>
<line x1="879.7" y1="161.8" x2="879.7" y2="242.2" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="178.6" width="2.35" height="23.5" fill="var(--down)"/>
<line x1="883.5" y1="176.9" x2="883.5" y2="237.1" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="179.4" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="887.3" y1="167.3" x2="887.3" y2="241.8" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="179.4" width="2.35" height="32.4" fill="var(--down)"/>
<line x1="891.1" y1="211.6" x2="891.1" y2="322.9" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="211.7" width="2.35" height="43.1" fill="var(--down)"/>
<line x1="894.9" y1="245.2" x2="894.9" y2="330.2" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="254.7" width="2.35" height="64.3" fill="var(--down)"/>
<line x1="898.7" y1="302.6" x2="898.7" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="319.0" width="2.35" height="38.2" fill="var(--down)"/>
<line x1="902.4" y1="318.7" x2="902.4" y2="362.2" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="332.2" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="906.2" y1="299.9" x2="906.2" y2="367.8" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="323.1" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="910.0" y1="272.6" x2="910.0" y2="326.6" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="323.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="913.8" y1="308.2" x2="913.8" y2="360.4" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="323.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="917.6" y1="321.6" x2="917.6" y2="345.7" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="331.0" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="921.4" y1="310.1" x2="921.4" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="312.7" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="925.2" y1="291.4" x2="925.2" y2="324.3" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="312.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="928.9" y1="279.0" x2="928.9" y2="322.3" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="294.3" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="932.7" y1="294.1" x2="932.7" y2="359.2" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="294.2" width="2.35" height="61.1" fill="var(--down)"/>
<line x1="936.5" y1="325.8" x2="936.5" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="355.3" width="2.35" height="71.8" fill="var(--down)"/>
<line x1="940.3" y1="410.7" x2="940.3" y2="495.1" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="427.1" width="2.35" height="23.4" fill="var(--down)"/>
<line x1="944.1" y1="443.2" x2="944.1" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="450.7" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="947.9" y1="457.3" x2="947.9" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="466.7" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="951.7" y1="443.1" x2="951.7" y2="487.9" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="467.7" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="955.5" y1="436.2" x2="955.5" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="470.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="959.2" y1="435.1" x2="959.2" y2="471.3" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="439.0" width="2.35" height="31.6" fill="var(--up)"/>
<line x1="963.0" y1="411.8" x2="963.0" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="438.9" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="966.8" y1="436.2" x2="966.8" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="455.3" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="970.6" y1="440.5" x2="970.6" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="447.9" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="974.4" y1="419.3" x2="974.4" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="437.0" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="978.2" y1="401.3" x2="978.2" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="427.5" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="982.0" y1="406.8" x2="982.0" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="413.8" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="985.7" y1="409.3" x2="985.7" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="413.7" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="989.5" y1="406.8" x2="989.5" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="413.8" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="993.3" y1="413.2" x2="993.3" y2="449.5" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="413.8" width="2.35" height="31.7" fill="var(--down)"/>
<line x1="997.1" y1="441.8" x2="997.1" y2="460.8" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="445.5" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="1000.9" y1="444.1" x2="1000.9" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="449.4" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="1004.7" y1="459.9" x2="1004.7" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="461.7" width="2.35" height="41.6" fill="var(--down)"/>
<line x1="1008.5" y1="497.7" x2="1008.5" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="498.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="1012.2" y1="482.2" x2="1012.2" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="498.3" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="1016.0" y1="491.4" x2="1016.0" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="500.9" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="1019.8" y1="487.6" x2="1019.8" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="490.6" width="2.35" height="27.9" fill="var(--up)"/>
<line x1="1023.6" y1="484.5" x2="1023.6" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="487.7" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="1027.4" y1="469.5" x2="1027.4" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="479.0" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="1031.2" y1="467.0" x2="1031.2" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="468.3" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="1035.0" y1="465.3" x2="1035.0" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="468.3" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="1038.7" y1="470.4" x2="1038.7" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="474.2" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1042.5" y1="471.5" x2="1042.5" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="474.2" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="1046.3" y1="390.7" x2="1046.3" y2="479.1" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="406.6" width="2.35" height="72.1" fill="var(--up)"/>
<line x1="1050.1" y1="400.5" x2="1050.1" y2="414.1" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="401.4" width="2.35" height="5.3" fill="var(--up)"/>
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
<circle cx="1052.0" cy="401.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="393.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $2,464.08 (2026-08-23)</text>
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

*작성일: 2026-08-21 (최종 수정일: 2026-08-25)*
