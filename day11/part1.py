def are_equal(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("ni comprovo")
        return False
    
    return all((l1 == l2 for l1, l2 in zip(matrix1, matrix2)))

def find_empty_lines(matrix):
    return [index for index, line in enumerate(matrix, start=1) if sum((1 for element in line if element == '.')) == len(line)]

def add_lines(matrix, lines):
    offset = 0
    for line in lines:
        matrix.insert(line+offset, ''.join(('.' for _ in range(len(matrix[0])))))
        offset += 1
    return matrix

with open('input.txt', 'r') as file:
    matrix = [line.strip("\n") for line in file]

for index, line in enumerate(matrix, start=1):
    print(f"{index}:\t {line}")

new_horizontal = find_empty_lines(matrix)
rMatrix = [''.join([matrix[j][i] for j in range(len(matrix))]) for i in range(len(matrix[0]))]
new_vertical = find_empty_lines(rMatrix)

print(new_horizontal, new_vertical)
rMatrix = add_lines(rMatrix, new_vertical)
matrix = add_lines(
    [''.join([rMatrix[j][i] for j in range(len(rMatrix))]) for i in range(len(rMatrix[0]))],
    new_horizontal
)

"""
with open('.txt', 'r') as file:
    test_data = [line.strip("\n") for line in file]
   
for index, line in enumerate(matrix, start =1):
    print(f"{index}:\t {line}")

for index, line in enumerate(test_data, start=1):
    print(f"{index}:\t {line}")

print(are_equal(matrix, test_data))
"""
asteriscs = {}
number = 1
for i, line in enumerate(matrix, start=1):
    for j, element in enumerate(line, start=1):
        if element == '#':
            asteriscs[number] = (i,j)
            number += 1

print(asteriscs)

from itertools import combinations
distances_to_all = [
    abs(a[1] - b[1]) + abs(a[0] - b[0]) for a, b in combinations(asteriscs.values(), 2)
]

result = sum(distances_to_all)
print(result)