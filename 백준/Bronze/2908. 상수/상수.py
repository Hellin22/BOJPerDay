import sys
inp = sys.stdin.readline

a,b = inp().split()

c,d = a[::-1], b[::-1]

print(max(int(c), int(d)))