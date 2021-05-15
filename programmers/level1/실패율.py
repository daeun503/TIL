def solution(N, stages):
    # N번째 스테이지까지 클리어한 사람이 있는지, 있다면 그만큼 수 누적
    user = stages.count(N+1) if N+1 in stages else 0
    stage_fail = []
    
    for i in range(N, 0, -1):
        user += stages.count(i)     # i번 스테이지에 있는 사람 count해서 누적시켜주기
        if user == 0:               # 만약에 user 수가 0 이라면 실패율 0 예외처리
            stage_fail += [(i, 0)]
        else:                       # 실패율 = 해당 스테이지에서 막힌 사람 / 거기까지 간 사람 
            stage_fail += [(i, stages.count(i) / user)]
    
    # stage_fail 형태 : [(스테이지, 실패율)] 이므로 실패율을 기준으로 sort (오름차순)
    stage_fail.sort(key=lambda x: x[1])
    # 내림차순으로 바꿔주기 위해 reverse
    return list(reversed([x for x, y in stage_fail]))