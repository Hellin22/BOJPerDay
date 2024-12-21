import sys
inp = sys.stdin.readline

s=inp().rstrip()

if(s==s[::-1]): print(1)
else: print(0)