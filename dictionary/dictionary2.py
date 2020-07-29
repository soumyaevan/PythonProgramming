# Following given two lists. create a dictionary where key will be the elements of the first
# list and value will be the element of the second list
# store the result in the answer dictionary

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0, len(list1))}

print(answer)

# following is a list. Make as dictionary from this were first element of will be key and th second will be value
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

p_dict = {person[i][0]: person[i][1] for i in range(0, len(person))}
print(p_dict)

# print(tuple(person).count(["name","Jared"]))
print(list1.count("CA"))

def yell(message):
    return ("{}!".format(message.upper()))

def add(a=5,b=6):
    print(a*a + b)

add(b=5, a=1)

def return_day(n):
    return {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}.get(n,None)
def single_letter_count(string, char):
    return string.upper().count(char.upper())

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

print(multiple_letter_count("dadadadadad"))