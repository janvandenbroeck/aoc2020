with open('input.txt') as f:
    rules, yt, nt = f.read().split('\n\n')

rulebook = set()
for rule in rules.split('\n'):
    # print(rule)
    field, value = rule.split(': ')
    ranges = value.split(' or ')
    rulebook.update([(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges])

error_rate = 0

for nearby_t in nt.split('\n'):
    if nearby_t == 'nearby tickets:':
        continue
    for v in nearby_t.split(','):
        print(v)
        valid = False
        for rule_min, rule_max in rulebook:
            if rule_min <= int(v) <= rule_max:
                valid = True
                break
            else:
                continue
        if not valid:
            print(' not valid')
            error_rate += int(v)

print(rulebook)
print(error_rate)