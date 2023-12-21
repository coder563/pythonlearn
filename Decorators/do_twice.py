def do_twice(func):

    def repeater(*args,**kwargs):
         func(*args,**kwargs)
         func(*args,**kwargs)


    return repeater