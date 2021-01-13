# 실전문제 4-3 : 왕실의 나이트

# 열 a, b, c, d, e, f, g, h
# 행 1, 2, 3, 4, 5, 6, 7, 8
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h']
row = [1, 2, 3, 4, 5, 6, 7, 8]

loc = input()
count = 0

for i in range(8):
    if loc[0] == column[i]:
        c = i
        r = int(loc[1]) - 1
# print(r, c)

### dx, dy 2개의 리스트 이용한 방향벡터 정의
dx = [-2, -2, -1, -1, 1, 1, 2, 2]   # 행 방향 이동
dy = [-1, 1, -2, 2, -2, 2, -1, 1]   # 열 방향 이동

for i in range(8):
    nx = r + dx[i]
    ny = c + dy[i]

    if 0 <= nx <= 7 and 0 <= ny <= 7:
        count += 1

print(count)


"""
### steps 1개의 리스트 이용한 방향벡터 정의


# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])   # 행 <- 두 번째 위치의 문자를 숫자로 바꾸기
column = int(ord(input_data[0])) - int(ord('a')) + 1
                           # 열 <- 첫 번째 위치의 문자를 아스키코드로 바꾸고 문자 a의 아스키코드 값과 빼고 1 더하기
                           # ord() : 특정 문자의 아스키코드 값으로 변환해주는 함수
                           # chr() : 아스키코드 값을 문자로 변환해주는 함수

# 나이트가 이동할 수 있는 8가지 방향 정의 - 2차원 배열을 이용한 방향벡터 정의
steps = [
         (-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
"""