# 2회차 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):             # 기준이랑
        for j in range(i+1, len(prices)):    # 기준 이후 값을 비교할 것  
            answer[i] += 1                   # 일단 시간이 흘렀으니까 무조건 +1
            if prices[i] > prices[j]: break  # 기준 이후가 더 크면 가격 떨어진거니까 break
    return answer