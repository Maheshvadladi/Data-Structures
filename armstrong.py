#using list method
'''n = int(input("Enter value:"))
s = []
while n!=0:
    r = n % 10
    s.append(r*r*r)
    n = n//10
t = sum(s)
if t==n:
    print("n is armstrong number")
else:
    print("n is not armstrong number")'''

#normal method
'''n = int(input("Enter value:"))
t = n
s = 0
while n != 0:
    r = n % 10
    s += r*r*r
    n //= 10
if t==s:
    print(t, "n is armstrong number")
else:
    print(t, "n is not armstrong number")'''