# recursion 재귀
'''
1. 더 간단히, 더 작게
2. base case(종료조건) 설정
'''

# factorial
def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)

print(factorial(3)) # 6

# hanoi 하노이탑
def hanoi(_from, _by, _to, cnt):
  if cnt == 1:
    print(f"{_from}->{_to}")
    return
  hanoi(_from, _to, _by, cnt-1)
  print(f"{_from}->{_to}")
  hanoi(_by, _from, _to, cnt-1)

hanoi(1,2,3,3)
'''
1->3
1->2
3->2
1->3
2->1
2->3
1->3
'''
