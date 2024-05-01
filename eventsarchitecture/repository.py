from typing import Dict, List


from events import Event
from models import User


class UserRepository:
    
    saved_user : Dict[int, List[Event]] = {}

    def get(self, id:int):

        events = self.saved_user.get(id)
        if events is None:
            raise ValueError('No events in the list')
         
        user = User()
        for event in events:
            user.apply(event)
        
        return user
    
    def save(self, user:User):
        if user.id is None:
            raise ValueError("User has no ID")
        
        self.saved_user[user.id] = list(user.events)

    def get_user_id(self):
        return len(self.saved_user)





