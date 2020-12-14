with open('input.txt') as f:
    rules = dict([(line.split(' bags contain ')[0], line.split(' bags contain ')[1]) for line in f.read().split('\n') if len(line) > 1])
    rules = dict([(c, dict([(b.lstrip(' 0123456789').split(' bag')[0], b.lstrip()[:b.lstrip().find(' ')]) for b in r.rstrip('.').split(',')])) for c, r in rules.items()])
    count = 0
    i = 0
    current_level = {'shiny gold': 1}
    while True:
        print(f'iteration {i}: {count}')
        current_count = count
        new_level = dict()
        for bag, amount in current_level.items():
            for new_bag, new_amount in rules[bag].items():
                print(f'{bag} {amount} -- {new_bag} : {new_amount}')
                if new_bag != 'no other':
                    if new_bag in new_level:
                        new_level[new_bag] += amount*int(new_amount)
                    else:
                        new_level[new_bag] = amount*int(new_amount)
            count += amount
        print(new_level)
        current_level = new_level
        if len(new_level) == 0:
            break
        i += 1
print(count-1) #exclude original shiny gold bag 