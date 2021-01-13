# 예제 4-2 : 시각

# H를 입력받기
h = int(input())

count = 0

for i in range(h + 1):    # i (시) -> 0부터 h까지 1씩 증가
    for j in range(60):     # j (분) -> 0부터 59까지 1씩 증가
        for k in range(60):   # k (초) -> 0부터 59까지 1씩 증가
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):   # 문자열 덧셈 연산
                count += 1

print(count)



"""
### 행렬 (Matrix) <- 일반적인 알고리즘 문제에서의 2차원 공간 !

for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end='')
        # end : print 함수가 끝난 후 넣을 문자 지정    (기본값 : 계행 \n)
        # sep : print 함수의 값들 사이에 넣을 문자 지정 (기본값 : 공백 1칸)
    print()
"""