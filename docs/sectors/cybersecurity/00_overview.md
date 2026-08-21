# Cybersecurity (사이버보안)

> 기업·정부의 네트워크·클라우드·엔드포인트·데이터를 위협으로부터 보호하는 소프트웨어·서비스 산업으로, 생성형 AI가 공격·방어 양쪽의 무기가 되면서 지출 성장세가 재가속되고 있는 동시에 벤더 통합(M&A) 물결이 시장 구조를 빠르게 재편하고 있다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(`04_metrics.md`·`07_investment.md`)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ 개념 정리는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: Cybersecurity (사이버보안)
- **밸류체인 위치**: 미드스트림 — 위협 인텔리전스·보안 리서치(업스트림) 위에서 네트워크·클라우드·엔드포인트·ID 보안 제품/플랫폼을 개발해 기업·정부 최종 고객(다운스트림)에게 공급하는 벤더 계층. 팔로알토 네트웍스는 네트워크 보안(NGFW·SASE)에서 출발해 클라우드 보안(Prisma Cloud)·보안 운영(Cortex)까지 확장한 통합 플랫폼 벤더에 해당한다.
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [Palo Alto Networks](./palo_alto_networks/01_overview.md)
- **인접 섹터**: 이 저장소에서 아직 별도로 다루는 인접 섹터 없음(클라우드 인프라·통신 장비 등은 커버리지 밖)

---

## 1. 한 줄 요약

사이버보안 산업은 기업·정부의 IT 자산(네트워크·클라우드·엔드포인트·ID·데이터)을 사이버 공격으로부터 지키는 소프트웨어·서비스 산업이다. 생성형 AI가 피싱·딥페이크 등 공격 정교화와 AI 기반 위협 탐지·대응 양쪽을 동시에 밀어올리면서 지출이 다시 가속되는 한편, 대형 벤더가 M&A로 네트워크·클라우드·엔드포인트·ID 보안을 하나의 플랫폼으로 묶는 통합(consolidation) 흐름이 시장 구조를 재편하고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 위협 인텔리전스·보안 리서치 (업스트림) | 취약점(CVE)·악성코드·공격 기법을 수집·분석해 방어 제품에 공급 | 벤더 자체 위협 리서치팀(Unit 42 등), MITRE·CISA 등 공공기관, 오픈소스 커뮤니티 | 글로벌 텔레메트리(탐지 데이터) 축적 규모, 리서치 인력 |
| **보안 제품/플랫폼 (이 섹터)** | 네트워크 보안(NGFW·SASE), 엔드포인트/XDR, 클라우드 보안(CNAPP), ID/IAM, SIEM/SOAR 등 개발·판매 | Palo Alto Networks·CrowdStrike·Fortinet·Zscaler·Cisco·Check Point 등 | 플랫폼 통합에 따른 전환비용(락인), 위협 데이터 규모의 경제, 규제 인증(FedRAMP 등) |
| 보안 서비스/통합 | 제품 구축·운영 대행(MDR·MSSP), 컨설팅 | Accenture·Deloitte 등 SI, 전문 MSSP | 숙련 보안 인력 확보 |
| 최종 수요 (다운스트림) | 기업 IT/보안팀·정부기관·클라우드 사업자가 제품·서비스를 도입해 자산을 방어 | 각 산업 CISO 조직 | — |

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 `07_investment.md`에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **정보보안 지출 규모(TAM)**: Gartner는 전 세계 정보보안(information security) 최종사용자 지출을 2025년 $213B, 2026년 약 $244B(전년比 약 12~13% 증가)로 전망했고, IDC는 2026년 약 $212B(전년比 +12.2%)로 추정한다(두 기관 모두 "정보보안" 카테고리 기준). 반면 시장 리서치 기관들은 "사이버보안 시장" 정의를 더 넓게 잡아 2026년 $234B(Persistence Market Research)~$340B(Precedence Research)까지 편차가 크다 — 포함 범위(하드웨어·서비스·컨설팅 포함 여부)가 기관마다 달라 단일 값으로 단정하지 않는다.
- **성장률(CAGR)**: Gartner 기준 2026년 단년도 성장률 11~13%대. 리서치 기관들의 중장기(2026~2033/2034/2035) CAGR 전망은 9.7%~13.8% 범위.
- **핵심 성장 동력**:
  1. **생성형 AI의 양면성** — 공격자는 AI로 피싱·딥페이크·악성코드 정교화를, 방어자는 AI 기반 위협 탐지·자동 대응(XDR·SOC 자동화)을 확대하며 양쪽 모두 지출을 밀어올린다. Gartner는 클라우드 보안을 2026년 가장 빠르게 성장하는 하위 세그먼트(전년比 +28.8%)로 꼽는다.
  2. **클라우드·하이브리드 전환 지속** — 워크로드가 클라우드로 이동하며 클라우드 네이티브 보안(CNAPP) 수요가 온프레미스 네트워크 보안보다 빠르게 성장.
  3. **규제 강화** — 미 SEC 사이버 인시던트 공시 규정, EU NIS2 지침 등 컴플라이언스 요구가 산업 전반의 최소 보안 지출 하한을 밀어올림.
  4. **사이버 공격 빈도 증가** — 랜섬웨어 등 공격이 늘며(설문 응답 기업의 83%가 최근 12개월간 공격 증가를 보고) 방어 지출의 필요성이 구조적으로 유지됨.

Sources: [Gartner Forecasts Worldwide End-User Spending on Information Security to Total $213 Billion in 2025](https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025) · [Top 6 cybersecurity trends from Gartner's 2026 Security Forecast](https://softwarestrategiesblog.com/2026/02/10/gartner-cybersecurity-trends-2026/) · [Cybersecurity Spending Statistics 2026 — StationX](https://app.stationx.net/articles/cybersecurity-spending-statistics) · [Cybersecurity Market Size & Growth Report 2034 — Persistence Market Research](https://www.persistencemarketresearch.com/market-research/cyber-security-market.asp) · [Cybersecurity Market — Precedence Research](https://www.precedenceresearch.com/cyber-security-market)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| IT 예산 민감도 | 보안은 필수 지출로 여겨져 경기 방어적인 편이나, 경기 둔화기엔 예산 증가율 자체가 둔화된다 — 2026년 설문에서 예산을 6%p 이상 늘린 CISO 비중이 22%로, 2024년 40%에서 하락 | CISO 예산 서베이(Deloitte-NASCIO, Wiz CISO Budget Benchmark 등) 연간 갱신치 |
| 벤더 통합(M&A)·플랫폼화 압력 | 2025년 사이버보안 M&A 거래액이 $96B(전년比 +270%)로 급증했고 2026년 1분기에만 $47B 규모 — 대형 벤더가 네트워크·클라우드·엔드포인트·ID 보안을 하나의 플랫폼으로 묶는 추세가 포인트 솔루션 벤더의 입지를 좁힌다. 대형 플랫폼 벤더에도 통합 실패·반독점 심사 리스크가 있음 | 분기별 사이버보안 M&A 거래 건수·총액, 대형 벤더의 플랫폼 제품군 확장(신규 카테고리 인수) 발표 |
| 가격 경쟁·과금 모델 전환 | 좌석(seat) 기반 과금은 AI가 보안 운영 인건비를 줄이면서 마진 압박을 받고 있어, 아웃컴 기반 과금으로 전환 압력이 커짐 | 주요 벤더 실적 발표의 순매출유지율(NRR)·평균판매단가(ASP) 추이 |
| 규제·정치 리스크 | SEC 공시 규정·EU NIS2 등 규제 강도가 정치 지형·행정부 정책 기조에 따라 완화/강화를 오갈 수 있음 | SEC·EU 등 주요 규제기관의 규정 제·개정 동향 |
| 인재 부족 | 숙련 보안 인력 부족이 MSSP·자동화(AI) 수요로 이어지지만, 동시에 고객사 내부 도입·운영 역량 부족이 신제품 채택을 늦추는 장벽이 되기도 함 | (ISC)² 등의 사이버보안 인력 격차(workforce gap) 통계 |

> 개별 회사의 Bull/Bear Case는 각 회사 `07_investment.md`에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **Gartner/IDC 정보보안 지출 전망 분기 업데이트** — 산업 전체 지출 성장률의 가장 표준적인 선행지표
- **CISO 예산 서베이(Deloitte-NASCIO, Wiz 등) 연간 발표치** — 실제 구매 의사결정권자의 지출 의향
- **분기별 사이버보안 M&A 거래 건수·총액** — 벤더 통합 속도, 대형 벤더의 카테고리 확장 방향
- **주요 벤더(팔로알토·크라우드스트라이크·포티넷·지스케일러 등)의 잔여계약가치(RPO)·순매출유지율(NRR)** — 산업 수요의 동행/후행 확인 지표
- **랜섬웨어·데이터 침해 발생 빈도 통계** — 방어 지출 필요성의 직접적 트리거

---

## 관련 문서

- [Palo Alto Networks 개요](./palo_alto_networks/01_overview.md)

---

## 참고 자료

- [Gartner Forecasts Worldwide End-User Spending on Information Security to Total $213 Billion in 2025](https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025)
- [Top 6 cybersecurity trends from Gartner's 2026 Security Forecast — Software Strategies Blog](https://softwarestrategiesblog.com/2026/02/10/gartner-cybersecurity-trends-2026/)
- [Cybersecurity Spending Statistics 2026 — StationX](https://app.stationx.net/articles/cybersecurity-spending-statistics)
- [Cybersecurity Market Size & Growth Report 2034 — Persistence Market Research](https://www.persistencemarketresearch.com/market-research/cyber-security-market.asp)
- [Cybersecurity Market — Precedence Research](https://www.precedenceresearch.com/cyber-security-market)
- [The $96 Billion Consolidation — Lyrie Research](https://lyrie.ai/research/research/cybersecurity-ma-consolidation-96bn-platform-wave-ciso-vendor-fatigue)
- [2026 CISO Budget Benchmark Report — Wiz](https://www.wiz.io/reports/ciso-security-budget-benchmark-2026)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-21)*
