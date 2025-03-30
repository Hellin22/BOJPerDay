'''
cacheSize == 0~3 숫자임
cities는 도시의 이름 == "Jeju"  100,000개
(대소문자 구분 없음 -> 대소문자가 바껴서 들어온다는 의미? 맞네)
-> cities에는 lower 추가해주기
'''
def solution(cacheSize, cities):
    answer = 0
    cache = dict()
    curTime = 0
    for i in range(len(cities)):
        curTime+=1
        sttr = cities[i].lower()
        if sttr in cache:
            # 있는 경우
            answer+=1
            cache[sttr] = curTime
        else:
            # 없는 경우
            answer+=5
            if cacheSize == 0: continue
            # dict의 크기는 3을 넘어가면 안됨
            if len(cache) < cacheSize:
                cache[sttr] = curTime
            else:
                delKey = ""
                delVal = 1000000
                for key, val in cache.items():
                    if delVal > val:
                        delKey, delVal = key, val
                # print(delKey)
                del cache[delKey]
                
                cache[sttr] = curTime
        
    
    # 여기서 중요한것 -> 현재 캐시에 있는것이 무엇인지 + 캐시에서 빼야할게 무엇인지
    # dict로 진행 -> if dict에 없다 -> cachesize는 최대 3이니까 다 돌아봐도 됨
    # dict로 진행 -> if dict에 있다 -> 값 바꿔주기(ans+=1)
    # elif dict에 없다 -> dict를 돌면서 value가 가장 낮은거를 빼고 현재꺼 추가하기 (ans+=5)
    # 제일 처음에는 없으니까 5추가해야함
    # 현재 시간도 저장해놔야함. -> 0으로 시작하자.
    
    
    
    
    return answer