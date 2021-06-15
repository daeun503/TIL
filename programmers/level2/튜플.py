def solution(s):
    s = s.replace('{','')
    s = s.replace('}','')
    
    # {, } 다 벗겨주기 
    s = list(map(int, s.split(',')))
    s_set = set(s)
    result = [0] * len(s_set)
    
    # 갯수가 len(s)인 요소가 인덱스 0 번, 1인 요소가 인덱스 len(s)-1번 
    for i in s_set:
        result[s.count(i)-1] = i
    
    # 반대라서 뒤집어주기
    return list(reversed(result))