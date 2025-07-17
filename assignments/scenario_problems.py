#reflection problem
def is_sample_reflection(word1,word2):
    reversed_word=word1[::-1]
    if len(word1) != len(word2):
        return -1
    n=len(word1)
    for i in range(n):
        rotated=word1[-i:]+word1[:-i]
        if rotated==word2:
            return 1
    return -1
word1=input("enter word:")
word2=input("enter word:")
is_sample_reflection(word1,word2)



#array transport
n=int(input("size of array n: "))
arr=list(map(int,input().split()))
m=int(input("size of array m: "))
brr=list(map(int,input().split()))
arr.sort()
brr.sort()
missing=[]
i=0
j=0
while j<len(brr):
    if i < len(arr) and arr[i]==brr[j]:
        i+=1
        j+=1
    else:
        missing.append(brr[j])
        j+=1
for num in missing:
    print(num,end=" ")


#arrangement of boys and girls
def is_arrangement_possible(boys, girls):
    n = len(boys)
    boys.sort()
    girls.sort()
    valid_boy_first = True
    for i in range(n):
        if boys[i] > girls[i]:
            valid_boy_first = False
            break

    valid_girl_first = True
    for i in range(n):
        if girls[i] > boys[i]:
            valid_girl_first = False
            break

    if valid_boy_first or valid_girl_first:
        return "YES"
    else:
        return "NO"
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    girls = list(map(int, input().split()))
    boys = list(map(int, input().split()))

    result = is_arrangement_possible(boys, girls)
    results.append(result)

for res in results:
    print(res)



#list partitioning
def vaild_count(n,x,y,arr):
    arr.sort()
    a=arr[:y]
    b=arr[y:]
    if a[-1]<b[0]:
        return b[0]-a[-1]
    else:
        return 0
n,x,y=map(int,input().split())
arr=list(map(int,input().split()))
print(vaild_count(n,x,y,arr))


#cloud computing
def cloud_computing_server(num_of_req, req_list):
    server1 = 0
    for i in range(num_of_req):
        if i%2 == 0:
            server1 += int(req_list[i])
    print('Total number of memory units allocated/deallocated in server1 :',server1)
num_of_req = int(input('Enter number of requests'))
req_list = (input('Enter the requests :')).split()
cloud_computing_server(num_of_req, req_list)


#orange partioning
def orange_partioning(arr,n):
    k = 0
    pivot = arr[n-1]
    for i in range(n-1):
        if arr[i] <= pivot:
            arr[i],arr[k] = arr[k],arr[i]
            k += 1
    arr[k],arr[n-1] = arr[n-1],arr[k]
    return arr
n = int(input("No:of oranges: "))
arr = list(map(int,input().split()))
result=orange_partioning(arr,n)
print(result)


