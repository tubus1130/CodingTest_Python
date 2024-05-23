'''
2/n 까지만 반복문을 돌리는 이유는 반 이상으로 나눌경우 의미가 없기 때문에 => 어차피 압축이안됨(최소 같은게 2개는 있어야하는데 안됨)

'''
def solution(s):
    answer = len(s) # 반복문을 도는동안 최소값이 나오지않는다면 전체의 길이가 최소
    # step은 압축단위 1개, 2개, ...    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에문자
        count = 1

        # step(압축단위)만큼 증가시키면서 비교
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1 # 같다면
            else:
                # 압축된게 하나라도 있다면 2a이런식으로 넣고 아니면 걍 a 만 넣는다
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 비교문자 바꿔주기
                count = 1
                
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

  
    return answer
