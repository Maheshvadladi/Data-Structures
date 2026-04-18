#Hashing
'''item -> key + value

key      value
vijay    6.2, 98
aditya   5.8, 90'''

'''1 1 2 2 3 4 4 5 6 6 6 6
1 = 2
2 = 2
3 = 1
4 = 2
5 = 1
6 = 4'''

#frequency of all occurances
'''arr = list(map(int, input("Enter the elements of the array:").split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key in freq:
    print(key, ":", freq[key], "times.")
print("frequency :", freq)'''