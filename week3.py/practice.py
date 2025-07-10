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
