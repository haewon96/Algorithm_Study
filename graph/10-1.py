# 예제 10-1 : 기본적인 서로소 집합 알고리즘 소스코드

# find 연산 : 특정 원소가 속한 집합을 찾기 -> 루트노드 반환하기
def find_parent(parent, x):   # parent : 부모 테이블 / x : 노드 번호
    # 관행적인 함수명 <- 경로 압축 기법 사용하면 사실상 루트노드가 테이블상 자신의 부모로 기록될 수 있기 때문에 합리적 !
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:   # 현재 부모가 자기 자신이 아니라면 (루트노드 X)
        return find_parent(parent, parent[x])   # 루트노드를 찾기 위해 자신의 부모 노드 번호를 통해 재귀적으로 함수 호출
    return x

# union 연산 : 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)   # a의 루트노드 찾기
    b = find_parent(parent, b)   # b의 루트노드 찾기
    if a < b:   # 각각의 루트노드를 확인하여 번호가 큰 쪽이 작은 쪽을 부모로 설정
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)   # 부모 테이블 초기화 <- 모든 노드의 정보를 담을 수 있는 형태 (1번 ~ v번)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행 -> 실제로 두 원소의 연결 여부 확인하기 (간선의 개수에 따라서)
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)   # 원소 a와 b가 서로 연결되어 있다는 의미

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')   # 각 노드에 대한 루트노드 확인 -> 루트노드가 같은 원소끼리는 같은 집합으로 판단 가능
print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')   # 유의) 단순히 자신의 부모에 대한 정보 != 루트노드(집합)에 대한 정보