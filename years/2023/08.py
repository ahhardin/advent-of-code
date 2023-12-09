# day 8
import math
import re
from years.process import get_response, parse_response_to_array
raw_test_data_1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

raw_test_data_2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

raw_data = get_response(day=8)

PATTERN = "(?P<key>[A-Z]{3})\s*=\s*\((?P<L>[A-Z]{3}),\s*(?P<R>[A-Z]{3})\)"

def build_mapping(data):
    lines = parse_response_to_array(data)
    directions = lines[0]
    nodes = {}
    for line in lines[2:]:
        line_data = re.search(PATTERN, line)
        nodes[line_data.group("key")] = {
            "L": line_data.group("L"),
            "R": line_data.group("R")
        }
    return nodes, directions

def traverse_map(mapping, directions):
    node = "AAA"
    idx = 0
    steps = 0
    while node != "ZZZ":
        try:
            direction = directions[idx]
        except:
            idx = 0
            direction = directions[idx]
        node = mapping[node][direction]
        idx+=1
        steps+=1
    return steps

assert traverse_map(*build_mapping(raw_test_data_1)) == 2
assert traverse_map(*build_mapping(raw_test_data_2)) == 6

part_1 = traverse_map(*build_mapping(raw_data))
print(f"Part 1: {part_1}") # 13771

raw_test_data_3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".replace("1", "Q").replace("2", "M")

def find_starting_nodes(mapping):
    return [key for key in mapping.keys() if key[2] == "A"]

def traverse_map_to_XXZ(start_node, mapping, directions):
    node=start_node
    idx = 0
    steps = 0
    while node[2] != "Z":
        try:
            direction = directions[idx]
        except:
            idx = 0
            direction = directions[idx]
        node = mapping[node][direction]
        idx+=1
        steps+=1
    return steps
    

def get_all_steps(data):
    mapping, directions = build_mapping(data)
    starting_nodes = find_starting_nodes(mapping)
    steps = []
    for node in starting_nodes:
        steps.append(traverse_map_to_XXZ(node, mapping, directions))
    return math.lcm(*steps)

assert get_all_steps(raw_test_data_3) == 6
part_2 = get_all_steps(raw_data)

print(f"Part 2: {part_2}") # 13129439557681