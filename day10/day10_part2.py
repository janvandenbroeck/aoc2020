from collections import defaultdict

with open('input.txt') as f:
    adts = sorted([int(l) for l in f.readlines()])
    adts = [0] + adts + [adts[-1]+3]

ways = defaultdict(lambda:0)
ways[0] = 1

for adt in adts:
    if adt == 0: continue
    ways[adt] = ways[adt-1] + ways[adt-2] + ways[adt-3]

print(ways[adts[-1]])
