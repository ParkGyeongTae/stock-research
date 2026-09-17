# 미국 국채금리 3종 비교 (수익률곡선)

::: info
[2년물](./treasury_2y.md)·[10년물](./treasury_10y.md)·[30년물](./treasury_30y.md)을 한 차트에 겹쳐, 수익률곡선이 가팔라졌는지·평평해졌는지·역전됐는지를 보기 위한 자료다. 통화·금속 비교 문서와 달리 **지수화하지 않는다** — 셋 다 이미 같은 단위(%)이고, 금리는 0%에 가까워질 수 있어 그런 값을 기준(100)으로 나누면 지수가 크게 왜곡되기 때문이다.
:::

---

## 1. 차트 — 최근 5년 일간, 원값(%) 그대로 겹침

<style>
.fred-dgs2-dgs10-dgs30 {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-dgs2:#2a78d6; --s-dgs10:#eb6834; --s-dgs30:#1baf7a;
}
.dark .fred-dgs2-dgs10-dgs30 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs2:#3987e5; --s-dgs10:#d95926; --s-dgs30:#199e70; }
.fred-dgs2-dgs10-dgs30 svg { width:100%; height:auto; display:block; }
.fred-dgs2-dgs10-dgs30 text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-dgs2-dgs10-dgs30 .title { fill: var(--ink); font-weight:600; }
.fred-dgs2-dgs10-dgs30 .grid { stroke: var(--grid); stroke-width:1; }
.fred-dgs2-dgs10-dgs30 .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-dgs2-dgs10-dgs30">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미국 2년물 국채금리·미국 10년물 국채금리·미국 30년물 국채금리, 최근 5년 일간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 국채금리 3종 비교 (상수만기) (최근 5년 일간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-16 · 단위: % · 출처: FRED DGS2 · FRED DGS10 · FRED DGS30</text>
<line x1="60" y1="580.6" x2="1052" y2="580.6" class="grid"/>
<text x="52" y="584.6" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="489.9" x2="1052" y2="489.9" class="grid"/>
<text x="52" y="493.9" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="399.2" x2="1052" y2="399.2" class="grid"/>
<text x="52" y="403.2" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="308.5" x2="1052" y2="308.5" class="grid"/>
<text x="52" y="312.5" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="217.8" x2="1052" y2="217.8" class="grid"/>
<text x="52" y="221.8" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="127.1" x2="1052" y2="127.1" class="grid"/>
<text x="52" y="131.1" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
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
<polyline points="60.0,562.5 60.5,562.5 61.1,561.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="63.2,560.7 63.8,560.7 64.3,559.8 64.8,559.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="66.5,561.6 67.0,561.6 67.5,561.6 68.1,559.8 68.6,559.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="70.2,559.8 70.8,560.7 71.3,557.9 71.9,556.1 72.4,554.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="74.0,552.5 74.5,552.5 75.1,553.4 75.6,555.2 76.2,556.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="77.8,556.1 78.3,555.2 78.9,553.4 79.4,551.6 79.9,551.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="82.1,548.9 82.6,547.1 83.2,548.0 83.7,543.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="85.3,540.7 85.9,543.4 86.4,544.3 86.9,539.8 87.5,537.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="89.1,538.0 89.6,538.0 90.2,535.3 90.7,535.3 91.3,537.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="92.9,535.3 93.4,538.9 93.9,538.0 94.5,543.4 95.0,545.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="96.6,539.8 97.2,543.4 97.7,534.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="98.8" cy="532.5" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="100.4,532.5 101.0,531.6 101.5,533.5 102.0,533.5 102.6,533.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="104.2,523.5 104.7,526.2 105.3,522.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="106.3" cy="535.3" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="108.0,534.4 108.5,533.5 109.0,529.8 109.6,523.5 110.1,526.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="111.7,521.7 112.3,517.1 112.8,518.9 113.3,517.1 113.9,519.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="115.5,520.8 116.0,519.8 116.6,518.0 117.1,522.6 117.7,520.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="119.3,521.7 119.8,517.1 120.3,518.9 120.9,516.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="123.0,511.7 123.6,513.5 124.1,512.6 124.7,514.4 125.2,514.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="126.8,509.9 127.4,510.8 127.9,505.3 128.4,500.8 129.0,501.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="130.6,497.2 131.1,499.0 131.7,497.2 132.2,498.1 132.7,490.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="134.9,484.5 135.4,486.3 136.0,482.7 136.5,489.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="138.1,490.8 138.7,488.1 139.2,478.1 139.7,473.6 140.3,476.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="141.9,473.6 142.4,473.6 143.0,475.4 143.5,472.7 144.1,461.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="145.7,462.7 146.2,458.2 146.8,457.3 147.3,434.6 147.8,444.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="149.4,437.3 150.0,437.3 150.5,442.7 151.1,445.5 151.6,447.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="153.8,439.1 154.3,437.3 154.8,440.9 155.4,440.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="157.0,450.0 157.5,461.8 158.1,444.6 158.6,441.8 159.1,444.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="160.8,440.0 161.3,432.8 161.8,428.2 162.4,424.6 162.9,421.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="164.5,411.0 165.1,412.8 165.6,403.7 166.2,404.6 166.7,401.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="168.3,386.5 168.8,382.9 169.4,387.4 169.9,387.4 170.5,372.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="172.1,367.5 172.6,367.5 173.2,371.1 173.7,373.8 174.2,359.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="175.9,360.2 176.4,352.9 176.9,353.9 177.5,356.6 178.0,351.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="179.6,353.9 180.2,363.8 180.7,365.6 181.2,356.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="183.4,357.5 183.9,343.9 184.5,344.8 185.0,337.5 185.5,333.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="187.2,342.1 187.7,350.2 188.2,346.6 188.8,342.1 189.3,335.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="190.9,333.0 191.5,328.5 192.0,339.3 192.6,334.8 193.1,333.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="194.7,343.9 195.2,343.0 195.8,339.3 196.3,348.4 196.9,343.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="198.5,346.6 199.0,334.8 199.6,337.5 200.1,342.1 200.6,344.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="202.3,340.2 202.8,353.9 203.3,355.7 203.9,357.5 204.4,356.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="206.6,351.1 207.1,339.3 207.6,340.2 208.2,339.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="209.8,333.0 210.3,331.2 210.9,328.5 211.4,323.9 212.0,303.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="213.6,272.2 214.1,267.7 214.6,290.4 215.2,295.8 215.7,293.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="217.9,289.4 218.4,303.1 219.0,307.6 219.5,304.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="221.1,301.2 221.7,299.4 222.2,303.1 222.7,315.8 223.3,323.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="225.4,324.8 226.0,311.2 226.5,305.8 227.0,297.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="228.7,302.1 229.2,305.8 229.7,296.7 230.3,294.9 230.8,296.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="232.4,294.9 233.0,287.6 233.5,285.8 234.0,299.4 234.6,310.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="236.2,308.5 236.7,306.7 237.3,312.1 237.8,322.1 238.4,318.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="240.0,317.6 240.5,303.1 241.0,299.4 241.6,305.8 242.1,286.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="243.7,289.4 244.3,283.1 244.8,287.6 245.4,287.6 245.9,285.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="247.5,290.4 248.1,285.8 248.6,283.1 249.1,288.5 249.7,285.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="251.3,279.5 251.8,282.2 252.4,275.8 252.9,276.7 253.4,274.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="255.1,270.4 255.6,266.8 256.1,267.7 256.7,262.2 257.2,272.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="259.4,263.1 259.9,267.7 260.4,265.0 261.0,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="262.6,255.9 263.1,240.5 263.7,237.7 264.2,229.6 264.8,231.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="266.4,222.3 266.9,221.4 267.5,216.0 268.0,207.8 268.5,199.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="270.1,193.3 270.7,190.6 271.2,211.4 271.8,203.3 272.3,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="273.9,206.9 274.5,208.7 275.0,204.2 275.5,196.9 276.1,190.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="278.2,190.6 278.8,192.4 279.3,175.2 279.8,174.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="281.5,177.0 282.0,178.8 282.5,167.9 283.1,161.5 283.6,173.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="285.2,172.4 285.8,179.7 286.3,182.4 286.9,190.6 287.4,180.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="289.0,171.5 289.5,168.8 290.1,162.5 290.6,153.4 291.2,157.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="292.8,152.5 293.3,157.0 293.9,162.5 294.4,186.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="296.5,181.5 297.1,184.2 297.6,186.0 298.2,178.8 298.7,171.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="300.3,174.2 300.9,175.2 301.4,176.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="302.5" cy="179.7" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="304.1,176.1 304.6,174.2 305.2,183.3 305.7,195.1 306.2,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="307.9,180.6 308.4,186.9 308.9,194.2 309.5,189.7 310.0,187.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="311.6,182.4 312.2,197.8 312.7,196.9 313.3,196.9 313.8,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="315.4,195.1 315.9,195.1 316.5,198.7 317.0,196.0 317.6,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="319.7,188.8 320.3,189.7 320.8,186.9 321.3,180.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="323.5,181.5 324.0,185.1 324.6,177.0 325.1,196.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="326.7,200.6 327.3,196.0 327.8,199.6 328.3,206.9 328.9,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="331.0,201.5 331.6,212.3 332.1,209.6 332.7,205.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="334.3,198.7 334.8,206.9 335.3,207.8 335.9,202.4 336.4,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="338.0,195.1 338.6,198.7 339.1,209.6 339.7,209.6 340.2,190.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="341.8,177.9 342.4,175.2 342.9,177.0 343.4,174.2 344.0,172.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="345.6,170.6 346.1,163.4 346.7,161.5 347.2,161.5 347.7,163.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="349.9,157.0 350.4,157.9 351.0,157.9 351.5,147.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="353.1,147.0 353.7,144.3 354.2,137.1 354.7,137.1 355.3,139.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="356.9,137.1 357.4,127.1 358.0,122.5 358.5,136.2 359.1,163.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="360.7,215.1 361.2,199.6 361.7,224.1 362.3,205.1 362.8,235.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="364.4,225.0 365.0,202.4 365.5,221.4 366.1,239.6 366.6,239.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="368.2,223.2 368.8,216.0 369.3,210.5 369.8,208.7 370.4,212.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="372.0,220.5 372.5,232.3 373.1,236.8 373.6,234.1 374.1,220.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="375.8,217.8 376.3,215.1 376.8,222.3 377.4,221.4 377.9,210.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="379.5,201.5 380.1,200.6 380.6,196.0 381.1,205.1 381.7,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="383.3,206.9 383.8,230.5 384.4,226.9 384.9,211.4 385.5,214.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="387.1,205.1 387.6,220.5 388.2,227.8 388.7,240.5 389.2,225.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="390.8,217.8 391.4,216.9 391.9,226.9 392.5,227.8 393.0,219.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="394.6,218.7 395.2,212.3 395.7,206.9 396.2,196.0 396.8,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="398.4,191.5 398.9,194.2 399.5,189.7 400.0,172.4 400.5,168.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="402.7,176.1 403.2,181.5 403.8,187.9 404.3,172.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="405.9,176.1 406.5,171.5 407.0,167.0 407.6,170.6 408.1,164.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="409.7,167.9 410.2,157.0 410.8,150.7 411.3,161.5 411.9,154.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="414.0,156.1 414.6,156.1 415.1,147.9 415.6,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="417.2,158.8 417.8,150.7 418.3,153.4 418.9,138.9 419.4,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="421.0" cy="132.5" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="422.1,132.5 422.6,128.0 423.2,132.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="424.8,140.7 425.3,138.0 425.9,152.5 426.4,164.3 426.9,150.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="428.6,150.7 429.1,150.7 429.6,150.7 430.2,145.2 430.7,143.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="432.3,144.3 432.9,140.7 433.4,143.4 434.0,135.2 434.5,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="436.1,138.0 436.6,134.3 437.2,138.0 437.7,136.2 438.3,147.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="439.9,148.8 440.4,150.7 441.0,146.1 441.5,143.4 442.0,137.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="443.7,130.7 444.2,134.3 444.7,129.8 445.3,132.5 445.8,134.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="447.4,129.8 448.0,125.3 448.5,131.6 449.0,128.9 449.6,124.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="451.2,128.9 451.7,138.9 452.3,136.2 452.8,140.7 453.4,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="455.5,132.5 456.0,126.2 456.6,132.5 457.1,128.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="458.7,129.8 459.3,128.9 459.8,130.7 460.4,127.1 460.9,125.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="462.5,122.5 463.1,119.8 463.6,116.2 464.1,116.2 464.7,118.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="466.3,118.9 466.8,123.5 467.4,118.0 467.9,123.5 468.4,124.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="470.1,116.2 470.6,113.5 471.1,122.5 471.7,124.4 472.2,119.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="474.4,130.7 474.9,128.0 475.4,121.6 476.0,123.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="477.6,118.9 478.1,109.8 478.7,109.8 479.2,114.4 479.8,120.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="481.4,122.5 481.9,125.3 482.4,119.8 483.0,125.3 483.5,128.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="485.1,124.4 485.7,120.7 486.2,131.6 486.8,128.9 487.3,142.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="488.9,133.4 489.5,135.2 490.0,133.4 490.5,124.4 491.1,123.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="492.7,125.3 493.2,145.2 493.8,136.2 494.3,142.5 494.8,138.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="496.5,137.1 497.0,139.8 497.5,137.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="498.6" cy="134.3" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="500.2,141.6 500.8,151.6 501.3,159.7 501.8,151.6 502.4,167.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="504.0,159.7 504.5,166.1 505.1,163.4 505.6,165.2 506.2,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="507.8,153.4 508.3,151.6 508.9,176.1 509.4,184.2 509.9,177.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="511.5,178.8 512.1,180.6 512.6,186.9 513.2,187.9 513.7,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="515.9,194.2 516.4,199.6 516.9,194.2 517.5,196.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="519.6,187.9 520.2,187.9 520.7,183.3 521.2,181.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="522.9,185.1 523.4,185.1 523.9,184.2 524.5,194.2 525.0,205.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="527.2,197.8 527.7,186.9 528.2,186.9 528.8,182.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="530.4,184.2 530.9,189.7 531.5,186.9 532.0,192.4 532.6,186.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="534.2,191.5 534.7,185.1 535.3,193.3 535.8,199.6 536.3,185.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="537.9,176.1 538.5,182.4 539.0,180.6 539.6,176.1 540.1,174.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="541.7,176.1 542.3,159.7 542.8,167.0 543.3,167.0 543.9,159.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="546.0,164.3 546.6,159.7 547.1,155.2 547.6,157.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="549.3,155.2 549.8,154.3 550.3,159.7 550.9,159.7 551.4,168.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="553.0,162.5 553.6,168.8 554.1,167.9 554.7,172.4 555.2,174.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="556.8,171.5 557.3,165.2 557.9,162.5 558.4,156.1 559.0,152.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="560.6,151.6 561.1,156.1 561.7,164.3 562.2,161.5 562.7,164.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="564.4,168.8 564.9,167.0 565.4,168.8 566.0,164.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="568.1,152.5 568.7,154.3 569.2,156.1 569.7,158.8 570.3,151.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="571.9,147.0 572.4,150.7 573.0,129.8 573.5,133.4 574.1,138.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="575.7,133.4 576.2,129.8 576.7,133.4 577.3,128.9 577.8,129.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="579.4,129.8 580.0,139.8 580.5,137.1 581.1,130.7 581.6,130.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="583.2,129.8 583.8,123.5 584.3,130.7 584.8,138.9 585.4,144.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="587.0,143.4 587.5,143.4 588.1,141.6 588.6,145.2 589.1,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="590.8,140.7 591.3,144.3 591.8,151.6 592.4,147.0 592.9,142.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="594.5,143.4 595.1,143.4 595.6,139.8 596.1,135.2 596.7,133.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="598.8,132.5 599.4,130.7 599.9,134.3 600.5,137.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="602.1,143.4 602.6,147.9 603.1,152.5 603.7,152.5 604.2,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="605.8,138.9 606.4,144.3 606.9,149.8 607.5,156.1 608.0,157.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="609.6,149.8 610.2,155.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="611.2,154.3 611.8,154.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="613.4,153.4 613.9,158.8 614.5,153.4 615.0,154.3 615.5,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="617.2,147.9 617.7,150.7 618.2,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="619.3" cy="163.4" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="620.9,161.5 621.5,161.5 622.0,161.5 622.5,172.4 623.1,177.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="624.7,177.9 625.2,178.8 625.8,179.7 626.3,176.1 626.9,173.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="628.5,172.4 629.0,181.5 629.6,184.2 630.1,180.6 630.6,185.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="632.2,185.1 632.8,186.0 633.3,191.5 633.9,203.3 634.4,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="636.0,227.8 636.6,218.7 637.1,217.8 637.6,214.2 638.2,213.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="639.8,216.9 640.3,224.1 640.9,223.2 641.4,210.5 641.9,212.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="643.6,212.3 644.1,218.7 644.6,225.0 645.2,218.7 645.7,226.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="647.3,226.0 647.9,233.2 648.4,233.2 648.9,229.6 649.5,226.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="651.6,228.7 652.2,239.6 652.7,240.5 653.3,248.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="654.9,246.8 655.4,255.0 656.0,252.3 656.5,250.4 657.0,256.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="658.6,257.7 659.2,255.0 659.7,253.2 660.3,255.0 660.8,258.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="662.4,256.8 663.0,264.1 663.5,260.4 664.0,254.1 664.6,258.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="666.2,248.6 666.7,253.2 667.3,251.4 667.8,245.0 668.3,224.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="670.0,218.7 670.5,219.6 671.0,218.7 671.6,219.6 672.1,222.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="674.3,222.3 674.8,224.1 675.4,221.4 675.9,222.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="677.5,216.0 678.0,215.1 678.6,211.4 679.1,211.4 679.7,207.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="681.3,206.9 681.8,207.8 682.4,204.2 682.9,203.3 683.4,198.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="685.1,202.4 685.6,200.6 686.1,193.3 686.7,198.7 687.2,194.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="689.4,186.9 689.9,193.3 690.4,186.9 691.0,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="692.6,191.5 693.1,193.3 693.7,189.7 694.2,186.9 694.8,184.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="696.4,198.7 696.9,198.7 697.4,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="698.5" cy="206.0" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="700.1,202.4 700.7,202.4 701.2,206.0 701.8,204.2 702.3,208.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="703.9,206.0 704.4,204.2 705.0,204.2 705.5,201.5 706.1,195.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="707.7,195.1 708.2,195.1 708.8,186.0 709.3,188.8 709.8,190.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="711.5,190.6 712.0,191.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="713.1,190.6 713.6,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="715.2,196.0 715.8,195.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="716.8,195.1 717.4,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="719.0,192.4 719.5,190.6 720.1,192.4 720.6,193.3 721.2,181.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="722.8,181.5 723.3,184.2 723.8,193.3 724.4,196.9 724.9,193.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="727.1,191.5 727.6,191.5 728.2,191.5 728.7,193.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="730.3,202.4 730.9,200.6 731.4,198.7 731.9,201.5 732.5,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="734.1,194.2 734.6,198.7 735.2,202.4 735.7,198.7 736.2,191.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="737.9,192.4 738.4,191.5 738.9,185.1 739.5,189.7 740.0,194.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="742.2,191.5 742.7,192.4 743.2,192.4 743.8,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="745.4,206.0 745.9,211.4 746.5,213.3 747.0,211.4 747.6,218.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="749.2,221.4 749.7,221.4 750.3,218.7 750.8,221.4 751.3,218.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="752.9,227.8 753.5,223.2 754.0,216.9 754.6,223.2 755.1,216.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="756.7,212.3 757.3,214.2 757.8,218.7 758.3,222.3 758.9,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="760.5,214.2 761.0,221.4 761.6,219.6 762.1,220.5 762.6,227.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="764.3,227.8 764.8,229.6 765.3,226.0 765.9,244.1 766.4,246.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="768.0,242.3 768.6,244.1 769.1,226.0 769.6,232.3 770.2,221.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="771.8,232.3 772.3,232.3 772.9,238.7 773.4,235.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="775.6,240.5 776.1,239.6 776.7,235.0 777.2,238.7 777.7,241.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="779.3,247.7 779.9,249.5 780.4,254.1 781.0,245.0 781.5,233.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="783.1,233.2 783.7,237.7 784.2,237.7 784.7,226.9 785.3,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="786.9,219.6 787.4,216.0 788.0,213.3 788.5,221.4 789.0,219.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="790.7,220.5 791.2,220.5 791.7,217.8 792.3,217.8 792.8,217.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="795.0,225.0 795.5,221.4 796.1,225.0 796.6,227.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="798.2,223.2 798.7,221.4 799.3,229.6 799.8,225.0 800.4,214.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="802.0,216.9 802.5,216.9 803.1,223.2 803.6,226.9 804.1,221.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="805.8,220.5 806.3,223.2 806.8,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="807.9" cy="226.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="809.5,232.3 810.1,240.5 810.6,241.4 811.1,245.0 811.7,242.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="813.3,243.2 813.8,237.7 814.4,237.7 814.9,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="817.1,226.9 817.6,226.9 818.1,230.5 818.7,230.5 819.2,226.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="820.8,226.9 821.4,222.3 821.9,228.7 822.5,226.0 823.0,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="824.6,231.4 825.1,233.2 825.7,228.7 826.2,226.0 826.8,226.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="828.4,226.0 828.9,230.5 829.5,223.2 830.0,223.2 830.5,245.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="832.2,245.9 832.7,243.2 833.2,245.9 833.8,243.2 834.3,239.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="835.9,239.6 836.5,243.2 837.0,247.7 837.5,241.4 838.1,240.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="839.7,238.7 840.2,240.5 840.8,241.4 841.3,236.8 841.9,246.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="843.5,242.3 844.0,253.2 844.5,255.0 845.1,252.3 845.6,255.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="847.8,248.6 848.3,253.2 848.9,255.0 849.4,262.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="851.0,264.1 851.6,259.5 852.1,259.5 852.6,261.3 853.2,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="854.8,259.5 855.3,262.2 855.9,261.3 856.4,256.8 856.9,256.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="858.6,253.2 859.1,260.4 859.6,256.8 860.2,250.4 860.7,251.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="862.3,251.4 862.9,254.1 863.4,258.6 863.9,258.6 864.5,255.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="866.1,254.1 866.6,256.8 867.2,255.9 867.7,254.1 868.3,261.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="870.4,265.0 871.0,263.1 871.5,271.3 872.0,266.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="873.6,266.8 874.2,267.7 874.7,267.7 875.3,265.0 875.8,265.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="877.4,265.0 878.0,265.9 878.5,255.0 879.0,253.2 879.6,254.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="881.2,254.1 881.7,255.9 882.3,251.4 882.8,256.8 883.3,258.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="885.0" cy="255.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="886.0,257.7 886.6,255.9 887.1,252.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="888.7,254.1 889.3,255.9 889.8,255.9 890.3,258.6 890.9,262.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="892.5,266.8 893.0,269.5 893.6,267.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="894.7" cy="265.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="896.3,259.5 896.8,262.2 897.4,264.1 897.9,261.3 898.4,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="900.0,256.8 900.6,253.2 901.1,259.5 901.7,261.3 902.2,261.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="903.8,262.2 904.4,265.0 904.9,264.1 905.4,266.8 906.0,265.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="907.6,268.6 908.1,265.0 908.7,265.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="909.7" cy="266.8" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="911.4,267.7 911.9,267.7 912.4,265.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="913.5" cy="265.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="915.1,266.8 915.7,265.9 916.2,265.9 916.8,264.1 917.3,259.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="918.9,259.5 919.4,260.4 920.0,262.2 920.5,257.7 921.1,255.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="923.2,254.1 923.8,254.1 924.3,253.2 924.8,254.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="926.5,257.7 927.0,260.4 927.5,257.7 928.1,260.4 928.6,261.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="930.2,256.8 930.8,256.8 931.3,256.8 931.8,265.9 932.4,263.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="934.0,265.0 934.5,267.7 935.1,261.3 935.6,265.9 936.1,272.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="938.3,269.5 938.8,265.9 939.4,265.9 939.9,265.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="941.5,269.5 942.1,269.5 942.6,267.7 943.2,270.4 943.7,274.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="945.3,265.9 945.8,262.2 946.4,259.5 946.9,256.8 947.5,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="949.1,257.7 949.6,256.8 950.2,250.4 950.7,239.6 951.2,242.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="952.9,246.8 953.4,246.8 953.9,239.6 954.5,236.8 955.0,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="956.6,233.2 957.2,226.9 957.7,232.3 958.2,221.4 958.8,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="960.4,234.1 960.9,236.8 961.5,235.0 962.0,236.8 962.6,232.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="964.2,232.3 964.7,235.0 965.2,236.8 965.8,237.7 966.3,235.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="967.9,237.7 968.5,239.6 969.0,239.6 969.6,237.7 970.1,244.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="971.7,243.2 972.3,237.7 972.8,236.8 973.3,233.2 973.9,237.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="975.5,237.7 976.0,232.3 976.6,225.0 977.1,228.7 977.6,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="979.3,222.3 979.8,224.1 980.3,229.6 980.9,225.0 981.4,226.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="983.0,222.3 983.6,217.8 984.1,219.6 984.6,217.8 985.2,209.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="986.8,211.4 987.3,206.0 987.9,214.2 988.4,210.5 989.0,206.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="991.1,216.9 991.7,217.8 992.2,218.7 992.7,219.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="994.3,213.3 994.9,213.3 995.4,210.5 996.0,213.3 996.5,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="998.1,204.2 998.7,206.0 999.2,206.0 999.7,213.3 1000.3,209.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1001.9,211.4 1002.4,213.3 1003.0,199.6 1003.5,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1005.7,196.0 1006.2,203.3 1006.7,207.8 1007.3,209.6 1007.8,211.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1009.4,208.7 1010.0,205.1 1010.5,202.4 1011.0,205.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1013.2,206.0 1013.7,200.6 1014.3,198.7 1014.8,203.3 1015.4,198.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1017.0,194.2 1017.5,201.5 1018.1,206.0 1018.6,203.3 1019.1,201.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1020.7,198.7 1021.3,194.2 1021.8,189.7 1022.4,184.2 1022.9,187.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1024.5,189.7 1025.1,194.2 1025.6,197.8 1026.1,196.9 1026.7,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1028.3,195.1 1028.8,199.6 1029.4,201.5 1029.9,195.1 1030.4,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1032.1,195.1 1032.6,197.8 1033.1,199.6 1033.7,204.2 1034.2,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1035.8,200.6 1036.4,200.6 1036.9,200.6 1037.5,200.6 1038.0,196.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1039.6,196.0 1040.1,202.4 1040.7,200.6 1041.2,199.6 1041.8,186.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1043.4,186.9 1043.9,182.4 1044.5,182.4 1045.0,186.9 1045.5,184.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1047.7,182.4 1048.2,178.8 1048.8,167.0 1049.3,160.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1050.9,158.8 1051.5,157.0 1052.0,150.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="60.0,461.8 60.5,463.6 61.1,460.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="63.2,455.4 63.8,458.2 64.3,462.7 64.8,458.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="66.5,460.0 67.0,464.5 67.5,461.8 68.1,459.1 68.6,456.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="70.2,461.8 70.8,460.0 71.3,460.9 71.9,452.7 72.4,447.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="74.0,446.4 74.5,440.9 75.1,440.0 75.6,442.7 76.2,446.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="77.8,445.5 78.3,440.9 78.9,441.8 79.4,437.3 79.9,434.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="82.1,436.4 82.6,439.1 83.2,442.7 83.7,436.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="85.3,436.4 85.9,431.0 86.4,431.0 86.9,428.2 87.5,430.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="89.1,431.9 89.6,432.8 90.2,440.9 90.7,438.2 91.3,440.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="92.9,437.3 93.4,439.1 93.9,435.5 94.5,441.8 95.0,449.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="96.6,443.7 97.2,448.2 97.7,439.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="98.8" cy="437.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="100.4,432.8 101.0,432.8 101.5,435.5 102.0,436.4 102.6,440.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="104.2,432.8 104.7,429.1 105.3,431.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="106.3" cy="446.4" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="108.0,442.7 108.5,450.9 109.0,450.9 109.6,450.0 110.1,458.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="111.7,450.9 112.3,446.4 112.8,442.7 113.3,445.5 113.9,446.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="115.5,451.8 116.0,450.0 116.6,447.3 117.1,450.0 117.7,452.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="119.3,450.9 119.8,446.4 120.3,448.2 120.9,444.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="123.0,446.4 123.6,445.5 124.1,440.0 124.7,442.7 125.2,442.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="126.8,432.8 127.4,430.0 127.9,425.5 128.4,423.7 129.0,421.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="130.6,419.2 131.1,421.9 131.7,422.8 132.2,426.4 132.7,419.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="134.9,411.0 135.4,414.6 136.0,414.6 136.5,421.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="138.1,421.9 138.7,419.2 139.2,412.8 139.7,416.4 140.3,419.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="141.9,418.3 142.4,416.4 143.0,419.2 143.5,415.5 144.1,405.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="145.7,406.5 146.2,402.8 146.8,404.6 147.3,396.5 147.8,406.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="149.4,401.0 150.0,394.7 150.5,396.5 151.1,401.9 151.6,406.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="153.8,404.6 154.3,400.1 154.8,402.8 155.4,401.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="157.0,414.6 157.5,424.6 158.1,411.9 158.6,411.9 159.1,422.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="160.8,419.2 161.3,411.9 161.8,404.6 162.4,401.0 162.9,399.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="164.5,386.5 165.1,385.6 165.6,382.0 166.2,381.1 166.7,386.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="168.3,370.2 168.8,364.7 169.4,370.2 169.9,368.4 170.5,355.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="172.1,357.5 172.6,362.0 173.2,367.5 173.7,370.2 174.2,363.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="175.9,361.1 176.4,350.2 176.9,343.9 177.5,339.3 178.0,333.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="179.6,327.5 180.2,333.9 180.7,335.7 181.2,323.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="183.4,322.1 183.9,314.8 184.5,322.1 185.0,317.6 185.5,317.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="187.2,325.7 187.7,329.4 188.2,324.8 188.8,322.1 189.3,318.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="190.9,309.4 191.5,311.2 192.0,314.8 192.6,304.0 193.1,297.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="194.7,304.0 195.2,309.4 195.8,316.7 196.3,323.0 196.9,314.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="198.5,319.4 199.0,310.3 199.6,318.5 200.1,323.0 200.6,328.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="202.3,321.2 202.8,330.3 203.3,331.2 203.9,331.2 204.4,332.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="206.6,322.1 207.1,313.9 207.6,315.8 208.2,312.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="209.8,304.9 210.3,310.3 210.9,305.8 211.4,304.9 212.0,294.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="213.6,269.5 214.1,264.1 214.6,278.6 215.2,283.1 215.7,285.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="217.9,280.4 218.4,294.0 219.0,300.3 219.5,296.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="221.1,290.4 221.7,290.4 222.2,299.4 222.7,310.3 223.3,319.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="225.4,324.8 226.0,314.8 226.5,307.6 227.0,300.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="228.7,309.4 229.2,312.1 229.7,316.7 230.3,312.1 230.8,314.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="232.4,312.1 233.0,307.6 233.5,304.9 234.0,316.7 234.6,329.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="236.2,325.7 236.7,325.7 237.3,328.5 237.8,337.5 238.4,338.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="240.0,344.8 240.5,331.2 241.0,333.0 241.6,337.5 242.1,323.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="243.7,329.4 244.3,326.6 244.8,328.5 245.4,320.3 245.9,323.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="247.5,327.5 248.1,324.8 248.6,318.5 249.1,319.4 249.7,310.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="251.3,305.8 251.8,304.0 252.4,298.5 252.9,305.8 253.4,304.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="255.1,297.6 255.6,298.5 256.1,294.9 256.7,284.9 257.2,290.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="259.4,278.6 259.9,284.0 260.4,282.2 261.0,278.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="262.6,274.9 263.1,270.4 263.7,271.3 264.2,267.7 264.8,267.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="266.4,264.1 266.9,256.8 267.5,262.2 268.0,245.0 268.5,245.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="270.1,228.7 270.7,220.5 271.2,243.2 271.8,239.6 272.3,233.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="273.9,247.7 274.5,252.3 275.0,239.6 275.5,233.2 276.1,227.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="278.2,224.1 278.8,226.0 279.3,220.5 279.8,217.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="281.5,216.0 282.0,216.9 282.5,205.1 283.1,196.0 283.6,198.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="285.2,195.1 285.8,208.7 286.3,214.2 286.9,221.4 287.4,216.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="289.0,208.7 289.5,211.4 290.1,208.7 290.6,205.1 291.2,202.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="292.8,197.8 293.3,205.1 293.9,206.9 294.4,234.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="296.5,228.7 297.1,235.9 297.6,247.7 298.2,238.7 298.7,234.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="300.3,233.2 300.9,239.6 301.4,244.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="302.5" cy="246.8" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="304.1,245.9 304.6,240.5 305.2,246.8 305.7,260.4 306.2,262.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="307.9,254.1 308.4,262.2 308.9,270.4 309.5,265.0 310.0,256.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="311.6,253.2 312.2,262.2 312.7,264.1 313.3,268.6 313.8,265.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="315.4,256.8 315.9,245.9 316.5,246.8 317.0,247.7 317.6,240.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="319.7,232.3 320.3,228.7 320.8,233.2 321.3,228.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="323.5,236.8 324.0,245.9 324.6,244.1 325.1,258.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="326.7,260.4 327.3,253.2 327.8,259.5 328.3,269.5 328.9,264.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="331.0,260.4 331.6,274.9 332.1,273.1 332.7,265.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="334.3,261.3 334.8,266.8 335.3,266.8 335.9,264.1 336.4,261.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="338.0,258.6 338.6,261.3 339.1,273.1 339.7,272.2 340.2,260.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="341.8,251.4 342.4,247.7 342.9,251.4 343.4,247.7 344.0,241.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="345.6,243.2 346.1,238.7 346.7,235.0 347.2,230.5 347.7,234.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="349.9,222.3 350.4,224.1 351.0,228.7 351.5,222.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="353.1,225.0 353.7,225.0 354.2,216.9 354.7,210.5 355.3,220.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="356.9,219.6 357.4,220.5 358.0,219.6 358.5,224.1 359.1,245.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="360.7,258.6 361.2,250.4 361.7,262.2 362.3,257.7 362.8,273.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="364.4,265.9 365.0,255.0 365.5,265.0 366.1,274.0 366.6,274.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="368.2,260.4 368.8,258.6 369.3,256.8 369.8,258.6 370.4,265.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="372.0,269.5 372.5,276.7 373.1,281.3 373.6,281.3 374.1,273.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="375.8,271.3 376.3,269.5 376.8,271.3 377.4,267.7 377.9,261.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="379.5,254.1 380.1,255.9 380.6,254.1 381.1,259.5 381.7,256.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="383.3,261.3 383.8,272.2 384.4,269.5 384.9,260.4 385.5,268.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="387.1,255.0 387.6,268.6 388.2,274.0 388.7,274.9 389.2,268.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="390.8,261.3 391.4,260.4 391.9,269.5 392.5,273.1 393.0,266.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="394.6,263.1 395.2,259.5 395.7,256.8 396.2,249.5 396.8,245.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="398.4,243.2 398.9,245.0 399.5,242.3 400.0,233.2 400.5,235.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="402.7,245.9 403.2,250.4 403.8,253.2 404.3,245.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="405.9,245.9 406.5,245.0 407.0,236.8 407.6,242.3 408.1,240.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="409.7,242.3 410.2,232.3 410.8,233.2 411.3,243.2 411.9,238.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="414.0,241.4 414.6,243.2 415.1,235.9 415.6,241.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="417.2,243.2 417.8,238.7 418.3,244.1 418.9,231.4 419.4,235.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="421.0" cy="230.5" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="422.1,222.3 422.6,213.3 423.2,212.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="424.8,216.9 425.3,218.7 425.9,230.5 426.4,239.6 426.9,233.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="428.6,235.0 429.1,235.9 429.6,240.5 430.2,231.4 430.7,232.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="432.3,230.5 432.9,226.0 433.4,230.5 434.0,216.9 434.5,221.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="436.1,220.5 436.6,213.3 437.2,210.5 437.7,199.6 438.3,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="439.9,209.6 440.4,216.0 441.0,217.8 441.5,209.6 442.0,203.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="443.7,200.6 444.2,198.7 444.7,192.4 445.3,190.6 445.8,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="447.4,186.9 448.0,186.9 448.5,200.6 449.0,196.9 449.6,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="451.2,199.6 451.7,206.9 452.3,206.9 452.8,209.6 453.4,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="455.5,193.3 456.0,190.6 456.6,193.3 457.1,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="458.7,191.5 459.3,193.3 459.8,195.1 460.4,191.5 460.9,187.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="462.5,188.8 463.1,184.2 463.6,186.0 464.1,173.3 464.7,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="466.3,167.9 466.8,167.0 467.4,162.5 467.9,164.3 468.4,164.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="470.1,155.2 470.6,144.3 471.1,151.6 471.7,152.5 472.2,147.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="474.4,157.9 474.9,165.2 475.4,154.3 476.0,160.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="477.6,153.4 478.1,142.5 478.7,135.2 479.2,128.9 479.8,133.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="481.4,139.8 481.9,142.5 482.4,131.6 483.0,139.8 483.5,141.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="485.1,138.0 485.7,138.0 486.2,147.9 486.8,157.0 487.3,166.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="488.9,157.0 489.5,165.2 490.0,173.3 490.5,161.5 491.1,162.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="492.7,160.6 493.2,177.9 493.8,169.7 494.3,177.0 494.8,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="496.5,179.7 497.0,180.6 497.5,179.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="498.6" cy="175.2" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="500.2,182.4 500.8,186.9 501.3,193.3 501.8,184.2 502.4,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="504.0,192.4 504.5,201.5 505.1,206.9 505.6,205.1 506.2,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="507.8,196.9 508.3,199.6 508.9,214.2 509.4,225.0 509.9,226.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="511.5,222.3 512.1,224.1 512.6,230.5 513.2,227.8 513.7,226.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="515.9,227.8 516.4,236.8 516.9,232.3 517.5,228.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="519.6,222.3 520.2,226.0 520.7,218.7 521.2,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="522.9,216.9 523.4,216.0 523.9,214.2 524.5,219.6 525.0,221.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="527.2,211.4 527.7,208.7 528.2,205.1 528.8,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="530.4,207.8 530.9,205.1 531.5,201.5 532.0,205.1 532.6,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="534.2,210.5 534.7,212.3 535.3,218.7 535.8,229.6 536.3,215.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="537.9,202.4 538.5,209.6 539.0,209.6 539.6,204.2 540.1,202.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="541.7,202.4 542.3,189.7 542.8,193.3 543.3,196.0 543.9,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="546.0,193.3 546.6,188.8 547.1,187.9 547.6,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="549.3,192.4 549.8,189.7 550.3,193.3 550.9,195.1 551.4,200.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="553.0,197.8 553.6,206.0 554.1,207.8 554.7,209.6 555.2,209.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="556.8,208.7 557.3,203.3 557.9,200.6 558.4,191.5 559.0,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="560.6,186.9 561.1,190.6 561.7,193.3 562.2,193.3 562.7,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="564.4,195.1 564.9,196.0 565.4,199.6 566.0,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="568.1,187.9 568.7,185.1 569.2,185.1 569.7,189.7 570.3,182.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="571.9,179.7 572.4,185.1 573.0,167.9 573.5,167.0 574.1,172.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="575.7,160.6 576.2,157.0 576.7,164.3 577.3,159.7 577.8,161.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="579.4,161.5 580.0,162.5 580.5,158.8 581.1,154.3 581.6,157.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="583.2,160.6 583.8,155.2 584.3,160.6 584.8,165.2 585.4,172.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="587.0,173.3 587.5,175.2 588.1,174.2 588.6,177.0 589.1,172.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="590.8,174.2 591.3,177.0 591.8,185.1 592.4,183.3 592.9,179.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="594.5,177.9 595.1,180.6 595.6,178.8 596.1,175.2 596.7,176.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="598.8,168.8 599.4,162.5 599.9,167.9 600.5,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="602.1,180.6 602.6,187.9 603.1,191.5 603.7,192.4 604.2,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="605.8,175.2 606.4,182.4 606.9,189.7 607.5,196.0 608.0,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="609.6,192.4 610.2,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="611.2,195.1 611.8,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="613.4,195.1 613.9,196.9 614.5,188.8 615.0,191.5 615.5,185.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="617.2,174.2 617.7,178.8 618.2,185.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="619.3" cy="192.4" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="620.9,192.4 621.5,190.6 622.0,192.4 622.5,199.6 623.1,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="624.7,196.9 625.2,202.4 625.8,203.3 626.3,199.6 626.9,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="628.5,194.2 629.0,195.1 629.6,192.4 630.1,193.3 630.6,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="632.2,202.4 632.8,204.2 633.3,209.6 633.9,218.7 634.4,235.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="636.0,237.7 636.6,226.9 637.1,221.4 637.6,218.7 638.2,223.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="639.8,226.9 640.3,231.4 640.9,233.2 641.4,225.0 641.9,227.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="643.6,230.5 644.1,234.1 644.6,236.8 645.2,230.5 645.7,235.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="647.3,234.1 647.9,233.2 648.4,232.3 648.9,229.6 649.5,226.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="651.6,232.3 652.2,238.7 652.7,242.3 653.3,243.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="654.9,245.0 655.4,249.5 656.0,249.5 656.5,246.8 657.0,248.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="658.6,251.4 659.2,249.5 659.7,245.0 660.3,242.3 660.8,242.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="662.4,240.5 663.0,241.4 663.5,236.8 664.0,236.8 664.6,240.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="666.2,235.0 666.7,241.4 667.3,236.8 667.8,231.4 668.3,219.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="670.0,215.1 670.5,214.2 671.0,212.3 671.6,209.6 672.1,210.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="674.3,215.1 674.8,216.0 675.4,209.6 675.9,210.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="677.5,200.6 678.0,199.6 678.6,196.0 679.1,198.7 679.7,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="681.3,192.4 681.8,192.4 682.4,191.5 682.9,192.4 683.4,184.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="685.1,189.7 685.6,194.2 686.1,179.7 686.7,189.7 687.2,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="689.4,178.8 689.9,177.9 690.4,178.8 691.0,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="692.6,179.7 693.1,182.4 693.7,180.6 694.2,178.8 694.8,180.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="696.4,193.3 696.9,190.6 697.4,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="698.5" cy="201.5" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="700.1,200.6 700.7,196.9 701.2,200.6 701.8,202.4 702.3,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="703.9,199.6 704.4,197.8 705.0,194.2 705.5,188.8 706.1,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="707.7,182.4 708.2,181.5 708.8,172.4 709.3,166.1 709.8,170.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="711.5,164.3 712.0,164.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="713.1,165.2 713.6,161.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="715.2,167.9 715.8,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="716.8,166.1 717.4,163.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="719.0,161.5 719.5,157.0 720.1,157.0 720.6,156.1 721.2,147.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="722.8,146.1 723.3,147.0 723.8,157.9 724.4,162.5 724.9,162.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="727.1,166.1 727.6,163.4 728.2,158.8 728.7,160.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="730.3,169.7 730.9,167.9 731.4,167.9 731.9,170.6 732.5,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="734.1,168.8 734.6,170.6 735.2,178.8 735.7,177.0 736.2,173.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="737.9,171.5 738.4,168.8 738.9,161.5 739.5,170.6 740.0,175.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="742.2,167.9 742.7,169.7 743.2,172.4 743.8,179.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="745.4,181.5 745.9,190.6 746.5,195.1 747.0,191.5 747.6,196.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="749.2,203.3 749.7,197.8 750.3,192.4 750.8,191.5 751.3,188.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="752.9,197.8 753.5,192.4 754.0,188.8 754.6,193.3 755.1,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="756.7,189.7 757.3,191.5 757.8,195.1 758.3,196.0 758.9,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="760.5,186.9 761.0,189.7 761.6,186.0 762.1,183.3 762.6,193.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="764.3,196.9 764.8,202.4 765.3,199.6 765.9,212.3 766.4,216.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="768.0,204.2 768.6,194.2 769.1,186.9 769.6,181.5 770.2,174.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="771.8,183.3 772.3,186.0 772.9,191.5 773.4,186.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="775.6,179.7 776.1,180.6 776.7,181.5 777.2,188.8 777.7,191.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="779.3,196.9 779.9,200.6 780.4,202.4 781.0,195.1 781.5,187.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="783.1,185.1 783.7,190.6 784.2,194.2 784.7,184.2 785.3,184.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="786.9,177.0 787.4,173.3 788.0,169.7 788.5,177.0 789.0,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="790.7,176.1 791.2,174.2 791.7,165.2 792.3,168.8 792.8,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="795.0,178.8 795.5,175.2 796.1,178.8 796.6,180.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="798.2,176.1 798.7,176.1 799.3,184.2 799.8,181.5 800.4,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="802.0,173.3 802.5,175.2 803.1,180.6 803.6,185.1 804.1,180.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="805.8,176.1 806.3,182.4 806.8,183.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="807.9" cy="183.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="809.5,186.9 810.1,190.6 810.6,191.5 811.1,194.2 811.7,191.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="813.3,196.0 813.8,194.2 814.4,190.6 814.9,186.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="817.1,181.5 817.6,179.7 818.1,186.9 818.7,186.0 819.2,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="820.8,178.8 821.4,172.4 821.9,176.1 822.5,175.2 823.0,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="824.6,183.3 825.1,186.0 825.7,181.5 826.2,178.8 826.8,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="828.4,179.7 828.9,186.9 829.5,183.3 830.0,184.2 830.5,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="832.2,197.8 832.7,197.8 833.2,197.8 833.8,196.9 834.3,193.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="835.9,193.3 836.5,191.5 837.0,196.0 837.5,191.5 838.1,187.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="839.7,186.9 840.2,190.6 840.8,191.5 841.3,187.9 841.9,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="843.5,192.4 844.0,194.2 844.5,196.0 845.1,197.8 845.6,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="847.8,192.4 848.3,197.8 848.9,202.4 849.4,208.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="851.0,213.3 851.6,210.5 852.1,214.2 852.6,216.9 853.2,212.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="854.8,213.3 855.3,214.2 855.9,212.3 856.4,207.8 856.9,205.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="858.6,204.2 859.1,206.9 859.6,203.3 860.2,201.5 860.7,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="862.3,204.2 862.9,203.3 863.4,206.9 863.9,208.7 864.5,206.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="866.1,201.5 866.6,205.1 867.2,206.0 867.7,205.1 868.3,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="870.4,215.1 871.0,213.3 871.5,218.7 872.0,216.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="873.6,217.8 874.2,219.6 874.7,220.5 875.3,216.9 875.8,216.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="877.4,216.9 878.0,218.7 878.5,210.5 879.0,207.8 879.6,207.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="881.2,206.0 881.7,208.7 882.3,202.4 882.8,207.8 883.3,207.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="885.0" cy="206.0" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="886.0,210.5 886.6,207.8 887.1,205.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="888.7,206.0 889.3,206.9 889.8,206.0 890.3,208.7 890.9,212.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="892.5,214.2 893.0,216.9 893.6,217.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="894.7" cy="216.0" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="896.3,209.6 896.8,209.6 897.4,212.3 897.9,207.8 898.4,205.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="900.0,202.4 900.6,201.5 901.1,206.0 901.7,205.1 902.2,200.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="903.8,201.5 904.4,204.2 904.9,203.3 905.4,206.9 906.0,203.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="907.6,202.4 908.1,201.5 908.7,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="909.7" cy="205.1" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="911.4,206.9 911.9,205.1 912.4,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="913.5" cy="200.6" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="915.1,202.4 915.7,201.5 916.2,204.2 916.8,200.6 917.3,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="918.9,200.6 919.4,201.5 920.0,204.2 920.5,202.4 921.1,196.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="923.2,190.6 923.8,194.2 924.3,194.2 924.8,196.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="926.5,197.8 927.0,196.0 927.5,194.2 928.1,196.0 928.6,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="930.2,191.5 930.8,192.4 931.3,191.5 931.8,198.7 932.4,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="934.0,197.8 934.5,203.3 935.1,201.5 935.6,209.6 936.1,214.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="938.3,213.3 938.8,209.6 939.4,210.5 939.9,210.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="941.5,215.1 942.1,214.2 942.6,213.3 943.2,216.0 943.7,220.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="945.3,213.3 945.8,212.3 946.4,209.6 946.9,206.0 947.5,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="949.1,206.9 949.6,204.2 950.2,198.7 950.7,193.3 951.2,192.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="952.9,196.9 953.4,199.6 953.9,194.2 954.5,195.1 955.0,182.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="956.6,186.9 957.2,182.4 957.7,187.9 958.2,179.7 958.8,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="960.4,186.0 960.9,190.6 961.5,187.9 962.0,189.7 962.6,186.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="964.2,186.9 964.7,187.9 965.2,191.5 965.8,191.5 966.3,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="967.9,190.6 968.5,194.2 969.0,191.5 969.6,188.8 970.1,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="971.7,194.2 972.3,190.6 972.8,190.6 973.3,186.9 973.9,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="975.5,186.0 976.0,185.1 976.6,179.7 977.1,181.5 977.6,182.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="979.3,177.0 979.8,178.8 980.3,185.1 980.9,180.6 981.4,183.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="983.0,179.7 983.6,176.1 984.1,176.1 984.6,175.2 985.2,164.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="986.8,162.5 987.3,157.0 987.9,166.1 988.4,166.1 989.0,167.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="991.1,172.4 991.7,174.2 992.2,177.0 992.7,177.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="994.3,175.2 994.9,176.1 995.4,173.3 996.0,175.2 996.5,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="998.1,167.0 998.7,169.7 999.2,167.9 999.7,177.0 1000.3,174.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1001.9,175.2 1002.4,178.8 1003.0,173.3 1003.5,176.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1005.7,171.5 1006.2,172.4 1006.7,180.6 1007.3,181.5 1007.8,183.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1009.4,183.3 1010.0,177.9 1010.5,174.2 1011.0,173.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1013.2,174.2 1013.7,167.9 1014.3,167.0 1014.8,168.8 1015.4,167.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1017.0,161.5 1017.5,165.2 1018.1,167.9 1018.6,166.1 1019.1,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1020.7,163.4 1021.3,160.6 1021.8,157.0 1022.4,153.4 1022.9,155.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1024.5,158.8 1025.1,162.5 1025.6,157.0 1026.1,156.1 1026.7,149.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1028.3,154.3 1028.8,160.6 1029.4,160.6 1029.9,155.2 1030.4,158.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1032.1,152.5 1032.6,154.3 1033.1,156.1 1033.7,160.6 1034.2,156.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1035.8,152.5 1036.4,153.4 1036.9,158.8 1037.5,155.2 1038.0,150.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1039.6,154.3 1040.1,159.7 1040.7,157.9 1041.2,157.0 1041.8,151.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1043.4,149.8 1043.9,146.1 1044.5,146.1 1045.0,147.9 1045.5,147.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1047.7,145.2 1048.2,142.5 1048.8,131.6 1049.3,130.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1050.9,129.8 1051.5,127.1 1052.0,126.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="60.0,406.5 60.5,408.3 61.1,404.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="63.2,400.1 63.8,403.7 64.3,408.3 64.8,404.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="66.5,407.4 67.0,412.8 67.5,411.0 68.1,410.1 68.6,407.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="70.2,412.8 70.8,411.9 71.3,413.7 71.9,406.5 72.4,400.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="74.0,400.1 74.5,392.9 75.1,391.0 75.6,391.9 76.2,395.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="77.8,394.7 78.3,390.1 78.9,391.9 79.4,387.4 79.9,384.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="82.1,390.1 82.6,394.7 83.2,397.4 83.7,394.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="85.3,398.3 85.9,391.0 86.4,388.3 86.9,387.4 87.5,391.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="89.1,391.0 89.6,394.7 90.2,403.7 90.7,402.8 91.3,405.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="92.9,401.0 93.4,402.8 93.9,399.2 94.5,402.8 95.0,411.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="96.6,409.2 97.2,414.6 97.7,406.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="98.8" cy="403.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="100.4,398.3 101.0,397.4 101.5,399.2 102.0,401.9 102.6,407.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="104.2,401.0 104.7,397.4 105.3,402.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="106.3" cy="414.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="108.0,411.0 108.5,419.2 109.0,420.1 109.6,421.0 110.1,427.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="111.7,421.9 112.3,417.3 112.8,411.0 113.3,411.0 113.9,410.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="115.5,416.4 116.0,415.5 116.6,411.9 117.1,411.0 117.7,415.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="119.3,412.8 119.8,409.2 120.3,411.9 120.9,407.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="123.0,410.1 123.6,408.3 124.1,402.8 124.7,405.6 125.2,408.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="126.8,398.3 127.4,392.9 127.9,391.0 128.4,391.0 129.0,389.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="130.6,389.2 131.1,391.9 131.7,391.9 132.2,394.7 132.7,388.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="134.9,382.9 135.4,386.5 136.0,386.5 136.5,392.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="138.1,390.1 138.7,388.3 139.2,384.7 139.7,391.0 140.3,392.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="141.9,389.2 142.4,388.3 143.0,389.2 143.5,386.5 144.1,378.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="145.7,379.3 146.2,376.5 146.8,376.5 147.3,372.0 147.8,377.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="149.4,372.9 150.0,365.6 150.5,368.4 151.1,371.1 151.6,377.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="153.8,377.4 154.3,372.9 154.8,373.8 155.4,372.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="157.0,383.8 157.5,389.2 158.1,377.4 158.6,377.4 159.1,384.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="160.8,382.0 161.3,377.4 161.8,372.9 162.4,364.7 162.9,366.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="164.5,356.6 165.1,354.8 165.6,357.5 166.2,353.9 166.7,361.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="168.3,349.3 168.8,344.8 169.4,352.0 169.9,352.9 170.5,344.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="172.1,347.5 172.6,351.1 173.2,355.7 173.7,359.3 174.2,359.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="175.9,355.7 176.4,347.5 176.9,342.1 177.5,336.6 178.0,330.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="179.6,323.0 180.2,324.8 180.7,325.7 181.2,315.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="183.4,313.0 183.9,307.6 184.5,317.6 185.0,313.9 185.5,313.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="187.2,319.4 187.7,321.2 188.2,316.7 188.8,315.8 189.3,312.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="190.9,302.1 191.5,305.8 192.0,307.6 192.6,294.9 193.1,287.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="194.7,291.3 195.2,297.6 195.8,304.0 196.3,308.5 196.9,299.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="198.5,300.3 199.0,293.1 199.6,302.1 200.1,304.0 200.6,309.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="202.3,301.2 202.8,310.3 203.3,311.2 203.9,309.4 204.4,311.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="206.6,302.1 207.1,300.3 207.6,300.3 208.2,298.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="209.8,291.3 210.3,296.7 210.9,292.2 211.4,292.2 212.0,290.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="213.6,270.4 214.1,267.7 214.6,273.1 215.2,276.7 215.7,281.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="217.9,273.1 218.4,285.8 219.0,289.4 219.5,284.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="221.1,280.4 221.7,281.3 222.2,288.5 222.7,295.8 223.3,298.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="225.4,304.0 226.0,295.8 226.5,290.4 227.0,284.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="228.7,292.2 229.2,296.7 229.7,301.2 230.3,298.5 230.8,299.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="232.4,295.8 233.0,293.1 233.5,293.1 234.0,301.2 234.6,308.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="236.2,304.9 236.7,305.8 237.3,305.8 237.8,306.7 238.4,308.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="240.0,315.8 240.5,308.5 241.0,312.1 241.6,311.2 242.1,303.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="243.7,308.5 244.3,307.6 244.8,304.9 245.4,294.9 245.9,297.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="247.5,299.4 248.1,298.5 248.6,294.9 249.1,295.8 249.7,288.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="251.3,286.7 251.8,284.9 252.4,279.5 252.9,285.8 253.4,289.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="255.1,285.8 255.6,287.6 256.1,284.0 256.7,274.9 257.2,276.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="259.4,264.1 259.9,270.4 260.4,267.7 261.0,265.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="262.6,260.4 263.1,262.2 263.7,265.9 264.2,265.0 264.8,261.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="266.4,261.3 266.9,255.0 267.5,263.1 268.0,249.5 268.5,253.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="270.1,243.2 270.7,229.6 271.2,245.0 271.8,244.1 272.3,236.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="273.9,242.3 274.5,245.0 275.0,237.7 275.5,235.0 276.1,230.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="278.2,225.0 278.8,226.9 279.3,220.5 279.8,218.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="281.5,214.2 282.0,214.2 282.5,204.2 283.1,196.0 283.6,187.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="285.2,181.5 285.8,194.2 286.3,200.6 286.9,206.9 287.4,204.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="289.0,197.8 289.5,205.1 290.1,204.2 290.6,201.5 291.2,193.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="292.8,186.9 293.3,192.4 293.9,189.7 294.4,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="296.5,211.4 297.1,219.6 297.6,231.4 298.2,227.8 298.7,225.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="300.3,226.0 300.9,233.2 301.4,241.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="302.5" cy="241.4" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="304.1,241.4 304.6,235.0 305.2,235.9 305.7,250.4 306.2,257.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="307.9,252.3 308.4,261.3 308.9,270.4 309.5,268.6 310.0,257.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="311.6,256.8 312.2,260.4 312.7,261.3 313.3,265.0 313.8,260.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="315.4,252.3 315.9,241.4 316.5,241.4 317.0,242.3 317.6,234.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="319.7,224.1 320.3,219.6 320.8,225.0 321.3,220.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="323.5,228.7 324.0,235.0 324.6,237.7 325.1,247.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="326.7,248.6 327.3,241.4 327.8,247.7 328.3,257.7 328.9,253.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="331.0,250.4 331.6,259.5 332.1,256.8 332.7,248.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="334.3,245.9 334.8,252.3 335.3,252.3 335.9,252.3 336.4,250.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="338.0,248.6 338.6,249.5 339.1,258.6 339.7,258.6 340.2,251.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="341.8,247.7 342.4,243.2 342.9,245.0 343.4,240.5 344.0,233.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="345.6,236.8 346.1,235.0 346.7,231.4 347.2,225.0 347.7,228.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="349.9,219.6 350.4,223.2 351.0,228.7 351.5,224.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="353.1,224.1 353.7,224.1 354.2,220.5 354.7,215.1 355.3,226.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="356.9,225.0 357.4,228.7 358.0,228.7 358.5,228.7 359.1,245.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="360.7,245.0 361.2,238.7 361.7,245.0 362.3,244.1 362.8,254.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="364.4,249.5 365.0,242.3 365.5,246.8 366.1,248.6 366.6,250.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="368.2,238.7 368.8,238.7 369.3,237.7 369.8,241.4 370.4,247.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="372.0,250.4 372.5,254.1 373.1,257.7 373.6,259.5 374.1,253.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="375.8,252.3 376.3,252.3 376.8,250.4 377.4,245.9 377.9,241.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="379.5,235.0 380.1,236.8 380.6,236.8 381.1,240.5 381.7,237.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="383.3,242.3 383.8,249.5 384.4,245.0 384.9,239.6 385.5,247.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="387.1,232.3 387.6,243.2 388.2,245.0 388.7,242.3 389.2,239.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="390.8,232.3 391.4,231.4 391.9,235.9 392.5,242.3 393.0,237.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="394.6,232.3 395.2,229.6 395.7,228.7 396.2,226.0 396.8,222.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="398.4,220.5 398.9,221.4 399.5,220.5 400.0,216.9 400.5,221.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="402.7,226.9 403.2,231.4 403.8,232.3 404.3,228.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="405.9,227.8 406.5,229.6 407.0,222.3 407.6,227.8 408.1,227.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="409.7,229.6 410.2,223.2 410.8,226.9 411.3,231.4 411.9,230.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="414.0,233.2 414.6,235.0 415.1,228.7 415.6,234.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="417.2,233.2 417.8,232.3 418.3,235.0 418.9,225.0 419.4,231.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="421.0" cy="229.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="422.1,222.3 422.6,216.9 423.2,213.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="424.8,213.3 425.3,215.1 425.9,221.4 426.4,226.9 426.9,224.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="428.6,223.2 429.1,226.0 429.6,232.3 430.2,226.0 430.7,226.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="432.3,225.0 432.9,222.3 433.4,223.2 434.0,212.3 434.5,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="436.1,216.0 436.6,207.8 437.2,202.4 437.7,188.8 438.3,198.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="439.9,193.3 440.4,199.6 441.0,201.5 441.5,196.0 442.0,193.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="443.7,191.5 444.2,188.8 444.7,183.3 445.3,180.6 445.8,183.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="447.4,177.0 448.0,179.7 448.5,193.3 449.0,190.6 449.6,190.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="451.2,191.5 451.7,196.9 452.3,196.9 452.8,199.6 453.4,191.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="455.5,183.3 456.0,184.2 456.6,185.1 457.1,187.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="458.7,184.2 459.3,186.0 459.8,186.9 460.4,182.4 460.9,179.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="462.5,181.5 463.1,178.8 463.6,181.5 464.1,167.0 464.7,169.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="466.3,157.0 466.8,154.3 467.4,151.6 467.9,153.4 468.4,151.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="470.1,144.3 470.6,131.6 471.1,138.9 471.7,137.1 472.2,131.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="474.4,140.7 474.9,151.6 475.4,139.8 476.0,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="477.6,138.9 478.1,132.5 478.7,127.1 479.2,117.1 479.8,118.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="481.4,126.2 481.9,130.7 482.4,118.9 483.0,126.2 483.5,124.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="485.1,123.5 485.7,123.5 486.2,130.7 486.8,143.4 487.3,147.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="488.9,141.6 489.5,149.8 490.0,159.7 490.5,147.9 491.1,151.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="492.7,149.8 493.2,162.5 493.8,156.1 494.3,160.6 494.8,164.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="496.5,166.1 497.0,166.1 497.5,167.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="498.6" cy="163.4" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="500.2,169.7 500.8,170.6 501.3,177.9 501.8,168.8 502.4,181.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="504.0,178.8 504.5,190.6 505.1,197.8 505.6,195.1 506.2,189.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="507.8,188.8 508.3,190.6 508.9,200.6 509.4,215.1 509.9,217.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="511.5,213.3 512.1,215.1 512.6,219.6 513.2,215.1 513.7,213.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="515.9,214.2 516.4,222.3 516.9,219.6 517.5,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="519.6,210.5 520.2,213.3 520.7,206.0 521.2,198.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="522.9,202.4 523.4,201.5 523.9,199.6 524.5,201.5 525.0,199.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="527.2,190.6 527.7,189.7 528.2,184.2 528.8,185.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="530.4,188.8 530.9,183.3 531.5,180.6 532.0,183.3 532.6,183.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="534.2,189.7 534.7,192.4 535.3,197.8 535.8,208.7 536.3,197.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="537.9,186.0 538.5,191.5 539.0,189.7 539.6,185.1 540.1,184.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="541.7,184.2 542.3,176.1 542.8,177.0 543.3,179.7 543.9,177.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="546.0,177.9 546.6,173.3 547.1,175.2 547.6,184.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="549.3,181.5 549.8,177.9 550.3,181.5 550.9,183.3 551.4,187.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="553.0,185.1 553.6,193.3 554.1,196.0 554.7,195.1 555.2,194.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="556.8,194.2 557.3,189.7 557.9,186.0 558.4,177.9 559.0,178.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="560.6,176.1 561.1,177.9 561.7,177.0 562.2,177.9 562.7,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="564.4,179.7 564.9,181.5 565.4,185.1 566.0,186.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="568.1,175.2 568.7,171.5 569.2,171.5 569.7,175.2 570.3,168.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="571.9,167.9 572.4,172.4 573.0,159.7 573.5,158.8 574.1,162.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="575.7,150.7 576.2,147.9 576.7,153.4 577.3,150.7 577.8,152.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="579.4,152.5 580.0,151.6 580.5,147.0 581.1,143.4 581.6,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="583.2,149.8 583.8,146.1 584.3,150.7 584.8,152.5 585.4,157.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="587.0,159.7 587.5,162.5 588.1,159.7 588.6,163.4 589.1,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="590.8,160.6 591.3,164.3 591.8,170.6 592.4,170.6 592.9,167.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="594.5,165.2 595.1,167.9 595.6,167.9 596.1,165.2 596.7,166.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="598.8,157.9 599.4,150.7 599.9,155.2 600.5,158.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="602.1,167.9 602.6,174.2 603.1,177.9 603.7,178.8 604.2,167.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="605.8,164.3 606.4,169.7 606.9,175.2 607.5,181.5 608.0,186.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="609.6,181.5 610.2,185.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="611.2,182.4 611.8,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="613.4,183.3 613.9,185.1 614.5,177.0 615.0,178.8 615.5,171.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="617.2,159.7 617.7,163.4 618.2,169.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="619.3" cy="175.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="620.9,176.1 621.5,173.3 622.0,175.2 622.5,180.6 623.1,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="624.7,176.1 625.2,183.3 625.8,184.2 626.3,180.6 626.9,177.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="628.5,174.2 629.0,174.2 629.6,168.8 630.1,172.4 630.6,177.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="632.2,179.7 632.8,181.5 633.3,186.0 633.9,193.3 634.4,207.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="636.0,212.3 636.6,201.5 637.1,194.2 637.6,192.4 638.2,196.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="639.8,200.6 640.3,203.3 640.9,206.9 641.4,201.5 641.9,204.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="643.6,207.8 644.1,211.4 644.6,212.3 645.2,206.0 645.7,208.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="647.3,207.8 647.9,206.0 648.4,206.0 648.9,204.2 649.5,199.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="651.6,206.0 652.2,212.3 652.7,216.0 653.3,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="654.9,217.8 655.4,220.5 656.0,221.4 656.5,217.8 657.0,219.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="658.6,223.2 659.2,221.4 659.7,215.1 660.3,212.3 660.8,211.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="662.4,209.6 663.0,209.6 663.5,205.1 664.0,206.9 664.6,208.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="666.2,205.1 666.7,210.5 667.3,205.1 667.8,201.5 668.3,194.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="670.0,190.6 670.5,188.8 671.0,186.9 671.6,183.3 672.1,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="674.3,188.8 674.8,190.6 675.4,182.4 675.9,183.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="677.5,173.3 678.0,173.3 678.6,171.5 679.1,175.2 679.7,171.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="681.3,169.7 681.8,170.6 682.4,173.3 682.9,175.2 683.4,166.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="685.1,172.4 685.6,177.9 686.1,163.4 686.7,170.6 687.2,175.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="689.4,165.2 689.9,160.6 690.4,165.2 691.0,163.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="692.6,162.5 693.1,166.1 693.7,164.3 694.2,162.5 694.8,163.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="696.4,177.0 696.9,174.2 697.4,177.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="698.5" cy="185.1" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="700.1,185.1 700.7,181.5 701.2,186.0 701.8,187.9 702.3,186.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="703.9,182.4 704.4,180.6 705.0,174.2 705.5,167.9 706.1,162.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="707.7,163.4 708.2,164.3 708.8,158.8 709.3,150.7 709.8,152.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="711.5,147.0 712.0,148.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="713.1,148.8 713.6,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="715.2,147.9 715.8,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="716.8,146.1 717.4,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="719.0,140.7 719.5,135.2 720.1,135.2 720.6,134.3 721.2,130.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="722.8,129.8 723.3,128.9 723.8,138.0 724.4,141.6 724.9,141.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="727.1,145.2 727.6,143.4 728.2,138.9 728.7,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="730.3,148.8 730.9,147.0 731.4,146.1 731.9,148.8 732.5,142.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="734.1,147.9 734.6,149.8 735.2,159.7 735.7,158.8 736.2,155.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="737.9,153.4 738.4,149.8 738.9,142.5 739.5,152.5 740.0,155.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="742.2,147.9 742.7,148.8 743.2,150.7 743.8,157.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="745.4,157.9 745.9,167.9 746.5,171.5 747.0,167.0 747.6,171.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="749.2,177.0 749.7,169.7 750.3,166.1 750.8,165.2 751.3,161.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="752.9,168.8 753.5,164.3 754.0,160.6 754.6,164.3 755.1,161.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="756.7,163.4 757.3,165.2 757.8,167.0 758.3,167.9 758.9,164.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="760.5,157.9 761.0,158.8 761.6,155.2 762.1,151.6 762.6,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="764.3,164.3 764.8,170.6 765.3,168.8 765.9,173.3 766.4,180.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="768.0,165.2 768.6,153.4 769.1,152.5 769.6,139.8 770.2,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="771.8,145.2 772.3,146.1 772.9,150.7 773.4,145.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="775.6,135.2 776.1,138.0 776.7,142.5 777.2,147.9 777.7,150.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="779.3,155.2 779.9,159.7 780.4,157.9 781.0,150.7 781.5,146.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="783.1,142.5 783.7,144.3 784.2,147.9 784.7,142.5 785.3,142.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="786.9,137.1 787.4,132.5 788.0,129.8 788.5,135.2 789.0,137.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="790.7,134.3 791.2,130.7 791.7,119.8 792.3,122.5 792.8,123.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="795.0,132.5 795.5,129.8 796.1,134.3 796.6,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="798.2,128.0 798.7,128.9 799.3,137.1 799.8,138.0 800.4,129.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="802.0,131.6 802.5,133.4 803.1,135.2 803.6,141.6 804.1,136.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="805.8,130.7 806.3,138.0 806.8,138.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="807.9" cy="137.1" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="809.5,138.9 810.1,142.5 810.6,142.5 811.1,144.3 811.7,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="813.3,147.0 813.8,147.0 814.4,143.4 814.9,139.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="817.1,134.3 817.6,132.5 818.1,138.9 818.7,139.8 819.2,130.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="820.8,129.8 821.4,126.2 821.9,126.2 822.5,126.2 823.0,127.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="824.6,132.5 825.1,136.2 825.7,131.6 826.2,130.7 826.8,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="828.4,130.7 828.9,139.8 829.5,137.1 830.0,137.1 830.5,144.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="832.2,145.2 832.7,147.0 833.2,144.3 833.8,144.3 834.3,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="835.9,141.6 836.5,138.0 837.0,142.5 837.5,138.0 838.1,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="839.7,132.5 840.2,136.2 840.8,137.1 841.3,134.3 841.9,138.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="843.5,137.1 844.0,136.2 844.5,135.2 845.1,138.0 845.6,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="847.8,129.8 848.3,136.2 848.9,139.8 849.4,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="851.0,155.2 851.6,152.5 852.1,155.2 852.6,158.8 853.2,156.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="854.8,157.9 855.3,158.8 855.9,157.9 856.4,152.5 856.9,149.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="858.6,147.9 859.1,151.6 859.6,148.8 860.2,149.8 860.7,147.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="862.3,153.4 862.9,151.6 863.4,152.5 863.9,155.2 864.5,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="866.1,148.8 866.6,151.6 867.2,152.5 867.7,152.5 868.3,160.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="870.4,161.5 871.0,159.7 871.5,165.2 872.0,163.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="873.6,165.2 874.2,167.9 874.7,168.8 875.3,165.2 875.8,164.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="877.4,166.1 878.0,167.9 878.5,162.5 879.0,158.8 879.6,157.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="881.2,155.2 881.7,157.0 882.3,150.7 882.8,155.2 883.3,154.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="885.0" cy="153.4" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="886.0,157.0 886.6,154.3 887.1,150.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="888.7,151.6 889.3,150.7 889.8,149.8 890.3,151.6 890.9,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="892.5,156.1 893.0,157.0 893.6,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="894.7" cy="157.0" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="896.3,150.7 896.8,150.7 897.4,151.6 897.9,148.8 898.4,146.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="900.0,144.3 900.6,145.2 901.1,147.0 901.7,146.1 902.2,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="903.8,141.6 904.4,143.4 904.9,142.5 905.4,145.2 906.0,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="907.6,141.6 908.1,142.5 908.7,146.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="909.7" cy="144.3" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="911.4,145.2 911.9,144.3 912.4,141.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="913.5" cy="139.8" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="915.1,140.7 915.7,139.8 916.2,143.4 916.8,140.7 917.3,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="918.9,142.5 919.4,142.5 920.0,146.1 920.5,146.1 921.1,142.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="923.2,135.2 923.8,138.9 924.3,141.6 924.8,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="926.5,145.2 927.0,142.5 927.5,140.7 928.1,140.7 928.6,138.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="930.2,136.2 930.8,136.2 931.3,135.2 931.8,140.7 932.4,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="934.0,140.7 934.5,147.0 935.1,143.4 935.6,152.5 936.1,155.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="938.3,156.1 938.8,153.4 939.4,154.3 939.9,152.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="941.5,154.3 942.1,154.3 942.6,154.3 943.2,157.0 943.7,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="945.3,154.3 945.8,154.3 946.4,152.5 946.9,150.7 947.5,147.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="949.1,152.5 949.6,147.0 950.2,139.8 950.7,138.0 951.2,136.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="952.9,139.8 953.4,140.7 953.9,138.0 954.5,142.5 955.0,130.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="956.6,135.2 957.2,132.5 957.7,137.1 958.2,133.4 958.8,128.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="960.4,135.2 960.9,138.0 961.5,135.2 962.0,138.0 962.6,135.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="964.2,137.1 964.7,136.2 965.2,137.1 965.8,136.2 966.3,135.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="967.9,136.2 968.5,138.9 969.0,137.1 969.6,133.4 970.1,138.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="971.7,138.0 972.3,137.1 972.8,136.2 973.3,134.3 973.9,135.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="975.5,132.5 976.0,132.5 976.6,128.9 977.1,128.9 977.6,129.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="979.3,125.3 979.8,128.9 980.3,132.5 980.9,129.8 981.4,131.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="983.0,128.9 983.6,124.4 984.1,124.4 984.6,125.3 985.2,116.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="986.8,114.4 987.3,110.8 987.9,117.1 988.4,118.0 989.0,120.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="991.1,124.4 991.7,126.2 992.2,128.9 992.7,128.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="994.3,128.0 994.9,129.8 995.4,128.0 996.0,129.8 996.5,126.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="998.1,124.4 998.7,126.2 999.2,124.4 999.7,131.6 1000.3,129.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1001.9,129.8 1002.4,133.4 1003.0,133.4 1003.5,136.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1005.7,131.6 1006.2,132.5 1006.7,139.8 1007.3,139.8 1007.8,138.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1009.4,139.8 1010.0,135.2 1010.5,129.8 1011.0,128.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1013.2,128.0 1013.7,122.5 1014.3,121.6 1014.8,122.5 1015.4,121.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1017.0,118.0 1017.5,119.8 1018.1,119.8 1018.6,118.9 1019.1,121.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1020.7,117.1 1021.3,115.3 1021.8,113.5 1022.4,111.7 1022.9,112.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1024.5,116.2 1025.1,118.9 1025.6,108.9 1026.1,108.0 1026.7,102.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1028.3,106.2 1028.8,110.8 1029.4,111.7 1029.9,107.1 1030.4,109.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1032.1,104.4 1032.6,105.3 1033.1,105.3 1033.7,108.0 1034.2,104.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1035.8,99.0 1036.4,101.7 1036.9,109.8 1037.5,106.2 1038.0,102.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1039.6,106.2 1040.1,111.7 1040.7,110.8 1041.2,109.8 1041.8,107.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1043.4,104.4 1043.9,102.6 1044.5,102.6 1045.0,104.4 1045.5,105.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1047.7,104.4 1048.2,101.7 1048.8,93.5 1049.3,95.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1050.9,96.2 1051.5,94.4 1052.0,95.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<text x="1058" y="99.3" font-size="11.5" font-weight="700" fill="var(--s-dgs30)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 30년물 국채금리 5.35%</text>
<text x="1058" y="130.2" font-size="11.5" font-weight="700" fill="var(--s-dgs10)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 10년물 국채금리 5.01%</text>
<text x="1058" y="154.7" font-size="11.5" font-weight="700" fill="var(--s-dgs2)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 2년물 국채금리 4.74%</text>
</svg>
</div>

### 5년간 변화 요약

| 지표 | 시작 | 현재 | 변화 | 기간 최고 | 기간 최저 |
|------|------|------|------|-----------|-----------|
| 미국 2년물 국채금리 | 0.20% (2021-09-01) | 4.74% (2026-09-16) | +4.54 | 5.19% (2023-10-17) | 0.20% (2021-09-01) |
| 미국 10년물 국채금리 | 1.31% (2021-09-01) | 5.01% (2026-09-16) | +3.70 | 5.01% (2026-09-16) | 1.28% (2021-09-14) |
| 미국 30년물 국채금리 | 1.92% (2021-09-01) | 5.35% (2026-09-16) | +3.43 | 5.37% (2026-09-10) | 1.69% (2021-12-03) |

---

## 2. 해석 참고 — 이 차트를 읽는 법

이 절은 특정 구간의 결과가 아니라 **차트와 표를 어떤 순서로 읽는지**만 정리한다.

- **먼저 볼 것**: 세 만기의 변화(%p) 방향과 크기 순서. 비슷한 폭으로 함께 움직였다면(평행 이동) 금리 수준 전체가 재조정된 것이고, 만기별로 크기가 갈렸다면 곡선의 **모양**이 바뀐 것이다.
- **곡선의 기울기 = 10년물 − 2년물**: 표의 두 "현재" 값을 빼면 장단기 스프레드(흔히 2s10s)가 나온다. 양수면 정상(장기 > 단기), 음수면 **역전(inversion)**이다. 역전은 역사적으로 침체의 선행 신호로 자주 인용되고, 역전이 풀려 다시 양수로 돌아서는 시점도 별개의 관전 포인트로 다뤄진다 — 차트에서 두 선이 교차하는 구간을 확인한다.
- **만기마다 담는 정보가 다르다**: 2년물은 앞으로 몇 차례 FOMC의 정책 경로 기대를, 10년물은 장기 성장·물가 기대를, 30년물은 거기에 기간 프리미엄(장기 발행량·재정 전망)까지 담는다. 단기물만 움직인 구간은 통화정책이, 장기물만 움직인 구간은 재정·물가 기대가 주도했다고 읽는다.
- **30년물 − 10년물 = 장기 구간의 기간 프리미엄**: 이 간격이 유지되고 있으면 장기 프리미엄이 안정적이라는 뜻이고, 벌어졌다면 시장이 먼 미래의 재정·물가 위험에 더 큰 보상을 요구하기 시작했다는 신호로 읽는다.
- **수준이 아니라 간격을 본다**: 금리 수준의 높낮이 자체보다 만기 사이의 **간격과 그 변화**가 이 차트의 정보다. 수준만 보면 정책 국면과 기간 프리미엄이 뒤섞인다.
- **차트의 회색 음영**: NBER이 사후에 판정한 미국의 침체 국면이다. 실시간 신호가 아니라 나중에 붙는 라벨이다.

---

*작성일: 2026-09-18*
