#2. 곱하기 혹은 더하기
s = input()
result = int(s[0])
for i in range(1, len(s)):
  value = int(s[i])
  if value <= 1 or result <=1:
    result += value
  else:
    result *= value

print(result)
