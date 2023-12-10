type_dict = {}
with open('input.txt', 'r') as file:
    lines = file.readlines()
    first_line = lines[0]
    objectives = first_line[first_line.find(":")+2:].strip("\n").split(" ")
    print(objectives)

    i=2
    while i <= len(lines)-1:
        if lines[i] == "\n":
            continue

        if not lines[i].isdigit():
            actual_type = lines[i].strip("\n").split(" ")[0]
            type_dict[actual_type] = []

            i+=1
            while lines[i] != "\n":
                type_dict[actual_type] += [lines[i].strip("\n").split(" ")]
                i+=1
        i+=1

def map_vis(x, conditions):
    for c in conditions:
        domain, image, amount = int(c[1]), int(c[0]), int(c[2])
        #print(f"Entry domain: {x}. Lower domain: {domain}. Upper domain: {domain + amount}")
        if x >= domain and x < domain + amount:
            #print(f"domain in: {(image-domain) + x}")
            return (image-domain) + x
        else:
            #print(f"Seed out: {x}")
            pass
        
    return x

minim = []
for seed in objectives:
    for type_seed in type_dict.keys():
        seed = map_vis(int(seed), type_dict[type_seed])
        print(f"Seed {seed}: Pos {type_seed}: {seed}")

    minim.append(seed)

print(min(minim))

    
    


