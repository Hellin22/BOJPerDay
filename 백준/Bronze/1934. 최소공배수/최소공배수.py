import math

T = int(input()) 
results = []

for _ in range(T):
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    lcm = (A * B) // gcd
    results.append(lcm)

for result in results:
    print(result)