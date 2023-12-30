from typing import List
def capital_indexes(input:str)->List:
    characters = input.split()
    capital_list = list()
    for character in characters:
        position = 0
        if character.isUpper():
            capital_list.append(position)
        position+=1


    return capital_list








