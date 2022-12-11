import sys
sys.stdin = open('input.txt')

IN = list(input())
stack = []
error = -1
for idx, txt in enumerate(IN):
    # ( 이면 일단 넣음
    if txt == "(":
        stack.append((txt, idx))
    # ) 이고, stack 최상단이 (이면 pop
    elif stack and stack[-1][0] == "(":
        stack.pop()
    # ) 이고, stack 최상단이 ) 이거나 비어있으면 잘못된 것
    else:
        error = (txt, idx)
        break

# 만약 스택이 비었는데 error도 못 찾으면 정상적인 괄호임
if not stack and error == -1:
    print(0)
    exit()
# error를 못 찾았고 스택이 차 있으면 거기서 잘못된 거 찾음
elif error == -1:
    error = stack[-1]

# 자기 자신 (error_idx) 자체를 뒤집는 횟수
result = 1
error_text, error_idx = error
# 자기가 ( 이면 자기 기준 우측에 있는 (를 뒤집어서 )로 만들어주면 됨
if error_text == "(":
    result += IN[error_idx + 1:].count("(")
# 자기가 ) 이면 자기 기준 좌측에 있는 )를 뒤집어서 (로 만들어주면 됨
else:
    result += IN[:error_idx].count(")")

print(result)
