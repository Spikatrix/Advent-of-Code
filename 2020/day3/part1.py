import sys
input_lines = [line.strip() for line in sys.stdin]

x = 0
count = 0
for line in input_lines:
    if line[x] == '#':
        count += 1
    x = (x + 3) % len(line)

print(count)
