# import sys
# sys.stdin = open("input.txt", "r")

def func(player_position, score):
    global result
    
    # 선수를 모두 배치했으면 능력치 갱신하고 return
    if len(player_position) == 11:
        result = max(result, score)
        return

    # player(0~10)의 포지션(0~10) 정하기
    player = len(player_position)
    for position in range(0, 11):
        # player의 포지션 적합도가 0이거나, 그 포지션을 다른 player가 차지하고 있으면 패스
        if not IN[player][position] or not (position not in player_position):
            continue
        # player의 포지션 정함
        func(player_position + [position], score + IN[player][position])


for _ in range(int(input())):
    IN = [list(map(int, input().split())) for _ in range(11)]
    result = 0
    func([], 0)
    print(result)
