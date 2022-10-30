import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

# 나라 0번부터 시작하도록 바꾸기
P = list(map(int, input().split()))
for idx in range(M):
    P[idx] -= 1

# 티켓, IC, IC카드 값 구분하기
ticket, IC, IC_card = [], [], []
for _ in range(N-1):
    A, B, C = map(int, input().split())
    ticket.append(A)
    IC.append(B)
    IC_card.append(C)

# 각 나라를 몇 번 방문해야하는지 구하기
country_visit_count = [0] * N
for i in range(M-1):
    # current가 더 작은 숫자. 2 -> 4 ok / 4 -> 2면 변경
    current, next = P[i], P[i+1]
    if current > next:
        current, next = next, current

    # 이렇게 하면 시간초과가 난다.
    # while current < next:
    #     country_visit_count[current] += 1
    #     current += 1
    country_visit_count[current] += 1
    country_visit_count[next] -= 1

# 티켓 비용 * 방문 횟수 > IC 비용 * 방문 횟수 + IC 카드 비용이면 IC 카드를 사는 것이 낫다
# 나라가 N개면 철도는 N-1 개라서 N-1 까지만 본다
total, count = 0, 0
for country in range(N-1):
    # 위 주석과 함께 이렇게 하면 시간초과가 난다.
    # count = country_visit_count[country]
    count += country_visit_count[country]
    total_ticket = ticket[country] * count
    total_IC = IC[country] * count + IC_card[country]
    total += min(total_ticket, total_IC)

print(total)
