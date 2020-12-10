import sys

input_jolts = [int(line) for line in sys.stdin]

max_jolt_adapter = max(input_jolts) + 3
jolt_diffs = {key: 0 for key in range(1, 4)}

curr_jolt = 0
input_jolts.sort()
for jolt in input_jolts:
    jolt_diffs[jolt - curr_jolt] += 1
    curr_jolt = jolt

jolt_diffs[3] += 1

print(jolt_diffs[1] * jolt_diffs[3])
