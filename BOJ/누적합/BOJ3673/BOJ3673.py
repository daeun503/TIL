import sys
sys.stdin = open('input.txt')
from collections import defaultdict

c = int(sys.stdin.readline())
for _ in range(c):
    d, n = map(int, sys.stdin.readline().split())
    IN = list(map(int, sys.stdin.readline().split()))

    # 누적합으로, d로 나눈 나머지 값을 dict로 만듦
    count_dict = defaultdict(int)
    hap = 0
    for i in range(n):
        hap += IN[i]
        num = hap % d
        count_dict[num] += 1

    # idx 0~i까지 중 d로 나누어지는 건 dict[0]에 있음
    result = count_dict[0]

    # num = idx 0~j의 나머지 값을 뺏을 때 그게 d로 나누어 떨어진다는 것은
    # dict[num]의 값을 구하는 것과 동일한
    hap = 0
    for j in range(n):
        hap += IN[j]
        num = hap % d
        count_dict[num] -= 1
        result += count_dict[num]

    print(result)


"""
idx  0 1 2 3 4 5 6 7
val  2 1 2 1 1 2 1 2
    [0]
    [0~1]
    [0~2  ]
    [0~3    ]
    [0~4      ]
    [0~5        ]
    [0~6          ]   
    [0~7            ]
위 값에서 %d를 한 것이 dict 값
그럼 dict[0]이 0~i 의 d로 나누어 떨어지는 갯수임

    [0~7            ]의 %d가 2면
2만큼의 값을 빼어준다면 d로 나누어 줄 수 있다는 말
    [ 1   ][  2     ]
그래서 1영역(line24. 0~j합)이 2이면 dict[2]값을 더해줌
근데 1영역 = 2영역일 때는 고려하면 안되기 때문에 -1

"""
