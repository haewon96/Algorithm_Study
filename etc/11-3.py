# 예제 11-3 : 에라토스테네스의 체 알고리즘

import math

n = 1000   # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)]   # 처음엔 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
                                       # 인덱스 0부터 n까지의 모든 값에 대해 True값 -> 각각의 수의 소수 판별은 테이블 인덱스 접근 확인

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):   # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True:   # i가 소수인 경우 (남은 수인 경우)
        # i(소수)를 제외한 i의 모든 배수를 지우기
        j = 2   # 배수
        while i * j <= n:   # 범위 내
            array[i * j] = False   # 소수가 아님을 기록하기
            j += 1   # 배수 증가

# 에라토스테네스의 체로 걸러진 모든 소수 출력
for i in range(2, n + 1):   # 2부터 n까지의 모든 자연수 중 소수
    if array[i]:   # 해당 인덱스 값이 True(참)인 경우
        print(i,end=' ')   # 인덱스 값 출력
