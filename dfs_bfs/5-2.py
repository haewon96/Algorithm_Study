# 예제 5-2 : 큐 예제

from collections import deque   # 큐 자료구조를 이용하게 위해 deque 라이브러리 사용
                                # 스택과 큐 자료구조의 장점을 합친 것

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()   # deque 객체 생성

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)   # append() : 가장 오른쪽에 위치한 하나의 원소 넣기 -> 시간복잡도 O(1) 상수시간
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()   # popleft() : 가장 왼쪽에 위치한 하나의 원소 빼기 -> 시간복잡도 O(1) 상수시간
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)   # 먼저 들어온 순서대로 출력

queue.reverse()   # 다음 출력을 위해 역순으로 바꾸기 <- 그려지는 형태는 그림과 반대방향
                  # 실제 구현상으로는 데이터가 오른쪽으로 들어와서 왼쪽으로 나감
print(queue)   # 나중에 들어온 원소부터 출력
