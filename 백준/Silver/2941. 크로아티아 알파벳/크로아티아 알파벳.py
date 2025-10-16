import sys

inp = sys.stdin.readline

n = inp().strip()

dt = {1:"c=", 2:"c-",3:"dz=",4:"d-",5:"lj",6:"nj",7:"s=",8:"z="}
for i in range(1, 9):
    n = n.replace(dt[i], "!")
print(len(n))