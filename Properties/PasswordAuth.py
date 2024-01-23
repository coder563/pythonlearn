from dataclasses import dataclass
import pprint

@dataclass(frozen=True)
class PasswordAuth:
    passwordassword:str = None
    retry_cound:int=0


    


if __name__ == '__main__':
    P1 = PasswordAuth()

    pprint.pprint(P1.__dict__)
    pprint.pprint(dir(P1))
    pprint.pprint(locals())
    

