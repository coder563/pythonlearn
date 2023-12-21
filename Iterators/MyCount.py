class MyCount:
    def __init__(self, start=0, step=1, end=100 ):
       
        self.value = start
        self.end = end
        self.step = step

        print(f"start = {self.value}, step = {self.step}, end= {self.end}")

    def __iter__(self):
        return self

    def __next__(self):
                
        curr = self.value
        
        if self.value > self.end:
            print(f"curr greater than end, curr = {curr}")
            raise StopIteration
        else:
            print(f"curr = {curr}")
            self.value +=self.step
            return curr
    

