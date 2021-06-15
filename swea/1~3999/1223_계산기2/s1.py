import sys
sys.stdin = open("input.txt", "r")

# 연산자는 +, * / 피연산자는 0 ~ 9의 정수
for tc in range(1, 11):
    N = int(input())
    IN = input()

    # 중위 표현식 -> 후위 표현식 변환하기
    postfix = ''
    stack = []
    for i in IN:
        # i가 숫자면 표현식에 바로 넣어주기
        if i.isdigit():
            postfix += i

        # 스택이 비어있을 때는 그냥 push하면 되는데, 각 조건의 while에서 처리가 된다.

        # i가 +이고, top이 *일 때: 다 pop한 다음에 push(*, +는 i(+)보다 우선순위 낮은게 X)
        # i가 +이고, top이 +일 때: 다 pop한 다음에 push
        # => 즉, i가 + 일때, 죄다 pop한 후 // push.
        elif i == '+':
            while stack:
                postfix += stack.pop()
            stack.append(i)

        # i가 *이고, top이 *일 때: + or 스택 빌 때 까지 pop하고 push
        # i가 *이고, top이 +일 때: 그냥 push
        # => 즉, i가 * 일때, top이 *이면 +나 스택 빌 때까지 pop한 후 // push.
        elif i == '*':
            while stack[-1:] == ['*']: # pop해서 스택이 비어있을 때 stack[-1]을 해주면 인덱스 에러. 이 때문에 stack[-1:]
                postfix += stack.pop()
            stack.append(i)

    # 스택에 남아 있는 것들 모두 꺼내서 더해주기
    while stack:
        postfix += stack.pop()


    # 후위 표현식 계산하기
    stack = []
    for i in postfix:
        # 만약 숫자면 stack에 쌓기
        if i.isdigit():
            stack.append(i)
        # 숫자가 아니면(+ or *) 계산해주기
        else:
            B = int(stack.pop())
            A = int(stack.pop())
            # +면 A+B를 넣고, *면 A*B를 push해주기
            stack += [A + B] if i == '+' else [A * B]
            # cal = {'+': A + B, '-': A - B, '*': A * B, '/': A // B}
            # stack.append(cal[i])


    # 마지막 계산 값 빼서 출력해주기
    result = stack.pop()
    print("#{} {}".format(tc, result))