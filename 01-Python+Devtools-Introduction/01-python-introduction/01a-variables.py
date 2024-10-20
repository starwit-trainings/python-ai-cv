# Examples of datatypes available in Python

# basic types
i = 0 # integer
k = 1.0 # float
s = "string" # string

# boolean type
bool_example = True

# None type
none_example = None

bytes_example = b'Hello'
print(f"Bytes: {bytes_example} (Type: {type(bytes_example)})")

complex_example = 2 + 3j
print(f"Complex: {complex_example} (Type: {type(complex_example)})")

# date and time
import datetime

today = datetime.datetime.today()
print(today)
print(today.weekday())