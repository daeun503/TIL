# p : 균현잡힌 괄호 문자열. 만약 p가 올바른이면 그대로 리턴 
def solution(p):
    # 1. 빈 문자열인 경우 빈 문자열을 반환.
    if not p: return p 
    
    # 가장 작은 균형잡힌 괄호 문자열인 u, 그 외의 부분 v로 슬라이싱
    check = {'(':0 , ')':0}
    idx = 0
    for i in p:
        check[i] += 1
        if check['('] == check[')']:
            u = p[:idx+1]
            v = p[idx+1:]
            break
        idx += 1
    
    # flag: u가 올바른 괄호 문자열인지 판단. 
    # u_copy를 통해 복사해서 사용. 만약 ()쌍이 모두 있어서 u_copy가 ''이 되면 flag는 1
    u_copy = u
    while u_copy:
        if '()' in u_copy:
            u_copy = u_copy.replace('()', '')
        else:
            break
    flag = 0 if u_copy else 1
    
    # flag가 1: u가 올바른 괄호 문자열
    if flag:
        return u + solution(v)
    # flag가 0: u가 올바른 괄호 문자열이 아님
    else:
        # 괄호 방향 뒤집어주기 
        n = ''
        for a in u[1:-1]:
            n += ')' if a == '(' else '('
        return '(' + solution(v) + ')' + n