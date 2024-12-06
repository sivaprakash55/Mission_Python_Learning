list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

for i in range(len(list1)):
    print(f"Index is {i} and element is {list1[i]}")

list1[2][2].append(7000)
print(list1[2][2][0],list1[2][2][1],list1[2][2][2])

list2 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
print(list2)
#for i in range(len(list2)):
    #print(f"Index is {i} and element is {list2[i]}")

list2[2][1][2].append(["h","k"])
print(list2)