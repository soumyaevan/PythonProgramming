"""
delete users For this exercise, you'll be working with a file called users. csv user's last name.
Implement the following function: Each row of data consists of two columns: a user's first name, and a :
Takes in a first name and a last name. Updates the users. csv file so that any user whose first and last names
match the delete users inputs are removed. The function should return a count of how many users were removed.
"""
'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

import csv
def delete_users(old_fn,ols_ln):
    remove = 0
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    with open("users.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            if row[0]==old_fn and row[1]==ols_ln:
                remove += 1
            else:
                csv_writer.writerow(row)
    return "Users deleted {}.".format(remove)