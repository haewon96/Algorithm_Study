# 예제 6-1 : 선택 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 총 10개의 데이터 리스트에 저장

for i in range(len(array)):   # 0부터 전체 데이터의 개수(len(array)) - 1까지 반복
    # i : 가장 작은 데이터와 위치과 바뀔 인덱스 (매번 앞쪽으로 보내고자 하는 원소의 위치)
    min_index = i   # 가장 작은 원소의 인덱스 <- 반복할 때마다 매번 가장 작은 원소의 인덱스 고르기
                    # 처음에는, 가장 앞쪽 원소가 가장 작은 원소가 되도록 수행
    for j in range(i + 1, len(array)):   # i + 1부터 전체 원소의 개수(len(array)) - 1까지 선형탐색 수행하며 가장 작은 원소 찾기
        if array[min_index] > array[j]:
            min_index = j   # 현재 가장 작은 원소보다 더 작은 원소가 있다며 그 위치 인덱스 값을 min_index값으로 당김
                            # 결과적으로, 안쪽의 j 반복문 수행 종료 후 가장 작은 원소의 인덱스가 min_index가 되도록 수행
    array[i], array[min_index] = array[min_index], array[i]   # 스와프 <- 가장 앞쪽 원소와 가장 작은 원소 위치 바꾸기
                                                              # 파이썬 간단 ! (별도의 표준 라이브러리 필요 X)

print(array)