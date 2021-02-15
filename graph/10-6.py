# 예제 10-6 : 위상 정렬 소스코드

from collections import deque   # 위상 정렬 알고리즘에서 사용하는 큐 라이브러리 호출

# 노드의 개수(vertex : 정점)와 간선의 개수(edge : 간선)를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 (그래프) 초기화 - 방향 그래프 정보 입력
graph = [[] for i in range(v + 1)]   # 전체 노드의 개수 v개 -> 1번부터 v번까지 각 노드에 대한 인접 노드 정보 2차원 리스트

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)   # 정점 A에서 B로 이동 가능
    # 진입차수를 1 증가 <- B에 대해서 들어오는 간선 존재
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []   # 알고리즘 수행 결과를 담을 리스트
    q = deque()   # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()    # 큐에 들어간 순서 == 전체 위상 정렬의 수행 결과
        result.append(now)   # 큐에서 원소를 꺼낼 때마다 결과 리스트에 담기

        # 해당 원소와 연결된 (이동 가능한) 노드들의 진입차수에서 1 빼기 <- 나가는 간선 제거
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력 - 결과 리스트에 담겨있는 각각의 원소 출력
    for i in result:
        print(i, end=' ')

topology_sort()
