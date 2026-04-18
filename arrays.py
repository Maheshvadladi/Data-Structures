# accessing an array element using index
'''arr = list(map(int, input("Enter the array elements:").split()))
print(arr[2])
print(arr[-2])'''

# travesing an array
'''arr = list(map(int, input("Enter the array elements:").split()))
for i in range(len(arr)):
    print(arr[i], end="->")'''

'''arr = list(map(int, input("Enter the array elements:").split()))
for i in range(len(arr)):
    print(arr[i]+1, end="->")'''
    
# finding the minimum value in array without min
'''arr = list(map(int, input("Enter array elements:").split()))
min = arr[0]
for i in arr:
    if i < min:
        min = i
print("Minimum value is:", min)'''

# finding the maximum value in array without max
'''arr = list(map(int, input("Enter array elements:").split()))
max = arr[0]
for i in arr:
    if i > max:
        max = i
print("Maximum value is:", max)'''

# program to reverse the words in a string
'''words = input("Enter the string:").split()
for word in words:
    print(word[::-1], end=" ")'''

# finding the minimum values in array strings without min
'''arr = input("Enter array elements:").split()
min = arr[0]
for i in arr:
    if len(i) < len(min):
        min = i
print("Minimum value is:", min)'''

# program to find the smallest word lexiographically from the given list of words
'''arr = input("Enter array elements:").split()
min = arr[0]
for i in arr:
    if i < min:
        min = i
print("Smallest word is:", min)'''

