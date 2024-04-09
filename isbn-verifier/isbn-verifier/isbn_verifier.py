import functools as ft
import re


def is_valid(isbn:str)->bool:
    ''' check if a string is a valid ISBN number

    isbn = 3-598-21508-8
    '''

    valid_isbn = format_validator(isbn)
    if valid_isbn:
        print(f'valid ISBN = {valid_isbn=}')
        return value_check(valid_isbn)
    else: return False
        
    
    

def format_validator(isbn:str)->bool:

    
    pattern_string = r"[0-9-]+X{0,1}\Z"

    pattern = re.compile(pattern_string)

    if pattern.fullmatch(isbn) == None:
        return False
    else:
        isbn = isbn.replace('-','')
        
        if len(isbn) != 10 :
            return False
        else:
            return isbn    

def value_check(isbn:str)->bool:
    #TODO:'Check value'

    position  = list(range(1,11))

    if isbn[-1] == 'X':
        isbn_parsed = list(isbn[:-1])
        isbn_parsed.append('10')
        print(f'list with x = {isbn_parsed=}')
    else:
        isbn_parsed = list(isbn)
    

    isbn_parsed = list(map(int,isbn_parsed))
    
   

    prod = list(map(lambda l1, l2:l1*l2,position,isbn_parsed))
    summation = ft.reduce(lambda a, b:a+b,prod) 
    val = summation % 11

    print(f'{isbn_parsed}, {prod=}, {summation=}, {val=}')
    
    if val == 0:return True
    else: return False
   




if __name__ == '__main__':
    print('inside main')
    print(is_valid('3-598-21507-X'))













