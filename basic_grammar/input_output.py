# 입력
'''
a = list(map(int, input().split()))
print(a)

a,b,c = map(int, input().split())
print(a,b,c)

n = str(input())
print(n)

n = int(input())
print(n)


import sys

data = sys.stdin.readline().rstrip()
print(data)
'''

# 출력
a = 1
b = 2
print(a, b)
print(3, end=" ")
print(4, end=" ")
c = 5
print("난" + str(c) + "시가 좋다")

# f-string
a = 7
print(f"난 내일 {a}시에 일어날거야")