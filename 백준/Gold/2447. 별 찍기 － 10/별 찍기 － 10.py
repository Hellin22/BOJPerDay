import sys

inp = sys.stdin.readline

'''
2번째 줄의 가운데부분은 모두 공백처리해야함.
recursion은 9번 해야함. 언제까지? 길이가 3이 될때까지
'''

def empty_recursion(n, x, y):
    for i in range(n):
        for j in range(n):
            arr[x+i][y+j] = " "

def recursion(n, x, y):

    if n == 1:
        arr[x][y] = "*"
        return
    
    n //= 3
    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                empty_recursion(n, x+i*n, y+j*n)
            else: recursion(n, x+i*n, y+j*n)

n = int(inp().strip())
arr = [[-1] * n for _ in range(n)]
recursion(n, 0, 0)

print("\n".join("".join(row) for row in arr))