import sys

inp = sys.stdin.readline

s = inp().strip()
st = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        st.add(s[i:j+1])

print(len(st))