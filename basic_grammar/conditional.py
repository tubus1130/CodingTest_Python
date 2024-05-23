# 조건문
grade = 84
if grade > 80:
  print("pass with nice grade")
elif grade > 60:
  print("pass")
else:
  print("fail")

# 논리 연산자
if True and True:
  print("yes")

if not True or True:
  print("yepp")

# IN, NOT IN
a = [1,2,3]
if 4 in a:
  print("O")
else:
  print("X")

a = "hello"
if "e" in a:
  print("wow")

# pass
if 1 in [1,2,3]:
  pass
else:
  print(1)

# 부등식
x = 3
if 0<x<5:
  print("정답")

if 0<x and x<5:
  print("정답")

# 기타
score = 84
if score > 60: print("합격")
else: print("불합격")

result = "합격" if score>60 else "불합격"
print(result)