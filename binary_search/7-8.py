# 실전문제 7-8 : 떡볶이 떡 만들기

def max_height(n, m, h_list):
    height = 1

    while height >= 1:
        result = 0
        for i in range(n):
            if h_list[i] > height:
                result += h_list[i] - height
            else:
                continue

        if result == m:
            return height
        elif result > m:
            height += 1
        else:
            height -= 1

# 떡의 개수(N)와 요청한 떡의 길이(M)를 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
h_list = list(map(int, input().split()))

max_h = max_height(n, m, h_list)
print(max_h)


