import sys
from collections import Counter
inp = sys.stdin.readline

cnt = int(inp())

books = [inp().strip() for _ in range(cnt)]
counter = Counter(books)
max_count = max(counter.values())

result = min(book for book, count in counter.items() if count == max_count)
print(result)