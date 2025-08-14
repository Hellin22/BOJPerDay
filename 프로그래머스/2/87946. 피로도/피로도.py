from itertools import permutations
def solution(k, dungeons):
    
    '''
    최소 필요 피로도
    소모 피로도
    1~8개의 던전
    '''
    
    
    maxx = 0
    cnt = len(dungeons)
    arr = [k for k in range(cnt)]
    llist = list(permutations(arr, cnt))
    
    def go_per(llist, health):
        ans = 0
        for i in llist:
            if health >= dungeons[i][0]:
                ans+=1
                health -= dungeons[i][1]
            else: break
        return ans
    
    
    for i in range(len(llist)):
        maxx = max(maxx, go_per(llist[i], k))
        
    return maxx
    