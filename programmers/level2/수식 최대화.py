def solution(expression):
    cases = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    result_list = []
    
    ex_list = ex_to_list(expression, ['+', '-', '*'])
    ex_list_copy = list(ex_list)
    
    for case in cases:       # case = ['+', '-', '*']
        for sign in case:    # sign = + 
            while sign in ex_list:
                sign_idx = ex_list.index(sign)
                result = case_func(ex_list[sign_idx-1], ex_list[sign_idx+1], sign)
                ex_list.pop(sign_idx+1)
                ex_list.pop(sign_idx)
                ex_list.pop(sign_idx-1)
                ex_list.insert(sign_idx-1, result)
        result_list.append(abs(ex_list[0]))
        ex_list = list(ex_list_copy)
        
    return max(result_list)


def case_func(A, B, sign):
    if sign == '*':
        return int(A) * int(B)
    if sign == '+':
        return int(A) + int(B)
    if sign == '-':
        return int(A) - int(B)
                
        
def ex_to_list(expression, case):
    ex_list = []
    tmp = ''
    
    # 첫 문자가 - 로 시작하면 tmp에 - 넣어주고 해당 문자는 잘라주기
    if expression[0] == '-':
        tmp = '-'
        expression = expression[1:]
        
    # 연산식에서 문자 하나씩 꺼내기
    for idx, ex in enumerate(expression):
        # 꺼낸 문자가 연산 문자면
        if ex in case:
            # 현재 문자가 -인데 이전 문자가 연산식이었으면 패스해주기 (line54에서 이미 고려해줌)
            if ex == '-' and expression[idx-1] in case:
                continue
            ex_list.append(int(tmp))
            ex_list.append(ex)
            # 지금 연산 문자인데 다음 문자가 - 이면 tmp에 - 추가, 아니면 공백
            tmp = '-' if expression[idx+1] == '-' else ''
        # 꺼낸 문자가 숫자면 tmp에 추가
        else:
            tmp += ex
    # 연산 문자일때 append해준거라 마지막 숫자는 추가 안됐음. 그거 추가
    else:
        ex_list.append(int(tmp))
        
    return ex_list