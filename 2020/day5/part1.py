import sys

input_lines = [line.strip() for line in sys.stdin]

seat_id_list = []
for line in input_lines:
    low, high = 0, 127

    for char in line[:7]:
        if char == 'F':
            high -= ((high - low) // 2 + 1)
        elif char == 'B':
            low += ((high - low) // 2 + 1)

    row = low

    low, high = 0, 7
    for char in line[7:]:
        if char == 'L':
            high -= ((high - low) // 2 + 1)
        elif char == 'R':
            low += ((high - low) // 2 + 1)

    col = high

    seat_id_list.append(row * 8 + col)

print(max(seat_id_list))
