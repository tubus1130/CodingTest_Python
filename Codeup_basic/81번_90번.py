# 81번
num = int(input(), 16)
for i in range(1, 16):
  print("%X"%num, "*%X"%i, "=%X"%(num*i), sep="")

# 82번
num = int(input())
for i in range(1, num+1):
  if "3" in str(i) or "6" in str(i) or "9" in str(i):
    print("X", end=" ")
  else:
    print(i, end=" ")

# 83번
r,g,b = map(int, input().split())
cnt = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i,j,k)
      cnt+=1

print(cnt)

# 84번
h,b,c,s = map(int, input().split())
print("%.1f"%(h*b*c*s/8/1024/1024) + " MB")

# 85번
w,h,b = map(int, input().split())
print("%.2f"%(w*h*b/8/1024/1024) + " MB")

# 86번
num = int(input())
sum = 0
cnt = 1
while True:
  sum += cnt
  cnt+=1
  if sum >= num:
    print(sum)
    break

# 87번
num = int(input())
for i in range(1, num+1):
  if i%3==0:
    pass
  else:
    print(i, end=" ")

# 88번
a,d,n = map(int, input().split())
print(a+(n-1)*d)

# 89번
a,r,n = map(int, input().split())
print(a*r**(n-1))

# 90번
a,m,d,n = map(int, input().split())
for _ in range(n-1):
  a*=m
  a+=d

print(a)
