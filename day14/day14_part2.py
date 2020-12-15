from itertools import product
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
        mem = int(mem[4:-1])
        value = int(value)

        floats = []

        # do all masking operations (read from right, hence index = 35 - index)
        for bit_index, val in [(35-i, l) for i, l in enumerate(mask)]:
            if val == '1':
                mem = mem | (1 << bit_index)
            if val == 'X':
                floats.append(bit_index)
        print(floats)
        
        # produce all combinations of floating bits
        for t in product([0, 1], repeat=len(floats)):
            new_mem = mem
            for i, bit in enumerate(t):
                if bit:
                    new_mem = new_mem | (bit << floats[i])
                else:
                    new_mem = new_mem & ~(1 << floats[i])
            mem_space[new_mem] = value
print(sum(mem_space.values()))
