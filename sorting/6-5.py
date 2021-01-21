# 예제 6-5 : 파이썬의 장점을 살린 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]   # 총 10개의 데이터

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    # 리스트 슬라이싱
    pivot = array[0]   # 피벗은 첫 번째 원소 - 피벗값 설정
    tail = array[1:]   # 피벗을 제외한 리스트 - 피벗값 제외 두 번째 원소부터 마지막 원소까지

    # 리스트 컴프리헨션
    left_side = [x for x in tail if x <= pivot]   # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]   # 분할된 오른쪽 부분
    # 피벗을 제외한 리스트의 각 원소를 하나씩 확인하면서 피벗값과 비교 - 1) 작으면 왼쪽 2) 크면 오른쪽

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    # 왼쪽 부분 퀵 정렬 결과 리스트 + 피벗값 포함 리스트 + 오른쪽 부분 퀵 정렬 결과 리스트 -> 모든 원소에 대해 정렬이 수행된 결과

print(quick_sort(array))



