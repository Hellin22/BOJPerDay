import sys
inp=sys.stdin.readline

a=int(inp())

maxx=-1000001
minn=1000001

arr=list(map(int,inp().split()))

for i in arr:
    if(i < minn):
        minn = i
    if(i > maxx):
        maxx = i


print(minn, maxx)
