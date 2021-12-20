import sys
sys.stdin = open("input.txt", "r")

M = int(sys.stdin.readline())
S = 0
for _ in range(M):
    op, *num = sys.stdin.readline().split()
    x = int(num[0]) if num else 0

    if op == "add":
        S = S | (1 << x)
    elif op == "remove":
        S = S & ~(1 << x)
    elif op == "check":
        print(1) if S & (1 << x) else print(0)
    elif op == "toggle":
        S = S ^ (1 << x)
    elif op == "all":
        S = (1 << 21) - 1
    elif op == "empty":
        S = 0
