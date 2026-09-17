# 미국 10년물 국채금리

::: info
만기 10년 미 국채의 상수만기(constant maturity) 수익률이다(FRED `DGS10`). DCF 밸류에이션에서 "위험이 거의 없는 이자율(무위험이자율)"의 대표 기준으로 쓰이며, 금리 국면에 따라 성장주의 밸류에이션 배수가 크게 달라진다.

:::
---

## 1. 차트 — 최근 5년 일간

<div class="fred-dgs10">
<style>
.fred-dgs10 {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-dgs10:#eb6834;
}
@media (prefers-color-scheme: dark) {
  .dark .fred-dgs10 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs10:#d95926; }
}
.dark .fred-dgs10 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs10:#d95926; }
.fred-dgs10 svg { width:100%; height:auto; display:block; }
.fred-dgs10 text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-dgs10 .title { fill: var(--ink); font-weight:600; }
.fred-dgs10 .grid { stroke: var(--grid); stroke-width:1; }
.fred-dgs10 .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미국 10년물 국채금리, 최근 5년 일간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 10년물 국채금리 (상수만기) (최근 5년 일간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-15 · 단위: % · 출처: FRED DGS10</text>
<line x1="60" y1="597.8" x2="1052" y2="597.8" class="grid"/>
<text x="52" y="601.8" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="471.7" x2="1052" y2="471.7" class="grid"/>
<text x="52" y="475.7" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="345.6" x2="1052" y2="345.6" class="grid"/>
<text x="52" y="349.6" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="219.6" x2="1052" y2="219.6" class="grid"/>
<text x="52" y="223.6" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="93.5" x2="1052" y2="93.5" class="grid"/>
<text x="52" y="97.5" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="125.8" y1="56" x2="125.8" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="125.8" y1="600" x2="125.8" y2="605" class="axis"/>
<text x="125.8" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.6" y1="56" x2="322.6" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.6" y1="600" x2="322.6" y2="605" class="axis"/>
<text x="322.6" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="519.3" y1="56" x2="519.3" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="519.3" y1="600" x2="519.3" y2="605" class="axis"/>
<text x="519.3" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.7" y1="56" x2="716.7" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.7" y1="600" x2="716.7" y2="605" class="axis"/>
<text x="716.7" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.4" y1="56" x2="913.4" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.4" y1="600" x2="913.4" y2="605" class="axis"/>
<text x="913.4" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<polyline points="60.0,558.7 60.5,561.2 61.1,556.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="63.2,549.9 63.8,553.7 64.3,560.0 64.9,553.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="66.5,556.2 67.0,562.5 67.5,558.7 68.1,554.9 68.6,551.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="70.2,558.7 70.8,556.2 71.3,557.4 71.9,546.1 72.4,538.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="74.0,537.3 74.6,529.7 75.1,528.4 75.6,532.2 76.2,537.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="77.8,536.0 78.3,529.7 78.9,531.0 79.4,524.7 79.9,520.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="82.1,523.4 82.6,527.2 83.2,532.2 83.7,523.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="85.3,523.4 85.9,515.8 86.4,515.8 87.0,512.1 87.5,514.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="89.1,517.1 89.7,518.4 90.2,529.7 90.7,525.9 91.3,528.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="92.9,524.7 93.4,527.2 94.0,522.1 94.5,531.0 95.0,541.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="96.7,533.5 97.2,539.8 97.7,527.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="98.8" cy="524.7" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="100.4,518.4 101.0,518.4 101.5,522.1 102.1,523.4 102.6,529.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="104.2,518.4 104.7,513.3 105.3,517.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="106.4" cy="537.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="108.0,532.2 108.5,543.6 109.1,543.6 109.6,542.3 110.1,553.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="111.8,543.6 112.3,537.3 112.8,532.2 113.4,536.0 113.9,537.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="115.5,544.8 116.1,542.3 116.6,538.5 117.1,542.3 117.7,546.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="119.3,543.6 119.8,537.3 120.4,539.8 120.9,534.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="123.1,537.3 123.6,536.0 124.2,528.4 124.7,532.2 125.2,532.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="126.9,518.4 127.4,514.6 127.9,508.3 128.5,505.8 129.0,502.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="130.6,499.4 131.2,503.2 131.7,504.5 132.2,509.5 132.8,499.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="134.9,488.1 135.5,493.1 136.0,493.1 136.6,503.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="138.2,503.2 138.7,499.4 139.3,490.6 139.8,495.7 140.3,499.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="141.9,498.2 142.5,495.7 143.0,499.4 143.6,494.4 144.1,480.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="145.7,481.8 146.3,476.8 146.8,479.3 147.3,467.9 147.9,481.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="149.5,474.2 150.0,465.4 150.6,467.9 151.1,475.5 151.7,481.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="153.8,479.3 154.3,473.0 154.9,476.8 155.4,475.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="157.0,493.1 157.6,507.0 158.1,489.4 158.7,489.4 159.2,504.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="160.8,499.4 161.4,489.4 161.9,479.3 162.4,474.2 163.0,471.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="164.6,454.1 165.1,452.8 165.7,447.8 166.2,446.5 166.7,454.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="168.4,431.4 168.9,423.8 169.4,431.4 170.0,428.9 170.5,411.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="172.1,413.7 172.7,420.0 173.2,427.6 173.8,431.4 174.3,422.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="175.9,418.8 176.5,403.6 177.0,394.8 177.5,388.5 178.1,380.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="179.7,372.1 180.2,380.9 180.8,383.5 181.3,367.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="183.5,364.6 184.0,354.5 184.5,364.6 185.1,358.3 185.6,358.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="187.2,369.6 187.8,374.6 188.3,368.3 188.9,364.6 189.4,359.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="191.0,346.9 191.5,349.4 192.1,354.5 192.6,339.3 193.2,330.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="194.8,339.3 195.3,346.9 195.9,357.0 196.4,365.8 196.9,354.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="198.6,360.8 199.1,348.2 199.6,359.5 200.2,365.8 200.7,373.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="202.3,363.3 202.9,375.9 203.4,377.2 203.9,377.2 204.5,378.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="206.6,364.6 207.2,353.2 207.7,355.7 208.3,350.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="209.9,340.6 210.4,348.2 211.0,341.9 211.5,340.6 212.0,326.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="213.7,291.4 214.2,283.9 214.7,304.0 215.3,310.4 215.8,314.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="218.0,306.6 218.5,325.5 219.0,334.3 219.6,329.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="221.2,320.4 221.7,320.4 222.3,333.0 222.8,348.2 223.4,360.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="225.5,368.3 226.1,354.5 226.6,344.4 227.1,334.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="228.7,346.9 229.3,350.7 229.8,357.0 230.4,350.7 230.9,354.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="232.5,350.7 233.1,344.4 233.6,340.6 234.1,357.0 234.7,374.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="236.3,369.6 236.8,369.6 237.4,373.4 237.9,386.0 238.5,387.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="240.1,396.1 240.6,377.2 241.1,379.7 241.7,386.0 242.2,367.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="243.8,374.6 244.4,370.9 244.9,373.4 245.5,362.0 246.0,365.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="247.6,372.1 248.2,368.3 248.7,359.5 249.2,360.8 249.8,348.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="251.4,341.9 251.9,339.3 252.5,331.8 253.0,341.9 253.5,340.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="255.2,330.5 255.7,331.8 256.2,326.7 256.8,312.9 257.3,320.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="259.5,304.0 260.0,311.6 260.6,309.1 261.1,304.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="262.7,299.0 263.3,292.7 263.8,294.0 264.3,288.9 264.9,288.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="266.5,283.9 267.0,273.8 267.6,281.4 268.1,257.4 268.6,258.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="270.3,234.7 270.8,223.4 271.3,254.9 271.9,249.8 272.4,241.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="274.0,261.2 274.6,267.5 275.1,249.8 275.7,241.0 276.2,233.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="278.3,228.4 278.9,230.9 279.4,223.4 280.0,219.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="281.6,217.1 282.1,218.3 282.7,201.9 283.2,189.3 283.7,193.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="285.4,188.1 285.9,207.0 286.4,214.5 287.0,224.6 287.5,217.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="289.1,207.0 289.7,210.8 290.2,207.0 290.7,201.9 291.3,198.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="292.9,191.8 293.4,201.9 294.0,204.5 294.5,242.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="296.7,234.7 297.2,244.8 297.8,261.2 298.3,248.6 298.8,242.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="300.5,241.0 301.0,249.8 301.5,256.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="302.6" cy="259.9" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="304.2,258.7 304.8,251.1 305.3,259.9 305.8,278.8 306.4,281.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="308.0,270.0 308.5,281.4 309.1,292.7 309.6,285.1 310.2,273.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="311.8,268.7 312.3,281.4 312.9,283.9 313.4,290.2 313.9,285.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="315.5,273.8 316.1,258.7 316.6,259.9 317.2,261.2 317.7,251.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="319.9,239.8 320.4,234.7 320.9,241.0 321.5,234.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="323.6,246.1 324.2,258.7 324.7,256.1 325.3,276.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="326.9,278.8 327.4,268.7 327.9,277.6 328.5,291.4 329.0,283.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="331.2,278.8 331.7,299.0 332.3,296.5 332.8,285.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="334.4,280.1 335.0,287.7 335.5,287.7 336.0,283.9 336.6,280.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="338.2,276.3 338.7,280.1 339.3,296.5 339.8,295.2 340.3,278.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="342.0,266.2 342.5,261.2 343.0,266.2 343.6,261.2 344.1,252.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="345.7,254.9 346.3,248.6 346.8,243.5 347.4,237.2 347.9,242.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="350.1,225.9 350.6,228.4 351.1,234.7 351.7,225.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="353.3,229.7 353.8,229.7 354.4,218.3 354.9,209.5 355.4,223.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="357.1,222.1 357.6,223.4 358.1,222.1 358.7,228.4 359.2,257.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="360.8,276.3 361.4,265.0 361.9,281.4 362.5,275.1 363.0,296.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="364.6,286.4 365.1,271.3 365.7,285.1 366.2,297.7 366.8,297.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="368.4,278.8 368.9,276.3 369.5,273.8 370.0,276.3 370.5,285.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="372.2,291.4 372.7,301.5 373.2,307.8 373.8,307.8 374.3,296.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="375.9,294.0 376.5,291.4 377.0,294.0 377.5,288.9 378.1,280.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="379.7,270.0 380.2,272.5 380.8,270.0 381.3,277.6 381.9,273.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="383.5,280.1 384.0,295.2 384.6,291.4 385.1,278.8 385.6,290.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="387.3,271.3 387.8,290.2 388.3,297.7 388.9,299.0 389.4,290.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="391.0,280.1 391.6,278.8 392.1,291.4 392.6,296.5 393.2,287.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="394.8,282.6 395.3,277.6 395.9,273.8 396.4,263.7 397.0,257.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="398.6,254.9 399.1,257.4 399.7,253.6 400.2,241.0 400.7,244.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="402.9,258.7 403.4,265.0 404.0,268.7 404.5,258.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="406.1,258.7 406.7,257.4 407.2,246.1 407.7,253.6 408.3,251.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="409.9,253.6 410.4,239.8 411.0,241.0 411.5,254.9 412.1,248.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="414.2,252.4 414.7,254.9 415.3,244.8 415.8,252.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="417.4,254.9 418.0,248.6 418.5,256.1 419.1,238.5 419.6,243.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="421.2" cy="237.2" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="422.3,225.9 422.8,213.3 423.4,212.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="425.0,218.3 425.5,220.8 426.1,237.2 426.6,249.8 427.1,241.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="428.8,243.5 429.3,244.8 429.8,251.1 430.4,238.5 430.9,239.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="432.5,237.2 433.1,230.9 433.6,237.2 434.2,218.3 434.7,224.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="436.3,223.4 436.9,213.3 437.4,209.5 437.9,194.4 438.5,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="440.1,208.2 440.6,217.1 441.2,219.6 441.7,208.2 442.2,199.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="443.9,195.6 444.4,193.1 444.9,184.3 445.5,181.8 446.0,186.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="447.6,176.7 448.2,176.7 448.7,195.6 449.3,190.6 449.8,188.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="451.4,194.4 451.9,204.5 452.5,204.5 453.0,208.2 453.6,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="455.7,185.5 456.3,181.8 456.8,185.5 457.3,186.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="459.0,183.0 459.5,185.5 460.0,188.1 460.6,183.0 461.1,178.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="462.7,179.2 463.3,172.9 463.8,175.5 464.3,157.8 464.9,164.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="466.5,150.2 467.0,149.0 467.6,142.7 468.1,145.2 468.7,145.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="470.3,132.6 470.8,117.5 471.4,127.6 471.9,128.8 472.4,121.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="474.6,136.4 475.1,146.5 475.7,131.3 476.2,140.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="477.8,130.1 478.4,114.9 478.9,104.9 479.4,96.0 480.0,102.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="481.6,111.2 482.1,114.9 482.7,99.8 483.2,111.2 483.8,113.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="485.4,108.6 485.9,108.6 486.5,122.5 487.0,135.1 487.5,147.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="489.1,135.1 489.7,146.5 490.2,157.8 490.8,141.4 491.3,142.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="492.9,140.2 493.5,164.1 494.0,152.8 494.5,162.9 495.1,164.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="496.7,166.6 497.2,167.9 497.8,166.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="498.9" cy="160.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="500.5,170.4 501.0,176.7 501.5,185.5 502.1,172.9 502.6,191.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="504.2,184.3 504.8,196.9 505.3,204.5 505.9,201.9 506.4,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="508.0,190.6 508.6,194.4 509.1,214.5 509.6,229.7 510.2,230.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="511.8,225.9 512.3,228.4 512.9,237.2 513.4,233.5 513.9,232.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="516.1,233.5 516.6,246.1 517.2,239.8 517.7,234.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="519.9,225.9 520.4,230.9 521.0,220.8 521.5,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="523.1,218.3 523.7,217.1 524.2,214.5 524.7,222.1 525.3,224.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="527.4,210.8 528.0,207.0 528.5,201.9 529.0,200.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="530.7,205.7 531.2,201.9 531.7,196.9 532.3,201.9 532.8,200.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="534.4,209.5 535.0,212.0 535.5,220.8 536.1,236.0 536.6,215.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="538.2,198.2 538.7,208.2 539.3,208.2 539.8,200.7 540.4,198.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="542.0,198.2 542.5,180.5 543.1,185.5 543.6,189.3 544.1,181.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="546.3,185.5 546.8,179.2 547.4,178.0 547.9,186.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="549.5,184.3 550.1,180.5 550.6,185.5 551.1,188.1 551.7,195.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="553.3,191.8 553.8,203.2 554.4,205.7 554.9,208.2 555.5,208.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="557.1,207.0 557.6,199.4 558.2,195.6 558.7,183.0 559.2,180.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="560.9,176.7 561.4,181.8 561.9,185.5 562.5,185.5 563.0,191.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="564.6,188.1 565.2,189.3 565.7,194.4 566.2,194.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="568.4,178.0 568.9,174.2 569.5,174.2 570.0,180.5 570.6,170.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="572.2,166.6 572.7,174.2 573.3,150.2 573.8,149.0 574.3,156.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="575.9,140.2 576.5,135.1 577.0,145.2 577.6,138.9 578.1,141.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="579.7,141.4 580.3,142.7 580.8,137.6 581.3,131.3 581.9,135.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="583.5,140.2 584.0,132.6 584.6,140.2 585.1,146.5 585.7,156.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="587.3,157.8 587.8,160.3 588.3,159.1 588.9,162.9 589.4,156.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="591.0,159.1 591.6,162.9 592.1,174.2 592.7,171.7 593.2,166.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="594.8,164.1 595.4,167.9 595.9,165.4 596.4,160.3 597.0,161.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="599.1,151.5 599.7,142.7 600.2,150.2 600.7,155.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="602.4,167.9 602.9,178.0 603.4,183.0 604.0,184.3 604.5,165.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="606.1,160.3 606.7,170.4 607.2,180.5 607.8,189.3 608.3,194.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="609.9,184.3 610.5,191.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="611.5,188.1 612.1,188.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="613.7,188.1 614.2,190.6 614.8,179.2 615.3,183.0 615.8,174.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="617.5,159.1 618.0,165.4 618.5,174.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="619.6" cy="184.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="621.2,184.3 621.8,181.8 622.3,184.3 622.9,194.4 623.4,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="625.0,190.6 625.5,198.2 626.1,199.4 626.6,194.4 627.2,188.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="628.8,186.8 629.3,188.1 629.9,184.3 630.4,185.5 630.9,194.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="632.6,198.2 633.1,200.7 633.6,208.2 634.2,220.8 634.7,244.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="636.3,247.3 636.9,232.2 637.4,224.6 637.9,220.8 638.5,227.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="640.1,232.2 640.6,238.5 641.2,241.0 641.7,229.7 642.3,233.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="643.9,237.2 644.4,242.3 645.0,246.1 645.5,237.2 646.0,243.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="647.7,242.3 648.2,241.0 648.7,239.8 649.3,236.0 649.8,230.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="652.0,239.8 652.5,248.6 653.0,253.6 653.6,254.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="655.2,257.4 655.7,263.7 656.3,263.7 656.8,259.9 657.4,262.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="659.0,266.2 659.5,263.7 660.1,257.4 660.6,253.6 661.1,253.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="662.7,251.1 663.3,252.4 663.8,246.1 664.4,246.1 664.9,251.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="666.5,243.5 667.1,252.4 667.6,246.1 668.1,238.5 668.7,222.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="670.3,215.8 670.8,214.5 671.4,212.0 671.9,208.2 672.5,209.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="674.6,215.8 675.1,217.1 675.7,208.2 676.2,209.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="677.8,195.6 678.4,194.4 678.9,189.3 679.5,193.1 680.0,188.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="681.6,184.3 682.2,184.3 682.7,183.0 683.2,184.3 683.8,172.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="685.4,180.5 685.9,186.8 686.5,166.6 687.0,180.5 687.5,181.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="689.7,165.4 690.2,164.1 690.8,165.4 691.3,165.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="692.9,166.6 693.5,170.4 694.0,167.9 694.6,165.4 695.1,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="696.7,185.5 697.3,181.8 697.8,188.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="698.9" cy="196.9" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="700.5,195.6 701.0,190.6 701.6,195.6 702.1,198.2 702.6,200.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="704.3,194.4 704.8,191.8 705.3,186.8 705.9,179.2 706.4,169.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="708.0,170.4 708.6,169.2 709.1,156.6 709.7,147.7 710.2,154.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="711.8,145.2 712.3,145.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="713.4,146.5 714.0,141.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="715.6,150.2 716.1,146.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="717.2,147.7 717.7,143.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="719.4,141.4 719.9,135.1 720.4,135.1 721.0,133.9 721.5,122.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="723.1,120.0 723.7,121.3 724.2,136.4 724.7,142.7 725.3,142.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="727.4,147.7 728.0,143.9 728.5,137.6 729.1,140.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="730.7,152.8 731.2,150.2 731.8,150.2 732.3,154.0 732.8,146.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="734.5,151.5 735.0,154.0 735.5,165.4 736.1,162.9 736.6,157.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="738.2,155.3 738.8,151.5 739.3,141.4 739.8,154.0 740.4,160.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="742.5,150.2 743.1,152.8 743.6,156.6 744.2,166.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="745.8,169.2 746.3,181.8 746.9,188.1 747.4,183.0 747.9,189.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="749.5,199.4 750.1,191.8 750.6,184.3 751.2,183.0 751.7,179.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="753.3,191.8 753.9,184.3 754.4,179.2 754.9,185.5 755.5,180.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="757.1,180.5 757.6,183.0 758.2,188.1 758.7,189.3 759.3,188.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="760.9,176.7 761.4,180.5 761.9,175.5 762.5,171.7 763.0,185.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="764.6,190.6 765.2,198.2 765.7,194.4 766.3,212.0 766.8,218.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="768.4,200.7 769.0,186.8 769.5,176.7 770.0,169.2 770.6,159.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="772.2,171.7 772.7,175.5 773.3,183.0 773.8,176.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="776.0,166.6 776.5,167.9 777.0,169.2 777.6,179.2 778.1,183.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="779.7,190.6 780.3,195.6 780.8,198.2 781.4,188.1 781.9,178.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="783.5,174.2 784.1,181.8 784.6,186.8 785.1,172.9 785.7,172.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="787.3,162.9 787.8,157.8 788.4,152.8 788.9,162.9 789.4,165.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="791.1,161.6 791.6,159.1 792.1,146.5 792.7,151.5 793.2,155.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="795.4,165.4 795.9,160.3 796.5,165.4 797.0,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="798.6,161.6 799.1,161.6 799.7,172.9 800.2,169.2 800.8,155.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="802.4,157.8 802.9,160.3 803.5,167.9 804.0,174.2 804.5,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="806.2,161.6 806.7,170.4 807.2,171.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="808.3" cy="171.7" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="809.9,176.7 810.5,181.8 811.0,183.0 811.5,186.8 812.1,183.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="813.7,189.3 814.2,186.8 814.8,181.8 815.3,175.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="817.5,169.2 818.0,166.6 818.6,176.7 819.1,175.5 819.6,165.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="821.3,165.4 821.8,156.6 822.3,161.6 822.9,160.3 823.4,164.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="825.0,171.7 825.6,175.5 826.1,169.2 826.6,165.4 827.2,169.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="828.8,166.6 829.3,176.7 829.9,171.7 830.4,172.9 831.0,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="832.6,191.8 833.1,191.8 833.7,191.8 834.2,190.6 834.7,185.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="836.3,185.5 836.9,183.0 837.4,189.3 838.0,183.0 838.5,178.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="840.1,176.7 840.7,181.8 841.2,183.0 841.7,178.0 842.3,186.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="843.9,184.3 844.4,186.8 845.0,189.3 845.5,191.8 846.1,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="848.2,184.3 848.7,191.8 849.3,198.2 849.8,207.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="851.4,213.3 852.0,209.5 852.5,214.5 853.1,218.3 853.6,212.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="855.2,213.3 855.8,214.5 856.3,212.0 856.8,205.7 857.4,201.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="859.0,200.7 859.5,204.5 860.1,199.4 860.6,196.9 861.1,194.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="862.8,200.7 863.3,199.4 863.8,204.5 864.4,207.0 864.9,203.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="866.5,196.9 867.1,201.9 867.6,203.2 868.2,201.9 868.7,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="870.9,215.8 871.4,213.3 871.9,220.8 872.5,217.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="874.1,219.6 874.6,222.1 875.2,223.4 875.7,218.3 876.2,217.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="877.9,218.3 878.4,220.8 878.9,209.5 879.5,205.7 880.0,205.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="881.6,203.2 882.2,207.0 882.7,198.2 883.3,205.7 883.8,205.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="885.4" cy="203.2" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="886.5,209.5 887.0,205.7 887.6,201.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="889.2,203.2 889.7,204.5 890.3,203.2 890.8,207.0 891.3,212.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="893.0,214.5 893.5,218.3 894.0,219.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="895.1" cy="217.1" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="896.7,208.2 897.3,208.2 897.8,212.0 898.3,205.7 898.9,201.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="900.5,198.2 901.0,196.9 901.6,203.2 902.1,201.9 902.7,195.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="904.3,196.9 904.8,200.7 905.4,199.4 905.9,204.5 906.4,199.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="908.1,198.2 908.6,196.9 909.1,200.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="910.2" cy="201.9" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="911.8,204.5 912.4,201.9 912.9,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="914.0" cy="195.6" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="915.6,198.2 916.1,196.9 916.7,200.7 917.2,195.6 917.8,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="919.4,195.6 919.9,196.9 920.5,200.7 921.0,198.2 921.5,189.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="923.7,181.8 924.2,186.8 924.8,186.8 925.3,189.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="926.9,191.8 927.5,189.3 928.0,186.8 928.5,189.3 929.1,186.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="930.7,183.0 931.2,184.3 931.8,183.0 932.3,193.1 932.9,191.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="934.5,191.8 935.0,199.4 935.5,196.9 936.1,208.2 936.6,214.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="938.8,213.3 939.3,208.2 939.9,209.5 940.4,209.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="942.0,215.8 942.6,214.5 943.1,213.3 943.6,217.1 944.2,223.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="945.8,213.3 946.3,212.0 946.9,208.2 947.4,203.2 947.9,200.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="949.6,204.5 950.1,200.7 950.6,193.1 951.2,185.5 951.7,184.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="953.3,190.6 953.9,194.4 954.4,186.8 955.0,188.1 955.5,170.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="957.1,176.7 957.7,170.4 958.2,178.0 958.7,166.6 959.3,164.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="960.9,175.5 961.4,181.8 962.0,178.0 962.5,180.5 963.0,175.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="964.7,176.7 965.2,178.0 965.7,183.0 966.3,183.0 966.8,180.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="968.4,181.8 969.0,186.8 969.5,183.0 970.1,179.2 970.6,186.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="972.2,186.8 972.7,181.8 973.3,181.8 973.8,176.7 974.4,180.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="976.0,175.5 976.5,174.2 977.1,166.6 977.6,169.2 978.1,170.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="979.8,162.9 980.3,165.4 980.8,174.2 981.4,167.9 981.9,171.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="983.5,166.6 984.1,161.6 984.6,161.6 985.1,160.3 985.7,145.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="987.3,142.7 987.8,135.1 988.4,147.7 988.9,147.7 989.5,149.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="991.6,156.6 992.2,159.1 992.7,162.9 993.2,162.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="994.9,160.3 995.4,161.6 995.9,157.8 996.5,160.3 997.0,150.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="998.6,149.0 999.2,152.8 999.7,150.2 1000.2,162.9 1000.8,159.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1002.4,160.3 1002.9,165.4 1003.5,157.8 1004.0,161.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1006.2,155.3 1006.7,156.6 1007.3,167.9 1007.8,169.2 1008.3,171.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1009.9,171.7 1010.5,164.1 1011.0,159.1 1011.6,157.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1013.7,159.1 1014.3,150.2 1014.8,149.0 1015.3,151.5 1015.9,149.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1017.5,141.4 1018.0,146.5 1018.6,150.2 1019.1,147.7 1019.7,150.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1021.3,143.9 1021.8,140.2 1022.3,135.1 1022.9,130.1 1023.4,132.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1025.0,137.6 1025.6,142.7 1026.1,135.1 1026.7,133.9 1027.2,125.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1028.8,131.3 1029.4,140.2 1029.9,140.2 1030.4,132.6 1031.0,137.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1032.6,128.8 1033.1,131.3 1033.7,133.9 1034.2,140.2 1034.7,133.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1036.4,128.8 1036.9,130.1 1037.4,137.6 1038.0,132.6 1038.5,126.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1040.1,131.3 1040.7,138.9 1041.2,136.4 1041.8,135.1 1042.3,127.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1043.9,125.0 1044.5,120.0 1045.0,120.0 1045.5,122.5 1046.1,121.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1048.2,118.7 1048.8,114.9 1049.3,99.8 1049.8,98.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1051.5,97.3 1052.0,93.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<text x="1058" y="97.5" font-size="11.5" font-weight="700" fill="var(--s-dgs10)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 10년물 국채금리 5.00%</text>
</svg>
</div>

---

## 2. 해석

- **상승**: 성장·인플레이션 기대가 커지거나, 재정적자 우려가 부각되거나, 연준의 긴축 기대가 강해졌다는 신호로 흔히 해석한다 — DCF에서 쓰는 무위험이자율이 오르면 할인율도 함께 올라가 밸류에이션에는 하방 압력으로 작용한다.
- **하락**: 성장·인플레이션 기대가 둔화되거나, 안전자산 수요가 늘거나, 연준의 완화 기대가 커졌다는 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 10년물 국채는 발행량·거래량이 가장 많아 사고팔기 쉽고(유동성이 좋고), 주택담보대출 같은 실물경제 금리를 정할 때도 기준으로 널리 쓰여서 DCF 무위험이자율의 표준으로 자리 잡았다. 재정적자 우려가 반영되는 경로도 직접적이다 — 국채를 더 많이 찍어낼 것이라는 기대는, 만기가 긴 채권일수록(그만큼 더 오래 그 부담을 떠안아야 하므로) 가격에 더 크게 반영된다(기간 프리미엄).
- **여러 요인이 겹쳐 움직인다**: 연준의 정책, 인플레이션 기대, 재정정책이 한꺼번에 반영되므로 이 차트 하나만 보고 방향을 미리 단정하지 않는다. 움직임의 성격을 가르려면 [2년물](./treasury_2y.md)과 함께 봐야 한다 — 두 만기가 같이 움직였으면 정책 기대가, 10년물만 움직였으면 성장·물가·기간 프리미엄이 주도한 것으로 읽는다.

---

*작성일: 2026-09-18*
