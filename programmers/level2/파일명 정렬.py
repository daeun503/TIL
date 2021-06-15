def solution(files):
    #### input 조절: 2차원 배열 [파일명 소문자, head, number, tail, 원본 파일명] ####
    for i in range(len(files)):                                                 ##
        files[i] = [files[i].lower(), '', '', '', files[i]]                     ##
        for j in files[i][0]:                                                   ##
            if j.isdigit(): files[i][2] += j          # 숫자면 number에 추가     ##
            elif files[i][2] == '': files[i][1] += j  # 숫자X이고 number가 아직 빈값이면 head
            else: break                               # tail은 슬라이싱으로      ##
        files[i][3] = files[i][0][len(files[i][2])+len(files[i][1]):]           ##
        files[i][2] = int(files[i][2]) # number부분 str을 int로 변환             ##
    ##############################################################################

    files.sort(key= lambda x: (x[1], x[2])) # 우선순위1: x[1](head), 우선순위2: x[2](number)
    return [i[4] for i in files]    # 우선순위 3: 입력순은 기본적으로 되어있음