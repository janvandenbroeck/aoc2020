with open("input.txt") as f:
    rows = [line.rstrip() for line in f]

total = 1
for d_hor, d_ver in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    pos_horizontal = 0
    pos_vertical = 0
    count_trees = 0
    while pos_vertical < len(rows):
        if rows[pos_vertical][pos_horizontal] == '#':
            count_trees += 1

        pos_horizontal += d_hor

        if pos_horizontal > len(rows[pos_vertical])-1:
            pos_horizontal = pos_horizontal - len(rows[pos_vertical])

        pos_vertical += d_ver
    total *= count_trees

print(f'{total}')

'''
Alternative:

counter = 1
for hor, ver in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    counter *= ''.join([j[i] for i, j in zip([x % 31 for x in range(0, int(round(hor*len(rows)/ver)), hor)], [rows[x] for x in range(0, len(rows), ver)])]).count('#')
'''