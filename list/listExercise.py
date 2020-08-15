# Create a list called instructors

# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"

# Remove the last value in the list

# Remove the first value in the list

# Add the string "Done" to the beginning of the list

# Run the tests to make sure you've done this correctly!
#
# instructors = []
# instructors.extend(["Colt","Blue","Lisa"])
# instructors.pop()
# instructors.pop(0)
# instructors.insert(0,"Done")
# # print(instructors[::-1])
#
#
# a = [5,2,6,1,4,8,6,1,4]
# print(a.index(min(a)))


t = int(input())

for _ in range(t):
    n , k = map(int , input().split())
    print(n)
    print(k)
    print("*********")
    print(type(n))
    # print(k-1 if ((k-1) | k) <= n else k-2)
# print(n)
# print(k)