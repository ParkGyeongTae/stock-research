# Electronic Design Automation (EDA)

> 반도체 설계·검증에 쓰이는 소프트웨어 산업으로, 특정 칩 회사의 승패와 무관하게 반도체 설계 복잡도가 늘어날수록 수요가 함께 느는 "picks and shovels" 성격의 상류(upstream) 산업이다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(`04_metrics.md`·`07_investment.md`)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ 개념 정리는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: Electronic Design Automation (반도체 설계 자동화)
- **밸류체인 위치**: 업스트림 — 반도체 설계·검증에 쓰이는 소프트웨어/IP 공급. 팹리스·IDM(반도체 설계사)의 설계 단계, 파운드리 이전 단계에 위치
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [Synopsys](./synopsys/01_overview.md)
  - [Cadence Design Systems](./cadence_design_systems/01_overview.md)
- **인접 섹터**: 반도체 제조(파운드리)·반도체 장비 — 이 저장소에서는 아직 별도 섹터로 커버하지 않음. `automated_test_equipment`(반도체 테스트 장비)는 밸류체인상 다운스트림(검증·양산 단계)에 위치해 인접함

---

## 1. 한 줄 요약

EDA는 칩 설계·검증에 필수적인 소프트웨어 도구(디지털 구현, 시뮬레이션, 검증 등)와 사전 검증된 설계 IP를 반도체 설계사에 공급하는 산업이다. 반도체 자체의 수요·공급 사이클과 달리, AI·데이터센터발 반도체 설계 복잡도 증가라는 구조적 흐름의 직접 수혜를 받는 위치에 있어 최근 주목받고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

EDA는 반도체 밸류체인에서 실제 칩 제조(파운드리) 이전, 설계·검증 단계에 소프트웨어·IP를 공급하는 역할을 한다.

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| EDA 도구/IP (이 섹터) | 디지털 구현·검증·아날로그 설계 소프트웨어, 사전 검증된 설계 IP(코어 라이선스) 공급 | Synopsys·Cadence·Siemens EDA ("Big Three" 과점) | 전환비용(설계팀 교육·기존 설계 자산 재검증)·파운드리 공정 사전 인증(sign-off) 관계·R&D 규모의 경제 |
| 칩 설계 (고객) | EDA 도구로 실제 칩(로직·아날로그·SoC) 설계 | 팹리스(NVIDIA·AMD·Apple 등)·IDM(Intel·Samsung 등) | 설계 인력·아키텍처 역량 |
| 파운드리 (다운스트림) | 설계된 칩을 실제로 제조 | TSMC·Samsung Foundry·Intel Foundry | 막대한 자본 지출, 공정 미세화 기술력 |
| 패키징·테스트 (다운스트림) | 제조된 칩의 패키징·검증 | ASE·Amkor 등 OSAT, 반도체 테스트 장비사(`automated_test_equipment` 섹터 참고) | 장비 투자, 수율 관리 노하우 |

이 섹터의 커버리지 기업(Synopsys·Cadence)은 모두 EDA 도구/IP 단계에 위치하며, 최근 둘 다 칩을 넘어선 시스템 레벨 설계·해석(Synopsys의 Ansys 인수, Cadence의 System Design and Analysis 사업)으로 영역을 확장하는 공통 흐름을 보인다.

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 `07_investment.md`에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **시장 규모(TAM)**: 리서치 기관별로 $16~21B(2026년 기준)로 추정치가 갈린다 — Mordor Intelligence $17.85B(2026), Persistence Market Research $20.78B(2026), Research and Markets $18.2B(2026), Fortune Business Insights $16.37B(2026). 정의(EDA 소프트웨어만 포함하는지, 설계 IP·서비스까지 포함하는지)가 기관마다 달라 단일 값으로 단정하지 않고 범위로 남긴다.
- **성장률(CAGR)**: 기관별로 7.8%~10.2% 범위(2026년 기준 향후 4~9년 전망). 대체로 8~9%대에 수렴하는 추정이 많다.
- **핵심 성장 동력**:
  1. **AI 반도체 설계 복잡도 증가** — 칩 설계 자체의 복잡도(트랜지스터 밀도, 멀티다이/칩렛 구조, 시스템 레벨 통합)가 늘어날수록 EDA 도구 사용량이 함께 증가하는 구조. 특정 AI 칩 회사의 승패와 무관하게 AI 반도체 설계 물량 자체가 늘어나면 수혜.
  2. **시스템 레벨 설계로의 확장** — 칩 단위를 넘어 패키지·보드·시스템 전체를 아우르는 멀티피직스 시뮬레이션·해석 수요 증가(Synopsys-Ansys, Cadence의 SD&A 사업이 이 흐름을 반영).
  3. **생성형 AI 기반 설계 자동화** — EDA 벤더들이 자사 도구에 에이전틱 AI를 결합해 설계 생산성을 높이는 투자를 확대 중(예: Cadence의 ChipStack·AgentStack).

Sources: [Electronic Design Automation Tools (EDA) Market Analysis — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/electronic-design-automation-eda-tools-market) · [Electronic Design Automation Market Size & Forecast — Persistence Market Research](https://www.persistencemarketresearch.com/market-research/electronic-design-automation-eda-market.asp) · [Electronic Design Automation (EDA) Market Report 2026 — Research and Markets](https://www.researchandmarkets.com/reports/5953345/electronic-design-automation-eda-market-report) · [Electronic Design Automation Software Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/electronic-design-automation-software-market-105985)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 지정학 규제(미·중 반도체 갈등) | 미 상무부(BIS)가 EDA 소프트웨어의 대중국 수출을 규제할 수 있다 — 2025-05-23 실제로 발효됐다가 2025-07-02 철회된 전례가 있음. 재도입되면 섹터 내 모든 회사의 중국 매출·가이던스가 동시에 타격받는 공통 리스크 | BIS의 EDA 관련 수출규제 발표·철회 여부, 커버리지 기업들의 중국 매출 비중 공시 |
| 반도체 설계 사이클 둔화 | EDA는 라이선스 기반이라 반도체 제조 자체의 경기 사이클보다는 완만하지만, AI 반도체 투자 사이클이 급격히 꺾이면 신규 설계 프로젝트 감소로 이어질 수 있음 | 주요 팹리스·하이퍼스케일러의 AI 반도체 capex 가이던스, TSMC 등 파운드리의 첨단 공정 가동률 |
| 생성형 AI 기반 신흥 경쟁자 | 아직 초기 단계이지만, 생성형 AI로 설계 워크플로우 일부를 자동화하는 스타트업이 장기적으로 전통 EDA 벤더의 영역을 잠식할 가능성 | 신흥 EDA/설계 자동화 스타트업의 대형 팹리스 고객 채택 사례 |
| 고객 집중도 | 매출 상당 부분이 소수의 대형 팹리스·하이퍼스케일러(NVIDIA·AMD·Apple 등)에 집중 — 이들의 설계 투자 축소가 섹터 전체 수요에 영향 | 대형 팹리스 고객사들의 R&D/설계 투자 가이던스 |

> 개별 회사의 Bull/Bear Case는 각 회사 `07_investment.md`에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **미 상무부(BIS) 수출관리규정(EAR) 개정·발표** — EDA 소프트웨어 관련 대중국 수출통제 신설·완화 여부
- **DAC(Design Automation Conference)** — 매년 열리는 업계 최대 컨퍼런스. 신제품·대형 고객사 협업 발표가 주로 이때 나옴
- **주요 팹리스·하이퍼스케일러의 AI 반도체 capex 가이던스** — NVIDIA·AMD·Apple·주요 클라우드 업체의 반도체 설계·capex 투자 계획은 EDA 수요의 선행지표
- **TSMC 등 파운드리의 첨단 공정 가동률·capex** — 신규 설계 프로젝트 착수 여부와 연동

---

## 관련 문서

- [Synopsys 개요](./synopsys/01_overview.md)
- [Cadence Design Systems 개요](./cadence_design_systems/01_overview.md)

---

## 참고 자료

- [Electronic Design Automation Tools (EDA) Market Analysis — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/electronic-design-automation-eda-tools-market)
- [Electronic Design Automation Market Size & Forecast, 2033 — Persistence Market Research](https://www.persistencemarketresearch.com/market-research/electronic-design-automation-eda-market.asp)
- [Electronic Design Automation (EDA) Market Report 2026 — Research and Markets](https://www.researchandmarkets.com/reports/5953345/electronic-design-automation-eda-market-report)
- [Electronic Design Automation Software Market Size, Share, Forecast to 2034 — Fortune Business Insights](https://www.fortunebusinessinsights.com/electronic-design-automation-software-market-105985)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-21)*
