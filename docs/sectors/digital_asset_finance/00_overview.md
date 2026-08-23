# Digital Asset Finance (디지털 자산 금융)

> 암호화폐 거래·보관과 스테이블코인 발행을 다루는 금융 인프라 산업으로, 2025년 GENIUS Act 제정을 계기로 미국에서 처음으로 연방 차원의 규제 틀이 갖춰지며 제도권 편입이 빠르게 진행되고 있다.

- **섹터명**: Digital Asset Finance (디지털 자산 금융 — 암호화폐 거래소·스테이블코인)
- **밸류체인 위치**: 미드스트림 — 블록체인 인프라(업스트림) 위에서 자산 거래·보관·발행 서비스를 제공하는 금융 중개/발행 계층. 커버리지 기업 중 Coinbase·Robinhood는 거래소(중개) 사업자, Circle은 스테이블코인 발행사로 사업 모델이 다르다
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [Coinbase](./coinbase/01_overview.md)
  - [Robinhood](./robinhood/01_overview.md)
  - [Circle](./circle/01_overview.md)
- **인접 섹터**: `payment_networks`(카드 결제 네트워크 — 스테이블코인이 장기적으로 결제 레일을 일부 대체할 가능성이 있어 경쟁·보완 관계) — 이 저장소에서 순수 블록체인 인프라(레이어1 프로토콜)·DeFi 섹터는 아직 별도로 커버하지 않음

---

## 1. 한 줄 요약

디지털 자산 금융은 암호화폐의 거래·보관(거래소)과 달러 연동 스테이블코인 발행이라는 두 축으로 이뤄진 산업이다. 2025년 7월 GENIUS Act(미국 최초의 연방 스테이블코인 규제법) 제정을 계기로 규제 불확실성이 크게 줄면서, 전통 금융기관·기관투자자의 참여가 빠르게 늘고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 블록체인 인프라 (업스트림) | 거래를 기록·정산하는 기반 프로토콜 | Bitcoin·Ethereum·Solana 등 레이어1 네트워크 | — (이 저장소에서 별도 커버 안 함) |
| **거래·중개 (이 섹터)** | 암호화폐 매매 중개, 보관(커스터디), 파생상품 등 | Coinbase·Robinhood·Binance·Kraken 등 | 규제 라이선스(MTL·BitLicense 등) 취득, 보안·신뢰 트랙레코드 |
| **스테이블코인 발행 (이 섹터)** | 달러 등 법정화폐에 1:1 연동된 토큰 발행·준비자산 운용 | Circle(USDC)·Tether(USDT) | 준비자산 규제 준수(GENIUS Act 등), 발행 신뢰도 |
| 최종 사용 (다운스트림) | 결제·송금·트레이딩·DeFi 담보 등으로 활용 | 개인·기관 투자자, 핀테크, DeFi 프로토콜 | — |

이 섹터는 사업 모델이 이질적인 두 그룹(거래소 vs 발행사)을 함께 묶는다 — 거래소는 거래대금 기반 수수료가, 스테이블코인 발행사는 준비자산 운용 이자수익(금리 연동)이 핵심 매출원이라는 점에서 금리 민감도의 방향이 다를 수 있다.

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 투자 판단에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **암호화폐 거래소 시장 규모(TAM)**: 리서치 기관마다 정의 차이로 편차가 매우 크다 — Straits Research(플랫폼 시장) $41.33B(2026)~$96.62B(2034, CAGR 11.2%), Coherent Market Insights $103.30B(2026)~$381.18B(2033, CAGR 20.5%), SNS Insider $68.85B(2026)~$173.92B(2030, CAGR 26.1%). 정의(플랫폼 매출 vs 거래대금 기반 다른 산정)가 기관마다 달라 단일 값으로 단정하지 않는다.
- **스테이블코인 시장 규모**: 시가총액 기준 2026년 약 $0.3T(3천억 달러) 수준이며, Mordor Intelligence는 2031년까지 $1.16T로 CAGR 28.77% 성장을 전망. Coinbase는 2028년까지 $1.2T로 확대될 것으로 전망한 바 있다(자체 추정, 편향 가능성 감안).
- **핵심 성장 동력**:
  1. **규제 명확화** — GENIUS Act(2025-07 제정) 등 연방 차원의 스테이블코인 규제 프레임워크가 갖춰지며, 규제 불확실성 때문에 참여를 미뤄온 전통 금융기관·기관투자자의 진입 장벽이 낮아짐.
  2. **기관·주류 금융 편입** — 크립토 네이티브 기업의 S&P500 편입(2025), 자산운용사의 크립토 ETP 상품 확대 등 전통 금융 시스템과의 통합이 가속.
  3. **스테이블코인의 결제·정산 레일 확장** — 온체인 정산·해외 송금 등에서 카드 네트워크·전신송금 대비 빠르고 저렴한 대안으로 스테이블코인 활용이 늘어남.

Sources: [Cryptocurrency Exchange Platform Market — Straits Research](https://straitsresearch.com/report/cryptocurrency-exchange-platform-market) · [Crypto Exchange Market — Coherent Market Insights](https://www.coherentmarketinsights.com/industry-reports/crypto-exchange-market) · [Cryptocurrency Exchange Market — SNS Insider](https://www.snsinsider.com/reports/cryptocurrency-exchange-market-7226) · [Stablecoin Market — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/stablecoin-market)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 규제 불확실성·정치 리스크 | GENIUS Act로 스테이블코인 규제는 명확해졌으나, 거래소 사업(증권성 판단 등)에 대한 SEC·CFTC 관할권 다툼은 진행형. 규제 완화 기조가 친(親)크립토 행정부 정책에 크게 의존해, 정치 지형 변화 시 다시 강화될 수 있음 | SEC·CFTC의 규정 제정·집행 동향, 행정부·의회의 크립토 정책 기조 |
| 암호화폐 가격 변동성 | 거래소 매출은 거래대금에 연동되는데, 거래대금은 암호화폐 가격 변동성·투자심리에 크게 좌우됨 — 약세장에서는 거래대금·매출이 동반 급감 | 비트코인·이더리움 등 주요 암호화폐 가격 추이, 거래소 거래대금 통계 |
| 금리 민감도(스테이블코인 발행사) | 스테이블코인 준비자산(주로 단기국채)의 이자수익이 발행사 매출의 핵심이라, 기준금리 하락은 유통량이 늘어도 이자수익 증가를 상쇄할 수 있음 | 미 연준 기준금리 결정, 단기국채 금리 추이 |
| 경쟁·규제차익(offshore 거래소) | 미국 역외에 기반한 대형 거래소(Binance 등)와의 경쟁 — 규제 준수 비용을 부담하는 미국 상장 거래소가 상대적으로 불리할 수 있음 | 주요 거래소별 거래량 점유율 통계 |
| 보안/커스터디 리스크 | 해킹·내부자 유출 등 보안 사고가 발생하면 신뢰 기반 사업 특성상 타격이 큼 | 업계 보안 사고 발생 빈도·규모 |

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **GENIUS Act 시행세칙·감독기관 규정 제정 현황** (본 법 발효는 2028-07-18 예정) — 스테이블코인 발행사에 미치는 구체적 규제 부담
- **SEC·CFTC의 크립토 자산 관할권 관련 규정·소송·화해 동향** — 거래소 사업의 법적 명확성
- **미 연준 기준금리 결정** — 스테이블코인 발행사 이자수익의 방향
- **암호화폐 시가총액·거래대금 통계** (CoinMarketCap 등) — 거래소 매출의 선행지표
- **스테이블코인 시가총액 성장 추이** — 발행사 매출 기반(유통량)의 직접 지표

---

## 관련 문서

- [Coinbase 개요](./coinbase/01_overview.md)
- [Robinhood 개요](./robinhood/01_overview.md)
- [Circle 개요](./circle/01_overview.md)

---

## 참고 자료

- [Cryptocurrency Exchange Platform Market Size, Share, Growth, 2034 — Straits Research](https://straitsresearch.com/report/cryptocurrency-exchange-platform-market)
- [Crypto Exchange Market Size and Forecast – 2026 to 2033 — Coherent Market Insights](https://www.coherentmarketinsights.com/industry-reports/crypto-exchange-market)
- [Cryptocurrency Exchange Market Size & Growth Report 2026-35 — SNS Insider](https://www.snsinsider.com/reports/cryptocurrency-exchange-market-7226)
- [Stablecoin Market Size, Share & 2031 Growth Trends Report — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/stablecoin-market)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-23)*
