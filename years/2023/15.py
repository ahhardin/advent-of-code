# day 15
from collections import defaultdict, OrderedDict

from years.process import get_response

test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
raw_data = get_response(day=15)

test_data = test_input.split(",")
data = raw_data.strip().split(",")

def apply_hash(code):
    result = 0
    for char in code:
        result = (result + ord(char)) * 17 % 256
    return result

def part_1(data):
    return sum([apply_hash(code) for code in data])

assert part_1(test_data) == 1320
part_1(data)

print(f"Part 1: {part_1(data)}")

def get_code(line):
    if "=" in line:
        return line.split("=")
    else:
        return line.split("-")

def build_boxes(data):
    boxes = defaultdict(OrderedDict)
    for item in data:
        code, focal_length = get_code(item)
        box_num = apply_hash(code)
        if focal_length:
            boxes[box_num][code] = int(focal_length)
        elif code in boxes[box_num]:
            del boxes[box_num][code]
            if not boxes[box_num]:
                del boxes[box_num]
    return boxes

def get_focus_power(boxes):
    focus_power = 0
    for box, contents in boxes.items():
        for idx, focal_length in enumerate(contents.values()):
            focus_power += (box + 1) * (idx + 1) * focal_length
    return focus_power


def part_2(data):
    return get_focus_power(build_boxes(data))

assert part_2(test_data) == 145
part_2(data)

print(f"Part 2: {part_2(data)}")