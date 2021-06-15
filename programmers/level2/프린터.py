def solution(priorities, location):
    return_num = 0
    # 현재 맨 앞의 값이랑 뒤쪽의 값들이랑 비교해서, 뒤쪽에 큰 값이 있으면 pop한 뒤 다시 맨 뒤에 붙여주기
    # 현재 값이랑, max를 통해 얻은 값이랑 비교하자.
    while priorities:
        if priorities[0] == max(priorities):  # 우선순위 제일 높으면
            num_pop = priorities.pop(0)       # 인쇄했으니 pop 하고
            return_num += 1                   # +1 해주기
            if location == 0:
                return return_num
            else:
                location -= 1
        else:                                 # 우선순위 낮으면
            num_pop = priorities.pop(0)       # 맨 앞에 pop하고
            priorities.append(num_pop)        # 뒤로 보내기
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1