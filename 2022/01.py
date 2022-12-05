import requests
from advent_of_code.session import SESSION

# part 1
response = requests.get('https://adventofcode.com/2022/day/1/input', headers={'Cookie': SESSION})
split_data = response.content.decode('utf-8').strip().split('\n\n')
data = [d.split('\n') for d in split_data]
calorie_sum = [sum(map(int, cals)) for cals in data]
calorie_sum.sort(reverse=True)
top_calories = calorie_sum[0]
print(top_calories)
# part 2
top_three = sum(calorie_sum[:3])
print(top_three)