# 3D was hurting my head but I think I figured it out
# But now I realize I don't understand their example

# Update: I just realized the size of the thing increases every
#         cycle but I still don't understand the example ;-;

import sys

input_lines = [line.strip() for line in sys.stdin]
row_len = len(input_lines)
col_len = len(input_lines[0])
cube = {0: []}

offset = 1
for line in input_lines:
    cube[0].append([state for state in line])

def print_cube():
    for key, value in cube.items():
        print('Z =', key)
        for row in value:
            print(row)
    print()

def adjacent_helper(vel, index):
    max_dim = (row_len, col_len, offset)

    for i in range(0, len(vel)):
        index[i] += vel[i]

        min_dim = 0
        if i == 2:
            min_dim = -offset + 1

        if index[i] < min_dim or index[i] >= max_dim[i]:
            return 0

    if cube[index[2]][index[0]][index[1]] == '#':
        return 1

    return 0

def adjacent_count(fi, fj, fk):
    adjacent = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not (i == 0 and j == 0 and k == 0):
                    adjacent += adjacent_helper((i, j, k), [fi, fj, fk])

    return adjacent

while offset < 7:
    cube[+offset] = [['.' for i in range(0, col_len)] for j in range(0, row_len)]
    cube[-offset] = [['.' for i in range(0, col_len)] for j in range(0, row_len)]
    toggle_positions = {key: [] for key in range(-offset, offset + 1)}

    for k in range(-offset, offset + 1):
        for i in range(0, row_len):
            for j in range(0, col_len):
                adjacent = adjacent_count(i, j, k)

                if cube[k][i][j] == '#':
                    if adjacent not in [2, 3]:
                        toggle_positions[k].append( (i, j) )
                else:
                    if adjacent == 3:
                        toggle_positions[k].append( (i, j) )

    for key, value in toggle_positions.items():
        for pos in value:
            pos_x, pos_y = pos
            if cube[key][pos_x][pos_y] == '#':
                cube[key][pos_x][pos_y] = '.'
            else:
                cube[key][pos_x][pos_y] = '#'

    offset += 1

active_count = 0
for key, value in cube.items():
    for row in value:
        for item in row:
            if item == '#':
                active_count += 1

print(active_count)

