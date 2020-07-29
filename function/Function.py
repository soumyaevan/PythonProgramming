'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''
def capitalize(word):
    return "{}{}".format(word[0].upper(),word[1:])

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''
def multiply_even_numbers(lis):
    res = 1
    for num in lis:
        if num %2 == 0:
            res *= num
    return res

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''
def is_palindrome(word):
    word = word.replace(" ","")
    if(word == "".join(reversed(word))):
        return True
    return False



'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
def compact(lis):
    return [i for i in lis if i]



'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def partition(lis, func):
    return [[l for l in lis if func(l)],[m for m in lis if not func(m)]]

print(type("sdfsf")==str)

def calculate(score):
    if score in range(40.0,55.0):
        print("pass")
    else:
        print("fail")

calculate(44.14)