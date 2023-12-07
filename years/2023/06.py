# day 6
import math
from years.process import get_response

raw_data = get_response(day=6)

raw_test_data ="""
Time:      7  15   30
Distance:  9  40  200
"""

def split_input(raw_data):
    categories = [d.split() for d in raw_data.strip().split('\n')]
    return [(int(t),int(d)) for t, d in zip(*categories) if t.isnumeric()]

def solve_quadratic(a, b, c):
    start = -b
    radical = (b**2 - 4*a*c)
    denominator = 2*a
    return[(start - (radical)**(1/2))/denominator, (start + (radical)**(1/2))/denominator]
        
def calculate_exclusive_diff(lower, upper):
    lower = math.ceil(lower)
    upper = upper - 1 if upper.is_integer() else math.ceil(upper)
    return upper - lower

def calculate_win_product(data):
    ## dist = t*th - th^2 or th^2 - t*th + d = 0
    ## figure out all ths for which d > dist given
    win_product = 1
    for (t,d) in split_input(data):
        roots = solve_quadratic(1, -t, d)
        num_wins = calculate_exclusive_diff(*roots)
        win_product = win_product * (num_wins)
    return win_product
    
assert calculate_win_product(raw_test_data) == 288
part_1 = calculate_win_product(raw_data)
print("Part 1: ", part_1) # 3317888

def split_input_part_2(data):
    categories = [d.split() for d in data.strip().split('\n')]
    t = ""
    d = ""
    for c in categories:
        for num in c[1:]:
            if c[0] == "Time:":
                t += num
            else:
                d += num
    return int(t), int(d)

def part_2(data):
    (t,d) = split_input_part_2(data)
    roots = solve_quadratic(1, -t, d)
    num_wins = calculate_exclusive_diff(*roots)
    return num_wins

assert part_2(raw_test_data) == 71503
part_2 = part_2(raw_data) # 24655068

print("Part 2: ", part_2)