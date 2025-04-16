'''
[[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

[[10, 14], [11, 13], [5, 12], [4, 8], [3, 7], [4, 5], [1, 4]]
'''


def solution(targets):
    answer = 0
    targets.sort(key = lambda x: -x[1])
    
    
    cur = targets[0]
# [[10, 14], [12, 13], [5, 12], [4, 8], [3, 7], [4, 5], [1, 4]]
    answer +=1
    for s, e in targets:
        if cur[0] < e: 
            cur[0] = max(cur[0], s)
        else: 
            answer+=1
            cur = [s, e]
    
    
    return answer