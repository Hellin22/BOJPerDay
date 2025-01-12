n, m = map(int, input().split())
matrix_a = []
for _ in range(n):
    matrix_a.append(list(map(int, input().split())))

matrix_b = []
for _ in range(n):
    matrix_b.append(list(map(int, input().split())))

matrix_c = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_c.append(row)

for row in matrix_c:
    print(" ".join(map(str, row)))