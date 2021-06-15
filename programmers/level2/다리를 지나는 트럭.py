# 다리 길이: bridge_length / 견딜 수 있는 무게: weight / 트럭의 무게: truck_weights
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 처음 트럭은 무조건 다리 길이만큼 시간이 걸림
    time = bridge_length
    dq = deque([0] * bridge_length)
    num = 0
    # 매번 sum을 하면 시간초과 된다 (테케5) 이전 값을 활용해서 더해주자
    sum_dq = 0
    
    while num != len(truck_weights):
        time += 1                 # 1초 지남
        sum_dq -= dq.popleft()    # 1초 지났으니 맨 앞 트럭 위치 pop해줌
        # 다리 위에 있는 트럭(sum_dq)랑 다리에 올라가려고 하는 트럭이 weight보다 작으면
        if sum_dq + truck_weights[num] <= weight:
            # dq에 넣어주고 sum_dq에 더해줌. 그리고 다음 트럭으로 num +1
            dq.append(truck_weights[num])
            sum_dq += truck_weights[num]
            num += 1
        # weight보다 크면 0을 넣어준다.
        else:
            dq.append(0)
    
    return time