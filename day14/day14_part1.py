with open('input.txt') as f:
    ops_raw = [op.rstrip().lstrip('mask = ') for op in f.read().split('\nmask = ')]
    ops_list = dict([(op.split('\n')[0], op.split('\n')[1:]) for op in ops_raw])
print(ops_list)

mem_space = dict()

for mask, ops in ops_list.items():
    print(mask)    
    print(ops)

    for op in ops:
        mem, value = op.split(' = ')
        mem = mem[4:-1]
        value = int(value)
        # do all masking operations (read from right, hence index = 35 - index)
        for bit_index, val in [(35-i, l) for i, l in enumerate(mask) if l != 'X']:
            if val == '1':
                value = value | (1 << bit_index)
            if val == '0':
                value = value & ~(1 << bit_index)
        mem_space[mem] = value
        print(f'  {mem} {value}')
print(sum(mem_space.values()))
