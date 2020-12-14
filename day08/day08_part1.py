with open('input.txt') as f:
    instr = [(l.split()[0], int(l.split()[1])) for l in f.readlines() if len(l) > 1]
seen = set()
i = 0
acc = 0
while True:
    thisin, mod = instr[i]
    print(f'{i} {acc} {thisin} {mod}')
    if i in seen:
        break
    if thisin == 'jmp':
        i += mod - 1 # we add to i anyway 
    if thisin == 'acc':
        acc += mod
    seen.add(i)
    i += 1
print(acc)