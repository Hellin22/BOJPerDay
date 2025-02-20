import sys
import heapq
inp = sys.stdin.readline

T = int(inp().strip())
for _ in range(T):

    team_cnt, problem_cnt, my_team_num, log_cnt = map(int, inp().strip().split())
    arr = [[0] * (problem_cnt+2) for _ in range(team_cnt+1)]
    for ttime in range(log_cnt): # 로그 개수
        team_num, problem_num, score = map(int, inp().strip().split())
        # 해당팀 제출시간[team_num][-1] = ttime, 해당팀 제출 횟수[team_num][0]+=1
        # 해당팀 문제 점수[team_num][problem_num]->max
        arr[team_num][0]+=1 # 제출 횟수
        arr[team_num][-1] = ttime # 마지막 제출 시간
        arr[team_num][problem_num] = max(arr[team_num][problem_num], score)

    hq = []

    for i in range(1, team_cnt+1):
        cur_team_submit_cnt = arr[i][0]
        cur_team_score = 0
        cur_team_last_submit_time = arr[i][-1]
        for j in range(1, problem_cnt+1):
            cur_team_score+=arr[i][j]
            '''
            점수(커야함), 제출횟수(적어야함), 제출시간(작아야함함), 팀번호
            첫번째 3번째만 - 붙이기
            '''
        heapq.heappush(hq, [-cur_team_score, cur_team_submit_cnt, cur_team_last_submit_time, i])

    res = 0
    while hq:
        res+=1
        curs = heapq.heappop(hq)
        if curs[3] == my_team_num:
            print(res)
            break