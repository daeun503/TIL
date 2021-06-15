import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


T = int(input())
for tc in range(1, T + 1):
    IN, N = map(int, input().split())
    IN = list(map(int, list(str(IN))))
    idea_IN = sorted(IN, reverse=True)   # IN 으로 만들 수 있는 max값
    targets = sorted(list(set(IN)))      # 비교 대상

    n = 0
    while n < N:
        ################ IN으로 만들 수 있는 max값일 때 ################
        if IN == idea_IN:
            flag = 0
            # 만약 같은 숫자가 2개 이상 있으면 flag=1
            for i in range(len(IN)-1):
                if IN[i] == IN[i+1]:
                    flag = 1
            # flag가 0이고 앞으로 홀수번 교환해야하면 맨 뒤 두자리 교환
            if not flag and (N-n)%2:
                IN[-1], IN[-2] = IN[-2], IN[-1]
                break
            # flag가 1이거나 앞으로 짝수번 교환해야하면 max값 그대로
            else:
                break
        #############################################################

        # while문 한 바퀴에서 target 숫자 여러개 교환하는 횟수(nn) 세기
        target = targets.pop()
        nn = 0

        # IN의 뒤부터 보면서 target의 값을 세고 -1로 바꿔줌
        for i in range(len(IN)-1, -1, -1):
            if IN[i] == target and nn+n < N:
                IN[i] = -1
                nn += 1

        # target이랑 위치 교환해줄 작은 숫자 찾아서 tmp에 넣고,
        # 그 숫자 위치에는 target을 넣어준다.
        # nn개 만큼 작은 숫자를 찾아줄건데 nn개 찾기 전에 원래 target 위치를
        # 찾으면 그 자리에 다시 target 넣어주고 nn은 하나 빼준다
        tmp = []
        for j in range(len(IN)):
            if IN[j] == -1 and len(tmp) < nn:
                IN[j] = target
                nn -= 1
            elif IN[j] < target and len(tmp) < nn:
                tmp.append(IN[j])
                IN[j] = target

        # 작은 숫자들 모아둔거 sort하고, 처음에 target을 빼서 -1 넣은 곳에
        # 순서대로 작은 숫자들을 넣어 줌
        tmp.sort()
        for k in range(len(IN)):
            if IN[k] == -1:
                IN[k] = tmp.pop()

        # while 한 세트 끝났으면 nn을 전체 n에 더해준다
        n += nn

    print("#{} {}".format(tc, ''.join(map(str, IN))))