# 3-1 거스름돈

N = int(input()) # 거슬러 줘야할 돈
cnt = 0
coin = [500, 100, 50, 10]
for i in coin:
  cnt += N//i
  N %= i

print(cnt)
