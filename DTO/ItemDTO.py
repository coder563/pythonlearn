'''itemdto = {

    "name":"Potion",
    "location":Location("name"),
    "description":"Recover 20 HP",
}'''


class itemDto:
    def __init__(self, *args,**kwargs) -> None:
        self.name = kwargs[name]
        



