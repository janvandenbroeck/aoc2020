with open('input.txt') as f:
    groups = f.read().split('\n\n')
    groups = [x.rstrip().split('\n') for x in groups]
    cnt = 0
    for g in groups:
        cnt += len([x for x in 'abcdefghijklmnopqrstuvwxyz' if all([x in d for d in g])])
print(cnt)