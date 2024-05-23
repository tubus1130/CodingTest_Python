# 41번
a, b = map(int, input().split())
print(a%b)

# 42번
a = float(input())
print(round(a, 2))

# 43번
a, b = map(float, input().split())
print("%0.3f" %(a/b))

# 44번
a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%0.2f" %(a/b))

# 45번
a,b,c = map(int, input().split())
sum = a+b+c
print(sum)
print("%0.2f" %(sum/3))

# 46번
a = int(input())
print(2*a)

# 47번
a,b = map(int, input().split())
print(a*2**b)

# 48번
a,b = map(int, input().split())
if a<b:
  print(True)
else:
  print(False)

# 49번
a,b = map(int, input().split())
if a==b:
  print(True)
else:
  print(False)

# 50번
a,b = map(int, input().split())
if b>=a:
  print(True)
else:
  print(False)
