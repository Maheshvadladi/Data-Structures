# write a code to print n even natural numbers
n = int(input("Enter the number: "))
i = 1
while i<=n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1