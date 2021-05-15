def solution(n, lost, reserve):
    answer = 0
    count = 0
    
    # 여벌 가져왔는데 잃어버린 사람 제외해주기 위해 차집합
    # 찐으로 빌려줄 수 있는 사람(real_reserve) 찐으로 잃어버린 사람(real_lost)
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    
    for j in range(len(real_lost)):
        # 잃어버린 사람의 앞 번호가 빌려줄 수 있는 사람 안에 있으면 빌려준 사람 제거 후 카운트+1
        if real_lost[j]-1 in real_reserve:
            real_reserve.remove(real_lost[j]-1)
            count += 1
        # 잃어버린 사람의 뒷 번호가 빌려줄 수 있는 사람 안에 있으면 빌려준 사람 제거 후 카운트+1
        elif real_lost[j]+1 in real_reserve:
            real_reserve.remove(real_lost[j]+1)
            count += 1
            
    # 수업 참여 가능은 총 인원 - (진짜 잃어버린 사람 - 빌린 사람)
    answer = n - (len(real_lost) - count)
    
    return answer