def solution(answers):
    # 수포자가 찍는 방식 배열
    p1 = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    
    # 수포자들 점수
    OK = { 1 : 0 , 2 : 0, 3 : 0 }
    
    # 수포자들이 정답 맞추면 점수 +1
    for answer, p1, p2, p3 in zip(answers, p1, p2, p3):
        OK[1] += 1 if answer == p1 else 0
        OK[2] += 1 if answer == p2 else 0
        OK[3] += 1 if answer == p3 else 0
    
    # 점수 제일 높은 사람 찾기
    max_score = max(OK.values())
    answer = [key for key, value in OK.items() if value == max_score]
    
    return answer