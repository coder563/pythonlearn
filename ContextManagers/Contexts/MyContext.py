class MyContext:
    def __init__(self):
        self.obj = None

    def __enter__(self):
        print("Entered context Manager")
        self.obj = "The Return Object"
        return self.obj

    def __exit__(self,*args, **kwargs):
        print("Exiting Context")
        if  args[0]:
            print(f"Exception raised of type{args[0]}")
            return True
        else:
            return False











    