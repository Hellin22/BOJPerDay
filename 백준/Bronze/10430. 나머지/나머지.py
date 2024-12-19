import sys
inp = sys.stdin.readline

a,b,c=map(int, inp().split())


print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
