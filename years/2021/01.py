import requests

from years.session import SESSION

response = requests.get('https://adventofcode.com/2021/day/1/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n')

# part 1
num_increasing = 0
for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):
        num_increasing += 1
print(f'part 1: {num_increasing}')

# part 2
num_increasing = 0
groups = [int(data[i]) + int(data[i+1]) + int(data[i+2]) for i in range(0, len(data)-2)]
for i in range(1, len(groups)):
    if groups[i] > groups[i-1]:
        num_increasing += 1
print(f'part 2: {num_increasing}')