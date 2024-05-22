# examples how lists and dictionaries work

# simple list
myList = ["red","green","blue"]

#for each element
for c in myList:
    print(c)

# access item
print(myList[0])

myList.append("yellow")

print(myList)

# check if an element is part of list
if "yellow" in myList:
    myList.remove("yellow")

print(myList)

# list size
print(len(myList))

numberList = [1,5,9,12,0,4]
print(sum(numberList))

# lists of lists
myColors = [["red","green","blue"],["yellow","magenta","cyan"]]
print(myColors[1][0])

############## dictionaries ##############

# define empty, adding elements
values = {}
values['math I'] = 15
values['math II'] = 16

# define ad-hoc
values = {'math I': 15, 'math II': 16, 'algorithms I': 22, 'algorithms II': 14, 'software architecture': 18}
print(values)

# check if key is existing
if values['math II']:
    del values['math II']
print(values)

for key in values:
    print(key)
    print(values[key])


# dictionary with lists
values = {'A': [37.4, 174, 'male'],
          'B': [36.6, 154, 'female'],
          'C': [37.0, 170, 'male']
          }

for name, record in values.items():
    print(name, ":", record)

# modelling complex data types
values = {
        "sampleNumber": 114,
        "subjects": [
            {"id":'A',"temp": 37.4, "height": 174, "gender": 'male'},
            {"id":'B',"temp": 36.6, "height": 154, "gender": 'female'},
            {"id":'C',"temp": 37.0, "height": 170, "gender": 'male'}
            ]
        }

print("Heights of participants")
for subject in values['subjects']:
    print(subject['height'])