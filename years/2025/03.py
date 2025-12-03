from years.process import *

real_data_raw = (get_response(day=3, year=2025))
test_data_raw = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

def process_data(raw_data):
    return parse_response_to_array(raw_data.strip())

test_data = process_data(test_data_raw)
real_data = process_data(real_data_raw)
  
# part 1

def find_max_index(line):
    max_num = max(line[:-1])
    idx = line.index(max_num)
    return max_num, idx

def find_next_max(line, start_index):
    max_num = max(line[start_index+1:])
    idx = line.index(max_num)
    return max_num, idx

def get_max_joltage(line):
    max_num, idx = find_max_index(line)
    second_num, idx_2 = find_next_max(line, idx)
    return int(max_num + second_num)

def part_1(data):
    total_joltage = 0
    for line in data:
        total_joltage += get_max_joltage(line)
    return total_joltage

assert part_1(test_data) == 357
print(f"Part 1: {part_1(real_data)}")

# part 2

def find_max_for_line(line, num_digits):
    limit = num_digits - 1
    limited_line = line[:-limit] if limit else line
    max_num = max(limited_line)
    idx = line.index(max_num)
    return max_num, idx

def get_max_joltage_part_2(line, num_digits):
    max_joltage = ""
    for i in range(num_digits, 0, -1):
        max_num, idx = find_max_for_line(line, i)
        line = line[idx+1:]
        max_joltage += max_num
    return max_joltage
        
def get_total_max_joltage(data, num_digits):
    total_joltage = 0
    for line in data:
        total_joltage += int(get_max_joltage_part_2(line, num_digits))
    return total_joltage
    
    
# this should also work for part 1 - test that
assert get_total_max_joltage(test_data, 2) == part_1(test_data)
assert get_total_max_joltage(real_data, 2) == part_1(real_data)

# and on the test output for this part
assert get_total_max_joltage(test_data, 12) == 3121910778619
print(f"Part 2: {get_total_max_joltage(real_data, 12)}")