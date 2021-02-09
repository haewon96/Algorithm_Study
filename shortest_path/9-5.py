# 실전문제 9-5 : 전보

import heapq
# import sys
# input = sys.stdin.readline
INF = int(1e9)   # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수, 시작 노드를 입력 받기 <- 그래프 정보 입력 받기
n, m, c = map(int, input().split())
# n : 도시의 개수 (노드의 개수)
# m : 통로의 개수 (간선의 개수)
# c : 메시지를 보내고자 하는 도시 (시작 노드)

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기 <- 각 노드에 대해서 다른 노드로 이동하기 위한 비용 정보 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))
    # 특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며 메시지 전달되는 시간 z


### 개선된 다익스트라 알고리즘 코드 그대로 사용 ( 우선순위 큐를 이용한 다익스트라 알고리즘 )
def dijkstra(c):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, c))
    distance[c] = 0

    while q:   # 큐가 비어있지 않다면 (큐가 빌 때까지 반복)
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:   # 우선순위 큐에서 꺼낸 노드가 이미 처리된 적이 있는지 확인
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인 (아직 방문하지 않은 노드일 경우)
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서 인접한 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost   # 해당 비용값으로 최단 거리 테이블 갱신
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(c)

result = []
for i in range(1, n + 1):
    if distance[i] != INF:
        result.append(distance[i])

print(len(result) - 1, max(result))
# 도시 c에서 보낸 메시지를 받는 도시의 총 개수, 총 걸리는 시간



"""
# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:   # 각 노드에 대한 최단 거리 값을 하나씩 확인하면서
    # 도달할 수 있는 노드인 경우
    if d != INF:   # 무한 X -> 도달 O
        count += 1   # count 값 증가
        max_distance = max(max_distance, d)   # 그때마다 도달 가능한 노드 중에서 가장 거리가 먼 노드까지의 거리 값 기록
                                              # 헤당 최단 거리 값의 최댓값
# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)
"""