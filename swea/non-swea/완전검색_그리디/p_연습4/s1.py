"""
연습문제 4. 순열

4-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if i != k and j != k:
                    print(i, j, k)