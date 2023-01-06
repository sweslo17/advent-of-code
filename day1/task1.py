max = 0
cur = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        if len(line.strip()) == 0:
            if cur > max:
                max = cur
            cur = 0
            continue
        cur += int(line.strip())
    if len(line.strip()) == 0:
        if cur > max:
            max = cur
print(max)
