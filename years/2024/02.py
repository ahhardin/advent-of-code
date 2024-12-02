# day 2
from years.process import get_response

response = get_response(day=2, year=2024)

test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
test_lines = [[int(num) for num in nums.split(" ")] for nums in test_input.strip().split("\n")]
real_lines = [[int(num) for num in nums.split(" ")] for nums in response.strip().split("\n")]

def is_increasing_safely(line):
    return all(a<b and b-a<=3 for a,b in zip(line, line[1:]))

def is_decreasing_safely(line):
    return all(b<a and a-b<=3 for a,b in zip(line, line[1:]))
    
            
def part_1(lines):
    safe_lines = 0
    for line in lines:
        if is_increasing_safely(line) or is_decreasing_safely(line):
            safe_lines += 1
    return safe_lines
        
assert part_1(test_lines) == 2

print(f"Part 1 = {part_1(real_lines)}")

# part 2
def is_increasing_with_dampner(line, dampened=False):
    for idx, (a,b) in enumerate(zip(line, line[1:])):
        if a<b and b-a<=3:
            continue
        elif not dampened:
            new_line_b = line.copy()
            new_line_a = line.copy()
            new_line_b.pop(idx+1)
            new_line_a.pop(idx)
            pop_b = is_increasing_with_dampner(new_line_b, True)
            pop_a = is_increasing_with_dampner(new_line_a, True)
            return pop_b or pop_a
        else:
            return False
    return True

def is_decreasing_with_dampner(line, dampened=False):
    for idx, (a,b) in enumerate(zip(line, line[1:])):
        if a>b and a-b<=3:
            continue
        elif not dampened:
            new_line_b = line.copy()
            new_line_a = line.copy()
            new_line_b.pop(idx+1)
            new_line_a.pop(idx)
            pop_b = is_decreasing_with_dampner(new_line_b, True)
            pop_a = is_decreasing_with_dampner(new_line_a, True)
            return pop_b or pop_a
        else:
            return False
    return True
        
def part_2(lines):
    safe_lines = 0
    for line in lines:
        if is_increasing_with_dampner(line) or is_decreasing_with_dampner(line):
            safe_lines += 1
    return safe_lines

assert part_2(test_lines) == 4
print(f"Part 2 = {part_2(real_lines)}")