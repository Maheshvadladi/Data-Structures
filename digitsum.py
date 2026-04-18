# write a code to add the sum of digits of a given number
'''n = int(input("Enter the number:"))
s = 0
while n!=0:
    r = n % 10
    s += r
    n = n // 10
print("sum:", s)'''

# with using list
'''n = int(input("Enter the number:"))
l = []
while n!=0:
    r = n % 10
    l.append(r)
    n = n // 10
print("Sum:", sum(l))'''