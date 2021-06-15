import heapq

def solution(scoville, K):
    # 모든 음식의 스코빌 지수가 k 이상 => min이 k 이상
    # 아니라면 min (최소) remove하고 min (두번째)
    
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K :
        if len(scoville) <= 1:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        result = min1 + min2 *2
        heapq.heappush(scoville, result)
        answer += 1
    
    return answer