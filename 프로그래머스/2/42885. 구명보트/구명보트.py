def solution(people, limit):
    answer = 0    
    people.sort()
    right = len(people)-1
    left = 0
    
    while True:
        if left > right: break
        cur = 0
        cur += people[right]
        right-=1
        answer+=1
        if limit >= cur+people[left]: # 2명이 최대임?
             left+=1
    
    
    
    return answer