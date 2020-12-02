import sys
input_lines = [line for line in sys.stdin]

valid = 0
for line in input_lines:
    line = line.split()
    range_string = line[0].split('-')
    low, high = [int(value) for value in range_string]

    single_valid = (line[2][low - 1] == line[1][0]) ^ (line[2][high - 1] == line[1][0])
    if single_valid:
        valid += 1

print(valid)
