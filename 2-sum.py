'''#2-sum approach for target value
arr =list(map(int,input("Enter Values:").split()))
target=int(input("Enter target:"))
found = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("Pair found :",arr[i],arr[j])
            found=True
            break
    if found:
        break
if not found:
    print("No pair foumd....!")'''


#3-sum approach for target value 
'''arr =list(map(int,input("Enter Values:").split()))
target=int(input("Enter target:"))
found = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==target:
                print("Pair found :",arr[i],arr[j],arr[k])
                found=True
                break
    if found:
        break
if not found:
    print("No pair foumd....!")'''



#2-sum approach for target value [optimization], best approach time=O(n)
'''def Two_sum(arr,target):
    left=0
    right=len(arr)-1
    while left<right :
        sum =arr[left]+arr[right]
        if sum==target:
            return arr[left],arr[right]
        if sum<target:
            left+=1
        else:
            right-=1
    return None
arr =list(map(int,input("Enter Values:").split()))
target=int(input("Enter target:"))
result=Two_sum(arr,target)
if result:
    print("Pair found at ",result[0],result[1])
else:
    print("not found....!")'''

#prefix sum array
'''arr=list(map(int,input("Enter values :").split()))
prefix=[]
sum=0
for num in arr:
    sum+=num
    prefix.append(sum)
print("prifix sum array",prefix)'''

#prefix  sum math approach {prefix[i]=prefix[i-1]+arr[i]}
'''arr=list(map(int,input("Enter values :").split()))
n=len(arr)
prefix=[0]*n
prefix[0]=arr[0]
for i in range (n):
    prefix[i]=prefix[i-1]+arr[i]
print("Original array :",arr)
print("prefix Sum array :",prefix)'''