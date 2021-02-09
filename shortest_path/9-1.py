# 예제 9-1 : 간단한 다익스트라 알고리즘 소스코드

# 빠르게 입력받기 : 입력 데이터의 개수가 많은 문제에 input() 함수 대신 readline() 함수 이용하기
import sys
input = sys.stdin.readline

"""
# 파이썬의 다양한 입력 방법
1. input() : 기본적으로 문자열을 입력받는 함수
   -> 입력받는 값을 list()로 변형시켜서 값을 쪼개거나, 정수형 int() 실수형 float() 입력 변형 가능
   
2. sys.stdin.readline() : 한 줄에 여러 입력 값을 받을 수 있는 함수
                        ( 입력 데이터의 개수가 많은 경우 시간 초과 피할 수 있는 방법 )
   -> 1) import sys 라이브러리 필요
      2) readline() 함수의 경우, 기본적으로 계행문자 ( 줄 바꿈 문자 : enter ) 포함하기 때문에
         문자열 마지막에 계행문자가 포함되어 출력
      3) 공백 문자를 제거하기 위한 옵션 ( 공백 없이 출력하기 위한 함수 )
         - rstrip() : 오른쪽 공백 삭제
         - lstrip() : 왼쪽 공백 삭제
         - strip()  : 왼쪽, 오른쪽 공백 삭제
      4) map()을 사용하여 한 줄로 여러 변수에 값 입력 가능   
"""

INF = int(1e9)   # 무한을 의미하는 값으로 10억을 설정 <- 기본적으로 테이블 초기화 할 때 무한 사용

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]   # 연결리스트 형태로 그래프 초기화
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기 <- 방향 그래프 기본 가정
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))   # a번째 리스트에 b와 c를 하나의 튜플로 묶어 넣어주기

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():   # 매번 단계 반복하는 과정에서 사용되는 함수
    min_value = INF   # 임의로 처음에 무한을 할당 해놓은 min_value 변수 이용
    index = 0   # 가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1, n + 1):   # 1번부터 n번까지 모든 노드를 하나씩 확인하면서
        if distance[i] < min_value and not visited[i]:   # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호 반환하기
            min_value = distance[i]
            index = i
    return index

# 실제 다익스트라 알고리즘 작성 : 간단한 구현 방법
def dijkstra(start):
    # 시작 노드에 대해서 초기화 (출발 노드)
    distance[start] = 0      # 출발 노드까지의 거리 0
    visited[start] = True    # 출발 노드 방문처리 O
    for j in graph[start]:   # 출발 노드로부터 당장 도달할 수 있는 다른 노드까지의 거리 갱신
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1개 노드에 대해 반복
    for i in range(n - 1):   # 이후 총 n - 1개 노드에 대해 반복
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인 (꺼내진 노드)
        for j in graph[now]:
            cost = distance[now] + j[1]   # 현재 선택된 노드까지의 거리 + 현재 노드와 연결된 거리
            # 현재 노드를 거쳐서 인접한 다른 노드로 이동하는 거리가 더 짧은 경우 최단 거리 값 갱신
            if cost < distance[j[0]]:   # 기존 비용보다 더 작다면 해당 비용으로 테이블 갱신
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력 <- 수행 이후 각각의 노드에 대해 최단 거리 확인
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우, 거리 출력
    else:
        print(distance[i])
