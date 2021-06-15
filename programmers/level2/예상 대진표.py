import math

def solution(n,a,b):
    if a > b:
        a, b = b, a
    return recursion(n, a, b)
        
def recursion(n,a,b):
    # 반대 쪽에 있을 때
    if a <= n//2 and b > n//2:
        return math.log(n)/math.log(2)
    # 같은 쪽에 있을 때
    else:
        k = n // 2
        # a, b가 k 이하이면 그대로
        if a <= n//2:
            return recursion(k, a, b)
        # a, b가 k 이상이면 k만큼 빼주기 (한 쪽 에서 경기하는 참가자들 제거하고 a, b있는 쪽만 확인)
        else:
            return recursion(k, a-k, b-k)