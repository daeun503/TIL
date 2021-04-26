def solution(new_id):
    texts = '~!@#$%^&*()=+[{]}:?,<>/'
    id_1st = new_id.lower()                     # 1단계
    
    for text in texts:
        while (text in id_1st):
            id_1st = id_1st.replace(text, '')   # 2단계
    
    while '..' in id_1st:
        id_1st = id_1st.replace('..', '.')      # 3단계
    
    id_4th = id_1st.strip('.')                  # 4단계
    
    id_5th = 'a' if id_4th == '' else id_4th    # 5단계
        
    if len(id_5th) >= 16:                       # 6단계
        id_6th = id_5th[:15].strip('.') 
    elif len(id_5th) == 2:
        id_6th = id_5th + id_5th[1]
    elif len(id_5th) == 1:
        id_6th = id_5th * 3
    else:
        id_6th = id_5th
            
    return id_6th