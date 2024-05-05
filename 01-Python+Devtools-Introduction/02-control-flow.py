# Some examples for control flow in Python

use_case = input("What shall I do?\n")

print("Let's check type of input " + str(type(use_case)))

use_case = int(use_case)
print("Let's check type of input " + str(type(use_case)))

if use_case == 1:
    print("I do use case one - whatever that is")
if use_case == 2:
    print("I do use case two - whatever that is")

match use_case:
    case 1:
         print("I do use case one - with matching")
    case 2:
         print("I do use case two - with matching")
    case _:
        print("no idea what to do - but at least you get some output")