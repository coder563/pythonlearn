

print(f'=====Running module1  __name__= {__name__}======= ')
 

def pprint(header, d):
    
    print('\n\n')
    print(f'--------{header}---------\n\n')
    for key,value in d.items(): 
        print(f'key = {key}, value = {value}')
    print('\n\n-------------------------\n\n')


#pprint("global",globals())