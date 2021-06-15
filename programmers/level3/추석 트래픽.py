def solution(lines):
    ######### input 파싱 : my = [(시작, 끝, 처리시간) ...] ###########
    lines = [line.split() for line in lines]                     ##
    my = []                                                      ##
    for i in range(len(lines)):                                  ##
        end = list(map(float, lines[i][1].split(':')))           ##
        T = float(lines[i][2][:-1])                              ##
        if 0.001 <= T <= 3:                # 타임아웃 아닐때만 추가 ##
            end = end[0]*3600 + end[1]*60 + end[2]    # 초로 변환 ##  
            start = end - T + 0.001                              ##
            my.append((start*1000, end*1000, T))                 ##
    my.sort(key = lambda x: x[1])                                ##
    ###############################################################
    
    result = 0
    # my[i] 요청 로그에 대해 분석 
    for i in range(len(my)):
        tmp = 0
        s_log = my[i][1]     # 1초간 측정하는 부분의 시작(요청 로그의 끝)
        e_log = s_log + 999  # 1초간 측정하는 부분의 끝 (0.999는 오차가 생겨서 *1000해줌)
        
        for j in range(len(my)):
            # 측정이 시작되고 요청이 들어오고, 측정이 끝났을 때
            # 요청이 들어오고 측정이 시작하고, 요청이 완료됐을 때
            # 요청이 들어오고 측정이 끝나고, 요청이 완료 됐을 때 
            if s_log <= my[j][0]<= e_log or \
            my[j][0] <= s_log <= my[j][1] or\
            my[j][0] <= e_log <= my[j][1]:
                tmp += 1 # 해당 요청을 세준다.
                            
        # 저장해둔 result보다 더 큰 초당 최대 처리량이 있으면 갱신
        if result < tmp:
            result = tmp
			
    return result