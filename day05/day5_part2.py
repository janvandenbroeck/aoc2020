foundseats = set()
with open("input.txt") as f:
    for line in f:
        row_b = [ True if l == 'B' else False for l in line.rstrip()[:7]]
        row = sum([b*c for b, c in zip(row_b, [64, 32, 16, 8, 4, 2, 1])])
        seat_b = [ True if l == 'R' else False for l in line.rstrip()[7:]]
        seat = sum([b*c for b, c in zip(seat_b, [4, 2, 1])])
        foundseats.add(row*8 + seat)
for sid in ((row*8 + seat) for seat in range(8) for row in range(128)):
    if sid not in foundseats and sid+1 in foundseats and sid-1 in foundseats:
        print(sid)