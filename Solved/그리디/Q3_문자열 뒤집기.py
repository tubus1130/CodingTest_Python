#3. 문자열 뒤집기
'''
카운트해서 
0에서 1로갈때
1에서 0으로갈떄

list = [0, 0]
0카운트
1카운트
'''

s = input()
cnt = [0, 0]
cnt[int(s[0])] += 1
before = int(s[0])
for i in range(1, len(s)):
  if before != int(s[i]):
    cnt[int(s[i])] += 1
  before = int(s[i])

print(min(cnt))
