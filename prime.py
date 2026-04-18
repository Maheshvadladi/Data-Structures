#program to check if a number is prime or not using brute force method

'''num = int(input("Enter a number:"))
is_prime = True
for i in range(2,num):
    if num%i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''

#program to check if a number is prime or not using math method
num = int(input("Enter the number:"))
is_prime = True
i = 2
while i*i <= num:
    if num%i == 0:
        is_prime = False
        break
    i+=1
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")