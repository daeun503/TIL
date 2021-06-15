def solution(record):
    record = [ _.split() for _ in record ]
    # 빠르게 한바퀴 돌면서 users라는 dict에 user_id = user_nickname 형태로 저장
    # user_id = record[i][1] , user_nickname = record[i][2]
    users = {}
    for i in range(len(record)):
        if not record[i][0] == 'Leave':
            users[record[i][1]] = record[i][2]
    
    # users 딕셔너리에는 최신 정보가 들어있으므로 출력하면 됨 
    result = []
    for i in range(len(record)):
        if record[i][0] == 'Leave':
            result.append('{}님이 나갔습니다.'.format(users[record[i][1]]))
        elif record[i][0] == "Enter":
            result.append('{}님이 들어왔습니다.'.format(users[record[i][1]]))
        
    return result 