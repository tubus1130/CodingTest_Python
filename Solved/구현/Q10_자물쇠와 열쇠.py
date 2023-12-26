# Q10. 자물쇠와 열쇠
'''
자물쇠 n*n lock
열쇠 m*m key

열쇠 회전, 이동가능
열쇠 돌기 -> 자물쇠 홈
열쇠 돌기, 자물쇠돌기 만나면안됨
자물쇠의 모든 홈을 채워야함
홈 0, 돌기 1

키
0 0 0
1 0 0 
0 1 1

자물쇠
1 1 1
1 1 0
1 0 1

자물쇠 크기 조정!!!
'''
# 2차원 리스트 90도 회전(시계방향)
def rotate(a):
  n = len(a)
  m = len(a[0])
  result = [[0]*n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]

  return result

# 자물쇠의 중간부분이 모두 1인지 확인
def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length*2):
    for j in range(lock_length, lock_length*2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)

  # 3배크기의 새로운 lock배열 생성
  new_lock = [[0] * (n*3) for _ in range(n*3)]서
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]

  
  for rotation in range(4):
    key = rotate(key)
    for x in range(n*2): # 2*n + m 하면 전체 탐새가능
      for y in range(n*2):
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] += key[i][j]
        if check(new_lock) == True:
          return True

        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]

  return False
