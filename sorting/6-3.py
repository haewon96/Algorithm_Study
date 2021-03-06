# 예제 6-3 : 삽입 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 총 10개의 데이터

for i in range(1, len(array)):   # 두 번째 원소부터 시작하여 왼쪽으로 이동 해나가면서 위치 바꾸기 (by 안쪽의 j 반복문)
    for j in range(i, 0, -1):    # 인덱스 i부터 1까지 감소하며 반복하는 문법
             # range() 함수의 3번째 인자 : step
        # j : 현재 삽입하고자 하는 원소의 위치
        if array[j] < array[j - 1]:   # 한 칸씩 왼쪽으로 이동
                                      # 왼쪽의 데이터와 비교했을 때 값이 더 작다면,
            array[j], array[j - 1] = array[j - 1], array[j]   # 위치 바꾸기 (swap)
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                # 왼쪽의 데이터와 비교했을 때 삽입하고자 하는 현재 데이터 값이 더 크거나 같다면,
            break   # 멈추기 (break)

print(array)
