import sys
inp = sys.stdin.readline

a,b=map(int,inp().split())

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")