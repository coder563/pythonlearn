from dataclasses import dataclass
import pprint


class PasswordAuth:


    def __init__(self, name, password):
        self.name = name
        self.password:str = None


    @property
    def password(self):
        raise AttributeError('Password is write only')

    @password.setter
    def password(self,new_password):
        password = new_password    
    


    

    


if __name__ == '__main__':
    P1 = PasswordAuth()

    pprint.pprint(P1.__dict__)
    pprint.pprint(dir(P1))
    pprint.pprint(locals()['P1'].__doc__)

