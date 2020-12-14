with open('input.txt') as f:
    instr = [(l.split()[0], int(l.split()[1])) for l in f.readlines() if len(l) > 1]
    changes = [ln for ln, inst in enumerate(instr) if inst[0] in ('jmp', 'nop')]

for change in changes:
    print(f'CHANGE {change}')
    is_loop = True
    seen = set()
    i = 0
    acc = 0
    while True:
        thisin, mod = instr[i]
        print(f'  PRE {i} {acc} {thisin} {mod}')

        if i in seen:
            break # It's an infinite loop
        seen.add(i)
        if i == change:
            if thisin == 'jmp':
                thisin = 'nop'
            elif thisin == 'nop':
                thisin = 'jmp'
                
        if thisin == 'jmp':
            i += mod - 1 # we add to i anyway later
        if thisin == 'acc':
            acc += mod

        i += 1
        print(f'  POST next {i} {acc}  (we did {thisin} {mod})')

        if len(instr) == i:
            is_loop = False # reached the end
            break

    if not is_loop:
        print(acc)
        break