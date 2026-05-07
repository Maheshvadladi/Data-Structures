'''a = list(map(int, input("Enter the value:").split()))
greater = a[0]
if greater< a[1]:
    greater = a[1]
if greater< a[2]:
    greater = a[2]
print(greater, "it is greater")'''

'''days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
day = input("Enter the day:")
no_of_days = int(input("Enter the no of days:"))
for i in range(len(days)):
    if day == days[i]:
        if no_of_days < len(days):
            i += no_of_days
            if i > 7:
                i %= 7
                print(days[i])
            else:
                print(days[i])
        elif no_of_days > len(days):
            no_of_days %= 7
            if i > 7:
                i %= 7
                print(days[i])
            else:
                print(days[i])'''
    
'''a = [1,2,3,4]
b = [5,6,7,8]
print(a+b)'''
