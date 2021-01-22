# 예제 7-3 : 반복문으로 구현한 이진 탐색 소스코드

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    # 반복문이 수행될 때마다 현재 중간점 위치의 값을 확인해서 찾고자 하는 데이터를 찾았는지 검사하고, 찾기 못했다면 탐색 범위를 좁혀가는 방식
    while start <= end:
        mid = (start + end) // 2   # 중간점 설정 (몫 연산)

        # 찾은 경우, 중간점 인덱스 반환
        if array[mid] == target:
            return mid        # 중간점 인덱스 반환 == 찾은 값의 인덱스 반환

        # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1     # 끝점을 (중간점 - 1)로 대체

        # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
        else:
            start = mid + 1   # 시작점을 (중간점 + 1)로 대체

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)