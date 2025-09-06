def solution(diffs, times, limit):
    '''
    n개의 퍼즐 제한시간내로 풀어야함
    
    diff = 난이도
    time_cur = 현재 퍼즐의 소요 시간
    time_prev = 이전 퍼즐 소요시간
    level = 내 숙련도
    
    1. diff <= level이면 time_cur로 바로 해결
    
    2. diff > level이면 퍼즐은 diff-level 만큼 틀림
    퍼즐 틀릴때마다 time_cur만큼의 시간 추가 사용 + time_prev 만큼 시간으로 이전 퍼즐을 풀고 와야함.
    (diff-level+1) * time_cur + time_prev
    (diff - level) * (time_cur+time_prev) + time_cur
    
    limit 시간 내로 퍼즐을 모두 해결하기 위한 숙련도의 최소값 -> 1부터 증가
    
    diffs[0] = 1
    
    이진탐색으로 수정?
    '''
    
    
    cl, cr = 1, max(diffs)+1
    minn = 10000000000000000
    cnt = 0
    while cl <= cr:
        level = (cl+cr) // 2
        
        time_prev = times[0]
        sum_time = times[0]
        flag = True
        
        for diff, time_cur in zip(diffs[1:], times[1:]):
            # 1. diff <= level
            if diff <= level:
                sum_time += time_cur
                if sum_time > limit:
                    cl = level+1
                    flag = False
                    break
                time_prev = time_cur
            else:
                sum_time += (diff-level) * (time_cur + time_prev) + time_cur
                if sum_time > limit:
                    flag = False # level을 더 늘려야함
                    cl = level+1
                    break
                time_prev = time_cur
                
        if flag:
            minn = min(minn, level)
            cr = level-1 # level을 줄여야함
    return minn