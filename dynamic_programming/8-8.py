# 실전문제 8-8 : 효율적인 화폐 구성

"""
n, m = map(int, input().split())
array = [0] * n
for i in range(n):
    array[i] = int(input())

d = [0] * (m + 1)
array.sort(reverse=True)

d[m] = -1
for i in range(1, m + 1):   # 금액
    for a in array:   # 화폐
        if i >= a:
            d[i] = d[i - a] + 1
            print('금액', i, ', 화폐', a, '-> d[', i, '] = ', d[i])

print(d[m])
"""



# 정수 N, M을 입력받기 <- N : 화폐 개수 / M : 만들고자 하는 금액
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)   # 0원부터 m원까지 각각의 금액에 대한 최소한의 화폐 개수 구하기

# 다이나믹 프로그래밍 (Dynamic Programming) 진행 (보텀업)
d[0] = 0   # 0원은 아무 것도 안 해도 만들 수 있는 금액
# 점화식 활용하여 각각의 화폐 단위를 하나씩 확인하면서 모든 금액에 대한 각각의 optimal solution 값 갱신하기
for i in range(n):
    # i : 각각의 화폐 단위
    for j in range(array[i], m + 1):   # 해당 금액부터 m원까지 확인
        # j : 각각의 금액
        if d[j - array[i]] != 10001:   # (i - k)원을 만드는 방법이 존재하는 경우
                                       # 현재 금액에서 확인하고 있는 화폐 단위를 뺀 금액을 만들 수 있는 경우
            # 점화식 코드로 구현 !
            d[j] = min(d[j], d[j - array[i]] + 1)   # 현재 금액과 (i - k)원을 만드는 방법에 1을 더한 값을 비교하여 더 작은 값 갱신

# 계산된 결과 출력
if d[m] == 10001:   # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:   # 결과적으로 M원을 만드는 방법이 있는 경우 출력하는 방식
    print(d[m])
