import sys
inputs = [int(line) for line in sys.stdin]

a, b = 0, 0
for i in inputs:
    for j in inputs:
        if i != j and i + j == 2020:
            a, b = i, j
            break
    if a * b != 0:
        break

print(a * b);

