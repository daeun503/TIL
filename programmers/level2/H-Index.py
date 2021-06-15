def solution(citations):
    h = max(citations)
    result = 0
    
    while h > 0:
        cnt = 0
        # 논문 리스트에서 인용횟수가 h보다 크면 + 1
        for i in citations:
            if i >= h:
                cnt += 1
        # 만약 h번 이상 논문이 h편 이상이면 리턴 h
        if cnt >= h:
            return h
        else:
            h -= 1
    return result