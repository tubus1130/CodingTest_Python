# 02. 배열 제어하기
'''
1. 중복값 제거후 내림차순 정렬 반환
순서대로 데이터읽어서 count가 1이 아니면 remove쓰면될듯?
- 오답

2. 역순정렬후에 현재값 다음값 같으면 현재값 삭제
- 오답

3. 역순정렬후 현재값 다음값 다르면 새로운 리스트에 append
- 정답
'''

def solution(arr):
  arr.sort(reverse=True)
  result = []
  for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
      result.append(arr[i])
  result.append(arr[len(arr)-1])
  return result

# 테스트케이스
print(solution([4,2,2,1,3,4]))
print(solution([2,1,1,3,2,5,4]))

'''
set 함수를 이용해서 중복값 제거 O(N)
'''

# 좋은 정답
def bestSolution(arr):
  result = list(set(arr))
  result.sort(reverse=True)
  return result
