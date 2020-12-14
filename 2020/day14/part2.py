import sys
import itertools

input_lines = [line.strip() for line in sys.stdin]

memory = {}
mask = 'X' * 36
for line in input_lines:
    if line.startswith('mask = '):
        mask = list(line[:6:-1])
    else:
        mem_addr = int(line[line.index('[') + 1: line.index(']')])
        val = int(line[line.index('=') + 2:])

        binary = bin(mem_addr)[:1:-1]
        temp_mask = list(map(lambda x: x if x != 'X' else '0', mask.copy()))

        for (index, num) in enumerate(binary):
            if mask[index] == 'X':
                temp_mask[index] = 'X';
            elif mask[index] == '1':
                temp_mask[index] = '1';
            else:
                temp_mask[index] = str(num)

        temp_str = temp_mask

        len_offset = 0
        for char in temp_str[::-1]:
            if char != '0':
                break
            len_offset += 1

        result = ''.join(temp_mask)[max(len(binary) - 1, 35 - len_offset)::-1]
        perm_count = result.count('X')
        if perm_count == 0:
            memory[int(result, 2)] = val
        else:
            perm_set = set(itertools.combinations_with_replacement('01' * perm_count, perm_count))
            addrs = []
            for perm in perm_set:
                index = 0
                temp_str = ''
                for char in result:
                    if char == 'X':
                        temp_str += perm[index]
                        index += 1
                    else:
                        temp_str += char
                addrs.append(int(temp_str, 2))
            for addr in addrs:
                memory[addr] = val

print(sum(memory.values()))
