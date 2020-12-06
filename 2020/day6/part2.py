import sys

input_lines = sys.stdin.read()

declarations = [declaration.replace(' ', '') for declaration in input_lines.replace('\r', '').split('\n\n')]

final_answer = 0
for declaration in declarations:
    groups = declaration.split('\n')
    freq = {chr(x): 0 for x in range(97, 97 + 26)}

    for group in groups:
        for answer in group:
            freq[answer] += 1

    answers = [key for key, value in freq.items() if value == len(groups)]

    final_answer += len(answers)

print(final_answer)
