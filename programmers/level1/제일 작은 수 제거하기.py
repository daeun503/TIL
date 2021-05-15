def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]
    # remove는 리턴 값이 None이라 if문에 통째로 못 넣음