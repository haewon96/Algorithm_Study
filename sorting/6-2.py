# 예제 6-2 : 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교

from random import randint   # 정렬 실행 시킬 목적으로 랜덤한 10,000개의 데이터 이용하기 위해 randint() 함수 필요
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i   # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()
# 수행 시간 출력 <- 수행 시간 측정을 위해서 실제 알고리즘 밖에 선언된 start_time, end_time 변수 이용
print('선택 정렬 성능 측정 : ', end_time - start_time)   # 종료 시간 - 시작 시간

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()   # 파이썬의 경우, 병합 정렬을 기반으로 하는 하이브리드 방식의 정렬 알고리즘 사용
               # 최악의 경우에도 O(NlogN)의 시간 복잡도 보장 -> 선택 정렬과 비교했을 때 1초보다 훨씬 짧은 시간에 동작

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print('기본 정렬 라이브러리 성능 측정 : ', end_time - start_time)
