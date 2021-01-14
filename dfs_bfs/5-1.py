# 예제 5-1 : 스택 예제

stack = list()   # 스택 자료구조를 이용하기 위해 기본적으로 제공되는 리스트 자료형 이용 가능 O
                 #                         별도의 표준 라이브러리 이용할 필요 X

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)   # append() : 가장 오른쪽에 하나의 원소 삽입 -> 시간복잡도 O(1) 상수시간
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()       # pop()    : 가장 오른쪽에서 하나의 원소 꺼냄 -> 시간복잡도 O(1) 상수시간
stack.append(1)
stack.append(4)
stack.pop()

print(stack)         # 최하단 원소부터 출력 (그대로) <- 가장 먼저 들어온 원소부터
print(stack[::-1])   # 최상단 원소부터 출력 (거꾸로) <- 가장 먼저 나가고자 하는 원소부터