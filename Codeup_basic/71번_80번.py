# 71번
from sre_constants import CATEGORY_NOT_SPACE


while True:
  num = int(input())
  if num == 0:
    break
  else:
    print(num)

# 72번
num = int(input())
while num!=0:
  print(num)
  num-=1

# 73번
num = int(input())
while num!=0:
  num -= 1
  print(num)

# 74번
ch = input()
target = "a"
while target!=ch:
  print(target, end=' ')
  target = chr(ord(target) + 1)
print(target)

# 75번
num = int(input())
for i in range(num):
  print(i)
print(num)

# 76번
num = int(input())
for i in range(num):
  print(i)
print(num)

# 77번
num = int(input())
result = 0
for i in range(1, num+1):
  if i%2==0:
    result += i
print(result)

# 78번
while True:
  ch = input()
  print(ch)
  if ch == "q":
    break

# 79번
num = int(input())
result = 0
cnt = 1
while True:
  result += cnt
  if num <= result:
    print(cnt)
    break
  cnt+=1

# 80번
n,m = map(int, input().split())
for i in range(1, n+1):
  for j in range(1, m+1):
    print(i, j)
