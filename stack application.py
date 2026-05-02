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

'''def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
n = int(input("Enter the number:"))
count(n)'''

# application of stack of redo and undo operation
'''undo_stack = []
redo_stack = []

undo_stack.append("India")
undo_stack.append("Brazil")
undo_stack.append("China")
print("Current Stack:", undo_stack)
if len(undo_stack)>0:
    action = undo_stack.pop()
    undo_stack.append(action)
    print("Undo:", action)
print("Current Stack:", undo_stack)
if len(redo_stack)>0:
    action=redo_stack.pop()
    undo_stack.append(action)
    print("Redo:", action)
print("Redo Stack:", redo_stack)'''

# application of stack for menu driven operations

'''undo_stack = []
redo_stack = []
while True:
    print("\n1. Perform action")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice==1:
        action = input("Enter action:")
        undo_stack.append(action)
        redo_stack.clear()
        print("Action Performed", action)
    elif choice==2:
        if len(undo_stack)==0:
            print("Undo Stack is Empty !!!!")
        else:
            action = undo_stack.pop()
            redo_stack.append(action)
            print("Undo:", action)
    elif choice==3:
        if len(redo_stack) == 0:
            print("Redo Stack is Empty !!!!")
        else:
            action = redo_stack.pop()
            undo_stack.append(action)
            print("Redo:", action)
    elif choice == 4:
        print("Undo Stack:", undo_stack)
        print("Redo Stack", redo_stack)
    elif choice == 5:
        break
    else:
        print("Invalid choice .... try again")'''

# application of stack for menu driven operations using file

'''undo_stack = []
redo_stack = []
filename = "sample.txt"
try:
    with open(filename, "r") as f:
        text = f.read()
except:
    text = ""
while True:
    print("\n1. Perform action")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice==1:
        newtext = input("Enter text:")
        undo_stack.append(text)
        text += newtext
        redo_stack.clear()
        with open(filename, "w") as f:
            f.write(text)
        print("Written in file .... check sample.txt")
    elif choice==2:
        if len(undo_stack)==0:
            print("Nothing to perform !!!!")
        else:
            redo_stack.append(text)
            text = undo_stack.pop()
            with open(filename, "a") as f:
                f.write(text)
            print("Undo performes")
    elif choice==3:
        if len(redo_stack) == 0:
            print("Nothing to perform redo !!!!")
        else:
            undo_stack.append(text)
            text = redo_stack.pop()
            with open(filename, "a") as f:
                f.write(text)
            print("Redo Performed")
    elif choice == 4:
        with open(filename, "r") as f:
            print("File Content:", f.read())
    elif choice == 5:
        break
    else:
        print("Invalid choice .... try again")'''