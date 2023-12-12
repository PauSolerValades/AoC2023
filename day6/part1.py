from math import prod

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    info = [line.split(":")[1].strip(" \n").split(" ") for line in lines]

info = [[int(element) for element in row if element != ""] for row in info]
info = zip(info[0], info[1])

possible_options = []
for time, distance in info:
    meters = ((i)*(time-i) for i in range(1,time))
    satisfies = (1 for meters in meters if meters > distance)
    possible_options.append(sum(satisfies))

result = prod(possible_options)
print(result)