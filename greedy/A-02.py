# 기출문제 A02 : 곱하기 혹은 더하기
"""
# num = input()
# number = [n for n in num]

number = str(input())
result = list()

for n in number:
    if n == '0':
        result.append(n + '+')
    else:
        result.append(n + '*')

print(result)
"""



data = input()   # 숫자로만 구성된 문자열 입력

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):   # 두 번째 숫자부터 차례대로 확인 -> 매번 result 변수값과 새로운 값 사이의 연산 수행
    # 두 수 중에서 하나라도 '0' 또는 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)