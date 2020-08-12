class User:
    active_user = 0

    @classmethod
    def print_total_uset(cls):
        return (f"Total active user: {User.active_user}")

    @classmethod
    def createUser(cls, details):
        fname, lname, age = details.split(",")
        return cls(fname, lname, age)

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        User.active_user += 1

    def logout(self):
        User.active_user -= 1
        print(f"{self.fname} is logged out")

    def __repr__(self):
        return (f"User name: {self.fname} {self.lname}, Age: {self.age}")

u1 = User.createUser("Soumya,Sen,26")
u2 = User.createUser("Pranoy,Das,28")
print(User.print_total_uset())
u2.logout()
print(User.print_total_uset())
print(u1)