# 61번
a,b = map(int, input().split())
print(a|b)

# 62번
a,b = map(int, input().split())
print(a^b)

# 63번
a,b = map(int, input().split())
if a>b:
  print(a)
else:
  print(b)

# 64번
a,b,c = map(int, input().split())
result = a
if(b<result):
  result = b
if(c<result):
  result = c
print(result)

# 65번
list = list(map(int, input().split()))
for i in list:
  if i%2==0:
    print(i)

# 66번
list = list(map(int, input().split()))
for i in list:
  if i%2==1:
    print("odd")
  else:
    print("even")

# 67번
a = int(input())
if a<0:
  if a%2==0:
    print("A")
  else:
    print("B")
else:
  if a%2==0:
    print("C")
  else:
    print("D")

# 68번
score = int(input())
if score>=90:
  print("A")
elif score>=70:
  print("B")
elif score>=40:
  print("C")
else:
  print("D")

# 69번
a = input()
if a=="A":
  print("best!!!")
elif a=="B":
  print("good!!")
elif a=="C":
  print("run!")
elif a=="D":
  print("slowly~")
else:
  print("what?")


# 70번
month = int(input())
if month // 3 == 1:
  print("spring")
elif month // 3 == 2:
  print("summer")
elif month // 3 == 3:
  print("fall")
else:
  print("winter")
