# 31번
a = int(input())
print(chr(a))

# 32번
a = int(input())
print(str(-a))

# 33번
a = ord(input())
print(chr(a+1))

# 34번
a, b = map(int, input().split())
print(a - b)

# 35번
a, b = map(float, input().split())
print(a * b)

# 36번
str, cnt = input().split()
for _ in range(int(cnt)):
  print(str, end='')

# 37번
cnt = int(input())
str = input()
for _ in range(cnt):
  print(str, end="")

# 38번
a, b = map(int, input().split())
print(a**b)

# 39번
a, b = map(float, input().split())
print(a**b)

# 40번
a, b = map(int, input().split())
print(a//b)
