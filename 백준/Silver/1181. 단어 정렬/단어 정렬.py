import sys

inp = sys.stdin.readline

t = int(inp().strip())
strs = []
for i in range(t):
    strs.append(inp().strip())

sett = set(strs) # 중복 제거

sorted_words = sorted(sett, key=lambda x: (len(x), x))
print("\n".join(sorted_words))