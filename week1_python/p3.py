# check if a year is leap year

input_year=int(input('Enter the year: '))
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(input_year,'is a Leap year')


# check if a positive integer is perfect square

import math
input_number=int(input("Enter the positive number: "))
if input_number > 0:
    if int(input_number ** 0.5)** 2 == input_number:
        print(input_number,"is a perfect square")
else:
    print("enter positive integer")  


# Find smallest of 3 distinct numbers

input_number1=int(input("Enter number1: "))
input_number2=int(input("Enter number2: "))
input_number3=int(input("Enter number3: "))
if input_number1 < input_number2:
    print(input_number1, "is smallest")
elif input_number2 < input_number3:
    print(input_number2,"is smallest")
else:
    print(input_number3,"is smallest")