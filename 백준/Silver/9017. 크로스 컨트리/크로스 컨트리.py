import sys
import heapq
inp = sys.stdin.readline

t= int(inp().strip())
for _ in range(t):
    n= int(inp().strip())
    team = list(map(int, inp().strip().split()))
    team_max = -1
    dtt = dict()
    for i in team:
        team_max = max(team_max, i)
        dtt[i] = dtt.get(i, 0) + 1
    for i in range(1, team_max+1):
        if dtt[i] != 6:
            # team에서 없애야함.
            for j in range(dtt[i]):
                team.remove(i)
    team = [0] + team
    teamres = [0] * (team_max+1)
    teamfive = [0] * (team_max+1)
    teamcnt = [0] * (team_max+1)
    for i in range(1, len(team)):
        teamcnt[team[i]]+=1
        if teamcnt[team[i]] <= 4:
            teamres[team[i]]+=i
        if teamcnt[team[i]] == 5:
            teamfive[team[i]] = i
    pq = []
    for i in range(1, team_max+1):
        if teamcnt[i] == 6:
            heapq.heappush(pq, (teamres[i], teamfive[i], i))
    print(heapq.heappop(pq)[2])
