# day 2 
import re
import requests

from years.session import SESSION

response = requests.get('https://adventofcode.com/2021/day/2/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().replace('\n', ' ')

# part 1
commands = re.findall("(\w+) (\d+)", data)
def part_1(commands):
    x_pos = 0
    y_pos = 0
    for c in commands:
        amount = int(c[1])
        if c[0] == 'forward':
            x_pos += amount
        elif c[0] == 'up':
            y_pos -= amount
        elif c[0] == 'down':
            y_pos += amount
    return(x_pos * y_pos)

# part 2
def part_2(commands):
    x_pos_2 = 0
    y_pos_2 = 0
    aim = 0
    for c in commands:
        amount = int(c[1])
        if c[0] == 'forward':
            y_pos_2 += (aim * amount)
            x_pos_2 += amount
        elif c[0] == 'up':
            aim -= amount
        elif c[0] == 'down':
            aim += amount
    return x_pos_2 * y_pos_2

# test
test_commands = [
    ('forward', '5'),
    ('down', '5'),
    ('forward', '8'),
    ('up', '3'),
    ('down', '8'),
    ('forward', '2'),
]

assert(part_1(test_commands) == 150)
assert(part_2(test_commands) == 900)

print(f'part 1: {part_1(commands)}')
print(f'part 2: {part_2(commands)}')