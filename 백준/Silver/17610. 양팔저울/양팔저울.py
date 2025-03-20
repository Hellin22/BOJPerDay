k = int(input().strip())
llist = list(map(int, input().strip().split()))
llist.sort()
st = set()
st.add(llist[0])
for i in range(1, k):
    tmpst = set()
    tmpst.add(llist[i])
    for key in st:
        if llist[i]-key > 0:
            tmpst.add(llist[i]-key)
        elif llist[i] -key < 0:
            tmpst.add(key - llist[i])
        tmpst.add(llist[i]+key)
    for key in tmpst:
        st.add(key)
summ = sum(llist)
print(summ-len(st))