# 힙으로 구현
import heapq

def solution(operations):
    hq = []
    for op in operations:
        if op[0] == 'I':
            heapq.heappush(hq, int(op[2:]))
        elif hq:
            # 최솟값 삭제
            if op == 'D -1':
                heapq.heappop(hq)
            # 최댓값 삭제
            elif op == 'D 1':
                # max heap으로 바꿔주기(??)
                for i in range(len(hq)):
                    hq[i] = -hq[i]
                heapq.heapify(hq)
                # 최댓값 삭제
                heapq.heappop(hq)
                # min heap으로 바꿔주기(???)
                for i in range(len(hq)):
                    hq[i] = -hq[i]
                heapq.heapify(hq)

    return [max(hq), min(hq)] if hq else [0, 0]

# 그냥 리스트로 구현
def solution(operations):
    tmp = []
    for op in operations:
        if op[0] == 'I':
            tmp.append(int(op[2:]))
        elif tmp:
            if op[2:] == '-1': tmp.remove(min(tmp))  # 최솟값 제거
            elif op[2:] == '1': tmp.remove(max(tmp)) # 최댓값 제거
    return [max(tmp), min(tmp)] if tmp else [0, 0]