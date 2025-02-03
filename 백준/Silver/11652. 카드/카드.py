import sys
from collections import Counter
inp = sys.stdin.readline

cnt = int(inp().strip())
llist = [int(inp()) for _ in range(cnt)]
count = Counter(llist)

max_cnt = max(count.values())

result = min(num for num, num_cnt in count.items() if num_cnt == max_cnt)
print(result)
