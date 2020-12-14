from itertools import combinations
with open('input.txt') as f:
    nrs = [int(l) for l in f.readlines() if len(l) > 1]

preamble = 25
for i in range(preamble, len(nrs)):
    if nrs[i] not in [a+b for a,b in combinations(nrs[i-preamble:i], 2)]:
        print(nrs[i])
        break