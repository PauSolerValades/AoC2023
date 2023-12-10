from math import lcm
from itertools import cycle

with open('input.txt', 'r') as file:
    rl_sequence = file.readline().strip().strip("\n")
    file.readline() #skip empty line

    data = {key.strip(): tuple(value.strip().strip('()').split(', ')) 
        for line in file 
        for key, value in [line.strip().split(' = ')]}

def point_end(point: str, directions: str, data: dict[str, tuple[str, str]]) -> tuple[str, int]:
    directions_iter = cycle(directions)
    iterations = 0

    print(f"Checking point {point}")
    while not point.endswith('Z'):
        point = data[point][int(next(directions_iter))]
        iterations += 1

    return point, iterations

# we convert left and right into zeros and ones to enter the list faster
binaryRL = rl_sequence.translate(str.maketrans("LR", "01"))

starting_points = [points for points in data.keys() if points.endswith('A')]
iterations = {point: point_end(point, binaryRL, data) for point in starting_points}

print(list((i for _, i in iterations.values())))
print(lcm(*(i for _, i in iterations.values())))
