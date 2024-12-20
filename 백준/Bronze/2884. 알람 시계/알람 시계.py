import sys
inp = sys.stdin.readline

a,b=map(int, inp().split())

if(b < 45):
    b = 60-45+b
    a-=1
else:
    b -= 45

if(a == -1):
    a = 23

print(a, b)