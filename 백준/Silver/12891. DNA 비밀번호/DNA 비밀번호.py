s, p = map(int, input().strip().split())

sttr = list(input().strip())
alpha_able_cnt = list(map(int, input().strip().split()))
# a b c d
# A C G T
for i in range(len(sttr)):
    if sttr[i] == "A": sttr[i] = "a"
    elif sttr[i] == "C": sttr[i] = "b"
    elif sttr[i] == "G": sttr[i] = "c"
    else: sttr[i] = "d"

alpha_cnt = [0, 0, 0, 0]
res=0
for i in range(p): # 0 ~ p-1 까지 모두 넣기기
    alpha_cnt[ord(sttr[i])-97] +=1
flag = True
for j in range(4):
    if alpha_cnt[j] < alpha_able_cnt[j]:
        flag = False
        break
if flag:
    res+=1

for i in range(p, s):
    # i와 i-p를 비교해야함. 즉, i를 추가하고 i-p를 빼야함.
    alpha_cnt[ord(sttr[i])-97]+=1
    alpha_cnt[ord(sttr[i-p])-97]-=1
    flag = True
    for j in range(4):
        if alpha_cnt[j] < alpha_able_cnt[j]:
            flag = False
            break
    if flag: 
        res+=1

print(res)