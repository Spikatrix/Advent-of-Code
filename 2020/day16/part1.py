import sys

ticket_ranges, your_ticket, nearby_tickets = sys.stdin.read().replace('\r', '').split('\n\n')
valid = set()

for line in ticket_ranges.split('\n'):
    parts = line.split(' ')

    start_index = 0
    while ':' not in parts[start_index]:
        start_index += 1

    for index in range(start_index + 1, len(parts), 2):
        low, high = [int(x) for x in parts[index].split('-')]
        valid.update(range(low, high + 1))

scanning_error_rate = 0

for line in nearby_tickets.split('\n'):
    if line.startswith('nearby'):
        continue

    for ticket in line.split(','):
        ticket = int(ticket)
        if ticket not in valid:
            scanning_error_rate += ticket

print(scanning_error_rate)
