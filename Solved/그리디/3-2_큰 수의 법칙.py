# 3-2 큰 수의 법칙

n, m, k = map(int, input().split())
list = list(map(int, input().split()))

list.sort()
answer = list[n-1]

for i in range(1, m):
  if i % k == 0:
    answer += list[n-2]
  else:
    answer += list[n-1]

print(answer)
