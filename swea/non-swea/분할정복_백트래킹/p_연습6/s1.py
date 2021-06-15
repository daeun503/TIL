"""
연습 문제6. 힙 구현
 - 최소힙이 유지될 수 있도록 삽입 & 삭제 연산 함수를 구현하시오.
 - 완전 이진 트리의 조건에 위배되지 않도록 연산 수행을 수행하시오.
"""

#1. 삽입 연산
"""
1) Tree의 가장 마지막에 요소 삽입
2) 삽입된 노드와 부모 노드를 비교하여 swap
3) 부모 노드보다 크거나/작거고 and root에 도달하기 전까지 반복
"""
def heap_push(value):
    # value -> node의 값 / heap_count -> node의 index
    global heap_count

    heap_count += 1

    # child & parent (parent = child // 2)
    c = heap_count
    p = c // 2
    heap[c] = value
    while heap[c] < heap[p]:
        heap[c], heap[p] = heap[p], heap[c]
        c = p
        p = c // 2

    return heap


#2. 삭제 연산
"""
1) 루트 노드의 원소 삭제
2) 마지막 노드 삭제 후 루트 노드에 삽입 (heap의 모양 유지)
3) (자리가 확정될 때까지) 부모 & 자식 비교하며 swap 
"""
def heap_pop():
    global heap_count

    result = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    heap_count -= 1

    # 부모와 자식
    p = 1
    c = p * 2
    # 오른쪽 자식이 존재하고, 오른쪽이 더 작으면 오른쪽과 비교
    if c+1 <= heap_count and heap[c] > heap[c+1]:
        c += 1

    # 자식이 존재하고 부모가 자식보다 크면 바꾸기
    while c <= heap_count and heap[p] > heap[c] :
        heap[p], heap[c] = heap[c], heap[p]
        # 부모와 자식
        p = c
        c = p * 2
        # 오른쪽 자식이 존재하고, 오른쪽이 더 작으면 오른쪽과 비교
        if c + 1 <= heap_count and heap[c] > heap[c + 1]:
            c += 1

    return result

heap_count = 0
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N+1)

# 삽입
for i in range(N):
    heap_push(temp[i])

print(*heap) # 0 2 3 5 7 4 6

# 삭제
for i in range(N):
    print(heap_pop(), end=' ') # 2 3 4 5 6 7