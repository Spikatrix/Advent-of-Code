import sys

nav_inputs = [line.strip() for line in sys.stdin]

move_steps = { 
              'N': (0, 1),
              'E': (1, 0),
              'W': (-1, 0),
              'S': (0, -1),
             }
dirs = 'ESWN'
curr_dir_index = 0
curr_dir = dirs[curr_dir_index]
curr_x, curr_y = 0, 0

for nav_input in nav_inputs:
    cmd, steps = nav_input[0], int(nav_input[1:])
    if cmd == 'F':
        move_x, move_y = move_steps[curr_dir]
        curr_x += move_x * steps
        curr_y += move_y * steps
    elif cmd == 'N':
        curr_y += steps
    elif cmd == 'E':
        curr_x += steps
    elif cmd == 'W':
        curr_x -= steps
    elif cmd == 'S':
        curr_y -= steps
    else:
        if cmd == 'R':
            curr_dir_index = (curr_dir_index + (steps // 90)) % len(dirs)
        else:
            curr_dir_index = (curr_dir_index - (steps // 90)) % len(dirs)
        curr_dir = dirs[curr_dir_index]

print(abs(curr_x) + abs(curr_y))
