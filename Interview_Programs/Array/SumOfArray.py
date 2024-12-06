# To find sum of Array elements

from functools import reduce

def __sum(arr):
    sum = 0
    for i in arr:
        sum +=i
    return sum

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(f"Sum of Array elements is : {__sum(arr)}")
    print("sum is",reduce(lambda a,b:a+b,arr))