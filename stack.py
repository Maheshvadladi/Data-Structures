'''stack = []

#push

stack.append(11)
stack.append(22)
stack.append(33)
print(stack)

#pop

stack.pop()
print(stack)
stack.pop()
print(stack)

#peek
print(stack[-1])

#size
print(len(stack))

print(len(stack)==0)'''

stack=[]
size = 2
if len(stack) < size:
    stack.append(10)
else:
    print("Stack Overflow...")
if len(stack) < size:
    stack.append(20)
else:
    print("Stack Overflow...")
if len(stack) < size:
    stack.append(30)
else:
    print("Stack Overflow...")
print(stack)