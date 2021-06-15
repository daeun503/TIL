def solution(numbers):
    # 필요한 값들 만들기: 최대값과 numbers (int형)list.
    num = sorted(numbers, reverse=True)    # 내림차순, str
    numbers = list(map(int, num))          # 내림차순, int
    max_num = int(''.join(num))            # 만들 수 있는 최댓값

    # 각 종이 조각이 몇 개 있는지 카운팅
    num_cnt = [0] * 10
    for i in numbers:
        num_cnt[i] += 1
        
    result = 0
    # 에라토스테네스의 체 
    prime = [1] * (max_num+1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2, max_num+1):
        if prime[i]:
            # 숫자 i는 어떤 종이 조각, 몇 개로 만들 수 있는지 카운팅
            i_cnt = [0] * 10
            for j in list(str(i)): 
                i_cnt[int(j)] += 1
            
            # 내가 가지고 있는 종이 조각으로 숫자 i를 못만들면 break, 만들 수 있으면 result +1
            for k in range(10):
                if i_cnt[k] > num_cnt[k]:
                    break
            else:
                result += 1
            
            # 배수 지우기(에라토스테네스의 체)
            for j in range(i*i, max_num+1, i):
                prime[j] = 0
    
    return result