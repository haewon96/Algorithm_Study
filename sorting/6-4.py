# 예제 6-4 : 퀵 정렬 소스코드 (일반적인 방식)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]   # 총 10개의 데이터

def quick_sort(array, start, end):
    # 정렬하고자 하는 데이터의 범위가 하나인 경우
    if start >= end:   # 원소가 1개인 경우 종료
        return

    # 정렬하고자 하는 데이터의 범위가 여러개인 경우
    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1     # 첫 번째 원소 제외 왼쪽   <- 왼쪽에서부터 피벗값보다 큰 데이터 찾기
    right = end          # 첫 번째 원소 제외 오른쪽 <- 오른쪽에서부터 피벗값보다 작은 데이터 찾기

    while left <= right:   # 엇갈릴 때까지 선형탐색 반복 수행 (left 인덱스 <= right 인덱스) -> 엇갈리면 반복문 탈출
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1    # 왼쪽 -> 오른쪽 이동
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1   # 오른쪽 -> 왼쪽 이동

        if left > right:   # 엇갈렸다면 작은 right -= 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            # 참고) 엇갈린 이후에는 right이 가지는 값이 더 작은 값
        else:   # 엇갈리지 않았다면 작은 left 데이터와 큰 right 데이터를 교체
            array[left], array[right] = array[right], array[left]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 - 재귀적 호출
        quick_sort(array, start, right - 1)   # 이미 정렬이 완료된 right 위치를 기준으로 좌/우 재귀함수 반복
        quick_sort(array, right + 1, end)     # 이상적인 경우 왼쪽과 오른쪽 균형있는 분할 -> 빠른 동작 기대

quick_sort(array, 0, len(array) - 1)
print(array)