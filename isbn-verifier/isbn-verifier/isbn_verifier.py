import functools as ft
import re
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="ISBN_verifier.log",
                    filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S'
                    )



def is_valid(isbn:str)->bool:
    formatted_isbn = format_validator(isbn)
    if formatted_isbn:
        return value_check(formatted_isbn)
    else:   
        logging.info('The string format was invalid') 
        return False

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
    position  = list(range(10,0,-1))
    isbn_parsed = list(isbn)

    if isbn[-1] == 'X':isbn_parsed[-1]='10'

    prod = list(map(lambda l1, l2:l1*int(l2),position,isbn_parsed))
    val = ft.reduce(lambda a, b:a+b,prod) % 11
    if val == 0:return True
    else: return False

if __name__ == '__main__':
    logging.debug('Inside Main')
    logging.debug(f'checking for {is_valid('3-59A-21507-X')=}')