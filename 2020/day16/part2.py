import sys

ticket_ranges, your_ticket, nearby_tickets = sys.stdin.read().replace('\r', '').split('\n\n')
valid = {}
valid_all = set()

for line in ticket_ranges.split('\n'):
    parts = line.split(' ')

    start_index = 0
    while ':' not in parts[start_index]:
        start_index += 1
    start_index += 1

    key = ' '.join(parts[:start_index])
    for index in range(start_index, len(parts), 2):
        low, high = [int(x) for x in parts[index].split('-')]
        if key not in valid.keys():
            valid[key] = []
        valid[key].extend(range(low, high + 1))
        valid_all.update(valid[key])

valid_tickets = {key: {'class': [], 'elems': [], 'checked': False}
                 for key in range(0, len(nearby_tickets.split('\n')[1].split(',')))}

for line in nearby_tickets.split('\n'):
    if line.startswith('nearby'):
        continue

    tickets = line.split(',')
    valid_ticket = True
    for ticket in tickets:
        ticket = int(ticket)
        if ticket not in valid_all:
            valid_ticket = False
            break

    if valid_ticket:
        for (index, ticket) in enumerate(tickets):
            valid_tickets[index]['elems'].append(int(ticket))

for key, value in valid_tickets.items():
    for c, val in valid.items():
        valid_class = True
        for elem in value['elems']:
            if elem not in val:
                valid_class = False
                break
        if valid_class:
            value['class'].append(c)

while True:
    key_search = -1
    for key, value in valid_tickets.items():
        if len(value['class']) == 1 and not value['checked']:
            valid_tickets[key]['checked'] = True
            key_search = key
            break

    if key_search == -1:
        break

    remove_val = valid_tickets[key]['class'][0]
    for key2, value in valid_tickets.items():
        if key2 != key and remove_val in value['class']:
            valid_tickets[key2]['class'].remove(remove_val)

final_order = list(zip([order['class'][0] for order in valid_tickets.values()], 
                       [int(val) for val in your_ticket.split('\n')[1].split(',')]))
answer = 1
for item_name, value in final_order:
    if item_name.startswith('departure'):
        answer *= value

print(answer)
