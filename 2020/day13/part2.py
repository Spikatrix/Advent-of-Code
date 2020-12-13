import sys

bus_times = [int(x) if x != 'x' else 0 for x in sys.stdin.readline().split(',')]
time_table = bus_times.copy()
max_index = bus_times.index(max(bus_times))
magic_number = 100000000000000 // bus_times[max_index]
bus_times = [(x * magic_number) + 1 if x != 0 else 0 for x in bus_times]

def get_closer():
    for (index, time) in enumerate(bus_times):
        if index != max_index and bus_times[index] != 0:
            # Something's definitely wrong in here
            bus_times[index] += (((bus_times[max_index] - bus_times[index]) // time_table[index]) * time_table[index])

loop = True
while loop:
    loop = False
    for (index, time) in enumerate(bus_times):
        if 0 < time <= 100000000000000:
            loop = True
        bus_times[index] += time_table[index]

# All timings are above 100000000000000 now

loop = True
while loop:
    loop = False
    # I can do this, but need time to plan everything properly
    index, count, last_val = 0, 0, 0
    print(bus_times)
    get_closer()

    print(bus_times)

print(time_table)

