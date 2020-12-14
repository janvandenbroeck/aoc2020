with open('input.txt') as f:
    adts = sorted([int(l) for l in f.readlines()])
adts.append(adts[-1]+3)
deltas = [adt - adts[i-1] for i, adt in enumerate(adts) if i != 0]
deltas.insert(0, adts[0])

print( sum([1 for d in deltas if d == 1]) * sum([1 for d in deltas if d == 3]))
