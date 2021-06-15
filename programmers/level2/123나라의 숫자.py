def solution(n):
    result = ''
    to124 = {1: '1', 2:'2', 0: '4'}
    
    if (n-1) // 3 == 0:
        return f'{to124[n%3]}'
    else:
        return solution((n-1)//3) + f'{to124[n%3]}'