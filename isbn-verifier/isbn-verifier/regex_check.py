import re

if __name__ == '__main__':
    print('inside main')
    pattern_string = r"[0-9-]+X{0,1}\Z"
    #$*[X]
    pattern = re.compile(pattern_string)


    result = pattern.fullmatch('890-899348-099')

    print(f'result 1={result}')

    result = pattern.fullmatch('890-899348-99X')
    
    print(f'result 2={result}')

    result = pattern.fullmatch('890-899348-099R')
    
    print(f'result 3={result}')

    result = pattern.fullmatch('890-899348-X99')
    
    print(f'result 4={result}')

    result = pattern.fullmatch('890-899348-9XX')
    
    print(f'result 5={result}')

    result = pattern.fullmatch('3598215088')
    
    print(f'result 6={result}')
    
    result = pattern.fullmatch('3-598-21508-8')
    
    print(f'result 7={result}')

    result = pattern.fullmatch('3-598-21507-A')
    
    print(f'result 8={result}')
    