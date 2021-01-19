# 실전문제 5-11 : 미로 탈출

from collections import deque

def bfs(x, y):
    if x <= -1 or x >= n or y <= -1 or x >= n:
        return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

count = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            count += 0

print(count)