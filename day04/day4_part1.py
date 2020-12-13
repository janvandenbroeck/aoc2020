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
count = 1
for passport in rows:
    if (len(passport) == 8) or (len(passport) == 7 and 'cid' not in passport):
        count += 1
print(count)