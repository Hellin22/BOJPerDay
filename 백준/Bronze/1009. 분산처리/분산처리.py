t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    cycle = []
    x = a % 10
    while x not in cycle:
        cycle.append(x)
        x = (x * a) % 10

    idx = (b - 1) % len(cycle)
    result = cycle[idx]
    
    print(result if result != 0 else 10)
