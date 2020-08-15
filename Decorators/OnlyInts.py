'''
only_ints Write a function called only_ints which accepts a function and returns another function. The function passed
to it should only be invoked if all of the arguments passed to it are integers.
Otherwise the inner function should return "Please only invoke with integers.".
'''

'''
@only_ints 
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if all(isinstance(x,int) for x in args) and all(isinstance(v,int) for (k,v) in kwargs.items()):
            return fn(*args,**kwargs)
        return "Please only invoke with integers."
    return wrapper

@only_ints
def add(x, y):
    return x + y

print(add(x=1, y=2)) # 3
print(add(x="1", y="2")) # "Please only invoke with integers."