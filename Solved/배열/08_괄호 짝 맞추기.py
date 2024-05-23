'''
괄호 개수

입력개수동안
( 들어오면 append
) 들어오면 pop
체크사항 : pop인데 스택이 0 이라면 false하고 break

다끝나고 스택이 비어있으면 true 아니면 false

'''
# 05. 괄호 짝 맞추기

s = input()

stack = []
cnt = 0
for i in s:
  if i =='(':
    stack.append('(')
  else:
    if len(stack) == 0:
      break
    else:
      stack.pop()
  cnt+=1

if len(stack) == 0 and cnt == len(s):
  print("True")
else:
  print("False")
