# day 7
import itertools
from years.process import get_response

test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
response = get_response(day=7, year=2024)

def build_data_dict(data):
    lines = data.strip().split("\n")    
    return {int(line.split(": ")[0]): [int(num) for num in line.split(": ")[1].split(" ")] for line in lines}

operators_1 = [lambda a,b: a+b, lambda a,b: a*b]

def check_permutation(items, op_perm, result):
    value = items[0]
    for pair in zip(items[1:], op_perm):
        value = pair[1](value, pair[0])
    return value == result
        
def solve(data, operators):
    data_dict = build_data_dict(data)
    total = 0
    for value, items in data_dict.items():
        op_permutations = itertools.product(*[operators for _ in range(0, len(items)-1)])
        for op_perm in op_permutations:
            if check_permutation(items, op_perm, value):
                total += value
                break
    return total

assert solve(test_input, operators_1) == 3749
print (f"Part 1 = {solve(response, operators_1)}")

# part 2
operators_2 = [lambda a,b: a+b, lambda a,b: a*b, lambda a,b: int(str(a)+str(b))]
assert solve(test_input, operators_2) == 11387
print (f"Part 2 = {solve(response, operators_2)}")

