import sys
inp = sys.stdin.readline

n = int(inp())
# set을 사용해야할거 같음.
# 대소문자 구별 안하니까 대문자면 소문자도 or 소문자면 대문자도 추가해야할듯
arr = []
st = set()
for i in range(n):
    flag = False
    strr = inp().strip()

    llist = strr.split() # "Save", "As"가 저장
    idx = 0 # idx 추가해줄 변수
    for j in range(len(llist)): # "Save"
        if ord(llist[j][0]) not in st and ord(llist[j][0])+32 not in st and ord(llist[j][0])-32 not in st:
            st.add(ord(llist[j][0]))

            flag = True
        if flag: break
        idx = idx + len(llist[j]) + 1
    if flag: # 단어의 처음 부분이 단축키로 등록된것.
        res = []
        for l in range(len(strr)):
            if idx == l:
                res.append("[")
                res.append(strr[l])
                res.append("]")
            else: res.append(strr[l])

        print(''.join(map(str, res)))
        continue
    # 2. 첫글자가 선정 안된것 -> strr을 처음부터 쭊 돌면서 공백 제외하고 등록 안된거 있으면 그거 선정
    res = []
    flag = False
    for j in range(len(strr)):
        if ord(strr[j]) != 32 and ord(strr[j]) not in st and ord(strr[j]) + 32 not in st and ord(strr[j]) - 32 not in st and not flag:
            res.append("[")
            res.append(strr[j])
            res.append("]")
            flag = True
            st.add(ord(strr[j]))
        else: res.append(strr[j])
    print(''.join(map(str, res)))