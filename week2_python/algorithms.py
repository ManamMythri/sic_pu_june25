

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 

    return -1 
arr =list(map(int,input().split()))
target = int(input())
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

#bubble sort

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        sorted=True
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j+1]= arr[j+1],arr[j]
               
                sorted=False
        if sorted:
            break

arr=list(map(int,input().split()))
print("Original list:", arr)
bubble_sort(arr)

print("Sorted list:",arr)




#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(2,n):
        element=arr[i-1]
        position=i-1
       
        for j in range(i-1 ,n):
            if arr[j]<element:
                element=arr[j]
                position=j
                arr[position], arr[i - 1] = arr[i - 1], arr[position]
arr = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

print("Original list:", arr)

selection_sort(arr)

print("Sorted list:", arr)


#orange problem
def orange(n,arr):
    k=0
    pivot=arr[n-1]
    for i in range(n-1):
         if arr[i]<= pivot:
             arr[i],arr[k]=arr[k],arr[i]
             k+=1
    arr[k],arr[n-1]=arr[n-1],arr[k]
    return arr
n=int(input())
arr=list(map(int,input().split()))
result=orange(n,arr)
print(result)



#quick sort
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)   
        quick_sort(arr, pivot_index + 1, high) 

def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1        
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Original array:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)

