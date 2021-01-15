# 예제 5-9 : BFS 예제

from collections import deque   # 큐 라이브러리

# BFS 함수 정의
def bfs(graph, start, visited):
    # graph : 그래프 정보 / start: 시작 노드 / visited : 방문 처리 여부 기록 정보

    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])   # 시작 노드 큐에 넣기

    # 현재 노드를 방문처리
    visited[start] = True    # 시작 노드 방문 처리

    # 큐가 빌 때까지 반복 (더 이상 수행할 수 없을 때까지)
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()   # popleft() : 가장 먼저 들어 온 원소 꺼내기
        print(v, end=' ')     # 해당 노드의 번호 출력

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:   # 꺼낸 노드와 인접한 노드를 하나씩 확인하면서
            if not visited[i]:   # 아직 방문하지 않은 인접 노드가 있다면 모두 큐에 넣기
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (그래프 표현을 위한 2차원 리스트)
graph = [
    [],   # 0번 노드 사용 X
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
    # 1번 노드부터 ~ 8번 노드까지 8개의 노드 처리 -> 총 원소가 9개인 리스트 객체 생성
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (방문 처리를 위한 1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수호출
bfs(graph, 1, visited)