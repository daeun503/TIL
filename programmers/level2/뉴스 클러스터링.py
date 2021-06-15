def solution(str1, str2):
    s1, s2 = list(str1.lower()), list(str2.lower()) # 리스트 & 소문자화

    my = {}  # my의 key: 글자쌍, value: (s1에서 나온 수, s2에서 나온 수)
    for i in range(len(s1) - 1):
        w = s1[i] + s1[i + 1]  # 두 글자씩 끊어서
        if w.isalpha():        # 그 글자가 알파벳이면 s1에서 나온 수 +1
            my[w] = (my.get(w, (0, 0))[0] + 1, my.get(w, (0, 0))[1])
    for j in range(len(s2) - 1):
        w = s2[j] + s2[j + 1]  # 두 글자씩 끊어서
        if w.isalpha():        # 그 글자가 알파벳이면 s2에서 나온 수 +1
            my[w] = (my.get(w, (0, 0))[0], my.get(w, (0, 0))[1] + 1)
            
    # a는 교집합, b는 합집합. 문제 중간에 ↓텍스트 보고 작성함 
    # 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다.
    a, b = 0, 0
    for w in my:
        a += min(my[w])
        b += max(my[w])
        
    return int(a / b * 65536) if b else 65536