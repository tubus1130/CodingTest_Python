# 4-1. 상하좌우

'''
n = 공간의 크기(n * n)

L R U D
리스트에 넣고 for문
if
L : y좌표가 1이면 무시 아니면 y-=1
R : y좌표가 n이면 무시 아니면 y+=1
U : x좌표가 1이면 무시 아니면 x-=1
D : x좌표가 n이면 무시 아니면 x+=1
'''

n = int(input())
move_list = list(map(str, input().split()))
x,y = 1,1

for move in move_list:
  if move == "L":
    if y == 1:
      continue
    else:
      y -= 1
  elif move == "R":
    if y == n:
      continue
    else:
      y += 1
  elif move == "U":
    if x == 1:
      continue
    else:
      x -= 1
  elif move == "D":
    if x == n:
      continue
    else:
      x += 1

print(x,y)
