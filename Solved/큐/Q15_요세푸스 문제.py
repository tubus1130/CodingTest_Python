# 15. 요세푸스 문제
'''
popleft, append 반복하면서
개수에 맞으면 append안함
'''
n = 5
k = 2
from collections import deque
queue = deque()

for i in range(1, n+1):
  queue.append(i)

while len(queue) != 1:
  for _ in range(k-1):
    queue.append(queue.popleft())
  queue.popleft()
print(queue.popleft())
