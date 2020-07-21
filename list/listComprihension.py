
# Given a list ["Elie", "Tim", "Matt"], create a variable called answer , which is a new list
# containing the first letter of each name in the list. I would use a list comprehension,
# though you could also loop over manually.

# Given a list [1,2,3,4,5,6] , create a new variable called answer2
# , which is a new list of all the even values.  Another good candidate for a list comp.

answer = [name[0] for name in ["Elie", "Tim", "Matt"]]

answer2 = [num for num in [1,2,3,4,5,6] if num%2==0]

print(answer)
print(answer2)

# 1. Given two lists [1,2,3,4]  and [3,4,5,6] , create a variable called answer,
# which is a new list that is the intersection of the two. Your output should be
# [3,4] .  Hint: use the in   operator to test whether an element is in a list.  For example:
# 5 in [1,5,2]  is True.  3 in [1,5,2]  is False.

#2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2,
# which is a new list with each word reversed and in lower case (use a slice to do the reversal!)
# Your output should be ['eile', 'mit', 'ttam']

print([num for num in [1,2,3,4] if num in [3,4,5,6]])
print([''.join(word[::-1]).lower() for word in ["Elie", "Tim", "Matt"]])

# For all the numbers between 1 and 100(including 100), create a variable called answer
# , which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
print([num for num in range(1,101) if num%12==0])


# Given the string "amazing", create a variable called answer, which is a list containing all the
# letters from "amazing" but not the vowels (a, e, i, o, and u).
# The answer should look like: ['m', 'z', 'n', 'g'].Use a list comprehension!
print([char for char in "amazing" if char not in "aeiou"])

# Using a nested list comprehension and range(), create a variable called answer with the following
# value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]]. To break it down...start by using
# range and a list comp to generate the list [0,1,2]. And then repeat that whole
# thing 3 times in a nested list comp. It's all a bit tricky to discuss,
# so maybe it's just best to look at the solution if you get stuck.
print([[num for num in range(0,3)] for val in range(0,3)])


# Using list comprehension, create a variable called answer with the following value :
# it's a nested list. 10 rows, each row contains the numbers 0-9.
# Don't worry about the formatting/spacing, I just added a bunch of returns to make things clearer.
# Your answer will be all on one giant line. Use nested list comprehension and range() to accomplish this.
print([[num for num in range(0,10)] for num in range(0,10)])