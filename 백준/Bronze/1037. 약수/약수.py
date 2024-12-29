import sys
input = sys.stdin.read
data = input().split()

count = int(data[0])

divisors = list(map(int, data[1:]))

n = min(divisors) * max(divisors)

print(n)