# 실전문제 5-11 : 미로 탈출

from collections import deque   # 라이브러리 호출 필요

# BFS 소스코드 구현       <- BFS 함수 동작
def bfs(x, y):
    # 큐 (Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()        # deque를 통한 큐 기능 구현
    queue.append((x, y))   # 초기에 (x, y) 튜플 데이터 담기

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()   # 반복할 때마다 큐에서 하나의 원소를 꺼내고
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시 <- 연결된 위치가 공간 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시 <- 괴물이 존재해서 이동할 수 없는 위치인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1   # 바로 직전 노드 위치에서의 최단 경로값 + 1
                queue.append((nx, ny))   # 다음으로 이동할 위치까지는 1만큼 거리가 먼 곳이므로
                                         # 큐에 데이터를 넣으면서 거리값 증가시키기

    # 가장 오른쪽 아래까지의 최단 거리 반환 (결과적)
    return graph[n - 1][m - 1]

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기 (2차원 데이터) <- 그래프 초기화
graph = []
for i in range(n):
    graph.append(list(map(int, input())))   # 공백 없이 0과 1로 구성된 문자열 -> 문자열 입력 후 int형 list 변환

# 이동할 네 방향 정의 (상, 하, 좌, 우)        <- 방향벡터 정의
                # 상 : 행 기준 - 1
                # 하 : 행 기준 + 1
                # 좌 : 열 기준 - 1
                # 우 : 열 기준 + 1
dx = [-1, 1, 0, 0]   # 세로축 (행)
dy = [0, 0, -1, 1]   # 가로축 (열)

# BFS를 수행한 결과 출력   <- BFS 함수 호출
print(bfs(0, 0))



"""
count = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            count += 1

print(count)
"""