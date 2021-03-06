# 예제 8-4 : 피보나치 수열 소스코드 (반복적) - 보텀업 다이나믹 프로그래밍 소스코드

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100   # 0부터 99까지의 인덱스를 가지면서 각 원소의 값이 0이 되도록 초기화

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
# 재귀함수의 종료 조건 대신에 반복문의 점화식 시작항 초기화
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):   # 3번째부터 n번째까지의 모든 피보나치 수 계산
    d[i] = d[i - 1] + d[i - 2]   # 반복문을 이용하여 점화식을 그대로 기입하고 차례대로 각각의 항 구하기
                                 # 작은 문제부터 먼저 해결한 후 조합하여 앞으로의 큰 문제를 차례대로 구하는 방식

print(d[n])
