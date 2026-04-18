'''Searching in array data structures:
1. searching on number/string
2. occurrences
3. finding the duplicate elements - print duplicate, remove duplicate
1 2 3 3 4 5 6
lineaar -> approach
arr = [10,20,30,40,50]
search = 30
30 is found at index value 2'''

#searching an element and returning the index value
'''arr = list(map(int, input("Enter the elements of the array:").split()))
search = int(input("enter the value to be searched:"))
found = False
for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("Element not found !!!!")'''

#searching an element and returning the index value for string array
'''arr = input("Enter the elements of the array:").split()
search  = input("enter the value to be searched:")
found = False
for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("Element not found !!!!")'''

#find greater than a given value in an array
'''arr = list(map(int, input("Enter the elements of the array:").split()))
value = int(input("enter the value:"))
found = False
for i in range(len(arr)):
    if arr[i] > value:
        found = True
        print(arr[i])
if not found:
    print("No element is greater than the given value !!!!")'''


    