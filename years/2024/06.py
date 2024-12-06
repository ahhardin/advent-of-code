# day 6
from years.process import catchtime, get_response

test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

response = get_response(day=6, year=2024)

orientation_map = {
    "^": (0,-1),
    "v": (0,1),
    "<": (-1,0),
    ">": (1,0)
}

def get_matrix_origin_and_orientation(data):
    lines = data.strip().split("\n")
    matrix = set()
    origin = None
    orientation = None
    for j, line in enumerate(lines):
        items = list(line)
        for i, item in enumerate(items):
            if item != ".":
                if item in orientation_map.keys():
                    origin = (i,j)
                    orientation = (orientation_map[item])
                else:
                    matrix.add((i,j))
    return matrix, origin, orientation, (i,j)

def rotate(orientation):
    rotator = [(0,1),(-1,0)]
    return (
        orientation[0]*rotator[0][0] + orientation[1]*rotator[1][0],
        orientation[0]*rotator[0][1] + orientation[1]*rotator[1][1]
    )

def step(coordinate, orientation, matrix):
    new_coordinate = (coordinate[0] + orientation[0], coordinate[1] + orientation[1])
    if new_coordinate in matrix:
        orientation = rotate(orientation)
        return step(coordinate, orientation, matrix)
    return new_coordinate, orientation

def get_path(matrix, origin, orientation, bounds):
    coordinate = origin
    path = set()
    while coordinate[0] >= 0 and coordinate[0] <= bounds[0] and coordinate[1] >= 0 and coordinate[1] <= bounds[1]:
        path.add(coordinate)
        coordinate, orientation = step(coordinate, orientation, matrix)
    return path

def part_1(data):
    matrix, origin, orientation, bounds = get_matrix_origin_and_orientation(data)
    path = get_path(matrix, origin, orientation, bounds)
    return len(path)
    
    
assert part_1(test_input) == 41
print (f"Part 1 = {part_1(response)}")

# part 2
def part_2(data):
    matrix, origin, orig_orientation, bounds = get_matrix_origin_and_orientation(data)
    path = get_path(matrix, origin, orig_orientation, bounds)
    path.remove(origin)
    num_obstacles = 0
    for coord in path:
        new_matrix = matrix.copy()
        coordinate = origin
        orientation = orig_orientation
        new_path = set()
        new_matrix.add(coord)
        while coordinate[0] >= 0 and coordinate[0] <= bounds[0] and coordinate[1] >= 0 and coordinate[1] <= bounds[1]:
            new_path.add((coordinate, orientation))
            coordinate, orientation = step(coordinate, orientation, new_matrix)
            if (coordinate, orientation) in new_path:
                num_obstacles += 1
                break
    return num_obstacles
        
assert part_2(test_input) == 6
print (f"Part 2 = {part_2(response)}")