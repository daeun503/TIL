def solution(a, b):
    # m_day: 달별 며칠까지 있는지, result: 7로 나눴을 때 나머지가 무슨 요일인지
    m_day = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    result = {0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    total = 0
    
    # 1일부터 a월 b일까지 며칠인지?
    for i in range(1, a):
        total += m_day[i]
    total += b
    
    return result[total%7]