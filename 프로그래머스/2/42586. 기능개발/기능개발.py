def solution(progresses, speeds):
    answer = []
    
    # 며칠 걸리는지는 상관없음
    n = len(speeds)
    cur = 0 # 0번째 부터 speeds만큼 progresses 증가시키기
    while cur < n:
        for i in range(cur, n):
            # cur ~ n-1까지 모두 speeds만큼 progresses 증가시키기
            if progresses[i] < 100: # 100보다 작다면
                progresses[i]+=speeds[i] # speeds만큼 증가
        # 만약 progresses[cur]이 100보다 커진다면? answer에 추가할 준비
        
        if progresses[cur] >= 100:
            cnt = 0
            while cur < n:
                if progresses[cur] < 100:
                    break
                cnt+=1
                cur+=1
                    
            answer.append(cnt)
    return answer