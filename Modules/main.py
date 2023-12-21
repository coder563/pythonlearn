
import sys



sys.modules['test'] = lambda: "hello world" 

import test

print(sys.modules)

print(type(test) )

def fun1():
    import module1
    module1.pprint("my dict", {"name":"Superman"})
    
    
#fun1()

#module1 = sys.modules['module1']

#module1.pprint("reborn",{"name":"batman"})


