from do_n_times import do_n_times
from do_twice import do_twice



@do_n_times
def greeting(wishes:str=None) -> None:
    print(wishes)

#greeting("Hello")
#with param (function) def do_n_times(times: int = 2) -> ((func: Any) -> ((wishes: str) -> None))
# w/o param (function) def do_n_times(times: int = 2) -> ((func: Any) -> ((wishes: str) -> None))
#do_n_times(1)(greeting)("Hi There")
#do_n_times()(greeting)("Wish Default 2 times")
#do_twice(greeting)("Namaskar")
##do_n_times(greeting)()
greeting("yo")

    