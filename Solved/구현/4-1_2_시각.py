# 4-1-2 시각
'''
00시 00분 00초
n시 00분 00초

n = 1분에 3이 몇개?
03
13
23
30 ~ 39
43
53

1분 : 15개
2분 : 15개
3분 : 60개

3중포문?
'''
hour = int(input())
cnt = 0

for h in range(hour+1):
  for m in range(60):
    for s in range(60):
      if "3" in str(h) or "3" in str(m) or "3" in str(s):
        cnt += 1

print(cnt)
