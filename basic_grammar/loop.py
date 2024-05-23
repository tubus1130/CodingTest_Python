# while
i = 1
result = 0
while i < 10:
  result += i
  i += 1

print(result)

# for
result = 0
for i in range(1, 10):
  result += i

print(result)

# continue
scores = [90, 84, 72, 57]
cheat_list = {2, 4}

for i in range(4):
  if i+1 in cheat_list:
    continue
  print(str(i+1) + "번째 학생은 합격")

# break
i = 1
while True:
  print(i)
  if i == 5:
    break
  i+=1

# 중첩 반복문
for i in range(2, 10):
  for j in range(1, 10):
    print(str(i) + " * " + str(j) + " = " + str(i*j))
  print()