
import numpy as np
# arange()

array1 = np.arange(10)
array2 = np.arange(10, 20)
array3 = np.arange(10, 30, 3)
print(type(array1))
print(array1)
print(array2)
print(array3)


import numpy as np
# ones()

array1 = np.ones(10)
array2 = np.ones((2, 8))
array3 = np.ones((3, 5))

print(type(array1))
print(array1)
print(array2)
print(array3)


import numpy as np

vector = np.arange(5)
print('Vector shape:', vector.shape)

matrix = np.ones([3, 2])
print('Matrix:', matrix)
print('Matrix shape:', matrix.shape)

tensor = np.zeros([2, 3, 3])
print('Tensor:', tensor)
print("Tensor shape:", tensor.shape)


import numpy as np

arr = np.arange(1, 10)
print(arr, '\n')

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(1,9)
print(arr)

arr = arr.reshape(1, 4) # ValueError
print(arr) 

import numpy as np

arr1 = np.arange(12)

arr2 = arr1.reshape(2, 6)
arr3 = arr1.reshape(6, 2)
arr4 = arr1.reshape(3, 4)
arr5 = arr1.reshape(12, 1)
arr6 = arr1.reshape(4, 3)

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)

import numpy as np

arr = np.arange(1, 10).reshape(3, -1) # Here python infers/decides the number of columns by itself.
print(arr)

import numpy as np

arr1 = np.arange(1, 10)
arr2 = np.arange(2, 25, 2)
arr3 = arr1.reshape(3, -1)
arr4 = arr2.reshape(4, -1)
arr5 = arr2.reshape(2, -1)
arr6 = arr2.reshape(3, -1)
arr7 = arr2.reshape(-1, 4) # Numpy predicts and fixes number of rows
#arr8 = arr2.reshape(-1, -1) #ValueError. Can only specify one unknown dimension

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)
print('Arr7:\n', arr7)
#print('Arr8:\n', arr8)


import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])

array1.shape = (6, 2)
print(array1.shape)
print(array1)

array1.shape = (3, 4)
print(array1.shape)
print(array1)

array1.shape = (4, 3)
print(array1.shape)
print(array1)

array1.shape = (4, 2) # Error New shape of the array must consist of same number of elements as that of original array
print(array1.shape)
print(array1)


import numpy as np

matrix1 = np.array([[3, 4, 5], [2, 6, 9]])
matrix2 = np.array([[3, 4], [3, 5], [2, 6]])

matrix3 = np.dot(matrix1, matrix2)

print('Matrix3=\n', matrix3) 

import numpy as np

array = np.array([2, 4, 6, 8, 9, 19])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)


import numpy as np

array = np.array([[2, 4, 6, 8], [9, 19, 4, 10]])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)

import numpy as np

matrix1 = np.array([[3, 3, 4], [2, 3, 9]])
matrix2 = np.array([[2, 5, 4], [2, 3, 19]])

sum_matrix = matrix1 + matrix2
difference_matrix = matrix1 - matrix2
product_matrix = matrix1 * matrix2
quotient_matrix = matrix1 / matrix2

print(sum_matrix)
print(difference_matrix)
print(product_matrix)
print(quotient_matrix)


import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = scipy.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode = ', mode)

import numpy as np
def f(x, y):
	return 10 * x + y

my_aaray = np.fromfunction(f, (5, 4), dtype = int)
print(my_aaray)
# Slicing the Numpy Arrays:
print(my_aaray[2, 3]) # my_array[2][3]
print(my_aaray[0:5, 1]) # From Row-1 to Row-5, print the 2nd element
print(my_aaray[ : , 1]) # From all rows, print 2nd element
print(my_aaray[1:3, : ]) # From Row-2 to Row-3, print all elements


import numpy as np

import numpy as np
def f(x, y):
	return 10 * x + y

my_array = np.fromfunction(f, (5, 4), dtype = int)

print(f'Before:\n {my_array}')
#my_array[:, [0, -1]] = 0  #For all Rows, set 0 to 1st and last columns
my_array[[0, -1], :] = 0 #For 1st row and last row, set all elements to 0

#After:
print(f'After:\n {my_array}')

import numpy as np

my_array = np.zeros((8, 8), dtype = int)
#my_array[1::2, ::2] = 8
#Starting from row-index-1 and there after, for all alternatives rows, and for all columns from index 0 and there after alternative columns, replace the cells with value 8
my_array[::2, 1::2] = 1
# Odd indexed-rows Even Indexed-Columns
print(my_array)

import numpy as np

# nan is not a number

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)


# In a np array of spendings of the week, find the highest spending and the day.

import numpy as np
week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = 1
big_spending = week_spendings[0]
index = np.argmax(week_spendings)
days = {1:'mon', 2:'tue', 3:'wed', 4:'thus', 5:'fri', 6:'sat', 7:'sun'}
print(big_spending, days[index])


for i in range(len(week_spendings)):
	if week_spendings[i] > big_spending:
		big_spending = week_spendings[i]
		index = i

# Replacing values less than 50 with 0 in an array

# Explanation: Using np.where() to replace values meeting the condition
import numpy as np
expenses = np.array([20, 60, 5, 80, 45, 90])
modified_expenses = np.where(expenses < 50, 0, expenses)
print(modified_expenses)  # Output: [ 0 60  0 80  0 90]



#Generating random floating-point numbers between 0 and 1

#Explanation: Using np.random.rand() to create a random array of given shape
import numpy as np
random_data = np.random.rand(3, 4) # Creates a 3x4 array with random values
print(random_data)

import random

user_number = int(input('Enter a number of your choice between [0 and 9]: '))
system_number = random.randint(0,9) 
if system_number == user_number:
	print('CrorePati')
else:
	print('RoadPati')



import pandas as pd

def read_csv_file():
    # Define the path to the CSV file
    file_path = r"C:\Users\Lenovo\Downloads\students.csv"

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())


def read_csv_file1():
    file_path = r"C:\Users\Lenovo\Downloads\students.csv"

    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        print(row[0], '  ', row[1])


def read_csv_file2():
    file_path = r"C:\Users\Lenovo\Downloads\students.csv"

    df = pd.read_csv(file_path)
    for row in df.iterrows():
        print(row[1][0], row[1][1])

#read_csv_file()
#read_csv_file1()
read_csv_file2()


#Creating a DataFrame

#Explanation: Using pandas to create a DataFrame from a dictionary

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)


# # Generating 23 equally spaced values between 0 and 100

# Explanation: Using np.linspace() to generate specified number of values in a range
import numpy as np
values = np.linspace(0, 100, 23)
print("Generated values:", values)
print("Total count:", len(values)) 

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('data.csv')  # Reads the CSV file
df.head()  # Displays the first 5 rows
print(df.isnull().sum()) 
