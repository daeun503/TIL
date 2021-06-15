def solution(routes):
    N = len(routes)
    routes.sort()
    cnt = 1                   # routes가 1개여도, 디폴트는 1

    a, b = 0, 1               # a는 기준, b는 기준에 포함되는가?
    while b < N:              # e1은 고정 s2는 계속 변화
        s1, e1 = routes[a]
        s2, e2 = routes[b]
        if e1 > e2:           # sort 했기 때문에 s1 < s2는 보장 
            a = b             # s1<s2 & e1 >e2 이면, 1이 2를 감싼다.
            b += 1            # 따라서 2에서 어디에 카메라 설치하든 1은 카메라 만날 수 있다.
            continue
    
        if s2 <= e1 <= e2 :   # 이 부분 줄일 수 있는데 명시적으로 써주기 위해 안 줄임 
            b += 1            # 기준(a)가 다음 루트(b)를 포함하므로, b의 다음(+1)을 포함하는 지 확인한다.
        else:                 # 기준(a)이 다음 루트(b)를 포함하지 않으면 
            a = b             # b를 새로운 기준으로 만들고,
            b += 1            # b의 다음(+1)을 b로 만들어서 반복한다.
            cnt += 1          # 이 경우 카메라를 새로 설치하는 것이므로 cnt +1 
    
    return cnt