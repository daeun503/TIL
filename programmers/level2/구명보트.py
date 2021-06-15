from collections import deque

def solution(people, limit):
    answer = 0
    dq_people = deque(sorted(people))
    dq_stop = deque([])
    while dq_people != dq_stop :
        if len(dq_people) > 1 and dq_people[-1] + dq_people[0] <= limit:
            dq_people.pop()
            dq_people.popleft()
        else:
            dq_people.pop()
        answer += 1
    return answer