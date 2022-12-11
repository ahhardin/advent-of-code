import requests
import re

from years.session import SESSION
response = requests.get('https://adventofcode.com/2022/day/10/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split("\n")
test_data_file = open('years/2022/10_test.txt', 'r')
test_data = test_data_file.read().strip().split("\n")

def get_cycles(commands):
    x = [1]
    for c in commands:
        if c == "noop":
            x.append(x[-1])
        else:
            value = int(re.search("(-?\d+)", c).group())
            x.append(x[-1])
            x.append(x[-1] + value)
    return x

test_cycles = get_cycles(test_data)

def get_signal_strength(data):
    cycles = get_cycles(data)
    samples = [20, 60, 100, 140, 180, 220]
    return sum([cycles[s-1]*s for s in samples])

assert(get_signal_strength(test_data) == 13140)
print(f"part 1: {get_signal_strength(data)}")

def draw(data):
    for idx, sprite_position in enumerate(get_cycles(data)):
        if idx and not idx % 40:
            print("")
        if idx % 40 in [sprite_position + 1, sprite_position, sprite_position - 1]:
            print('#', end="")
        else:
            print(" ", end="")

print("part 2:")
draw(data)