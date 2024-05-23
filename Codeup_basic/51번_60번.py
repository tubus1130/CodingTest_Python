# 51번
a, b = map(int, input().split())
if a != b:
  print(True)
else:
  print(False)

# 52번
a = int(input())
if a==0:
  print(False)
else:
  print(True)

# 53번
a = int(input())
if bool(a) == False:
  print(True)
else:
  print(False)

# 54번
a,b = map(int, input().split())
if bool(a) == True and bool(b) == True:
  print(True)
else:
  print(False)

# 55번
a,b = map(int, input().split())
if bool(a) == True or bool(b) == True:
  print(True)
else:
  print(False)

# 56번
a,b = map(int, input().split())
if bool(a) != bool(b):
  print(True)
else:
  print(False)

# 57번
a,b = map(int, input().split())
if bool(a) == bool(b):
  print(True)
else:
  print(False)

# 58번
a,b = map(int, input().split())
if bool(a) == False and bool(b) == False:
  print(True)
else:
  print(False)

# 59번
a = int(input())
print(~a)

# 60번
a,b = map(int, input().split())
print(a&b)
