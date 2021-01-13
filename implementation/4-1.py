# 예제 4-1 : 상하좌우

# N을 입력받기
n = int(input())
x, y = 1, 1   # 현재 위치
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]   # 방향벡터 - 세로축 (행)
dy = [-1, 1, 0, 0]   # 방향벡터 - 가로축 (열)
move_types = ['L', 'R', 'U', 'D']   # 이동 가능한 문자 리스트

# 이동 계획을 하나씩 확인 (계획서)
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):   # 현재의 이동 계획이 move_types 중 어떤 것인지 확인하고
        if plan == move_types[i]:      # 해당 move_types에 맞는 다음 위치 값 설정하기
            # 다음 위치
            nx = x + dx[i]   # 행 방향 이동
            ny = y + dy[i]   # 열 방향 이동

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)



"""
### 방향벡터 <- 시뮬레이션 및 완전 탐색 문제에서 자주 활용 !

# 방향 벡터 정의 (동, 북, 서, 남)
dx = [0, -1, 0, 1]   # 세로축 (행)
dy = [1, 0, -1, 0]   # 가로축 (열)

# 현재 위치 (특정 위치)
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]   # 행 방향 이동
    ny = y + dy[i]   # 열 방향 이동
    print(nx, ny)
"""