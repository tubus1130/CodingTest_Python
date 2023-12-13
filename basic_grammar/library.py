# 내장함수

result = sum([1,2,3])
print(result)

result = min([1,2,3])
print(result)

result = max([1,2,3])
print(result)

result = eval("(7*6)+1")
print(result)

result = sorted([4,1,2,7,3])
print(result)

result = sorted([4,1,2,7,3], reverse=True)
print(result)

result = sorted([('김', 84), ('박', 75), ('신', 79)], key = lambda x:x[1], reverse=True)
print(result)

data = [3,2,5,1,6]
data.sort()
print(data)

# itertools
from itertools import permutations
data = ['A', 'B', 'C']
result =  list(permutations(data, 2))
print(result)

from itertools import combinations
result = list(combinations(data, 2))
print(result)

from itertools import product
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)

# heapq
import heapq

def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, value)
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1,5,4,6,2,3,8,7,9])
print(result)

# bisect
from bisect import bisect_left, bisect_right

a = [1,2,4,4,7]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

# deque(큐 구현)
from collections import deque
data = deque([1, 2, 3])
data.append(5)
data.popleft()
print(list(data))

# deque(스택 구현)
data = deque([1,2,3])
data.append(4)
data.pop()
print(list(data))

# math
import math
print(math.factorial(5))
print(math.sqrt(9))
print(math.gcd(21, 14))

def lcm(a,b):
  return a*b // math.gcd(a,b)

print(lcm(21, 14))