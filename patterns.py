'''n = int(input("Enter value:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == j or i+j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''n = int(input("Enter value:"))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == j or i+j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''n = int(input("Enter value:"))
for i in range(n):
    for j in range(n):
        if i == 0 or j == n-1 or i+j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''n = int(input("Enter value:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()'''

'''n = int(input("Enter number:"))
for i in range(1, n+1):
    for j in range(n, n-i,-1):
        print(j, end=" ")
    print()'''

'''n = int(input("Enter number:"))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n-i):
        print("*", end="")
    print()'''

'''n = int(input("Enter value:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''n = int(input("Enter number:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()'''

'''n = int(input("Enter number:"))
for i in range((n+1)-1, 0, -1):
    for j in range(n, i-1, -1):
        print(j, end=" ")
    print()'''

'''n = 68
for i in range((n+1)-1, 64, -1):
    for j in range(n, i-1, -1):
        print(chr(j), end=" ")
    print()'''