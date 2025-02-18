import sys
inp = sys.stdin.readline

# 처음 주어진 단어와 비슷한 단어 찾기
# 비슷하다 == 첫번째 단어에 문자 하나 더하고 빼고 바꾸면 같아지는것
# 첫번째 단어와 비교 -> 알파벳 배열 2개로 처리 가능?
# 단어는 총 100개, 단어의 길이는 10 이하 -> 1000번 * 26개 알파벳 -> 복잡도 안높음
# A는 65 -> Z는 90
n = int(inp().strip())
strr = inp().strip()
arr = [0]*26
res = 0
for i in range(len(strr)):
    arr[ord(strr[i])-65]+=1

for _ in range(n-1):
    tmp_str = inp().strip()
    tmp_arr = [0] * 26
    for i in range(len(tmp_str)):
        tmp_arr[ord(tmp_str[i])-65]+=1
    ta, tb = 0, 0
    for i in range(26):
        if arr[i] == tmp_arr[i]: continue
        elif arr[i] - tmp_arr[i] > 0: ta+=(arr[i]-tmp_arr[i])
        elif tmp_arr[i] - arr[i] > 0: tb+=(tmp_arr[i]-arr[i])
    if (ta, tb) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        res+=1
print(res)

'''
4
DOG
'''