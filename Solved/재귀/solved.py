# 문제1. 자연수 더하기

def solution1(n):
  if n == 1:
    return 1
  return n + solution1(n-1)

print(solution1(5))

# 문제2. 거듭제곱 계산
def solution2(base, exponent):
  if exponent == 0:
    return 1
  return base * solution2(base, exponent-1)

print(solution2(2, 3))

# 문제3. 문자열 뒤집기
def solution3(s):
  if len(s) == 1:
    return s
  return s[-1] + solution3(s[:-1])

print(solution3("hello"))
