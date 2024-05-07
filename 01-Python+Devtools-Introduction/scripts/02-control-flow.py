# Some examples for control flow in Python

use_case = input("What shall I do?\n")

print("Let's check type of input " + str(type(use_case)))

# note that input always outputs string
if type(use_case) == int:
    print("right type, let's move on")
else:
    print("wrong type...")

# check if we can convert input to integer
use_case = int(use_case)
print("Let's check type of input ", str(type(use_case))) # note different use of print function

# simple if
if use_case == 1:
    print("I do use case one - simple if")
if use_case == 2:
    print("I do use case two - simple if")

# using elif
if use_case == 1:
    print("I do use case one - using elif")
elif use_case == 2:
    print("I do use case two - using elif")
else:
    print("no idea what to do - but at least you get some output")

# latest addition - matching
match use_case:
    case 1:
         print("I do use case one - with matching")
    case 2:
         print("I do use case two - with matching")
    case _:
        print("no idea what to do - but at least you get some output")