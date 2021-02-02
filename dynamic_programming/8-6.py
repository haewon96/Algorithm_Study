# 실전문제 8-6 : 개미 전사

# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

d = [0] * n
k_array = array
step = 0

while step < n:
    k = max(k_array)

    for i in range(n):
        if array[i] == k:
            d[i] = k

    k_array[i] = 0
    if 0 <= i - 1 < n: k_array[i - 1] = 0
    if 0 <= i + 1 < n: k_array[i + 1] = 0

    step += 1

print(sum(d))



"""
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 (보텀업)
d = [0] * 100   # 3 <= N <= 100 (최대 100까지 가능하기에 각각의 부분 문제에 대한 값이 담길 수 있도록 크기 설정)

# 다이나믹 프로그래밍 (Dynamic Programming) 진행 (보텀업)
d[0] = array[0]   # 1번째 위치까지 얻을 수 있는 식량의 최댓값은 1번째 원소 그대로 가져오기
d[1] = max(array[0], array[1])   # 2번째 위치까지 얻을 수 있는 식량의 최댓값은 1번째 원소와 2번째 원소 중 큰 값 1개 고르기

for i in range(2, n):   # 3번째 위치부터 n번째 위치까지 모든 경우에 대해 optimal solution 구하기
    # 점화식 그대로 사용 !
    d[i] = max(d[i - 1], d[i - 2] + array[i])   # i번째 위치까지 얻을 수 있는 식량의 최댓값은 
           # (i - 1)번째와 (i - 2)번째에 현재 i번째 위치에 대한 식량의 값을 더한 값을 비교하여 더 큰 값 1개 고르기

# 계산된 결과 출력
print(d[n - 1])
"""