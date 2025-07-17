#Count number of Prime digits in a number
number=int(input("Enter the number to count number of prime digits in a number: "))
prime_digits = {2, 3, 5, 7}
count = 0
while number > 0:
    digit = number% 10
    if digit in prime_digits:
        count += 1
    number//= 10
print("Number of prime digits:", count)



#Find biggest digit in a number
number = int(input("Enter a number: "))
number = abs(number) 
largest_digit = 0
while number > 0:
    digit = number % 10
    if digit > largest_digit:
        largest_digit = digit
    number //= 10

print("Largest digit:", largest_digit)




#Find smallest digit in a number
number = int(input("Enter a number: "))
number = abs(number) 
smallest_digit = 9
while number > 0:
    digit = number % 10
    if digit < smallest_digit:
        smallest_digit = digit
    number //= 10

print("smallest digit:", smallest_digit)




#Print the Prime numbers in decreasing order between m and n (m < n)

m=int(input("enter a value of m(starting number): "))
n=int(input("enter a value of n(ending number) : "))
def is_prime(number):
    if number<=1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print("Prime numbers between {} and {} in decreasing order:".format(m,n))
for i in range(n, m - 1, -1):
    if is_prime(i):
        print(i, end=' ')



        
#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2

input_number = int(input("Enter the term number : "))
if input_number == 1:
    print("Term 1 is 1")
elif input_number == 2:
    print("Term 2 is 2")
else:
    a, b = 1, 2
    for i in range(3, input_number + 1):
        a, b = b, a + b
    print('{} Term is {}'.format(input_number,b))




#Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)

n = int(input("Enter value of n (1 to 4): "))
m = int(input("Enter number of terms m (2 to 10): "))

total = 0
power = 1
denominator = 1
sign = -1

for i in range(m):
    denominator=2 * i + 1
    term = sign * (n ** power) / denominator
    total += term
    power *= 2
    sign *= -1
print("Sum of the series:", total)

''' Print the following shapes by accepting number of lines
A. Right Angled Triangle
B. Equi lateral Triangle
C. Hollow Square
D. howllow Rhombus
E. Pascal's Triangle
F. X shape
G. X shape inside hollow Square
H. Benzene Ring (C6H6) Hexagon

'''

#A. Right Angled Triangle
lines = int(input("Enter the number of lines: "))
for i in range(1, lines + 1):
    print('*' * i)

#Equi lateral Triangle
lines = int(input("Enter the number of lines: "))
for i in range(1,lines+1):
    spaces = ' ' * (lines - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
#Hollow square 
lines = int(input("Enter the number of lines: "))
for i in range(lines):
    for j in range(lines):
        if i==0 or i==lines-1 or j==0 or j==lines-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#hollow rhombus

lines = int(input("Enter number of lines: "))
for i in range(lines):
    print(" "*(lines-i),end=" ")
    for j in range(lines):
        if j==0 or j==lines-1 or i==0 or i==lines-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



#. Pascal's Triangle

lines = int(input("Enter number of lines: "))
triangle=[]
for i in range(lines):
    row=[]
    for j in range(i+1):
        if j==0 or j==i:
            row.append(1)
        else:
            row.append(triangle[i-1][j-1]+triangle[i-1][j])
    triangle.append(row)

for i in range(lines):
    for j in range(lines-i-1):
        print(format(" ","<2"),end= "")
    for j in range(i+1):
        print(format(triangle[i][j],"<3"),end=" ")
    print()


#x shape
lines = int(input("Enter number of lines: "))
for i in range(lines):
    for j in range(lines):
        if i==j or i+j==lines-1:
            print("*",end=" ")
        else:
            print(end=" ")
    print()


#benzene ring hexagon
lines = int(input("Enter number of lines: "))
width = 2 * lines - 1
print(' ' * lines + '_' * width)
for i in range(lines):
    print(' ' * (lines - i - 1) + '/' + ' ' * (width + 2 * i) + '\\')
for i in range(lines):
    print(' ' * i + '\\' + ' ' * (width + 2 * (lines - i - 1)) + '/')
print(' ' * lines+ '-' * width)



#X shape inside hollow Square
lines = int(input("Enter number of lines: "))

for i in range(lines):
    for j in range(lines):
        if i in (0, lines-1) or j in (0, lines-1) or j == i or j == lines-i-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()


#Find sum of the Even placed digits in the given number.
input_number = input("Enter a number: ")
sum = 0

for index in range(len(input_number)):
    if (index + 1) % 2 == 0:
        sum += int(input_number[index])

print(sum)
 
# Find sum of the Odd placed Even digits in the given number.
input_number = input("Enter a number: ")
sum = 0

for index in range(len(input_number)):
    if (index + 1) % 2 != 0:
        sum += int(input_number[index])

print(sum)


#Find smallest and biggest elements in an list of n number

user_input = input("Enter numbers separated by space: ")
input_list = list(map(int, user_input.split()))
input_list.sort() 
smallest = input_list[0]
largest = input_list[-1]

print("Smallest element:", smallest)
print("Largest element:", largest)


#Find the frequency an element in a list of n elements.

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

element = int(input("Enter the element to find its frequency: "))

count = 0
for num in numbers:
    if num == element:
        count += 1
print(f"The frequency of {element} is: {count}")



#Remove the duplicates in a list of size n

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)


#Given a number, find very next possible bigger number that has all the digits of the given number.


num = input("Enter a number: ").strip()
digits = list(num)  
i = len(digits) - 2
while i >= 0 and digits[i] >= digits[i + 1]:
    i -= 1
if i < 0:
    print("No larger number possible")
else:
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i+1:] = reversed(digits[i+1:])
    print("Next bigger number is", "".join(digits))

 # Accpet a number from the user (4 digit number where a digit can repeat at most 2 times )and 
    # print the coutn of recursions reqired to arrive at Karpekar's Constant.
n = int(input("Enter a 4-digit number): "))
count = 0
prev = -1

while True:
    s = f"{n:04d}"                  
    asc = int("".join(sorted(s)))
    desc = int("".join(sorted(s, reverse=True)))
    diff = desc - asc

    count += 1
    if diff == prev or diff == 6174 or diff == 0:
        n = diff
        break

    prev, n = diff, diff

if n == 6174:
    print("Reached Kaprekar's constant 6174 in", count, "iterations")
elif n == 0:
    print("Reached 0 in", count, "iterations (no further progression)")
else:
    print("Stopped at", n, "after", count, "iterations")

# Find Factorial of a number
input_number=int(input("Enter the number: "))
fact = 1
for i in range(1, input_number + 1):
    fact *= i
print(f"{input_number}! = {fact}")


#Print N Fibo terms with 1 and 2 as 1st 2 terms.

n = int(input("Enter N (number of terms): "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(1)
else:

    a, b = 1, 2
    print(a, end=" ")
    if n >= 2:
        print(b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a, b = b, c

print()  


#Find sum of list elements
number = list(map(int, input("Enter numbers: ").split()))
total = 0
for num in number:
    total += num
print("Sum of list elements:", total)
