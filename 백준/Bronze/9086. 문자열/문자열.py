import sys
inp = sys.stdin.readline

t = int(inp().strip())

for i in range(t):
    s = inp().strip()
    # print("".join([s[0], s[len(s)-1]]))
    # print(s[len(s)-1])
    print("".join([s[0], s[-1]]))