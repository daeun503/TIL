# arr 배열의 첫 요소는 무조건 들어가야 하므로 tmp의 초기값으로 지정
# tmp와 arr의 요소를 비교하며, 다를 때 answer에 추가하고 해당 값으로 tmp를 갱신한다.

def solution(arr):
    tmp = arr[0]
    answer = [tmp]
    
    # tmp와 a의 값을 비교하며, 다를 땐 answer에 추가하고 tmp를 갱신한다.
    for a in arr:
        if tmp != a:
            answer.append(a)
            tmp = a 
            
    return answer