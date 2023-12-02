# ownerproof-3492965-1701471333-518cddb452b2

def search_first_last_number(paraula):

    for lletra in paraula:
        if lletra.isnumeric():
            first_number = lletra
            break
    
    for lletra in paraula[::-1]:
        if lletra.isnumeric():
            last_number = lletra
            break
    
    return int(first_number + last_number)

def search_first_last_number_while(paraula):

    start_pointer = 0
    end_pointer =  len(paraula) -1
    first_number = ""
    last_number = ""

    while (not first_number or not last_number):
        
        if paraula[start_pointer].isnumeric():
            first_number = paraula[start_pointer]
        else:
            start_pointer += 1

        if paraula[end_pointer].isnumeric():
            last_number = paraula[end_pointer]
        else:
            end_pointer -= 1

    return int(first_number + last_number)
        


# read the input file
with open('input.txt', 'r') as file:
    suma = sum([search_first_last_number_while(linia) for linia in file])

print(suma)