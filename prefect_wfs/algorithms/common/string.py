from typing import List

def replace(input: List[str], old_value: str, new_value: str) -> List[str]:
    return [x.replace(old_value, new_value) for x in input]

def split(input: List[str]) -> List[str]:
    intermediate = []
    for element in input:
        n = 3
        intermediate.append([element[i:i+n] for i in range(0, len(element), n) ])
    return [item for sublist in intermediate for item in sublist]

def concat(input: List[str]) -> List[str]:
    # initialize N 
    N = 3
    temp = '{}' * N 
    return [temp.format(*ele) for ele in zip(*[iter(input)] * N)]