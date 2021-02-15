# 예제 10-4 : 서로소 집합을 활용한 사이클 판별 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):   # 서로소 집합 자료구조와 동일
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])   # 경로 압축 기법 적용 -> 보다 빠르게 루트 노드를 찾을 수 있도록 !
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):   # 서로소 집합 자료구조와 동일
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)   # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


### 추가되는 부분 !!

cycle = False   # 사이클 발생 여부 (초기 상태)

for i in range(e):   # 모든 간선을 하나씩 확인하면서 합집합 연산 수행
    a, b = map(int, input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):   # 노드 a와 b 두 원소가 이미 같은 집합에 속해있다면 사이클 발생 판단 가능
        cycle = True
        break   # 반복문 빠져나가기

    # 사이클이 발생하지 않은 경우 합집합 (union) 수행
    else:   # 노드 a와 b 두 원소가 같은 집합에 속해있지 않다면
        union_parent(parent, a, b)   # 같은 집합에 속할 수 있도록 합집합 연산 수행

if cycle:   # 최종적으로 cycle 변수 값에 따라서 발생 여부 출력
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')