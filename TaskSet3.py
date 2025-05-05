from xmlrpc.client import Boolean

"""1. Add a Number and a String Containing a Number"""
num = 5
str_num = "10"
convert_num = int(str_num)
print(num+convert_num)

"""2. Input Two Numbers as Strings, Multiply Them as Integers"""
input1 = "4"
input2 = "5"
convert_input1 = int(input1)
convert_input2 = int(input2)
print(convert_input1 * convert_input2)

"""3. Convert a Float to an Int and Observe the Change"""
inputNumber = 9.81
print(int(inputNumber))

"""4.Cast Boolean to Integer and Back"""
boolInput1 = True
boolInput2 = False
convertedBool1 = int(boolInput1)
convertedBool2 = int(boolInput2)
print(convertedBool1)
print(convertedBool2)
print(Boolean(convertedBool1))
print(Boolean(convertedBool2))