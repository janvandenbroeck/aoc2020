count = 0
with open('input.txt') as f:
    yes_q = set()
    for line in f:
        yes_q.update(line.rstrip())
        if len(line.rstrip()) == 0:
            count += len(yes_q)
            yes_q = set()
    count += len(yes_q)
print(count)