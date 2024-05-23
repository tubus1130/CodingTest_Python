'''
10 -> 1010
0이될때까지 2로나눈 나머지를 스택에 넣고
다 pop하면될듯?
'''
# 09. 10진수를 2진수로 변환하기

def solution(n):
  stack = []
  while n !=0:
    stack.append(n%2)
    n //= 2
  
  result = 0
  while stack:
    result *= 10
    result += stack.pop()
  return result

print(solution(10))
print(solution(27))
print(solution(12345))
