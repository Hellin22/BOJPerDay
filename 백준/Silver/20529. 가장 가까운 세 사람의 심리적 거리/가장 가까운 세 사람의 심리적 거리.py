import sys

inp = sys.stdin.readline

testcase = int(inp().strip())
mbti_map = {
    0: "ESTJ", 1: "ESTP", 2: "ESFJ", 3: "ESFP",
    4: "ENTJ", 5: "ENTP", 6: "ENFJ", 7: "ENFP",
    8: "ISTJ", 9: "ISTP", 10: "ISFJ", 11: "ISFP",
    12: "INTJ", 13: "INTP", 14: "INFJ", 15: "INFP"
}
distance = [[0] * 16 for _ in range(16)]
for i in range(16):
    for j in range(16):
        str1 = mbti_map.get(i)
        str2 = mbti_map.get(j)
        for k in range(4):
            if str1[k] != str2[k]:
                distance[i][j]+=1

resList = []
while testcase != 0:
    testcase-=1
    res = 123456789
    flag = True
    n = int(inp().strip()) # 사람의 수
    arr = [0] * 16
    llist = list(inp().split())
    for i in range(len(llist)):
        if llist[i] == "ESTJ":
            arr[0]+=1
        elif llist[i] == "ESTP":
            arr[1]+=1
        elif llist[i] == "ESFJ":
            arr[2]+=1
        elif llist[i] == "ESFP":
            arr[3]+=1
        elif llist[i] == "ENTJ":
            arr[4]+=1
        elif llist[i] == "ENTP":
            arr[5]+=1
        elif llist[i] == "ENFJ":
            arr[6]+=1
        elif llist[i] == "ENFP":
            arr[7]+=1
        elif llist[i] == "ISTJ":
            arr[8]+=1
        elif llist[i] == "ISTP":
            arr[9]+=1
        elif llist[i] == "ISFJ":
            arr[10]+=1
        elif llist[i] == "ISFP":
            arr[11]+=1
        elif llist[i] == "INTJ":
            arr[12]+=1
        elif llist[i] == "INTP":
            arr[13]+=1
        elif llist[i] == "INFJ":
            arr[14]+=1
        elif llist[i] == "INFP":
            arr[15]+=1

    # 1. 하나가 3개 이상이면 0 출력임
    for i in range(16):
        if arr[i] >= 3: 
            res = 0
            flag = False
            break

    # 2. 3개 이상이 없음.
    if(flag):
        # 2. 2개가 존재하는 경우 -> 2중 반복문(모든 경우를 다 보긴 해야함.)
        for i in range(16):
            if arr[i] == 2: # 2개가 존재하는 경우에는 1개만 더 추가하면 됨
                for j in range(16):
                    if j == i: continue 
                    if arr[j] != 0: # 존재하긴 한다면 어떤거든 됨 -> 0이 아님 
                        res = min(res, abs(distance[i][j])*2)
        
        # 3. 1개가 존재하는 경우 -> 3중 반복문 봐야함.
        for i in range(16):
            if arr[i] == 1:
                for j in range(16):
                    if i == j: continue
                    if arr[j] == 1:
                        for k in range(16):
                            if k == i or k == j: continue
                            if arr[k] == 1:
                                res = min(res, distance[i][j] + distance[i][k]+distance[j][k])
    resList.append(res)

print("\n".join(map(str, resList)))