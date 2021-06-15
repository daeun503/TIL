import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    max = 0
    ascend = []

    for i in range(N):
        if num[i] >= max:
            ascend = [num[i]] + ascend
            max = num[i]

        else: # 15 20 8 28 16 27 17 27 10 12
            for j in range(len(ascend)):
                if ascend[j] <= num[i]:
                    ascend.insert(j, num[i])
                    break

                elif ascend[j] > num[i] and j == len(ascend) - 1:
                    ascend += [num[i]]
                    break

    print(ascend)