# 실전문제 3-4 : 1이 될 때까지

n, k = map(int, input().split())
count = 0

if n >= k:
    print(n, k)

    while (n != 1):
        if n % k != 0:
            n = n - 1
            count += 1
        else:
            n = n // k
            count += 1

    print(count)

else:
    print('n should be bigger than or equal to k ')


"""
### 단순하게 풀기


n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떠러잊지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)



### 빠른 수행을 위한 테크닉 사용하기


# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    # 반복 횟수에 따라서 바로 N이 K로 나누어지는 연산이 수행되어 기하급수적으로 빠르게 줄어드는 효과 !
    target = (n // k) * k    # 가장 가까운 K로 나누어 떨어지는 수 찾기
    result += (n - target)   # 1을 빼는 연산횟수 한번에 계산하기
    n = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1   # N >= K일 때 K로 나누는 연산 1번 수행하기
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
"""