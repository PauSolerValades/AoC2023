from multiprocessing import Pool

import numpy as np

type_dict = {}
with open('input.txt', 'r') as file:
    lines = file.readlines()
    first_line = lines[0]
    objectives = first_line[first_line.find(":")+2:].strip("\n").split(" ")

    i=2
    while i <= len(lines)-1:
        if lines[i] == "\n":
            continue

        if not lines[i].isdigit():
            actual_type = lines[i].strip("\n").split(" ")[0]
            type_dict[actual_type] = []

            i+=1
            while lines[i] != "\n":
                type_dict[actual_type] += [[int(item) for item in lines[i].strip("\n").split(" ")]]
                i+=1
        i+=1

def map_vis(x, conditions):
    for c in conditions:
        #c[1], c[0], c[2] = image, domain, amount
        #print(f"Entry domain: {x}. Lower domain: {domain}. Upper domain: {domain + amount}")
        if x >= c[1] and x < c[1] + c[2]:
            return (c[0]-c[1]) + x
    return x

def worker(args):
    seeds, values = args
    return [map_vis(seed, values) for seed in seeds]

llavors_nombres = zip(
    [int(objectives[i]) for i in range(0, len(objectives), 2)],
    [int(objectives[i]) for i in range(1, len(objectives), 2)]
)

all_seeds = [seed for inici, nombre in llavors_nombres for seed in range(inici, inici + nombre)]

# Number of processes to create
num_processes = 10  # or however many your machine can handle

# Create a process pool
with Pool(num_processes) as pool:
    for index, values in enumerate(type_dict.values()):
        print(f"Processing {index} values")
        # Divide work among processes
        chunksize = len(all_seeds) // num_processes
        args = [(all_seeds[i:i + chunksize], values) for i in range(0, len(all_seeds), chunksize)]
        # Collect results
        all_seeds = [seed for sublist in pool.map(worker, args) for seed in sublist]

print(min(all_seeds))
