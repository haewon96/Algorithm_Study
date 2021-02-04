# 기출문제 A34 : 병사 배치하기

n = int(input())
array = list(map(int, input().split()))

result = 0
for i in range(1, n - 1):
    if array[i - 1] > array[i] and array[i] < array[i + 1]:
        result += 1
        array[i] = array[i - 1]

print(result)



"""
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()   # 입력받은 병사들의 전투력 정보 뒤집기

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1, n):   # 두 번째 원소부터 마지막 원소까지 각 원소를 확인하면서
                        # 해당 원소를 마지막 원소로 설정하는 증가하는 부분 수열의 최대 길이 구하는 내부 반복문 수행
    for j in range(0, i):   # 앞에 있는 모든 원소 중에서
        if array[j] < array[i]:   # 자기 자신보다 해당 원소가 작은 경우에 한해서
            dp[i] = max(dp[i], dp[j] + 1)   # 점화식을 이용한 테이블 갱신 수행

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))   # 테이블에 담겨있는 값 중 가장 큰 값 == 가장 긴 부분 수열의 길이
"""