from years.process import *

real_data = parse_response_to_array(get_response(day=1, year=2025))

test_raw_data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
test_data = parse_response_to_array(test_raw_data)


# part 1
def part_1(data):
    MAX = 100
    num_zeroes = 0
    position = 50
    operators = {
        "L": lambda x,y: x - y,
        "R": lambda x,y: x + y
    }
    for item in data:
        direction = item[0]
        length = int(item[1:])
        raw_new_position = operators[direction](position, length)
        new_position = raw_new_position % MAX
        
        position = new_position
        
        if not position:
            num_zeroes += 1
        
    return num_zeroes
        
        
print(f"Part 1:{part_1(real_data)}")

def part_2(data):
    MAX = 100
    num_zeroes = 0
    position = 50
    operators = {
        "L": lambda x,y: x - y,
        "R": lambda x,y: x + y
    }
    for item in data:
        direction = item[0]
        length = int(item[1:])
        mod_length = length // MAX
        raw_new_position = operators[direction](position, length % MAX)
        new_position = raw_new_position % MAX
        
        num_zeroes += mod_length # number of times we cross zero in full rotations
        
        # if we're already on zero - count it and don't count further rotational zeros (other than mod zeroes)
        if not position:
            num_zeroes += 1
        
        elif raw_new_position > MAX or raw_new_position < 0:
            num_zeroes += 1
        
        position = new_position
    
    if not position:
        num_zeroes += 1
        
    return num_zeroes

print(f"Part 2:{part_2(real_data)}")


