import requests
from time import perf_counter
from contextlib import contextmanager

from years.session import SESSION

def get_response(*, day, year):
    response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={'Cookie': SESSION})
    return response.content.decode("utf-8")

def parse_response_to_array(content):
    return content.strip().split('\n')


@contextmanager
def timer():
    t1 = t2 = perf_counter() 
    yield lambda: t2 - t1
    t2 = perf_counter()