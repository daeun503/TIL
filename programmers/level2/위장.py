def solution(clothes):
    dict_clothes = {}
    result = 1
    for a, b in clothes:
        if b not in dict_clothes:
            dict_clothes[b] = []
        dict_clothes[b] += [a]
    
    for clothes in dict_clothes:
        result *= len(dict_clothes[clothes])+1
    
    return result -1