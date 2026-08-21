# 주식 리서치 노트

개인 투자자가 **실제 투자 판단**을 위해 작성·갱신하는 주식 리서치 아카이브입니다. [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)로 빌드해 GitHub Pages로 배포합니다.

**🔗 사이트: https://parkgyeongtae.github.io/stock-research/**

## 구성

- `docs/sectors/` — 섹터별·회사별 리서치 문서(개요·연혁·경영진·재무·밸류에이션·투자 결론·뉴스·기술적 차트)
- `docs/meta/` — 용어집·개념 정리·거시지표 차트 등 특정 회사·섹터에 종속되지 않는 참고 문서
- `scripts/` — 기술적 분석 차트(SVG)·거시지표 비교 차트를 생성하는 Python 스크립트(표준 라이브러리만 사용, 추가 설치 불필요)
- `.claude/skills/` — 회사/섹터/거시지표 문서를 새로 만들거나 개선하는 절차를 코드화한 Claude Code 스킬 모음
- `.github/workflows/deploy.yml` — `main` 브랜치에 푸시하면 `uv run mkdocs build` 결과를 GitHub Pages로 자동 배포
- `authoring-guide.md` — `docs/` 문서를 쓰고 관리할 때 지키는 규칙. 사이트 방문자용이 아니라 작성 절차용이라 `docs/` 밖에 둠

작성 규칙·새 회사/섹터 추가 절차는 [`authoring-guide.md`](./authoring-guide.md), AI 에이전트(Claude Code 등) 작업 지침은 [`AGENTS.md`](./AGENTS.md)에 정리되어 있습니다.

## 로컬에서 실행

의존성 관리에는 [uv](https://docs.astral.sh/uv/)를 씁니다.

```bash
uv sync
uv run mkdocs serve   # http://127.0.0.1:8000 에서 미리보기
uv run mkdocs build   # 배포와 동일하게 정적 사이트 빌드 (site/)
```
