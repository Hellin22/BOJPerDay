import sys
inp = sys.stdin.readline

s = inp().strip()
arr = [-1] * 26

for i in range(len(s)):
    if(arr[ord(s[i])-97] == -1):
        arr[ord(s[i])-97] = i

print(" ".join(map(str, arr)))