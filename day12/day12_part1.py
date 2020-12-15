with open('input.txt') as f:
    directions = [(line[0], int(line[1:])) for line in f.readlines() if len(line)  > 1]

pos = [0, 0] # X and Y
hdg = 90

for move, amount in directions:
    print(f'at {pos} {hdg} asked to {move} {amount}')
    if move == 'N':
        pos[1] += amount
    if move == 'S':
        pos[1] -= amount
    if move == 'E':
        pos[0] += amount
    if move == 'W':
        pos[0] -= amount

    if move == 'L':
        hdg = abs((hdg - amount) % 360)
    if move == 'R':
        hdg = abs((hdg + amount) % 360)
    if move == 'F':
        if hdg == 0:
            pos[1] += amount
        elif hdg == 90:
            pos[0] += amount
        elif hdg == 180:
            pos[1] -= amount
        elif hdg == 270:
            pos[0] -= amount
        else:
            raise ValueError
    print(f'  now at {pos} {hdg}')

print(abs(pos[0]) + abs(pos[1]))