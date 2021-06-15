import sys
sys.stdin = open('input.txt')
# from pandas import DataFrame

for tc in range(1, int(input())+1):
    text = [input() for _ in range(5)]
    result = ''

    # 5개의 단어들 중 어떤 단어가 가장 긴지 확인하고 max저장
    # text = ['ABCDE', 'abcde', '01234', 'FGHIJ', 'fghij']
    max_len = 0
    for t in text:
        if max_len < len(t):
            max_len = len(t)

    for r in range(max_len):        # 가장 긴 단어에 맞춘 r
        for c in range(len(text)):  # 5개의 단어랬으니 c는 5
            if r >= len(text[c]):   # 만약 r(열이 될 예정)이 text[c]의 길이보다 같거나 길면
                result += ''        # 길이 초과이므로 result에 더하지 않는다
            else:                   # 만약 r이 text[c]보다 작으면 길이 범위 내이므로
                result += text[c][r]   # 추가해준다

    print("#{} {}".format(tc, result))
