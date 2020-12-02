import sys
input_lines = [line for line in sys.stdin]

valid = 0
for line in input_lines:
    line = line.split()
    range_string = line[0].split('-')
    low, high = [int(value) for value in range_string]

    if line[2].count(line[1][0]) >= low and line[2].count(line[1][0]) <= high:
        valid += 1

print(valid)
