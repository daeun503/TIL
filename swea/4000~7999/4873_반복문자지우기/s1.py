import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    IN = input()

    # IN에서 한 글자씩 읽으면서, 방금 넣은 값이랑 같으면 pop 다르면 push (리스트로 비교)
    stack = []
    for t in IN:
        if [t] == stack[-1:]:
            stack.pop()
        else:
            stack.append(t)

    print("#{} {}".format(tc, len(stack)))