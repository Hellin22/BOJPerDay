import sys
inp = sys.stdin.readline


# 두개를 합치는 == 연결 ==> 부모를 바꿔야함.(근데 일단 맨 처음에 저장해놔야하는데)
def union(x, y):
    rootx, rooty = find(x), find(y) # 부모 찾기
    if rootx == rooty: # 부모가 같으면 부모의 size 출력해주면 됨
        return size[rootx]
    else: # 부모가 달라서 size를 교체해줘야함. + 부모도 바꿔야하.
        # rootx, rooty중에 적은게 root가 안됨
        if size[rootx] < size[rooty]:
            rootx, rooty = rooty, rootx
        # rootx가 항상 부모가 된다.
        root[rooty] = rootx
        size[rootx] = size.get(rootx) + size.get(rooty)
        return size.get(rootx)


# 부모를 찾는 메서드
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


tc = int(inp())
for _ in range(tc):
    size = {}
    root = {}

    netCnt = int(inp())
    for i in range(netCnt):
        a, b = inp().strip().split()
        # a, b의 루트를 찾기 -> map으로 해야할듯? == union을 해야함.
        # 만약 root에 a가 없다면 추가
        if a not in root.keys():
            root[a] = a
            size[a] = 1
        if b not in root.keys():
            root[b] = b
            size[b] = 1
        print(union(a, b))