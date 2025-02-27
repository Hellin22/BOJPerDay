import sys
inp = sys.stdin.readline

n, r, c = map(int, inp().strip().split())
res = 0
def z(m, a, b):
    global res
    if m == 1:
        for i in range(2):
            for j in range(2):
                if (a+i, b+j) == (r, c):
                    print(res)
                    exit()
                res+=1
        return
    if a <= r <= a+pow(2, m-1)-1 and b <= c <= b+pow(2, m-1)-1:
        z(m-1, a, b)
    else: res += pow(2, m-1) * pow(2, m-1)
    if a <= r <= a+pow(2, m-1)-1 and b+pow(2, m-1) <= c <= b+pow(2, m-1) + pow(2, m-1)-1:
        z(m-1, a, b+pow(2, m-1))
    else: res += pow(2, m-1) * pow(2, m-1)

    if a+pow(2, m-1) <= r <= a+pow(2, m-1) + pow(2, m-1)-1 and b <= c <= b+pow(2, m-1)-1:
        z(m-1, a+pow(2, m-1), b)
    else: res += pow(2, m-1) * pow(2, m-1)
    if a+pow(2, m-1) <= r <= a+pow(2, m-1) + pow(2, m-1)-1 and b+pow(2, m-1) <= c <= b+pow(2, m-1) + pow(2, m-1)-1:
        z(m-1, a+pow(2, m-1), b+pow(2, m-1))
    else: res += pow(2, m-1) * pow(2, m-1)


z(n, 0, 0)