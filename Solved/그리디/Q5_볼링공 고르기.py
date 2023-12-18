#5. 볼링공 고르기
'''
두 사람은 서로 무게가 다른 볼링공을 고르려고 한다

n = 5, m = 3
1 3 2 3 2

1 2 2 3 3

1 2 3

12 : 2개 1*2
13 : 2개 1*2
23 : 4개 2*2

1 2 13
1 3 12
1 4 13
1 5 12
2 3 32
2 5 32
3 4 23
4 5 32

0 ~ m까지의 배열
[1, 2, 3, ..., m]
개수대로 +=1
[1, 2, 2]
이중 for문으로 조합구하면될듯?
'''

n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt = [0 for _ in range(m+1)]
total = 0
for i in data:
  cnt[i] += 1

for i in range(1, len(cnt)):
  for j in range(i+1, len(cnt)):
    total += cnt[i]*cnt[j]

print(total)
