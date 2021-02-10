# 예제 9-3 : 플로이드 워셜 알고리즘 소스코드

INF = int(1e9)   # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]   # 파이썬의 경우 리스트 컴프리헨션을 이용한 2차원 리스트 초기화 가능
               # 각각의 노드가 1번부터 출발한다고 가정하여 n + 1 크기만큼 각각의 행과 열을 구성한 2차원 리스트 만들기

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c   # 방향 그래프 가정. 인접 행렬 방식 (2차원 배열) 이용하여 그래프 정보 표현 -> 2차원 리스트에 바로 비용정보 기록
        # a행 b열 c값

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    # k : 거쳐가는 노드
    for a in range(1, n + 1):
        # a : 출발 노드
        for b in range(1, n + 1):
            # b : 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            # a에서 b까지 가는 최단 노드 = 기존의 값과 a에서 k로 갔다가 다시 k에서 b로 가는 거리 비교하여 더 작은 값으로 갱신

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # 도달할 수 있는 경우, 거리 출력
        else:
            print(graph[a][b], end=' ')
    print()