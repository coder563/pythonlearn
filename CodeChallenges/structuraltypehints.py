from typing import Protocol

class Printable(Protocol):
    def print_info(self) -> None:
        pass

def print_object(obj: Printable) -> None:
    obj.print_info()

class MyClass:
    def print_info(self) -> None:
        print("Printing information from MyClass")

class AnotherClass:
    def display_info(self) -> None:
        print("Displaying information from AnotherClass")
    
    def print_info(self)->None:
        print('Another class Print_info implementation')

# Both MyClass and AnotherClass can be passed to print_object
print_object(MyClass())
print_object(AnotherClass())