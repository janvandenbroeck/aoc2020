import copy
with open('input.txt') as f:
    sm = [[char for char in line.rstrip('\n')] for line in f.readlines()]

while True:
    nm =  copy.deepcopy(sm)
    for y, line in enumerate(sm):
        for x, char in enumerate(line):
            if char == '.':
                continue

            vis_occ = 0

            # look left
            for chk in reversed(range(0, x)):
                if sm[y][chk] == 'L':
                    break
                if sm[y][chk] == '#':
                    vis_occ += 1
                    break

            # look right
            for chk in range(min(x+1, len(line)), len(line)):
                if sm[y][chk] == 'L':
                    break
                if sm[y][chk] == '#':
                    vis_occ += 1
                    break
            
            # look up
            for chk in reversed(range(0, y)):
                if sm[chk][x] == 'L':
                    break
                if sm[chk][x] == '#':
                    vis_occ += 1
                    break

            # look down
            for chk in range(min(y+1, len(sm)), len(sm)):
                if sm[chk][x] == 'L':
                    break
                if sm[chk][x] == '#':
                    vis_occ += 1
                    break
            
            # diagonal up left
            ul_y, ul_x = (y - 1, x - 1)
            while ul_y >= 0 and ul_x >= 0:
                if sm[ul_y][ul_x] == 'L':
                    break
                if sm[ul_y][ul_x] == '#':
                    vis_occ += 1
                    break
                ul_x -= 1
                ul_y -= 1

            # diagonal up right
            ul_y, ul_x = (y - 1, x + 1)
            while ul_y >= 0 and ul_x < len(line):
                if sm[ul_y][ul_x] == 'L':
                    break
                if sm[ul_y][ul_x] == '#':
                    vis_occ += 1
                    break
                ul_x += 1
                ul_y -= 1

            # diagonal down left
            ul_y, ul_x = (y + 1, x - 1)
            while ul_y < len(sm) and ul_x >= 0:
                if sm[ul_y][ul_x] == 'L':
                    break
                if sm[ul_y][ul_x] == '#':
                    vis_occ += 1
                    break
                ul_x -= 1
                ul_y += 1

            # diagonal down right
            ul_y, ul_x = (y + 1, x + 1)
            while ul_y < len(sm) and ul_x < len(line):
                if sm[ul_y][ul_x] == 'L':
                    break
                if sm[ul_y][ul_x] == '#':
                    vis_occ += 1
                    break
                ul_x += 1
                ul_y += 1

            if char == 'L':
                if vis_occ == 0:
                    nm[y][x] = '#'
            if char == '#':
                if vis_occ >= 5:
                    nm[y][x] = 'L'

    if all([sm[y][x] == nm[y][x] for y in range(len(sm)) for x in range(len(sm[y])) ]):
        break

    sm = nm

print(sum([char == '#' for line in sm for char in line]))