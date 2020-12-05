import sys

input_lines = [line.strip() for line in sys.stdin]

all_seats = [row * 8 + col for row in range(1, 127) for col in range(8)]
seats_in_list = []
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

    seat_id = row * 8 + col
    seats_in_list.append(seat_id)
    all_seats.remove(seat_id)

my_seat = [seat_id for seat_id in all_seats 
               if seat_id + 1 in seats_in_list and seat_id -1 in seats_in_list]
print(my_seat[0])
