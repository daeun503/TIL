def solution(m, n, board):
    board = list(map(list, board))                # 2차원 배열로 만들기
    board = [list(_)[::-1] for _ in zip(*board)]  # 반시계 방향으로 90도 회전
    flag, result = 1, 0

    while flag:
        ################ 같은 모양 찾아서, 인덱스 번호 킵해두는 로직 ################
        box = set()
        for r in range(n-1):
            for c in range(m-1):
                me = board[r][c]
                if me and me == board[r+1][c] and me == board[r][c+1] and me == board[r+1][c+1]:
                    box.update([(r, c), (r+1, c), (r, c+1), (r+1, c+1)])
        #######################################################################
        
        # 같은 모양 없으면 끝내도 됨. while뒤로 가면 box 없으니까 앞에 써주기
        flag = 1 if box else 0  
        box = sorted(list(box), key=lambda x: (x[0], x[1]))
        while box:
            a, b = box.pop()  
            board[a].pop(b)    # 킵해뒀던 인덱스 뽑으면서 pop 해주기
            board[a].append(0) # pop이후, 배치 맞춰주기 위해 append(0)
            result += 1
    return result