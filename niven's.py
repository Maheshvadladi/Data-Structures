n = int(input("Enter value:"))
t = n
s=0
while n!=0:
    r = n%10
    s += r
    n//=10
if t%s==0:
    print(t, "n is niven's number")
else:
    print(t, "n is not niven's number") 