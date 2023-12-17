# 91번
a,b,c = map(int, input().split())
target = a
while True:
  if target%a==0 and target%b==0 and target%c==0:
    print(target)
    break
  target+=1

# 92번
n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

d = []
for i in range(24):
  d.append(0)

for i in range(n):
  d[a[i]] += 1

for i in range(1, 24):
  print(d[i], end=" ")

# 93번
n = int(input())
list = list(map(int, input().split()))
for i in range(n):
  print(list[n-i-1], end=" ")

# 94번
n = int(input())
list = list(map(int, input().split()))
min = list[0]
for i in range(n):
  if min > list[i]:
    min = list[i]

print(min)

# 95번
list = [[0 for _ in range(20)] for _ in range(20)]
num = int(input())
for _ in range(num):
  x,y = map(int, input().split())
  list[x][y] = 1

for i in range(1, 20):
  for j in range(1,20):
    print(list[i][j], end=" ")
  print()
