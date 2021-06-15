def solution(msg):
    my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
               'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
               'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    result = []

    i, flag = 0, 1
    while flag and i < len(msg):
        tmp = msg[i]                   # tmp의 초기값은 예시의 "다음 글자"
        while tmp in my_dict:          # tmp가 my_dict 안에 있으면 while문 
            if i == len(msg)-1:        # i가 msg의 마지막 인덱스면 break     
                flag = 0; tmp += '-'   # flag로 겉 while문 중지, tmp는 append 때문에 정크값('-') 넣어줌 
                break                  # 이 break문은 else문 때문에 따로 분기처리 해준 것
            i += 1                     # 마지막 인덱스가 아니면 i는 1증가하고
            tmp += msg[i]              # msg[i]를 tmp에 추가
        else:                          # key 안에 tmp가 없어서 정상적으로 끝난 경우에만 dict에 추가
            my_dict[tmp] = len(my_dict) + 1
        result.append(my_dict[tmp[:-1]])
        
    return result