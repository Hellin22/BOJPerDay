x_list = []
y_list = []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for xi in x_list:
    if x_list.count(xi) == 1:
        x4 = xi
        break

for yi in y_list:
    if y_list.count(yi) == 1:
        y4 = yi
        break

print(x4, y4)
