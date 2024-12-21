import sys
inp = sys.stdin.readline

cnt = inp().strip()

s = inp().strip()
summ = 0
for i in range(len(s)):
    summ += int(s[i])

print(summ)