with open("input.txt") as f:
    rows = [line.rstrip() for line in f]

pos_horizontal = 0
pos_vertical = 0
count_trees = 0

while pos_vertical < len(rows):
    # print(f'H: {pos_horizontal} V: {pos_vertical}')
    # print(rows[pos_vertical][pos_horizontal])
    if rows[pos_vertical][pos_horizontal] == '#':
        count_trees += 1

    pos_horizontal += 3

    if pos_horizontal > len(rows[pos_vertical])-1:
        pos_horizontal = pos_horizontal - len(rows[pos_vertical])

    pos_vertical += 1

print(f'Encountered { count_trees } trees')