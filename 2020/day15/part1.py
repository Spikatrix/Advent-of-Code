import sys

starting_numbers = [int(number) for number in sys.stdin.readline().split(',')]
history = { key: { 'count': 0, 'last': 0, 'laster': 0 } for key in starting_numbers }

turn = 1
prev = -1
turn_limit = 2020 + 1

for num in starting_numbers:
    prev = num
    history[num]['count'] += 1
    history[num]['laster'], history[num]['last'] = history[num]['last'], turn
    turn += 1

while turn != turn_limit:
    if history[prev]['laster'] == 0:
       prev = 0
    else:
       prev = history[prev]['last'] - history[prev]['laster']

    if prev not in history.keys():
        history[prev] = { 'count': 0, 'last': 0, 'laster': 0 }

    history[prev]['count'] += 1
    history[prev]['laster'], history[prev]['last'] = history[prev]['last'], turn

    turn += 1

print(prev)
