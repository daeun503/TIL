# divisor로 나눠지는 값만 새 배열에 담은 뒤 sort

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer += [i]
    return [-1] if answer == [] else sorted(answer)