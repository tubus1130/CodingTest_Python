# 양의정수
a = 1130
print(a)

# 음의정수
a = -57
print(a)

# 0
a = 0
print(a)

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -234.54
print(a)

# 소수부가 0일때 0 생략
a = 11.
print(a)

# 정수부가 0일때 0생략
a = -.78
print(a)

# 10억의 지수 표현방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# 실수의 오차
a = 0.3 + 0.6
print(a)
if a == 0.9:
  print(True)
else:
  print(False)

# Round함수를 활용한 실수오차 줄이기
a = round(a, 4)
print(a)
if a == 0.9:
  print(True)
else:
  print(False)

# 수 자료형 연산
a = 5
b = 3
print(a / b)
print(a % b)
print(a // b)
print(a**b)
