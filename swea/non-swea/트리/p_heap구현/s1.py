#1. 최소힙 직접 구현

# 삽입
"""
1) heap 가장 마지막에 원소 삽입
2) 부모 & 자식 비교하며 swap
"""
def heap_push(value):
    # value -> node의 값 / heap_count -> node의 index
    global heap_count

    # child & parent (parent = child // 2)
    heap_count += 1
    heap[heap_count] = value
    c = heap_count
    while heap[c] < heap[c//2]:
        heap[c], heap[c//2] = heap[c//2], heap[c]
        c //= 2


# 삭제
"""
1) 루트 노드의 원소 삭제
2) 마지막 노드 삭제 후 루트 노드에 삽입 (heap의 모양 유지)
3) (자리가 확정될 때까지) 부모 & 자식 비교하며 swap 
"""
def heap_pop():
    global heap_count
    result = heap[1]
    heap[1] = heap[heap_count]
    heap_count -= 1
    p = 1
    while 2*p+1 <= heap_count:
        if heap[2*p] < heap[2*p+1] and heap[p] > heap[2*p]:
            heap[p], heap[2*p] = heap[2*p], heap[p]
            p = 2*p
        elif heap[2*p] > heap[2*p+1] and heap[p] > heap[2*p+1]:
            heap[p], heap[2*p+1] = heap[2*p+1], heap[p]
            p = 2*p+1
    if heap_count == 2 and heap[1] > heap[2]:
        heap[1], heap[2] = heap[2], heap[1]
    return result


heap_count = 0
temp = [7, 2, 5, 3, 4, 6]
temp = [9, 8, 7, 6, 5, 4]
N = len(temp)
heap = [0] * (N+1)

##########################################################

# 삽입 연산
for i in range(N):
    heap_push(temp[i])

print(*heap) # 0 2 3 5 7 4 6

# 삭제 연산
for i in range(N):
    print(heap_pop(), end=' ') # 2 3 4 5 6 7