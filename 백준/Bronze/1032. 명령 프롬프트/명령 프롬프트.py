n = int(input())
files = [input().strip() for _ in range(n)]

pattern = list(files[0])

for i in range(1, n):
    for j in range(len(pattern)):
        if pattern[j] != files[i][j]:
            pattern[j] = '?'

print("".join(pattern))
