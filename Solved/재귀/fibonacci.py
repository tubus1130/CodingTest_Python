# 실전1-1. 피보나치
'''
1 1 2 3 5 8
f(n) = f(n-1) + f(n-2)
'''
def fibonacci_for(n):
  a, b = 1, 1
  for i in range(n-2):
    a, b = b, a+b
  return b

print(fibonacci_for(6))

def fibonacci_recur(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci_recur(n-1) + fibonacci_recur(n-2)

print(fibonacci_recur(6))

# 실전1-2. 피보나치 재귀연산횟수
'''
3 -> f(1), f(2) 2
4 -> f(3), f(2) 3
5 -> f(4), f(3) 5
연산횟수는 피보나치처럼 늘어남 2^n같은 느낌?
호출해야하는 함수가 계속 쌓여서 recursion depth가 어마어마하게늘어남
줄이는법은 반복문활용?
'''
