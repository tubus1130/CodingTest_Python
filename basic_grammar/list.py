# 리스트 초기화
a = []
print(a)

a = [1, 2, 3, 4, 5]
print(a)

print(a[4])

a = list()
print(a)

# 크기가 n이고, 모든값이 0인 1차원 리스트 초기화
n = 5
a = [0] * n
print(a)

# 인덱싱
a = [1,2,3,4,5]
print(a[-1])
print(a[-3])

a[3] = 7
print(a)

# 슬라이싱
a = [1,2,3,4,5]
print(a[1:4])

# 리스트 컴프리헨션
array = []
for i in range(10):
  if i % 2 == 1:
    array.append(i)

print(array)

a = [i for i in range(10) if i % 2 == 1]
print(a)

a = [i*i for i in range(1, 5)]
print(a)

# 2차원 배열 초기화
n = 2
m = 3
a = [[0] * m for _ in range(n)]
print(a)

n = 2
m = 3
a = [[0] * m] * n
print(a)

a[1][1] = 1
print(a)

# _언더바의 의미
for i in range(3):
  print(i)

for _ in range(3):
  print("hi")

# 메소드
a = [1,2,3]
a.append(1)
print(a)

a.sort()
print(a)

a.sort(reverse = True)
print(a)

a.reverse()
print(a)

a.insert(2,1)
print(a)

print(a.count(1))

a.remove(1)
print(a)

# 특정값 원소 모두 제거
a = [1,1,2,3,4,5,5]
remove_set = {1,5}
result = [i for i in a if i not in remove_set]
print(result)