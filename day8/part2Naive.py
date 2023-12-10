from itertools import cycle

with open('test3.txt', 'r') as file:
    rl_sequence = file.readline().strip().strip("\n")
    file.readline() #skip empty line

    data = {key.strip(): tuple(value.strip().strip('()').split(', ')) 
        for line in file 
        for key, value in [line.strip().split(' = ')]}

# we convert left and right into zeros and ones to enter the list faster
binaryRL = rl_sequence.translate(str.maketrans("LR", "01"))
binaryRL_iter = cycle(binaryRL)

actual_points = [points for points in data.keys() if points.endswith('A')]
iterations = 0

condition = (not point.endswith('Z') for point in actual_points)

while any(condition):

    direction = int(next(binaryRL_iter))
    point_condition = [
        (data[point][direction], not data[point][direction].endswith('Z')) 
        for point in actual_points
    ]
    actual_points, condition = zip(*point_condition)
    actual_points = list(actual_points)

    iterations += 1

print(iterations)