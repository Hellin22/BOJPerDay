import sys
inp = sys.stdin.readline

n = int(inp().strip()) # 단어의 개수
arr = []
for i in range(n):
    arr.append(inp().strip())

arr = list(set(arr))
arr.sort(key=lambda x:(len(x), x))

print("\n".join(arr))