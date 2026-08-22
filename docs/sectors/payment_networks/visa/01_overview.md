# Visa Inc.

> 전 세계 카드 결제의 약 61%(2024년 기준, 미국 시장)를 처리하는 결제 네트워크 회사. 카드를 발급하지도, 대출을 하지도 않고 은행·가맹점 사이의 승인·정산·결제 파이프(VisaNet)만 운영하는 "톨게이트" 사업모델이라 신용 리스크를 지지 않으면서 결제금액 성장에 그대로 올라타는 구조가 핵심 투자 포인트다.

> ⚠️ 시가총액은 2026-08-14(금) 종가 $364.15, Class A 발행주식수 기준 환산 약 $669B(출처: stockanalysis.com — Visa의 다중 클래스 주식 구조로 인해 기관별 집계 방법론이 조금씩 다를 수 있음, 상세는 [`04_metrics.md`](./04_metrics.md) A.2 각주 참고).

- **회사명**: Visa Inc.
- **티커 / 상장 시장**: NYSE: V (Class A common stock)
- **설립 / 본사**: 1958년 BankAmericard(Bank of America 신용카드 프로그램)로 출발, 1976년 Visa로 개명, 2007년 Visa Inc.로 재편(2008년 IPO) / 본사 San Francisco, California
- **CEO**: Ryan McInerney (2023-02-01 취임)
- **홈페이지**: https://usa.visa.com , https://investor.visa.com
- **섹터 / 산업**: Payment Networks (결제 네트워크) — Financial Services, Transaction & Payment Processing Services
- **시가총액**: 약 $669B (2026-08-14 종가 기준)
- **회계연도(FY) 마감월**: 9월 말 (FY2025 = 2024-10-01 ~ 2025-09-30) — 다른 문서에서 이 값을 그대로 인용할 것

---

## 1. 한 줄 요약

Visa는 전 세계 200개 이상의 국가·지역에서 카드 결제의 승인·정산·결제를 처리하는 결제 네트워크(VisaNet) 운영사다. 은행이 카드를 발급(issuing)하고 가맹점 계약을 관리(acquiring)하는 반면, Visa 자신은 신용을 제공하거나 카드를 발급하지 않고 그 사이의 "통행료" 역할만 한다 — 이 구조 덕분에 신용 부실 리스크 없이 전 세계 소비 지출·전자결제 전환(현금→카드) 성장에 직접 노출된다.

---

## 2. 사업 모델 — 어떻게 돈을 버는가

Visa는 전통적 의미의 "사업 부문(segment)"을 구분해 공시하지 않는다(단일 보고 세그먼트) — 대신 매출을 4개 수익원으로 나누고, 여기서 은행·가맹점에 지급하는 리베이트(client incentives)를 차감해 순매출(net revenue)을 계산한다.

| 매출 구성 요소 | 설명 | FY2025 총매출 대비 비중 |
|-----------|------|-----------|
| Data processing revenue | 거래 승인·정산·결제(authorization/clearing/settlement) 처리 수수료, 부가가치서비스(Acceptance Solutions·Risk and Security 등), 네트워크 접속료. 당분기 거래 실적 기준으로 인식 | 35.9% |
| Service revenue | 결제망 상시 접속·운영에 대한 대가. **직전 분기** 결제금액(nominal payments volume) 기준으로 당분기 인식 | 31.5% |
| International transaction revenue | 국경간(cross-border) 거래 처리·환전 수수료 — 카드 발급국과 가맹점 소재국이 다른 거래에서 발생, 마진이 가장 높은 매출원 | 25.4% |
| Other revenue | 자문(Advisory)·발급 지원 등 기타 부가가치서비스 | 7.3% |
| (차감) Client incentives | 은행·가맹점 대상 장기 인센티브 계약에 따른 리베이트 — 매출 차감 항목(contra-revenue)으로 처리 | −28.2%(총매출 대비) |
| **= 순매출 (Net revenue)** | | **100%("순" 기준, 총매출 $55,751M − 인센티브 $15,751M = $40,000M)** |

> 비중은 FY2025(2024-10-01~2025-09-30) 총매출(client incentives 차감 전, $55,751M) 대비 각 항목의 비율로 계산. 원자료·GAAP 손익계산서 항목은 [`04_metrics.md`](./04_metrics.md) A.1 참조. 출처: [Visa FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm) MD&A "Net Revenue" 절.

**핵심 특징**:

- **4-party 모델**: 카드 발급 은행(issuer) — 카드 소지자(cardholder) — 가맹점(merchant) — 매입 은행(acquirer) 사이에서 Visa는 네트워크·표준·브랜드만 제공한다. 신용 손실은 발급 은행이 부담하므로 Visa의 손익계산서에는 대손충당금이 사실상 없다.
- **Service revenue의 1분기 시차 인식** 구조 때문에, 특정 분기의 소비 급변(경기 충격 등)이 매출에 온전히 반영되기까지 한 분기가 걸린다 — 실적 해석 시 유의할 지점.
- **Client incentives(리베이트)가 사실상의 실효 할인율**로 기능하며, 최근 확대 추세(총매출 대비 21%→22% 근처)를 보이고 있다 — 은행·대형 가맹점에 대한 협상력 지표로 추적할 가치가 있다([`04_metrics.md`](./04_metrics.md) C절 참고).
- Visa Direct(실시간 자금이동), Cybersource(가맹점 결제 게이트웨이), 최근에는 스테이블코인 정산(USDC)·AI 에이전트 커머스(Trusted Agent Protocol) 등으로 "카드 레일 밖" 자금이동까지 사업 영역을 넓히는 중([`08_news.md`](./08_news.md) 참고).

---

## 3. 산업 / 시장 내 위치

> 산업 밸류체인·시장 규모/성장 동력·구조적 리스크는 [`../00_overview.md`](../00_overview.md) 참고.

Visa는 미국 카드 결제금액 기준 시장점유율 약 61%(2024년, Mastercard 26%·Amex 11%·Discover 2%)로 업계 1위이며, 사실상 Mastercard와의 양강 구도(글로벌 기준 두 회사 합산 점유율이 압도적)다. American Express·Discover는 폐쇄형(closed-loop, 자체 발급·매입까지 겸업) 네트워크라 Visa·Mastercard의 개방형(open-loop) 모델과 경쟁 구도가 다르다.

시장 자체는 "현금·수표 → 전자결제 전환"이라는 장기 구조적 성장 동력을 여전히 가지고 있고, 여기에 국경간 전자상거래 확대가 더해진다. 다만 최근 실시간 계좌이체(FedNow 등 A2A 결제), 스테이블코인 기반 정산처럼 카드 네트워크를 우회할 수 있는 대안 레일이 부상하는 중이며, Visa는 이를 경쟁 위협이자 자체 사업 기회(Visa Direct·스테이블코인 정산)로 동시에 다루고 있다. 이 섹터에 다른 커버리지 기업이 아직 없어 경쟁사 배수 비교는 생략 — 추후 Mastercard 등이 추가되면 그때 다룰 것.

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

- [공식 홈페이지](https://usa.visa.com)
- [Visa FY2025 10-K (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm)
- [Investor Relations](https://investor.visa.com)
- [Nilson Report — Mastercard and Visa Cards in the US 2025](https://nilsonreport.com/articles/mastercard-and-visa-cards-in-the-us-2025/)

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-16)*
