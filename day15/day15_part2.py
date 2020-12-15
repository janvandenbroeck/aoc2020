with open('input.txt') as f:
    nrs = [int(n) for n in f.readline().split(',') ]

lastused = dict([(nr, i + 1) for i, nr in enumerate(nrs)])

spoken_this_round = nrs[-1]
spoken = 0 # only of no doubles in input
turn = len(nrs)

while turn < 30000000:
    turn += 1

    # Spoken is spoken this turn, Prepare for next turn
    spoken_now = spoken
    
    if spoken in lastused:
        # In the next turn, we'll speak the diff between this turn (it's always this turn minus some earlier one)
        spoken = turn - lastused[spoken]
    else:
        # First time, speak 0 next time
        spoken = 0
    # also, the spoken value was last seen this turn
    lastused[spoken_now] = turn
    
print(spoken_now)