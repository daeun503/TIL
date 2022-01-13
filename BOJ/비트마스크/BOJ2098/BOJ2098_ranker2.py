N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
dp_table = [[-1 for _ in range(1<<N)] for _ in range(N)]

def dp(current, visited):
    ret = dp_table[current][visited]
    if ret != -1:
        return ret
    if visited == (1<<N)-1:
        if G[current][0] != 0:
            return G[current][0]
        return 200000000
    ret = 200000000
    for i in range(N):
        if visited & (1<<i) or G[current][i] == 0:
            continue
        ret = min(ret, dp(i, visited|(1<<i)) + G[current][i])
    dp_table[current][visited] = ret
    return ret

print(dp(0,1))