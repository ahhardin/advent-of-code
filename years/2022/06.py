import re
import requests

from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/6/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip()


def find_non_repeating(test_string, num_chars):
    regex = "(?=([a-z])"
    for i in range(1, num_chars):
        regex += "(?!"+"|".join([f"\{j}" for j in range(1, i+1)]) + ")([a-z])"
    regex += ")"
    match = re.search(regex, test_string)
    return match.end(num_chars)
    
test_data_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_data_2 = "nppdvjthqldpwncqszvftbrmjlhg"
test_data_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_data_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

assert(find_non_repeating(test_data_1, 4) == 5)
assert(find_non_repeating(test_data_2, 4) == 6)
assert(find_non_repeating(test_data_3, 4) == 10)
assert(find_non_repeating(test_data_4, 4) == 11)

assert(find_non_repeating(test_data_1, 14) == 23)
assert(find_non_repeating(test_data_2, 14) == 23)
assert(find_non_repeating(test_data_3, 14) == 29)
assert(find_non_repeating(test_data_4, 14) == 26)

# part 1
print(f"part 1: {find_non_repeating(data, 4)}")
# part 2
print(f"part 1: {find_non_repeating(data, 14)}")