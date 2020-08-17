'''
find user For this exercise, you'll be working with a file called users. csv user's last name.
Implement the following function: Each row of data consists of two columns: a user's first name,
and a Takes in a first name and a last name and searches for a user with that first and last name in the file.
If the user is find user users. csv found, find_user returns the index where the user is found.
Otherwise it returns a message stating that the user wasn't found.
'''

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
import csv
def find_user(fname, lname):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        for item in data:
            if fname in item and lname in item:
                return data.index(item)
        return "{} {} not found".format(fname, lname)

