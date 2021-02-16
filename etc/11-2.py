# 예제 11-2 : 소수의 판별 - 개선된 알고리즘

import math   # 제곱근을 구하기 위한 별도의 math 라이브러리    -> math.squrt(x)
              # 참고) 파이썬에서는 기본적으로 거듭제곱 연산 지원 -> x ** 0.5

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):   # x의 제곱근을 다시 실수로 바꾼 값 + 1 -> 실질적으로 제곱근까지 확인
                                                # 제곱근 값이 소수점 이하의 데이터를 가진다고 하더라도 정상적으로 확인 가능
    # for i in range(2, x):   # 기본적인 로직은 동일하되, i의 증가범위 달라짐 !
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False   # 소수가 아님
    return True   # 소수임

print(is_prime_number(4))
print(is_prime_number(7))
