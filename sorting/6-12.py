# 실전문제 6-12 : 두 배열의 원소 교체

n, k = map(int, input().split())   # N과 K를 입력받기
array_a = list(map(int, input().split()))   # 배열 A의 모든 원소를 입력받기
array_b = list(map(int, input().split()))   # 배열 B의 모든 원소를 입력받기

array_a.sort()
array_b.sort()

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if array_a[i] < array_b[n - 1 - i]:
        array_a[i], array_b[n - 1 - i] = array_b[n - 1 - i], array_a[i]

result = 0
for a in array_a:
    result += a
print(result)



"""
a.sort()               # 배열 A는 오른차순 정렬 수행
b.sort(reverse=True)   # 배열 B는 내림차순 정렬 수행

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
        
    # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출 (더 이상 배열 A의 원소 합을 크게 만들 수 없는 경우)
    else:
        break
        
print(sum(a))   # 배열 A의 모든 원소의 합을 출력
"""