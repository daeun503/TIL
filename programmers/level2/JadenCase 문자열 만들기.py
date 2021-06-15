def solution(s):
    s_list = s.split()
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = []
    flag = 0
    for word in s_list:
        if word[0] in number:
            result.append(word.lower())
            flag += 1
        else:
            result.append(word.title())
            
    if flag > 0:
        return ' '.join(result)
    else:
        return s.title()
