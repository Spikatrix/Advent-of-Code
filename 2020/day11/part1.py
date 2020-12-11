import sys
import copy

seats = [list(line.strip()) for line in sys.stdin]
row_len = len(seats)
col_len = len(seats[0])

def adjacent_count(index_r, index_c):
    adjacent = 0

    if index_r > 0 and index_c > 0 and seats[index_r - 1][index_c - 1] == '#':
        adjacent += 1
    if index_r > 0 and seats[index_r - 1][index_c] == '#':
        adjacent += 1
    if index_r > 0 and index_c < col_len - 1 and seats[index_r - 1][index_c + 1] == '#':
        adjacent += 1
    if index_c < col_len - 1 and seats[index_r][index_c + 1] == '#':
        adjacent += 1
    if index_r < row_len - 1 and index_c < col_len - 1 and seats[index_r + 1][index_c + 1] == '#':
        adjacent += 1
    if index_r < row_len - 1 and seats[index_r + 1][index_c] == '#':
        adjacent += 1
    if index_r < row_len - 1 and index_c > 0 and seats[index_r + 1][index_c - 1] == '#':
        adjacent += 1
    if index_c > 0 and seats[index_r][index_c - 1] == '#':
        adjacent += 1

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
            elif adjacent >= 4 and seat == '#':
                temp_seats[index_r][index_c] = 'L'
                changed = True
    seats = copy.deepcopy(temp_seats)

count = 0
for seat_row in seats:
    for seat in seat_row:
        if seat == '#':
            count += 1
print(count)
