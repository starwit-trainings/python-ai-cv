# How to handle exceptions

use_case = input("What shall I do?\n")

try:
    # Convert it into integer
    use_case = int(use_case)
    print("Input is an integer number. Number = ", use_case)
except ValueError:
    print("not an integer")

print("Let's check type of input " + str(type(use_case)))

match use_case:
    case 1:
         print("I do use case one - with matching")
    case 2:
         print("I do use case two - with matching")
    case _:
        print("no idea what to do - but at least you get some output")