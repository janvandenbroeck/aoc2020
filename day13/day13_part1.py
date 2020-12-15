with open('input.txt') as f:
    timestamp = int(f.readline().rstrip('\n'))
    busses = [int(line) for line in f.readline().split(',') if line != 'x']
remainder = [x - (timestamp % x) for x in busses]
i = remainder.index(min(remainder))
print(busses[i] * remainder[i])