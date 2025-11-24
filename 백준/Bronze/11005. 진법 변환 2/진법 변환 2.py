N, B = map(int, input().split())

digits = []

while N > 0:
    r = N % B
    N //= B

    if r < 10:
        digits.append(str(r))
    else:
        digits.append(chr(r - 10 + ord('A')))

print(''.join(reversed(digits)))
