import re
from years.process import *


real_data_raw = (get_response(day=2, year=2025))
test_data_raw = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

def process_data(raw_data):
    return [tuple(int(d) for d in data.split("-")) for data in raw_data.split(",")]
  
real_data = process_data(real_data_raw)
test_data = process_data(test_data_raw)

PART_1_PATTERN = r"^(\d+)\1\Z"
PART_2_PATTERN = r"^(\d+)\1+\Z"

def day_2(data, pattern):
    sum_invalid = 0
    for endpoints in data:
        start, finish = endpoints
        for i in range(start, finish+1):
            if match := re.match(pattern, str(i)):
                sum_invalid += int(match[0])
    return sum_invalid

# part 1
assert day_2(test_data, PART_1_PATTERN) == 1227775554
print(f"Part 1: {day_2(real_data, PART_1_PATTERN)}")


# part 2
assert day_2(test_data, PART_2_PATTERN) == 4174379265
print(f"Part 2: {day_2(real_data, PART_2_PATTERN)}")
        
