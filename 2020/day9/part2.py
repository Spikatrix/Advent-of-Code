import sys

input_numbers = [int(line.strip()) for line in sys.stdin]

preamble_len = 25
index = preamble_len
answer = 0

while index < len(input_numbers) and answer == 0:
    check_list = input_numbers[index - preamble_len: index]
    check_num = input_numbers[index]

    found = False
    for a in check_list:
        b = check_num - a
        if a != b and b in check_list:
            found = True
            break

    if not found:
        answer = check_num

    index += 1

final_answer = 0
for (index, a) in enumerate(input_numbers):
    s = a
    answer_list = [a]
    for b in input_numbers[index + 1:]:
        s += b
        answer_list.append(b)
        if s > answer:
            break
        elif s == answer:
            final_answer = min(answer_list) + max(answer_list)

    if final_answer != 0:
        break

print(final_answer)

