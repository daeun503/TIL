def solution(relation):
    col_N = len(relation[0])
    row_N = len(relation)
    sel = [1] * col_N
    
    #--부분집합을 이용해서 가능한 모든 후보키 구하기--#
    result = []
    def powerset(idx):
        nonlocal result
        ############## 종료 조건 ##############
        if idx == col_N:
            tmp = {}
            for rel_row in relation:             # relation의 한 줄: rel_row
                s = ''
                for a, b in zip(rel_row, sel):   # rel_row와 sel의 각 요소를 곱해 더한값을
                    s += a * b
                tmp[s] = tmp.get(s, 0) + 1       # key로 해서 dict에 넣는다
            if len(tmp) == row_N:                # 만약 각 key값이 1개씩 나오면 유일성 만족
                result.append(sel[:])            # 복사해서 집어넣기. sel로하면 주소로 들어간다
            return
        ################ 재귀 ################
        sel[idx] = 0; powerset(idx + 1)
        sel[idx] = 1; powerset(idx + 1)
    powerset(0)
    #------------------------------------------#
    
    #-------------------최소성------------------#
    result.sort(key= lambda x : x.count(0))      # 0의갯수 (1의갯수역순)으로 정렬
    result2 = [result.pop()]                     # 초기값 / result2가 최소성 포함 답 
    while result:
        for r2 in result2:                      
            tmp = 0
            for a, b in zip(r2, result[-1]):     # 뒤부터 검사 r2, result[-1]의
                tmp += a * b                     # 요소끼리 곱했는데
            if tmp >= r2.count(1):               # 그 값이 r2의 1갯수보다 많으면
                result.pop()                     # r2를 포함하는 것이기 때문에 버림
                break
        else:                                    # 모든 result2의 요소에 대해 검사 성공하면
            result2.append(result.pop())         # result2에 없는, 최소성 만족이므로 추가

    return len(result2)