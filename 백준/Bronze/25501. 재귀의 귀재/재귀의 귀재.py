import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global cnt
    cnt += 1
    
    if l >= r:        # 중앙까지 왔으면 팰린드롬
        return 1
    elif s[l] != s[r]:  # 같지 않으면 팰린드롬 아님
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())
for _ in range(t):
    s = input().rstrip()
    cnt = 0
    result = isPalindrome(s)
    print(result, cnt)
