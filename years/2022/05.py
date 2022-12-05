import re
import requests

from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/5/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n\n')
stack_rows = data[0].split('\n')
moves = data[1]
move_tuples = re.findall('move (\d+) from (\d) to (\d)', moves)
part_1 = {}
part_2 = {}
for idx in range(0, int(stack_rows[-1][-2])):
    i = idx+1+(idx*3)
    stack = [sr[i] for sr in stack_rows[:-1] if sr[i] != ' ']
    stack.reverse()
    part_1[idx+1] = stack.copy()
    part_2[idx+1] = stack.copy()

def move_items(num, start, end):
    for n in range(0, num):
        item = start.pop()
        end.append(item)

for m in move_tuples:
    start = part_1[int(m[1])]
    end = part_1[int(m[2])]
    move_items(int(m[0]), start, end)

print(''.join([s[-1] for s in part_1.values()]))

def move_multi_items(num, start, end):
    items = start[-num:]
    del start[-num:]
    end.extend(items)


for m in move_tuples:
    start = part_2[int(m[1])]
    end = part_2[int(m[2])]
    move_multi_items(int(m[0]), start, end)

print(''.join([s[-1] for s in part_2.values()]))