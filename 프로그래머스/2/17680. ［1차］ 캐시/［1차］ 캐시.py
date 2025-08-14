
def solution(cacheSize, cities):
    
    '''
    캐시 크기 얼마로 설정
    
    배열 순서대로 처리 -> 총 실행시간
    hit = 1
    miss = 5
    
    dict 사용?
    if hit면 ok
    elif miss면 
    
    '''
    if cacheSize == 0: return 5*len(cities)
    for i,ct in enumerate(cities):
        cities[i] = ct.upper()
    cache = dict()
    ans = 0
    for idx, ct in enumerate(cities):
        if len(cache) < cacheSize: # 캐시 용량 남아있으면
            if ct not in cache: # 만약 캐시에 존재안하면
                ans += 5 # miss기 때문
            else: #이미 캐시에 존재하면?
                ans+=1
                
            cache[ct] = idx # 캐시 데이터 갱신
            
        else: # 캐시 용량이 없음
            if ct not in cache: # 캐시에 없다면
                ans+=5 # miss
                del_k = "dfw"
                min_v = 9999999999
                for k, v in cache.items():
                    if v < min_v:
                        min_v = v
                        del_k = k
                del cache[del_k] # LRU 작동
                
            else: # 캐시에 이미 있다면
                ans+=1
                
            cache[ct] = idx
    return ans