# 예제 8-1 : 피보나치 함수 소스코드 - 단순 재귀 소스코드

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:   # 재귀함수 종료조건 명시 <- 재귀함수가 무한루프를 돌지 않고 특정 지점에서 호출을 멈출 수 있도록 구현
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))