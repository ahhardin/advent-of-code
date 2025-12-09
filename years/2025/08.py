from years.process import *
from collections import defaultdict
import math
test_input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
real_input = get_response(day=8, year=2025)

def process_input_into_coords(data_input):
    return([tuple(int(d) for d in data.split(",")) for data in data_input.strip().split("\n")])
  
def get_distance_map(coordinates):
    distance_map = defaultdict(frozenset)
    for x1,y1,z1 in coordinates:
        for x2,y2,z2 in coordinates:
            if (x1,y1,z1) == (x2,y2,z2) or distance_map[frozenset([(x1,y1,z1), (x2,y2,z2)])]:
                continue
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            distance_map[frozenset([(x1,y1,z1), (x2,y2,z2)])] = dist
    return sorted([(v,k) for k,v in distance_map.items()], key=lambda x: x[0])
        

def get_sorted_nodes(nearest_node_lookup):
    return sorted([(v,k) for k,v in nearest_node_lookup.items()], key=lambda x: x[0])


def merge_circuits(circuits):
    merged_circuits = set()
    for circuit in circuits:
        merged_circuits.update(circuit)
    return merged_circuits

def part_1(input_data, num_connections):
    coords = process_input_into_coords(input_data)
    sorted_nodes = get_distance_map(coords)
    circuits = []
    for _, (node_1, node_2) in sorted_nodes[:num_connections]:
        in_circuits = []
        for circuit in circuits:
            if node_1 in circuit or node_2 in circuit:
                circuit.add(node_1)
                circuit.add(node_2)
                in_circuits.append(circuit)
        if not in_circuits:
            circuits.append(set([node_1, node_2]))
        for circuit in in_circuits:
            circuits.remove(circuit)
        circuits.append(merge_circuits(in_circuits))
    sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    top_3 = sorted_circuits[:3]
    return math.prod(len(circuit) for circuit in top_3)

assert part_1(test_input, 10) == 40
print(f"Part 1: {part_1(real_input, 1000)}")

def part_2(input_data):
    coords = process_input_into_coords(input_data)
    sorted_nodes = get_distance_map(coords)
    circuits = [set((coord,)) for coord in coords]
    for _, (node_1, node_2) in sorted_nodes:
        in_circuits = []
        for circuit in circuits:
            if node_1 in circuit or node_2 in circuit:
                circuit.add(node_1)
                circuit.add(node_2)
                in_circuits.append(circuit)
        if not in_circuits:
            circuits.append(set([node_1, node_2]))
        for circuit in in_circuits:
            circuits.remove(circuit)
        circuits.append(merge_circuits(in_circuits))
        if len(circuits) == 1:
            return (node_1[0] * node_2[0])

assert part_2(test_input) == 25272
print(f"Part 2: {part_2(real_input)}")
      