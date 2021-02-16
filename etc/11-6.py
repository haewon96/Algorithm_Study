# 예제 11-6 : 구간합 빠르게 계산하기 - 코드 예시

# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합 (Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:   # 데이터를 하나씩 확인하면서 (데이터가 존재할 때)
    sum_value += i   # 합계 값에 더하기
    prefix_sum.append(sum_value)   # 그 위치까지의 합계 값을 접두사 합 리스트에 담기 (모든 위치에 대해서 접두사 합 구하기)

# 구간 합 계산 (세 번째 수부터 네 번째 수까지) <- 쿼리가 들어왔을 때 공식에 따라서 구간합 처리 (상수시간 소요)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])