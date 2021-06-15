def solution(brown, yellow):
    # 노란색을 x, y로 표현했더니, x+2 * y+2 가 브라운+노란색 
    for x in range(1, yellow//2+2):
        if (yellow / x) % 1 == 0 :
            y = yellow / x
        if (x+2)*(y+2) == brown + yellow:
            if x < y :
                x, y = y, x
            return [x+2, y+2]