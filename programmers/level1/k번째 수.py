def solution(array, commands):
    result = []
    
    # command i~j까지 슬라이싱한 후 정렬하고, k번째 수 구해서 리스트에 넣기
    for com in commands:
        result += [sorted(array[com[0]-1 : com[1]])[com[2]-1]]
        
    return result