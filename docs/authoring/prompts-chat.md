# 프롬프트 모음 레포 읽는 법 — prompts.chat

이 문서는 가장 널리 알려진 프롬프트 모음 저장소 [prompts.chat](https://prompts.chat)(구 *Awesome ChatGPT Prompts*, GitHub `f/prompts.chat`)이 **무엇을 모아 놓은 것이고 거기서 무엇을 배울 수 있는지**를 정리합니다. 번역이 아니라 저장소의 데이터(`prompts.csv`)를 직접 집계한 분석이며, 재현 방법은 맨 아래에 있습니다.

이 저장소가 따르는 규칙이 아니라 **참고용**입니다 — 결론부터 말하면 **프롬프트 목록은 베낄 것이 아니고, 반복해서 나타나는 문형(文型)만 값이 있습니다.**

---

## 1. 무엇인가

| 항목 | 값 |
| --- | --- |
| GitHub | `f/prompts.chat` (구 `f/awesome-chatgpt-prompts`) |
| 규모 | 169,224 ★ · 21,774 fork |
| 시작 | 2022-12-05 — **ChatGPT 공개 닷새 뒤** |
| 수록 | 프롬프트 2,162개 · 기여자 1,038명 |
| 데이터 | `prompts.csv` (약 5.7MB) — 컬럼 `act` · `prompt` · `for_devs` · `type` · `contributor` |
| 라이선스 | 프롬프트 본문은 **CC0 1.0**(퍼블릭 도메인), 사이트 코드는 MIT |

수록된 프롬프트의 성격은 `type` 컬럼으로 갈립니다 — 일반 텍스트 지시(TEXT) 1,829개, 구조화된 출력을 요구하는 것(STRUCTURED) 312개, 이미지 생성용(IMAGE) 21개. 개발자용 표시(`for_devs`)가 붙은 것은 159개뿐이고 나머지 2,003개는 일반 용도입니다.

**유명해진 이유는 품질보다 시점입니다.** ChatGPT가 공개된 직후, "이걸로 뭘 할 수 있는지" 아무도 모르던 시기에 나온 **사용 예시 목록**이었습니다. 그래서 별 개수(16.9만)는 프롬프트 작성법 가이드 중 1위인 DAIR.AI 가이드(7.8만)의 두 배가 넘지만, 성격은 교재가 아니라 **예제 사전**에 가깝습니다.

---

## 2. 대표작 하나를 해부하기

이 저장소를 유명하게 만든 초기 프롬프트인 `Linux Terminal`입니다(CC0).

> I want you to act as a linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is pwd

62단어짜리 문장에 장치가 다섯 개 들어 있습니다.

1. **역할 부여** — "act as a linux terminal". 모델이 낼 수 있는 응답의 분포를 한 번에 좁힙니다.
2. **출력 형식 고정** — "only reply with the terminal output inside one unique code block". 형식이 고정되면 결과를 **기계적으로 검증**할 수 있습니다.
3. **금지 목록** — "and nothing else", "do not write explanations". 모델이 기본적으로 하려는 행동(설명 덧붙이기)을 명시적으로 끕니다.
4. **탈출 통로** — "when i need to tell you something in english, i will do so by putting text inside curly brackets". 역할극을 깨지 않고 지시를 끼워 넣는 채널을 따로 만들어 둔 것으로, 이 목록 전체에서 가장 세련된 장치입니다.
5. **첫 입력 예시** — "my first command is pwd". 설명 대신 **예시 한 개로 형식을 굳히는** 원샷 few-shot입니다.

여기서 눈여겨볼 것은 "linux terminal"이라는 소재가 아니라, **원하는 것을 형식으로 못 박고 원치 않는 것을 이름으로 지목했다**는 구조입니다.

---

## 3. 2,162개에서 반복되는 문형

`prompts.csv` 전체를 정규식으로 집계한 결과입니다.

| 문형 | 비중 | 하는 일 |
| --- | ---: | --- |
| **역할 부여** (`act as` · `you are`) | 56.5% | 응답 분포를 좁힌다 |
| **출력 형식 고정** (코드블록·표·마크다운) | 35.6% | 결과를 검증 가능하게 만든다 |
| **범위 제한** (`do not` · `only`) | 31.0% | 기본 행동을 끈다 |
| **말투·언어 지정** | 26.3% | 문체를 고정한다 |
| **첫 요청 예시** (`my first … is`) | 5.6% | 예시 하나로 형식을 굳힌다 |
| **설명 금지** (`do not write explanations`) | 2.5% | 잡담을 제거한다 |

프롬프트 길이의 중앙값은 **139단어**이고, 하위 10%가 42단어, 상위 10%가 660단어입니다. 즉 대부분은 **"역할 + 형식 + 금지 + 첫 예시"** 네 덩어리로 이뤄진 한 문단짜리 지시입니다. 2,162개는 이 문법에 도메인만 갈아 끼운 변주에 가깝습니다.

---

## 4. 이 저장소가 이미 쓰고 있는 것

위 문형은 낯선 기술이 아니라 이 저장소가 이미 쓰는 장치입니다. 이름을 붙여 보면 어디를 더 조일 수 있는지가 보입니다.

| 문형 | 이 저장소의 대응물 |
| --- | --- |
| 역할 부여 | `AGENTS.md` "너는 이 저장소의 주인을 돕는 **시니어 주식 리서치 애널리스트**다" |
| 출력 형식 고정 | 회사 문서 템플릿(개요~최종 보고서의 번호 체계)과 `docs/.template/` |
| 범위 제한 | "투자 권유가 아니다", "용어를 새로 정의하지 않는다", "부분 수정하지 말고 다시 만든다" |
| 첫 예시로 형식 굳히기 | 템플릿 안의 ✅/❌ 예시 쌍 (예: 지우는 지침 블록 vs 남기는 경고 블록) |
| 말투 지정 | "대화 응답과 문서 갱신은 모두 한국어", 문서별 존댓말·반말 관행 |

즉 이 저장소의 지침은 **한 문단짜리 프롬프트를 파일 단위로 키운 것**입니다. 차이는 분량이 아니라 다음 절에 있습니다.

---

## 5. 이 모음이 통째로 빠뜨린 네 가지

2,162개를 훑어보면 **어떤 종류의 지시가 거의 등장하지 않는지**가 더 눈에 띕니다.

1. **출처 요구** — 어디서 가져온 숫자인지 밝히라는 지시가 사실상 없습니다.
2. **검증 방법** — "결과가 맞는지 무엇으로 확인하라"는 지시가 없습니다. 형식은 고정하면서 내용의 참·거짓은 열어 둡니다.
3. **불확실성 표기** — 모르는 것을 모른다고 표시하는 규약(추정치 표기 등)이 없습니다.
4. **사실과 의견의 분리** — 관측된 수치와 판단을 나눠 쓰라는 요구가 없습니다.

금융 분야 프롬프트에서 이 결핍이 가장 위험하게 드러납니다. 수록된 `Stock Market Analysis Expert`는 이렇게 되어 있습니다(CC0).

> Act as a Stock Market Analyst. … You will: - Evaluate stock performance based on the latest data - Identify trends and potential risks - Suggest strategic actions for investors  Rules: - **Use real-time market data** - Consider economic indicators - **Provide actionable and clear advice**

!!! warning "이런 프롬프트를 그대로 쓰지 않는다"
    세 가지가 동시에 잘못됐습니다. **(1)** 모델에게 없는 **실시간 데이터가 있다고 가정**합니다 — 도구로 가져오라는 지시가 없으면 모델은 기억으로 답을 지어냅니다. **(2)** 출처·기준 시점·GAAP 여부를 요구하지 않아 **검증 불가능한 숫자**가 나옵니다. **(3)** "actionable advice"를 요구해 **사실과 투자 판단이 한 문장에 뒤섞입니다.** 같은 목록의 `Financial Analyst`·`Investment Manager`도 "informed predictions", "safest possible options"처럼 같은 결함을 공유합니다.

이 저장소의 규칙은 정확히 이 셋을 막으려고 만들어졌습니다 — 수치는 1차 공시로 확인하고, 확인 못 한 값은 추정치로 표시하고, 사실과 의견을 섞지 않습니다.

---

## 6. 어떻게 쓸 것인가

- **문형은 가져오고 목록은 가져오지 않는다.** 위 여섯 가지는 어떤 도메인에도 적용되지만, 개별 프롬프트는 2023년 초 단발 대화 시대를 전제로 쓰였습니다. 도구를 호출하고 파일을 읽는 지금의 에이전트에게는 결이 맞지 않습니다.
- **"형식 고정"을 가장 먼저 쓴다.** 여섯 중 실무 효과가 가장 큰 장치입니다. 출력 형식이 정해지면 결과를 눈으로 훑는 대신 **검사할 수** 있게 됩니다.
- **금지 목록은 관찰한 뒤에 추가한다.** 미리 상상해서 채우면 지시가 길어지고 정작 중요한 규칙이 묻힙니다. 같은 실수가 두 번 반복될 때 한 줄씩 추가하는 편이 낫습니다.
- **역할 부여를 만능으로 여기지 않는다.** 절반 넘는 프롬프트가 쓰는 장치지만, 역할만으로는 **출처도 검증도 생기지 않습니다.** 5절의 네 가지를 따로 적어 줘야 합니다.

---

## 7. 이 문서의 수치를 다시 뽑으려면

집계 기준 시점은 2026-09-04이며, 아래 커맨드로 재현합니다.

```bash
curl -sL -o prompts.csv \
  https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv

python3 - <<'PY'
import csv, re, sys, collections
csv.field_size_limit(sys.maxsize)          # 긴 프롬프트가 있어 기본 한도로는 못 읽는다
rows = list(csv.DictReader(open("prompts.csv")))
texts = [r["prompt"] for r in rows]
pats = {
    "역할 부여":   r"(?i)\b(act as|acting as|you are|you will be)\b",
    "형식 고정":   r"(?i)(code block|in a table|markdown|bullet|format)",
    "범위 제한":   r"(?i)\b(do not|don't|only)\b",
    "말투 지정":   r"(?i)(in english|same language|tone|style of|voice)",
    "첫 요청 예시": r"(?i)my first (request|task|command|sentence|suggestion|question|topic)",
    "설명 금지":   r"(?i)(do not (write |provide |give )?(any )?explanation|only reply|nothing else)",
}
print(len(rows), collections.Counter(r["type"] for r in rows))
for name, p in pats.items():
    n = sum(bool(re.search(p, t)) for t in texts)
    print(f"{n:>5} ({n/len(texts)*100:4.1f}%)  {name}")
PY
```

별·fork 수는 GitHub API로 확인합니다: `curl -sL https://api.github.com/repos/f/awesome-chatgpt-prompts`

---

*작성일: 2026-09-04*
