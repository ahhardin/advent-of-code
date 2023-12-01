# day 1
import regex as re
import requests
from years.session import SESSION

test_data_1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

test_data_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

response = requests.get('https://adventofcode.com/2023/day/1/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n')
# part 1
def get_calibration_sum(data):
    calibration_sum = 0
    for item in data:
        numbers = re.findall("[0-9]", item)
        calibration_sum += int(numbers[0] + numbers[-1])
    return calibration_sum

assert get_calibration_sum(test_data_1)==142
part_1 = get_calibration_sum(data)

# part 2
number_lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
def get_digit(number):
    return number_lookup[number] if number in number_lookup else number 

def get_calibration_sum_2(data):
    calibration_sum = 0
    for item in data:
        numbers = re.findall("([1-9]|one|two|three|four|five|six|seven|eight|nine)", item, overlapped=True)
        calibration_sum += int(get_digit(numbers[0]) + get_digit(numbers[-1]))
    return calibration_sum
assert get_calibration_sum_2(test_data_2)==281
part_2 = get_calibration_sum_2(data)

print("Part 1: ", part_1)
print("Part 2: ", part_2)