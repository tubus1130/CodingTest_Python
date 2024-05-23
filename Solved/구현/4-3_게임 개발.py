# 4-3 개임 개발
'''
가로 m
세로 n
m*n

캐릭터 좌표 a,b
바라보는방향 d[0, 1, 2, 3] : 북동남서 -> 리스트로구현

현재방향 look

1. 2차원배열 생성
while true:
  움직임 반복수행
  if 방향:
    북쪽이면 (a-1,b)가 0이면 이동
  else:
    1이면 look = d[look+1]
'''

n,m = map(int,input().split())

# 방문위치 저장
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재좌표 방문완료

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)
