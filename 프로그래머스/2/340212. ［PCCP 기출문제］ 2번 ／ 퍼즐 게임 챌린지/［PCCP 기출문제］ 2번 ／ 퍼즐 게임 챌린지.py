def solution(diffs, times, limit):
    answer = limit
    
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left+right)//2
        res = times[0]
        for i in range(1, len(times)):
            res += (times[i] + times[i-1]) * max(0, diffs[i]-mid) + times[i]
        
        if res > limit: # 이건 못써먹음
            left = mid+1
        elif res <= limit: # 써먹을 수 있음.
            answer = min(answer, mid)
            right = mid-1
            
    return answer # 숙련도는 양의 정수
    