# 기출문제 A27 : 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())   # 데이터의 개수 N, 찾고자 하는 값 x 입력받기
array = list(map(int, input().split()))   # 전체 데이터 입력받기

count = bisect_right(array, x) - bisect_left(array, x)



"""
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):   # 실제로 다양한 코딩테스트에서 효과적으로 사용하는 count_by_range() 함수 !!
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 값이 [x, x] 범위에 있는 특정 데이터의 개수 계산 (left_value == right_value)
count = count_by_range(array, x, x)
"""



# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)