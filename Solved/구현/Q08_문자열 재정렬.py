# Q08. 문자열 재정렬
'''
s입력받기
문자열 리스트
숫자 별개로 더하기
if 지금인덱스가 65이상이면
  문자열리스트에 append
else
  sum에 더하기

문자열리스트 오름차순 정렬후 출력하고 sum 출력
'''

s = input()
list = []
sum = 0

for i in range(len(s)):
  if int(ord(s[i])) >= 65:
    list.append(s[i])
  else:
    sum += int(s[i])

list.sort()
for str in list:
  print(str, end='')
print(sum)
