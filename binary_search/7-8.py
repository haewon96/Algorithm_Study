# 실전문제 7-8 : 떡볶이 떡 만들기

def max_height(n, m, h_list):
    height = 1

    while height >= 1:
        result = 0
        for i in range(n):
            if h_list[i] > height:
                result += h_list[i] - height
            else:
                continue

        if result == m:
            return height
        elif result > m:
            height += 1
        else:
            height -= 1

# 떡의 개수(N)와 요청한 떡의 길이(M)를 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
h_list = list(map(int, input().split()))

max_h = max_height(n, m, h_list)
print(max_h)



"""
# 이진 탐색을 위한 시작점과 끝점 설정 <- 탐색 범위 설정 (높이로 설정할 수 있는 값의 범위 국한)
start = 0
end = max(array)   # 입력으로 들어온 (현재 가지고 있는) 떡의 높이 중 가장 긴 떡의 길이

# 이진 탐색 수행 (반복적) -> 최적의 해 구하기
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2   # 매번 현재 탐색 범위를 이용해 중간점 (높이) 설정
    for x in array:
        # 잘랐을 때의 떡의 양 계산 -> 현재 높이로 떡을 잘랐을 때의 전체 떡의 양
        if x > mid:            # 현재 떡의 길이가 높이보다 더 클 때에만 실제로 떡을 얻을 수 있기에
            total += x - mid   # 잘린 부분의 떡을 total 변수에 담기 (전체 떡을 잘랐을 때의 떡의 양 정보)

    # 탐색 범위 바꾸기 1) 2)
    # 1) 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
                                 # 높이 값이 줄어드는 방향으로 탐색 범위를 조절하여 더 많은 떡을 얻을 수 있도록 업데이트
    if total < m:
        end = mid - 1   # 끝점 위치 조정
    # 2) 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
                                 # 높이 값을 늘리는 방향으로 탐색 범위를 조절하여 떡을 덜 자를 수 있도록 업데이트
    else:
        result = mid   # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
                       # 떡의 양이 충분한 경우 (m 이상의 떡을 얻을 수 있는 경우) -> result의 값을 높이 값으로 갱신
                       # 최종적으로 가장 마지막에 기록된 높이 값 출력
        start = mid + 1   # 시작점 위치 조정

# 정답 출력
print(result)
"""
