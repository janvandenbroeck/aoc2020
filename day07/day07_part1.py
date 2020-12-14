with open('input.txt') as f:
    rules = dict([(line.split(' bags contain ')[0], line.split(' bags contain ')[1]) for line in f.read().split('\n') if len(line) > 1])
    inner_bags = set(['shiny gold'])
    while True:
        prev_len = len(inner_bags)
        for c, contents in rules.items():
            if any([bag for bag in inner_bags if bag in contents]):
                inner_bags.add(c)
        if(len(inner_bags) == prev_len):
            break
print(len(inner_bags)-1)