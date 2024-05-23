# 4-2 왕실의 나이트
'''
8*8

입력 a1

x = 1
y = a

8가지방법
우2, 상1
우1, 상2
좌2, 상1
좌1, 상2
우2, 하1
우1, 하2
좌2, 하1
좌1, 하2

ord("input")-96 = 1

'''

steps = [(-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, 2), (2,1), (1, -2), (2, -1)]

now = str(input())
y = int(ord(now[0]) - 96)
x = int(now[1])
cnt = 0

for step in steps:
  nx = x + step[0]
  ny = y + step[1]
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  cnt+=1

print(cnt)
