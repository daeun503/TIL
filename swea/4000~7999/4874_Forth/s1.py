import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    IN = input().split()

    stack = []
    for i in IN:
        # .이 들어왔을 때. stack이 1이면 결과값, 아니면 error
        if i == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
        # 숫자가 들어오면 스택에 넣기
        elif i.isdigit():
            stack.append(int(i))
        # 연산자가 들어오면 2개 pop해서 계산하고 넣어주기. 2개 pop못하면 error
        else:
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()
            else:
                result = 'error'
                break
            cal = {'+': A+B, '-': A-B, '*': A*B, '/': A//B}
            stack.append(cal[i])

    print("#{} {}".format(tc, result))