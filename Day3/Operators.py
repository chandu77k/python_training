# #a program to calculate the area of a rectangle (length × breadth).
# length = int(input("Length : "))
# breadth = int(input("Breadth : "))
# area = length * breadth
# print("Area of Rectangle = ", area)
#
# #Calculate the average of three numbers entered by the user.
# number1 =int(input("Number1 : "))
# number2 =int(input("Number2 : "))
# number3 =int(input("Number3 : "))
# result = (number1 + number2 + number3)/3
# print("Average of 3 numbers : ",result)
#
# #Compare two numbers and print which one is greater, or if they are equal.
# input1 = int(input("Input1 : "))
# input2 = int(input("Input2 : "))
# if (input1 > input2):
#     print(input1)
# elif (input2 < input1):
#     print(input2)
# else:
#     print("Equal")
#
# #Check if a person is eligible to vote (age ≥ 18).
# inputAge = int(input("Enter Age : "))
# if inputAge >= 18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")
#
# #Check if a number is within the range (10, 50).
# number = int(input("Enter Number : "))
# rangeBetween = range(10,50)
# if number in rangeBetween:
#     print("It's in the range")
# else:
#     print("It's not in the range")
#
# #Validate a user’s login based on username and password using logical AND.
# usernameInput = input("Enter Username : ")
# passswordInput = input("Enter Password : ")
# username = "chandu"
# password = "Chandu@123"
# if usernameInput in username and passswordInput in password:
#     print("Login Successful")
# else:
#     print("Login Failed")
#
# #Create a variable and apply +=, -=, *=, /= on it. Print the result after each operation.
# assignmentVariable = 7
# assignmentVariable += 5
# print(assignmentVariable)
#
# assignmentVariable -= 5
# print(assignmentVariable)
#
# assignmentVariable *= 5
# print(assignmentVariable)
#
# assignmentVariable /= 5
# print(assignmentVariable)

#Show the result of AND, OR, and XOR on two binary numbers (e.g. 5 and 3).
binaryNumber1 = 5
binaryNumber2 = 3
print(binaryNumber1 & binaryNumber2)
print(binaryNumber1 | binaryNumber2)
print(binaryNumber1 ^ binaryNumber2)