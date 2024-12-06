# To find the largest element in the Array

# Using Native approach
arr = [10,2,1333,234,9999,555030]
maximum = arr[0]
for i in range(1,len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
print("Max element using antive approch is :",maximum)

#using built-in function max()
print("Max element using max() is :",max(arr))

#using sort()
arr.sort()
print("Max element using sort()",arr[-1])

#using reduce()
from functools import reduce
print("Max element using reduce() :",reduce(max,arr))

#