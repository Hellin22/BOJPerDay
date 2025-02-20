import sys
inp = sys.stdin.readline

strr = inp().strip()

# strr의 0과 1의 개수는 모두 짝수
# 0과 1 모두 절반을 제거해야함
# 사전순으로 제일 빠른것을 출력
# 사전순으로 빠르다 == 앞에 0이 나오기 + 뒤에 1이 나오기
# 앞에서부터 절반 1 빼기 + 뒤에서부터 절반 0 빼기
# strr을 돌면서 0개수 1개수 찾기
# 반복문 돌면서 strr 크기와 동일한 배열하나 만들고 모두 True로

arr = [True] * len(strr)
zeroCnt, oneCnt = 0, 0
for i in range(len(strr)):
    if strr[i] == "0": zeroCnt+=1
    else: oneCnt+=1

oneRes = 0
for i in range(len(strr)):
    if oneRes == oneCnt//2: break

    if strr[i] == "1": 
        arr[i] = False
        oneRes+=1
zeroRes = 0
for i in range(len(strr)-1, -1, -1):
    if zeroRes == zeroCnt//2: break

    if strr[i] == "0":
        arr[i] = False
        zeroRes+=1

res=""
for i in range(len(strr)):
    if arr[i] == True: res+=strr[i]
print(res)