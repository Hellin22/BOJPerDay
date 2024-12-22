import sys
inp = sys.stdin.readline

rows, cols = 9, 9

arr = [[0 for _ in range(cols)] for _ in range(rows)]
maxx = -1
x,y = 0,0
for i in range(rows):
    listt = list(map(int, inp().split()))
    for j in range(len(listt)):
        arr[i][j] = listt[j]
        if(maxx < arr[i][j]):
            maxx = arr[i][j]
            x,y = i,j

print(maxx)
print(" ".join(map(str, [x+1, y+1])))