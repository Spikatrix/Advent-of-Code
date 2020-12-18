# Got some other work to do eek

import sys

input_lines = [line.strip() for line in sys.stdin]

for line in input_lines:
    line = [int(x) if x not in ['*', '+'] else x for x in line.split(' ')]
    acc = line.pop(0)
    for c in line:
        if c == '+' or c == '*':
            op = c
            continue

        if op == '+':
            acc += c
        elif op == '*':
            acc *= c
        print(acc)

