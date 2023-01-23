import requests
import re

from collections import defaultdict
from datetime import datetime

from years.session import SESSION

test_input = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3"

pattern = "[a-zA-Z\s]+x=(-?\d+), y=(-?\d+):[a-zA-Z\s]+x=(-?\d+), y=(-?\d+)"
decode = lambda x: [((int(r[0]), int(r[1])), (int(r[2]), int(r[3]))) for text in x.split('\n') for r in re.findall(pattern, text)]
test_data = decode(test_input)

response = requests.get('https://adventofcode.com/2022/day/15/input', headers={'Cookie': SESSION})
real_input = response.content.decode('utf-8').strip()
real_data = decode(real_input)


dist = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1])

overlap = lambda a, b: max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1) 

def collapse_intervals(intervals):
    # sort intervals by start
    intervals.sort(key=lambda x: x[0])
    new_intervals = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= new_intervals[-1][1] + 1:
            new_intervals[-1][1] = max([interval[1], new_intervals[-1][1]])
        else:
            new_intervals.append(interval)
    return new_intervals  

def get_intervals(sensor, beacon, intervals, min_pos, max_pos, limit_x):
    distance = dist(sensor, beacon)
    for idx, j in enumerate(range(sensor[1] - distance, sensor[1] + distance)):
        if min_pos <= j <= max_pos:
            delta = idx if idx <= distance else (distance * 2) - idx
            start = sensor[0] - delta
            end = sensor[0] + delta
            if limit_x:
                if overlap((start, end), (min_pos, max_pos)):
                    start = start if start > min_pos else min_pos
                    end = end if end < max_pos else max_pos
                    intervals[j].append([start, end])
            else:
                intervals[j].append([start, end])
            intervals[j] = collapse_intervals(intervals[j])
    return intervals  

def get_all_intervals(data, min_pos, max_pos, limit_x=False):
    intervals = defaultdict(list)
    for d in data:
        intervals.update(get_intervals(d[0], d[1], intervals, min_pos, max_pos, limit_x))
    return intervals

def part_1(data, y_level):
    intervals = get_all_intervals(data, y_level, y_level)[y_level]
    return sum([i[1] - i[0] for i in intervals])

def part_2(data, min_pos, max_pos):
    intervals = get_all_intervals(data, min_pos, max_pos, True)
    for k,v in intervals.items():
        # between intervals
        if len(v) > 1:
            coord = (v[1][0] - 1, k)
            break
        # start of interval
        if v[0][0] > min_pos:
            coord = (v[0][0], k)
            break
        # end of interval
        if v[0][1] < max_pos:
            coord = (v[0][1], k)
    return coord[0] * 4000000 + coord[1]

print("--- Part 1 ---")
assert(part_1(test_data, 10) == 26)
start1 = datetime.now()
print(f"part 1: {part_1(real_data, 2000000)}")
end1 = datetime.now()
print(f"part 1 took {end1-start1}\n")

print("--- Part 2 ---")
assert(part_2(test_data, 0, 20) == 56000011)
start2 = datetime.now()
print(f"part 2: {part_2(real_data, 0, 4000000)}")
end2 = datetime.now()
print(f"part 2 took {end2-start2}\n")


# For fun / debugging - plot of test data 

def plot_empty_slots(grid, sensor, beacon):
    grid[sensor] = " S "
    grid[beacon] = " B "
    distance = dist(sensor, beacon)
    for x in range(sensor[0] - distance, sensor[0] + distance + 1):
        for y in range(sensor[1] - distance, sensor[1] + distance + 1):
            if grid[(x,y)] not in [" S ", " B "]:
                if dist(sensor, (x,y)) <= distance:
                    grid[(x,y)] = " # "
    return grid

def build_grid(data):
    grid = defaultdict(str)
    for line in data:
        grid.update(plot_empty_slots(grid, line[0], line[1]))
    return grid

def plot_grid(grid):
    x_list = [c[0] for c in grid.keys()]
    y_list = [c[1] for c in grid.keys()]
    min_x = min(x_list)
    max_x = max(x_list)
    min_y = min(y_list)
    max_y = max(y_list)
    for i in range(min_x - 1, max_x + 1):
        print(f"{i} " if i < 0 or i > 9 else f" {i} ", end="\n" if i >= max_x else "")
    for j in range(min_y, max_y + 1):
        for i in range(min_x - 1, max_x + 1):
            if i == min_x - 1:
                print(j if j<-9 else f"{j} " if j < 0 or j > 9 else f" {j} ", end="")
            else:
                print(grid[i,j] or " . ", end="\n" if i >= max_x else "")

print("--- For fun ---")
plot_grid(build_grid(test_data))