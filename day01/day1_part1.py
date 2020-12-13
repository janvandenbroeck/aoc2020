with open("input.txt") as f:
    inputnrs = [int(line) for line in f.readlines() if len(line) >1]

for i, nr in enumerate(inputnrs):
    for j, nr_next in enumerate(inputnrs, start=i):
        if nr + nr_next == 2020:
            print(f'{nr} {nr_next}: {nr * nr_next}')
            