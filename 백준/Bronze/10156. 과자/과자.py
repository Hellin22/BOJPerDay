K, N, M = map(int, input().split())
total_cost = K * N
if total_cost > M:
    print(total_cost - M)
else:
    print(0)
