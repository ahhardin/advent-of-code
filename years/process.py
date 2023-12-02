import requests

from years.session import SESSION

def get_response(*, day):
    response = requests.get(f'https://adventofcode.com/2023/day/{day}/input', headers={'Cookie': SESSION})
    return response.content.decode("utf-8")

def parse_response_to_array(content):
    return content.strip().split('\n')