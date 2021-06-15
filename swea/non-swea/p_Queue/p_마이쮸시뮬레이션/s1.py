"""
연습문제2. 마이쮸 시뮬레이션 구현

포인트: 문제를 통해서 말하고자 하는 바를 Queue의 핵심 동작 원리와 연결지어 생각해보자
"""

# 마이쮸의 개수
N = 20

# 초기화
queue = [(1, 0)]

# (0, 0) [0]: 사람 번호, [1]: 직전까지 받았던 마이쮸의 개수
new_people = 1
last_people = 0

while N > 0:
    # 받으러온 사람(num), 직전까지 받은 개수(cnt)
    num, cnt = queue.pop(0)

    # 마지막으로 받으러 온 사람
    last_people = num

    # 지난번보다는 하나 더 챙겨가자
    cnt += 1

    # num이라는 친구가 cnt 개수만큼 마이쭈를 가져감
    N -= cnt

    # 새로운 사람이 와서 줄을 선다.
    new_people += 1

    # 맨 뒤로 가서 줄을 선다.(queue의 특성 -> 삽입은 제일 뒤에서 발생)
    queue.append((num, cnt))

    # 새로운 사람은 줄을 서고 처음에는 아무 마이쮸도 받기 못했기 때문에 0으로 초기화
    # 직전에 마이쮸를 받은 사람 바로 뒤에 서게 된다.
    queue.append((new_people, 0))

print('마지막으로 마이쮸를 가져간 사람은? {}번!!!'.format(last_people))