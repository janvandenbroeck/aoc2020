from collections import defaultdict
with open('input.txt') as f:
    nrs = [int(n) for n in f.readline().split(',') ]

#nrs = [14,3,1,0,9,5]

lastused = defaultdict(list)

for i, nr in enumerate(nrs):
    lastused[nr].append(i+1)

spoken = nrs[-1]

for turn in range(i+2, 2021):
    #print(lastused)
    if len(lastused[spoken]) == 1:
        spoken = 0
    else:
        spoken = lastused[spoken][-1] - lastused[spoken][-2]
    #print(spoken)
    lastused[spoken].append(turn)

print(spoken)