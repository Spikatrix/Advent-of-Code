import sys
inputs = [int(line) for line in sys.stdin]

a, b, c = 0, 0, 0
for i in inputs:
    for j in inputs:
        for k in inputs:
            if i + j + k == 2020:
                a, b, c = i, j, k
                break
        if a * b * c != 0:
            break
    if a * b * c != 0:
        break

print(a * b * c);
