n = int(input("Enter number:"))
t = n
s = 0
while n!=0:
    r = n%10
    f = 1
    i = 1
    while i<=r:
        f = f*i
        i = i+1
    s = s+f
    n//=10
print(s)
if t==s:
    print(t, "n in strong number")
else:
    print(t, "n is not strong number")

#Time complexity: O(n2)
#Space complexity: O(1)