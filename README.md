# 주식 리서치 노트

개인 투자자가 **실제 투자 판단**을 위해 작성·갱신하는 주식 리서치 아카이브입니다. [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)로 빌드해 GitHub Pages로 배포합니다.

**🔗 사이트: https://parkgyeongtae.github.io/stock-research/**

## 구성

- `docs/sectors/` — 섹터별·회사별 리서치 문서(개요·연혁·경영진·재무·밸류에이션·투자 결론·뉴스·기술적 차트·최종 보고서)
- `docs/glossary.md`·`docs/concepts/`·`docs/macro/` — 용어집·개념 정리·거시지표 차트 등 특정 회사·섹터에 종속되지 않는 참고 문서
- `docs/authoring/` — 이 저장소의 문서를 만드는 규칙(문서 작성·차트 생성·스킬 작성·에이전트 활용 가이드)
- `scripts/` — 기술적 분석 차트(SVG)·거시지표 비교 차트 생성 스크립트(표준 라이브러리만 사용, 추가 설치 불필요)
- `.claude/skills/` — 회사/섹터/거시지표 문서를 새로 만들거나 개선하는 절차를 코드화한 Claude Code 스킬 모음
- `.github/workflows/deploy.yml` — `main`에 푸시하면 빌드 결과를 GitHub Pages로 자동 배포

저장소를 굴리는 절차서 세 편은 `docs/authoring/`에 모아 사이트와 함께 발행합니다 — 어떤 규칙으로 이 문서들이 만들어졌는지 사이트에서 바로 읽기 위해서입니다.

- [`docs/authoring/authoring-guide.md`](./docs/authoring/authoring-guide.md) — 폴더 구조·파일별 역할·작성 규칙·새 회사/섹터 추가 절차
- [`docs/authoring/chart-generation-guide.md`](./docs/authoring/chart-generation-guide.md) — 차트 생성 스크립트 사용법·재현 파라미터
- [`docs/authoring/skill-authoring-guide.md`](./docs/authoring/skill-authoring-guide.md) — `.claude/skills/` 스킬 작성 규칙 (Anthropic 공식 [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) 한국어 정리)
- [`docs/authoring/claude-code-guide.md`](./docs/authoring/claude-code-guide.md) — Claude Code 활용 규칙 (Anthropic 공식 [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) 한국어 정리)
- [`docs/authoring/codex-guide.md`](./docs/authoring/codex-guide.md) — Codex 활용법 참고 (OpenAI 공식 [Best practices](https://learn.chatgpt.com/guides/best-practices) 한국어 정리)

에이전트 지침만 저장소 루트에 남습니다 — 세션 시작 시 루트에서 읽히는 파일이기 때문입니다.

- [`AGENTS.md`](./AGENTS.md) — AI 에이전트(Claude Code 등) 작업 지침 (`CLAUDE.md`는 이 파일의 심볼릭 링크)

## 로컬에서 실행

의존성 관리에는 [uv](https://docs.astral.sh/uv/)를 씁니다.

```bash
uv sync
uv run mkdocs serve   # http://127.0.0.1:8000 에서 미리보기
uv run mkdocs build   # 배포와 동일하게 정적 사이트 빌드 (site/)
```
