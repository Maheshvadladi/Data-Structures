# write a code to reverse a given number
# navie approach
'''n = int(input("enter number:"))
while n!=0:
    r = n % 10
    print(r, end="")
    n = n // 10'''

# math approach
'''n = int(input("Enter the number:"))
rev = 0
while n!=0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
print("reverse:", rev)'''