# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

# Examples

# divide(4,2)  2
# divide([],"1")  "Please provide two integers or floats"
# divide(1,0)  "Please do not divide by zero"
def devide(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        print("Please provide two integers or floats")
    except ZeroDivisionError:
        print("Please do not devide bu zero")