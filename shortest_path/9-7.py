# 예제 9-7 : 힙 라이브러리 사용 예제 - 최대 힙

# 기본적으로 파이썬은 최소 힙 제공 O 별도의 최대 힙 제공 X
import heapq

# 내림차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입 <- heapq.heappush() 메소드
    for value in iterable:
        heapq.heappush(h, -value)          # 최대 힙을 이용하기 위해서 데이터를 힙에 넣기 전에 부호를 바꾸어 넣기
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 <- heapq.heappush() 메소드
    for i in range(len(h)):
        result.append(-heapq.heappop(h))   # 최대 힙을 이용하기 위해서 다시 데이터를 꺼낼 때 마찬가지로 부호를 바꾸어 꺼내기
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)