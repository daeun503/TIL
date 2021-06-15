"""
원형 큐로 구현

문제3. 고정 배열 크기의 Queue 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

# Queue의 사이즈 지정 - createQueue
# 고정 크기의 배열로 Queue를 생성하는 것이 상대적으로 가변 배열(리스트)보다 빠르다.
SIZE = 4
Q = [0] * SIZE

# 초기 상태의 표현
front, rear = 0, 0

# isFull
def is_full():
    global front, rear
    return (rear + 1) % len(Q) == front

# isEmpty
def is_empty():
    global front, rear
    return rear == front

# enQueue
def enqueue(item):
    global rear
    if is_full() : print("Queue is full!")
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

# deQueue
def dequeue():
    global front
    if is_empty() : print("Queue is empty!")
    else:
        front = (front + 1) % len(Q)
        return Q[front]

# Qpeek
def Qpeek():
    global front, rear
    if is_empty(): print("Queue is empty!")
    else:
        return Q[(front + 1) % len(Q)]


#1. Queue 초기화 상태 확인
print(Q)

#2. Queue가 비었는지 확인
print(is_empty()) # True

#3. enQueue 작업 & 확인
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4) # Queue is full!
enqueue(5) # Queue is full!

print(Q)

#4. Qpeek
print(Qpeek())

#5. deQueue 작업 & 확인
print(dequeue()) # 1
print(dequeue()) # 2
print(dequeue()) # 3
print(dequeue()) # Queue is empty!
print(dequeue()) # Queue is empty!