# 기출문제 A31 : 금광

test_case = int(input())
for t in range(test_case):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    gold_mine = []
    for i in range(n):
        gold_mine.append(array[(i * m):(i * m) + m])

    d = []
    for i in range(n):
        d.append([0] * m)

    """
    # 참고사항
    for i in range(n):
        for j in range(m):
            print('d[', i, '][', j, '] = ', gold_mine[i][j])
    print(gold_mine)
    # 00 01 02 03
    # 10 11 12 13
    # 20 21 22 23
    """

    for j in range(m):
        for i in range(n):
            if j == 0:
                d[i][j] = gold_mine[i][j]

            else:
                if i == 0:
                    d[i][j] = max(d[i][j - 1], d[i + 1][j - 1]) + gold_mine[i][j]
                elif i == (n - 1):
                    d[i][j] = max(d[i - 1][j - 1], d[i][j - 1]) + gold_mine[i][j]
                else:
                    d[i][j] = max(d[i - 1][j - 1], d[i][j - 1], d[i + 1][j - 1]) + gold_mine[i][j]

    result = [d[i][m - 1] for i in range(n)]
    print(max(result))



"""
# 테스트 케이스 (Test Case) 단위로 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))   # 금광 정보가 한 줄로 이어져서 입력

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])   # 열의 크기 m 단위로 데이터 슬라이싱하여 DP 테이블에 담아 2차원 데이터 표현
        index += m

    # 다이나믹 프로그래밍 진행 (보텀업)
    for j in range(1, m):   # 열 기준으로 각 데이터를 확인하면서 테이블 갱신 - 오른쪽 이동하여 각 열마다 전체 행 확인
        for i in range(n):
            # 1) 왼쪽 위에서 오는 경우 <- 인덱스를 벗어나지 않는지 체크 (i == 0 일 때)
            if i == 0:
                left_up = 0     # 인덱스를 벗어난다면 해당 경우의 값 0으로 초기화
            else:
                left_up = dp[i - 1][j - 1]

            # 2) 왼쪽 아래에서 오는 경우 <- 인덱스를 벗어나지 않는지 체크 (i == n - 1 일 때)
            if i == n - 1:
                left_down = 0   # 인덱스를 벗어난다면 해당 경우의 값 0으로 초기화
            else:
                left_down = dp[i + 1][j - 1]

            # 3) 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
                                # 3가지 경우의 optimal solution 중 가장 큰 값을 가지는 경우에
                     # 현재 매립된 금의 값을 더하여
            # 현재 위치에 대한 optimal solution 갱신하기

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])   # 결과적으로 가장 오른쪽 열에 기록된 값 중 제일 큰 값 출력

    print(result)
"""
