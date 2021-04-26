def solution(participant, completion):
    result = {}
    
    # 참여했으면 +1
    for part in participant: 
        result[part] = result.get(part, 0) + 1
    
    # 완주했으면 -1
    for comple in completion:
        result[comple] = result.get(comple, 0) - 1
    
    # 완주 못한 사람은 value가 1
    fail = [key for key, value in result.items() if value == 1]
    
    return fail[0]