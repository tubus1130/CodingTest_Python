# 3-3 숫자 카드 게임

n,m = map(int, input().split())
data = []

for _ in range(n):
  temp_list = list(map(int, input().split()))
  temp_list.sort()
  data.append(temp_list[0])

data.sort()
print(data[n-1])
