'''
jobs는 [s, i] s는 요청시점, i는 소요시간
우선순위 높은거는 i가 낮은거
heap에 추가할때에는 (i, s)로

구해야하는 거는 반환시간의 평균의 정수부


'''
from heapq import heappush, heappop

def solution(jobs):
    # [[0, 3], [1, 9], [3, 5]] = jobs들
    # 들어온 시간, 걸리는 시간 -> 우선순위는 걸리는 시간
    answer = 0
    n = len(jobs)
    hq = []

    # 하니씩 pop 할 예정
    jobs.sort(key = lambda x: (-x[0], -x[1])) # pop 할 예정이니까 들러온시간, 걸리는시간 음수로 처리
    
    cur_time = 0
    cur_time += jobs[-1][0] + jobs[-1][1] # 제일 우선순위가 높은거는 추가해주기
    answer += cur_time - jobs[-1][0]
    # 작업 종료시간 - 요청시간
    jobs.pop() # 빼기
    
    while jobs or hq:
        while jobs and jobs[-1][0] <= cur_time: # jobs에 작업이 남아있고 현재 시간보다 작거나 같은걸들만 hq에 추가
            heappush(hq, (jobs[-1][1], jobs[-1][0])) # 작업시간, 요청시간
            jobs.pop()
        
        if not hq and jobs: # cur_time보다 늦은 작업만 존재하기 때문에 문제
            cur_time = jobs[-1][0] # 요청시간으로 변경
            heappush(hq, (jobs[-1][1], jobs[-1][0]))
            jobs.pop()            
            
        a, b = heappop(hq) # 작업시간, 요청시간
        cur_time += a
        answer += cur_time - b # 작업 끝난시간 - 요청시간

    
    
    return answer // n