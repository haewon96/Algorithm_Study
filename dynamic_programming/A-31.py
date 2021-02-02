# 기출문제 A31 : 금광

n, m = map(int, input().split())
array = list(map(int, input().split()))
gold_mine = []

for i in range(n):
    gold_mine.append(array[i * m : (i * m) + m])

"""
for i in range(n):
    for j in range(m):
        print('d[', i, '][', j, '] = ', gold_mine[i][j])
print(gold_mine)
# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
"""


