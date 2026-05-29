# program to find a target sum using 2-pointer approach
'''arr = list(map(int, input("Enter values: ").split()))
target = int(input("Enter the target: "))
left = 0
right = len(arr) - 1
while left < right:
    sum = arr[left] + arr[right]
    if sum == target:
        print("Pair found with indexes: ", left, right)
        print("Pair found: ", arr[left], arr[right])
        break
    elif sum < target:
        left += 1
    else:
        right -= 1'''

# program to find a target sum using 2-pointer approach from one-side (left)
'''arr = list(map(int, input("Enter values: ").split()))
target = int(input("Enter the target: "))
slow = 0
while slow < len(arr):
    fast = slow + 1
    while fast < len(arr):
        sum = arr[slow] + arr[fast]
        if sum == target:
            print("Pair found: ", arr[slow], arr[fast])
            print("Pair found with indexes: ", slow, fast)
        fast += 1
    slow += 1'''

