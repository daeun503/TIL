#2. 최소힙 라이브러리 활용 - heapq

import heapq

# 단순 리스트
temp = [7, 2, 5, 3, 4, 6]

# 직접 검색으로 찾아 구현하기
# heapify -> heap으로 변경
heapq.heapify(temp)

# 삽입(heappush)
temp1 = []
heapq.heapify(temp1)
for i in temp:
    heapq.heappush(temp1, i)
print(*temp1)

# 삭제(heappop)
heapq.heappop(temp1)
print(*temp1)

# 오름차순으로 출력
while temp1:
    print(heapq.heappop(temp1), end=' ')
print()

# 내림차순으로 출력
temp2 = []
heapq.heapify(temp2)
for i in temp:
    heapq.heappush(temp2, -i)
while temp2:
    print(-heapq.heappop(temp2), end=' ')