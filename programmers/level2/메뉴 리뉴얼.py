def solution(orders, course):
    n = len(orders)
    SetOrders = list(map(set, orders))
    TotalSingle = {}
    
    # 모든 단품 메뉴 조합 모두 찾기
    for i in range(n):
        for j in range(i+1, n):
            menu = ''.join(sorted(SetOrders[i] & SetOrders[j]))
            # menu의 부분 집합 구하기
            menu_n = len(menu)
            for k in range(1 << menu_n):
                tmp = ''
                for l in range(menu_n):
                    if k & (1 << l):
                        tmp += menu[l]
                # 만약 부분집합의 길이가 course안에 있으면 TotalSingle에 추가
                if len(tmp) in course: 
                    TotalSingle[tmp] = 0
    
    # 단품 메뉴가 몇 번 주문됐는지 찾기
    for i in TotalSingle.keys():
        for j in orders:
            if set(i) & set(j) == set(i):
                TotalSingle[i] += 1
    
    max_course = [-1] * 11
    for i in TotalSingle.keys():
        if TotalSingle[i] > max_course[len(i)]:
            max_course[len(i)] = TotalSingle[i]
    
    result = []
    for key, value in TotalSingle.items():
        if max_course[len(key)] == value:
            result += [key]
            
    return sorted(result)