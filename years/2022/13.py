import requests
import json
from functools import cmp_to_key
from itertools import zip_longest

from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/13/input', headers={'Cookie': SESSION})
real_input = response.content.decode('utf-8').strip()

test_input = "[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]"

def parse_input(input_data):
    groupings = [d.split('\n') for d in input_data.split('\n\n')]
    return [[json.loads(d) for d in g] for g in groupings]

def compare(left, right):
    type_left = type(left)
    type_right = type(right)
    if type_left == type_right:
        if type_left == int:
            return right - left
        elif type_left == list:
            tuples = zip_longest(left, right)
            for t in tuples:
                if t[0] is None:
                    return 1
                if t[1] is None:
                    return -1
                comparison = compare(t[0], t[1])
                if comparison != 0:
                    return comparison
            return 0
    if type_left == list:
        return compare(left, [right])
    return compare([left], right)
        
            
def get_orderings(data):
    orderings = []
    for g in parse_input(data):
        orderings.append(compare(g[0], g[1]))
    values = [idx + 1 for idx, o in enumerate(orderings) if o >= 0]
    return orderings, sum(values)

assert(get_orderings(test_input)[1] == 13)
print(f"part 1: {get_orderings(real_input)[1]}")

def parse_input_part_2(input_data):
    return [json.loads(d) for d in input_data.replace('\n\n', '\n').split('\n')]

def get_orderings_part_2(data):
    divider_1 = [[2]]
    divider_2 = [[6]]
    parsed_data = parse_input_part_2(data)
    parsed_data.extend([divider_1, divider_2])
    orderings = sorted(parsed_data, key=cmp_to_key(compare), reverse=True)
    return (orderings.index(divider_1) + 1) * (orderings.index(divider_2) + 1)

assert(get_orderings_part_2(test_input) == 140)
print(f"part 2: {get_orderings_part_2(real_input)}")
