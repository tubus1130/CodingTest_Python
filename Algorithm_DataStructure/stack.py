# 1. 자료구조 개념:
#    스택(Stack)은 선입후출(FILO, First In Last Out) 원칙에 따라 작동하는 자료구조입니다. 
#    새로운 요소는 스택의 상단에 추가되고, 상단의 요소만이 삭제될 수 있습니다.

# 2. 예시 입력 / 출력:
#    입력: [1, 2, 3, 4]
#    출력: [1, 2, 3] (4를 pop한 결과)

# 3. 자료구조의 시간 복잡도:
#    - Push: O(1)
#    - Pop: O(1)
#    - Top: O(1)

# 4. 해당 자료구조로 풀 수 있는 문제 예시:
#    - 괄호 짝 맞추기
#    - 브라우저 뒤로 가기 기능
#    - 트리의 깊이 우선 탐색(DFS)

# 5. 상세과정:
#    - 스택 생성: 리스트를 초기화하여 스택으로 사용
#    - Push: 리스트의 append 메소드를 사용하여 요소를 스택의 맨 위에 추가
#    - Pop: 리스트의 pop 메소드를 사용하여 스택의 맨 위 요소를 삭제하고 반환
#    - Top: 리스트의 마지막 요소를 참조하여 스택의 맨 위 요소를 확인

# 스택 생성
stack = []

# Push 연산: 요소를 스택의 맨 위에 추가
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)  # 출력: [1, 2, 3, 4]

# Top 연산: 스택의 맨 위 요소 확인
print(stack[-1])  # 출력: 4

# Pop 연산: 스택의 맨 위 요소 삭제 및 반환
stack.pop()
print(stack)  # 출력: [1, 2, 3]
