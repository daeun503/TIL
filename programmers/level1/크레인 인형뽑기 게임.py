def solution(board, moves):
    # board[0]은 가로로 맨 윗줄, [1]은 두번째 줄 ...
    # move 1하기 위해서는 각 리스트의 첫 인덱스(board[0][1], [1][1], [2][1]...)를 봐야한다.
    # 숫자를 만나면 빼서 store에 집어넣기. 근데 store에 같은게 있으면 pop
    
    answer = 0
    store = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                store.append(board[i][move-1])
                board[i][move-1] = 0
                break
    
    while 1:
        for i in range(1, len(store)): 
            if store[i-1] == store[i]:     # store안에 연속된 수가 있는지 검사해서 있으면 
                store.pop(i)               # 해당 수들 지우기. 이때 뒤 인덱스부터 지울 것.
                store.pop(i-1)             # 앞에서부터 지우면 지운만큼 밀려서 값이 달라진다. 
                answer += 2                # i-1, i순으로 지웠더니 동작이 안 됐음.
                break
        else:
            break
                
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))