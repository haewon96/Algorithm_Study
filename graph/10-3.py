# 예제 10-3 : 개선된 서로소 집합 알고리즘 소스코드

# 기본적인 서로소 집합 알고리즘 소스코드와 비교했을 때 find_parent()만 변경 ! 나머지는 동일 !
# 경로 압축 기법 : 현재 노드가 루트 노트가 아닐 때 재귀적으로 부모에 find_parent() 함수 호출한 뒤에 반환된 루트 노드 값을 부모 테이블에 담기

# find 연산 : 특정 원소가 속한 집합을 찾기
# 경로 압축 기법 O -> 부모 노드 == 루트 노드
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 -> 반환값을 자신의 부모값이 될 수 있도록 갱신
    if parent[x] != x:   # 현재 노드의 부모값이 자기 자신이 아니라면 (루트 노드 X)
        parent[x] = find_parent(parent, parent[x])
        # 결과적으로 find_parent() 함수 호출 후 부모 테이블에 적힌 부모의 값이 자신의 루트 노드가 될 수 있도록 설정하기
        # find 연산 수행 후 함수 호출할 때 사용했던 노드에 대한 부모의 값이 루트 노드와 동일하도록 경로 압축 !
    return parent[x]

"""
# 경로 압축 기법 X -> 부모 노드 != 루트 노드
def find_parent(parent, x):   # parent : 부모 테이블 / x : 노드 번호
    # 관행적인 함수명 <- 경로 압축 기법 사용하면 사실상 루트 노드가 테이블상 자신의 부모로 기록될 수 있기 때문에 합리적 !
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:   # 현재 부모가 자기 자신이 아니라면 (루트 노드 X)
        return find_parent(parent, parent[x])   # 루트 노드를 찾기 위해 자신의 부모 노드 번호를 통해 재귀적으로 함수 호출
    return x
"""


# union 연산 : 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)    # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')