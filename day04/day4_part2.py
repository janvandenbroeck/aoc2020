rows = []
with open("input.txt") as f:
    passport = {}
    for line in f:
        splits = line.rstrip().split(" ")
        if len(splits) == 1 and splits[0] == '':
            rows.append(passport)
            passport = {}
        else:
            for code in splits:
                kv = code.split(":")
                passport[kv[0]] = kv[1]
count = 0
for passport in rows:
    if not ((len(passport) == 8) or (len(passport) == 7 and 'cid' not in passport)):
        continue
    if not (len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002):
        continue
    if not (len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020):
        continue
    if not (len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030):
        continue
    if not ((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in') and 59 <= int(passport['hgt'][:-2]) <= 76):
        continue
    if not (len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and passport['hcl'][1:].isalnum()):
        continue
    if not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        continue
    if not (len(passport['pid']) == 9 and passport['pid'].isdecimal()):
        continue
    count += 1
print(count)