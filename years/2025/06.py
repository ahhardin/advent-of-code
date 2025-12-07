from years.process import *
import re

test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

real_input = get_response(day=6, year=2025)

pattern = r"\d+|\+|\*"

def process_input_into_lines(input_data):
    lines = []
    data_array = [d.strip() for d in input_data.strip().split("\n")]
    for idx, string in enumerate(data_array):
        matches = re.findall(pattern, string)
        lines.append(matches)
    return list(map(list, zip(*lines)))

def calculate_lines(lines):
    total = 0
    for line in lines:
        operator = line[-1]
        line_result = eval(operator.join(line[0:-1]))
        total += line_result
    return total

def part_1(input_data):
    lines = process_input_into_lines(input_data)
    return calculate_lines(lines)

assert part_1(test_input) == 4277556
print(f"Part 1: {part_1(real_input)}")

## part 2 ## 

def process_input_into_data(input_data):
    return [d for d in input_data.split("\n") if d]

def process_data_part_2(input_data):
    input_data_adjusted = [data + " " for data in input_data]
    zipped_string = zip(*input_data_adjusted)
    num_rows = len(input_data)
    all_nums = []
    num_array = []
    operator = None
    for item in zipped_string:
        if item == tuple(" " for i in range(0,num_rows)):
            num_array.append(operator)
            all_nums.append(num_array)
            num_array = []
            continue
        if item[-1] in ["*", "+"]:
            operator = item[-1]
        item = item[0:-1]
        num="".join(item).strip()
        num_array.append(num)
    return all_nums

def part_2(input_data):
    data = process_input_into_data(input_data)
    num_arrays = process_data_part_2(data)
    return calculate_lines(num_arrays)

assert part_2(test_input) == 3263827
print(f"Part 2: {part_2(real_input)}")