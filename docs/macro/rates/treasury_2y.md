# 미국 2년물 국채금리

::: info
만기 2년 미 국채의 상수만기(constant maturity) 수익률이다(FRED `DGS2`). 만기가 짧아 기간 프리미엄이 얇게 섞이는 대신 앞으로 몇 차례의 FOMC 결정 경로가 압축돼 담기는 구간이라, 연준 정책금리 기대의 대표 프록시로 인용되며 [10년물](./treasury_10y.md)과의 차이는 수익률곡선 기울기의 표준 척도로 쓰인다.

:::
---

## 1. 차트 — 최근 5년 일간

<style>
.fred-dgs2 {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-dgs2:#2a78d6;
}
.dark .fred-dgs2 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs2:#3987e5; }
.fred-dgs2 svg { width:100%; height:auto; display:block; }
.fred-dgs2 text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-dgs2 .title { fill: var(--ink); font-weight:600; }
.fred-dgs2 .grid { stroke: var(--grid); stroke-width:1; }
.fred-dgs2 .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-dgs2">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미국 2년물 국채금리, 최근 5년 일간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 2년물 국채금리 (상수만기) (최근 5년 일간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-15 · 단위: % · 출처: FRED DGS2</text>
<line x1="60" y1="581.3" x2="1052" y2="581.3" class="grid"/>
<text x="52" y="585.3" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="487.3" x2="1052" y2="487.3" class="grid"/>
<text x="52" y="491.3" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="393.3" x2="1052" y2="393.3" class="grid"/>
<text x="52" y="397.3" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="299.3" x2="1052" y2="299.3" class="grid"/>
<text x="52" y="303.3" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="205.4" x2="1052" y2="205.4" class="grid"/>
<text x="52" y="209.4" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="111.4" x2="1052" y2="111.4" class="grid"/>
<text x="52" y="115.4" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
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
<polyline points="60.0,562.5 60.5,562.5 61.1,561.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="63.2,560.6 63.8,560.6 64.3,559.7 64.9,559.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="66.5,561.5 67.0,561.5 67.5,561.5 68.1,559.7 68.6,559.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="70.2,559.7 70.8,560.6 71.3,557.8 71.9,555.9 72.4,554.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="74.0,552.1 74.6,552.1 75.1,553.1 75.6,555.0 76.2,555.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="77.8,555.9 78.3,555.0 78.9,553.1 79.4,551.2 79.9,551.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="82.1,548.4 82.6,546.5 83.2,547.4 83.7,542.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="85.3,539.9 85.9,542.7 86.4,543.7 87.0,539.0 87.5,536.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="89.1,537.1 89.7,537.1 90.2,534.3 90.7,534.3 91.3,536.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="92.9,534.3 93.4,538.0 94.0,537.1 94.5,542.7 95.0,544.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="96.7,539.0 97.2,542.7 97.7,533.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="98.8" cy="531.5" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="100.4,531.5 101.0,530.5 101.5,532.4 102.1,532.4 102.6,532.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="104.2,522.1 104.7,524.9 105.3,521.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="106.4" cy="534.3" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="108.0,533.3 108.5,532.4 109.1,528.6 109.6,522.1 110.1,524.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="111.8,520.2 112.3,515.5 112.8,517.4 113.4,515.5 113.9,518.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="115.5,519.3 116.1,518.3 116.6,516.4 117.1,521.1 117.7,519.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="119.3,520.2 119.8,515.5 120.4,517.4 120.9,514.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="123.1,509.9 123.6,511.7 124.2,510.8 124.7,512.7 125.2,512.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="126.9,508.0 127.4,508.9 127.9,503.3 128.5,498.6 129.0,499.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="130.6,494.8 131.2,496.7 131.7,494.8 132.2,495.8 132.8,488.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="134.9,481.7 135.5,483.5 136.0,479.8 136.6,486.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="138.2,488.2 138.7,485.4 139.3,475.1 139.8,470.4 140.3,473.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="141.9,470.4 142.5,470.4 143.0,472.3 143.6,469.4 144.1,458.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="145.7,459.1 146.3,454.4 146.8,453.5 147.3,430.0 147.9,440.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="149.5,432.8 150.0,432.8 150.6,438.4 151.1,441.2 151.7,443.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="153.8,434.7 154.3,432.8 154.9,436.5 155.4,435.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="157.0,445.9 157.6,458.2 158.1,440.3 158.7,437.5 159.2,440.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="160.8,435.6 161.4,428.1 161.9,423.4 162.4,419.6 163.0,416.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="164.6,405.5 165.1,407.4 165.7,398.0 166.2,399.0 166.7,396.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="168.4,380.2 168.9,376.4 169.4,381.1 170.0,381.1 170.5,365.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="172.1,360.4 172.7,360.4 173.2,364.2 173.8,367.0 174.3,352.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="175.9,352.9 176.5,345.4 177.0,346.3 177.5,349.1 178.1,343.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="179.7,346.3 180.2,356.7 180.8,358.5 181.3,349.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="183.5,350.1 184.0,336.0 184.5,336.9 185.1,329.4 185.6,325.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="187.2,334.1 187.8,342.6 188.3,338.8 188.9,334.1 189.4,327.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="191.0,324.7 191.5,320.0 192.1,331.3 192.6,326.6 193.2,325.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="194.8,336.0 195.3,335.0 195.9,331.3 196.4,340.7 196.9,336.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="198.6,338.8 199.1,326.6 199.6,329.4 200.2,334.1 200.7,336.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="202.3,332.2 202.9,346.3 203.4,348.2 203.9,350.1 204.5,349.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="206.6,343.5 207.2,331.3 207.7,332.2 208.3,331.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="209.9,324.7 210.4,322.8 211.0,320.0 211.5,315.3 212.0,293.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="213.7,261.7 214.2,257.0 214.7,280.5 215.3,286.2 215.8,283.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="218.0,279.6 218.5,293.7 219.0,298.4 219.6,295.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="221.2,291.8 221.7,289.9 222.3,293.7 222.8,306.9 223.4,314.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="225.5,316.3 226.1,302.2 226.6,296.5 227.1,288.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="228.7,292.8 229.3,296.5 229.8,287.1 230.4,285.2 230.9,287.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="232.5,285.2 233.1,277.7 233.6,275.8 234.1,289.9 234.7,301.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="236.3,299.3 236.8,297.5 237.4,303.1 237.9,313.4 238.5,309.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="240.1,308.7 240.6,293.7 241.1,289.9 241.7,296.5 242.2,276.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="243.8,279.6 244.4,273.0 244.9,277.7 245.5,277.7 246.0,275.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="247.6,280.5 248.2,275.8 248.7,273.0 249.2,278.7 249.8,275.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="251.4,269.3 251.9,272.1 252.5,265.5 253.0,266.4 253.5,264.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="255.2,259.9 255.7,256.1 256.2,257.0 256.8,251.4 257.3,261.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="259.5,252.3 260.0,257.0 260.6,254.2 261.1,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="262.7,244.8 263.3,228.8 263.8,226.0 264.3,217.6 264.9,219.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="266.5,210.1 267.0,209.1 267.6,203.5 268.1,195.0 268.6,186.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="270.3,180.0 270.8,177.2 271.3,198.8 271.9,190.3 272.4,184.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="274.0,194.1 274.6,196.0 275.1,191.3 275.7,183.7 276.2,177.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="278.3,177.2 278.9,179.0 279.4,161.2 280.0,160.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="281.6,163.1 282.1,164.9 282.7,153.7 283.2,147.1 283.7,159.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="285.4,158.4 285.9,165.9 286.4,168.7 287.0,177.2 287.5,166.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="289.1,157.4 289.7,154.6 290.2,148.0 290.7,138.6 291.3,143.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="292.9,137.7 293.4,142.4 294.0,148.0 294.5,173.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="296.7,167.8 297.2,170.6 297.8,172.5 298.3,164.9 298.8,157.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="300.5,160.2 301.0,161.2 301.5,162.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="302.6" cy="165.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="304.2,162.1 304.8,160.2 305.3,169.6 305.8,181.9 306.4,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="308.0,166.8 308.5,173.4 309.1,180.9 309.6,176.2 310.2,174.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="311.8,168.7 312.3,184.7 312.9,183.7 313.4,183.7 313.9,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="315.5,181.9 316.1,181.9 316.6,185.6 317.2,182.8 317.7,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="319.9,175.3 320.4,176.2 320.9,173.4 321.5,166.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="323.6,167.8 324.2,171.5 324.7,163.1 325.3,182.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="326.9,187.5 327.4,182.8 327.9,186.6 328.5,194.1 329.0,184.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="331.2,188.4 331.7,199.7 332.3,196.9 332.8,192.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="334.4,185.6 335.0,194.1 335.5,195.0 336.0,189.4 336.6,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="338.2,181.9 338.7,185.6 339.3,196.9 339.8,196.9 340.3,177.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="342.0,164.0 342.5,161.2 343.0,163.1 343.6,160.2 344.1,158.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="345.7,156.5 346.3,149.0 346.8,147.1 347.4,147.1 347.9,149.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="350.1,142.4 350.6,143.3 351.1,143.3 351.7,132.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="353.3,132.0 353.8,129.2 354.4,121.7 354.9,121.7 355.4,124.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="357.1,121.7 357.6,111.4 358.1,106.7 358.7,120.8 359.2,149.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="360.8,202.5 361.4,186.6 361.9,211.9 362.5,192.2 363.0,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="364.6,212.9 365.1,189.4 365.7,209.1 366.2,227.9 366.8,227.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="368.4,211.0 368.9,203.5 369.5,197.8 370.0,196.0 370.5,199.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="372.2,208.2 372.7,220.4 373.2,225.1 373.8,222.3 374.3,208.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="375.9,205.4 376.5,202.5 377.0,210.1 377.5,209.1 378.1,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="379.7,188.4 380.2,187.5 380.8,182.8 381.3,192.2 381.9,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="383.5,194.1 384.0,218.5 384.6,214.8 385.1,198.8 385.6,201.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="387.3,192.2 387.8,208.2 388.3,215.7 388.9,228.8 389.4,212.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="391.0,205.4 391.6,204.4 392.1,214.8 392.6,215.7 393.2,207.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="394.8,206.3 395.3,199.7 395.9,194.1 396.4,182.8 397.0,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="398.6,178.1 399.1,180.9 399.7,176.2 400.2,158.4 400.7,154.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="402.9,162.1 403.4,167.8 404.0,174.3 404.5,158.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="406.1,162.1 406.7,157.4 407.2,152.7 407.7,156.5 408.3,149.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="409.9,153.7 410.4,142.4 411.0,135.8 411.5,147.1 412.1,139.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="414.2,141.4 414.7,141.4 415.3,133.0 415.8,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="417.4,144.3 418.0,135.8 418.5,138.6 419.1,123.6 419.6,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="421.2" cy="117.0" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="422.3,117.0 422.8,112.3 423.4,117.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="425.0,125.5 425.5,122.7 426.1,137.7 426.6,149.9 427.1,135.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="428.8,135.8 429.3,135.8 429.8,135.8 430.4,130.2 430.9,128.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="432.5,129.2 433.1,125.5 433.6,128.3 434.2,119.8 434.7,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="436.3,122.7 436.9,118.9 437.4,122.7 437.9,120.8 438.5,132.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="440.1,133.9 440.6,135.8 441.2,131.1 441.7,128.3 442.2,121.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="443.9,115.1 444.4,118.9 444.9,114.2 445.5,117.0 446.0,118.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="447.6,114.2 448.2,109.5 448.7,116.1 449.3,113.3 449.8,108.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="451.4,113.3 451.9,123.6 452.5,120.8 453.0,125.5 453.6,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="455.7,117.0 456.3,110.4 456.8,117.0 457.3,113.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="459.0,114.2 459.5,113.3 460.0,115.1 460.6,111.4 461.1,109.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="462.7,106.7 463.3,103.9 463.8,100.1 464.3,100.1 464.9,102.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="466.5,102.9 467.0,107.6 467.6,102.0 468.1,107.6 468.7,108.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="470.3,100.1 470.8,97.3 471.4,106.7 471.9,108.6 472.4,103.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="474.6,115.1 475.1,112.3 475.7,105.7 476.2,107.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="477.8,102.9 478.4,93.5 478.9,93.5 479.4,98.2 480.0,104.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="481.6,106.7 482.1,109.5 482.7,103.9 483.2,109.5 483.8,112.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="485.4,108.6 485.9,104.8 486.5,116.1 487.0,113.3 487.5,127.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="489.1,118.0 489.7,119.8 490.2,118.0 490.8,108.6 491.3,107.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="492.9,109.5 493.5,130.2 494.0,120.8 494.5,127.4 495.1,122.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="496.7,121.7 497.2,124.5 497.8,121.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="498.9" cy="118.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="500.5,126.4 501.0,136.7 501.5,145.2 502.1,136.7 502.6,152.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="504.2,145.2 504.8,151.8 505.3,149.0 505.9,150.8 506.4,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="508.0,138.6 508.6,136.7 509.1,162.1 509.6,170.6 510.2,164.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="511.8,164.9 512.3,166.8 512.9,173.4 513.4,174.3 513.9,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="516.1,180.9 516.6,186.6 517.2,180.9 517.7,183.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="519.9,174.3 520.4,174.3 521.0,169.6 521.5,167.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="523.1,171.5 523.7,171.5 524.2,170.6 524.7,180.9 525.3,192.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="527.4,184.7 528.0,173.4 528.5,173.4 529.0,168.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="530.7,170.6 531.2,176.2 531.7,173.4 532.3,179.0 532.8,173.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="534.4,178.1 535.0,171.5 535.5,180.0 536.1,186.6 536.6,171.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="538.2,162.1 538.7,168.7 539.3,166.8 539.8,162.1 540.4,160.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="542.0,162.1 542.5,145.2 543.1,152.7 543.6,152.7 544.1,145.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="546.3,149.9 546.8,145.2 547.4,140.5 547.9,142.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="549.5,140.5 550.1,139.6 550.6,145.2 551.1,145.2 551.7,154.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="553.3,148.0 553.8,154.6 554.4,153.7 554.9,158.4 555.5,160.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="557.1,157.4 557.6,150.8 558.2,148.0 558.7,141.4 559.2,137.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="560.9,136.7 561.4,141.4 561.9,149.9 562.5,147.1 563.0,149.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="564.6,154.6 565.2,152.7 565.7,154.6 566.2,149.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="568.4,137.7 568.9,139.6 569.5,141.4 570.0,144.3 570.6,136.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="572.2,132.0 572.7,135.8 573.3,114.2 573.8,118.0 574.3,122.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="575.9,118.0 576.5,114.2 577.0,118.0 577.6,113.3 578.1,114.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="579.7,114.2 580.3,124.5 580.8,121.7 581.3,115.1 581.9,115.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="583.5,114.2 584.0,107.6 584.6,115.1 585.1,123.6 585.7,129.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="587.3,128.3 587.8,128.3 588.3,126.4 588.9,130.2 589.4,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="591.0,125.5 591.6,129.2 592.1,136.7 592.7,132.0 593.2,127.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="594.8,128.3 595.4,128.3 595.9,124.5 596.4,119.8 597.0,118.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="599.1,117.0 599.7,115.1 600.2,118.9 600.7,121.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="602.4,128.3 602.9,133.0 603.4,137.7 604.0,137.7 604.5,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="606.1,123.6 606.7,129.2 607.2,134.9 607.8,141.4 608.3,142.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="609.9,134.9 610.5,140.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="611.5,139.6 612.1,139.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="613.7,138.6 614.2,144.3 614.8,138.6 615.3,139.6 615.8,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="617.5,133.0 618.0,135.8 618.5,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="619.6" cy="149.0" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="621.2,147.1 621.8,147.1 622.3,147.1 622.9,158.4 623.4,163.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="625.0,164.0 625.5,164.9 626.1,165.9 626.6,162.1 627.2,159.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="628.8,158.4 629.3,167.8 629.9,170.6 630.4,166.8 630.9,171.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="632.6,171.5 633.1,172.5 633.6,178.1 634.2,190.3 634.7,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="636.3,215.7 636.9,206.3 637.4,205.4 637.9,201.6 638.5,200.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="640.1,204.4 640.6,211.9 641.2,211.0 641.7,197.8 642.3,199.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="643.9,199.7 644.4,206.3 645.0,212.9 645.5,206.3 646.0,214.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="647.7,213.8 648.2,221.3 648.7,221.3 649.3,217.6 649.8,213.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="652.0,216.6 652.5,227.9 653.0,228.8 653.6,237.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="655.2,235.4 655.7,243.9 656.3,241.1 656.8,239.2 657.4,245.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="659.0,246.7 659.5,243.9 660.1,242.0 660.6,243.9 661.1,247.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="662.7,245.8 663.3,253.3 663.8,249.5 664.4,242.9 664.9,247.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="666.5,237.3 667.1,242.0 667.6,240.1 668.1,233.5 668.7,211.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="670.3,206.3 670.8,207.2 671.4,206.3 671.9,207.2 672.5,210.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="674.6,210.1 675.1,211.9 675.7,209.1 676.2,210.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="677.8,203.5 678.4,202.5 678.9,198.8 679.5,198.8 680.0,195.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="681.6,194.1 682.2,195.0 682.7,191.3 683.2,190.3 683.8,185.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="685.4,189.4 685.9,187.5 686.5,180.0 687.0,185.6 687.5,180.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="689.7,173.4 690.2,180.0 690.8,173.4 691.3,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="692.9,178.1 693.5,180.0 694.0,176.2 694.6,173.4 695.1,170.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="696.7,185.6 697.3,185.6 697.8,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="698.9" cy="193.1" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="700.5,189.4 701.0,189.4 701.6,193.1 702.1,191.3 702.6,196.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="704.3,193.1 704.8,191.3 705.3,191.3 705.9,188.4 706.4,181.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="708.0,181.9 708.6,181.9 709.1,172.5 709.7,175.3 710.2,177.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="711.8,177.2 712.3,178.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="713.4,177.2 714.0,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="715.6,182.8 716.1,181.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="717.2,181.9 717.7,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="719.4,179.0 719.9,177.2 720.4,179.0 721.0,180.0 721.5,167.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="723.1,167.8 723.7,170.6 724.2,180.0 724.7,183.7 725.3,180.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="727.4,178.1 728.0,178.1 728.5,178.1 729.1,180.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="730.7,189.4 731.2,187.5 731.8,185.6 732.3,188.4 732.8,184.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="734.5,180.9 735.0,185.6 735.5,189.4 736.1,185.6 736.6,178.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="738.2,179.0 738.8,178.1 739.3,171.5 739.8,176.2 740.4,180.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="742.5,178.1 743.1,179.0 743.6,179.0 744.2,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="745.8,193.1 746.3,198.8 746.9,200.7 747.4,198.8 747.9,206.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="749.5,209.1 750.1,209.1 750.6,206.3 751.2,209.1 751.7,206.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="753.3,215.7 753.9,211.0 754.4,204.4 754.9,211.0 755.5,203.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="757.1,199.7 757.6,201.6 758.2,206.3 758.7,210.1 759.3,211.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="760.9,201.6 761.4,209.1 761.9,207.2 762.5,208.2 763.0,215.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="764.6,215.7 765.2,217.6 765.7,213.8 766.3,232.6 766.8,235.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="768.4,230.7 769.0,232.6 769.5,213.8 770.0,220.4 770.6,209.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="772.2,220.4 772.7,220.4 773.3,227.0 773.8,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="776.0,228.8 776.5,227.9 777.0,223.2 777.6,227.0 778.1,229.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="779.7,236.4 780.3,238.2 780.8,242.9 781.4,233.5 781.9,221.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="783.5,221.3 784.1,226.0 784.6,226.0 785.1,214.8 785.7,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="787.3,207.2 787.8,203.5 788.4,200.7 788.9,209.1 789.4,207.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="791.1,208.2 791.6,208.2 792.1,205.4 792.7,205.4 793.2,205.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="795.4,212.9 795.9,209.1 796.5,212.9 797.0,215.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="798.6,211.0 799.1,209.1 799.7,217.6 800.2,212.9 800.8,201.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="802.4,204.4 802.9,204.4 803.5,211.0 804.0,214.8 804.5,209.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="806.2,208.2 806.7,211.0 807.2,211.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="808.3" cy="214.8" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="809.9,220.4 810.5,228.8 811.0,229.8 811.5,233.5 812.1,230.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="813.7,231.7 814.2,226.0 814.8,226.0 815.3,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="817.5,214.8 818.0,214.8 818.6,218.5 819.1,218.5 819.6,214.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="821.3,214.8 821.8,210.1 822.3,216.6 822.9,213.8 823.4,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="825.0,219.5 825.6,221.3 826.1,216.6 826.6,213.8 827.2,213.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="828.8,213.8 829.3,218.5 829.9,211.0 830.4,211.0 831.0,234.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="832.6,234.5 833.1,231.7 833.7,234.5 834.2,231.7 834.7,227.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="836.3,227.9 836.9,231.7 837.4,236.4 838.0,229.8 838.5,228.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="840.1,227.0 840.7,228.8 841.2,229.8 841.7,225.1 842.3,235.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="843.9,230.7 844.4,242.0 845.0,243.9 845.5,241.1 846.1,243.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="848.2,237.3 848.7,242.0 849.3,243.9 849.8,251.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="851.4,253.3 852.0,248.6 852.5,248.6 853.1,250.5 853.6,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="855.2,248.6 855.8,251.4 856.3,250.5 856.8,245.8 857.4,245.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="859.0,242.0 859.5,249.5 860.1,245.8 860.6,239.2 861.1,240.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="862.8,240.1 863.3,242.9 863.8,247.6 864.4,247.6 864.9,244.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="866.5,242.9 867.1,245.8 867.6,244.8 868.2,242.9 868.7,250.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="870.9,254.2 871.4,252.3 871.9,260.8 872.5,256.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="874.1,256.1 874.6,257.0 875.2,257.0 875.7,254.2 876.2,254.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="877.9,254.2 878.4,255.2 878.9,243.9 879.5,242.0 880.0,242.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="881.6,242.9 882.2,244.8 882.7,240.1 883.3,245.8 883.8,247.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="885.4" cy="244.8" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="886.5,246.7 887.0,244.8 887.6,241.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="889.2,242.9 889.7,244.8 890.3,244.8 890.8,247.6 891.3,251.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="893.0,256.1 893.5,258.9 894.0,257.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="895.1" cy="255.2" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="896.7,248.6 897.3,251.4 897.8,253.3 898.3,250.5 898.9,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="900.5,245.8 901.0,242.0 901.6,248.6 902.1,250.5 902.7,250.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="904.3,251.4 904.8,254.2 905.4,253.3 905.9,256.1 906.4,254.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="908.1,258.0 908.6,254.2 909.1,255.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="910.2" cy="256.1" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="911.8,257.0 912.4,257.0 912.9,255.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="914.0" cy="255.2" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="915.6,256.1 916.1,255.2 916.7,255.2 917.2,253.3 917.8,248.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="919.4,248.6 919.9,249.5 920.5,251.4 921.0,246.7 921.5,243.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="923.7,242.9 924.2,242.9 924.8,242.0 925.3,242.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="926.9,246.7 927.5,249.5 928.0,246.7 928.5,249.5 929.1,250.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="930.7,245.8 931.2,245.8 931.8,245.8 932.3,255.2 932.9,252.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="934.5,254.2 935.0,257.0 935.5,250.5 936.1,255.2 936.6,261.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="938.8,258.9 939.3,255.2 939.9,255.2 940.4,254.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="942.0,258.9 942.6,258.9 943.1,257.0 943.6,259.9 944.2,263.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="945.8,255.2 946.3,251.4 946.9,248.6 947.4,245.8 947.9,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="949.6,246.7 950.1,245.8 950.6,239.2 951.2,227.9 951.7,230.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="953.3,235.4 953.9,235.4 954.4,227.9 955.0,225.1 955.5,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="957.1,221.3 957.7,214.8 958.2,220.4 958.7,209.1 959.3,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="960.9,222.3 961.4,225.1 962.0,223.2 962.5,225.1 963.0,220.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="964.7,220.4 965.2,223.2 965.7,225.1 966.3,226.0 966.8,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="968.4,226.0 969.0,227.9 969.5,227.9 970.1,226.0 970.6,232.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="972.2,231.7 972.7,226.0 973.3,225.1 973.8,221.3 974.4,226.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="976.0,226.0 976.5,220.4 977.1,212.9 977.6,216.6 978.1,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="979.8,210.1 980.3,211.9 980.8,217.6 981.4,212.9 981.9,214.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="983.5,210.1 984.1,205.4 984.6,207.2 985.1,205.4 985.7,196.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="987.3,198.8 987.8,193.1 988.4,201.6 988.9,197.8 989.5,193.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="991.6,204.4 992.2,205.4 992.7,206.3 993.2,207.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="994.9,200.7 995.4,200.7 995.9,197.8 996.5,200.7 997.0,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="998.6,191.3 999.2,193.1 999.7,193.1 1000.2,200.7 1000.8,196.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1002.4,198.8 1002.9,200.7 1003.5,186.6 1004.0,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1006.2,182.8 1006.7,190.3 1007.3,195.0 1007.8,196.9 1008.3,198.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1009.9,196.0 1010.5,192.2 1011.0,189.4 1011.6,192.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1013.7,193.1 1014.3,187.5 1014.8,185.6 1015.3,190.3 1015.9,185.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1017.5,180.9 1018.0,188.4 1018.6,193.1 1019.1,190.3 1019.7,188.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1021.3,185.6 1021.8,180.9 1022.3,176.2 1022.9,170.6 1023.4,174.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1025.0,176.2 1025.6,180.9 1026.1,184.7 1026.7,183.7 1027.2,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1028.8,181.9 1029.4,186.6 1029.9,188.4 1030.4,181.9 1031.0,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1032.6,181.9 1033.1,184.7 1033.7,186.6 1034.2,191.3 1034.7,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1036.4,187.5 1036.9,187.5 1037.4,187.5 1038.0,187.5 1038.5,182.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1040.1,182.8 1040.7,189.4 1041.2,187.5 1041.8,186.6 1042.3,173.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1043.9,173.4 1044.5,168.7 1045.0,168.7 1045.5,173.4 1046.1,170.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1048.2,168.7 1048.8,164.9 1049.3,152.7 1049.8,146.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1051.5,144.3 1052.0,142.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<text x="1058" y="146.4" font-size="11.5" font-weight="700" fill="var(--s-dgs2)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 2년물 국채금리 4.67%</text>
</svg>
</div>

---

## 2. 해석

- **상승**: 연준이 정책금리를 더 높이 올리거나 높은 수준을 더 오래 끌고 갈 것이라는 기대가 커졌다는 신호로 흔히 해석한다 — 인플레이션 지표가 예상보다 높게 나오거나 고용이 강하게 나온 뒤 가장 먼저 반응하는 만기다.
- **하락**: 인하 시점이 앞당겨졌거나 인하 폭이 커질 것이라는 기대, 또는 경기 둔화·안전자산 수요 확대 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 2년물 수익률은 대략 "앞으로 2년간 평균 단기금리가 어디쯤일지"에 대한 기대에 얇은 기간 프리미엄(만기가 길어질수록 투자자가 추가로 요구하는 보상)을 더한 값이다. 연준이 직접 정하는 것은 하루짜리 금리뿐이지만, 2년이라는 기간은 통화정책 사이클 한 국면을 온전히 담을 만큼 길면서도 장기 성장·물가 기대에 휘둘릴 만큼 길지는 않다 — 그래서 정책 경로 기대만 따로 떼어 보기에 가장 적합한 만기로 취급된다.
- **밸류에이션 할인율에는 쓰지 않는다**: DCF 무위험이자율의 표준은 [10년물](./treasury_10y.md)이다. 이 문서는 정책 국면과 수익률곡선 모양을 읽기 위한 자료다.
- **정의를 섞지 않는다**: FRED `DGS2`는 상수만기·투자수익률(investment basis) 기준이다. 단기 재정증권을 **할인율**(discount yield)로 표시하는 지표와는 계산 기준 자체가 달라 소수점 단위로 어긋나므로, 두 값을 그대로 빼서 스프레드로 쓰지 않는다.

---

*작성일: 2026-09-18*
