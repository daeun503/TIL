def solution(begin, target, words):
    if not target in words: return 0
    words.append(begin)  # bfs에서 index로 사용하기 때문에 begin 넣고 시작
    N = len(words)      
    visited = [0] * N    # 방문 표시 (거리체크)
    
    # 단어 한 글자만 다른지 판단하는 함수 (이거 제대로 안하면 tc 3 에러)
    # 이전에 len(set(v) & set(w)) == len(v) - 1 라고 썼더니 에러가 발생했다.
    # hhh에서 hht로 혹은 hht에서 hhh로 변환할 때 판단이 제대로 안 되기 때문
    def check(a, b):
        if len(a) == len(b):
            diff = 0
            for i, j in zip(a, b):
                if i != j: diff += 1
        return True if diff == 1 else False
    
    def bfs(s):
        q = [s]
        while q:
            v = q.pop(0)
            for i in range(N):
                w = words[i]
                # 아직 방문 안 했고 글자가 한 글자 차이나면 실행. 
                if visited[i] == 0 and check(v, w):
                    q.append(w)
                    visited[i] = visited[words.index(v)] + 1
        return visited[words.index(target)]
    
    return bfs(begin)