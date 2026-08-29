# Synopsys (시놉시스)

> 반도체 설계 자동화(EDA) 시장의 1위 사업자. 2025년 Ansys 인수로 "칩 설계"에서 "시스템 시뮬레이션"까지 영역을 넓혔고, AI 반도체 설계 수요를 직접 받는 상류 위치에 있다 — 다만 그 확장 대가로 자본구조와 회계 지표가 단절적으로 바뀌었다.

- **회사명**: Synopsys, Inc.
- **티커 / 상장 시장**: SNPS (NASDAQ)
- **설립 / 본사**: 1986년 / 미국 캘리포니아 서니베일(Sunnyvale)
- **CEO**: Sassine Ghazi (2024년 1월 취임)
- **홈페이지**: https://www.synopsys.com
- **섹터 / 산업**: 테크 / EDA (Electronic Design Automation)
- **시가총액**: 약 890.8억 달러 (2026-08-27 종가 $464.89 × 기말 발행주식수 191.605백만 주, [핵심 지표](./04_metrics.md) A.2 인용)
- **회계연도(FY) 마감월**: 10월 말 (FY2025 = 2024.11~2025.10). 다른 문서는 이 정의를 인용만 한다

---

## 1. 사업 모델 — 어떻게 돈을 버는가

반도체 설계사(팹리스·IDM)와 전자 시스템 기업에 **설계·검증 소프트웨어를 시분할 라이선스(time-based license) 형태로 판매**하고, 사전 검증된 설계 블록(IP)을 라이선스·로열티로 공급한다. 소프트웨어 라이선스는 계약 기간에 걸쳐 매출로 인식되므로 매출의 상당 부분이 이미 수주된 잔고에서 나오며, 이것이 FY2023~FY2025 매출 증감률이 15.21%·15.22%·15.13%로 극히 안정적이었던 이유다([핵심 지표](./04_metrics.md) A.1).

회사가 공시하는 보고 부문은 **Design Automation과 Design IP 둘뿐**이며, 2025년 인수한 Ansys는 별도 부문이 아니라 Design Automation에 통합돼 있다.

| 사업 부문 | 설명 | 매출 비중 | 기준 시점 |
|-----------|------|-----------|-----------|
| Design Automation | 디지털·커스텀 설계 구현, 검증·시뮬레이션, 에뮬레이션 하드웨어, 그리고 인수한 Ansys의 구조·유체·전자기 멀티피직스 해석 | $5,302.4M (**75.2%**) | FY2025 (2025-12-10 실적발표 부문 표) |
| Design IP | 인터페이스 IP(USB·PCIe·DDR 등), 파운드리 공정별 재사용 설계 블록 | $1,751.8M (**24.8%**) | FY2025 (2025-12-10 실적발표 부문 표) |

- FY2024는 Design Automation 68.9%($4,221.1M) / Design IP 31.1%($1,906.3M)였다. **한 해 만에 비중이 6%p 이동한 것은 두 부문이 서로 반대로 움직였기 때문**이다 — Design Automation은 Ansys 편입으로 +25.6%, Design IP는 중국 수출규제와 대형 파운드리 고객 수요 부진으로 −8.1%.
- FY2026 Q3(2026-07-31 종료)에는 Ansys 온기 반영으로 이 쏠림이 더 커졌다: Design Automation $2,003.0M(80.9%, YoY +52.6%) / Design IP $473.8M(19.1%, YoY +10.8%). Design IP는 전년 부진의 기저효과로 성장률이 플러스 전환했으나 비중 자체는 계속 줄고 있다.
- **매각으로 빠지는 매출이 있다.** Optical Solutions Group과 Ansys PowerArtist RTL은 **FTC 동의명령에 따른 강제 매각**으로 2025-10-17경 Keysight에 넘겼고(FY2025 Q4), Processor IP Solutions는 FY2026 중 자발적으로 매각했다. 회사는 이 셋이 FY2026 매출을 각각 약 $110M·약 $40M(합계 약 $150M) 낮춘다고 밝혔으며 이미 가이던스에 반영돼 있다(2026-08-26 FY2026 Q3 실적발표).

Sources: [Synopsys Q4·FY2025 실적발표](https://news.synopsys.com/2025-12-10-Synopsys-Posts-Financial-Results-for-Fourth-Quarter-and-Fiscal-Year-2025) · [Synopsys FY2026 Q3 실적발표](https://news.synopsys.com/2026-08-26-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2026)

---

## 2. 산업 / 시장 내 위치

EDA 시장은 **Synopsys · Cadence · Siemens EDA** 3사가 과점하며, Synopsys는 매출 기준 1위다. 같은 섹터의 [Cadence](../cadence_design_systems/01_overview.md) FY2025 매출이 약 $53억인 데 비해 Synopsys는 $70.5억(FY2025)·FY2026 가이던스 $97.2억으로, Ansys 인수 이후 **매출 규모에서 2위와의 격차를 크게 벌렸다.**

- **경쟁 구도의 축이 "칩"에서 "시스템"으로 옮겨가고 있다.** Synopsys의 Ansys 인수와 Cadence의 System Design and Analysis 사업(BETA CAE·OpenEye·Hexagon D&E 인수)은 같은 방향의 경쟁이다. 다만 Synopsys는 약 $349억을 한 번에 들여 시장 1위 해석 소프트웨어 회사를 통째로 사들인 반면, Cadence는 중소형 인수를 연속으로 쌓는 방식이라 **재무 부담의 성격이 다르다**([재무 / 실적](./05_financials.md) 3. 재무 건전성).
- **지리적으로는 중국 익스포저가 줄고 있다.** FY2025 중국 매출은 약 $814M으로 전체의 약 11.5% 수준이며, 회사는 실적발표에서 중국 매출이 전년 대비 18%(Ansys 제외 시 22%) 감소했다고 밝혔다. 2025년 수출규제 국면 당시 보도된 약 16%에서 낮아진 것으로, 규제 재도입 시 충격의 크기도 그만큼 달라진다([투자 판단](./07_investment.md) 3. 리스크).
- **Design IP는 EDA 도구와 성격이 다르다.** 도구 사업이 라이선스 갱신으로 방어되는 반면, IP는 개별 칩 프로젝트 수주에 연동돼 변동성이 크다 — FY2025 −8.1%가 그 예다. 회사가 FY2026에 Processor IP Solutions를 매각한 것도 이 사업의 선택과 집중으로 읽힌다.

Sources: [Bullfincher — Synopsys revenue by geography](https://bullfincher.io/companies/synopsys/revenue-by-geography) (집계 사이트, 1차 공시 대조 필요) · [Synopsys Q4 FY2025 실적 컨퍼런스콜](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/)

---

*작성일: 2026-08-28*
