# 동종사와 맞추기

같은 섹터 문서끼리 지표와 가정이 근거 없이 갈리면 회사를 나란히 놓고 볼 수 없다. **동종사 문서를 통째로 읽지 말고 필요한 행만 뽑는다** — 아래 두 명령은 한 턴에 같이 낸다(섹터에 회사가 5개여도 합쳐 3k 토큰 안쪽이다).

## C절 사업 고유 지표 (SKILL.md 2-3)

```bash
S=docs/sectors/<sector>
for f in $S/*/04_metrics.md; do c=$(basename $(dirname $f)); [ "$c" = "<company>" ] && continue
  sed -n '/^## C\. 사업 고유 지표/,/^## D\./p' $f | grep -E '^\||^\*\*이 섹터' \
    | awk -F'|' 'NF>3{print "| "$2"|"$3"|"$4} !/\|/{print}' | grep -v '^| *-\+' \
    | cut -c1-120 | sed "s#^#[$c] #"
done
```

**같은 섹터라도 밸류체인 위치가 다르면 지표도 다르다.** `natural_gas`의 Cheniere(LNG 수출)는 EQT(업스트림 E&P)와 다른 지표를 쓰고 그 사유를 C절 머리에 적어 뒀다. 무조건 베끼지 말고 **밸류체인 위치가 같은 회사**를 따른다.

## 밸류에이션 가정 (SKILL.md 4-1)

```bash
S=docs/sectors/<sector>
for f in $S/*/06_valuation.md; do c=$(basename $(dirname $f)); [ "$c" = "<company>" ] && continue
  sed -n '/^## 1\. 적용 방법론/,/^## 2\./p' $f | grep -E '^\|' \
    | grep -E '할인율|영구성장률|목표 ?(PER|PBR)|가중치' | cut -c1-160 | sed "s#^#[$c] #"
done
```

- **값을 맞추라는 뜻이 아니다.** 사업 위험이 다르면 Ke도 달라야 한다 — 다만 동종사와 크게 다르면 `06`에 **왜 다른지 한 줄**을 남긴다. Kinder Morgan `06`은 Williams와 무위험이자율이 0.03%p 다른 이유까지 각주로 남겼다.
- 무위험이자율은 같은 macro 문서(`rates/treasury_10y.md`)를 쓰되 조회 시점이 다르면 날짜를 밝힌다.
- 섹터 첫 회사면 이 대조를 건너뛴다.
