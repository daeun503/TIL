def solution(m, musicinfos):
    def trans(a):  # 음 변환 함수 A# C# D# F# G# => H I J K L
        return a.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
    
    ####################### 필요한 input 조절 ############################
    m = trans(m) # 음 변환                                              ##
    for i in range(len(musicinfos)):                                   ##
        # ,를 기준으로 나누고, index 3은 악보 음이니까, 음 변환           ##
        musicinfos[i] = musicinfos[i].split(',')                       ##
        musicinfos[i][3] = trans(musicinfos[i][3])                     ##
        # 시간 계산                                                     ##
        t1 = int(musicinfos[i][0][:2])*60 + int(musicinfos[i][0][3:5]) ##
        t2 = int(musicinfos[i][1][:2])*60 + int(musicinfos[i][1][3:5]) ##
        musicinfos[i].append(t2-t1)                                    ##
        # 조건 일치 음악 여러 개일 때를 위한 flag 변수                    ##
        musicinfos[i].append(0)                                        ##
    #####################################################################
    
    for i in range(len(musicinfos)):     # i번째 음악
        t = musicinfos[i][4]             # 위에서 미리 구해둔 재생 시간
        play = ( musicinfos[i][3] * (t//len(musicinfos[i][3])+1) )[:t]
        if m in play:                    # 만약 play 안에 기억한 멜로디 m이 있으면
            musicinfos[i][5] = 1         # flag 변수에 체크해준다
            
    # flag변수가 1일때 조건에 부합되므로, 재생시간*1을 기준으로 정렬하면 된다 (-는 내림차순)
    musicinfos.sort(key= lambda x : - x[4]*x[5])
    # flag변수가 0이면 조건 부합이 아예 없으므로, 그때는 None. 있으면 [0][2]반환하면 됨
    return musicinfos[0][2] if musicinfos[0][5] else "(None)"
