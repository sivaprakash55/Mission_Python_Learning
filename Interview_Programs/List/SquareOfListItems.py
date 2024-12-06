numbers = [1, 2, 3, 4, 5, 6, 7]

print([i*i for i in numbers])


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print([i+j for i in list1 for j in list2])

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1,list2[::-1]):
    print(i,j)
