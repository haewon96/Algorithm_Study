# 실전문제 9-4 : 미래 도시

INF = int(1e9)

n, m = map(int, input().split())
# n : 회사의 개수 (노드의 개수)
# m : 경로의 개수 (간선의 개수)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())
# x : 도착하는 회사 (노드)
# k : 거쳐가는 회사 (노드)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]

if graph[1][k] != INF and graph[k][x] != INF:
    print(result)
else:
    print(-1)