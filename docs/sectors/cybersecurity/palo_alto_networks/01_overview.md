# Palo Alto Networks

> 네트워크 방화벽(NGFW)에서 출발해 클라우드 보안·보안운영(SOC)·아이덴티티 보안까지 인수·자체개발로 확장한 사이버보안 플랫폼 기업. 2026년 2월 CyberArk($25B) 인수를 종결하며 "보안 전 영역을 하나의 플랫폼으로" 전략을 아이덴티티 보안까지 밀어붙이는 국면에 들어섰다.

> ⚠️ 시가총액은 2026-08-14 종가($384.27) × 유통주식수(815.0M, stockanalysis.com) 기준.

- **회사명**: Palo Alto Networks, Inc.
- **티커 / 상장 시장**: PANW / Nasdaq (2012-07 NYSE 상장 → 2021-10 Nasdaq 이전)
- **설립 / 본사**: 2005년 설립(Nir Zuk) / 미국 캘리포니아주 산타클라라
- **CEO**: Nikesh Arora (2018년 6월 취임)
- **홈페이지**: https://www.paloaltonetworks.com
- **섹터 / 산업**: [Cybersecurity](../00_overview.md)
- **시가총액**: $313,180M (약 $313.2B) — 2026-08-14 종가 기준
- **회계연도(FY) 마감월**: 7월 말 (FY2026 = 2025-08 ~ 2026-07). 다른 문서에서 FY를 언급할 땐 이 기준을 그대로 인용.

---

## 1. 한 줄 요약

Palo Alto Networks는 차세대 방화벽(NGFW)으로 시작해 네트워크 보안·클라우드 보안·보안운영(SOC)·(2026년부터) 아이덴티티 보안까지 인수와 자체개발을 병행하며 확장한 사이버보안 플랫폼 기업이다. "포인트 솔루션을 하나씩 사지 말고 하나의 플랫폼으로 통합하라"는 메시지로 대형 M&A(2026-02 CyberArk $25B, Chronosphere)를 밀어붙이고 있으며, 이는 업계 전반의 벤더 통합(consolidation) 흐름과 맞물려 있다([섹터 개요](../00_overview.md) 4. 구조적 리스크 / 경기 민감도 참고).

---

## 2. 사업 모델 — 어떻게 돈을 버는가

GAAP 매출은 크게 두 축으로 잡힌다(FY2025 기준):

| 사업 부문 | 설명 | 매출 비중 | 기준 시점 |
|-----------|------|-----------|-----------|
| Subscription and support (구독·지원) | 클라우드 딜리버리 보안 서비스(Threat Prevention·WildFire·URL Filtering 등), SaaS형 Prisma·Cortex 제품군, 기존 하드웨어에 대한 지원·유지보수 계약 | 80.5% ($7,419.6M) | FY2025 (2025-07-31 마감) |
| Product (제품) | NGFW 물리·가상 어플라이언스 하드웨어/소프트웨어 라이선스 판매 | 19.5% ($1,801.9M) | FY2025 |

회사는 이 GAAP 구분과 별개로, 사업 전략상 세 개 제품군으로 스스로를 나눈다(GAAP 매출 기준 세부 비중은 별도 공시하지 않고 [핵심 지표](./04_metrics.md) C절의 **Next-Gen Security ARR**로만 진행 상황을 공시):

- **네트워크 보안 (Strata / Prisma SASE)** — NGFW(물리·가상·컨테이너형)와 Prisma Access(ZTNA)+Prisma SD-WAN을 결합한 SASE. 매출의 절대적 비중은 여전히 이 영역(전통 NGFW 하드웨어+지원계약 포함)에서 나온다.
- **클라우드 보안 (Prisma Cloud)** — 멀티클라우드 환경의 애플리케이션·데이터·인프라를 개발 전 주기에 걸쳐 보호하는 CNAPP(Cloud Native Application Protection Platform).
- **보안운영 (Cortex)** — XDR·SIEM·SOAR로 위협 탐지·대응을 자동화하는 SOC 플랫폼. 자체 추정 SIEM 시장 규모는 약 $40B.
- **(2026-02 신규) 아이덴티티 보안 (CyberArk)** — 특권접근관리(PAM) 시장 1위 CyberArk 인수로 새로 추가된 사업군. Chronosphere(옵저버빌리티)도 함께 인수해 SOC/모니터링 영역을 보강했다. 두 회사의 실적은 Q3 FY2026(2026-04-30 마감)부터 연결에 반영([핵심 지표](./04_metrics.md) 참고).

매출 인식과 별개로 회사가 투자자에게 강조하는 진행 지표는 **Next-Gen Security ARR**(전통 하드웨어를 제외한 차세대 제품군의 연환산 반복매출, FY2025 $5.6B·+32% YoY)이다 — 이는 GAAP 매출보다 사업 믹스 전환(하드웨어→구독형 플랫폼)을 더 잘 보여주는 지표이지만 GAAP 매출과 인식 기준이 다르다는 점에 유의.

---

## 3. 산업 / 시장 내 위치

Palo Alto Networks는 [Cybersecurity](../00_overview.md) 섹터에서 네트워크·클라우드·SOC·(신규) 아이덴티티 보안을 아우르는 **통합 플랫폼 벤더**로 자리매김하고 있다. Gartner 기준 2026년 전 세계 정보보안 지출 약 $244B(전년比 약 12~13%) 중 이 회사가 커버하는 영역은 네트워크 보안·클라우드 보안·SOC를 합친 규모다.

- **경쟁사**: 네트워크 보안에서는 Fortinet·Check Point·Cisco, 클라우드 보안(SASE)에서는 Zscaler, 엔드포인트/XDR에서는 CrowdStrike·SentinelOne과 직접 경쟁한다. 아이덴티티 보안 신규 진입 이후에는 Okta·Microsoft Entra 등과도 경쟁 구도가 생긴다.
- **시장 내 위치**: 네트워크 보안(NGFW) 부문에서는 Gartner Magic Quadrant 리더로 다년간 자리매김해왔고([역사 / 주요 이벤트](./02_history.md) 참고), 클라우드 보안·SOC는 CrowdStrike·Zscaler 등 클라우드 네이티브 경쟁사 대비 상대적으로 후발주자에서 대형 M&A로 격차를 좁혀온 전략을 취해왔다.
- **산업 전체의 밸류체인·시장 규모·구조적 리스크(벤더 통합·가격 경쟁·규제 등)는 [섹터 개요](../00_overview.md)로 넘기고, 여기서는 이 회사가 그 구조 안에서 "통합자(consolidator)" 포지션을 취하고 있다는 점만 짚는다** — [섹터 개요](../00_overview.md) 4. 구조적 리스크 / 경기 민감도의 "벤더 통합(M&A)·플랫폼화 압력"이 이 회사에는 리스크이자 동시에 전략(CyberArk 인수)이라는 양면성이 있다.

---

## 관련 문서

- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 일봉·1년](./09_technical_daily.md)
- [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [공식 홈페이지](https://www.paloaltonetworks.com)
- [10-K FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1327567/000132756725000027/panw-20250731.htm)
- [Palo Alto Networks Announces Agreement to Acquire CyberArk](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-announces-agreement-to-acquire-cyberark--the-identity-security-leader)
- [Fiscal Third Quarter 2026 Financial Results](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-reports-fiscal-third-quarter-2026-financial-results)

---

*작성일: 2026-08-16*
