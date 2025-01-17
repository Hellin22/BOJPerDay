import sys

inp = sys.stdin.readline

# 1. 칭호를 모두 입력받음
# 2. 칭호[1]에 대해서 sort 진행
# 3. 이게 안되네... 결국 최악의 경우에는 모든 경우 살펴야함.
# 4. 점수만 주어지면 바로 칭호를 찾을 수 있어야함.
# 이진탐색?
# n개의 칭호, m명의 사람 둘다 10만개
# 사람 m명 -> log n번 탐색 -> mlogn -> log2 십만 *0정도? 그러면 가능할듯?

# 이진탐색이란?
# start, end를 통해서 만약 원하는 값(입력 숫자)이 start+end/2보다 작다면 end를 갱신
# 그러면 end = start+end/2-1
# 반대라면? start = start+end/2+1
# 언제까지 반복? start가 end와 같아질때 또는 start가 end보다 커질때? 
res = []
n, m = map(int, inp().strip().split(" "))
llist = [0] * n # 칭호의 개수
for i in range(n):
    strs = inp().split(" ")
    # 2번째꺼는 int로 넣어놔야함.
    llist[i] = ([strs[0], int(strs[1])])

def binary_search(score):
    start, end = 0, n-1
    result = ""
    while(start <= end):
        mid = (start + end)//2
        if score <= llist[mid][1]:
            result = llist[mid][0]
            end = mid-1
        else:
            start = mid+1
    return result


for i in range(m): 
    score = int(inp())
    res.append(binary_search(score))

for i in range(len(res)):
    print(res[i])