def solution(n):
    ans = 0
    # 홀수일 때는 -1 해주고 1이동, 짝수일때는 순간이동 
    # (뒤로 간다고 생각하자)
    while n:
        if n % 2 :
            n -= 1
            ans += 1
        else:
            n = n // 2
    return ans