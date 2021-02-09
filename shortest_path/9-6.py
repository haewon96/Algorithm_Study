# 예제 9-6 : 힙 라이브러리 사용 예제 - 최소 힙

# 기본적으로 파이썬은 힙 라이브러리를 그대로 사용하면 최소 힙 (Min Heap) 방식으로 구현되어 있어 우선순위가 낮은 원소부터 차례대로 꺼내짐 (오름차순)
import heapq   # 힙 라이브러리 불러오기 -> 데이터를 꺼낼 때 우선순위가 높은 데이터부터 차례대로 나오는 자료구조의 특성을 이용하여 정렬 수행

# 오름차순 힙 정렬 (Heap Sort)
def heapsort(iterable):   # 리스트나 튜플과 같은 iterable한 객체
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입 <- heapq.heappush() 메소드
    for value in iterable:
        heapq.heappush(h, value)   # 힙 라이브러리에 구현되어 있는 메소드 이용하여 특정 리스트에 데이터 넣기
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 result 리스트에 담기 <- heapq.heappop() 메소드
    for i in range(len(h)):
        result.append(heapq.heappop(h))   # 힙 라이브러리에 구현되어 있는 메소드 이용하여 특정 리스트에 데이터 꺼내기
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
