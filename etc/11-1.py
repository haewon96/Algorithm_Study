# 예제 11-1 : 소수의 판별 - 기본적인 알고리즘

# 소수 판별 함수
def is_prime_number(x):   # 특정 자연수 x가 소수의 정의를 만족하는지 여뷰를 반복문을 이용하여 하나씩 확인
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:   # 입력으로 주어진 수 x가 i로 나누어 떨어지는 경우가 하나라도 존재한다면
            return False   # 소수가 아님
    return True   # 소수임

print(is_prime_number(4))
print(is_prime_number(7))