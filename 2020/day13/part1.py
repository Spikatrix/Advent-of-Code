import sys

start_time = int(sys.stdin.readline())
bus_times = [int(x) for x in filter(lambda x: x != 'x', sys.stdin.readline().split(','))]
bus_board_time = [-1 for i in range(0, len(bus_times))]
time_table = bus_times.copy()

bus_eval_count = 0
while bus_eval_count < len(bus_times):
    for (index, time) in enumerate(time_table):
        if time >= start_time and bus_board_time[index] == -1:
            bus_board_time[index] = time
            bus_eval_count += 1
        time_table[index] += bus_times[index]

min_time, answer = -1, -1
for (index, board_time) in enumerate(bus_board_time):
    board_time -= start_time
    if min_time == -1 or min_time > board_time:
        min_time = board_time
        answer = min_time * bus_times[index]

print(answer)

