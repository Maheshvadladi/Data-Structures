#append operation in array using append method
'''arr = [2,3,4,5]
print("before append:", arr)
arr.append(6)
print("after append:", arr)'''

#insert operation in array using insert method
'''arr = [2,3,4,5,6]
print("before insert:", arr)
arr.insert(2, 4)
print("after insert:", arr)'''

'''n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
print("Array using append:", arr)
index = int(input("enter the value:"))
value = int(input("Enter the value:"))
arr.insert(index, value)
print("Array using insert:", arr)'''

#insert operation in array using array with user input
'''a = list(map(int, input("Enter the array elements:").split()))
print("before insertion:", a)
index = int(input("Enter the index:"))
value = int(input("Enter the value:"))
a.insert(index, value)
print("after insertion:", a)'''

#insert operation in array using character array with user input
'''a = list(map(str, input("enter the character:").split()))
print("before insertion:", a)
index = int(input("enter the index:"))
value = input("enter the value:")
a.insert(index, value)
print("after insertion:", a)'''

#using append and insert method in character array with user input
'''n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(input("Enter the character:"))
print("using append:", arr)
index = int(input("Enter the index:"))
value = input("Enter the value:")
arr.insert(index, value)
print("using insert:", arr)'''

#delete operation in array using pop method
'''a = [1,2,3,5,4]
print("before deletion:", a)
a.pop(2)
print("after deletion:", a)'''

#delete operation in array using del method
'''a = [1,2,3,5,4]
print("before deletion:", a)
del a[3]
print("after deletion:", a)'''

#delete operation in array using remove method
'''a = [1,2,3,5,4]
print("before deletion:", a)
a.remove(5)
print("after deletion:", a)'''

#delete operation in array using pop method with user input
'''n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
print("before deletion:", arr)
index = int(input("Enter the index:"))
arr.pop(index)
print("after deletion:", arr)'''

#delete operation in array using remove method with user input
'''n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
print("before deletion:", arr)
value = int(input("Enter the value:"))
arr.remove(value)
print("after deletion:", arr)'''

#update operation in array
'''a = [1,2,3,5,5,6]
print("before update:", a)
a[3] = 4
print("after update:", a)'''

#update operation in array with user input
'''n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
print("before update:", arr)
index = int(input("Enter the index:"))
value = int(input("Enter the value:"))
arr[index] = value
print("after update:", arr)'''

#sorting operations in array in descending order
'''a = [5,4,3,4,0]
print("before sorting:", a)
a.sort(reverse=True)
print("after sorting:", a)'''

#sorting operations in array in ascending order
'''a = [5,4,3,4,0]
print("before sorting:", a)
a.sort()
print("after sorting:", a)'''