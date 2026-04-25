# example for indirect function calling
'''def three():
    print("this is inside function-3")
def two():
    print("this is inside function-2")
    three()
def one():
    print("this is inside function-1")
    two()
one()'''

def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
n = int(input("Enter the number:"))
count(n)