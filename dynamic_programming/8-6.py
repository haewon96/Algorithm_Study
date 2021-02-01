# 실전문제 8-6 : 개미 전사

n = int(input())
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
