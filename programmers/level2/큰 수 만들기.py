def solution(number, k):
    numbers = list(number) # 리스트로 만들어 줌
    result = max(numbers[:k+1])
    i = numbers[:k+1].index(result)
    want = len(number) - k   # 출력값의 길이 미리 구해주기
    k += 1                   # 초기 k 범위 맞추기 위해 1 더해주기

    while len(result) != want:
        # 매번 특정 구간에서 max값을 찾아줄 예정
        max_num = '-1'
        for j in range(i+1, k+1):
            # 가장 클 때는 뒷 수를 볼 필요가 없다.
            if numbers[j] == '9':
                max_num = '9'
                max_idx = j
                break
            # 8 이하일 때는 뒷 수에 max값이 있는지 확인해야 함
            elif numbers[j] > max_num:
                max_num = numbers[j]
                max_idx = j
		
		# for문을 이렇게도 쓸 수 있는데, 아마 in이나 index에서 시간초과 걸리는 듯 슬라이싱인가?
        # max_num = '9' if '9' in numbers[i+1:k+1] else max(numbers[i+1:k+1])
        # max_idx = i+1 + numbers[i+1:k+1].index(max_num)
		
        # 결과에 해당 max값을 더해주고, i, k 갱신
        result += max_num
        i = max_idx
        k += 1
    
    return result