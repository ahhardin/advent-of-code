import requests
from collections import defaultdict, deque

from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/12/input', headers={'Cookie': SESSION})
real_data = [list(d) for d in response.content.decode('utf-8').strip().split('\n')]
test_input = "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi"
test_data = [list(d) for d in test_input.split('\n')]


def build_graph(data, start_node_list, end_node_letter):
    graph = defaultdict(list)
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    loc_lookup = {"S": "a", "E": "z"}
    start_nodes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            raw_pos = data[i][j] 
            pos = raw_pos if raw_pos not in loc_lookup else loc_lookup[raw_pos]
            if raw_pos in start_node_list:
                start_nodes.append((i,j))
            elif raw_pos == end_node_letter:
                end_node = (i,j)
            for step in steps:
                dx = step[0]
                dy = step[1]
                valid = 0 <= (i + dx) < len(data) and 0 <= (j + dy) < len(data[0])
                raw_new_loc = data[i + dx][j + dy] if valid else None
                new_loc = raw_new_loc if raw_new_loc not in loc_lookup else loc_lookup[raw_new_loc]
                if new_loc:
                    if ord(new_loc) - ord(pos) <= 1:
                        graph[(i,j)].append((i + dx,j + dy))
    return graph, start_nodes, end_node

def get_shortest_path(graph, start_node, end_node):
    visited = set()
    path_queue = deque([[start_node]])
    while path_queue:
        path = path_queue.popleft()
        node = path[-1]
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                path_queue.append(new_path)
                if neighbor == end_node:
                    return new_path
            visited.add(node)

graph, start_nodes, end_node = build_graph(test_data, ["S"], "E")
path = get_shortest_path(graph, start_nodes[0], end_node)
assert(len(path) - 1 == 31)

graph, start_nodes, end_node = build_graph(real_data, ["S"], "E")
path = get_shortest_path(graph, start_nodes[0], end_node)
print(f"part 1: {len(path) - 1}")

# part 2
def find_shortest_path_part_2(graph, start_nodes, end_node):
    shortest_path = 0
    for n in start_nodes:
        path = get_shortest_path(graph, n, end_node)
        if path:
            if not shortest_path or len(path) - 1 < shortest_path:
                shortest_path = len(path) - 1
    return shortest_path

assert(find_shortest_path_part_2(*build_graph(test_data, ["S", "a"], "E")) == 29)
print(f'part 2: {find_shortest_path_part_2(*build_graph(real_data, ["S", "a"], "E"))}')