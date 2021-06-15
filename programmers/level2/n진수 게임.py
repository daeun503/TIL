# 이건.. 푼지 오래돼서 기억이 안 난다 다음에 다시 풀어보기 
def solution(n, t, m, p):
    tmp = [0] * t * m
    result = ''
    i, cnt = 0, -1
    while len(result) < t:
        num = dec_to_n(n, i)
        for x in num:
            cnt += 1
            if (cnt % m) == p-1:  
                result += x 
                if len(result) == t: break
        i += 1
    return result
    
def dec_to_n(n, num):
    hex_en = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    result = ''
    if num == 0:
        return '0'
    while num :
        if num % n < 10:
            result = str(num%n) + result
        else:
            result = hex_en[num%n] + result
        num = num // n
    return result