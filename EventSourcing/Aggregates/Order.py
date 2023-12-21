from Events import OrderCreated, StatusChanged
class Order: 

    @classmethod
    def create_order(cls, user_id:int):
           initial_event = OrderCreated(user_id)
           instance  =  cls[initial_event]
           instance.changes = [initial_event]
           return isinstance




    def __init__(self, events ) -> None:
       for event in events:
            self.apply(event)

       self.changes = []
       
         
         
    def apply(self, event):
        if isinstance(event, OrderCreated):
            self.user_id = event.user_id
            self.staus = 'new'
        elif isinstance(event,StatusChanged ):
            self.status = event.new_status
        else:
            raise ValueError(f'{type(event)} Unknown Event Type')
        
    def set_status(self, new_status: str):
        if new_status not in ('new', 'paid', 'confirmed', 'shipped'):
             raise ValueError(f'{new_status} is not a correct status!')
         
        event = StatusChanged(new_status)

        self.apply(event)
         
        self.changes.append(event)
    
    def Howdy(arg1, arg2):
        pass

    def Howdy(arg1, arg2, arg3):
        pass

