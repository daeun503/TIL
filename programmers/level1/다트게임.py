# 순차적으로 읽으면서 word가 옵션인지, 보너스인지, 숫자인지 구분
# 리스트 만들어서 기회별로 점수 따로 계산. 숫자가 나오면 다음 기회라는 뜻이므로 리스트 인덱스 +1

def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    result = [0, 0, 0]
    th, old_num = -1, 0
    
    for word in dartResult:
        # word가 option일 때
        if word == '*':              # *일 때
            result[th] *= 2          # 현재값 x2
            if th: result[th-1] *= 2 # th가 1이상(2, 3번째)이면 이전값 x2
        elif word == '#':            # #일 때
            result[th] *= -1         # 현재값 x(-1)
        # word가 bonus일 때
        elif word in bonus.keys():
            result[th] = result[th] ** bonus[word] # bonus[word]제곱
        # word가 숫자일 때. 숫자면 다음 점수로 넘어가므로 th +1
        else:
            if old_num == '1' and word == '0': # '10' 나왔을 때
                result[th] = 10
            else:          # 숫자가 나왔을 때.
                th += 1    # 새로운 점수이므로 다음 번째로 넘어감
                result[th] = int(word)
            old_num = word # '10' 판단을 위한 임시변수
            
    return sum(result)