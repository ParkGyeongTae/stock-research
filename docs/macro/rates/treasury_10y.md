# 미국 10년물 국채금리

::: info
만기 10년 미 국채의 상수만기 수익률이다(FRED `DGS10`). DCF 밸류에이션에서 "위험이 거의 없는 이자율(무위험이자율)"의 표준 기준으로 쓰이며, 이 금리의 국면에 따라 성장주의 밸류에이션 배수가 크게 달라진다.
:::

---

## 1. 차트 — 최근 5년 일간

<style>
.fred-dgs10 {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-dgs10:#eb6834;
}
.dark .fred-dgs10 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs10:#d95926; }
.fred-dgs10 svg { width:100%; height:auto; display:block; }
.fred-dgs10 text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-dgs10 .title { fill: var(--ink); font-weight:600; }
.fred-dgs10 .grid { stroke: var(--grid); stroke-width:1; }
.fred-dgs10 .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-dgs10">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미국 10년물 국채금리, 최근 5년 일간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 10년물 국채금리 (상수만기) (최근 5년 일간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-16 · 단위: % · 출처: FRED DGS10</text>
<line x1="60" y1="597.7" x2="1052" y2="597.7" class="grid"/>
<text x="52" y="601.7" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="472.0" x2="1052" y2="472.0" class="grid"/>
<text x="52" y="476.0" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="346.2" x2="1052" y2="346.2" class="grid"/>
<text x="52" y="350.2" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="220.5" x2="1052" y2="220.5" class="grid"/>
<text x="52" y="224.5" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="94.8" x2="1052" y2="94.8" class="grid"/>
<text x="52" y="98.8" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="125.7" y1="56" x2="125.7" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="125.7" y1="600" x2="125.7" y2="605" class="axis"/>
<text x="125.7" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.4" y1="56" x2="322.4" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.4" y1="600" x2="322.4" y2="605" class="axis"/>
<text x="322.4" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="519.1" y1="56" x2="519.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="519.1" y1="600" x2="519.1" y2="605" class="axis"/>
<text x="519.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.3" y1="56" x2="716.3" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.3" y1="600" x2="716.3" y2="605" class="axis"/>
<text x="716.3" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.0" y1="56" x2="913.0" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.0" y1="600" x2="913.0" y2="605" class="axis"/>
<text x="913.0" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<polyline points="60.0,558.7 60.5,561.2 61.1,556.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="63.2,549.9 63.8,553.7 64.3,560.0 64.8,553.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="66.5,556.2 67.0,562.5 67.5,558.7 68.1,554.9 68.6,551.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="70.2,558.7 70.8,556.2 71.3,557.5 71.9,546.1 72.4,538.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="74.0,537.3 74.5,529.8 75.1,528.5 75.6,532.3 76.2,537.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="77.8,536.1 78.3,529.8 78.9,531.1 79.4,524.8 79.9,521.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="82.1,523.5 82.6,527.3 83.2,532.3 83.7,523.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="85.3,523.5 85.9,516.0 86.4,516.0 86.9,512.2 87.5,514.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="89.1,517.2 89.6,518.5 90.2,529.8 90.7,526.0 91.3,528.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="92.9,524.8 93.4,527.3 93.9,522.2 94.5,531.1 95.0,541.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="96.6,533.6 97.2,539.9 97.7,527.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="98.8" cy="524.8" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="100.4,518.5 101.0,518.5 101.5,522.2 102.0,523.5 102.6,529.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="104.2,518.5 104.7,513.4 105.3,517.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="106.3" cy="537.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="108.0,532.3 108.5,543.6 109.0,543.6 109.6,542.4 110.1,553.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="111.7,543.6 112.3,537.3 112.8,532.3 113.3,536.1 113.9,537.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="115.5,544.9 116.0,542.4 116.6,538.6 117.1,542.4 117.7,546.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="119.3,543.6 119.8,537.3 120.3,539.9 120.9,534.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="123.0,537.3 123.6,536.1 124.1,528.5 124.7,532.3 125.2,532.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="126.8,518.5 127.4,514.7 127.9,508.4 128.4,505.9 129.0,502.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="130.6,499.6 131.1,503.4 131.7,504.6 132.2,509.7 132.7,499.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="134.9,488.3 135.4,493.3 136.0,493.3 136.5,503.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="138.1,503.4 138.7,499.6 139.2,490.8 139.7,495.8 140.3,499.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="141.9,498.4 142.4,495.8 143.0,499.6 143.5,494.6 144.1,480.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="145.7,482.0 146.2,477.0 146.8,479.5 147.3,468.2 147.8,482.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="149.4,474.5 150.0,465.7 150.5,468.2 151.1,475.7 151.6,482.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="153.8,479.5 154.3,473.2 154.8,477.0 155.4,475.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="157.0,493.3 157.5,507.2 158.1,489.6 158.6,489.6 159.1,504.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="160.8,499.6 161.3,489.6 161.8,479.5 162.4,474.5 162.9,472.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="164.5,454.4 165.1,453.1 165.6,448.1 166.2,446.8 166.7,454.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="168.3,431.7 168.8,424.2 169.4,431.7 169.9,429.2 170.5,411.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="172.1,414.1 172.6,420.4 173.2,428.0 173.7,431.7 174.2,422.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="175.9,419.2 176.4,404.1 176.9,395.3 177.5,389.0 178.0,381.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="179.6,372.6 180.2,381.4 180.7,383.9 181.2,367.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="183.4,365.1 183.9,355.0 184.5,365.1 185.0,358.8 185.5,358.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="187.2,370.1 187.7,375.1 188.2,368.9 188.8,365.1 189.3,360.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="190.9,347.5 191.5,350.0 192.0,355.0 192.6,339.9 193.1,331.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="194.7,339.9 195.2,347.5 195.8,357.5 196.3,366.3 196.9,355.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="198.5,361.3 199.0,348.7 199.6,360.1 200.1,366.3 200.6,373.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="202.3,363.8 202.8,376.4 203.3,377.7 203.9,377.7 204.4,378.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="206.6,365.1 207.1,353.8 207.6,356.3 208.2,351.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="209.8,341.2 210.3,348.7 210.9,342.5 211.4,341.2 212.0,327.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="213.6,292.2 214.1,284.6 214.6,304.7 215.2,311.0 215.7,314.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="217.9,307.3 218.4,326.1 219.0,334.9 219.5,329.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="221.1,321.1 221.7,321.1 222.2,333.7 222.7,348.7 223.3,361.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="225.4,368.9 226.0,355.0 226.5,345.0 227.0,334.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="228.7,347.5 229.2,351.3 229.7,357.5 230.3,351.3 230.8,355.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="232.4,351.3 233.0,345.0 233.5,341.2 234.0,357.5 234.6,375.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="236.2,370.1 236.7,370.1 237.3,373.9 237.8,386.5 238.4,387.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="240.0,396.5 240.5,377.7 241.0,380.2 241.6,386.5 242.1,367.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="243.7,375.1 244.3,371.4 244.8,373.9 245.4,362.6 245.9,366.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="247.5,372.6 248.1,368.9 248.6,360.1 249.1,361.3 249.7,348.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="251.3,342.5 251.8,339.9 252.4,332.4 252.9,342.5 253.4,341.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="255.1,331.1 255.6,332.4 256.1,327.4 256.7,313.5 257.2,321.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="259.4,304.7 259.9,312.3 260.4,309.8 261.0,304.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="262.6,299.7 263.1,293.4 263.7,294.7 264.2,289.7 264.8,289.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="266.4,284.6 266.9,274.6 267.5,282.1 268.0,258.2 268.5,259.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="270.1,235.6 270.7,224.3 271.2,255.7 271.8,250.7 272.3,241.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="273.9,262.0 274.5,268.3 275.0,250.7 275.5,241.9 276.1,234.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="278.2,229.3 278.8,231.8 279.3,224.3 279.8,220.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="281.5,218.0 282.0,219.2 282.5,202.9 283.1,190.3 283.6,194.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="285.2,189.1 285.8,207.9 286.3,215.5 286.9,225.5 287.4,218.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="289.0,207.9 289.5,211.7 290.1,207.9 290.6,202.9 291.2,199.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="292.8,192.8 293.3,202.9 293.9,205.4 294.4,243.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="296.5,235.6 297.1,245.6 297.6,262.0 298.2,249.4 298.7,243.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="300.3,241.9 300.9,250.7 301.4,257.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="302.5" cy="260.7" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="304.1,259.5 304.6,251.9 305.2,260.7 305.7,279.6 306.2,282.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="307.9,270.8 308.4,282.1 308.9,293.4 309.5,285.9 310.0,274.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="311.6,269.5 312.2,282.1 312.7,284.6 313.3,290.9 313.8,285.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="315.4,274.6 315.9,259.5 316.5,260.7 317.0,262.0 317.6,251.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="319.7,240.6 320.3,235.6 320.8,241.9 321.3,235.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="323.5,246.9 324.0,259.5 324.6,257.0 325.1,277.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="326.7,279.6 327.3,269.5 327.8,278.3 328.3,292.2 328.9,284.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="331.0,279.6 331.6,299.7 332.1,297.2 332.7,285.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="334.3,280.9 334.8,288.4 335.3,288.4 335.9,284.6 336.4,280.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="338.0,277.1 338.6,280.9 339.1,297.2 339.7,295.9 340.2,279.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="341.8,267.0 342.4,262.0 342.9,267.0 343.4,262.0 344.0,253.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="345.6,255.7 346.1,249.4 346.7,244.4 347.2,238.1 347.7,243.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="349.9,226.8 350.4,229.3 351.0,235.6 351.5,226.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="353.1,230.6 353.7,230.6 354.2,219.2 354.7,210.4 355.3,224.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="356.9,223.0 357.4,224.3 358.0,223.0 358.5,229.3 359.1,258.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="360.7,277.1 361.2,265.8 361.7,282.1 362.3,275.8 362.8,297.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="364.4,287.1 365.0,272.1 365.5,285.9 366.1,298.5 366.6,298.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="368.2,279.6 368.8,277.1 369.3,274.6 369.8,277.1 370.4,285.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="372.0,292.2 372.5,302.2 373.1,308.5 373.6,308.5 374.1,297.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="375.8,294.7 376.3,292.2 376.8,294.7 377.4,289.7 377.9,280.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="379.5,270.8 380.1,273.3 380.6,270.8 381.1,278.3 381.7,274.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="383.3,280.9 383.8,295.9 384.4,292.2 384.9,279.6 385.5,290.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="387.1,272.1 387.6,290.9 388.2,298.5 388.7,299.7 389.2,290.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="390.8,280.9 391.4,279.6 391.9,292.2 392.5,297.2 393.0,288.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="394.6,283.4 395.2,278.3 395.7,274.6 396.2,264.5 396.8,258.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="398.4,255.7 398.9,258.2 399.5,254.4 400.0,241.9 400.5,245.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="402.7,259.5 403.2,265.8 403.8,269.5 404.3,259.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="405.9,259.5 406.5,258.2 407.0,246.9 407.6,254.4 408.1,251.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="409.7,254.4 410.2,240.6 410.8,241.9 411.3,255.7 411.9,249.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="414.0,253.2 414.6,255.7 415.1,245.6 415.6,253.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="417.2,255.7 417.8,249.4 418.3,257.0 418.9,239.4 419.4,244.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="421.0" cy="238.1" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="422.1,226.8 422.6,214.2 423.2,213.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="424.8,219.2 425.3,221.8 425.9,238.1 426.4,250.7 426.9,241.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="428.6,244.4 429.1,245.6 429.6,251.9 430.2,239.4 430.7,240.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="432.3,238.1 432.9,231.8 433.4,238.1 434.0,219.2 434.5,225.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="436.1,224.3 436.6,214.2 437.2,210.4 437.7,195.4 438.3,214.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="439.9,209.2 440.4,218.0 441.0,220.5 441.5,209.2 442.0,200.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="443.7,196.6 444.2,194.1 444.7,185.3 445.3,182.8 445.8,187.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="447.4,177.8 448.0,177.8 448.5,196.6 449.0,191.6 449.6,189.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="451.2,195.4 451.7,205.4 452.3,205.4 452.8,209.2 453.4,197.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="455.5,186.6 456.0,182.8 456.6,186.6 457.1,187.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="458.7,184.0 459.3,186.6 459.8,189.1 460.4,184.0 460.9,179.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="462.5,180.3 463.1,174.0 463.6,176.5 464.1,158.9 464.7,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="466.3,151.4 466.8,150.1 467.4,143.8 467.9,146.3 468.4,146.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="470.1,133.8 470.6,118.7 471.1,128.7 471.7,130.0 472.2,122.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="474.4,137.5 474.9,147.6 475.4,132.5 476.0,141.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="477.6,131.2 478.1,116.1 478.7,106.1 479.2,97.3 479.8,103.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="481.4,112.4 481.9,116.1 482.4,101.1 483.0,112.4 483.5,114.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="485.1,109.9 485.7,109.9 486.2,123.7 486.8,136.3 487.3,148.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="488.9,136.3 489.5,147.6 490.0,158.9 490.5,142.6 491.1,143.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="492.7,141.3 493.2,165.2 493.8,153.9 494.3,163.9 494.8,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="496.5,167.7 497.0,169.0 497.5,167.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="498.6" cy="161.4" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="500.2,171.5 500.8,177.8 501.3,186.6 501.8,174.0 502.4,192.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="504.0,185.3 504.5,197.9 505.1,205.4 505.6,202.9 506.2,191.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="507.8,191.6 508.3,195.4 508.9,215.5 509.4,230.6 509.9,231.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="511.5,226.8 512.1,229.3 512.6,238.1 513.2,234.3 513.7,233.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="515.9,234.3 516.4,246.9 516.9,240.6 517.5,235.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="519.6,226.8 520.2,231.8 520.7,221.8 521.2,214.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="522.9,219.2 523.4,218.0 523.9,215.5 524.5,223.0 525.0,225.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="527.2,211.7 527.7,207.9 528.2,202.9 528.8,201.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="530.4,206.7 530.9,202.9 531.5,197.9 532.0,202.9 532.6,201.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="534.2,210.4 534.7,213.0 535.3,221.8 535.8,236.8 536.3,216.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="537.9,199.1 538.5,209.2 539.0,209.2 539.6,201.6 540.1,199.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="541.7,199.1 542.3,181.5 542.8,186.6 543.3,190.3 543.9,182.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="546.0,186.6 546.6,180.3 547.1,179.0 547.6,187.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="549.3,185.3 549.8,181.5 550.3,186.6 550.9,189.1 551.4,196.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="553.0,192.8 553.6,204.2 554.1,206.7 554.7,209.2 555.2,209.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="556.8,207.9 557.3,200.4 557.9,196.6 558.4,184.0 559.0,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="560.6,177.8 561.1,182.8 561.7,186.6 562.2,186.6 562.7,192.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="564.4,189.1 564.9,190.3 565.4,195.4 566.0,195.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="568.1,179.0 568.7,175.2 569.2,175.2 569.7,181.5 570.3,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="571.9,167.7 572.4,175.2 573.0,151.4 573.5,150.1 574.1,157.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="575.7,141.3 576.2,136.3 576.7,146.3 577.3,140.0 577.8,142.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="579.4,142.6 580.0,143.8 580.5,138.8 581.1,132.5 581.6,136.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="583.2,141.3 583.8,133.8 584.3,141.3 584.8,147.6 585.4,157.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="587.0,158.9 587.5,161.4 588.1,160.2 588.6,163.9 589.1,157.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="590.8,160.2 591.3,163.9 591.8,175.2 592.4,172.7 592.9,167.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="594.5,165.2 595.1,169.0 595.6,166.4 596.1,161.4 596.7,162.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="598.8,152.6 599.4,143.8 599.9,151.4 600.5,156.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="602.1,169.0 602.6,179.0 603.1,184.0 603.7,185.3 604.2,166.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="605.8,161.4 606.4,171.5 606.9,181.5 607.5,190.3 608.0,195.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="609.6,185.3 610.2,192.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="611.2,189.1 611.8,189.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="613.4,189.1 613.9,191.6 614.5,180.3 615.0,184.0 615.5,175.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="617.2,160.2 617.7,166.4 618.2,175.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="619.3" cy="185.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="620.9,185.3 621.5,182.8 622.0,185.3 622.5,195.4 623.1,197.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="624.7,191.6 625.2,199.1 625.8,200.4 626.3,195.4 626.9,189.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="628.5,187.8 629.0,189.1 629.6,185.3 630.1,186.6 630.6,195.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="632.2,199.1 632.8,201.6 633.3,209.2 633.9,221.8 634.4,245.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="636.0,248.2 636.6,233.1 637.1,225.5 637.6,221.8 638.2,228.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="639.8,233.1 640.3,239.4 640.9,241.9 641.4,230.6 641.9,234.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="643.6,238.1 644.1,243.1 644.6,246.9 645.2,238.1 645.7,244.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="647.3,243.1 647.9,241.9 648.4,240.6 648.9,236.8 649.5,231.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="651.6,240.6 652.2,249.4 652.7,254.4 653.3,255.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="654.9,258.2 655.4,264.5 656.0,264.5 656.5,260.7 657.0,263.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="658.6,267.0 659.2,264.5 659.7,258.2 660.3,254.4 660.8,254.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="662.4,251.9 663.0,253.2 663.5,246.9 664.0,246.9 664.6,251.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="666.2,244.4 666.7,253.2 667.3,246.9 667.8,239.4 668.3,223.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="670.0,216.7 670.5,215.5 671.0,213.0 671.6,209.2 672.1,210.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="674.3,216.7 674.8,218.0 675.4,209.2 675.9,210.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="677.5,196.6 678.0,195.4 678.6,190.3 679.1,194.1 679.7,189.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="681.3,185.3 681.8,185.3 682.4,184.0 682.9,185.3 683.4,174.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="685.1,181.5 685.6,187.8 686.1,167.7 686.7,181.5 687.2,182.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="689.4,166.4 689.9,165.2 690.4,166.4 691.0,166.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="692.6,167.7 693.1,171.5 693.7,169.0 694.2,166.4 694.8,169.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="696.4,186.6 696.9,182.8 697.4,189.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="698.5" cy="197.9" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="700.1,196.6 700.7,191.6 701.2,196.6 701.8,199.1 702.3,201.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="703.9,195.4 704.4,192.8 705.0,187.8 705.5,180.3 706.1,170.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="707.7,171.5 708.2,170.2 708.8,157.6 709.3,148.8 709.8,155.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="711.5,146.3 712.0,146.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="713.1,147.6 713.6,142.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="715.2,151.4 715.8,147.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="716.8,148.8 717.4,145.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="719.0,142.6 719.5,136.3 720.1,136.3 720.6,135.0 721.2,123.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="722.8,121.2 723.3,122.4 723.8,137.5 724.4,143.8 724.9,143.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="727.1,148.8 727.6,145.1 728.2,138.8 728.7,141.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="730.3,153.9 730.9,151.4 731.4,151.4 731.9,155.1 732.5,147.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="734.1,152.6 734.6,155.1 735.2,166.4 735.7,163.9 736.2,158.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="737.9,156.4 738.4,152.6 738.9,142.6 739.5,155.1 740.0,161.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="742.2,151.4 742.7,153.9 743.2,157.6 743.8,167.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="745.4,170.2 745.9,182.8 746.5,189.1 747.0,184.0 747.6,190.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="749.2,200.4 749.7,192.8 750.3,185.3 750.8,184.0 751.3,180.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="752.9,192.8 753.5,185.3 754.0,180.3 754.6,186.6 755.1,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="756.7,181.5 757.3,184.0 757.8,189.1 758.3,190.3 758.9,189.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="760.5,177.8 761.0,181.5 761.6,176.5 762.1,172.7 762.6,186.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="764.3,191.6 764.8,199.1 765.3,195.4 765.9,213.0 766.4,219.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="768.0,201.6 768.6,187.8 769.1,177.8 769.6,170.2 770.2,160.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="771.8,172.7 772.3,176.5 772.9,184.0 773.4,177.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="775.6,167.7 776.1,169.0 776.7,170.2 777.2,180.3 777.7,184.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="779.3,191.6 779.9,196.6 780.4,199.1 781.0,189.1 781.5,179.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="783.1,175.2 783.7,182.8 784.2,187.8 784.7,174.0 785.3,174.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="786.9,163.9 787.4,158.9 788.0,153.9 788.5,163.9 789.0,166.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="790.7,162.7 791.2,160.2 791.7,147.6 792.3,152.6 792.8,156.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="795.0,166.4 795.5,161.4 796.1,166.4 796.6,169.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="798.2,162.7 798.7,162.7 799.3,174.0 799.8,170.2 800.4,156.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="802.0,158.9 802.5,161.4 803.1,169.0 803.6,175.2 804.1,169.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="805.8,162.7 806.3,171.5 806.8,172.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="807.9" cy="172.7" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="809.5,177.8 810.1,182.8 810.6,184.0 811.1,187.8 811.7,184.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="813.3,190.3 813.8,187.8 814.4,182.8 814.9,176.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="817.1,170.2 817.6,167.7 818.1,177.8 818.7,176.5 819.2,166.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="820.8,166.4 821.4,157.6 821.9,162.7 822.5,161.4 823.0,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="824.6,172.7 825.1,176.5 825.7,170.2 826.2,166.4 826.8,170.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="828.4,167.7 828.9,177.8 829.5,172.7 830.0,174.0 830.5,191.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="832.2,192.8 832.7,192.8 833.2,192.8 833.8,191.6 834.3,186.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="835.9,186.6 836.5,184.0 837.0,190.3 837.5,184.0 838.1,179.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="839.7,177.8 840.2,182.8 840.8,184.0 841.3,179.0 841.9,187.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="843.5,185.3 844.0,187.8 844.5,190.3 845.1,192.8 845.6,191.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="847.8,185.3 848.3,192.8 848.9,199.1 849.4,207.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="851.0,214.2 851.6,210.4 852.1,215.5 852.6,219.2 853.2,213.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="854.8,214.2 855.3,215.5 855.9,213.0 856.4,206.7 856.9,202.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="858.6,201.6 859.1,205.4 859.6,200.4 860.2,197.9 860.7,195.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="862.3,201.6 862.9,200.4 863.4,205.4 863.9,207.9 864.5,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="866.1,197.9 866.6,202.9 867.2,204.2 867.7,202.9 868.3,214.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="870.4,216.7 871.0,214.2 871.5,221.8 872.0,218.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="873.6,220.5 874.2,223.0 874.7,224.3 875.3,219.2 875.8,218.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="877.4,219.2 878.0,221.8 878.5,210.4 879.0,206.7 879.6,206.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="881.2,204.2 881.7,207.9 882.3,199.1 882.8,206.7 883.3,206.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="885.0" cy="204.2" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="886.0,210.4 886.6,206.7 887.1,202.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="888.7,204.2 889.3,205.4 889.8,204.2 890.3,207.9 890.9,213.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="892.5,215.5 893.0,219.2 893.6,220.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="894.7" cy="218.0" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="896.3,209.2 896.8,209.2 897.4,213.0 897.9,206.7 898.4,202.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="900.0,199.1 900.6,197.9 901.1,204.2 901.7,202.9 902.2,196.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="903.8,197.9 904.4,201.6 904.9,200.4 905.4,205.4 906.0,200.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="907.6,199.1 908.1,197.9 908.7,201.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="909.7" cy="202.9" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="911.4,205.4 911.9,202.9 912.4,197.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="913.5" cy="196.6" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="915.1,199.1 915.7,197.9 916.2,201.6 916.8,196.6 917.3,197.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="918.9,196.6 919.4,197.9 920.0,201.6 920.5,199.1 921.1,190.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="923.2,182.8 923.8,187.8 924.3,187.8 924.8,190.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="926.5,192.8 927.0,190.3 927.5,187.8 928.1,190.3 928.6,187.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="930.2,184.0 930.8,185.3 931.3,184.0 931.8,194.1 932.4,192.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="934.0,192.8 934.5,200.4 935.1,197.9 935.6,209.2 936.1,215.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="938.3,214.2 938.8,209.2 939.4,210.4 939.9,210.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="941.5,216.7 942.1,215.5 942.6,214.2 943.2,218.0 943.7,224.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="945.3,214.2 945.8,213.0 946.4,209.2 946.9,204.2 947.5,201.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="949.1,205.4 949.6,201.6 950.2,194.1 950.7,186.6 951.2,185.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="952.9,191.6 953.4,195.4 953.9,187.8 954.5,189.1 955.0,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="956.6,177.8 957.2,171.5 957.7,179.0 958.2,167.7 958.8,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="960.4,176.5 960.9,182.8 961.5,179.0 962.0,181.5 962.6,176.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="964.2,177.8 964.7,179.0 965.2,184.0 965.8,184.0 966.3,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="967.9,182.8 968.5,187.8 969.0,184.0 969.6,180.3 970.1,187.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="971.7,187.8 972.3,182.8 972.8,182.8 973.3,177.8 973.9,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="975.5,176.5 976.0,175.2 976.6,167.7 977.1,170.2 977.6,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="979.3,163.9 979.8,166.4 980.3,175.2 980.9,169.0 981.4,172.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="983.0,167.7 983.6,162.7 984.1,162.7 984.6,161.4 985.2,146.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="986.8,143.8 987.3,136.3 987.9,148.8 988.4,148.8 989.0,150.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="991.1,157.6 991.7,160.2 992.2,163.9 992.7,163.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="994.3,161.4 994.9,162.7 995.4,158.9 996.0,161.4 996.5,151.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="998.1,150.1 998.7,153.9 999.2,151.4 999.7,163.9 1000.3,160.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1001.9,161.4 1002.4,166.4 1003.0,158.9 1003.5,162.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1005.7,156.4 1006.2,157.6 1006.7,169.0 1007.3,170.2 1007.8,172.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1009.4,172.7 1010.0,165.2 1010.5,160.2 1011.0,158.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1013.2,160.2 1013.7,151.4 1014.3,150.1 1014.8,152.6 1015.4,150.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1017.0,142.6 1017.5,147.6 1018.1,151.4 1018.6,148.8 1019.1,151.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1020.7,145.1 1021.3,141.3 1021.8,136.3 1022.4,131.2 1022.9,133.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1024.5,138.8 1025.1,143.8 1025.6,136.3 1026.1,135.0 1026.7,126.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1028.3,132.5 1028.8,141.3 1029.4,141.3 1029.9,133.8 1030.4,138.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1032.1,130.0 1032.6,132.5 1033.1,135.0 1033.7,141.3 1034.2,135.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1035.8,130.0 1036.4,131.2 1036.9,138.8 1037.5,133.8 1038.0,127.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1039.6,132.5 1040.1,140.0 1040.7,137.5 1041.2,136.3 1041.8,128.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1043.4,126.2 1043.9,121.2 1044.5,121.2 1045.0,123.7 1045.5,122.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1047.7,119.9 1048.2,116.1 1048.8,101.1 1049.3,99.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1050.9,98.5 1051.5,94.8 1052.0,93.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<text x="1058" y="97.5" font-size="11.5" font-weight="700" fill="var(--s-dgs10)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 10년물 국채금리 5.01%</text>
</svg>
</div>

---

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **한 줄로**: 세계 자산 가격의 기준점 역할을 하는 금리다 — 여기가 움직이면 거의 모든 밸류에이션이 따라 움직인다.
- **오르면**: 성장·인플레이션 기대가 커졌거나, 재정적자 우려가 부각됐거나, 긴축 기대가 강해졌다는 신호로 흔히 해석한다. 할인율이 함께 올라 밸류에이션에는 하방 압력이다.
- **내리면**: 성장·물가 기대가 둔화됐거나, 안전자산 수요가 늘었거나, 완화 기대가 커졌다는 신호로 흔히 해석한다.
- **왜 이 만기가 기준이 됐나**: 10년물은 발행량·거래량이 가장 많아 사고팔기 쉽고, 주택담보대출 같은 실물경제 금리의 기준으로도 널리 쓰인다. 재정 우려가 반영되는 경로도 직접적이다 — 국채를 더 많이 찍을 것이라는 기대는 만기가 긴 채권일수록(그만큼 오래 그 부담을 떠안으므로) 가격에 크게 반영된다(기간 프리미엄).
- **원인을 가르려면 2년물과 함께 본다**: 두 만기가 같이 움직였으면 정책 기대가, 10년물만 움직였으면 성장·물가·기간 프리미엄이 주도한 것으로 읽는다([2년물](./treasury_2y.md)·[3종 비교](./comparison.md)).
- **상수만기(constant maturity)라는 표기**: 실제로 만기가 정확히 그 기간인 채권 하나의 값이 아니라, 거래되는 여러 국채의 수익률곡선에서 그 만기 지점을 읽어 낸 값이다. 시간이 지나도 만기가 줄지 않는 일정한 잣대를 유지하기 위한 방식이다.
- **차트의 회색 음영**: NBER이 사후에 판정한 미국의 침체 국면이다. 실시간 신호가 아니라 나중에 붙는 라벨이다.

---

*작성일: 2026-09-18*
