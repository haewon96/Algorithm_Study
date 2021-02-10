# 실전문제 9-4 : 미래 도시

INF = int(1e9)   # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# n : 회사의 개수 (노드의 개수)
# m : 경로의 개수 (간선의 개수)

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정 - 간선 설정 유의
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())
# x : 도착하는 회사 (노드)
# k : 거쳐가는 회사 (노드)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])   # 플로이드 워셜 알고리즘 점화식으로 2차원 테이블 갱신

# 수행된 결과 출력
min_time = graph[1][k] + graph[k][x]

# 도달할 수 있다면, 최단 거리 출력
if graph[1][k] != INF and graph[k][x] != INF:
    print(min_time)
# 도달할 수 없는 경우, -1 출력
# if min_time >= INF:
else:
    print(-1)