# given a list.
# Objective is to concatenate the strings of the list ans create a large string
# No space in between
# result needs to be in upper case

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for item in sounds:
    result = result + item
print(result.upper())