import sys
inp = sys.stdin.readline
n = int(inp().strip())

llist = [list(map(int, inp().strip().split())) for _ in range(n)]

max_dist = -1
dist_sum = abs(llist[0][0] - llist[1][0]) + abs(llist[0][1] - llist[1][1]) #if n != 3 else 0

for i in range(1, n-1):
    cur_dist1 = abs(llist[i][0] - llist[i-1][0]) + abs(llist[i][1] - llist[i-1][1])
    cur_dist2 = abs(llist[i][0] - llist[i+1][0]) + abs(llist[i][1] - llist[i+1][1])
    new_dist = abs(llist[i-1][0] - llist[i+1][0]) + abs(llist[i-1][1] - llist[i+1][1])
    cur_sum = cur_dist1 + cur_dist2-new_dist
    if max_dist < cur_sum:
        max_dist = cur_sum
    dist_sum += cur_dist2

print(dist_sum-max_dist)