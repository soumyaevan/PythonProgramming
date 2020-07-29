def contains_purple(*args):
    return "purple" in args


# Define combine_words below:
def combine_words(string,**kwargs):
    if "prefix" in kwargs:
        return "{}{}".format(kwargs["prefix"],string)
    elif "suffix" in kwargs:
        return "{}{}".format(string,kwargs["suffix"])
    return string


def factorial(n):
    result = 1
    if n== 1:
        result = 1
    else:
        result = n * factorial(n-1)
    return  result

print(factorial(0))

