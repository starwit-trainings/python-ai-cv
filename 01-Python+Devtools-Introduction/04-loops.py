# How to use loops

iterations = input("How many iterations?\n")

try:
    # Convert it into integer
    iterations = int(iterations)
    print("Input is an integer number. Number = ", iterations)
except ValueError:
    print("not an integer, defaulting to 10")
    iterations = 10

print("Let's check type of input " + str(type(iterations)))

i = 1
while i < iterations:
  print("While iteration: " + str(i))
  i += 1

for i in range(iterations):
  print("for iteration: " + str(i))
  i += 1
  # security precaution
  if i > 30:
    print("that is just too much, stopping")
    break