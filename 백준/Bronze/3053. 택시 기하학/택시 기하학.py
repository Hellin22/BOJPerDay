import math
R = int(input())
euclidean_area = math.pi * R * R
taxicab_area = 2 * R * R
print(f"{euclidean_area:.6f}")
print(f"{taxicab_area:.6f}")