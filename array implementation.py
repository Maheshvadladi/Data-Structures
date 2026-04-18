'''Array Implementation
1. Secoond largest
2. rotation of array with key
3. traverse / reverse
4. move all zeros at end'''

#rotate to the right by 1 an array
'''arr = list(map(int, input("Enter the array:").split()))
last = arr[-1]
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = last
print("Rotated array:", arr)'''

#move all zeros to the end of array
'''arr = list(map(int, input("Enter the array:").split()))
zero = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[zero], arr[i] = arr[i], arr[zero]
        zero += 1
print("After moving zeros:", arr)'''

#reverse sorted or unsorted array
'''arr = list(map(int, input("Enter the array:").split()))
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -=1
print("Reverse array:",arr)'''

#subarray sum
'''arr = list(map(int, input("Enter the array:").split()))
max_sum = arr[0]
current_sum = arr[0]
for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum+arr[i])
    max_sum = max(max_sum, current_sum)
print("Max Subarray Sum:", max_sum)'''
