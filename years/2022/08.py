import requests
import math

from years.session import SESSION
response = requests.get('https://adventofcode.com/2022/day/8/input', headers={'Cookie': SESSION})
data = [[int(item) for item in line] for line in response.content.decode('utf-8').strip().split('\n')]

test_data = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

test_data = [[int(item) for item in line] for line in test_data]

# part 1
def get_visible(plot):
    # outside trees
    visible_trees = len(plot) * 2 + len(plot[0]) * 2 - 4
    # inside trees
    max_i = len(plot)-1
    max_j = len(plot[0])-1
    for i in range(1, max_i):
        for j in range(1, max_j):
            tree_height = plot[i][j]
            if tree_height > max(plot[i][:j]):
                visible_trees += 1
            elif tree_height > max(plot[i][j+1:]):
                visible_trees +=1
            elif tree_height > max([plot[k][j] for k in range(0, i)]):
                visible_trees +=1  
            elif tree_height > max([plot[k][j] for k in range(i+1, max_i+1)]):
                visible_trees +=1
    return visible_trees

assert(get_visible(test_data) == 21)
print(f"part 1: {get_visible(data)}")

# part 2
def get_scenic(plot):
    step_map = {
        'left': -1,
        'right': 1,
        'up': 1,
        'down': -1
    }
    most_scenic = 0
    i_max = len(plot)
    j_max = len(plot[0])
    for i in range(0, len(plot[0])):
        for j in range(0, len(plot)):
            num_visible = {s: 0 for s in step_map.keys()}
            tree_height = int(plot[i][j])
            steps = ['left', 'right', 'up', 'down']
            for s in steps:
                i_step = 0 if s in ['up', 'down'] else step_map[s]
                j_step = 0 if s in ['left', 'right'] else step_map[s]
                delta_i = i + i_step
                delta_j = j + j_step
                while delta_i in range(0, i_max) and delta_j in range(0, j_max):
                    num_visible[s] += 1
                    if plot[delta_i][delta_j] >= tree_height:
                        break
                    delta_i += i_step
                    delta_j += j_step
            most_scenic = max(most_scenic, math.prod(num_visible.values()))
    return most_scenic
    
assert(get_scenic(test_data) == 8)
print(f"part 2: {get_scenic(data)}")