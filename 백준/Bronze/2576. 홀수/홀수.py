nums = [int(input()) for _ in range(7)]
odds = [n for n in nums if n % 2 == 1]

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
