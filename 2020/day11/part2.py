import sys
import copy

seats = [list(line.strip()) for line in sys.stdin]
row_len = len(seats)
col_len = len(seats[0])

def direction(x_vel, y_vel, index_r, index_c):
    while True:
        index_r += y_vel
        index_c += x_vel

        if index_r < 0 or index_c < 0 or index_r >= row_len or index_c >= col_len:
            break
        elif seats[index_r][index_c] == '#':
            return 1
        elif seats[index_r][index_c] == 'L':
            return 0
    return 0

def adjacent_count(index_r, index_c):
    adjacent = 0

    adjacent += direction(-1, -1, index_r, index_c)
    adjacent += direction(0, -1, index_r, index_c)
    adjacent += direction(1, -1, index_r, index_c)
    adjacent += direction(1, 0, index_r, index_c)
    adjacent += direction(1, 1, index_r, index_c)
    adjacent += direction(0, 1, index_r, index_c)
    adjacent += direction(-1, 1, index_r, index_c)
    adjacent += direction(-1, 0, index_r, index_c)

    return adjacent

changed = True
while changed:
    temp_seats = copy.deepcopy(seats)
    changed = False
    for (index_r, seat_row) in enumerate(seats):
        for (index_c, seat) in enumerate(seat_row):
            adjacent = adjacent_count(index_r, index_c)
            if adjacent == 0 and seat == 'L':
                temp_seats[index_r][index_c] = '#'
                changed = True
            elif adjacent >= 5 and seat == '#':
                temp_seats[index_r][index_c] = 'L'
                changed = True
    seats = copy.deepcopy(temp_seats)

count = 0
for seat_row in seats:
    for seat in seat_row:
        if seat == '#':
            count += 1
print(count)

