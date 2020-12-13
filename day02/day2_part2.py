myinput = []
with open("input.txt") as f:
    for line in f:
        parts = line.rstrip().split(':')        
        config = parts[0].split()
        myinput.append({
            'c_min': int(config[0].split("-")[0].strip()),
            'c_max': int(config[0].split("-")[1].strip()),
            'letter': config[1].strip(),
            'pw': parts[1].strip()
        })
cnt = 0
for w in myinput:
    if (w['pw'][w['c_min']-1] == w['letter']) != (w['pw'][w['c_max']-1] == w['letter']):
        cnt += 1

print(f'Number of valid passwords: {cnt}')