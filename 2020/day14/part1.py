import sys

input_lines = [line.strip() for line in sys.stdin]

memory = {}
mask = 'X' * 36
for line in input_lines:
    if line.startswith('mask = '):
        mask = list(line[:6:-1])
    else:
        mem_addr = int(line[line.index('[') + 1: line.index(']')])
        val = int(line[line.index('=') + 2:])

        binary = bin(val)[:1:-1]
        temp_mask = list(map(lambda x: x if x != 'X' else '0', mask.copy()))

        for (index, num) in enumerate(binary):
            if mask[index] == 'X':
                temp_mask[index] = str(num);

        memory[mem_addr] = int(''.join(temp_mask)[::-1], 2)

print(sum(memory.values()))
