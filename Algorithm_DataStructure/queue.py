# 1. 자료구조 개념:
#    큐는 데이터의 삽입이 한 쪽 끝에서 이루어지고 삭제는 반대 쪽 끝에서 이루어지는 선형 자료구조이다. 
#    이러한 특성 때문에 First In First Out (FIFO) 자료구조라고도 불린다. 
#    여기서는 deque라는 Python 라이브러리를 사용하여 큐를 구현하였다.

# 2. 예시 입력 / 출력:
#    입력: [1, 2, 3, 4, 5] (순차적으로 큐에 enqueue)
#    출력: 1 2 3 4 5 (순차적으로 큐에서 dequeue)

# 3. 자료구조의 시간 복잡도:
#    큐의 주요 연산인 enqueue와 dequeue 모두 O(1)의 시간 복잡도를 가진다. 
#    이는 각 연산이 상수 시간에 수행됨을 의미한다.

# 4. 해당 자료구조로 풀 수 있는 문제 예시:
#    - 너비 우선 탐색 (BFS) 구현
#    - 대기열 (Waiting Line) 문제 해결
#    - CPU 스케줄링 등

# 5. 상세 과정:
#    - 먼저 deque 라이브러리를 사용하여 큐 객체를 초기화한다.
#    - append() 메서드를 사용하여 요소를 큐에 삽입한다.
#    - popleft() 메서드를 사용하여 큐의 맨 앞 요소를 제거하고 반환한다.

from collections import deque

# 큐 객체 초기화
queue = deque()

# 요소들을 큐에 삽입 (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# 큐에서 요소들을 제거 (dequeue)하면서 출력
while queue:
    print(queue.popleft())  # 출력: 1, 2, 3, 4, 5 (FIFO 순서)
