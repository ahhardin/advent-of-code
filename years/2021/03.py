# day 3
import re 
import requests 
from collections import defaultdict

from years.session import SESSION

test_data = [ 
    "00100", 
    "11110", 
    "10110", 
    "10111", 
    "10101", 
    "01111", 
    "00111", 
    "11100", 
    "10000", 
    "11001",
     "00010", 
     "01010", 
] 

response = requests.get('https://adventofcode.com/2021/day/3/input', headers={'Cookie': SESSION}) 
data = response.content.decode('utf-8').strip().split('\n')

def part_1(data): 
    size = len(data[0]) 
    gamma = "" 
    epsilon = "" 
    for i in range(0, size): 
        digits_at_idx = [d[i] for d in data] 
        if digits_at_idx.count('1') > len(data) // 2: 
            gamma += '1' 
            epsilon += '0' 
        else: 
            gamma += '0' 
            epsilon += '1' 
    return gamma, epsilon

int(part_1(test_data)[0], 2) * int(part_1(test_data)[1], 2) 
assert(int(part_1(test_data)[0], 2) * int(part_1(test_data)[1], 2) == 198) 
gamma, epsilon = part_1(data) 
print(f"part 1: {int(gamma,2) * int(epsilon,2)}")

def part_2(data, default): 
    result = data.copy() 
    for i in range(0, len(data[0])): 
        if len(result) == 1: 
            break 
        digits_at_idx = [d[i] for d in result] 
        if default == '1':
            reference_bit = default if digits_at_idx.count(default) >= len(result) / 2 else str(int(default) ^ 1) 
        else:
            reference_bit = default if digits_at_idx.count(default) <= len(result) / 2 else str(int(default) ^ 1)
        result = [item for item in result if item[i] == reference_bit] 
    return result[0]

oxygen = part_2(test_data, '1') 
c02 = part_2(test_data, '0') 
assert((int(part_2(test_data,'1'), 2) * int(part_2(test_data, '0'), 2)) == 230)

print(f"part 2: {(int(part_2(data,'1'), 2) * int(part_2(data, '0'), 2))}")