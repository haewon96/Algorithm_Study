# 기출문제 A01 : 모험가 길드
"""
number = input()
data = list(map(int, input().split()))
sorted_data = sorted(data, reverse=True)

print(number)
print(sorted_data)
"""



n = int(input())
data = list(map(input().split()))
data.sort()   # 공백을 기준으로 입력된 정수 리스트 정렬

result = 0   # 총 그룹의 수
count = 0    # 현재 그룹에 포함된 모험가의 수 -> 그룹이 결정될 때마다 다시 0으로 업데이트 필요

for i in data:   # 정렬된 공포도를 낮은 것부터 하나씩 확인하며
    count += 1   # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:   # 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도 이상이라면, 그룹 결성
        result += 1   # 총 그룹의 수 증가시키기 -> 새로운 그룹 결성 확인 필요
        count = 0     # 현재 그룹에 포함된 모험가의 수 초기화 -> 다음 그룹을 확인하기 위해 초기화 필요

print(result)   # 총 그룹의 수 출력