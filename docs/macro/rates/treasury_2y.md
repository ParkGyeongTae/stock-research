# 미국 2년물 국채금리

::: info
만기 2년 미 국채의 상수만기 수익률이다(FRED `DGS2`). 만기가 짧아 장기 성장·물가 기대에 덜 휘둘리는 대신 **앞으로 몇 차례 FOMC 결정의 경로**가 압축돼 담기는 구간이라, 연준 정책금리 기대의 대표 프록시로 인용된다. [10년물](./treasury_10y.md)과의 차이는 수익률곡선 기울기의 표준 척도다.
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-16 · 단위: % · 출처: FRED DGS2</text>
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
<polyline points="60.0,562.5 60.5,562.5 61.1,561.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="63.2,560.6 63.8,560.6 64.3,559.7 64.8,559.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="66.5,561.5 67.0,561.5 67.5,561.5 68.1,559.7 68.6,559.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="70.2,559.7 70.8,560.6 71.3,557.8 71.9,555.9 72.4,554.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="74.0,552.1 74.5,552.1 75.1,553.1 75.6,555.0 76.2,555.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="77.8,555.9 78.3,555.0 78.9,553.1 79.4,551.2 79.9,551.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="82.1,548.4 82.6,546.5 83.2,547.4 83.7,542.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="85.3,539.9 85.9,542.7 86.4,543.7 86.9,539.0 87.5,536.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="89.1,537.1 89.6,537.1 90.2,534.3 90.7,534.3 91.3,536.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="92.9,534.3 93.4,538.0 93.9,537.1 94.5,542.7 95.0,544.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="96.6,539.0 97.2,542.7 97.7,533.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="98.8" cy="531.5" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="100.4,531.5 101.0,530.5 101.5,532.4 102.0,532.4 102.6,532.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="104.2,522.1 104.7,524.9 105.3,521.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="106.3" cy="534.3" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="108.0,533.3 108.5,532.4 109.0,528.6 109.6,522.1 110.1,524.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="111.7,520.2 112.3,515.5 112.8,517.4 113.3,515.5 113.9,518.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="115.5,519.3 116.0,518.3 116.6,516.4 117.1,521.1 117.7,519.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="119.3,520.2 119.8,515.5 120.3,517.4 120.9,514.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="123.0,509.9 123.6,511.7 124.1,510.8 124.7,512.7 125.2,512.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="126.8,508.0 127.4,508.9 127.9,503.3 128.4,498.6 129.0,499.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="130.6,494.8 131.1,496.7 131.7,494.8 132.2,495.8 132.7,488.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="134.9,481.7 135.4,483.5 136.0,479.8 136.5,486.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="138.1,488.2 138.7,485.4 139.2,475.1 139.7,470.4 140.3,473.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="141.9,470.4 142.4,470.4 143.0,472.3 143.5,469.4 144.1,458.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="145.7,459.1 146.2,454.4 146.8,453.5 147.3,430.0 147.8,440.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="149.4,432.8 150.0,432.8 150.5,438.4 151.1,441.2 151.6,443.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="153.8,434.7 154.3,432.8 154.8,436.5 155.4,435.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="157.0,445.9 157.5,458.2 158.1,440.3 158.6,437.5 159.1,440.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="160.8,435.6 161.3,428.1 161.8,423.4 162.4,419.6 162.9,416.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="164.5,405.5 165.1,407.4 165.6,398.0 166.2,399.0 166.7,396.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="168.3,380.2 168.8,376.4 169.4,381.1 169.9,381.1 170.5,365.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="172.1,360.4 172.6,360.4 173.2,364.2 173.7,367.0 174.2,352.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="175.9,352.9 176.4,345.4 176.9,346.3 177.5,349.1 178.0,343.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="179.6,346.3 180.2,356.7 180.7,358.5 181.2,349.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="183.4,350.1 183.9,336.0 184.5,336.9 185.0,329.4 185.5,325.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="187.2,334.1 187.7,342.6 188.2,338.8 188.8,334.1 189.3,327.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="190.9,324.7 191.5,320.0 192.0,331.3 192.6,326.6 193.1,325.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="194.7,336.0 195.2,335.0 195.8,331.3 196.3,340.7 196.9,336.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="198.5,338.8 199.0,326.6 199.6,329.4 200.1,334.1 200.6,336.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="202.3,332.2 202.8,346.3 203.3,348.2 203.9,350.1 204.4,349.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="206.6,343.5 207.1,331.3 207.6,332.2 208.2,331.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="209.8,324.7 210.3,322.8 210.9,320.0 211.4,315.3 212.0,293.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="213.6,261.7 214.1,257.0 214.6,280.5 215.2,286.2 215.7,283.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="217.9,279.6 218.4,293.7 219.0,298.4 219.5,295.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="221.1,291.8 221.7,289.9 222.2,293.7 222.7,306.9 223.3,314.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="225.4,316.3 226.0,302.2 226.5,296.5 227.0,288.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="228.7,292.8 229.2,296.5 229.7,287.1 230.3,285.2 230.8,287.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="232.4,285.2 233.0,277.7 233.5,275.8 234.0,289.9 234.6,301.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="236.2,299.3 236.7,297.5 237.3,303.1 237.8,313.4 238.4,309.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="240.0,308.7 240.5,293.7 241.0,289.9 241.6,296.5 242.1,276.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="243.7,279.6 244.3,273.0 244.8,277.7 245.4,277.7 245.9,275.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="247.5,280.5 248.1,275.8 248.6,273.0 249.1,278.7 249.7,275.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="251.3,269.3 251.8,272.1 252.4,265.5 252.9,266.4 253.4,264.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="255.1,259.9 255.6,256.1 256.1,257.0 256.7,251.4 257.2,261.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="259.4,252.3 259.9,257.0 260.4,254.2 261.0,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="262.6,244.8 263.1,228.8 263.7,226.0 264.2,217.6 264.8,219.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="266.4,210.1 266.9,209.1 267.5,203.5 268.0,195.0 268.5,186.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="270.1,180.0 270.7,177.2 271.2,198.8 271.8,190.3 272.3,184.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="273.9,194.1 274.5,196.0 275.0,191.3 275.5,183.7 276.1,177.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="278.2,177.2 278.8,179.0 279.3,161.2 279.8,160.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="281.5,163.1 282.0,164.9 282.5,153.7 283.1,147.1 283.6,159.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="285.2,158.4 285.8,165.9 286.3,168.7 286.9,177.2 287.4,166.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="289.0,157.4 289.5,154.6 290.1,148.0 290.6,138.6 291.2,143.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="292.8,137.7 293.3,142.4 293.9,148.0 294.4,173.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="296.5,167.8 297.1,170.6 297.6,172.5 298.2,164.9 298.7,157.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="300.3,160.2 300.9,161.2 301.4,162.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="302.5" cy="165.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="304.1,162.1 304.6,160.2 305.2,169.6 305.7,181.9 306.2,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="307.9,166.8 308.4,173.4 308.9,180.9 309.5,176.2 310.0,174.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="311.6,168.7 312.2,184.7 312.7,183.7 313.3,183.7 313.8,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="315.4,181.9 315.9,181.9 316.5,185.6 317.0,182.8 317.6,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="319.7,175.3 320.3,176.2 320.8,173.4 321.3,166.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="323.5,167.8 324.0,171.5 324.6,163.1 325.1,182.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="326.7,187.5 327.3,182.8 327.8,186.6 328.3,194.1 328.9,184.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="331.0,188.4 331.6,199.7 332.1,196.9 332.7,192.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="334.3,185.6 334.8,194.1 335.3,195.0 335.9,189.4 336.4,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="338.0,181.9 338.6,185.6 339.1,196.9 339.7,196.9 340.2,177.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="341.8,164.0 342.4,161.2 342.9,163.1 343.4,160.2 344.0,158.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="345.6,156.5 346.1,149.0 346.7,147.1 347.2,147.1 347.7,149.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="349.9,142.4 350.4,143.3 351.0,143.3 351.5,132.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="353.1,132.0 353.7,129.2 354.2,121.7 354.7,121.7 355.3,124.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="356.9,121.7 357.4,111.4 358.0,106.7 358.5,120.8 359.1,149.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="360.7,202.5 361.2,186.6 361.7,211.9 362.3,192.2 362.8,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="364.4,212.9 365.0,189.4 365.5,209.1 366.1,227.9 366.6,227.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="368.2,211.0 368.8,203.5 369.3,197.8 369.8,196.0 370.4,199.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="372.0,208.2 372.5,220.4 373.1,225.1 373.6,222.3 374.1,208.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="375.8,205.4 376.3,202.5 376.8,210.1 377.4,209.1 377.9,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="379.5,188.4 380.1,187.5 380.6,182.8 381.1,192.2 381.7,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="383.3,194.1 383.8,218.5 384.4,214.8 384.9,198.8 385.5,201.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="387.1,192.2 387.6,208.2 388.2,215.7 388.7,228.8 389.2,212.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="390.8,205.4 391.4,204.4 391.9,214.8 392.5,215.7 393.0,207.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="394.6,206.3 395.2,199.7 395.7,194.1 396.2,182.8 396.8,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="398.4,178.1 398.9,180.9 399.5,176.2 400.0,158.4 400.5,154.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="402.7,162.1 403.2,167.8 403.8,174.3 404.3,158.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="405.9,162.1 406.5,157.4 407.0,152.7 407.6,156.5 408.1,149.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="409.7,153.7 410.2,142.4 410.8,135.8 411.3,147.1 411.9,139.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="414.0,141.4 414.6,141.4 415.1,133.0 415.6,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="417.2,144.3 417.8,135.8 418.3,138.6 418.9,123.6 419.4,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="421.0" cy="117.0" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="422.1,117.0 422.6,112.3 423.2,117.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="424.8,125.5 425.3,122.7 425.9,137.7 426.4,149.9 426.9,135.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="428.6,135.8 429.1,135.8 429.6,135.8 430.2,130.2 430.7,128.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="432.3,129.2 432.9,125.5 433.4,128.3 434.0,119.8 434.5,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="436.1,122.7 436.6,118.9 437.2,122.7 437.7,120.8 438.3,132.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="439.9,133.9 440.4,135.8 441.0,131.1 441.5,128.3 442.0,121.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="443.7,115.1 444.2,118.9 444.7,114.2 445.3,117.0 445.8,118.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="447.4,114.2 448.0,109.5 448.5,116.1 449.0,113.3 449.6,108.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="451.2,113.3 451.7,123.6 452.3,120.8 452.8,125.5 453.4,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="455.5,117.0 456.0,110.4 456.6,117.0 457.1,113.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="458.7,114.2 459.3,113.3 459.8,115.1 460.4,111.4 460.9,109.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="462.5,106.7 463.1,103.9 463.6,100.1 464.1,100.1 464.7,102.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="466.3,102.9 466.8,107.6 467.4,102.0 467.9,107.6 468.4,108.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="470.1,100.1 470.6,97.3 471.1,106.7 471.7,108.6 472.2,103.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="474.4,115.1 474.9,112.3 475.4,105.7 476.0,107.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="477.6,102.9 478.1,93.5 478.7,93.5 479.2,98.2 479.8,104.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="481.4,106.7 481.9,109.5 482.4,103.9 483.0,109.5 483.5,112.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="485.1,108.6 485.7,104.8 486.2,116.1 486.8,113.3 487.3,127.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="488.9,118.0 489.5,119.8 490.0,118.0 490.5,108.6 491.1,107.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="492.7,109.5 493.2,130.2 493.8,120.8 494.3,127.4 494.8,122.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="496.5,121.7 497.0,124.5 497.5,121.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="498.6" cy="118.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="500.2,126.4 500.8,136.7 501.3,145.2 501.8,136.7 502.4,152.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="504.0,145.2 504.5,151.8 505.1,149.0 505.6,150.8 506.2,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="507.8,138.6 508.3,136.7 508.9,162.1 509.4,170.6 509.9,164.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="511.5,164.9 512.1,166.8 512.6,173.4 513.2,174.3 513.7,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="515.9,180.9 516.4,186.6 516.9,180.9 517.5,183.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="519.6,174.3 520.2,174.3 520.7,169.6 521.2,167.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="522.9,171.5 523.4,171.5 523.9,170.6 524.5,180.9 525.0,192.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="527.2,184.7 527.7,173.4 528.2,173.4 528.8,168.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="530.4,170.6 530.9,176.2 531.5,173.4 532.0,179.0 532.6,173.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="534.2,178.1 534.7,171.5 535.3,180.0 535.8,186.6 536.3,171.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="537.9,162.1 538.5,168.7 539.0,166.8 539.6,162.1 540.1,160.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="541.7,162.1 542.3,145.2 542.8,152.7 543.3,152.7 543.9,145.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="546.0,149.9 546.6,145.2 547.1,140.5 547.6,142.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="549.3,140.5 549.8,139.6 550.3,145.2 550.9,145.2 551.4,154.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="553.0,148.0 553.6,154.6 554.1,153.7 554.7,158.4 555.2,160.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="556.8,157.4 557.3,150.8 557.9,148.0 558.4,141.4 559.0,137.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="560.6,136.7 561.1,141.4 561.7,149.9 562.2,147.1 562.7,149.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="564.4,154.6 564.9,152.7 565.4,154.6 566.0,149.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="568.1,137.7 568.7,139.6 569.2,141.4 569.7,144.3 570.3,136.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="571.9,132.0 572.4,135.8 573.0,114.2 573.5,118.0 574.1,122.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="575.7,118.0 576.2,114.2 576.7,118.0 577.3,113.3 577.8,114.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="579.4,114.2 580.0,124.5 580.5,121.7 581.1,115.1 581.6,115.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="583.2,114.2 583.8,107.6 584.3,115.1 584.8,123.6 585.4,129.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="587.0,128.3 587.5,128.3 588.1,126.4 588.6,130.2 589.1,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="590.8,125.5 591.3,129.2 591.8,136.7 592.4,132.0 592.9,127.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="594.5,128.3 595.1,128.3 595.6,124.5 596.1,119.8 596.7,118.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="598.8,117.0 599.4,115.1 599.9,118.9 600.5,121.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="602.1,128.3 602.6,133.0 603.1,137.7 603.7,137.7 604.2,123.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="605.8,123.6 606.4,129.2 606.9,134.9 607.5,141.4 608.0,142.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="609.6,134.9 610.2,140.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="611.2,139.6 611.8,139.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="613.4,138.6 613.9,144.3 614.5,138.6 615.0,139.6 615.5,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="617.2,133.0 617.7,135.8 618.2,138.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="619.3" cy="149.0" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="620.9,147.1 621.5,147.1 622.0,147.1 622.5,158.4 623.1,163.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="624.7,164.0 625.2,164.9 625.8,165.9 626.3,162.1 626.9,159.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="628.5,158.4 629.0,167.8 629.6,170.6 630.1,166.8 630.6,171.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="632.2,171.5 632.8,172.5 633.3,178.1 633.9,190.3 634.4,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="636.0,215.7 636.6,206.3 637.1,205.4 637.6,201.6 638.2,200.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="639.8,204.4 640.3,211.9 640.9,211.0 641.4,197.8 641.9,199.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="643.6,199.7 644.1,206.3 644.6,212.9 645.2,206.3 645.7,214.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="647.3,213.8 647.9,221.3 648.4,221.3 648.9,217.6 649.5,213.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="651.6,216.6 652.2,227.9 652.7,228.8 653.3,237.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="654.9,235.4 655.4,243.9 656.0,241.1 656.5,239.2 657.0,245.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="658.6,246.7 659.2,243.9 659.7,242.0 660.3,243.9 660.8,247.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="662.4,245.8 663.0,253.3 663.5,249.5 664.0,242.9 664.6,247.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="666.2,237.3 666.7,242.0 667.3,240.1 667.8,233.5 668.3,211.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="670.0,206.3 670.5,207.2 671.0,206.3 671.6,207.2 672.1,210.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="674.3,210.1 674.8,211.9 675.4,209.1 675.9,210.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="677.5,203.5 678.0,202.5 678.6,198.8 679.1,198.8 679.7,195.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="681.3,194.1 681.8,195.0 682.4,191.3 682.9,190.3 683.4,185.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="685.1,189.4 685.6,187.5 686.1,180.0 686.7,185.6 687.2,180.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="689.4,173.4 689.9,180.0 690.4,173.4 691.0,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="692.6,178.1 693.1,180.0 693.7,176.2 694.2,173.4 694.8,170.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="696.4,185.6 696.9,185.6 697.4,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="698.5" cy="193.1" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="700.1,189.4 700.7,189.4 701.2,193.1 701.8,191.3 702.3,196.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="703.9,193.1 704.4,191.3 705.0,191.3 705.5,188.4 706.1,181.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="707.7,181.9 708.2,181.9 708.8,172.5 709.3,175.3 709.8,177.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="711.5,177.2 712.0,178.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="713.1,177.2 713.6,176.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="715.2,182.8 715.8,181.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="716.8,181.9 717.4,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="719.0,179.0 719.5,177.2 720.1,179.0 720.6,180.0 721.2,167.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="722.8,167.8 723.3,170.6 723.8,180.0 724.4,183.7 724.9,180.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="727.1,178.1 727.6,178.1 728.2,178.1 728.7,180.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="730.3,189.4 730.9,187.5 731.4,185.6 731.9,188.4 732.5,184.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="734.1,180.9 734.6,185.6 735.2,189.4 735.7,185.6 736.2,178.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="737.9,179.0 738.4,178.1 738.9,171.5 739.5,176.2 740.0,180.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="742.2,178.1 742.7,179.0 743.2,179.0 743.8,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="745.4,193.1 745.9,198.8 746.5,200.7 747.0,198.8 747.6,206.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="749.2,209.1 749.7,209.1 750.3,206.3 750.8,209.1 751.3,206.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="752.9,215.7 753.5,211.0 754.0,204.4 754.6,211.0 755.1,203.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="756.7,199.7 757.3,201.6 757.8,206.3 758.3,210.1 758.9,211.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="760.5,201.6 761.0,209.1 761.6,207.2 762.1,208.2 762.6,215.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="764.3,215.7 764.8,217.6 765.3,213.8 765.9,232.6 766.4,235.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="768.0,230.7 768.6,232.6 769.1,213.8 769.6,220.4 770.2,209.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="771.8,220.4 772.3,220.4 772.9,227.0 773.4,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="775.6,228.8 776.1,227.9 776.7,223.2 777.2,227.0 777.7,229.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="779.3,236.4 779.9,238.2 780.4,242.9 781.0,233.5 781.5,221.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="783.1,221.3 783.7,226.0 784.2,226.0 784.7,214.8 785.3,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="786.9,207.2 787.4,203.5 788.0,200.7 788.5,209.1 789.0,207.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="790.7,208.2 791.2,208.2 791.7,205.4 792.3,205.4 792.8,205.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="795.0,212.9 795.5,209.1 796.1,212.9 796.6,215.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="798.2,211.0 798.7,209.1 799.3,217.6 799.8,212.9 800.4,201.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="802.0,204.4 802.5,204.4 803.1,211.0 803.6,214.8 804.1,209.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="805.8,208.2 806.3,211.0 806.8,211.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="807.9" cy="214.8" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="809.5,220.4 810.1,228.8 810.6,229.8 811.1,233.5 811.7,230.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="813.3,231.7 813.8,226.0 814.4,226.0 814.9,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="817.1,214.8 817.6,214.8 818.1,218.5 818.7,218.5 819.2,214.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="820.8,214.8 821.4,210.1 821.9,216.6 822.5,213.8 823.0,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="824.6,219.5 825.1,221.3 825.7,216.6 826.2,213.8 826.8,213.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="828.4,213.8 828.9,218.5 829.5,211.0 830.0,211.0 830.5,234.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="832.2,234.5 832.7,231.7 833.2,234.5 833.8,231.7 834.3,227.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="835.9,227.9 836.5,231.7 837.0,236.4 837.5,229.8 838.1,228.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="839.7,227.0 840.2,228.8 840.8,229.8 841.3,225.1 841.9,235.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="843.5,230.7 844.0,242.0 844.5,243.9 845.1,241.1 845.6,243.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="847.8,237.3 848.3,242.0 848.9,243.9 849.4,251.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="851.0,253.3 851.6,248.6 852.1,248.6 852.6,250.5 853.2,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="854.8,248.6 855.3,251.4 855.9,250.5 856.4,245.8 856.9,245.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="858.6,242.0 859.1,249.5 859.6,245.8 860.2,239.2 860.7,240.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="862.3,240.1 862.9,242.9 863.4,247.6 863.9,247.6 864.5,244.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="866.1,242.9 866.6,245.8 867.2,244.8 867.7,242.9 868.3,250.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="870.4,254.2 871.0,252.3 871.5,260.8 872.0,256.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="873.6,256.1 874.2,257.0 874.7,257.0 875.3,254.2 875.8,254.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="877.4,254.2 878.0,255.2 878.5,243.9 879.0,242.0 879.6,242.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="881.2,242.9 881.7,244.8 882.3,240.1 882.8,245.8 883.3,247.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="885.0" cy="244.8" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="886.0,246.7 886.6,244.8 887.1,241.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="888.7,242.9 889.3,244.8 889.8,244.8 890.3,247.6 890.9,251.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="892.5,256.1 893.0,258.9 893.6,257.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="894.7" cy="255.2" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="896.3,248.6 896.8,251.4 897.4,253.3 897.9,250.5 898.4,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="900.0,245.8 900.6,242.0 901.1,248.6 901.7,250.5 902.2,250.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="903.8,251.4 904.4,254.2 904.9,253.3 905.4,256.1 906.0,254.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="907.6,258.0 908.1,254.2 908.7,255.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="909.7" cy="256.1" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="911.4,257.0 911.9,257.0 912.4,255.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="913.5" cy="255.2" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="915.1,256.1 915.7,255.2 916.2,255.2 916.8,253.3 917.3,248.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="918.9,248.6 919.4,249.5 920.0,251.4 920.5,246.7 921.1,243.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="923.2,242.9 923.8,242.9 924.3,242.0 924.8,242.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="926.5,246.7 927.0,249.5 927.5,246.7 928.1,249.5 928.6,250.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="930.2,245.8 930.8,245.8 931.3,245.8 931.8,255.2 932.4,252.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="934.0,254.2 934.5,257.0 935.1,250.5 935.6,255.2 936.1,261.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="938.3,258.9 938.8,255.2 939.4,255.2 939.9,254.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="941.5,258.9 942.1,258.9 942.6,257.0 943.2,259.9 943.7,263.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="945.3,255.2 945.8,251.4 946.4,248.6 946.9,245.8 947.5,246.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="949.1,246.7 949.6,245.8 950.2,239.2 950.7,227.9 951.2,230.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="952.9,235.4 953.4,235.4 953.9,227.9 954.5,225.1 955.0,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="956.6,221.3 957.2,214.8 957.7,220.4 958.2,209.1 958.8,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="960.4,222.3 960.9,225.1 961.5,223.2 962.0,225.1 962.6,220.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="964.2,220.4 964.7,223.2 965.2,225.1 965.8,226.0 966.3,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="967.9,226.0 968.5,227.9 969.0,227.9 969.6,226.0 970.1,232.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="971.7,231.7 972.3,226.0 972.8,225.1 973.3,221.3 973.9,226.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="975.5,226.0 976.0,220.4 976.6,212.9 977.1,216.6 977.6,216.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="979.3,210.1 979.8,211.9 980.3,217.6 980.9,212.9 981.4,214.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="983.0,210.1 983.6,205.4 984.1,207.2 984.6,205.4 985.2,196.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="986.8,198.8 987.3,193.1 987.9,201.6 988.4,197.8 989.0,193.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="991.1,204.4 991.7,205.4 992.2,206.3 992.7,207.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="994.3,200.7 994.9,200.7 995.4,197.8 996.0,200.7 996.5,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="998.1,191.3 998.7,193.1 999.2,193.1 999.7,200.7 1000.3,196.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1001.9,198.8 1002.4,200.7 1003.0,186.6 1003.5,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1005.7,182.8 1006.2,190.3 1006.7,195.0 1007.3,196.9 1007.8,198.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1009.4,196.0 1010.0,192.2 1010.5,189.4 1011.0,192.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1013.2,193.1 1013.7,187.5 1014.3,185.6 1014.8,190.3 1015.4,185.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1017.0,180.9 1017.5,188.4 1018.1,193.1 1018.6,190.3 1019.1,188.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1020.7,185.6 1021.3,180.9 1021.8,176.2 1022.4,170.6 1022.9,174.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1024.5,176.2 1025.1,180.9 1025.6,184.7 1026.1,183.7 1026.7,179.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1028.3,181.9 1028.8,186.6 1029.4,188.4 1029.9,181.9 1030.4,187.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1032.1,181.9 1032.6,184.7 1033.1,186.6 1033.7,191.3 1034.2,189.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1035.8,187.5 1036.4,187.5 1036.9,187.5 1037.5,187.5 1038.0,182.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1039.6,182.8 1040.1,189.4 1040.7,187.5 1041.2,186.6 1041.8,173.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1043.4,173.4 1043.9,168.7 1044.5,168.7 1045.0,173.4 1045.5,170.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1047.7,168.7 1048.2,164.9 1048.8,152.7 1049.3,146.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1050.9,144.3 1051.5,142.4 1052.0,135.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<text x="1058" y="139.8" font-size="11.5" font-weight="700" fill="var(--s-dgs2)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 2년물 국채금리 4.74%</text>
</svg>
</div>

---

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **한 줄로**: 시장이 예상하는 **연준의 향후 행보**가 가장 또렷하게 찍히는 금리다.
- **오르면**: 정책금리를 더 높이 올리거나 높은 수준을 더 오래 끌고 갈 것이라는 기대가 커졌다는 신호로 흔히 해석한다 — 물가·고용 지표가 예상보다 강하게 나온 뒤 가장 먼저 반응하는 만기다.
- **내리면**: 인하 시점이 앞당겨졌거나 인하 폭이 커질 것이라는 기대, 또는 경기 둔화·안전자산 수요 확대 신호로 흔히 해석한다.
- **왜 이 만기인가**: 2년물 금리는 대략 "앞으로 2년간의 평균 단기금리 기대"에 얇은 기간 프리미엄(만기가 길수록 투자자가 더 요구하는 보상)을 더한 값이다. 연준이 직접 정하는 것은 하루짜리 금리뿐이지만, 2년은 정책 사이클 한 국면을 담을 만큼 길면서 장기 기대에 휘둘릴 만큼 길지는 않다.
- **밸류에이션 할인율에는 쓰지 않는다**: DCF 무위험이자율의 표준은 [10년물](./treasury_10y.md)이다. 이 문서는 정책 국면과 수익률곡선 모양을 읽기 위한 자료다.
- **정의를 섞지 않는다**: `DGS2`는 상수만기·투자수익률(investment basis) 기준이다. 단기 재정증권을 **할인율**(discount yield)로 표시하는 지표와는 계산 기준이 달라, 두 값을 그대로 빼서 스프레드로 쓰면 안 된다.
- **상수만기(constant maturity)라는 표기**: 실제로 만기가 정확히 그 기간인 채권 하나의 값이 아니라, 거래되는 여러 국채의 수익률곡선에서 그 만기 지점을 읽어 낸 값이다. 시간이 지나도 만기가 줄지 않는 일정한 잣대를 유지하기 위한 방식이다.
- **차트의 회색 음영**: NBER이 사후에 판정한 미국의 침체 국면이다. 실시간 신호가 아니라 나중에 붙는 라벨이다.

---

*작성일: 2026-09-18*
