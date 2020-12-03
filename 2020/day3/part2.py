import sys
input_lines = [line.strip() for line in sys.stdin]

slope_check = [
                [1, 1],
                [3, 1],
                [5, 1],
                [7, 1],
                [1, 2],
              ]

final_answer = 1
for slope in slope_check:
    x_step, y_step = slope
    count = 0
    x = 0

    for line_index in range(0, len(input_lines), y_step):
        line = input_lines[line_index]

        if line[x] == '#':
            count += 1

        x = (x + x_step) % len(line)

    final_answer *= count

print(final_answer)
