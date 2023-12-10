import numpy as np

with open("test.txt", 'r') as file:
    data = (line.strip("\n").split(" ") for line in file)
    sequences = [[int(num) for num in line] for line in data]

def generate_diffs(sequence: list[int]) -> list[list[int]]:
    differences = [next_line:=np.array(sequence)]
    while next_line.sum() != 0:
        next_line = np.diff(next_line)
        differences.append(next_line)
    
    return differences

"""
new_lines = [generate_diffs(sequence) for sequence in sequences]
cum = [np.cumsum([diff[-1] for diff in sequence]) for sequence in new_lines]
result = sum([element[-1] for element in cum])
"""
result = sum(
    np.cumsum([diff[-1] for diff in sequence])[-1] 
    for sequence in [generate_diffs(sequence) for sequence in sequences]
)

print(result)