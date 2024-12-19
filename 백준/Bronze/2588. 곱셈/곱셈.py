import sys
inp = sys.stdin.readline

a=int(inp())
b=int(inp())

res = a*b
thr=b%10
fou=(b%100-thr)/10
fiv=(b-thr-fou*10)/100

print(int(thr*a))
print(int(fou*a))
print(int(fiv*a))
print(res)