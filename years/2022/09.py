import requests
import re
import math

from years.session import SESSION
response = requests.get('https://adventofcode.com/2022/day/9/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split("\n")
parsed_data = [re.search("((\w) (\d+))", item) for item in data]

test_data = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]
test_data = [re.search("((\w) (\d+))", item) for item in test_data]

test_data_2 = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20",
]

test_data_2 = [re.search("((\w) (\d+))", item) for item in test_data_2]

def take_step(loc, step):
    return tuple(a + b for a,b in zip(loc, step))

def pull_string(commands):
    step_map = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    tail_locations = set()
    tail_locations.add("0,0")
    current_head = current_tail = (0, 0)
    for c in commands:
        direction = c.group(2)
        move = int(c.group(3))
        for m in range(0, move):
            step = step_map[direction]
            current_head = take_step(current_head, step)
            # if current tail in ok position, continue
            diff = math.sqrt((current_head[0] - current_tail[0])**2 + (current_head[1] - current_tail[1])**2)
            if diff < 2:
                continue
            elif (current_tail[0] == current_head[0]) or (current_tail[1] == current_head[1]):
                current_tail = take_step(current_tail, step)
            else:
                tail_move = []
                dx = current_head[0] - current_tail[0]
                dy = current_head[1] - current_tail[1]
                tail_move.append(1) if dx > 0 else tail_move.append(-1)
                tail_move.append(1) if dy > 0 else tail_move.append(-1)
                current_tail = take_step(current_tail, tail_move)
            tail_locations.add(",".join(map(str, current_tail)))
    return len(tail_locations)
            
assert(pull_string(test_data) == 13)
print(f"part 1: {pull_string(parsed_data)}")

sign = lambda x: -1 if x < 0 else 1           

def pull_string_part_2(commands, rope_length):
    step_map = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    tail_locations = ["0,0"]
    knots = {i: (0,0) for i in range(0, rope_length)}
    for c in commands:
        direction = c.group(2)
        move = int(c.group(3))
        step = step_map[direction]
        for m in range(0, move):
            knots[0] = take_step(knots[0], step)
            for i in range(1, rope_length):
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]
                diff = math.sqrt(dx**2 + dy**2)
                # if current tail in ok position, continue
                if diff > math.sqrt(2):
                    # if current tail is in same x or y dimension, take one step in that direction 
                    if dx == 0:
                        knots[i] = take_step(knots[i], (0, sign(dy)))
                    elif dy == 0:
                        knots[i] = take_step(knots[i], (sign(dx), 0))
                    # otherwise, move diagonally
                    else:
                        knots[i] = take_step(knots[i], (sign(dx), sign(dy)))
            tail_locations.append(",".join(map(str, knots[rope_length-1])))
    return len(set(tail_locations))

assert(pull_string_part_2(test_data, 2) == 13)
assert(pull_string_part_2(parsed_data, 2) == 5619)
assert(pull_string_part_2(test_data, 10) == 1)
assert(pull_string_part_2(test_data_2, 10) == 36)
print(f"part 2: {pull_string_part_2(parsed_data, 10)}")