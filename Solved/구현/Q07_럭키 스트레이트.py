# Q07. 럭키 스트레이트
'''
n : 점수
점수기준 반 잘라서 합이 같으면 lucky 다르면 ready출력

정수입력받아서
길이를 기준으로 반이 어딘지 잘라서
합 구한다음 비교
'''

n = input()
length = len(n) // 2
first_sum, last_sum = 0, 0
for i in range(length):
  first_sum += int(n[i])

for i in range(length, len(n)):
  last_sum += int(n[i])

if first_sum == last_sum:
  print("LUCKY")
else:
  print("READY")
