from collections import defaultdict
with open('input.txt') as f:
    rules, yt, nt = f.read().split('\n\n')

# Define the Rulebook
rulebook = dict()
for rule in rules.split('\n'):
    field, value = rule.split(': ')
    rulebook[field] = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in value.split(' or ')]

# Find Valid Tickets
valid_tickets = []
for nearby_t in nt.split('\n'):
    if nearby_t == 'nearby tickets:': continue
    valid = True
    for v in nearby_t.split(','):
        if not any([r_min <= int(v) <= r_max for r in rulebook.values() for r_min, r_max in r]):
            valid = False
            break
    if valid:
        valid_tickets.append([int(v) for v in nearby_t.split(',')])    

#prepare Your Ticket
for l in yt.split('\n'):
    if l == 'your ticket:': continue
    your_ticket = [int(val) for val in l.split(',')]

# Get all the valid fields per position
mapping_options = defaultdict(list)
for i in range(len(your_ticket)):
    fields_valid_t = [valid_ticket[i] for valid_ticket in valid_tickets]
    for field, rules in rulebook.items():
        if all([any([r_min <= v <= r_max for r_min, r_max in rules]) for v in fields_valid_t]):
            mapping_options[i].append(field)

# Iterate over rules to find where only 1 options is valid, fixate it, and remove it
mapping = dict()
while not all([len(v) == 0 for v in mapping_options.values()]):
    for k, v in mapping_options.items():
        if len(v) == 1:
            field = v[0]
            mapping[field] = k
            break

    for v in mapping_options.values():
        if field in v: 
            v.remove(field)

res = 1
for field, pos in mapping.items():
    if field.startswith('departure'):
        res *= your_ticket[pos]

print(res)