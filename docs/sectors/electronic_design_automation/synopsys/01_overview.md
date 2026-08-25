# Synopsys (시놉시스)

> 반도체 설계 자동화(EDA) 분야의 글로벌 1위 기업. 전 세계 거의 모든 반도체 회사가 칩을 설계할 때 쓰는 소프트웨어를 만들어, 특정 AI 칩 회사의 승패와 무관하게 반도체 설계 물량 확대의 수혜를 받는 "숨은 인프라" 기업이다.

!!! warning "이 회사 숫자를 볼 때 먼저 알아둘 것"
    - **시가총액 산정 근거**: 2026-08-24 종가 $394.51 × FY2026 Q2 기준 희석주식수(192.3백만 주). 희석주식수는 근사치이므로 집계 사이트 표시값과 1% 안팎의 차이가 날 수 있다([핵심 지표](./04_metrics.md) A.2 참고).
    - **Ansys는 별도 사업 부문이 아니다.** 2025년 7월 인수한 Ansys의 매출은 **Design Automation 부문 안에** 포함돼 보고된다 — 아래 표를 "EDA + IP + Ansys" 세 축으로 읽으면 비중이 100%를 넘게 된다.
    - **GAAP 손익만 보고 수익성을 판단하면 안 된다.** Ansys 인수 관련 무형자산 상각·구조조정 비용이 FY2025부터 GAAP 영업이익을 크게 눌러, GAAP 지표는 사업의 실제 수익력보다 나쁘게 보인다. 반대로 회사가 강조하는 Non-GAAP은 매년 반복되는 주식보상비용(SBC)을 되더한 값이라 좋게 보인다 — 두 기준의 차이가 왜 생기는지는 [핵심 지표](./04_metrics.md)·[재무 / 실적](./05_financials.md)에서 다룬다.

- **회사명**: Synopsys, Inc.
- **티커 / 상장 시장**: SNPS (NASDAQ)
- **설립 / 본사**: 1986년 / 미국 캘리포니아 서니베일(Sunnyvale)
- **CEO**: Sassine Ghazi (2024년 1월 취임, 전임 Aart de Geus는 Executive Chairman으로 이동 — [CEO / 경영진](./03_ceo.md) 참고)
- **홈페이지**: [synopsys.com](https://www.synopsys.com)
- **섹터 / 산업**: [반도체 설계 자동화(EDA)](../00_overview.md) — 밸류체인상 업스트림(설계·검증 소프트웨어·IP 공급)
- **시가총액**: 약 758.6억 달러 (2026-08-24 종가 $394.51 기준)
- **회계연도(FY) 마감월**: 10월 말(또는 10월 마지막 일요일) — FY2025 = 2024.11~2025.10

---

## 1. 한 줄 요약

Synopsys는 **반도체 칩을 설계·검증하는 소프트웨어(EDA, Electronic Design Automation)** 와 **칩에 그대로 얹어 쓰는 설계 자산(Semiconductor IP)** 을 만드는 회사다. 엔비디아, AMD, 인텔, 삼성, TSMC 등 전 세계 거의 모든 반도체 회사가 칩을 만들 때 Synopsys의 도구를 사용하기 때문에 "반도체 산업의 숨은 인프라"로 불린다. 2025년 7월 약 349억 달러에 시뮬레이션 소프트웨어 기업 Ansys를 인수하며, 칩 단위를 넘어 패키지·시스템 전체를 아우르는 "실리콘에서 시스템까지" 엔지니어링 솔루션 기업으로 재편 중이다.

---

## 2. 사업 모델 — 어떻게 돈을 버는가

라이선스/구독 형태로 소프트웨어 툴과 IP를 반도체 회사에 판매하며, 매출 상당 부분이 반복 매출(recurring) 성격을 띤다. 고객이 한 번 특정 EDA 툴체인에 설계 워크플로우를 맞추면 바꾸기가 매우 어려워, 계약이 해마다 갱신되는 구조다.

| 사업 부문 | 설명 | 매출 비중 | 기준 시점 |
|-----------|------|-----------|-----------|
| Design Automation (Ansys 포함) | 칩 설계·검증 소프트웨어 툴 체인 — 논리 합성(Design Compiler, Fusion Compiler), 검증(VCS, Verdi), 물리 설계·사이닝오프(IC Compiler II, PrimeTime), 에뮬레이션(ZeBu, HAPS). 2025년 인수한 Ansys의 멀티피직스 시뮬레이션(구조·유체·전자기·열) 매출도 이 부문에 포함해 보고 | **75.2%** ($5,302M) | FY2025 |
| Design IP (Semiconductor IP) | 칩 설계 시 재사용하는 검증된 설계 블록 — USB·PCIe·DDR·Ethernet 등 인터페이스 IP, 프로세서·보안·아날로그 IP | **24.8%** ($1,752M) | FY2025 |

- 위 비중은 FY2025 확정 실적(총매출 $7,054M) 기준이다. **Ansys는 FY2025에 약 3.5개월치만 반영됐다** — FY2026 가이던스에 포함된 Ansys 기여분은 약 $29억으로, 연간 가이던스 중간값 $96.65억의 약 30%에 해당한다. 즉 FY2026부터 Design Automation 부문의 구성 자체가 크게 달라진다.
- 과거 사업부였던 **소프트웨어 보안(Software Integrity)** 부문은 2024년 9월 매각되어 현재 Synopsys 소속이 아니다(→ Black Duck Software). FY2024부터 매출·이익 기저에서 빠져 있어, FY2023과 FY2024를 단순 비교하면 성장률이 실제보다 낮게 보인다.

---

## 3. 산업 / 시장 내 위치

> 산업 밸류체인·시장 규모·성장 동력·구조적 리스크는 [섹터 개요](../00_overview.md)에서 다룬다. 여기서는 그 안에서 Synopsys가 어떤 위치인지만 정리한다.

EDA 시장은 **Synopsys · Cadence · Siemens EDA** 3사(Big Three)가 과점하고 있으며, 그중 Synopsys가 매출 기준 1위다. 이 저장소에서는 같은 섹터의 [Cadence](../cadence_design_systems/01_overview.md)를 함께 커버하고 있다.

- **높은 진입장벽 + 과점 구조**: 고객(반도체 회사)의 전환비용이 매우 높아 안정적 매출 구조. 파운드리 공정 사전 인증(sign-off) 관계까지 얽혀 있어 신규 진입자가 넘기 어렵다.
- **AI 반도체 수혜의 "곡괭이" 기업**: 엔비디아·AMD 등 AI 칩 수요가 늘수록, 특정 칩 회사의 성패와 무관하게 EDA 도구 수요도 함께 증가한다.
- **Ansys 인수로 인접 영역 확장**: 칩 설계 + 시스템 시뮬레이션 결합으로 TAM(총 시장 규모) 확대를 노린다. 다만 대형 인수에 따른 통합 리스크와 부채 부담이 함께 따라왔다 — 구체적 판단은 [투자 판단](./07_investment.md) 참고.
- **중국 노출**: 2025년 5월 미 상무부의 대중국 EDA 수출규제 당시 중국 매출 비중은 회사 전체의 약 16%로 보도됐다. 규제는 6주 만에 철회됐으나 섹터 공통의 구조적 리스크로 남아 있다.

---

## 관련 문서

- **먼저 읽기** — [최종 보고서](./11_final_report.md): 아래 문서 전체를 종합한 요약이라, 처음이라면 여기부터 봐도 된다
- **회사 이해** — [역사 / 주요 이벤트](./02_history.md) · [CEO / 경영진](./03_ceo.md)
- **숫자** — [핵심 지표](./04_metrics.md) · [재무 / 실적](./05_financials.md) · [밸류에이션 / 적정주가](./06_valuation.md)
- **판단 · 로그** — [투자 판단](./07_investment.md) · [최근 뉴스 / 이슈](./08_news.md)
- **가격 차트** — [기술적 분석 — 일봉·1년](./09_technical_daily.md) · [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Synopsys 공식 홈페이지](https://www.synopsys.com)
- [Synopsys Posts Financial Results for Fourth Quarter and Fiscal Year 2025 (2025.12.10)](https://news.synopsys.com/2025-12-10-Synopsys-Posts-Financial-Results-for-Fourth-Quarter-and-Fiscal-Year-2025) — FY2025 부문별 매출(Design Automation $5,302M / Design IP $1,752M)·FY2026 가이던스
- [Synopsys Posts Financial Results for Second Quarter Fiscal Year 2026 (2026.5.27)](https://news.synopsys.com/2026-05-27-Synopsys-Posts-Financial-Results-for-Second-Quarter-Fiscal-Year-2026) — FY2026 가이던스 상향
- [Synopsys Wikipedia](https://en.wikipedia.org/wiki/Synopsys)

---

*작성일: 2026-08-01 (최종 수정일: 2026-08-25)*
