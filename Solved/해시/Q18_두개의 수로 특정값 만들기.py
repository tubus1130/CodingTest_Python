# 18. 두개의 수로 특정값 만들기
'''
2중포문

'''

# 계수정렬로 해시테이블 생
def count_sort(arr, k):
  hashtable = [0] * (k+1)

  for num in arr:
    if num <= k:
      hashtable[num] = 1
  return hashtable

def solution(arr, target):
  hashtable = count_sort(arr, target)

  for num in arr:
    complement = target - num
    if (complement != num and complement >= 0 and complement <= target and hashtable[complement] == 1):
      return True
  return False


print(solution([1,2,3,4,8], 6))
