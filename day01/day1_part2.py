with open("input.txt") as f:
    inputnrs = [int(line) for line in f.readlines() if len(line) >1]

for i, nr in enumerate(inputnrs):
    for j, nr_next in enumerate(inputnrs, start=i):
        for k, nr_next2 in enumerate(inputnrs, start=j):
            if nr + nr_next + nr_next2 == 2020:
                print(f'{nr} {nr_next} {nr_next2}: {nr * nr_next * nr_next2}')