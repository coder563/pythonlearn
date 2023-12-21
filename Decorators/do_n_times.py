def do_n_times(_func=None,*,times:int=2):
    
    def will_repeat(_func):
      
        def funcgreet(wishes:str):
            for _ in range(0,times):
        
                _func(wishes)

        return funcgreet
    
    if _func == None:
        # will be called when decorator has parameters
        return will_repeat

    else:
        #will be called when decorator has no parameters
        return will_repeat(_func)




