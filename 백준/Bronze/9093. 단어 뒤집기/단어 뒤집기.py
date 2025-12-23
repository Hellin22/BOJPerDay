import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    words = input().split()
    reversed_words = []
    for w in words:
        reversed_words.append(w[::-1])
    print(" ".join(reversed_words))
