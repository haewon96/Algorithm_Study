# 기출문제 A08 : 문자열 재정렬

string = input()
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha = list()
num = list()

for s in string:
    if s in number:
        num.append(int(s))
    else:
        alpha.append(s)

result_num = 0
for n in num:
    result_num += n

result_alpha = ''
for a in sorted(alpha):
    result_alpha += a

print(result_alpha + str(result_num))



"""
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)

    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))   # 공백 없이 리스트에 포함된 모든 문자열 출력

       # join()  : 문자열 합치기 - 특정 구분자를 포함해 문자열로 변환해주는 함수
       #           -> 구분자.join(리스트) 
       # split() : 문자열 나누기 - 특정 구분자를 기준으로 나누어 리스트로 변환해주는 함수
       #           -> 문자열.split(구분자)
"""

