#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    name = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if(len(firstName)<=20 and len(emailID)<=50):
            if re.search('@gmail\.com',emailID):
                name.append(firstName)

name.sort()

for item in name:
    print(item)



