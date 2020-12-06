import sys

input_lines = sys.stdin.read()

declarations = [declaration.replace('\n', ' ').replace(' ', '') for declaration in input_lines.replace('\r', '').split('\n\n')]

final_answer = 0
for declaration in declarations:
    answers = {answer for answer in declaration}
    final_answer += len(answers)

print(final_answer)

