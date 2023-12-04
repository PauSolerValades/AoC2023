with open('input.txt', 'r') as file:
    matrix = []
    for line in file:
        non_group = line.find(":") +2 #we take into account the first space
        line = [element.split(" ") for element in line[non_group:].strip("\n").split("|")]
        line = [[value for value in card if value != ''] for card in line]
        matrix.append(line)

count = [len(set(numbers).intersection(set(winning))) for numbers, winning in matrix]
result = sum([2**(matches-1) for matches in count if matches != 0])
print(result)    