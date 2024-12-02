# day 1
import regex as re
import requests
from years.session import SESSION

response = requests.get('https://adventofcode.com/2024/day/1/input', headers={'Cookie': SESSION})

test_data="""
3   4
4   3
2   5
1   3
3   9
3   3
"""
pattern = r"([0-9]+)\s+([0-9]+)"

test_lines = test_data.strip().split("\n")
real_lines = response.content.decode('utf-8').strip().split('\n')

# part 1
def get_lists(lines):
    lhs = []
    rhs = []
    for line in lines:
        match = re.match(pattern,line)
        left = int(match.group(1))
        right = int(match.group(2))
        lhs.append(left)
        rhs.append(right)
    rhs.sort()
    lhs.sort()
    return lhs, rhs

def find_total_diff(lhs, rhs):
    total = 0
    for lh, rh in zip(lhs, rhs):
        total += abs(lh-rh)

    return total

def part_1(lines):
    lhs, rhs = get_lists(lines)
    return find_total_diff(lhs, rhs)

assert part_1(test_lines) == 11
    
print(f"Part 1 = {part_1(real_lines)}")

# part 2
from collections import Counter
def part_2(lines):
    lhs, rhs = get_lists(lines)
    counter = Counter(rhs)
    return sum([counter.get(lh, 0)*lh for lh in lhs])

assert part_2(test_lines) == 31

print(f"Part 2 = {part_2(real_lines)}")