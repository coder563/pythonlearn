from dataclasses import dataclass


@dataclass
class Order:
    user_id:int
    status:str


@property
def user_id(self):
    return self.user_id

@user_id.setter
def user_id(self,new_status:str):
    if new_status not in ('new','paid','confirmed','shipped'):
        raise ValueError(f'{new_status} not in correct status')    
    else:
        self.status = new_status



