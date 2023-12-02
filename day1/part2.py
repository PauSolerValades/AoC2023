# ownerproof-3492965-1701471333-518cddb452b2
import re

numeric_equivalence = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def treat_number(string):
    """
    The main objective of this funcion is to separate the connected words, like
    twone into two and one and remember the index
    """
    result = []
    #we iterate for each number avaliable
    for number in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
        #we copy the string to modify it
        cp_string = string[::]
        offset = 0
        while len(cp_string) >= len(number):
            index = cp_string.find(number)
            if index != -1:
                #if the number is found, we trim the original string to find if there is another one.
                result.append((number, offset + index))
                cp_string = cp_string[index+len(number):]
                #the offset is where the original number would be if we hadn't trimmed the string!
                offset += index + len(number)
            else:
                break

    return [numeric_equivalence[elem1] for elem1, _ in sorted(result, key=lambda x: x[1])]
                    

def search_first_last_number(paraula):

    # numbers: non digits caractrers
    # \d: digit caracters
    # +: group the encounters together
    # |: or, matches one or the other.
    # '\d|\D+' digit caracters one by one or non digits all together.
    numbers = re.findall(r'\d|\D+', paraula)


    result = [item for element in numbers for item in (treat_number(element) if not element.isnumeric() else [element])]

    return int(result[0] + result[-1])     


# read the input file
with open('input.txt', 'r') as file:
    suma = sum([search_first_last_number(linia) for linia in file])

print(suma)

"""
llista = [
    "twotwotwotwotwothreetwothree",
    "oneightwone",
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"]

suma = sum([search_first_last_number(linia) for linia in llista])

print(suma)
"""