def solution(num):
    cnt = 0
    
    while num != 1:
        num = num*3 + 1 if num % 2 else num//2
        cnt += 1
        if cnt == 500:
            return -1    
        
    return cnt