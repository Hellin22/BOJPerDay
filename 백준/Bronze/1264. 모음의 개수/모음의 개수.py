while True:
    line = input()
    if line == "#":
        break

    line = line.lower()
    count = 0

    for ch in line:
        if ch in "aeiou":
            count += 1

    print(count)
