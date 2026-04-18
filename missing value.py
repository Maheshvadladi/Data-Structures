#Finding the missing value in array
arr = list(map(int, input("Enter the elements of the array:").split()))
n = int(input("Enter the total number of elements:"))
e_sum = n*(n+1)//2
o_sum = sum(arr)
missing_value = e_sum - o_sum
print("The missing value is:", missing_value)