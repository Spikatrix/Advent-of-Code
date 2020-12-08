import sys

input_lines = [line.strip() for line in sys.stdin]
run_count = {key: 1 for key in range(0, len(input_lines))}

acc = 0
ip = 0
while run_count[ip] == 1:
    exec_line = input_lines[ip]
    inst, num = exec_line.split(' ')
    num = int(num)

    run_count[ip] += 1
    if inst == 'nop':
        ip += 1
    elif inst == 'acc':
        acc += num
        ip += 1
    elif inst == 'jmp':
        ip += num

print(acc)
