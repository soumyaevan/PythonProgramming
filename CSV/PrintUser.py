'''
print_users For this exercise, you'll be working with a file called users. csv user's last name.
Implement the following function: Each row of data consists of two columns: a user's first name, and a .
prints out all of the first and last names in the print_users users. csv file
'''

'''
print_users() # None
# prints to the console:
# Colt Steele
'''

from csv import DictReader
def print_users():
    with open('users.csv') as file:
        Csv_reader = DictReader(file)
        for item in Csv_reader:
            print("{} {}".format(item['First Name'],item['Last Name']))