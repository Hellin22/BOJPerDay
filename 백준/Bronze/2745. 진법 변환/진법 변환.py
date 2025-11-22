import sys
input_data = sys.stdin.read().split()
N, B = input_data[0], int(input_data[1])

digits = list(N)
result = 0
for ch in digits:
    if '0' <= ch <= '9':
        val = ord(ch) - ord('0')
    else:
        val = ord(ch) - ord('A') + 10
    result = result * B + val

print(result)
