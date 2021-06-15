def solution(cacheSize, cities):
    if not cacheSize: return 5*len(cities)
    
    cache = [0] * cacheSize
    result = 0
    
    while cities:
        s = cities.pop().lower()
        if s in cache:                  # 캐시 안에 도시 이름이 있으면
            result += 1                 # cache hit
            cache.pop(cache.index(s))   # 캐시에서 도시이름 제거
        else:                           # 캐시 안에 도시 이름 없으면
            result += 5                 # cache miss
            cache.pop(0)                # 캐시에서 가장 오래된거 제거
        cache.append(s)                 # 캐시에 새로 넣어 줌
    
    return result