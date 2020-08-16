'''
Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

Example

For n = "1302" and x = 5, the output should be
baseConversion(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.
'''

def baseConversion(n, x):
    return hex(int(str(n),x))[2:]
