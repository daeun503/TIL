# distance@는 버튼(벨류)에서 @(누를버튼)까지의 거리(키) 에 대한 정보를 미리 계산해서 만든 딕셔너리
# 가운데 버튼을 누르면 center_num에 접근해서 distance@으로 접근함
# 내가 누른 버튼(벨류)으로부터 키(거리)에 접근해서 거리를 구한 뒤 비교

def solution(numbers, hand):
    L, R, answer = '*', '#', ''
    distance2 = {1: {'1', '3', '5'}, 2: {'4', '6', '8'} , 3: {'7', '9', '0'} , 4: {'*', '#'}}
    distance5 = {1: {'2', '4', '6', '8'}, 2: {'1', '3', '7', '9', '0'} , 3: {'*', '#'}}
    distance8 = {1: {'5', '7', '9', '0'}, 2: {'2', '4', '6', '*', '#'} , 3: {'1', '3'}}
    distance0 = {1: {'8', '*', '#'}, 2: {'5', '7', '9'} , 3: {'2', '4', '6'} , 4: {'1', '3'}}
    center_num = {2: distance2, 5: distance5, 8: distance8, 0: distance0}
    
    for num in numbers:
        if num in [1, 4, 7]:     answer += 'L'; L = num  # 1, 4, 7 일 때
        elif num in [3, 6, 9]:   answer += 'R'; R = num  # 3, 6, 9 일 때
        else:  # 2, 5, 8, 0 일 때
            # ex) num = 2면, center_num[2] = distance2. 여기서 item()으로 키 벨류 가져옴
            # str(L/R)이 특정 벨류에 들어있으면, 그때의 특정 키(num ~ L/R까지의 거리) 반환
            dL = [key for key, value in center_num[num].items() if str(L) in value]
            dR = [key for key, value in center_num[num].items() if str(R) in value]
            # 버튼까지의 거리 비교. 같으면 손잡이로
            if dL < dR:          answer += 'L'; L = num
            elif dL > dR:        answer += 'R'; R = num
            elif hand == 'left': answer += 'L'; L = num
            else:                answer += 'R'; R = num

    return answer