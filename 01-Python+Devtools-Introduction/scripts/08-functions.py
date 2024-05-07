# Examples how functions work in Python
# to see many more variants, see https://www.w3schools.com/python/python_functions.asp
import sys

def main():
    print("This is a fake main function")
    helloWorld("you")
    helloWorld("major Tom")
    helloWorldToList("Alice", "Bob", "Charlie")
    helloWorldWithDefault()
    helloWorldWithDictionary(first="Alice", second="Bob")
    print(helloWorldWithRetun("Alice"))
    print ('argument list', sys.argv) # Note scope
    print(myLenghts("test"))
    print(myLenghts("test2"))

def helloWorld(toWhom):
    print("Hello World to", toWhom)

def helloWorldToList(*toWhom):
    print("Hello World to", *toWhom)

def helloWorldWithDefault(name = "Charlie"):
    print("Hello World to", name)

def helloWorldWithDictionary(**toWhom):
    print("Hello World with", toWhom)
    print(toWhom['first'])

def helloWorldWithRetun(toWhom):
    result = "Hello " + toWhom
    return result

# just for completness, this how you can define a lambda expression
myLenghts = lambda s: len(s)

main() # is this a good idea?