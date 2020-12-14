max_id = 0
with open("input.txt") as f:
    for line in f:
        row_binary = [ True if letter == 'B' else False for letter in line.rstrip()[:7]]
        rownr = sum([b*c for b, c in zip(row_binary, [64, 32, 16, 8, 4, 2, 1])])
        seat_binary = [ True if letter == 'R' else False for letter in line.rstrip()[7:]]
        seatnr = sum([b*c for b, c in zip(seat_binary, [4, 2, 1])])
        max_id = max(max_id, rownr*8 + seatnr)
print(max_id)