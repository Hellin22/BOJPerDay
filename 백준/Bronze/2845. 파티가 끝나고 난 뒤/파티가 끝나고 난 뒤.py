L, P = map(int, input().split())
nums = list(map(int, input().split()))
actual = L * P

for n in nums:
    print(n - actual, end=' ')
