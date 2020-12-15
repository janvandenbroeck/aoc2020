from math import gcd, lcm

with open('input.txt') as f:
    _ = f.readline()
    busses = [int(line) if line != 'x' else 1 for line in f.readline().split(',')]
    offsets = [i for i in range(len(busses))]

    n_busses = [bus for bus in busses if bus != 1]
    n_offsets = [offset * -1 for i, offset in enumerate(offsets) if busses[i] != 1]


def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase

def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

current_period = n_busses[0]
first_alignment = 0

print(n_busses)
print(n_offsets)

for i in range(1, len(n_busses)):
    # Where the arrows first align, where B starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        current_period, -first_alignment % current_period, n_busses[i], -n_offsets[i] % n_busses[i]
        )
    first_alignment = -phase % period
    current_period = lcm(n_busses[i], current_period) 
    print(f'{i} {n_busses[i]} {first_alignment} {current_period}')

print(first_alignment)