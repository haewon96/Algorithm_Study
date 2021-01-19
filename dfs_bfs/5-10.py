# 실전문제 5-10 : 음료수 얼려 먹기

"""
n, m = map(int, input().split())

graph = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    input_value = input()
    for j in range(m):
        graph[i][j] = int(input_value[j])

print(graph)

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            if graph[i + 1][j] == 0 or graph[i - 1][j] == 0 or graph[i][j + 1] == 0 or graph [i][j - 1] == 0:
                continue
            else:
                count += 1
        else:
            continue

print(count)
"""



# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):   # n줄에 걸쳐서 입력 <- 공백 없이 0과 1로 구성된 문자열 형태
    graph.append(list(map(int, input())))   # 한 줄 입력받고 정수형 리스트 변환 (모든 원소가 0 또는 1)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)   # 연결된 모든 위치에 대해 재귀적인 방문처리 진행 -> return 사용 X 단순 연결된 노드 방문처리 O
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True   # 결과적으로 True 반환 -> 현재 위치에 대해 처음 DFS 처리 되었기에 그 위치의 result 증가

    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):   # n * m 크기의 각 위치
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:   # 현재 위치 방문처리 확인
            result += 1

print(result)   # 정답 출력

### 결과적으로 DFS는 한 번 수행되면 해당 노드와 연결된 모든 노드 방문처리 수행
### 시작 노드(해당 노드)가 방문처리는 처음 방문할 때에만 result 값 증가



"""
### 인접 리스트 방식 : 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장 (연결리스트) -> 2차원 리스트로 구현

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))
# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))
# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)
"""