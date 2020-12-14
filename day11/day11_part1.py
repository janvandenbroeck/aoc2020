import copy
with open('input.txt') as f:
    sm = [[char for char in line.rstrip('\n')] for line in f.readlines()]

while True:
    nm =  copy.deepcopy(sm)
    for y, line in enumerate(sm):
        for x, char in enumerate(line):
            lim_l = max(0, x-1)
            lim_r = min(x+2, len(line))
            lim_u = max(0,y-1)
            lim_d = min(y+2,len(sm)) 

            surroundings = [letter for v in sm[lim_u:lim_d] for letter in v[lim_l:lim_r]]
            if char == 'L':
                if surroundings.count('#') == 0:
                    nm[y][x] = '#'
            if char == '#':
                if  surroundings.count('#')-1 >= 4:
                    nm[y][x] = 'L'
    
    if all([sm[y][x] == nm[y][x] for y in range(len(sm)) for x in range(len(sm[y])) ]):
        break
    sm = nm

print(sum([char == '#' for line in sm for char in line]))