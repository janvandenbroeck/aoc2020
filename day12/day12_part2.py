with open('input.txt') as f:
    directions = [(line[0], int(line[1:])) for line in f.readlines() if len(line)  > 1]

pos_ship = [0, 0] # X and Y
pos_wpt = [10, 1]

for move, amount in directions:
    print(f'at {pos_ship} asked to {move} {amount}')
    if move == 'N':
        pos_wpt[1] += amount
    if move == 'S':
        pos_wpt[1] -= amount
    if move == 'E':
        pos_wpt[0] += amount
    if move == 'W':
        pos_wpt[0] -= amount

    if move == 'L':
        for i in range(amount // 90):
            pos_wpt = [pos_wpt[1] * -1, pos_wpt[0]]
    if move == 'R':
        for i in range(amount // 90):
            pos_wpt = [pos_wpt[1], pos_wpt[0] * -1]
    if move == 'F':
        pos_ship[0] += pos_wpt[0] * amount
        pos_ship[1] += pos_wpt[1] * amount

    print(f'  now at {pos_ship}, wpt {pos_wpt}')

print(abs(pos_ship[0]) + abs(pos_ship[1]))