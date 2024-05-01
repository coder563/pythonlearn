from events import Event, UserCreated, UserBalanceChanged
class User:
    def __init__(self ):
        self.id = None
        self.username = None
        self.balance = None
        self.events = []

    def apply(self, event: Event):
        if isinstance(event,UserCreated):
            self.id = event.id
            self.username= event.username
            self.balance= event.balance
        elif isinstance(event,UserBalanceChanged):
            self.balance += event.change
        
        self.events.append(event)   




    
    def create_user(self,id: int , name: str, balance: int):
        self.apply(UserCreated(id=id,username=name,balance=balance))
    
    def change_balance(self,change:int):
        if self.balance + change < 0:
            raise ValueError('Balance is falling below 0')
        self.apply(UserBalanceChanged(self.id,change=change))
                   




                   
                   

