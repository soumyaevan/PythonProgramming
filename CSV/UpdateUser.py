'''
update_users For this exercise, you'll be working with a file called users. csv user's last name.
Implement the following function: Each row of data consists of two columns: a user's first name, and a :
Takes in an old first name, an old last name, a new first name, and a new last name. Updates the file so that update _
users users. csv any user whose first and last names match the old first and last names are updated to the new first
and last names. The function should return a count of how many users were updated.
'''

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
import csv
def update_users(old_fn,ols_ln,new_fn,new_ln):
    update = 0
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    with open("users.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            if row[0]==old_fn and row[1]==ols_ln:
                csv_writer.writerow([new_fn,new_ln])
                update += 1
            else:
                csv_writer.writerow(row)
    return update
