def solution(brackets:str)->bool:
  stack = []
  temp = ""
  for i in brackets:
    if i == '(' or i == '{' or i == '[':
      stack.append(i)
    else:
      temp = stack.pop()
    if i == ')' and temp != '(':
      return False
    if i == '}' and temp != '{':
      return False
    if i == ']' and temp != '[':
      return False
  if stack:
    return False
  else:
    return True
print(solution("(())")) # True
print(solution("{}[(]")) # False
