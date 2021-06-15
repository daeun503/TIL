def solution(n):
    result = 0
    for i in range(1, n//2+1):      # 1부터 절반까지
        cnt = i                     # 초기 시작값 i
        for j in range(i+1, n//2+2):  
            cnt += j                # 1씩 올려가면서 더한다
            if cnt > n:             # 만약 n보다 커지면 break
                break               # n과 같아지면 result +1 하고 break
            elif cnt == n:
                result += 1
                break
    return result + 1               # 자기 자신때문에 +1