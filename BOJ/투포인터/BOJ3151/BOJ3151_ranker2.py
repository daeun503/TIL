import sys
sys.stdin = open("input.txt", "r")

N = int(input())
IN = sorted(list(map(int, sys.stdin.readline().split())))

result = 0
for i in range(N - 2):
    p1, p2 = i + 1, N - 1
    target = -IN[i]
    pointer = N

    while p1 < p2:
        hap = IN[p1] + IN[p2]
        # 합이 target 보다 작으면 p1을 증가
        if hap < target:
            p1 += 1

        # 합과 target 이 같으면
        elif hap == target:
            # IN[p1], IN[p2] 같이 같으면 사이 값만큼 더해주기
            if IN[p1] == IN[p2]:
                result += p2 - p1
            # 다르면 pointer 를 옮겨주기
            else:
                if pointer > p2:
                    pointer = p2
                    while pointer >= 0 and IN[pointer - 1] == IN[p2]:
                        pointer -= 1
                result += p2 - pointer + 1
            p1 += 1

        # 합이 target 보다 크면 p2를 감소
        else:
            p2 -= 1
print(result)
