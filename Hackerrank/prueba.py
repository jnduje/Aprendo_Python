
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name, lastname = s.split(" ")
    
    return print(f'{name.capitalize()} {lastname.capitalize()}')


if __name__ == '__main__':
    s = input()
    result = solve(s)

