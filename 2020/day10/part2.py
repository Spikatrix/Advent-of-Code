# Doesn't work yet

import sys

input_jolts = [0]
input_jolts.extend([int(line) for line in sys.stdin])
input_jolts.sort()
input_jolts.append(max(input_jolts) + 3)

def jolter(jolt_array, index = 1):
    count = 1
    while index < len(jolt_array) - 1:
        jolt = jolt_array[index]
        diff_prev, diff_next = (jolt - jolt_array[index - 1], jolt_array[index + 1] - jolt)

        if diff_prev + diff_next <= 3:
            count *= (count + 1) * jolter(jolt_array[:index] + jolt_array[index + 1:])
            break
        else:
            index += 1

    return count

print(jolter(input_jolts))

