# 예제 5-5 : 2가지 방식으로 구현한 팩토리얼 예제

# 반복적으로 구현한 n! <- 반복문 이용
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n! <- 재귀함수 이용
def factorial_recursive(n):
    if n <= 1:   # n이 1 이하인 경우 1을 반환 (1! = 0! = 1)
        return 1
    # n! = n * (n - 1)!을 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력 (n = 5)
print('반복적으로 구현 : ', factorial_iterative(5))   # 반복문 사용 O
print('재귀적으로 구현 : ', factorial_recursive(5))   # 반복문 사용 X
