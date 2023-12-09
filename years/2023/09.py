## day 9
from years.process import get_response, parse_response_to_array

raw_test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

raw_data = get_response(day=9)

def process_data(data):
    return [[int(i) for i in line.split()] for line in data.strip().split("\n")]

def get_diff(line):
    diff_array = []
    for i in range(len(line)-1):
        diff_array.append(line[i+1]-line[i])
    return diff_array

def apply_diff(line, diff):
    return line + [line[-1]+diff]

test_data = process_data(raw_test_data)
data = process_data(raw_data)

def get_history(line):
    diffs = get_diff(line)
    history = [line, diffs]
    while sum(diffs) != 0:
        diffs = get_diff(diffs)
        history.append(diffs)
    return history

def process_history(history):
    nxt = history[-1][-1]
    for h in reversed(history):
        new_line = apply_diff(h, nxt)
        nxt = new_line[-1]
    return new_line[-1]
    
def part_1(data):
    return sum([process_history(get_history(line)) for line in data])
    
assert part_1(test_data) == 114
part_1 = part_1(data)
print(f"Part 1: {part_1}")

def apply_diff_pt2(line, diff):
     return [line[0]-diff] + line
    
def process_history_pt2(history):
    nxt = history[-1][0]
    for h in reversed(history):
        new_line = apply_diff_pt2(h, nxt)
        nxt = new_line[0]
    return new_line[0]

def part_2(data):
    return sum([process_history_pt2(get_history(line)) for line in data])

assert part_2(test_data) == 2
part_2 = part_2(data)
print(f"Part 2: {part_2}")
    