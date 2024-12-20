import sys
inp=sys.stdin.readline

a,b=map(int, inp().split())
c=int(inp().strip())

d = (c-c%60)/60 # 시간
c %= 60 # 분

a+=d # 시간 
b+=c # 분

if(b >= 60):
    b-=60
    a+=1
if(a >= 23):
    a%=24

print(int(a),b)