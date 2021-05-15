def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1 , arr2):
        list = []
        for i, j in zip(x, y):
            list += [i + j]
        answer.append(list)
    return answer


# 리스트 컴프리헨션
def solution(arr1, arr2):
    return [[i+j for i, j in zip(a, b)] for a, b in zip(arr1, arr2)]