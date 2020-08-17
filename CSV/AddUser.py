'''
add user For this exercise, you'll be working with a file called users. csv user's last name.
Implement the following function: Each row of data consists of two columns: a user's first name,
and a Takes in a first name and a last name and adds a new user to the add user users. csv file.
'''

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
from csv import DictWriter

def add_user(fname, lname):
    with open('users.csv','a') as file:
        headers = ('First Name','Last Name')
        csv_writer = DictWriter(file,fieldnames=headers)
        csv_writer.writerow({
            headers[0]:fname,
            headers[1]:lname
        })