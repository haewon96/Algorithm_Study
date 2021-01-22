# 예제 7-2 : 재귀 함수로 구현한 이진 탐색 소스코드

# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    # array : 탐색을 수행하고자 하는 배열 / target : 찾고자 하는 데이터 / start ~ end : 탐색범위
    if start > end:   # 탐색범위에 데이터가 존재하지 않음 -> None값 반환
        return None
    mid = (start + end) // 2   # 그렇지 않다면 중간값 명시 (몫 연산)

    # 찾은 경우, 중간점 인덱스 반환
    if array[mid] == target:   # 중간점 위치의 값과 찾고자 하는 값이 같다면 (해당 값 찾음)
        return mid   # 중간점 인덱스 반환 == 찾고자 하는 값이 위치하는 인덱스 반환

    # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽 확인 (중간점 위치 포함 오른쪽은 항상 target보다 큰 값이기 때문에)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
                                         # 끝점을 중간점 왼쪽으로 옮겨서 왼쪽부분 탐색 수행 by 재귀 함수

    # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인 (중간점 위치 포함 왼쪽은 항상 target보다 작은 값이기 때문에)
    else:
        return binary_search(array, target, mid + 1, end)
                                         # 시작점을 중간점 오른쪽으로 옮겨서 오른쪽부분 탐색 수행 by 재귀 함수

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:   # 탐색범위가 다 줄어들었음에도 불구하고 원소를 찾지 못한 경우
    print('원소가 존재하지 않습니다.')
else:                # 그렇지 않다면 해당 원소가 존재하는 인덱스 + 1 -> 몇 번째 원소인지 반환
    print(result + 1)