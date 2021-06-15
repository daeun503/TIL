def solution(s):
    result = []
    
    for word in s:
        result.append(word)
        if len(result) > 1 and result[-2] == '(' and result[-1] == ')':
            result.pop()
            result.pop()
            
    if result == []:
        return True
    else:
        return False