# day 3
import requests
import string
from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/3/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n')

# part 1
letters = string.ascii_lowercase+string.ascii_uppercase
weights = {letters[i]: i+1 for i in range(len(letters))}
total = 0
for d in data:
    d1 = d[:len(d)//2]
    d2 = d[len(d)//2:]
    for l in d1:
        if l in d2:
            total += weights[l]
            break
print(total)

# part 2
total_2 = 0
throuples = [data[i:i+3] for i in range(0, len(data), 3)]
for t in throuples:
    for l in t[0]:
        if l in t[1]:
            if l in t[2]:
                total_2 += weights[l]
                break
print(total_2)