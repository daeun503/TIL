import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    info = []
    for i in range(N):
        IN = list(map(int, list(input())))
        if sum(IN) and not info:
            info = IN

    while not info[-1]:
        info.pop()
    info = info[-56:]

    ctc = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    code8 = [0]*8
    for i in range(8):
        code8[i] = list(map(str, info[7*i:7*i+7]))
        code8[i] = ctc[''.join(code8[i])]

    hap = (code8[0] + code8[2] + code8[4] + code8[6]) * 3 + (code8[1] + code8[3] + code8[5]) + code8[7]
    result = sum(code8)
    result = 0 if hap % 10 else result

    print("#{} {}".format(tc, result))