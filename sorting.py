#Sorting the array in descending order without using sort function
'''n = int(input("Enter length of array:"))
arr = []
for i in range(n):
    ele = int(input("Enter the number:"))
    arr.append(ele)
print("Unsorted array:", arr)
for i in range(n):
    for j in range(i, n-1):
        if arr[i] < arr[j + 1]:
            arr[i], arr[j+1] = arr[j+1], arr[i]
print("Sorted array:", arr)'''

'''
Sortings:
Bubble sort
Selection sort
Insertion sort
'''

'''
Bubble sort(Algorithm)
1. start index
2. read array of size n
3. for each pass compare adj element
repeat for 0-> n-1:
4. for j 0-> n-i-1:
swap a[j], a[j+1]
5. after each pass the largest element moves to the 
6. repeat pass till all elements are sorted.

'''
# Bubble sort code
'''arr = list(map(int, input("Enter the array:").split()))               
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)'''

'''
Selection Sort(Algorithm)
1. Start from the first index i=0
2. Assume current position is minimum
3. Search the rest of the array to find the actual minimum
2-3  steps
for i : 0-> n-1
      min_index = 0
      for j: i+1 to n-1
if arr[j] < arr[min_index]
4. swap
swap arr[i] arr[min_index]
5. repeat will the last index
'''

#Selection sort code
'''arr = list(map(int, input("Enter the array:").split()))
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j]<arr[min_index]:
            min_index = j
    arr[i], arr[min_index]=arr[min_index], arr[i]
print("sorted array:", arr)'''

'''
Insertion sort(Algorithm)
1. Start from second value assuming 1st index value as sorted
for i-> 1 to n-1
2. pick the current element as key
key = arr[i]
3. compare with previous element
while j>=0 and arr[j]>key
4. Shift all the larger elements to the right
arr[j+1] = arr[j]
5. Insert the key in position
6. repeat till sorted
'''

#Insertion sort code
'''arr = list(map(int, input("Enter the array:").split()))
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print("Sorted array:", arr)'''

'''
Flip sort : Pancake sort(Algorithm)
1. find the max element in the unsorted array
2. bring it to the zero index value followed by respective values
3. then flip the total array to the correct position for array of size n:
start for last index(n-1)
repeat
- find index max(0->i)
- flip form 0-> max_index
- flip 0-> i
'''

#flip sort code
'''def flip(arr, k):
    start = 0
    while start<k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k-=1
def pancake(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        max_index = 0
        for j in range(1, i+1):
            if arr[j]>arr[max_index]:
                max_index = j
        if max_index != 0:
            flip(arr, max_index)
        flip(arr, i)
    return arr

arr = list(map(int, input("Enter the array:"). split()))
sortedarray = pancake(arr)
print("Sorted array", sortedarray)'''

'''
quick sort(Algorithm)
1. choose pivot element (last)
2. rearrange the array so that
- element <pivot leave it 
- element >pivot swap
3. repeat same process till all elements are sorted
'''

#quick sort code
'''def quick(arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quick(arr, low, pi-1)
        quick(arr, pi+1, high)
def partition(arr, low, high):
    piviot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j]< piviot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = list(map(int, input("Enter the array:").split()))
quick(arr, 0, len(arr)-1)
print("Sorted array", arr)'''