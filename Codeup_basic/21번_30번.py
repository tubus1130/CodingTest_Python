# 21번
s = input()
for i in range(len(s)):
  print(s[i])

# 22번
s = input()
for i in range(len(s)):
  if(i % 2 == 0):
    print(s[i], end = "")
  else:
    print(s[i], end = " ")

# 23번
hour, min, sec = input().split(":")
print(min)

# 24번
a, b = input().split()
print(a+b)

# 25번
a, b = map(int, input().split())
print(a+b)

# 26번
f1 = float(input())
f2 = float(input())
print(f1 + f2)

# 27번
a = int(input())
print("%x"%a)

# 28번
a = int(input())
print("%X"%a)

# 29번
a = int(input(), 16)
print("%o"%a)

# 30번
a = ord(input())
print(a)
