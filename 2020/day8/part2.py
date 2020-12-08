import sys

input_lines = [line.strip() for line in sys.stdin]

def toggleInstruction(inst, num):
    if inst == 'jmp':
        return 'nop'
    else: # nop
        if num == 0:
            return 'nop'
        else:
            return 'jmp'

acc = 0
ip = 0

for index, line in enumerate(input_lines):
    inst, num = line.split(' ')
    if inst == 'acc':
        continue

    acc = 0
    ip = 0
    run_count = {key: 1 for key in range(0, len(input_lines))}

    inst = toggleInstruction(inst, num)
    input_lines[index] = inst + ' ' + num

    while ip < len(run_count) and run_count[ip] == 1:
        exec_line = input_lines[ip]
        inst2, num2 = exec_line.split(' ')
        num2 = int(num2)

        run_count[ip] += 1
        if inst2 == 'nop':
            ip += 1
        elif inst2 == 'acc':
            acc += num2
            ip += 1
        elif inst2 == 'jmp':
            ip += num2

    if ip >= len(run_count):
        break

    input_lines[index] = toggleInstruction(inst, num) + ' ' + num

print(acc)
