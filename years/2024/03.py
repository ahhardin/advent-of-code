# day 3
import regex as re
from years.process import get_response

response = get_response(day=3, year=2024)

test_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

pattern_1 = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

def part_1(input_string):
    matches = re.findall(pattern_1, input_string)
    return sum([int(a)* int(b) for a,b in matches])

assert part_1(test_input) == 161

print(f"Part 1 = {part_1(response)}")

test_input_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

pattern_2 = r"(do\(\)|don\'t\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\))"

def part_2(input_string):
    matches = re.findall(pattern_2, input_string)
    total = 0
    do = True
    for match in matches:
        if match[0] == "do()":
            do = True
        elif match[0] == "don't()":
            do = False
        elif do:
            total += int(match[1]) * int(match[2]) 
    return total
        
        
assert part_2(test_input_2) == 48

print(f"Part 2 = {part_2(response)}")