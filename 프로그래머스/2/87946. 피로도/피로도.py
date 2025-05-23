'''
던전 탐험 시작을 위해 (드갈때 "최소 필요 피로도", 던전 끝날때 소모되는 "소모 피로도")

-> 최대한 많은 던전 탐험
현재 피로도는 k
던전별 피로도 dungeons(2차 배열)
최대 던전 수 return

던전 개수는 최대 8개임. -> 완탐 -> dp로는 어떻게 해결?
'''

import itertools
def solution(k, dungeons):
    answer = -1
    
    
    llist = [i for i in range(len(dungeons))]
    perm = list(itertools.permutations(llist))
    maxx = -1
    
    def check_perm(k, i):
        cur_k = k
        for idx, val in enumerate(perm[i]):
            if dungeons[val][0] > cur_k:
                return idx
            else: cur_k -= dungeons[val][1]
            
        return len(dungeons)
    
    for i in range(len(perm)):
        maxx = max(maxx, check_perm(k, i))
    
    
    return maxx