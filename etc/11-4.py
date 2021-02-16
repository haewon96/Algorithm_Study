# 예제 11-4 : 특정한 합을 가지는 부분 연속 수열 찾기 (투 포인터) - 코드 예시

# 투 포인터 알고리즘은 다양한 방법으로 구현 가능 -> 문제마다 실제로 구현되는 방식이 다를 수 있기에 보다 효율적인 구현 방식 유의

n = 5   # 데이터의 개수 N
m = 5   # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]   # 전체 수열

# 초기화
count = 0
interval_sum = 0   # 현재 부분 수열 값
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):   # start값은 반복문을 이용해서 차례로 0부터 n - 1까지 증가시키기 (선호하는 방식)
    # (현재 start를 기준으로) end를 가능한 만큼 오른쪽으로 이동시키기
    while interval_sum < m and end < n:   # 현재 부분합이 m보다 작다면 매번 end값을 오른쪽으로 이동하여 현재 부분합 증가시키기 !
                                          # end값은 n을 벗어나지 않도록 (데이터의 범위를 벗어나지 않도록) 설정하기
        interval_sum += data[end]
        end += 1
    # while문을 탈출한 상황 : 현재 부분합 m 이상

    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]   # 구간에 대한 부분합을 줄일 수 있도록 start값을 오른쪽으로 이동하여 현재 부분합 감소시키기 !

print(count)