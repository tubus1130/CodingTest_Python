# 15. 요세푸스 문제
'''
popleft, append 반복하면서
개수에 맞으면 append안함
'''
n = 5
k = 2
from collections import deque
deque = deque()

for i in range(1, n+1):
  deque.append(i)

while len(deque) != 1:
  for _ in range(k-1):
    deque.append(deque.popleft())
    print(deque)
  deque.popleft()
print(deque.popleft())
