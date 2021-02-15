# 예제 10-5 : 크루스칼 알고리즘 소스코드

# 기본적으로 두 원소가 서로 같은 집합인지 아닌지 판단하기 위해 서로소 집합 자료구조 사용

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])   # 경로 압축 기법
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기 <- 그래프 정보
v, e = map(int, input().split())
parent = [0] * (v + 1)   # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


### 추가되는 부분 !!

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))   # 별도의 리스트에 담기 <- 파이썬에서는 튜플을 이용하여 비용(cost)이 첫 번째 원소가 되도록 삽입
                                 # 기본적으로 튜플의 원소가 여러 개일 경우 첫 번째 원소 기준 정렬 수행 -> 비용(cost)이 낮은 순서대로

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 (비용 낮은 순서대로)
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):   # 해당 간선에 포함된 원소 a, b에 대해 같은 집합에 포함되어 있지 않다면
        # 합집합 연산 수행할 때마다 해당 간선 비용 값을 결과 변수에 더하기
        union_parent(parent, a, b)   # 합집합 연산 수행
        result += cost   # 해당 간선을 최소 신장 트리에 포함시키기

print(result)   # 최종 출력 : 최소 신장 트리에 포함되어 있는 모든 간선의 비용합