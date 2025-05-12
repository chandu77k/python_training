#Write a Python program to create a tuple containing five different data types: integer, string, float, list, and another tuple.
firstTuple = (7,"Chandu",7.5,["alpha","beta","gamma"],(1,"dhanush"))
print(firstTuple)

#2. Access Elements in a Tuple
my_tuple = ('apple', [10, 20], (1, 2, 3), 4.5, 'banana')
print(my_tuple[1])
insideTuple = my_tuple[2]
print(insideTuple[1])

#Tuple Immutability
"""my_tuple = (1, 2, 3)
my_tuple[1] = 4"""
#We can't directly do any operations in a tuple we need to convert it into list
my_tuple1 = (1,2,3)
my_list = list(my_tuple1)
my_list[1] = 4
my_tuple1 = tuple(my_list)
print(my_tuple1)

#Unpack the tuple coordinates = (45.4215, -75.6972) into two variables latitude and longitude, and print them.
tupleValues = (45.4215, -75.6972)
latitude = tupleValues[0]
longitude = tupleValues[1]
print("latitude : ",latitude)
print("longitude : ",longitude)

#Write a function that takes two tuples of integers and returns a new tuple with the element-wise sum.
def addition():
    list1 = []
    list2 = []
    list3 = []
    print("Enter Tuple 1 : ")
    for i in range(3):
        input1 = int(input())
        list1.append(input1)
    tuple1 = tuple(list1)
    print("Enter Tuple 2 : ")
    for i in range(3):
        input2 = int(input())
        list2.append(input2)
    tuple2 = tuple(list2)
    print(tuple1)
    print(tuple2)
    for i in range(len(tuple1)):
        tuple3 = tuple1[i] + tuple2[i]
        list3.append(tuple3)
    addTuple = tuple(list3)
    print(addTuple)
addition()